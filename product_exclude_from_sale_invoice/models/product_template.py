from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    exclude_from_sale_invoice = fields.Boolean(
        compute="_compute_exclude_from_sale_invoice",
        store=True,
        help="If checked, sale order lines for this product will remain on the "
        "sale order but will be skipped when creating invoices.",
    )

    @api.depends("detailed_type", "taxes_id", "company_id")
    def _compute_exclude_from_sale_invoice(self):
        """Evaluate the product against active exclusion rules. Rule changes
        trigger the recomputation from the rule model."""
        exclusion_rule_obj = self.env["product.sale.invoice.exclusion.rule"].sudo()
        active_rules = exclusion_rule_obj.search([("active", "=", True)])
        for product in self:
            product.exclude_from_sale_invoice = (
                exclusion_rule_obj._product_matches_any_rule(product, active_rules)
            )
