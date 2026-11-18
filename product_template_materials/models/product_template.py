from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_tmpl_id",
        string="Product Material Compositions",
        domain=[("type", "=", "product")],
    )

    product_packaging_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_tmpl_id",
        string="Product Packaging Material Compositions",
        domain=[("type", "=", "product_packaging")],
    )

    is_delivery_package = fields.Boolean(
        string="Delivery package",
        compute="_compute_is_delivery_package",
        store=True,
    )

    @api.depends(
        "product_variant_ids",
        "product_variant_ids.active",
        "product_variant_ids.is_delivery_package",
    )
    def _compute_is_delivery_package(self):
        for template in self:
            # Archived variants are ignored whatever the context of the recompute,
            # unless the whole product is archived (as core does for its variant fields)
            variants = (
                template.with_context(active_test=True).product_variant_ids
                or template.with_context(active_test=False).product_variant_ids
            )
            template.is_delivery_package = (
                len(variants) == 1 and variants.is_delivery_package
            )
