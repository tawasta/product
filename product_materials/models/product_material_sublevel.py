from odoo import fields, models


class ProductMaterialSublevel(models.Model):

    _name = "product.material.sublevel"
    _description = "Product Material Sublevel"

    name = fields.Char(string="Name", required=True)

    product_material_id = fields.Many2one(
        comodel_name="product.material",
        string="Parent Product Material",
        help="Parent Material of this Material Sublevel",
    )

    product_material_class_id = fields.Many2one(
        related="product_material_id.product_material_class_id",
        string="Parent Product Material Class",
        help="Parent Material of this Material Sublevel",
    )

    description = fields.Text(
        string="Material Sublevel Info",
        help="Additional info about the material sublevel",
    )
