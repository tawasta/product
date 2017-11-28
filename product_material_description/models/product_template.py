# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    material = fields.Char('Material Description')