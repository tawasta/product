from odoo import fields, models


class ProductMassUpdateTaxes(models.TransientModel):
    _name = "product.mass.update.taxes"
    _description = "Mass update product taxes"

    taxes_id = fields.Many2many(
        "account.tax",
        "product_mass_update_taxes_rel",
        "prod_id",
        "tax_id",
        help="Default taxes used when selling the product.",
        string="Customer Taxes",
        domain=[("type_tax_use", "=", "sale")],
        default=lambda self: self.env.company.account_sale_tax_id,
    )
    supplier_taxes_id = fields.Many2many(
        "account.tax",
        "product_supplier_mass_update_taxes_rel",
        "prod_id",
        "tax_id",
        string="Vendor Taxes",
        help="Default taxes used when buying the product.",
        domain=[("type_tax_use", "=", "purchase")],
        default=lambda self: self.env.company.account_purchase_tax_id,
    )

    def confirm(self):
        products = self.env["product.template"].browse(self._context.get("active_ids"))

        values = {}
        if self.taxes_id:
            values["taxes_id"] = self.taxes_id

        if self.supplier_taxes_id:
            values["supplier_taxes_id"] = self.supplier_taxes_id

        products.write(values)
