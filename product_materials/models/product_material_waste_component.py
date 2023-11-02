from odoo import fields, models


class ProductMaterialWasteComponent(models.Model):

    _name = "product.material.waste.component"
    _description = "Product Material Waste Component"

    name = fields.Char(string="Name", required=True)

    product_material_waste_component_class = fields.Many2one(
        comodel_name="product.material.waste.component.class",
        string="Waste Component Class",
    )

    description = fields.Text(
        string="Waste Component info", help="Additional info about the waste component"
    )
