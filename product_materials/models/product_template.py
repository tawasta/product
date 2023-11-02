from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    """
    # TODO: consider if this should be enforced
    @api.constrains('product_material_compositions')
    def _check_product_bom_count(self):
        for product in self:
             if product.bom_ids:
                raise ValidationError(
                    "Products with BOMs cannot have Product Material Compositions, "
                    "please add them for the raw materials instead.")
    """

    product_material_compositions = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_template",
        string="Product Material Compositions",
        domain=[("type", "=", "product")],
    )

    product_packaging_material_compositions = fields.One2many(
        comodel_name="product.material.composition",
        inverse_name="product_template",
        string="Product Packaging Material Compositions",
        domain=[("type", "=", "product_packaging")],
    )

    # material_purchase = fields.Many2many(
    #    related="product_tmpl_id.material_purchase", string="Material"
    # )
