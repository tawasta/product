# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class PurchaseOrder(models.Model):
    
    # 1. Private attributes
    _inherit = 'purchase.order'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def action_picking_create(self):
        # When an incoming picking is created from a PO, create the quality checklist
        res = super(PurchaseOrder, self).action_picking_create()
        self.env['stock.picking'].browse(res).initialize_quality_checks()
        return res

    # 8. Business methods
