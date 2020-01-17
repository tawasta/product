from odoo import api, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    @api.multi
    def price_rule_get(self, prod_id, qty, partner=None):
        """Pass context if the type of the pricelist is sale for restricting
        on the search product.supplierinfo records of type customer."""
        obj = (
            self.with_context(supplierinfo_type="customer")
            if self.type == "sale"
            else self
        )
        return super(ProductPricelist, obj).price_rule_get(
            prod_id, qty, partner=partner
        )
