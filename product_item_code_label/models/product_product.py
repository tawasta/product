from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    item_code = fields.Char(string='Item Code')
