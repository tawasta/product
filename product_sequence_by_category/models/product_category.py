# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductCategory(models.Model):

    _inherit = 'product.category'

    sequence_id = fields.Many2one(
        comodel_name='ir.sequence',
        string='Product sequence',
        required=True,
        help='A sequence that is used when '
        'creating new products to this category',
        default=lambda self: self.env.ref('product_sequence.seq_product_auto'),
    )
