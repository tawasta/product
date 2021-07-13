from odoo import fields
from odoo import models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    reach_compliant = fields.Boolean(
        string="REACH compliant",
        help="Registration, Evaluation, Authorisation and Restriction of Chemicals "
        "regulation compliant",
    )
