from odoo import models, fields

class product_template(models.Model):

    _inherit = "product.template"

    website_synopsis = fields.Char(string="Synopsis for Website")
