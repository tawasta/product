from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def action_update_quantity_on_hand(self):
        """Gate the standard 'On Hand' smart button on the product form
        so that belonging to a specific access group is required for access.
        Otherwise the user gets redirected to a readonly version of the
        stock.quant view"""

        self.ensure_one()
        if self.env.user.has_group(
            "product_on_hand_qty_opens_readonly_view.group_allow_update_on_hand_qty"
        ):
            return super().action_update_quantity_on_hand()
        return self._action_open_quants_readonly()

    def _action_open_quants_readonly(self):
        """Build the read-only counterpart of the standard stock.quant action.
        strip out any bits that make the view editable.
        """
        self.ensure_one()
        action = super().action_update_quantity_on_hand()

        readonly_tree_view = self.env.ref(
            "product_on_hand_qty_opens_readonly_view.view_stock_quant_tree_readonly"
        )
        action["views"] = [(readonly_tree_view.id, "tree")]
        action["view_mode"] = "tree"
        action.pop("view_id", None)

        ctx = dict(action.get("context") or {})
        for key in (
            "inventory_mode",
            "default_inventory_quantity_set",
            "search_default_inventory_quantity_set",
            "search_default_internal_loc",
        ):
            ctx.pop(key, None)

        ctx["create"] = False
        ctx["edit"] = False
        ctx["delete"] = False
        action["context"] = ctx

        return action
