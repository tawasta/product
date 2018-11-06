# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag',
        string='Analytic tags',
    )

    def get_analytic_tags(self):
        # The return won't work with multiple records
        self.ensure_one()

        analytic_tags = self.analytic_tag_ids \
            or self.categ_id.get_analytic_tags()

        return analytic_tags
