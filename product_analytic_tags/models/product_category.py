# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductCategory(models.Model):

    _inherit = 'product.category'

    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag',
        string='Analytic tags',
    )

    def get_analytic_tags(self):
        # The return won't work with multiple records
        self.ensure_one()

        # Own analytic tags are the priority
        analytic_tags = self.analytic_tag_ids

        if not analytic_tags and self.parent_id:
            # No analytic tags, check the parent
            # This will work recursively upwards
            analytic_tags = self.parent_id.get_analytic_tags()

        return analytic_tags
