from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _create_picking(self):
        # When a receipt is created from a PO,
        # create the quality checklist
        res = super()._create_picking()
        for record in self:
            for picking in record.picking_ids:
                if picking.picking_type_code != "incoming":
                    # Only match Receipts
                    continue
                picking.initialize_quality_checks()
        return res
