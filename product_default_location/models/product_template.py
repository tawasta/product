from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    product_default_location = fields.Many2one(
        'stock.location',
        string='Default Location',
    )
