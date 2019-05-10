# -*- coding: utf-8 -*-

from odoo import api, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        if 'default_code' not in vals or vals['default_code'] == '/':
            if vals.get('product_tmpl_id'):
                # Get the sequence by category
                product_tmpl = self.env['product.template'].browse(
                    vals['product_tmpl_id']
                )
                vals['default_code'] = \
                    product_tmpl.categ_id.sequence_id.next_by_id()

        return super(ProductProduct, self).create(vals)

    @api.multi
    def write(self, vals):
        for product in self:
            if product.default_code in [False, '/'] and product.product_tmpl_id:
                vals['default_code'] = \
                    product.product_tmpl_id.categ_id.next_by_id()
            super(ProductProduct, product).write(vals)
        return super(ProductProduct, self).write(vals)
