from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _action_done(self):
        res = super()._action_done()

        self.product_id._compute_stock_date()

        return res
