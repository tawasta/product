from odoo import _, models
from odoo.exceptions import ValidationError


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    def write(self, vals):
        allow_material_edit = self.product_product_id.allow_material_edit

        edit_delivery_package = vals.get("is_delivery_package", False)

        if allow_material_edit or edit_delivery_package:
            return super().write(vals)
        else:
            raise ValidationError(
                _("Editing materials is not enabled from its product")
            )
