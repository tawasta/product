from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    revision_code = fields.Char(copy=False)
    revision_note = fields.Text(copy=False)
    revision_date = fields.Date(copy=False)
