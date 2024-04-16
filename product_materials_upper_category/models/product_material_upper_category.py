from odoo import fields, models


class ProductMaterialUpperCategory(models.Model):

    _name = "product.material.upper.category"
    _description = "Product Material Upper Category"

    name = fields.Char(string="Category name")

    product_material_composition_ids = fields.One2many(
        "product.material.composition",
        "product_material_upper_category_id",
        string="Product Material compositions",
    )
