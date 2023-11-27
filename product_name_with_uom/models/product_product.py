from odoo import models


class ProductProduct(models.Model):

    _inherit = "product.product"

    def name_get(self):
        old_res = super(ProductProduct, self).name_get()
        # This is not optimal, but allows us to not override the whole method

        new_res = list()
        for record in old_res:
            product = self.browse(record[0])
            product_name = "{} / {}".format(record[1], product.sudo().uom_id.name)

            new_res.append((record[0], product_name))

        return new_res
