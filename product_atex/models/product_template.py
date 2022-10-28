from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    atex_compliant = fields.Boolean(
        string="ATEX Compliant",
        help="This product is ATEX directive compliant.",
    )
