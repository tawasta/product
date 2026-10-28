from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    putaway_rules_count = fields.Integer(
        string="Putaway rules Count",
        compute=lambda self: self._compute_putaway_rules_count(),
    )

    def _compute_putaway_rules_count(self):
        for template in self:
            template.putaway_rules_count = template.env[
                "stock.putaway.rule"
            ].search_count(
                [
                    "|",
                    ("category_id", "=", template.categ_id.id),
                    ("product_id", "in", template.product_variant_ids.ids),
                ]
            )


class ProductProduct(models.Model):
    _inherit = "product.product"

    putaway_rules_count = fields.Integer(
        string="Putaway rules Count",
        compute=lambda self: self._compute_putaway_rules_count(),
    )

    def _compute_putaway_rules_count(self):
        for product in self:
            product.putaway_rules_count = product.env[
                "stock.putaway.rule"
            ].search_count(
                [
                    "|",
                    ("category_id", "=", product.categ_id.id),
                    ("product_id", "=", product.id),
                ]
            )
