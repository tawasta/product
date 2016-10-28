# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:
import validators

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _
from openerp.exceptions import ValidationError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductTemplate(models.Model):
    
    # 1. Private attributes
    _inherit = 'product.template'

    # 2. Fields declaration
    note_catalog_number = fields.Char("Catalog number")
    note_length = fields.Char("Length")

    note_ismn_paper = fields.Char("ISMN paper", help="International Standard Music Number")
    note_ismn_pdf = fields.Char("ISMN PDF", help="International Standard Music Number")

    note_original_location = fields.Char("Original location")
    note_original_nonexistent = fields.Boolean("Original nonexistent")

    note_publisher = fields.Char("Publisher")

    note_contract_date = fields.Date("Contract date")

    note_publishing_contract_exists = fields.Char("Publishing contract exists")
    note_publishing_contract_date = fields.Date("Publishing contract date")

    note_publishing_agreement_exists = fields.Char("Publishing agreement exists")
    note_publishing_agreement_date = fields.Date("Publishing agreement date")

    note_royalty_contract_date = fields.Date("Royalty contract date")
    note_royalty_notice = fields.Date("Royalty notice done")

    note_contract_ended = fields.Boolean("Contract ended")

    note_creator_piece_delivered = fields.Boolean("Tekijänkappale delivered")
    note_free_piece_delivered = fields.Boolean("Vapaakappaleet (paper) delivered to Kansallisarkisto")
    note_free_piece_delivered_pdf = fields.Boolean("Vapaakappaleet (PDF) delivered to Kansallisarkisto")

    note_pdf_filename = fields.Char("Sample PDF Filename")
    note_pdf = fields.Binary("Sample PDF")

    note_url = fields.Char("Sample URL")
    note_youtube_url = fields.Char("Youtube URL")
    note_soundcloud_url = fields.Char("Soundcloud URL")
    note_finnbandshop_url = fields.Char("Finnbandshop URL")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.one
    @api.constrains('note_url')
    def _check_note_url(self):
        if self.note_url and not validators.url(self.note_url):
            raise ValidationError(_("Sample URL is not valid"))

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
