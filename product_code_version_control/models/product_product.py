
from odoo import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    version_code_ids = fields.One2many('product.code.version', 'product_id', string="Code versions", copy=False)
    version_code_count = fields.Integer(string="Version code Count", compute='_compute_product_version_code_count')

    def _compute_product_version_code_count(self):
        for product in self:
            product.version_code_count = product.env['product.code.version'].search_count([
                '|',
                    ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('product_id', '=', product.id),
            ])

    @api.model
    @api.readonly
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        print("NAME SEARCH name", name)
        print("NAME SEARCH args", args)
        print("NAME SEARCH operator", operator)
        print("NAME SEARCH limit", limit)

        codes = ['version_code_ids', 'ilike', name]
        args.append(codes)
        args.insert(0, '|')

        print("NAME SEARCH ARGS", args)

        args = [codes]

        res = super().name_search(name=name, args=args, operator=operator, limit=limit)


        return res

    @api.model
    def _search_display_name(self, operator, value):
        res = super()._search_display_name(operator=operator, value=value)

        search_fnames = self._rec_names_search or ([self._rec_name] if self._rec_name else [])

        print("------------------------------------")
        print("DISPLAY NAME SEARCH", res)
        print("DISPLAY NAME OPERATOR", operator)
        print("DISPLAY NAME VALUE", value)
        print("SEARCH FNAMES", search_fnames)
        print("DISPLAY NAME SEARCH RES NAMES", self._rec_names_search)
        print("------------------------------------")

        codes = ('version_code_ids', 'ilike', value)
        res.append(codes)
        res.insert(0, '|')

        print("DISPLAY NAME SEARCH AGAIN", res)

        #return [('name', '!=', False)]
        return res

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):

        print("SEARCH DOMAIN", domain)

        return super().search(domain=domain, offset=offset, limit=limit, order=order)

    def action_open_version_codes(self):
        res = self.product_tmpl_id.action_open_version_codes()

        res['context'].update({
            'default_product_tmpl_id': self.product_tmpl_id.id,
            'default_product_id': self.id,
        })
        return res
