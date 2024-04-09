from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, values):
        res = super(ProductTemplate, self).create(values)
        res._update_variant_dimensions(values)
        return res

    def write(self, values):
        res = super(ProductTemplate, self).write(values)
        self._update_variant_dimensions(values)
        return res

    def _update_variant_dimensions(self, values):
        for record in self:
            if "dimensional_uom_id" in values:
                record.product_variant_ids.write(
                    {"dimensional_uom_id": values["dimensional_uom_id"]}
                )

            if "product_length" in values:
                record.product_variant_ids.write(
                    {"product_length": values["product_length"]}
                )

            if "product_height" in values:
                record.product_variant_ids.write(
                    {"product_height": values["product_height"]}
                )

            if "product_width" in values:
                record.product_variant_ids.write(
                    {"product_width": values["product_width"]}
                )
