from odoo import _, api, fields, models


class ProductSaleInvoiceExclusionRule(models.Model):
    _name = "product.sale.invoice.exclusion.rule"
    _description = "Product Sale Invoice Exclusion Rule"
    _order = "sequence, id"
    _rec_name = "name"

    name = fields.Char(compute="_compute_name")
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    detailed_type = fields.Selection(
        selection="_get_detailed_type_selection",
        string="Product Type",
        required=True,
    )
    tax_ids = fields.Many2many(
        comodel_name="account.tax",
        string="Customer Taxes",
        domain=[("type_tax_use", "=", "sale")],
        required=True,
        help="Note that if you add multiple taxes, the rule will match only those "
        "products that have all of the same taxes set.",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
    )

    @api.depends("detailed_type", "tax_ids")
    def _compute_name(self):
        # fields_get returns translated labels for the current user's language
        type_labels = dict(
            self.env["product.template"].fields_get(["detailed_type"])["detailed_type"][
                "selection"
            ]
        )
        for rule in self:
            type_label = type_labels.get(rule.detailed_type, rule.detailed_type or "")
            tax_names = ", ".join(rule.tax_ids.mapped("name")) or _("No taxes")
            rule.name = f"{type_label} / {tax_names}" if type_label else tax_names

    @api.model
    def _get_detailed_type_selection(self):
        """Pull selection values dynamically from product.template so that
        values added by other modules (e.g. event, rental) are included,
        and labels are returned in the current user's language."""
        return self.env["product.template"].fields_get(["detailed_type"])[
            "detailed_type"
        ]["selection"]

    # In CRUD operations re-evaluate all products when rules change
    @api.model_create_multi
    def create(self, vals_list):
        rules = super().create(vals_list)
        self._reevaluate_all_products()
        return rules

    def write(self, vals):
        res = super().write(vals)
        self._reevaluate_all_products()
        return res

    def unlink(self):
        res = super().unlink()
        self._reevaluate_all_products()
        return res

    def _reevaluate_all_products(self):
        """Re-evaluate 'exclude_from_sale_invoice' field of every product template
        against the current set of active rules."""
        active_rules = self.sudo().search([("active", "=", True)])
        products = self.env["product.template"].sudo().search([])
        for product in products:
            product.exclude_from_sale_invoice = self._product_matches_any_rule(
                product,
                active_rules,
            )

    @api.model
    def _product_matches_any_rule(self, product, rules):
        """Return True if the product matches at least one rule.
        Match = same detailed_type AND exact same set of customer tax ids
        AND rule company is either empty or matches the product's company."""
        product_tax_ids = set(product.taxes_id.ids)
        product_company = product.company_id
        for rule in rules:
            if rule.company_id and rule.company_id != product_company:
                continue
            if (
                rule.detailed_type == product.detailed_type
                and set(rule.tax_ids.ids) == product_tax_ids
            ):
                return True
        return False
