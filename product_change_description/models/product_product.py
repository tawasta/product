from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    change_description = fields.Text(
        string="Imported description change",
        copy=False,
        help="Description change from import",
    )
