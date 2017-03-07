# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductTemplate(models.Model):
    
    # 1. Private attributes
    _inherit = 'product.template'

    # 2. Fields declaration
    royalties = fields.One2many('product.royalty', 'product')

    royalty_arrangers = fields.One2many(
        'product.royalty',
        'product',
        domain=[('role', '=', 'arranger')],
        string="Arrangers",
    )
    royalty_composers = fields.One2many(
        'product.royalty',
        'product',
        domain=[('role', '=', 'composer')],
        string="Composers",
    )
    royalty_lyricists = fields.One2many(
        'product.royalty',
        'product',
        domain=[('role', '=', 'lyricist')],
        string="Lyricists",
    )
    royalty_translators = fields.One2many(
        'product.royalty',
        'product',
        domain=[('role', '=', 'translator')],
        string="Translators",
    )

    royalty_arrangers_string = fields.Char(string="Arrangers", compute='compute_royalty_arrangers_string')
    royalty_composers_string = fields.Char(string="Composers", compute='compute_royalty_composers_string')
    royalty_lyricists_string = fields.Char(string="Lyricists", compute='compute_royalty_lyricists_string')
    royalty_translators_string = fields.Char(string="Translators", compute='compute_royalty_translators_string')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    def compute_royalty_string(self, records):
        string = ""
        for record in records:
            string += record.recipient.name + ",\n"

        string = string.rstrip("\n").rstrip(",")

        return string

    @api.multi
    def compute_royalty_arrangers_string(self):
        for record in self:
            record.royalty_arrangers_string = record.sudo().compute_royalty_string(record.royalty_arrangers)

    @api.multi
    def compute_royalty_composers_string(self):
        for record in self:
            record.royalty_composers_string = record.sudo().compute_royalty_string(record.royalty_composers)

    @api.multi
    def compute_royalty_lyricists_string(self):
        for record in self:
            record.royalty_lyricists_string = record.sudo().compute_royalty_string(record.royalty_lyricists)

    @api.multi
    def compute_royalty_translators_string(self):
        for record in self:
            record.royalty_translators_string = record.sudo().compute_royalty_string(record.royalty_translators)

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
