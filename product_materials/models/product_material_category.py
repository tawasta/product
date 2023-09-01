from odoo import fields, models


class ProductMaterialCategory(models.Model):

    _name = "product.material.category"
    _description = "Product Material Category"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
