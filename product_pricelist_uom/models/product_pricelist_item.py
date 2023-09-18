from odoo import fields, models


class ProductPricelistItem(models.Model):

    _inherit = "product.pricelist.item"

    unit_of_measure = fields.Char(
        string="Unit of measure", compute="_compute_unit_of_measure"
    )

    def _compute_unit_of_measure(self):
        for record in self:
            product_id = record.product_tmpl_id or record.product_id

            if product_id:
                record.unit_of_measure = product_id.uom_id.name
