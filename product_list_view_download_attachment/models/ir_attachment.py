from odoo import api, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)

        for values in vals_list:
            res_id = values.get("res_id", False)
            res_model = values.get("res_model", "")
            if res_model == "product.template" and res_id:
                product = self.env["product.template"].browse(res_id)
                if product:
                    product.write({"main_attachment_id": res.id})
        return res
