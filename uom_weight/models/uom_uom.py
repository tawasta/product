from odoo import models


class UomUom(models.Model):

    _inherit = "uom.uom"

    # Compute and search fields, in the same order that fields declaration
    def _compute_weight(self, weight, to_unit):
        if len(self) == 0:
            return 0

        self.ensure_one()

        if not self or not weight or not to_unit or self == to_unit:
            return weight

        if self.category_id.id != to_unit.category_id.id:
            return weight

        uom_weight = weight * self.factor

        if to_unit:
            uom_weight = uom_weight / to_unit.factor

        return uom_weight
