from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    """
    # TODO: consider if this should be enforced
    @api.constrains('product_material_composition_ids')
    def _check_product_bom_count(self):
        for product in self:
             if product.bom_ids:
                raise ValidationError(
                    "Products with BOMs cannot have Product Material Compositions, "
                    "please add them for the raw materials instead.")
    """

    product_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_product_id",
        string="Product Material Compositions",
        domain=[("type", "=", "product")],
    )

    product_packaging_material_composition_ids = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_product_id",
        string="Product Packaging Material Compositions",
        domain=[("type", "=", "product_packaging")],
    )
