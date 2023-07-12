from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def _calc_volume(self, product_length, product_height, product_width, uom_id):
        volume = super(ProductTemplate, self)._calc_volume(
            product_length, product_height, product_width, uom_id
        )

        # Just return the original volume, if the selected UoM is in cubic meters
        if self.volume_uom_id.id == self.env.ref("uom.product_uom_cubic_meter").id:
            return volume

        # Convert first to liters, which is the reference unit
        volume = volume * 1000

        # Then convert liters to the selected volume
        volume = volume * self.volume_uom_id.factor

        return volume

    @api.onchange(
        "product_length",
        "product_height",
        "product_width",
        "dimensional_uom_id",
        "volume_uom_id",
    )
    def onchange_calculate_volume(self):
        return super(ProductTemplate, self).onchange_calculate_volume()
