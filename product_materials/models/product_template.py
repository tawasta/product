from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    material = fields.Many2many("product.material", string="Material")

    material_purchase = fields.Many2many(comodel_name="product.material", relation="rel_purchase_material", string="Material")
