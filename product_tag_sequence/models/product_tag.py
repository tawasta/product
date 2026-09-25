from odoo import fields, models


class ProductTag(models.Model):
    _inherit = "product.tag"
    _order = "sequence, id"

    sequence = fields.Integer(
        default=1, help="Gives the sequence order for Product Tags"
    )
