# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo import:
from odoo import api, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('property_product_pricelist')
    def onchange_pricelist_update_children(self):
        for record in self:
            pricelist = record.property_product_pricelist

            if pricelist:
                for child in record.child_ids:
                    child.property_product_pricelist = pricelist

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        # Inherit pricelist from parent
        if 'property_product_pricelist' not in vals and 'parent_id' in vals:
            parent_id = self.browse([vals['parent_id']])
            vals['property_product_pricelist'] = \
                parent_id.property_product_pricelist.id

        res = super(ResPartner, self).create(vals)

        return res

    @api.multi
    def write(self, vals):
        res = super(ResPartner, self).write(vals)

        pricelist = vals.get('property_product_pricelist', False)
        if pricelist:
            for record in self:
                for child in record.child_ids:
                    child.property_product_pricelist = pricelist

        return res

    # 7. Action methods

    # 8. Business methods
