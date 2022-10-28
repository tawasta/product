from odoo import api, fields, models


class QualityCheck(models.Model):
    _name = "product_quality_instruction_i_s.check"
    _description = "Instruction for incoming shipments"
    _rec_name = "instruction_id"
    _RESULT_TYPES = [
        ("pass", "Passed"),
        ("fail", "Failed"),
        ("not_received", "Not Received"),
    ]

    instruction_id = fields.Many2one(
        comodel_name="product_quality_instruction.instruction",
        string="Instruction",
        required=True,
        ondelete="restrict",
    )
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product", required=True
    )
    completed = fields.Boolean()
    user_id = fields.Many2one(comodel_name="res.users", string="Completed by")
    picking_id = fields.Many2one(comodel_name="stock.picking", string="Receipt")
    comments = fields.Char()
    result = fields.Selection(_RESULT_TYPES)

    @api.onchange("completed")
    def onchange_completed(self):
        # When Completed checkbox is checked,
        # suggest current user for the Completed By field
        if not self.completed:
            self.user_id = False
        else:
            self.user_id = self.env.uid
