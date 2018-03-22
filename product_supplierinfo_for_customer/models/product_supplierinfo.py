# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductSupplierinfo(models.Model):
    _inherit = 'product.supplierinfo'

    type = fields.Selection(
        selection=[('customer', 'Customer'),
                   ('supplier', 'Supplier')], string='Type',
        default='supplier')

    @api.multi
    @api.onchange('type')
    def onchange_type(self):
        if self.type == 'supplier':
            return {'domain': {'name': [('supplier', '=', True)]}}
        elif self.type == 'customer':
            return {'domain': {'name': [('customer', '=', True)]}}
        return {'domain': {'name': []}}

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if not any(arg[0] == 'type' for arg in args):
            args += [('type', '=',
                      self._context.get('supplierinfo_type', 'supplier'))]
        return super(ProductSupplierinfo, self) \
            .search(args, offset=offset, limit=limit, order=order, count=count)
