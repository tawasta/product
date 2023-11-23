from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    product_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        string="Product Material Compositions",
        compute="_compute_product_material_composition_ids",
        inverse="_inverse_product_material_composition_ids",
    )

    product_packaging_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        string="Product Material Compositions",
        compute="_compute_product_packaging_material_composition_ids",
        inverse="_inverse_product_packaging_material_composition_ids",
    )

    # Helpers to keep the material composition infos in sync with the first variant.
    # The first should always be the only variant, because this module should
    # only be installed if Product Variants are not enabled in Odoo
    @api.depends(
        "product_variant_ids", "product_variant_ids.product_material_composition_ids"
    )
    def _compute_product_material_composition_ids(self):
        for p in self:
            if len(p.product_variant_ids) == 1:
                p.product_material_composition_ids = (
                    p.product_variant_ids.product_material_composition_ids
                )
            else:
                p.product_material_composition_ids = False

    def _inverse_product_material_composition_ids(self):
        for p in self:
            if len(p.product_variant_ids) == 1:
                p.product_variant_ids.product_material_composition_ids = (
                    p.product_material_composition_ids
                )

    @api.depends(
        "product_variant_ids",
        "product_variant_ids.product_packaging_material_composition_ids",
    )
    def _compute_product_packaging_material_composition_ids(self):
        for p in self:
            if len(p.product_variant_ids) == 1:
                p.product_packaging_material_composition_ids = (
                    p.product_variant_ids.product_packaging_material_composition_ids
                )
            else:
                p.product_packaging_material_composition_ids = False

    def _inverse_product_packaging_material_composition_ids(self):
        for p in self:
            if len(p.product_variant_ids) == 1:
                p.product_variant_ids.product_packaging_material_composition_ids = (
                    p.product_packaging_material_composition_ids
                )
