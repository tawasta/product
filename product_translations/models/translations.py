from odoo import fields, models


class IrTranslation(models.Model):

    _inherit = "ir.translation"

    product_template_id = fields.Many2one(
        string="Related product",
        comodel_name="product.template",
        compute="_compute_product_template_id",
        search="_search_product_template_id",
    )

    def _search_product_template_id(self, operator, value):
        recs = self.search([]).filtered(lambda x: x.product_template_id)
        if recs:
            return [("id", "in", [x.id for x in recs])]

    def _compute_product_template_id(self):
        product_template = self.env["product.template"]
        for record in self:
            try:
                model, _field = record.name.split(",")

                if model == "product.template":
                    product = product_template.browse(record.res_id)
                    if product:
                        record.product_template_id = product.id
                    else:
                        record.product_template_id = False
                else:
                    record.product_template_id = False
            except ValueError:
                # Skip translations with incomplete data
                record.product_template_id = False
