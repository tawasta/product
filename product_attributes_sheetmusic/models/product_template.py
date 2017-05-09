# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:
import validators

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _
from openerp.exceptions import ValidationError
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductTemplate(models.Model):
    
    # 1. Private attributes
    _inherit = 'product.template'

    # 2. Fields declaration
    note_information_checked = fields.Date("Everything checked", help="Everything is OK!")

    # Info
    note_catalog_number = fields.Char("Catalog number")
    note_length = fields.Char("Length")

    # ISMN
    note_ismn_paper = fields.Char("ISMN paper", help="International Standard Music Number")
    note_ismn_pdf = fields.Char("ISMN PDF", help="International Standard Music Number")

    # Note originals
    note_original_location = fields.Char("Original location")
    note_original_exists = fields.Boolean("Original exists")
    note_original_nonexistent = fields.Boolean("Original nonexistent")
    note_original_saleable_exists = fields.Boolean("Saleable original exists")
    note_original_non_saleable_exists = fields.Boolean("Non-saleable original exists")

    note_card_index = fields.Boolean("Card index")
    note_parts = fields.Text("Parts")
    note_publisher = fields.Char("Publisher")

    # Contracts
    note_contract_ended = fields.Boolean("Contract ended")
    note_contract_ended_date = fields.Date("Contract ended date")

    note_publishing_contract_exists = fields.Boolean("Publishing contract exists")
    note_publishing_contract_date = fields.Date("Publishing contract date")

    note_publishing_agreement_exists = fields.Boolean("Publishing agreement exists")
    note_publishing_agreement_date = fields.Date("Publishing agreement date")

    # Royalties
    note_royalty_notice_done = fields.Boolean("Royalty notice done")
    note_royalty_contract_date = fields.Date("Royalty contract date")
    note_royalty_old_list = fields.Boolean("Roayalty old list")
    note_royalty_list = fields.Boolean("Roayalty new list")

    # Digitalization
    note_free_copy = fields.Date("Free copy (PDF)")

    note_pdf_ok = fields.Char("PDF-version OK")
    note_scan_name = fields.Char("Scanned PDF name")
    note_scan_date = fields.Date("Scan date")
    note_page_count_score = fields.Integer("Page count score")
    note_parts_count = fields.Integer("Parts count")

    # Other
    note_creator_piece_delivered = fields.Boolean("Tekijänkappale delivered")
    note_creator_piece_delivered_date = fields.Date("Tekijänkappale delivered")

    note_free_piece_delivered = fields.Boolean("Vapaakappaleet (paper) delivered to Kansallisarkisto")
    note_free_piece_delivered_date = fields.Date("Vapaakappaleet (paper) delivered to Kansallisarkisto")

    note_free_piece_delivered_pdf = fields.Boolean("Vapaakappaleet (PDF) delivered to Kansallisarkisto")
    note_free_piece_delivered_pdf_date = fields.Date("Vapaakappaleet (PDF) delivered to Kansallisarkisto")

    # Samples
    note_pdf_filename = fields.Char("Sample PDF Filename")
    note_pdf = fields.Binary("Sample PDF")

    note_url = fields.Char("Sample URL")
    note_youtube_url = fields.Char("Youtube URL")
    note_soundcloud_url = fields.Char("Soundcloud URL")
    note_finnbandshop_url = fields.Char("Finnbandshop URL")

    # Helper fields
    note_grade = fields.Many2one(
        'product.attribute.value',
        "Grade",
        compute='compute_note_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Grade')],
    )
    note_class = fields.Many2one(
        'product.attribute.value',
        "Note class",
        compute='compute_note_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Laji')],
    )
    note_composition = fields.Many2one(
        'product.attribute.value',
        "Note composition",
        compute='compute_note_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Kokoonpano')],
    )
    note_publish_year = fields.Many2one(
        'product.attribute.value',
        "Note publish year",
        compute='compute_note_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Julkaisuvuosi')],
    )

    note_publishing_agreement_or_contract_date = fields.Date(
        "Contract date",
        compute='compute_note_publishing_agreement_or_contract_date',
        store=True
    )

    # Alternative price
    list_price_members = fields.Float("Member price", digits=dp.get_precision('Product Price'))

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    @api.depends('attribute_line_ids')
    def compute_note_attributes(self):
        for record in self:
            for attribute in record.attribute_line_ids:
                if attribute.attribute_id.name == 'Grade' and attribute.value_ids:
                    record.note_grade = attribute.value_ids[0].id

                if attribute.attribute_id.name == 'Laji' and attribute.value_ids:
                    record.note_class = attribute.value_ids[0].id

                if attribute.attribute_id.name == 'Kokoonpano' and attribute.value_ids:
                    record.note_composition = attribute.value_ids[0].id

                if attribute.attribute_id.name == 'Julkaisuvuosi' and attribute.value_ids:
                    record.note_publish_year = attribute.value_ids[0].id
    @api.multi
    @api.depends('note_publishing_contract_date', 'note_publishing_agreement_date')
    def compute_note_publishing_agreement_or_contract_date(self):
        for record in self:
            record.note_publishing_agreement_or_contract_date = \
                record.note_publishing_agreement_date or record.note_publishing_contract_date

    # 5. Constraints and onchanges
    @api.multi
    @api.constrains('note_url')
    def _check_note_url(self):
        for record in self:
            if record.note_url and not validators.url(record.note_url):
                raise ValidationError(_("Sample URL is not valid"))

    @api.multi
    @api.constrains('note_youtube_url')
    def _check_note_youtube_url(self):
        for record in self:
            if record.note_youtube_url and not validators.url(record.note_youtube_url):
                raise ValidationError(_("Sample URL is not valid"))

    @api.multi
    @api.constrains('note_soundcloud_url')
    def _check_note_soundcloud_url(self):
        for record in self:
            if record.note_youtube_url and not validators.url(record.note_soundcloud_url):
                raise ValidationError(_("Sample URL is not valid"))

    @api.multi
    @api.constrains('note_finnbandshop_url')
    def _check_note_finnbandshop_url(self):
        for record in self:
            if record.note_finnbandshop_url and not validators.url(record.note_finnbandshop_url):
                raise ValidationError(_("Sample URL is not valid"))

    @api.multi
    @api.onchange('note_creator_piece_delivered_date')
    def onchange_note_creator_piece_delivered_date_update_note_creator_piece_delivered(self):
        for record in self:
            if record.note_creator_piece_delivered_date:
                record.note_creator_piece_delivered = True

    @api.multi
    @api.onchange('note_free_piece_delivered_date')
    def onchange_note_free_piece_delivered_date_update_note_free_piece_delivered(self):
        for record in self:
            if record.note_free_piece_delivered_date:
                record.note_free_piece_delivered = True

    @api.multi
    @api.onchange('note_free_piece_delivered_pdf_date')
    def onchange_note_free_piece_delivered_pdf_date_update_note_free_piece_delivered_pdf(self):
        for record in self:
            if record.note_free_piece_delivered_pdf_date:
                record.note_free_piece_delivered_pdf = True

    @api.onchange('note_publishing_contract_date')
    def onchange_note_publishing_contract_date_update_note_publishing_contract_exists(self):
        for record in self:
            if record.note_publishing_contract_date:
                record.note_publishing_contract_exists = True

    @api.onchange('note_publishing_agreement_date')
    def onchange_note_publishing_agreement_date_update_note_publishing_agreement_exists(self):
        for record in self:
            if record.note_publishing_agreement_date:
                record.note_publishing_agreement_exists = True

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
