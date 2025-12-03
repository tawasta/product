from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    number_of_users_min = fields.Integer(
        string="Number of Users (min.)",
        help="How many persons can use this product at the same time",
    )

    number_of_users_max = fields.Integer(
        string="Number of Users (max.)",
        help="How many persons can use this product at the same time",
    )
