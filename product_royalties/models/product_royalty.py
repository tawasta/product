# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductRoyalty(models.Model):
    
    # 1. Private attributes
    _name = 'product.royalty'

    # 2. Fields declaration
    name = fields.Char("Description")
    recipient = fields.Many2one('res.partner')
    role = fields.Selection([
        ('arranger', 'Arranger'),
        ('composer', 'Composer'),
        ('lyricist', 'Lyricist'),
        ('translator', 'Translator'),
    ])
    percent = fields.Float('Royalty %')
    product = fields.Many2one('product.template')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    # @api.onchange('percent')
    # def onchange_percent(self):
    #     # Not implemented yet
    #     royalty_total = 0
    #
    #     for royalty in self.product.royalties:
    #         royalty_total += royalty.percent

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
