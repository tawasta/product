from odoo import fields
from odoo import models


class PricelistItem(models.Model):

    _inherit = "product.pricelist.item"

    product_tmpl_id = fields.Many2one(check_company=False)
    product_id = fields.Many2one(check_company=False)
