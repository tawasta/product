from odoo import models
import logging

class StockMoveLine(models.Model):

    _inherit = "stock.move.line"

    def _get_aggregated_product_quantities(self, **kwargs):
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for move_line in self:
            name = move_line.product_id.display_name
            description = move_line.move_id.description_picking
            if description == name or description == move_line.product_id.name:
                description = False
            uom = move_line.product_uom_id
            line_key = (
                str(move_line.product_id.id)
                + "_"
                + name
                + (description or "")
                + "uom "
                + str(uom.id)
            )

            materials = self.env["product.material"].sudo().search([
                ('id', 'in', move_line.move_id.product_id.material.ids)
            ])
            logging.info("=====MATERIALS======");
            logging.info(materials);
            if line_key in aggregated_move_lines:
                aggregated_move_lines[line_key]["materials"] = materials

        return aggregated_move_lines
