# -*- coding: utf-8 -*-


from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    drawing_number = fields.Char(string='Drawing number')
