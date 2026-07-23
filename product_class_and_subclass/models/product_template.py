from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_class = fields.Char(
        string="Class", store=True, copy=False, help="Assigned class of a product"
    )

    product_subclass = fields.Char(
        string="Subclass", store=True, copy=False, help="Assigned subclass of a product"
    )

    product_secondary_subclass = fields.Char(
        string="Secondary Subclass",
        store=True,
        copy=False,
        help="Assigned secondary subclass of a product",
    )
