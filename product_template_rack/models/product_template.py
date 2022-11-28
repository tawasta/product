from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    loc_rack = fields.Char(string="Rack")
