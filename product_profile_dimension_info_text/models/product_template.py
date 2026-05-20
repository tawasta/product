from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    profile_info_type = fields.Char(copy=False)
    dimension_text = fields.Text(string="Dimensions info", copy=False)
