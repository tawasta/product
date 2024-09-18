from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends("customer_ids", "customer_ids.product_code")
    def _compute_customer_codes(self):
        for record in self:
            record.customer_codes = (
                ", ".join(
                    [
                        customer.product_code
                        for customer in record.customer_ids
                        if customer.product_code
                    ]
                )
                or ""
            )

    customer_codes = fields.Char(
        compute="_compute_customer_codes", string="Customer Codes", store=True
    )
