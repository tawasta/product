from odoo import fields, models


class ProductMaterialComposition(models.Model):

    _inherit = "product.material.composition"

    product_material_upper_category_id = fields.Many2one(
        "product.material.upper.category", string="Upper category"
    )
