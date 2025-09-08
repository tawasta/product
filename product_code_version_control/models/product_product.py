
from odoo import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    version_code_ids = fields.One2many(
        'product.code.version',
        'product_id',
        string="Code versions",
        copy=False
    )
    version_code_count = fields.Integer(
        string="Version code Count",
        compute='_compute_product_version_code_count'
    )

    def _compute_product_version_code_count(self):
        for product in self:
            product.version_code_count = product.env['product.code.version'].search_count([
                '|',
                    ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('product_id', '=', product.id),
            ])

    @api.model
    def _search_display_name(self, operator, value):
        res = super()._search_display_name(operator=operator, value=value)

        codes = ('version_code_ids', 'ilike', value)
        res.append(codes)
        res.insert(0, '|')

        return res

    def action_open_version_codes(self):
        res = self.product_tmpl_id.action_open_version_codes()

        res['context'].update({
            'default_product_tmpl_id': self.product_tmpl_id.id,
            'default_product_id': self.id,
        })
        return res
