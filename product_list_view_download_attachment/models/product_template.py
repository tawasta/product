
from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    def download_attachment(self):
        for product in self:

            attach = self.env['ir.attachment'].search([
                ('res_model', '=',  'product.template'),
                ('res_id', '=', product.id),
            ])

            if attach:
                return {
                    "type": "ir.actions.act_url",
                    "url": "/web/content/{}?download=true".format(
                        attach.id
                    ),
                    "target": "self",
                }
