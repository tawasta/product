from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    revision_code = fields.Char(copy=False, store=True)
