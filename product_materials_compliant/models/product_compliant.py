from odoo import fields, models


class ProductCompliant(models.Model):

    _inherit = "product.compliant"

    # Add new compliances to the list that is originally provided by
    # the product_compliant modules. Note that REACH+ROHS don't need to
    # be added since they are already provided by product_compliant

    selectable_for = fields.Selection(
        selection_add=[
            ("chemicals", "Chemicals Compliant"),
            ("conflict_area_minerals", "Conflict Area Minerals Compliant"),
            ("halogens", "Halogen Compliant"),
            ("pop", "POP (Persistent Organic Pollutants) Compliant"),
            ("scip", "SCIP (Substances of Concern in Products) Compliant"),
        ]
    )
