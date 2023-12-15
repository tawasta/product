from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError


class ProductMaterialComposition(models.Model):

    _name = "product.material.composition"
    _description = "Product Material Composition"
    _order = "sequence, id"
    _rec_name = "product_material_id"

    @tools.ormcache()
    def _get_default_net_weight_uom_id(self):
        # Suggest grams as default
        return self.env.ref("uom.product_uom_gram")

    sequence = fields.Integer(string="Sequence")

    # This is the variant that the material row is linked to
    product_product_id = fields.Many2one(
        comodel_name="product.product", string="Product"
    )

    product_material_class_id = fields.Many2one(
        comodel_name="product.material.class", string="Material Class"
    )

    # This is an additional info field that becomes available if
    # the 3-level material classification is turned on
    name = fields.Char(string="Product or Part Name")

    product_material_id = fields.Many2one(
        comodel_name="product.material",
        string="Material",
    )

    product_material_sublevel_id = fields.Many2one(
        comodel_name="product.material.sublevel",
        string="Material Sublevel",
    )

    net_weight = fields.Float(string="Net weight")

    net_weight_uom_id = fields.Many2one(
        comodel_name="uom.uom",
        string="Unit of Measure",
        domain=lambda self: [
            ("category_id", "=", self.env.ref("uom.product_uom_categ_kgm").id)
        ],
        default=_get_default_net_weight_uom_id,
    )

    recycled_percentage = fields.Integer(
        string="Recycled Material %",
        help="What percentage originates from recycled materials",
    )

    product_material_waste_component_id = fields.Many2one(
        comodel_name="product.material.waste.component",
        string="Waste Component",
    )

    product_material_waste_endpoint_id = fields.Many2one(
        comodel_name="product.material.waste.endpoint",
        string="Waste Endpoint",
    )

    description = fields.Text(string="Notes")

    # Defines if the material row is related to product itself's materials or the
    # product's packaging's materials
    type = fields.Selection(
        selection=[("product", "Product"), ("product_packaging", "Product Packaging")],
        required=True,
    )

    attachment_ids = fields.Many2many(
        "ir.attachment",
        string="Attachments",
    )

    @api.constrains("recycled_percentage")
    def _check_percentage(self):
        for record in self:
            if record.recycled_percentage < 0 or record.recycled_percentage > 100:
                raise ValidationError(_("Percentage has to be between 0 and 100"))

    @api.onchange("product_material_sublevel_id")
    def _onchange_product_material_sublevel_id(self):
        # If user changes the Material Sublevel, set the Material
        self.product_material_id = self.product_material_sublevel_id.product_material_id

    @api.onchange("product_material_id")
    def _onchange_product_material_id(self):

        # If user changes the Material, set the Material Class
        self.product_material_class_id = (
            self.product_material_id.product_material_class_id
        )

        # Suggest also the default waste component
        self.product_material_waste_component_id = (
            self.product_material_id.product_material_waste_component_id
        )

    @api.onchange("product_material_waste_component_id")
    def _onchange_product_material_waste_component_id(self):
        # If user changes the Waste Component, suggest Waste Endpoint
        self.product_material_waste_endpoint_id = (
            self.product_material_waste_component_id.product_material_waste_endpoint_id
        )
