from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_tmpl_id",
        string="Product Material Compositions",
    )

    product_packaging_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_tmpl_id",
        string="Product Packaging Material Compositions",
    )

    is_delivery_package = fields.Boolean(
        compute=lambda self: self._compute_product_material_info(),
        store=True,
    )

    @api.depends(
        "product_variant_ids",
        "product_variant_ids.product_material_composition_ids",
        "product_variant_ids.product_packaging_material_composition_ids",
        "product_variant_ids.is_delivery_package",
    )
    def _compute_product_material_info(self):
        for template in self:
            if template.product_variant_count == 1:
                template.is_delivery_package = (
                    template.product_variant_ids.is_delivery_package
                )
            else:
                template.is_delivery_package = False
