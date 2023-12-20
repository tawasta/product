from odoo import api, fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    standard_price_write_date = fields.Datetime(
        "Cost updated",
        copy=False,
        readonly=True,
    )

    list_price_write_date = fields.Datetime(
        "Price updated",
        copy=False,
        readonly=True,
    )

    @api.model
    def write(self, vals):
        if "standard_price" in vals:
            vals["standard_price_write_date"] = fields.Datetime.now()
        if "list_price" in vals:
            vals["list_price_write_date"] = fields.Datetime.now()

        return super().write(vals)
