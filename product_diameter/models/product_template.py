from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    diameter = fields.Float(related="product_variant_ids.diameter", readonly=False)

    def _prepare_variant_values(self, combination):
        """
        As variant is created inside template create() method and as
        template fields values are flushed after _create_variant_ids(),
        we catch the variant values preparation to update them
        """
        res = super()._prepare_variant_values(combination)
        if self.diameter:
            res.update({"diameter": self.diameter})
        return res
