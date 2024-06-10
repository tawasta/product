from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    xyz_classification_id = fields.Many2one(
        "xyz.classification",
        related="product_tmpl_id.xyz_classification_id",
        readonly=True,
        store=True,
    )
