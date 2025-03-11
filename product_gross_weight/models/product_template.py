from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    gross_weight = fields.Float(string="Gross weight")
