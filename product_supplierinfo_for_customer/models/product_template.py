from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    customer_ids = fields.One2many(
        comodel_name="product.supplierinfo",
        inverse_name="product_tmpl_id",
        string="Customer",
        domain=[("type", "=", "customer")],
    )

    supplier_ids = fields.One2many(
        comodel_name="product.supplierinfo",
        inverse_name="product_tmpl_id",
        string="Supplier",
        domain=[("type", "=", "supplier")],
    )
