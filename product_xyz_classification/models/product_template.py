from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    xyz_classification_id = fields.Many2one(
        "xyz.classification", related="product_variant_id.xyz_classification_id"
    )
