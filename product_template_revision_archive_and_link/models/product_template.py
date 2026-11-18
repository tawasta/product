import logging
import re
from collections import defaultdict

from odoo import Command, api, fields, models
from odoo.tools import str2bool

_logger = logging.getLogger(__name__)

# "DEV" and "0" come before the first revision, then 1-9 or A-ZZ.
# An optional numeric sub revision follows a dot, e.g. "A.001".
REVISION_PATTERN = re.compile(r"^(DEV|[0-9]|[A-Z]{1,2})(?:\.([0-9]*))?$")


def _revision_rank(revision):
    """Return a sortable rank for the revision, or None if it is not one"""
    match = REVISION_PATTERN.match(revision)
    if not match:
        return None
    main, sub = match.groups()
    if main in ("DEV", "0"):
        rank = 0
    elif main.isdigit():
        rank = int(main)
    else:
        # A=1 ... Z=26, AA=27 ... ZZ=702
        rank = 0
        for letter in main:
            rank = rank * 26 + ord(letter) - ord("A") + 1
    return rank, int(sub or 0)


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
        copy=False,
        index="btree_not_null",
    )
    revision_product_tmpl_count = fields.Integer(
        string="Revision Count", compute="_compute_revision_product_tmpl_count"
    )

    @api.depends("revision_product_tmpl_ids")
    def _compute_revision_product_tmpl_count(self):
        for template in self:
            template.revision_product_tmpl_count = len(
                template.revision_product_tmpl_ids
            )

    def action_open_revision_products(self):
        self.ensure_one()
        return {
            "name": self.env._("Revisions"),
            "type": "ir.actions.act_window",
            "res_model": "product.template",
            "view_mode": "list,form,kanban",
            "domain": [
                ("id", "in", self.revision_product_tmpl_ids.ids),
                ("active", "in", [True, False]),
            ],
            "target": "current",
        }

    @api.model
    def archive_old_revision_product(self):
        """Archive the old revisions and link them to the newest revision"""
        for code, revisions in self._get_revision_groups().items():
            # One failing product must not stop the archiving of the others
            try:
                with self.env.cr.savepoint():
                    self._archive_old_revisions(revisions)
            except Exception:
                _logger.exception("Old revisions of code %s were not archived", code)

    @api.model
    def _get_revision_groups(self):
        """Return {code: [(rank, template)]} of codes with several revisions"""
        # The settings are readable only by administrators
        icp = self.env["ir.config_parameter"].sudo()
        code_length = int(float(icp.get_param("archive_code_len") or 0))
        code_is_digit = str2bool(icp.get_param("code_is_digit") or "0")

        templates = self.with_context(active_test=False).search_fetch(
            [("default_code", "like", " ")],
            ["default_code", "active", "product_tmpl_revision_id"],
        )
        groups = defaultdict(list)
        for template in templates:
            parts = template.default_code.split()
            if len(parts) != 2:
                continue
            code, revision = parts
            if code_length and len(code) != code_length:
                continue
            if code_is_digit and not code.isdigit():
                continue
            rank = _revision_rank(revision)
            if rank is not None:
                groups[code].append((rank, template))
        return {code: revs for code, revs in groups.items() if len(revs) > 1}

    @api.model
    def _archive_old_revisions(self, revisions):
        revisions.sort(key=lambda revision: revision[0], reverse=True)
        (newest_rank, newest), (previous_rank, previous) = revisions[:2]
        if newest_rank == previous_rank:
            _logger.warning(
                "Old revisions of %s were not archived: the newest revision "
                "is not unique",
                newest.default_code,
            )
            return

        old_revisions = self.browse([template.id for _rank, template in revisions[1:]])
        if not old_revisions.filtered(
            lambda template: template.active
            or template.product_tmpl_revision_id != newest
        ):
            return

        # Copy the prices only once, so that later price changes are kept
        if previous.product_tmpl_revision_id != newest:
            self._copy_revision_supplierinfo(previous, newest)
        to_archive = old_revisions.filtered("active")
        to_archive.write({"active": False})
        newest.revision_product_tmpl_ids = [Command.set(old_revisions.ids)]
        if to_archive:
            _logger.info(
                "These products have been automatically archived: %s", to_archive.ids
            )

    @api.model
    def _copy_revision_supplierinfo(self, previous, newest):
        supplierinfo_model = self.env["product.supplierinfo"]
        newest_supplierinfos = supplierinfo_model.search(
            [("product_tmpl_id", "=", newest.id)]
        )
        seen = {(s.partner_id, s.price, s.min_qty) for s in newest_supplierinfos}
        to_copy = supplierinfo_model
        for supplierinfo in supplierinfo_model.search(
            [("product_tmpl_id", "=", previous.id)]
        ):
            key = (supplierinfo.partner_id, supplierinfo.price, supplierinfo.min_qty)
            if key not in seen:
                seen.add(key)
                to_copy |= supplierinfo
        # The variant of the old revision would hide the price from the newest
        to_copy.copy({"product_tmpl_id": newest.id, "product_id": False})
