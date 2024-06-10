from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    xyz_classification_id = fields.Many2one(
        "xyz.classification",
        string="XYZ classification",
        store=True,
        copy=False,
    )
