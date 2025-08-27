import logging
from datetime import datetime
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel

from odoo import fields
from odoo.api import Environment
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

from odoo.addons.fastapi.dependencies import odoo_env

router = APIRouter()
_logger = logging.getLogger(__name__)


def parse_date(val: str) -> datetime:
    return datetime.strptime(val, DEFAULT_SERVER_DATE_FORMAT)


class ReportResponse(BaseModel):
    count: int
    rows: list[dict]
    secondary_on_hand: float


def _is_secondary(product) -> bool:
    name_l = (product.display_name or product.name or "").lower()
    categ_l = (product.categ_id.complete_name or product.categ_id.name or "").lower()
    return ("ii-laatu" in name_l) or ("sekundat" in categ_l)


@router.get("/product/report", response_model=ReportResponse)
async def product_report_min(
    env: Annotated[Environment, Depends(odoo_env)],
    limit: int = Query(500, ge=1, le=5000),
    offset: int = Query(0, ge=0),
):
    """
    Kaikki product.product -rivit (ei domain-suodatuksia):
    {id, name, default_code, tags:[{id,name}], standard_price, qty_available, is_secondary}
    Lisäksi: secondary_on_hand = sekundatuotteiden tämänhetkinen varastosumma.
    """
    _logger.info("Generating product report (ALL products) + secondary_on_hand")

    Product = env["product.product"].sudo().with_context(active_test=False)
    total = Product.search_count([])
    products = Product.search([], limit=limit, offset=offset, order="id asc")

    secondary_total = 0.0
    rows = []
    for p in products:
        is_sec = _is_secondary(p)
        qty = float(p.qty_available or 0.0)
        if is_sec:
            secondary_total += qty

        rows.append(
            {
                "id": p.id,
                "name": p.display_name or p.name or "",
                "default_code": p.default_code or "",
                "tags": [{"id": t.id, "name": t.name} for t in p.sh_product_tag_ids] or [{"id": 0, "name": ""}],
                "standard_price": p.standard_price or 0.0,
                "qty_available": qty,
                "is_secondary": is_sec,
            }
        )

    _logger.info(
        "Product report generated: %d rows (total=%d). secondary_on_hand=%.2f",
        len(rows), total, secondary_total
    )
    return {"count": total, "rows": rows, "secondary_on_hand": secondary_total}


