from odoo import models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    def _get_aggregated_product_quantities(self, **kwargs):
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)

        for aggregated_move_line in aggregated_move_lines:

            move_id = aggregated_move_lines[aggregated_move_line].get("move", False)
            materials = move_id.product_id.product_material_composition_ids.product_material_id
            show_materials = move_id.sale_line_id.order_id.show_materials_with_report

            aggregated_move_lines[aggregated_move_line]["materials"] = materials
            aggregated_move_lines[aggregated_move_line]["show_materials"] = show_materials

        return aggregated_move_lines
