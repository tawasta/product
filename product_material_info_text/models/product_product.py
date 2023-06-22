from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    material_info = fields.Text(string="Material information")
