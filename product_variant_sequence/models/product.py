from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"
    _order = "sequence_variant, default_code, name, id"

    sequence_variant = fields.Integer(
        "Sequence Variant",
        default=1,
        help="Gives the sequence order when displaying a product variant list",
    )
