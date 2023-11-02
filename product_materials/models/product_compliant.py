from odoo import fields, models


class ProductCompliant(models.Model):

    _inherit = "product.compliant"

    # Add compliances that are tracked at product material composition level
    selectable_for = fields.Selection(
        selection_add=[
            ("conflict_area_minerals", "Conflict Area Minerals Compliant"),
            ("halogens", "Halogen Free Compliant"),
            ("packaging_materials", "Packaging Materials Checked"),
        ]
    )
