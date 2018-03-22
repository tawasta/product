# -*- coding: utf-8 -*-
from odoo import models, api


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.multi
    def update_product_reference_from_sequence(self):
        self.ensure_one()
        self.default_code = self.env['ir.sequence'].get('product.product')
