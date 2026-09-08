from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    def _shop_lookup_products(self, options, post, search, website):
        # Kutsu alkuperäistä funktiota
        (
            fuzzy_search_term,
            product_count,
            search_product,
        ) = super()._shop_lookup_products(options, post, search, website)

        # Lisää tuotteiden suodatus
        hidden_products = search_product.filtered("show_only_in_suggested_accessories")
        if hidden_products:
            search_product -= hidden_products
            product_count -= len(hidden_products)

        return fuzzy_search_term, product_count, search_product
