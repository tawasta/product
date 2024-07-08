from odoo import _, models
from odoo.exceptions import ValidationError


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    def write(self, vals):
        for material in self:
            allow_material_edit = material.product_product_id.allow_material_edit

            edit_delivery_package = vals.get("is_delivery_package", False)
            edit_upper_category = vals.get("product_material_upper_category_id", False)

            if allow_material_edit or edit_delivery_package or edit_upper_category:
                return super().write(vals)
            else:
                raise ValidationError(
                    _("Editing materials is not enabled from its product")
                )
