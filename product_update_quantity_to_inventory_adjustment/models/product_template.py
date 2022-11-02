from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    def action_update_quantity_to_inventory_adjustment(self):
        company = self.env.user.company_id

        # Search based on Warehouse's address information
        stock_warehouse = (
            self.env["stock.warehouse"]
            .sudo()
            .search(
                [
                    "|",
                    ("partner_id", "=", company.partner_id.id),
                    ("partner_id", "=", False),
                ],
                limit=1,
            )
        )

        # Get Location Stock from warehouse
        location = stock_warehouse.lot_stock_id

        now_date = fields.Datetime.now().date()
        disp_name = self.display_name

        # All variants are included in an inventory adjustment
        inv_vals = {
            "product_ids": [(6, 0, self.product_variant_ids.ids)],
            "location_ids": [(6, 0, [location.id])],
            "company_id": company.id,
            "prefill_counted_quantity": "counted",
            "name": "{}/{}/{}".format("Adjustment", disp_name, now_date),
        }

        # Inventory is created
        adjustment = self.env["stock.inventory"].create(inv_vals)

        # Returns Inventory's form view on top of the product form view
        return {
            "type": "ir.actions.act_window",
            "res_model": "stock.inventory",
            "view_type": "form",
            "view_mode": "form",
            "res_id": adjustment.id,
            "target": "new",
        }
