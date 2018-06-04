# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplateTag(models.Model):

    _inherit = 'product.template.tag'

    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag',
        string='Analytic tags',
    )
