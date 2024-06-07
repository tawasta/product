import logging
import operator as py_operator

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

OPERATORS = {
    "<": py_operator.lt,
    ">": py_operator.gt,
    "<=": py_operator.le,
    ">=": py_operator.ge,
    "=": py_operator.eq,
    "!=": py_operator.ne,
}


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    relative_net_weight_percentage = fields.Float(
        string="Net Weight-%",
        compute=lambda self: self._compute_relative_net_weight(),
        search="_search_relative_net_weight_percentage",
    )

    relative_gross_weight_percentage = fields.Float(
        string="Gross Weight-%",
        compute=lambda self: self._compute_relative_net_weight(),
        search="_search_relative_gross_weight_percentage",
    )

    def _search_relative_net_weight_percentage(self, operator, value):
        if operator not in ("<", ">", "=", "!=", "<=", ">="):
            raise UserError(_("Invalid domain operator %s", operator))
        if not isinstance(value, (float, int)):
            raise UserError(_("Invalid domain right operand %s", value))

        ids = []
        for material in self.with_context(prefetch_fields=False).search([], order="id"):
            if OPERATORS[operator](material["relative_net_weight_percentage"], value):
                ids.append(material.id)
        return [("id", "in", ids)]

    def _search_relative_gross_weight_percentage(self, operator, value):
        if operator not in ("<", ">", "=", "!=", "<=", ">="):
            raise UserError(_("Invalid domain operator %s", operator))
        if not isinstance(value, (float, int)):
            raise UserError(_("Invalid domain right operand %s", value))

        ids = []
        for material in self.with_context(prefetch_fields=False).search([], order="id"):
            if OPERATORS[operator](material["relative_gross_weight_percentage"], value):
                ids.append(material.id)
        return [("id", "in", ids)]

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
