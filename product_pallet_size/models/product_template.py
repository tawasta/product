# -*- coding: utf-8 -*-
from odoo import fields, models, api
import odoo.addons.decimal_precision as dp


class ProductTemplate(models.Model):

    # 1. Private attributes
    _inherit = 'product.template'

    # 2. Fields declaration
    pallet_size = fields.Integer(
        string="Pallet size",
        help="How many products Unit of Measures fit on a pallet",
    )
    pallet_weight = fields.Float(
        string='Pallet weight',
        compute='_compute_pallet_weight',
        digits=dp.get_precision('Stock Weight'),
        store=True,
        help='The weight of pallet contents in Kg, '
             'not including pallet weight or any packaging, etc.')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends('weight', 'pallet_size')
    def _compute_pallet_weight(self):
        for record in self:
            record.pallet_weight = record.weight * record.pallet_size

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
