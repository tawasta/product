from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    reach_compliant = fields.Boolean(
        string="REACH Compliant",
        help="This product is Registration, Evaluation, Authorisation and Restriction "
        "of Chemicals regulation compliant.",
    )
