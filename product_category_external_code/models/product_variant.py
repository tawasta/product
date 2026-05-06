from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    external_code = fields.Char(
        string="External Code",
        related="categ_id.external_code",
        store=True,
        readonly=True,
        copy=False,
    )
