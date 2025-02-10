from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(default='product',)
