
from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    version_code_ids = fields.One2many('product.code.version', 'product_tmpl_id', string="Code versions", copy=False)
    version_code_count = fields.Integer(string="Version code Count", compute='_compute_product_version_code_count')

    def _compute_product_version_code_count(self):
        for template in self:
            template.version_code_count = template.env['product.code.version'].search_count([
                '|',
                    ('product_tmpl_id', '=', template.id),
                    ('product_id', 'in', template.product_variant_ids.ids),
            ])

    def action_open_version_codes(self):
        self.ensure_one()
        return {
            'name': self.env._('Version Codes'),
            'type': 'ir.actions.act_window',
            'res_model': 'product.code.version',
            'view_mode': 'list,form,kanban',
#            'view_mode': 'list,form',
            'context': {
                'default_product_tmpl_id': self.id,
                'default_product_id': (self.env.user.has_group('product.group_product_variant') and self.product_variant_ids.ids[0] or False),
#                'search_default_context_variant': 1,,
#                'default_product_tmpl_id': self._context.get('active_id'),
            },
            'domain': [
                '|',
                    ('product_tmpl_id', '=', self.id),
                    ('product_id', 'in', self.product_variant_ids.ids),
            ],
            'target': 'current',
        }
