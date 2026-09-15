from odoo import fields, models


class ProductTemplateEmissions(models.Model):
    _inherit = ["product.template"]

    co2_emissions = fields.Float(string="CO2 Emissions")
