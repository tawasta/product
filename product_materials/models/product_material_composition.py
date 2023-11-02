from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductMaterialComposition(models.Model):

    _name = "product.material.composition"
    _description = "Product Material Composition"
    _rec_name = "product_material"

    @api.constrains("recycled_percentage")
    def _check_percentage(self):
        for record in self:
            if record.recycled_percentage < 0 or record.recycled_percentage > 100:
                raise ValidationError(_("Percentage has to be between 0 and 100"))

    @api.onchange("product_material_class")
    def _onchange_product_material_class(self):
        # If user changes the Material Class, reset the Material also
        self.product_material = False

    product_template = fields.Many2one(
        comodel_name="product.template", string="Product"
    )

    product_material_class = fields.Many2one(
        comodel_name="product.material.class", string="Material Class", required=True
    )

    product_material_waste_component = fields.Many2one(
        comodel_name="product.material.waste.component",
        string="Product Material Waste Component",
    )

    product_material = fields.Many2one(
        comodel_name="product.material",
        string="Material",
    )

    recycled_percentage = fields.Integer(
        string="Recycled Material %",
        help="What percentage originates from recycled materials",
    )

    description = fields.Text(string="Description")

    halogen_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Halogen Compliant",
        domain=[("selectable_for", "in", [False, "halogens"])],
    )

    conflict_area_minerals_compliant = fields.Many2one(
        comodel_name="product.compliant",
        string="Conflict Area Minerals Compliant",
        domain=[("selectable_for", "in", [False, "conflict_area_minerals"])],
    )

    packaging_materials_checked = fields.Many2one(
        comodel_name="product.compliant",
        string="Packaging Materials Checked",
        domain=[("selectable_for", "in", [False, "packaging_materials"])],
    )

    type = fields.Selection(
        selection=[("product", "Product"), ("product_packaging", "Product Packaging")],
        required=True,
    )
