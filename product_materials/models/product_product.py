from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    material = fields.Many2many(
        comodel_name="product.material",
        related="product_tmpl_id.material",
        string="Material",
    )
    material_purchase = fields.Many2many(
        related="product_tmpl_id.material_purchase", string="Material"
    )
