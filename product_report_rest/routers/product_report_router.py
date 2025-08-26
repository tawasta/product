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


@router.get("/product/report", response_model=ReportResponse)
async def product_report_min(
    env: Annotated[Environment, Depends(odoo_env)],
    limit: int = Query(500, ge=1, le=5000),
    offset: int = Query(0, ge=0),
):
    """
    Minimiversio: PALAUTTAA KAIKKI product.product -rivit muotoa {id, name}.
    Ei domain-suodatuksia.
    """
    _logger.info("Generating minimal product report (ALL products, no domain filters)")

    Product = env["product.product"].sudo().with_context(active_test=False)
    total = Product.search_count([])
    products = Product.search([], limit=limit, offset=offset, order="id asc")

    rows = [{"id": p.id, "name": (p.display_name or p.name or "")} for p in products]

    _logger.info("Minimal product report generated: %d rows (total=%d)", len(rows), total)
    return {"count": total, "rows": rows}

