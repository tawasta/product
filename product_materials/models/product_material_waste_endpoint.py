from odoo import fields, models


class ProductMaterialWasteEndpoint(models.Model):

    _name = "product.material.waste.endpoint"
    _description = "Product Material Waste Endpoint"

    name = fields.Char(string="Name", required=True)

    description = fields.Text(
        string="Waste Endpoint Info",
        help="Additional info about the waste endpoint",
    )
