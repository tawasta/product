from odoo import fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"

    show_materials_with_report = fields.Boolean(string="Show materials with reports")
