from odoo import fields, models


class ProductPricelistEmissions(models.Model):
    _inherit = ["product.pricelist"]

    co2_emissions = fields.Float(string="CO2 Emissions")
