from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    number_of_users_min = fields.Integer(
        string="Number of Users (min.)",
        help="How many persons can use this product at the same time",
    )

    number_of_users_max = fields.Integer(
        string="Number of Users (max.)",
        help="How many persons can use this product at the same time",
    )

    def _prepare_variant_values(self, combination):
        """
        As variant is created inside template create() method and as
        template fields values are flushed after _create_variant_ids(),
        we catch the variant values preparation to update them
        """
        res = super()._prepare_variant_values(combination)

        if self.number_of_users_min:
            res.update({"number_of_users_min": self.number_of_users_min})

        if self.number_of_users_max:
            res.update({"number_of_users_max": self.number_of_users_max})

        return res
