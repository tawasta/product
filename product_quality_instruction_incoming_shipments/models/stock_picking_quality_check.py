# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class QualityCheck(models.Model):
    
    # 1. Private attributes
    _name = 'product_quality_instruction_i_s.check'
    _description = 'Instruction for incoming shipments'
    _rec_name = 'instruction_id'
    _RESULT_TYPES = [('pass', 'Passed'), ('fail', 'Failed'), ('not_received', 'Not Received')]

    # 2. Fields declaration
    instruction_id = fields.Many2one('product_quality_instruction.instruction', 'Instruction', required=True, ondelete='restrict')
    product_id = fields.Many2one('product.product', 'Product', required=True)
    completed = fields.Boolean('Completed')
    user_id = fields.Many2one('res.users', 'Completed by')
    picking_id = fields.Many2one('picking_id', string='Receipt')
    comments = fields.Char('Comments')
    result = fields.Selection(_RESULT_TYPES, 'Result')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('completed')
    def onchange_completed(self):
        # When Completed checkbox is checked, suggest current user for the Completed By field
        if not self.completed:
            self.user_id = False
        else:
            self.user_id = self.env.uid

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
