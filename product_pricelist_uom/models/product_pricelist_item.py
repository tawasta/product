# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo import:
from odoo import models, fields

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductPricelistItem(models.Model):
    
    # 1. Private attributes
    _inherit = 'product.pricelist.item'

    # 2. Fields declaration
    unit_of_measure = fields.Char(
        string='Unit of measure',
        compute='_compute_unit_of_measure',
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def _compute_unit_of_measure(self):
        for record in self:
            product_id = record.product_tmpl_id or record.product_id

            if product_id:
                record.unit_of_measure = product_id.uom_id.name

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
