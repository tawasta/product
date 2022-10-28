from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_picking_create(self):
        # When an incoming picking is created from a PO,
        # create the quality checklist
        res = super(PurchaseOrder, self).action_picking_create()
        res.initialize_quality_checks()
        return res
