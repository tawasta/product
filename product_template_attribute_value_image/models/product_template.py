from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    attribute_image_ids = fields.One2many(
        comodel_name="product.template.attribute.image",
        inverse_name="product_tmpl_id",
        string="Attribute Images",
    )
