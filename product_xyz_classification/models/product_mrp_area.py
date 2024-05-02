from odoo import fields, models


class ProductMrpArea(models.Model):

    _inherit = "product.mrp.area"

    xyz_classification_id = fields.Many2one(
        "xyz.classification", related="product_id.xyz_classification_id"
    )
