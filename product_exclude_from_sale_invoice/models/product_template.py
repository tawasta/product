from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    exclude_from_sale_invoice = fields.Boolean(
        readonly=False,
        help="If checked, sale order lines for this product will remain on the "
        "sale order but will be skipped when creating invoices.",
    )
