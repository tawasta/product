from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    cn8_code = fields.Char(string="CN8 code", related="product_variant_ids.cn8_code")
