from odoo import fields
from odoo import models


class ProductProduct(models.Model):

    _inherit = "product.template"

    rohs_compliant = fields.Boolean(
        string="RoHS compliant",
        help="Restriction of Hazardous Substances Directive 2002/95/EC compliant",
    )
