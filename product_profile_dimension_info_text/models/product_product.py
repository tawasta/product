from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    profile_info_type = fields.Char(copy=False)
    profile_info_text = fields.Text(copy=False)
