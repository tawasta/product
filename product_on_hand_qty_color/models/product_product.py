from odoo import api, fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    has_stock_on_several_locations = fields.Boolean(
        compute=lambda self: self._compute_stock_on_several_locations()
    )

    @api.depends("qty_available")
    def _compute_stock_on_several_locations(self):
        for product in self:
            quants = (
                self.env["stock.quant"].sudo().search([("product_id", "=", product.id)])
            )

            locations = [
                q.location_id.id for q in quants if q.location_id.usage == "internal"
            ]

            if locations and locations.count(locations[0]) != len(locations):
                product.has_stock_on_several_locations = True
            else:
                product.has_stock_on_several_locations = False
