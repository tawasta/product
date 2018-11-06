# -*- coding: utf-8 -*-
from odoo import models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    # Allow calling get_analytic_tags from product template
    def get_analytic_tags(self):
        return self.product_tmpl_id.get_analytic_tags()
