from odoo import fields, models


class ProductCompliant(models.Model):

    _name = "product.compliant"
    _description = "Product Compliant"

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")

    selectable_for = fields.Selection(
        string="Selectable For",
        selection=[
            ("atex", "ATEX Compliant"),
            ("reach", "REACH Compliant"),
            ("rohs", " RoHS Compliant"),
            ("composition", "Composition Checked"),
            ("msds", "MSDS (Material Safety Data Sheet) Checked"),
            ("work_safety", "Work Safety Checked"),
        ],
        help="When left empty, the value can be used for any of the Product Compliance. "
        "A selection can be made if the compliance term is specific to e.g. just REACH "
        "and should not be available for others.",
    )
