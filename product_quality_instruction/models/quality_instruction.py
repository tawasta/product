# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class QualityInstruction(models.Model):
    
    # 1. Private attributes
    _name = 'product_quality_instruction.instruction'
    _inherit = ['mail.thread']
    _description = 'Product Quality Instruction Document'
    _INSTRUCTION_TYPES = [('text', 'Text'), ('url', 'URL'), ('file', 'File')]

    # 2. Fields declaration
    name = fields.Char('Name', required=True)
    type = fields.Selection(_INSTRUCTION_TYPES, 'Type', required=True)
    instruction_text = fields.Text('Instruction')
    instruction_url = fields.Char('URL')
    instruction_file = fields.Binary('File', attachment=True)
    comments = fields.Text('Comments')
    active = fields.Boolean('Active', default=True, help='''Inactive quality instructions are hidden from lists but remain saved in Odoo. ''')
    product_template_ids = fields.Many2many('product.template',
        'prod_qual_instr_rel',
        'instr_id', 'prod_id', 
        'Products', help='''Products that this instruction applies to''')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
