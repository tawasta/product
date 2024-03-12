from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic account",
        related="product_tmpl_id.analytic_account_id",
    )
