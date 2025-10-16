from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _compute_pricelist_price(self):
        pricelist_item_obj = self.env["product.pricelist.item"]
        for rec in self:
            final_price = rec.list_price
            pricelist_item = pricelist_item_obj.search(
                [("product_tmpl_id", "=", rec.id)], limit=1
            )
            if pricelist_item:
                final_price = pricelist_item.fixed_price
            rec.pricelist_price = final_price

    pricelist_price = fields.Float(compute="_compute_pricelist_price")
