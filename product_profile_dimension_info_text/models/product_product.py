from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    profile_info_type = fields.Char(related="product_tmpl_id.profile_info_type")
    dimension_text = fields.Text(related="product_tmpl_id.dimension_text")
