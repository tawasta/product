from odoo import _, models
from odoo.exceptions import ValidationError


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    def write(self, vals):
        if self.env["res.users"].has_group(
            "product_materials_block_and_allow_edit.allow_material_edit"
        ):
            return super().write(vals)
        else:
            raise ValidationError(_("Editing materials is not enabled for your user"))
