
from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    has_stock_on_several_locations = fields.Boolean(
        compute=lambda self: self._compute_stock_on_several_locations())

    @api.depends('qty_available')
    def _compute_stock_on_several_locations(self):
        for product in self:
            quants = self.env['stock.quant'].sudo().search([
                ('product_tmpl_id', '=', product.id)])

            locations = [q.location_id.id for q in quants
                         if q.location_id.usage == 'internal']

            # locations is a list, e.g. [2, 2, 3]. We count the elements
            # on this list and they are all the same element, if they
            # match to the length of the list.
            if locations and locations.count(locations[0]) != len(locations):
                product.has_stock_on_several_locations = True
            else:
                product.has_stock_on_several_locations = False
