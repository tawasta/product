from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_filtered_sellers(
        self, partner_id=False, quantity=0.0, date=None, uom_id=False, params=False
    ):
        """Overrides the original function to ignore quantity criterium"""
        self.ensure_one()
        if date is None:
            date = fields.Date.context_today(self)

        sellers_filtered = self._prepare_sellers(params)
        sellers = self.env["product.supplierinfo"]
        for seller in sellers_filtered:
            # Set quantity in UoM of seller
            quantity_uom_seller = quantity
            if quantity_uom_seller and uom_id and uom_id != seller.product_uom:
                quantity_uom_seller = uom_id._compute_quantity(
                    quantity_uom_seller, seller.product_uom
                )

            if seller.date_start and seller.date_start > date:
                continue
            if seller.date_end and seller.date_end < date:
                continue
            if partner_id and seller.partner_id not in [
                partner_id,
                partner_id.parent_id,
            ]:
                continue
            if seller.product_id and seller.product_id != self:
                continue
            sellers |= seller
        return sellers
