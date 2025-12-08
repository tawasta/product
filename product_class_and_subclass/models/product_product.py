from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    product_class = fields.Char(
        related="product_tmpl_id.product_class",
        readonly=True,
        store=True,
    )

    product_subclass = fields.Char(
        related="product_tmpl_id.product_subclass",
        readonly=True,
        store=True,
    )
