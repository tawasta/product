# 1. Standard library imports:
import json
import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

# 2. Known third party imports:
# 3. Odoo imports (openerp):


class CheckProduct(http.Controller):

    @http.route(
        ["/check/product/<int:product_id>"],
        type="http",
        auth="public",
        website=True,
        csrf=False,
    )
    def get_product(self, product_id=None, **post):
        product = (
            request.env["product.product"].sudo().search([("id", "=", product_id)])
        )

        values = {
            'order_status': product.can_not_order
        }

        return json.dumps(values)
