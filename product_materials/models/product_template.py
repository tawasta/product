from odoo import fields, models

PRODUCT_DOMAIN = "[('category.code', '=', 'product')]"
PURCHASE_DOMAIN = "[('category.code', '=', 'purchase')]"


class ProductTemplate(models.Model):

    _inherit = "product.template"

    material = fields.Many2many(
        "product.material", string="Material", domain=PRODUCT_DOMAIN
    )

    material_purchase = fields.Many2many(
        comodel_name="product.material",
        relation="rel_purchase_material",
        string="Material",
        domain=PURCHASE_DOMAIN,
    )

    material_purchase_text = fields.Char(string="Material text")
