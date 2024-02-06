from odoo import api, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    @api.model
    def create(self, values):
        res = super(ProductTemplate, self).create(values)
        res._update_variant_volume(values)
        return res

    def write(self, values):
        res = super(ProductTemplate, self).write(values)
        self._update_variant_volume(values)
        return res

    def _update_variant_volume(self, values):
        for record in self:
            if "volume" in values:
                record.product_variant_ids.write({"volume": values["volume"]})

    @api.depends("product_variant_ids", "product_variant_ids.volume")
    def _compute_volume(self):
        for template in self:
            template.volume = (
                template.product_variant_ids and template.product_variant_ids[0].volume
            )
