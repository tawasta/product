import logging
from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Query, Request
from pydantic import BaseModel

from odoo.api import Environment
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

from odoo.addons.fastapi_auth_api_key.dependencies import (
    authenticated_env_by_auth_api_key,
)
from odoo.addons.fastapi_rest_log.services.rest_logger import log_fastapi_call

router = APIRouter(dependencies=[Depends(authenticated_env_by_auth_api_key)])
_logger = logging.getLogger(__name__)


def parse_date(val: str) -> datetime:
    return datetime.strptime(val, DEFAULT_SERVER_DATE_FORMAT)


def _get_client_ip(request: Request) -> str:
    xff = request.headers.get("x-forwarded-for", "")
    if xff:
        return xff.split(",")[0].strip()
    return request.client.host if request.client else ""


class ReportResponse(BaseModel):
    count: int
    rows: list[dict]
    secondary_on_hand: float
    secondary_rows: list[dict]


def _is_secondary(product) -> bool:
    cat = product.categ_id
    if not cat:
        return False
    return bool(cat.is_secondary or (cat.parent_id and cat.parent_id.is_secondary))


@router.get("/product/report", response_model=ReportResponse)
async def product_report_min(
    request: Request,
    env: Annotated[Environment, Depends(authenticated_env_by_auth_api_key)],
    limit: int = Query(500, ge=1, le=5000),
    offset: int = Query(0, ge=0),
    category: Optional[int] = Query(  # noqa UP007
        None,
        description="Rajaa tuoteryhmään (id). Sisältää myös alikategoriat.",
    ),
):
    """
    Palauttaa product.product -rivit (domain: vapaaehtoinen category):
    {id, name, default_code, tags:[{id,name}],
    standard_price, qty_available, is_secondary}

    Lisäksi:
      - secondary_on_hand: summa VAIN tästä products-joukosta (limit/offset)
      - niille, joilla is_secondary
      - secondary_rows: lista näistä sekundatuotteista
      - (nimi + qty, mukana myös id & default_code)
    """
    client_ip = _get_client_ip(request)

    Product = env["product.product"].with_context(active_test=False)

    domain = []
    if category is not None:
        domain.append(("categ_id", "child_of", category))

    total = Product.search_count(domain)
    products = Product.search(domain, limit=limit, offset=offset, order="id asc")

    secondary_total = 0.0
    secondary_rows = []
    rows = []

    for p in products:
        is_sec = _is_secondary(p)
        qty = float(p.qty_available or 0.0)

        if is_sec:
            secondary_total += qty
            secondary_rows.append(
                {
                    "id": p.id,
                    "name": p.display_name or p.name or "",
                    "default_code": p.default_code or "",
                    "category": p.categ_id.name or "",
                    "qty_available": qty,
                }
            )

        rows.append(
            {
                "id": p.id,
                "name": p.display_name or p.name or "",
                "default_code": p.default_code or "",
                "category": p.categ_id.name or "",
                "tags": [
                    {"id": t.id, "name": t.name}
                    for t in getattr(p, "sh_product_tag_ids", [])
                ]
                or [{"id": 0, "name": ""}],
                "standard_price": p.standard_price or 0.0,
                "qty_available": qty,
                "is_secondary": is_sec,
            }
        )

    result = {
        "count": total,
        "rows": rows,
        "secondary_on_hand": secondary_total,
        "secondary_rows": secondary_rows,
    }

    log_fastapi_call(
        env,
        method="GET",
        path="/product_rest_api/product/report",
        payload={
            "limit": limit,
            "offset": offset,
            "category": category,
        },
        response=result,
        status_code=200,
        ip_address=client_ip,
    )

    return result
