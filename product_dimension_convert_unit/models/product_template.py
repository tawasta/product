from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def _calc_volume(self, product_length, product_height, product_width, uom_id):
        volume = super(ProductTemplate, self)._calc_volume(
            product_length, product_height, product_width, uom_id
        )

        if self.volume_uom_id.uom_type == "reference":
            # Convert first to liters, which is the reference unit
            volume = volume * 1000
        else:
            # This is okay because the original volume is in cubic meters
            volume = volume / 1000

        volume = volume / self.volume_uom_id.factor

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
