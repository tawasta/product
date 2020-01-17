from odoo import _, api, fields, models
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    quality_check_ids = fields.One2many(
        "product_quality_instruction_i_s.check",
        "picking_id",
        string="Quality Checks",
        readonly=False,
        states={"cancel": [("readonly", True)], "done": [("readonly", True)]},
    )

    quality_check_count = fields.Integer(
        compute="_compute_quality_check_count", string="Quality Check Count", store=True
    )

    @api.depends("quality_check_ids")
    def _compute_quality_check_count(self):
        for picking in self:
            picking.quality_check_count = len(picking.quality_check_ids)

    @api.model
    def create(self, vals):
        # When an incoming picking is created from scratch,
        # create the quality checklist
        res = super(StockPicking, self).create(vals)
        if res.picking_type_code == "incoming":
            res.initialize_quality_checks()
        return res

    @api.multi
    def button_validate(self):
        # When clicking the Validate button, raise an exception if any
        # of the quality checks are incomplete
        for p in self:
            if [check for check in p.quality_check_ids if not check.completed]:
                raise UserError(
                    _(
                        "Please finish the quality check list "
                        "before receiving the goods."
                    )
                )

        return super(StockPicking, self).button_validate()

    @api.multi
    def initialize_quality_checks(self):
        # Go through all unique products that appear on the picking lines.
        # Find their quality instructions and add them to the list.
        self.ensure_one()

        quality_check_model = self.env["product_quality_instruction_i_s.check"]
        self.quality_check_ids = False

        incoming_products = list({move.product_id for move in self.move_lines})

        for product in incoming_products:
            for quality_instruction in product.product_tmpl_id.quality_instruction_ids:
                quality_check_model.create(
                    {
                        "instruction_id": quality_instruction.id,
                        "product_id": product.id,
                        "picking_id": self.id,
                    }
                )

    @api.multi
    def _create_backorder(self, backorder_moves=[]):
        # When an incoming picking is created as a backorder
        # from another picking, create the quality checklist

        res = super(StockPicking, self)._create_backorder(backorder_moves)

        res.initialize_quality_checks()

        return res
