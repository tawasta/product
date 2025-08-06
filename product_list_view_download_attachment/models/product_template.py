from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    attachment_ids = fields.One2many(
        comodel_name="ir.attachment",
        inverse_name="res_id",
        string="Attachments",
        domain=[("res_model", "=", "product.template")],
        copy=False,
    )

    main_attachment_id = fields.Many2one(
        comodel_name="ir.attachment",
        string="Main attachment",
        domain="[('id', 'in', attachment_ids)]",
        copy=False,
        store=True,
    )

    def download_attachment(self):
        self.ensure_one()
        if self.attachment_ids:
            attachment = self.main_attachment_id or self.attachment_ids[0]

            return {
                "type": "ir.actions.act_url",
                "url": f"/web/content/{attachment.id}?download=true",
                "target": "self",
            }
