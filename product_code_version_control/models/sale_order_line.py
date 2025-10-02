from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    version_code_info = fields.Text(
        string="Searched code",
        copy=False,
    )
