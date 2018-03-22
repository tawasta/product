# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StockPackOperation(models.Model):

    _inherit = 'stock.pack.operation'

    @api.multi
    def _compute_customer_product_info(self):
        for pack_operation in self:
            for partner_info in pack_operation.product_id.customer_ids:
                if partner_info.name == pack_operation.picking_id.partner_id:
                    pack_operation.customer_product_code \
                        = partner_info.product_code
                    pack_operation.customer_product_name \
                        = partner_info.product_name

    customer_product_code = fields.Char(
        compute='_compute_customer_product_info',
        string='Customer Product Code'
    )

    customer_product_name = fields.Char(
        compute='_compute_customer_product_info',
        string='Customer Product Name'
    )
