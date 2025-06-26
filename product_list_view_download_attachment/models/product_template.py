from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    attachment_ids = fields.One2many(
        comodel_name="ir.attachment",
        inverse_name="res_id",
        string="Attachments",
        domain=[("res_model", "=", "product.template")],
    )

    def download_attachment(self):
        self.ensure_one()
        if self.attachment_ids:
            return {
                "type": "ir.actions.act_url",
                "url": f"/web/content/{self.attachment_ids[0].id}?download=true",
                "target": "self",
            }
