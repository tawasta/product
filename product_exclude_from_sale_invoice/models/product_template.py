from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    exclude_from_sale_invoice = fields.Boolean(
        readonly=False,
        help="If checked, sale order lines for this product will remain on the "
        "sale order but will be skipped when creating invoices.",
    )

    # Helper to check if the user is allowed to set the exclusion manually or if
    # it's handled automatically by rules on the background
    exclude_from_sale_invoice_readonly = fields.Boolean(
        compute="_compute_exclude_from_sale_invoice_readonly",
        string="Exclusion Managed by Rules",
    )

    @api.depends_context("uid", "company")
    def _compute_exclude_from_sale_invoice_readonly(self):
        """The checkbox is readonly when at least one active exclusion rule
        exists for the current company (or with no company set)."""
        current_company = self.env.company
        has_rules = bool(
            self.env["product.sale.invoice.exclusion.rule"]
            .sudo()
            .search_count(
                [
                    ("active", "=", True),
                    "|",
                    ("company_id", "=", False),
                    ("company_id", "=", current_company.id),
                ],
                limit=1,
            )
        )
        for rec in self:
            rec.exclude_from_sale_invoice_readonly = has_rules

    @api.onchange("detailed_type", "taxes_id")
    def _onchange_check_exclusion_rules(self):
        """When product type or taxes change on the form, re-evaluate
        against active rules."""
        exclusion_rule_obj = self.env["product.sale.invoice.exclusion.rule"]
        active_rules = exclusion_rule_obj.sudo().search([("active", "=", True)])
        if not active_rules:
            return
        self.exclude_from_sale_invoice = exclusion_rule_obj._product_matches_any_rule(
            self,
            active_rules,
        )
