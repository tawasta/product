from odoo import fields, models


class StockInventoryLine(models.Model):
    _inherit = "stock.inventory.line"

    adjustment_date = fields.Datetime(related="inventory_id.date")
