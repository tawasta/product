from odoo import api, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    @api.model
    def create(self, values):
        res = super(ProductTemplate, self).create(values)
        res._update_variant_weight_and_volume(values)
        return res

    def write(self, values):
        res = super(ProductTemplate, self).write(values)
        self._update_variant_weight_and_volume(values)
        return res

    def _update_variant_weight_and_volume(self, values):
        for record in self:
            if "weight" in values:
                record.product_variant_ids.write({"weight": values["weight"]})

            if "volume" in values:
                record.product_variant_ids.write({"volume": values["volume"]})
