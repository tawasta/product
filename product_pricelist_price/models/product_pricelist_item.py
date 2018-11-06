# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo import:
from odoo import models, fields
import odoo.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductPricelistItem(models.Model):

    # 1. Private attributes
    _inherit = 'product.pricelist.item'

    # 2. Fields declaration
    list_price = fields.Char(
        string='Default price',
        compute='_compute_origin_prices',
        digits=dp.get_precision('Product Price'),
    )

    standard_price = fields.Char(
        string='Cost',
        compute='_compute_origin_prices',
        digits=dp.get_precision('Product Price'),
    )

    # 3. Default methods

    # 4. Compute and search fields
    def _compute_origin_prices(self):
        for record in self:
            product_id = record.product_tmpl_id or record.product_id

            if product_id:
                record.list_price = product_id.list_price
                record.standard_price = product_id.standard_price

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
