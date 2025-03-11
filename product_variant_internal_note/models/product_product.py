from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    internal_note = fields.Text(string="Variant Notes", copy=False)
