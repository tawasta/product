from odoo import models, fields

class ProductCompliant(models.Model):
    _name = 'product.compliant'
    _description = 'Product Compliant'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
