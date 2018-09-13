# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class StockPicking(models.Model):
    
    # 1. Private attributes
    _inherit = 'stock.picking'

    # 2. Fields declaration
    quality_check_ids = fields.One2many('product_quality_instruction_i_s.check', 
        'picking_id', 'Quality Checks', readonly=False,
        states={'cancel': [('readonly', True)], 'done': [('readonly', True)] })

    quality_check_count = fields.Integer(
        compute='_compute_quality_check_count',
        string='Quality Check Count',
        store=True,
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends('quality_check_ids')
    def _compute_quality_check_count(self):
        for picking in self:
            picking.quality_check_count = len(picking.quality_check_ids)

    # 5. Constraints and onchanges

    # 6. CRUD methods
    @api.model
    def create(self, vals):
        # When an incoming picking is created from scratch, create the quality checklist
        res = super(StockPicking, self).create(vals)
        if res.picking_type_code == 'incoming': 
            res.initialize_quality_checks()
        return res

    # 7. Action methods
    @api.cr_uid_ids_context
    def do_enter_transfer_details(self, cr, uid, picking, context=None):
        # When clicking the Transfer button, raise an exception if any 
        # of the quality checks are incomplete
        for p in self.browse(cr, uid, picking, context):
            if [check for check in p.quality_check_ids if not check.completed]:
                raise exceptions.except_orm(_('Error'), _('Please finish the quality check list before receiving the goods.'))

        return super(StockPicking, self).do_enter_transfer_details(cr, uid, picking, context)

    # 8. Business methods
    @api.multi
    def initialize_quality_checks(self):
        # Go through all unique products that appear on the picking lines.
        # Find their quality instructions and add them to the list.
        self.ensure_one()
        quality_check_model = self.env['product_quality_instruction_i_s.check']
        self.quality_check_ids = False
        incoming_products = list(set([move.product_id for move in self.move_lines]))
        for product in incoming_products:
            for quality_instruction in product.product_tmpl_id.quality_instruction_ids:
                quality_check_model.create({
                    'instruction_id': quality_instruction.id,
                    'product_id': product.id,
                    'picking_id': self.id,
                })

    def _create_backorder(self, cr, uid, picking, backorder_moves=[], context=None):
        # When an incoming picking is created as a backorder from another picking, create the quality checklist
        res = super(StockPicking, self)._create_backorder(cr, uid, picking, backorder_moves, context)
        if res:
            self.browse(cr,uid, res, context).initialize_quality_checks()
        return res
