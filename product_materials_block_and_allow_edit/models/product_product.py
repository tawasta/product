from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    allow_material_edit = fields.Boolean(
        string="Allow editing materials",
        copy=False,
        help="""Editing materials is enabled for this product if this
                field is active.""",
    )
