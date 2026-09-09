from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_attribute_value_image_record(self):
        """Return the product.template.attribute.image record configured
        on this variant's template for one of its own attribute values
        (e.g. the lampshade color), if any.

        Returns an empty recordset if none of the variant's attribute
        values has an image configured on the template.
        """
        self.ensure_one()

        attribute_value_ids = (
            self.product_template_attribute_value_ids.product_attribute_value_id.ids
        )
        if not attribute_value_ids:
            return self.env["product.template.attribute.image"]

        return self.env["product.template.attribute.image"].search(
            [
                ("product_tmpl_id", "=", self.product_tmpl_id.id),
                ("product_attribute_value_id", "in", attribute_value_ids),
            ],
            limit=1,
        )

    def _get_attribute_value_image(self):
        """Return the image (raw bytes) configured on the product
        template for one of this variant's attribute values, avoiding
        the need to upload a dedicated image per variant."""
        self.ensure_one()
        return self._get_attribute_value_image_record().image_1920
