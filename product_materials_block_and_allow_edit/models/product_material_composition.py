from odoo import _, models
from odoo.exceptions import ValidationError


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    def write(self, vals):
        allow_material_edit = self.product_product_id.allow_material_edit

        if allow_material_edit:
            return super().write(vals)
        else:
            raise ValidationError(
                _("Editing materials is not enabled from its product")
            )
