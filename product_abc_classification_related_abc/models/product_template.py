from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    abc_classification_profile_id = fields.Many2one(
        compute=None,
        inverse=None,
    )
    abc_classification_level_id = fields.Many2one(
        compute=None,
        inverse=None,
    )
