from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    gross_weight = fields.Float(string="Gross weight")

    # Remove this field in the next version
    gross_weight_product = fields.Float(string="Gross Weight (TO BE UPDATED)")
