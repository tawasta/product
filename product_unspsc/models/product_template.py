from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    unspsc_code = fields.Char(string="UNSPSC Code", size=10)
