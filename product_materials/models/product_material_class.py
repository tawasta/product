from odoo import fields, models


class ProductMaterialClass(models.Model):
    _name = "product.material.class"
    _description = "Product Material Class"

    name = fields.Char(required=True)

    description = fields.Text(
        string="Material Class Info", help="Additional info about the material class"
    )
