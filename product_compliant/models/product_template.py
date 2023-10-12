from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    atex_compliant = fields.Many2one(
        "product.compliant",
        string="ATEX Compliant",
        help="This product is ATEX directive compliant.",
    )

    reach_compliant = fields.Many2one(
        "product.compliant",
        string="REACH Compliant",
        help="""This product is Registration, Evaluation, Authorisation and
                Restriction of Chemicals regulation compliant.""",
    )

    rohs_compliant = fields.Many2one(
        "product.compliant",
        string="RoHS Compliant",
        help="""This product is Restriction of Hazardous Substances
                Directive 2002/95/EC compliant.""",
    )

    composition_checked_compliant = fields.Many2one(
        "product.compliant", string="Composition Checked"
    )

    msds_checked_compliant = fields.Many2one(
        "product.compliant", string="MSDS (Material Safety Data Sheet) Checked"
    )

    work_safety_checked_compliant = fields.Many2one(
        "product.compliant", string="Work Safety Checked"
    )
