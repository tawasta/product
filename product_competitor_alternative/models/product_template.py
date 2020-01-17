from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    competitor_alternative = fields.Char(
        string="Competitor's Alternative",
        help="Info about a similar product sold by a competitor",
    )
