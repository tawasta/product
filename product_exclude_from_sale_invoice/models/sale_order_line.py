import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    exclude_from_sale_invoice = fields.Boolean(
        compute="_compute_exclude_from_sale_invoice",
        store=True,
    )

    @api.depends("product_id")
    def _compute_exclude_from_sale_invoice(self):
        # Snapshot of the product's exclusion when the SO line is created or the
        # line's product changes.
        for line in self:
            line.exclude_from_sale_invoice = line.product_id.exclude_from_sale_invoice

    # Core dependencies are inherited from the parent method; only list the extras.
    @api.depends("exclude_from_sale_invoice")
    def _compute_qty_to_invoice(self):
        """Force qty_to_invoice = 0 for excluded lines."""
        res = super()._compute_qty_to_invoice()
        for line in self:
            if line.exclude_from_sale_invoice:
                line.qty_to_invoice = 0
        return res

    @api.depends("exclude_from_sale_invoice")
    def _compute_invoice_status(self):
        """Mark excluded lines as 'no' (nothing to invoice)"""
        res = super()._compute_invoice_status()
        for line in self:
            if line.exclude_from_sale_invoice:
                line.invoice_status = "no"

        return res
