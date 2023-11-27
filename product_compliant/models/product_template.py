from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    atex_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="ATEX Compliant",
        domain=[("selectable_for", "in", [False, "atex"])],
        help="This product is ATEX directive compliant.",
    )

    reach_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="REACH Compliant",
        domain=[("selectable_for", "in", [False, "reach"])],
        help="""This product is Registration, Evaluation, Authorisation and
                Restriction of Chemicals regulation compliant.""",
    )

    rohs_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="RoHS Compliant",
        domain=[("selectable_for", "in", [False, "rohs"])],
        help="""This product is Restriction of Hazardous Substances
                Directive 2002/95/EC compliant.""",
    )

    composition_checked_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Composition Checked",
        domain=[("selectable_for", "in", [False, "composition"])],
    )

    msds_checked_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="MSDS (Material Safety Data Sheet) Checked",
        domain=[("selectable_for", "in", [False, "msds"])],
    )

    work_safety_checked_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Work Safety Checked",
        domain=[("selectable_for", "in", [False, "work_safety"])],
    )
