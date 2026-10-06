from odoo import api, fields, models


class ProductTemplateAttributeImage(models.Model):
    _name = "product.template.attribute.image"
    _description = "Product Template Attribute Image"
    _order = "sequence, id"

    name = fields.Char()
    sequence = fields.Integer(default=10)

    product_tmpl_id = fields.Many2one(
        comodel_name="product.template",
        string="Product Template",
        required=True,
        ondelete="cascade",
        index=True,
    )
    product_attribute_value_id = fields.Many2one(
        comodel_name="product.attribute.value",
        string="Attribute Value",
        required=True,
        ondelete="cascade",
        help="Variants of this product template whose combination "
        "includes this attribute value (e.g. a lampshade color) will "
        "use this image.",
    )
    allowed_attribute_value_ids = fields.Many2many(
        comodel_name="product.attribute.value",
        compute="_compute_allowed_attribute_value_ids",
        help="Technical field limiting the attribute value selection to "
        "the values actually used on this product template.",
    )
    # Stored directly in a database column (attachment=False) instead of
    # relying on Odoo's automatic attachment-backed Binary/Image storage.
    # The ir.attachment record used by reports/emails is created and
    # maintained explicitly in _sync_image_attachment().
    image_1920 = fields.Image(string="Image", attachment=False)
    image_1920_filename = fields.Char(string="Image Filename")

    _sql_constraints = [
        (
            "product_tmpl_attribute_value_uniq",
            "unique(product_tmpl_id, product_attribute_value_id)",
            "Only one image can be set per attribute value for a given "
            "product template.",
        ),
    ]

    @api.depends("product_tmpl_id")
    def _compute_allowed_attribute_value_ids(self):
        for record in self:
            record.allowed_attribute_value_ids = (
                record.product_tmpl_id.attribute_line_ids.value_ids
            )

    def _sync_image_attachment(self):
        """Create/update/remove the ir.attachment record that represents
        this record's image, so it is findable in Settings > Technical >
        Attachments and usable by reports/emails
        (res_model=product.template.attribute.image, res_field=image_1920).
        """
        Attachment = self.env["ir.attachment"].sudo()
        for record in self:
            attachment = Attachment.search(
                [
                    ("res_model", "=", self._name),
                    ("res_field", "=", "image_1920"),
                    ("res_id", "=", record.id),
                ],
                limit=1,
            )
            if not record.image_1920:
                attachment.unlink()
                continue

            vals = {
                "name": record.image_1920_filename or "image_1920",
                "res_model": self._name,
                "res_field": "image_1920",
                "res_id": record.id,
                "type": "binary",
                "datas": record.image_1920,
            }
            if attachment:
                attachment.write(vals)
            else:
                Attachment.create(vals)

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._sync_image_attachment()
        return records

    def write(self, vals):
        res = super().write(vals)
        if "image_1920" in vals or "image_1920_filename" in vals:
            self._sync_image_attachment()
        return res

    def unlink(self):
        attachments = (
            self.env["ir.attachment"]
            .sudo()
            .search(
                [
                    ("res_model", "=", self._name),
                    ("res_field", "=", "image_1920"),
                    ("res_id", "in", self.ids),
                ]
            )
        )
        attachments.unlink()
        return super().unlink()
