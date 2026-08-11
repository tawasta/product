from odoo import api, fields, models


class ReportProductTemplateCustomA4(models.AbstractModel):
    _name = "report.product_print_custom_label.report_custom_a4"
    _description = "Product Template Custom A4 Label Report"

    @api.model
    def _get_report_values(self, docids, data):
        if not data:
            return {}
        active_model = data.get("active_model", "product.product")
        if active_model == "product.template":
            Product = self.env["product.template"]
        else:
            Product = self.env["product.product"]
        quantity_by_product = data.get("quantity_by_product", {})
        product_ids = [int(pid) for pid in quantity_by_product.keys()]
        docs = Product.browse(product_ids)
        return {
            "docs": docs,
            "quantity_by_product": quantity_by_product,
            "display_quantity": data.get("display_quantity", 1),
            "pallet_amount": data.get("pallet_amount", 1),
            "today": fields.Date.today(),
            "barcode_img_style": "width:160mm;height:20mm;",
        }
