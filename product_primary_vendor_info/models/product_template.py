# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.depends('seller_ids')
    def _compute_primary_supplierinfo(self):
        for p in self:
            p.primary_supplierinfo_id \
                = p.seller_ids and p.seller_ids[0].id or False

    primary_supplierinfo_id = fields.Many2one(
        compute=_compute_primary_supplierinfo,
        comodel_name='product.supplierinfo',
        string='Primary Vendor Info',
        store=True,
    )

    primary_vendor_id = fields.Many2one(
        comodel_name='res.partner',
        related='primary_supplierinfo_id.name',
        string="Primary Vendor",
        store=True
    )

    primary_vendor_code = fields.Char(
        related='primary_supplierinfo_id.product_code',
        string="Primary Vendor's Code",
        store=True
    )

    primary_vendor_price = fields.Float(
        related='primary_supplierinfo_id.price',
        digits=dp.get_precision('Product Price'),
        string="Primary Vendor's Price",
        store=True
    )

    primary_vendor_currency_id = fields.Many2one(
        comodel_name='res.currency',
        related='primary_supplierinfo_id.currency_id',
        string="Primary Vendor's Currency",
        store=True
    )
