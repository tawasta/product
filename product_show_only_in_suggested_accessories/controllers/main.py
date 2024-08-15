from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route


class WebsiteSale(WebsiteSale):
    def _shop_lookup_products(self, attrib_set, options, post, search, website):
        # Kutsu alkuperäistä funktiota
        fuzzy_search_term, product_count, search_product = super(
            WebsiteSale, self
        )._shop_lookup_products(attrib_set, options, post, search, website)

        # Lisää tuotteiden suodatus
        search_product = search_product.filtered(
            lambda p: p.show_only_in_suggested_accessories is False
        )

        return fuzzy_search_term, product_count, search_product
