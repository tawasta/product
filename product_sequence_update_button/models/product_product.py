# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductProduct(models.Model):

    _inherit = 'product.product'

    @api.one
    def update_product_reference_from_sequence(self):
        self.default_code = self.env['ir.sequence'].get('product.product')