from odoo import fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    show_materials_with_report = fields.Boolean(
        string="Show Materials on Prints",
        help="Show the products' materials when printing this order's invoice or delivery slip",
    )
