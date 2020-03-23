from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    cn8_code = fields.Char(string="CN8 code")
