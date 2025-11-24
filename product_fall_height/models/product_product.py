from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    fall_height = fields.Float(
        help="The greatest height the person using this product can fall from",
    )

    def _prepare_variant_values(self, combination):
        """
        As variant is created inside template create() method and as
        template fields values are flushed after _create_variant_ids(),
        we catch the variant values preparation to update them
        """
        res = super()._prepare_variant_values(combination)
        if self.fall_height:
            res.update({"fall_height": self.fall_height})

        return res
