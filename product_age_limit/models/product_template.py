from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    age_limit = fields.Integer(
        related="product_variant_ids.age_limit",
        readonly=False,
        help="Lowest age for persons using the product",
    )
