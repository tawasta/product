from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model_create_multi
    def create(self, vals_list):
        # Variants of a new product add the inherited is_storable default
        # themselves. Variants of an existing template are skipped: a value
        # here would be written to that template.
        self.env["product.template"]._set_not_storable_for_non_goods(
            [vals for vals in vals_list if not vals.get("product_tmpl_id")]
        )
        return super().create(vals_list)
