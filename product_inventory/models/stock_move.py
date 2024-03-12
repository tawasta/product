from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _action_done(self, cancel_backorder):
        res = super()._action_done(cancel_backorder)
        for record in self:
            record.sudo().product_id._compute_stock_date()

        return res
