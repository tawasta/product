from odoo import api, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    @api.model
    def create(self, values):

        return super(ProductTemplate, self).create(values)

    @api.multi
    def write(self, values):

        for record in self:
            if 'weight' in values:
                record.product_variant_ids.write({'weight': values['weight']})

            if 'volume' in values:
                record.product_variant_ids.write({'volume': values['volume']})

        return super(ProductTemplate, self).write(values)
