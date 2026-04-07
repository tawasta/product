import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends(
        "qty_invoiced",
        "qty_delivered",
        "product_uom_qty",
        "state",
    )
    def _compute_qty_to_invoice(self):
        """Force qty_to_invoice = 0 for excluded products."""
        res = super()._compute_qty_to_invoice()
        for line in self:
            if line.product_id.exclude_from_sale_invoice:
                line.qty_to_invoice = 0
        return res

    @api.depends(
        "state", "product_uom_qty", "qty_delivered", "qty_to_invoice", "qty_invoiced"
    )
    def _compute_invoice_status(self):
        """Mark excluded-product lines as 'no' (nothing to invoice)"""
        res = super()._compute_invoice_status()
        for line in self:
            if line.product_id.exclude_from_sale_invoice:
                line.invoice_status = "no"

        return res
