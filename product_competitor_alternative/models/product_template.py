# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    competitor_alternative = fields.Char(
        string="Competitor's Alternative",
        help='Info about a similar product sold by a competitor'
    )
