from odoo import fields, models


class ProductMaterial(models.Model):

    _name = "product.material"
    _description = "Product Material"

    name = fields.Char(string="Name", required=True)

    product_material_class = fields.Many2one(
        comodel_name="product.material.class", string="Product Material Class"
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
