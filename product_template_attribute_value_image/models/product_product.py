from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_attribute_value_image(self):
        """Return the image configured on the product template for one of
        this variant's attribute values (e.g. the lampshade color),
        avoiding the need to upload a dedicated image per variant.

        Returns an empty (falsy) image if none of the variant's attribute
        values has an image configured on the template.
        """
        self.ensure_one()

        attribute_value_ids = (
            self.product_template_attribute_value_ids.product_attribute_value_id.ids
        )
        if not attribute_value_ids:
            return False

        image_record = self.env["product.template.attribute.image"].search(
            [
                ("product_tmpl_id", "=", self.product_tmpl_id.id),
                ("product_attribute_value_id", "in", attribute_value_ids),
            ],
            limit=1,
        )
        return image_record.image_1920
