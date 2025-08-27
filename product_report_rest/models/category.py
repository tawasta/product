from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    is_secondary = fields.Boolean(default=False)
