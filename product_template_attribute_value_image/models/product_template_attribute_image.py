from odoo import api, fields, models


class ProductTemplateAttributeImage(models.Model):
    _name = "product.template.attribute.image"
    _description = "Product Template Attribute Image"
    _order = "sequence, id"

    name = fields.Char()
    sequence = fields.Integer(default=10)

    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        string="Product Template",
        required=True,
        ondelete="cascade",
        index=True,
    )
    product_attribute_value_id = fields.Many2one(
        comodel_name="product.attribute.value",
        string="Attribute Value",
        required=True,
        ondelete="cascade",
        help="Variants of this product template whose combination "
        "includes this attribute value (e.g. a lampshade color) will "
        "use this image.",
    )
    allowed_attribute_value_ids = fields.Many2many(
        comodel_name="product.attribute.value",
        compute="_compute_allowed_attribute_value_ids",
        help="Technical field limiting the attribute value selection to "
        "the values actually used on this product template.",
    )
    image_1920 = fields.Image(string="Image")

    _sql_constraints = [
        (
            "product_tmpl_attribute_value_uniq",
            "unique(product_tmpl_id, product_attribute_value_id)",
            "Only one image can be set per attribute value for a given "
            "product template.",
        ),
    ]

    @api.depends("product_tmpl_id")
    def _compute_allowed_attribute_value_ids(self):
        for record in self:
            record.allowed_attribute_value_ids = (
                record.product_tmpl_id.attribute_line_ids.value_ids
            )
