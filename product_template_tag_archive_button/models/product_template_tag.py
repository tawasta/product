# -*- coding: utf-8 -*-


from odoo import fields, models


class ProductTemplateTag(models.Model):

    _inherit = 'product.template.tag'

    active = fields.Boolean(default=True)
