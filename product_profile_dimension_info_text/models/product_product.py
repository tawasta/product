from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    profile_info_type = fields.Char(copy=False)
    dimension_text = fields.Text(string="Dimensions info", copy=False)
