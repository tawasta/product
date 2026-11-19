from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    change_description = fields.Text(related="product_variant_ids.change_description", readonly=False, copy=False)
