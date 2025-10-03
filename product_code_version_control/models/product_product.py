from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    version_code_ids = fields.One2many(
        "product.code.version", "product_id", string="Code versions", copy=False
    )
    version_code_count = fields.Integer(
        string="Version code Count", compute="_compute_product_version_code_count"
    )

    def _compute_product_version_code_count(self):
        for product in self:
            product.version_code_count = product.env[
                "product.code.version"
            ].search_count(
                [
                    "|",
                    ("product_tmpl_id", "=", product.product_tmpl_id.id),
                    ("product_id", "=", product.id),
                ]
            )

    @api.model
    def _name_search(self, name, domain=None, operator="ilike", limit=None, order=None):
        search_result = super()._name_search(
            name=name, domain=domain, operator=operator, limit=limit, order=order
        )

        codes = ("version_code_ids", "ilike", name)
        searched_ids = self.env["product.product"].search([codes]).ids
        if isinstance(searched_ids, list) and isinstance(search_result, list):
            searched_ids = list(set(search_result + searched_ids))
            domain = [("id", "in", searched_ids)]

        return super()._name_search("", domain, "ilike", limit, order)

    def action_open_version_codes(self):
        res = self.product_tmpl_id.action_open_version_codes()

        res["context"].update(
            {
                "default_product_tmpl_id": self.product_tmpl_id.id,
                "default_product_id": self.id,
            }
        )
        return res
