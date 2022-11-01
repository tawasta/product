from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.template"

    rohs_compliant = fields.Boolean(
        string="RoHS Compliant",
        help="This product is Restriction of Hazardous Substances Directive 2002/95/EC "
        "compliant.",
    )
