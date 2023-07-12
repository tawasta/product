from odoo import api, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    @api.onchange(
        "product_length",
        "product_height",
        "product_width",
        "dimensional_uom_id",
        "volume_uom_id",
    )
    def onchange_calculate_volume(self):
        return super(ProductProduct, self).onchange_calculate_volume()
