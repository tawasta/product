from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    material = fields.Many2one("product.material", string="Material")
