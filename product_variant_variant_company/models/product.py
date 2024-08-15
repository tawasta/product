from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    variant_company_id = fields.Many2one(
        "res.company", string="Variant Company", store=True, readonly=False
    )

    @api.model
    def create(self, values):
        company = values.get("company_id", False)
        if company:
            values["variant_company_id"] = company

        return super().create(values)
