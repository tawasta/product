# -*- coding: utf-8 -*-
from openerp import models, fields


class ProductProduct(models.Model):

    _inherit = 'product.product'

    internal_comments = fields.Text('Internal Comments')
