from odoo import fields, models


class ProductMaterial(models.Model):

    _name = "product.material"
    _description = "Product Material"

    name = fields.Char(string="Name", required=True, translate=True)

    product_material_class_id = fields.Many2one(
        comodel_name="product.material.class",
        string="Parent Product Material Class",
        help="Parent Material Class of this Material",
    )

    product_material_waste_component_id = fields.Many2one(
        comodel_name="product.material.waste.component",
        string="Waste Component",
        help="The Waste Component that typically results from this material",
    )

    is_product_material = fields.Boolean(
        string="Is a Material for Products",
        help="Check this box if you want this material to be selectable "
        "as a material for products",
    )

    is_product_packaging_material = fields.Boolean(
        string="Is a Material for Product Packaging",
        help="Check this box if you want this material to be selectable "
        "as a material for products' packaging",
    )

    description = fields.Text(
        string="Material info", help="Additional info about the material"
    )

    biogenic_material_weight_percentage = fields.Float(
        string="Biogenic material weight-%"
    )

    renewable_weight_percentage = fields.Float(string="Renewable weight-%")
