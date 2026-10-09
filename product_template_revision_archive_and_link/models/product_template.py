import logging

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    revision_product_tmpl_ids = fields.One2many(
        "product.template",
        "product_tmpl_revision_id",
        string="Code revisions",
        copy=False,
        context={"active_test": False},
    )

    product_tmpl_revision_id = fields.Many2one(
        "product.template",
        string="Recent product revision",
    )

    revision_product_tmpl_count = fields.Integer(
        string="Revision Count", compute="_compute_revision_product_tmpl_count"
    )

    def _compute_revision_product_tmpl_count(self):
        for template in self:
            if template.revision_product_tmpl_ids:
                template.revision_product_tmpl_count = len(
                    template.with_context(
                        active_test=False
                    ).revision_product_tmpl_ids.ids
                )
            else:
                template.revision_product_tmpl_count = 0

    def archive_old_revision_product(self):
        all_product_tmpl_ids = self.env["product.template"].search(
            [
                "|",
                ("active", "=", True),
                ("active", "=", False),
            ]
        )

        code_group = {}

        for product in all_product_tmpl_ids:
            if product.default_code:
                split_values = product.default_code.split()
                if len(split_values) == 2:
                    code, revision = split_values
                    if (
                        len(code) == 5
                        and code.isdigit()
                        and not revision.isnumeric()
                        and len(revision) == 1
                    ):
                        code_group[code] = [revision] + code_group.get(code, [])
                        code_group[code].sort(reverse=True)

        for code in code_group:
            archived_products = self.env["product.template"]

            if len(code_group[code]) > 1:
                active_product = code_group[code].pop(0)

                active_default_code = f"{code} {active_product}"
                active_product_id = (
                    self.env["product.template"]
                    .with_context(active_test=False)
                    .search([("default_code", "=", active_default_code)])
                )

                old_products = False

                for rev in code_group[code]:
                    default_code = f"{code} {rev}"
                    old_products = self.env["product.template"].search(
                        [
                            "|",
                            ("active", "=", True),
                            ("active", "=", False),
                            ("default_code", "=", default_code),
                        ]
                    )

                    if old_products:
                        old_products.active = False
                        archived_products |= old_products

                if archived_products:
                    supplier_pricelists_to_copy = self.env[
                        "product.supplierinfo"
                    ].search([("product_tmpl_id", "=", archived_products[0].id)])

                    pricelists = []
                    deduplicate_vendor_pricelists = self.env["product.supplierinfo"]

                    active_product_pricelists = self.env["product.supplierinfo"].search(
                        [("product_tmpl_id", "=", active_product_id.id)]
                    )

                    if active_product_pricelists:
                        active_values = [
                            (s.partner_id, s.price, s.min_qty)
                            for s in active_product_pricelists
                        ]
                    else:
                        active_values = []

                    if supplier_pricelists_to_copy:
                        for sup_pricelist in supplier_pricelists_to_copy:
                            if (
                                sup_pricelist.partner_id,
                                sup_pricelist.price,
                                sup_pricelist.min_qty,
                            ) not in pricelists + active_values:
                                pricelists.append(
                                    (
                                        sup_pricelist.partner_id,
                                        sup_pricelist.price,
                                        sup_pricelist.min_qty,
                                    )
                                )
                                deduplicate_vendor_pricelists |= sup_pricelist

                        if deduplicate_vendor_pricelists:
                            copied_pricelists = deduplicate_vendor_pricelists.copy()
                            copied_pricelists.write(
                                {"product_tmpl_id": active_product_id.id}
                            )

                    active_product_id.write(
                        {"revision_product_tmpl_ids": [(6, 0, archived_products.ids)]}
                    )
                    _logger.info(
                        "These products have been automatically archived: {}".format(
                            archived_products.ids
                        )
                    )

    def action_open_revision_products(self):
        self.ensure_one()
        return {
            "name": _("Revisions"),
            "type": "ir.actions.act_window",
            "res_model": "product.template",
            "view_mode": "tree,form,kanban",
            "domain": [
                ("active", "=", False),
                ("id", "in", self.revision_product_tmpl_ids.ids),
            ],
            "target": "current",
        }
