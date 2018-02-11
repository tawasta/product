# -*- coding: utf-8 -*-
from odoo import models, api


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.model
    def default_get(self, fields):
        res = super(ResPartner, self).default_get(fields)
        select_type = self.env.context.get('select_type', False)
        if select_type:
            res.update({
                'customer': select_type == 'customer',
                'supplier': select_type == 'supplier',
            })
        return res
