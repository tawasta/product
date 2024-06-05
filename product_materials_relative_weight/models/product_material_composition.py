import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    relative_net_weight_percentage = fields.Float(
        string="Net Weight-%", compute=lambda self: self._compute_relative_net_weight()
    )

    relative_gross_weight_percentage = fields.Float(
        string="Gross Weight-%",
        compute=lambda self: self._compute_relative_net_weight(),
    )

    @api.depends(
        "net_weight",
        "product_product_id",
        "product_product_id.weight",
        "product_product_id.gross_weight",
    )
    def _compute_relative_net_weight(self):
        for material in self:
            product = material.product_product_id

            grams = self.env.ref("uom.product_uom_gram")

            weight_in_grams = product.weight_uom_id._compute_quantity(
                product.weight, grams
            )
            gross_in_grams = product.weight_uom_id._compute_quantity(
                product.gross_weight, grams
            )
            material_in_grams = material.net_weight_uom_id._compute_quantity(
                material.net_weight, grams
            )

            if material.type == "product" and weight_in_grams:
                material.relative_net_weight_percentage = (
                    material_in_grams / weight_in_grams
                )
            else:
                material.relative_net_weight_percentage = 0

            if (
                material.type == "product_packaging"
                and gross_in_grams
                and (gross_in_grams - weight_in_grams > 0)
            ):
                material.relative_gross_weight_percentage = material_in_grams / (
                    gross_in_grams - weight_in_grams
                )
            else:
                material.relative_gross_weight_percentage = 0

            # Info if a result is negative value and this should not be possible
            if gross_in_grams - weight_in_grams < 0:
                _logger.info(
                    "Negative weight result on {} product. "
                    "PLEASE FIX THIS!".format(product.display_name)
                )
