from odoo import fields, models


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    _CHEMICALS_DOMAIN = [("selectable_for", "in", [False, "chemicals"])]
    _CONFLICT_AREA_MINERALS_DOMAIN = [
        ("selectable_for", "in", [False, "conflict_area_minerals"])
    ]
    _HALOGENS_DOMAIN = [("selectable_for", "in", [False, "halogens"])]
    _POP_DOMAIN = [("selectable_for", "in", [False, "pop"])]
    _REACH_DOMAIN = [("selectable_for", "in", [False, "reach"])]
    _ROHS_DOMAIN = [("selectable_for", "in", [False, "rohs"])]
    _SCIP_DOMAIN = [("selectable_for", "in", [False, "scip"])]

    # Suggest defaults for each compliancy based on what allowed option has the lowest secuence.
    def _get_default_chemicals_compliant(self):
        return self.env["product.compliant"].search(self._CHEMICALS_DOMAIN, limit=1).id

    def _get_conflict_area_minerals_compliant(self):
        return (
            self.env["product.compliant"]
            .search(self._CONFLICT_AREA_MINERALS_DOMAIN, limit=1)
            .id
        )

    def _get_default_halogen_compliant(self):
        return self.env["product.compliant"].search(self._HALOGENS_DOMAIN, limit=1).id

    def _get_default_pop_compliant(self):
        return self.env["product.compliant"].search(self._POP_DOMAIN, limit=1).id

    def _get_default_reach_compliant(self):
        return self.env["product.compliant"].search(self._REACH_DOMAIN, limit=1).id

    def _get_default_rohs_compliant(self):
        return self.env["product.compliant"].search(self._ROHS_DOMAIN, limit=1).id

    def _get_default_scip_compliant(self):
        return self.env["product.compliant"].search(self._SCIP_DOMAIN, limit=1).id

    chemicals_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Chemicals",
        domain=_CHEMICALS_DOMAIN,
        help="Is this material Chemical compliant?",
        default=_get_default_chemicals_compliant,
    )

    conflict_area_minerals_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Conflict Area Minerals",
        domain=_CONFLICT_AREA_MINERALS_DOMAIN,
        help="Is this material Conflict Area Minerals compliant?",
        default=_get_conflict_area_minerals_compliant,
    )

    halogen_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Halogens",
        domain=_HALOGENS_DOMAIN,
        help="Is this material Halogen compliant?",
        default=_get_default_halogen_compliant,
    )

    pop_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="POP",
        domain=_POP_DOMAIN,
        help="Is this material POP (Persistant Organic Pollutants) compliant?",
        default=_get_default_pop_compliant,
    )

    reach_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="REACH",
        domain=_REACH_DOMAIN,
        help="Is this material REACH compliant?",
        default=_get_default_reach_compliant,
    )

    rohs_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="RoHS ",
        domain=_ROHS_DOMAIN,
        help="Is this material RoHS compliant",
        default=_get_default_rohs_compliant,
    )

    scip_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="SCIP",
        domain=_SCIP_DOMAIN,
        help="Is this material SCIP (Substances of Concern In Products) compliant?",
        default=_get_default_scip_compliant,
    )
