# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductUom(models.Model):
    
    # 1. Private attributes
    _inherit = 'product.uom'

    # 2. Fields declaration
    reference_unit_id = fields.Many2one(
        string='Reference unit',
        comodel_name='product.uom',
        compute='_compute_reference_unit_id',
    )

    factor_example = fields.Char(
        string='Example 1',
        compute='_compute_factor_example'
    )

    factor_example_inverse = fields.Char(
        string='Example 2',
        compute='_compute_factor_example'
    )

    # 3. Default methods

    # 4. Compute and search fields
    @api.onchange('category_id')
    @api.depends('category_id')
    def _compute_reference_unit_id(self):
        ProductUom = self.env['product.uom']

        for record in self:
            record.reference_unit_id = ProductUom.search([
                ('category_id', '=', record.category_id.id),
                ('uom_type', '=', 'reference'),
            ], limit=1)

    @api.onchange('factor')
    @api.depends('factor')
    def _compute_factor_example(self):
        for record in self:
            example = ''
            example_inverse = ''

            example = '1 * %s = %s * %s' % (
                record.reference_unit_id.name,
                record.reference_unit_id._compute_quantity(1, record),
                record.name,
            )

            example_inverse = '1 * %s = %s * %s' % (
                record.name,
                record._compute_quantity(1, record.reference_unit_id),
                record.reference_unit_id.name,
            )

            if record.uom_type == 'smaller':
                # Swap examples
                example, example_inverse = example_inverse, example

            record.factor_example = example
            record.factor_example_inverse = example_inverse

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
