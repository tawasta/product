from odoo import api, fields, models


class ProductUom(models.Model):

    _inherit = "uom.uom"

    reference_unit_id = fields.Many2one(
        string="Reference unit",
        comodel_name="uom.uom",
        compute="_compute_reference_unit_id",
    )

    factor_example = fields.Char(string="Example 1", compute="_compute_factor_example")

    factor_example_inverse = fields.Char(
        string="Example 2", compute="_compute_factor_example"
    )

    @api.onchange("category_id")
    @api.depends("category_id")
    def _compute_reference_unit_id(self):
        ProductUom = self.env["uom.uom"]

        for record in self:
            record.reference_unit_id = ProductUom.search(
                [
                    ("category_id", "=", record.category_id.id),
                    ("uom_type", "=", "reference"),
                ],
                limit=1,
            )

    @api.onchange("factor")
    @api.depends("factor")
    def _compute_factor_example(self):
        for record in self:
            example = ""
            example_inverse = ""

            example = "1 * {} = {} * {}".format(
                record.reference_unit_id.name,
                record.reference_unit_id._compute_quantity(1, record),
                record.name,
            )

            example_inverse = "1 * {} = {} * {}".format(
                record.name,
                record._compute_quantity(1, record.reference_unit_id),
                record.reference_unit_id.name,
            )

            if record.uom_type == "smaller":
                # Swap examples
                example, example_inverse = example_inverse, example

            record.factor_example = example
            record.factor_example_inverse = example_inverse
