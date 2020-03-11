from odoo import api
from odoo import models
from odoo import fields


class ProductTemplate(models.Model):

    _inherit = "product.template"

    duplicate_product_ids = fields.Many2many(
        comodel_name='product.template',
        string='Duplicates',
        compute='_compute_duplicate_product_ids',
    )

    dismiss_duplicates = fields.Boolean(
        string='Dismiss duplicates warning',
        default=False,
        help='Hide duplicate warning'
    )

    @api.onchange('name')
    @api.depends('name')
    def _compute_duplicate_product_ids(self):
        for record in self:
            if record.name and len(record.name) < 5:
                # Don't try to match very short names, as they will probably
                # result in many false positive matches
                continue

            # Search for similar products
            domain = [('name', 'ilike', record.name)]

            if not isinstance(record.id, models.NewId):
                domain.append(('id', '!=', record.id))
            duplicate_product_ids = self.search(domain)

            if duplicate_product_ids:
                record.dismiss_duplicates = False
                record.duplicate_product_ids = duplicate_product_ids
