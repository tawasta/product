from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    material = fields.Many2many("product.material", string="Material")
