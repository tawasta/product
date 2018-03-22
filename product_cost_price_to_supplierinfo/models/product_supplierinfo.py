# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductSupplierinfo(models.Model):

    _inherit = 'product.supplierinfo'

    from_cost_price = fields.Boolean(
        string='Created from cost price',
        default=False
    )
