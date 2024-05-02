from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    xyz_classification_id = fields.Many2one(
        "xyz.classification",
        string="XYZ classification",
    )
