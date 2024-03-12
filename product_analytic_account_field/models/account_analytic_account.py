from odoo import fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    product_ids = fields.One2many(
        comodel_name="product.template",
        inverse_name="analytic_account_id",
        copy=False,
    )
