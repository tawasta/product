from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"


class ProductProduct(models.Model):
    _inherit = "product.product"

    inventory_date = fields.Date(
        compute="_compute_inventory_date",
        index=True,
        help="Latest product inventory date",
        store=True
    )
    stock_move_date = fields.Date(
        string="Stock in date",
        compute="_compute_stock_date",
        index=True,
        help="Latest product receipt from vendor",
        store=True
    )

    stock_inventory_line_ids = fields.One2many(
        "stock.inventory.line", "product_id", help="Technical: used to compute lines."
    )

    @api.depends("stock_inventory_line_ids")
    def _compute_inventory_date(self):
        inventory_line_model = self.env["stock.inventory.line"].sudo()

        for record in self:

            inventory_lines = (
                inventory_line_model.search(
                    [("product_id", "=", record.id), ("inventory_id.date", "!=", False)]
                )
                .mapped("inventory_id")
            )

            dates = [line.date for line in inventory_lines]
            record.inventory_date = dates and max(dates) or False


    @api.depends("stock_move_ids")
    def _compute_stock_date(self):
        for record in self:
            in_moves = record.stock_move_ids.filtered(
                lambda sm: sm.date
                and sm.state == "done"
                and sm.location_id.usage in ["supplier", "transit"]
                and sm.location_dest_id.usage in ["internal"]
            )

            dates = [move.date for move in in_moves]
            record.stock_move_date = dates and max(dates) or False

    def action_view_inventory_lines(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "product_inventory.stock_inventory_line_action"
        )
        action["domain"] = [("product_id", "=", self.id)]
        return action
