from odoo import fields, models


class ProductMaterial(models.Model):

    _name = "product.material"
    _description = "Product Material"

    name = fields.Char(string="Name")
    material_info = fields.Text(string="Material info")

    category = fields.Many2many(
        string="Category", comodel_name="product.material.category"
    )
