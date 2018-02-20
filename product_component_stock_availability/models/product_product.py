# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductProduct(models.Model):
    
    # 1. Private attributes
    _inherit = 'product.product'

    # 2. Fields declaration
    component_bom_id = fields.Many2one(
        comodel_name='mrp.bom',
        compute='_get_bom_component_ids',
        readonly=True,
    )

    bom_component_ids = fields.Many2many(
        comodel_name='product.product',
        relation='product_component_rel', 
        column1='parent_id',
        column2='child_id',
        compute='_get_bom_component_ids',        
        string='Component Availability',
        readonly=True,
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def _get_bom_component_ids(self):

        bom_model = self.env['mrp.bom']
        for product in self:            
            # Get the primary BOM for the variant
            product_bom_id = bom_model._bom_find(
                product_id=product.id, 
                product_tmpl_id=product.product_tmpl_id.id
            )
            # If BOM exists, find all its top-level lines' products
            if product_bom_id:
                product_bom = bom_model.browse(product_bom_id)
                product.bom_component_ids \
                    = [line.product_id.id for line in product_bom.bom_line_ids]

                # Also show which BOM was used for calculation
                product.component_bom_id = product_bom_id
            else:
                product.bom_component_ids = False
                product.component_bom_id = False


    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
