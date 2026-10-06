from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Helper to show an info alert on the sale order form
    has_lines_excluded_from_sale_invoice = fields.Boolean(
        compute="_compute_has_lines_excluded_from_sale_invoice",
    )

    @api.depends("order_line.exclude_from_sale_invoice")
    def _compute_has_lines_excluded_from_sale_invoice(self):
        for order in self:
            order.has_lines_excluded_from_sale_invoice = any(
                order.order_line.mapped("exclude_from_sale_invoice")
            )
