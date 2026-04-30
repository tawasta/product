from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_a_designer = fields.Boolean(
        string="Is a Designer",
        help="Enable this if the contact is a product designer.",
    )

    provision = fields.Float(
        string="Commission (%)",
        digits=(16, 2),
        help="Commission percentage for this designer.",
    )