from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic account",
        domain=[("product_ids", "=", False)],
        copy=False,
    )
