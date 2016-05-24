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
    note_catalog_number = fields.Char("Catalog number")
    note_length = fields.Char("Length")
    note_ismn = fields.Char("ISMN", help="International Standard Music Number")

    note_original_location = fields.Char("Original location")
    note_original_nonexistent = fields.Boolean("Original nonexistent")

    note_publisher = fields.Char("Publisher")

    note_contract_date = fields.Date("Contract date")
    note_publishing_contract_date = fields.Date("Publishing contract date")

    note_royalty_date = fields.Date("Royalty date")
    note_royalty_notice = fields.Date("Royalty notice done")

    note_contract_ended = fields.Boolean("Contract ended")

    note_creator_piece_delivered = fields.Boolean("Tekijänkappale delivered")
    note_free_piece_delivered = fields.Boolean("Vapaakappaleet delivered to Kansallisarkisto")

    note_pdf_filename = fields.Char("Sample PDF Filename")
    note_pdf = fields.Binary("Sample PDF")
    note_url = fields.Char("Sample URL")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
