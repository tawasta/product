from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    external_code = fields.Char(
        help="External code for the product category",
        copy=False,
        store=True,
    )
