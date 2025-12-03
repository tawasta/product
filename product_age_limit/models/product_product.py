from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    age_limit = fields.Integer(
        help="Lowest age for persons using the product",
    )

    def _prepare_variant_values(self, combination):
        """
        As variant is created inside template create() method and as
        template fields values are flushed after _create_variant_ids(),
        we catch the variant values preparation to update them
        """
        res = super()._prepare_variant_values(combination)
        if self.age_limit:
            res.update({"age_limit": self.age_limit})

        return res
