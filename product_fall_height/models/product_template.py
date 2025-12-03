from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    fall_height = fields.Float(
        related="product_variant_ids.fall_height",
        readonly=False,
        help="The greatest height the person using this product can fall from",
    )
