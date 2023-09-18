from odoo import fields, models


class ProductPricelist(models.Model):

    _inherit = "product.pricelist"

    partner_ids = fields.One2many(
        string="Partners using this pricelist",
        comodel_name="res.partner",
        inverse_name="property_product_pricelist",
    )
