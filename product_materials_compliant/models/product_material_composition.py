from odoo import fields, models


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    chemicals_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Chemicals Compliant",
        domain=[("selectable_for", "in", [False, "chemicals"])],
    )

    conflict_area_minerals_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Conflict Area Minerals Compliant",
        domain=[("selectable_for", "in", [False, "conflict_area_minerals"])],
    )

    halogen_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Halogen Compliant",
        domain=[("selectable_for", "in", [False, "halogens"])],
    )

    pop_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="POP Compliant",
        domain=[("selectable_for", "in", [False, "pop"])],
    )

    reach_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="REACH Compliant",
        domain=[("selectable_for", "in", [False, "reach"])],
        help="""This material is Registration, Evaluation, Authorisation and
                Restriction of Chemicals regulation compliant.""",
    )

    rohs_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="RoHS Compliant",
        domain=[("selectable_for", "in", [False, "rohs"])],
        help="""This material is Restriction of Hazardous Substances
                Directive 2002/95/EC compliant.""",
    )

    scip_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="SCIP Compliant",
        domain=[("selectable_for", "in", [False, "scip"])],
    )
