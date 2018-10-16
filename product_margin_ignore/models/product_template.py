# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    margin_ignore = fields.Boolean(
        string=_('Ignore in margin'),
        help=_('Ignore this product when computing margins'),
        default=False,
    )
