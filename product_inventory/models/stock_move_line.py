from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _action_done(self):
        res = super()._action_done()

        for record in self:
            record.sudo().product_id._compute_stock_date()

        return res
