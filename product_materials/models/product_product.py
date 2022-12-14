from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    material = fields.Many2one("product.material", string="Material")
