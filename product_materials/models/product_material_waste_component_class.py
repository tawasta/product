from odoo import fields, models


class ProductMaterialWasteComponentClass(models.Model):

    _name = "product.material.waste.component.class"
    _description = "Product Material Waste Component Class"

    name = fields.Char(string="Name", required=True)

    description = fields.Text(
        string="Waste Component Class Info",
        help="Additional info about the waste component class",
    )
