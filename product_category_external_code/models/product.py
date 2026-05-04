from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    external_code = fields.Char(
        string="External Code",
        related="categ_id.external_code",
        store=True,
        readonly=True,
        copy=False,
    )
