from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    gross_weight = fields.Float(string="Gross weight")
