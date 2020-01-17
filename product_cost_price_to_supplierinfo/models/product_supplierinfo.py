from odoo import fields, models


class ProductSupplierinfo(models.Model):

    _inherit = "product.supplierinfo"

    from_cost_price = fields.Boolean(string="Created from cost price", default=False)
