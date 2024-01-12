from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _action_done(self):
        # Needs a better way to do this, right? It will not fetch the latest
        # information but it cannot be run after "res = super()._action_done()"
        # because it would cause an error upon unbuilds in manufacturing orders
        # or when their produced quantity is changed after their initial assigned
        # quantity.
        for record in self:
            record.sudo().product_id._compute_stock_date()

        res = super()._action_done()
        return res
