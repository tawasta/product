from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    revision_code = fields.Char(copy=False, store=True)
    revision_note = fields.Text(copy=False, store=True)
    revision_date = fields.Date(copy=False, store=True)
