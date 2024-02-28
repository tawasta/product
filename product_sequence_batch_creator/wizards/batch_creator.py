import datetime

from odoo import _, fields, models


class ProductBatchCreatorWizard(models.TransientModel):
    _name = "product_sequence_batch_creator.creator_wizard"

    def create_products(self):
        """Creates placeholder products, the quantity and prefix are provided
        by the user in the wizard"""
        product_model = self.env["product.template"]

        for i in range(0, self.qty):
            product_model.create({"name": "{} {}".format(self.prefix, i + 1)})

    def _get_default_prefix(self):
        return _("Reserved Code {} - ").format(
            datetime.datetime.today().strftime("%Y-%m-%d")
        )

    prefix = fields.Char(
        string="Prefix for created products",
        default=_get_default_prefix,
        help=(
            "The naming convention for placeholder products. "
            "The prefix will be followed by a running number"
        ),
    )

    qty = fields.Integer(string="Number of products to create", default=50)
