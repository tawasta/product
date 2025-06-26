from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    name = fields.Char(index=True, required=True, translate=False)
