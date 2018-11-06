# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductProduct(models.Model):

    # 1. Private attributes
    _inherit = 'product.product'

    # 2. Fields declaration

    # 3. Default methods
    @api.multi
    def name_get(self):
        old_res = super(ProductProduct, self).name_get()
        # This is not optimal, but allows us to not override the whole method

        new_res = list()
        for record in old_res:
            product = self.browse(record[0])
            product_name = '%s / %s' % (record[1], product.uom_id.name)

            new_res.append((record[0], product_name))

        return new_res

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
