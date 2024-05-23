import logging

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


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
        string="Net Weight UoM",
        domain=lambda self: [
            ("category_id", "=", self.env.ref("uom.product_uom_categ_kgm").id)
        ],
        default=_get_default_net_weight_uom_id,
    )

    composition_and_product_informational_uom = fields.Char(
        compute="_compute_composition_and_product_informational_uom",
        string="Units",
        help="Format: <Material Composition UoM> / <Parent Product UoM>",
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

    is_delivery_package = fields.Boolean(
        related="product_product_id.is_delivery_package", store=True
    )

    # Defines if the material row is related to product itself's materials or the
    # product's packaging's materials
    type = fields.Selection(
        selection=[("product", "Product"), ("product_packaging", "Incoming Packaging")],
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

    def _compute_composition_and_product_informational_uom(self):
        """
        Compute an informational field that shows both the unit of the material
        composition and product, e.g. "g / kg", to make it clear in the UI that the
        parent product is not measured in grams, just the material.
        """
        for line in self:

            line_uom = line.net_weight_uom_id and line.net_weight_uom_id.name or "-"

            product_uom = (
                line.product_product_id
                and line.product_product_id.uom_id
                and line.product_product_id.uom_id.name
                or "-"
            )

            line.composition_and_product_informational_uom = (
                f"{line_uom} / {product_uom}"
            )

    def _fix_attachment_ownership(self):
        """
        If you create a product material composition line AND add an attachment for it
        on the fly, without saving the line first, the connection between the
        attachment and the res_id does not get stored properly, and a user who was not
        the original attachment creator will get access errors when trying to view
        the attached file.

        For workaround details see:
        1) https://www.odoo.com/forum/help-1
        /m2m-attachment-field-issue-in-odoo-16-ce-creator-can-access-but-others-cannot
        -221283
        and
        2) mail/models/mail_template.py
        """
        for record in self:
            record.attachment_ids.write(
                {"res_model": record._name, "res_id": record.id}
            )
        return self

    @api.model_create_multi
    def create(self, values_list):
        return super().create(values_list)._fix_attachment_ownership()

    def write(self, vals):
        super().write(vals)
        self._fix_attachment_ownership()
        return True
