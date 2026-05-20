from odoo import api, fields, models


class ProductMaterialComposition(models.Model):
    _inherit = "product.material.composition"

    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        string="Product Template",
        tracking=True,
        store=True,
    )

    @api.model
    def create(self, vals):
        prod_template_id = vals.get("product_tmpl_id", False)
        prod_template = self.env["product.template"].browse(prod_template_id)
        if prod_template and prod_template.product_variant_count == 1:
            vals["product_product_id"] = (
                prod_template.product_variant_ids
                and prod_template.product_variant_ids[0].id
            )
        return super().create(vals)

    def set_product_tmpl_id(self):
        for material in self:
            if not material.product_tmpl_id and material.product_product_id:
                material.product_tmpl_id = material.product_product_id.product_tmpl_id
            elif (
                material.product_tmpl_id
                and not material.product_product_id
                and material.product_tmpl_id.product_variant_count == 1
            ):
                material.product_product_id = (
                    material.product_tmpl_id.product_variant_ids
                )
            else:
                material.product_tmpl_id = False
