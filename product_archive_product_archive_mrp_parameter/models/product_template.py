from odoo import models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    def area_parameter_search(self, product):
        """MRP area Parameter generator"""
        parameters = (
            self.env["product.mrp.area"]
            .sudo()
            .search(
                [
                    ("product_tmpl_id", "=", product.id),
                    "|",
                    ("active", "=", True),
                    ("active", "=", False),
                ]
            )
        )
        for parameter in parameters:
            yield parameter

    def toggle_active(self):
        """Switch parameters as archived"""
        res = super(ProductTemplate, self).toggle_active()
        for product in self:
            for parameter in self.area_parameter_search(product):
                parameter.active = product.active
        return res
