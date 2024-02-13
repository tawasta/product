from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    abc_classification_profile_id = fields.Many2one(
        related="product_tmpl_id.abc_classification_profile_id",
        readonly=True,
    )

    abc_classification_level_id = fields.Many2one(
        related="product_tmpl_id.abc_classification_level_id",
        readonly=True,
    )
