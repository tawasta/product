from odoo import fields, models


class ProductMaterialWasteComponent(models.Model):

    _name = "product.material.waste.component"
    _description = "Product Material Waste Component"

    name = fields.Char(string="Name", required=True)

    product_material_waste_endpoint_id = fields.Many2one(
        comodel_name="product.material.waste.endpoint",
        string="Waste Endpoint",
        description="The endpoint this type of waste typically ends up in",
    )

    description = fields.Text(
        string="Waste Component info", help="Additional info about the waste component"
    )
