from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    list_price = fields.Float(groups="sales_team.group_sale_salesman")
