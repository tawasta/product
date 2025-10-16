from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _compute_vrnt_pricelist_price(self):
        pricelist_item_obj = self.env["product.pricelist.item"]
        for rec in self:
            final_price = rec.lst_price
            pricelist_item = pricelist_item_obj.search(
                [("product_id", "=", rec.id)], limit=1
            )
            if pricelist_item:
                final_price = pricelist_item.fixed_price
            rec.pricelist_price = final_price

    pricelist_price = fields.Float(compute="_compute_vrnt_pricelist_price")
