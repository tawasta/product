from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Core makes products storable by default only in the Inventory menus.
    # A default_type in the context (e.g. a services menu) must not get it.
    is_storable = fields.Boolean(
        default=lambda self: self.env.context.get("default_type", "consu") == "consu"
    )

    @api.model
    def _set_not_storable_for_non_goods(self, vals_list):
        """The is_storable default is applied before compute_is_storable,
        so services and combos created without the form would be storable."""
        default_type = self.env.context.get("default_type", "consu")
        for vals in vals_list:
            if "is_storable" not in vals and vals.get("type", default_type) != "consu":
                vals["is_storable"] = False

    @api.model_create_multi
    def create(self, vals_list):
        self._set_not_storable_for_non_goods(vals_list)
        return super().create(vals_list)
