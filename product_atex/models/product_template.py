from odoo import fields
from odoo import models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    atex_compliant = fields.Boolean(
        string="ATEX compliant",
        help="ATEX directive compliant",
    )
