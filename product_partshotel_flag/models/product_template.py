# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):

    # 1. Private attributes
    _inherit = 'product.template'

    # 2. Fields declaration
    export_to_partshotel = fields.Boolean(
        string='Export to Partshotel'
    )
