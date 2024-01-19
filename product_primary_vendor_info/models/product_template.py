from odoo import api, fields, models

from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):

    _inherit = "product.template"

    @api.depends("seller_ids")
    def _compute_primary_supplierinfo(self):
        for p in self:
            p.primary_supplierinfo_id = p.seller_ids and p.seller_ids[0].id or False

    def _compute_standard_price_from_vendor(self):
        for p in self:
            if not p.primary_supplierinfo_id:
                p.standard_price_from_vendor = 0.00
            else:
                unit_cost_in_eur = p.primary_supplierinfo_id.currency_id._convert(
                    p.primary_supplierinfo_id.price, p.currency_id
                )

                p.standard_price_from_vendor = p.uom_po_id._compute_price(
                    unit_cost_in_eur, p.uom_id
                )

    standard_price_from_vendor = fields.Float(
        compute=_compute_standard_price_from_vendor,
        digits=dp.get_precision("Product Price"),
        string="Cost Price (Vendor-based)",
        store=False,
        help="Alternative cost price calculated based on primary vendor "
        "information. Note that this does not affect stock valuation "
        "and is purely informational.",
    )

    primary_supplierinfo_id = fields.Many2one(
        compute=lambda self: self._compute_primary_supplierinfo(),
        comodel_name="product.supplierinfo",
        string="Primary Vendor Info",
        store=True,
    )

    primary_vendor_id = fields.Many2one(
        comodel_name="res.partner",
        related="primary_supplierinfo_id.partner_id",
        string="Primary Vendor",
        store=True,
    )

    primary_vendor_code = fields.Char(
        related="primary_supplierinfo_id.product_code",
        string="Primary Vendor's Code",
        store=True,
    )

    primary_vendor_price = fields.Float(
        related="primary_supplierinfo_id.price",
        digits=dp.get_precision("Product Price"),
        string="Primary Vendor's Price",
        store=True,
    )

    primary_vendor_currency_id = fields.Many2one(
        comodel_name="res.currency",
        related="primary_supplierinfo_id.currency_id",
        string="Primary Vendor's Currency",
        store=True,
    )
