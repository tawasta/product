from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    material_info = fields.Text(string="Material information")
