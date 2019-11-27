from odoo import models, fields


class ProductTemplate(models.Model):

    _inherit = "product.template"

    website_synopsis = fields.Char(string="Synopsis for Website")
