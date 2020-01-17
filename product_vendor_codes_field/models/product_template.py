from openerp import api, fields, models


class ProductProduct(models.Model):

    _inherit = "product.template"

    @api.depends("seller_ids", "seller_ids.product_code")
    def _compute_vendor_codes(self):
        for record in self:
            record.vendor_codes = (
                ", ".join(
                    [
                        seller.product_code
                        for seller in record.seller_ids
                        if seller.product_code
                    ]
                )
                or ""
            )

    vendor_codes = fields.Char(
        compute="_compute_vendor_codes", string="Partner Codes", store=True
    )
