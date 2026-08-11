from odoo import fields, models


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    print_format = fields.Selection(
        selection_add=[
            ("custom_a4", "A4 Custom Label"),
        ],
        ondelete={"custom_a4": "set default"},
    )
    display_quantity = fields.Integer("Quantity per pallet", default=1)
    pallet_amount = fields.Integer("Pallets (copies)", default=1)

    def _prepare_report_data(self):
        xml_id, data = super()._prepare_report_data()
        if self.print_format == "custom_a4":
            xml_id = "product_print_custom_label.report_product_template_custom_a4"
            data["display_quantity"] = self.display_quantity
            data["pallet_amount"] = self.pallet_amount
        return xml_id, data
