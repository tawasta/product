from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_storable = fields.Boolean(default=True)

    @api.depends('type')
    def compute_is_storable(self):
        """Re-check if the set product type is Goods and track its
        inventory in this case."""
        super().compute_is_storable()
        self.filtered(lambda t: t.type == 'consu').is_storable = True
