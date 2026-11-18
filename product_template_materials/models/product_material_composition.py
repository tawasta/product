from odoo import api, fields, models


class ProductMaterialComposition(models.Model):
    _inherit = "product.material.composition"

    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        string="Product Template",
        tracking=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        templates = self.env["product.template"].browse(
            [
                vals["product_tmpl_id"]
                for vals in vals_list
                if vals.get("product_tmpl_id")
            ]
        )
        template_by_id = {template.id: template for template in templates}
        for vals in vals_list:
            template = template_by_id.get(vals.get("product_tmpl_id"))
            if template and template.product_variant_count == 1:
                vals["product_product_id"] = template.product_variant_ids.id
        return super().create(vals_list)

    def set_product_tmpl_id(self):
        """Fill in the missing product or product template link.

        Links that are already set are never removed."""
        missing_template = self.filtered(
            lambda material: not material.product_tmpl_id
            and material.product_product_id
        )
        for template, materials in missing_template.grouped(
            lambda material: material.product_product_id.product_tmpl_id
        ).items():
            materials.product_tmpl_id = template

        missing_variant = self.filtered(
            lambda material: material.product_tmpl_id
            and not material.product_product_id
            and material.product_tmpl_id.product_variant_count == 1
        )
        for template, materials in missing_variant.grouped("product_tmpl_id").items():
            materials.product_product_id = template.product_variant_ids
