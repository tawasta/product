from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    diameter = fields.Float(related="product_variant_ids.diameter", readonly=False)
