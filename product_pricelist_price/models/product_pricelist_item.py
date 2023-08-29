from odoo import fields, models

import odoo.addons.decimal_precision as dp


class ProductPricelistItem(models.Model):

    _inherit = "product.pricelist.item"

    list_price = fields.Char(
        string="Default price",
        compute="_compute_origin_prices",
        digits=dp.get_precision("Product Price"),
    )

    standard_price = fields.Char(
        string="Cost",
        compute="_compute_origin_prices",
        digits=dp.get_precision("Product Price"),
    )

    def _compute_origin_prices(self):
        for record in self:
            product_id = record.product_tmpl_id or record.product_id

            if product_id:
                record.list_price = product_id.list_price
                record.standard_price = product_id.standard_price
