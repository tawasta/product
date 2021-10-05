from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    def _get_search_domain(self, search, category, attrib_values):
        res = super(WebsiteSale, self)._get_search_domain(search, category, attrib_values)
        res += [('show_only_in_suggested_accessories', '=', False)]
        return res
