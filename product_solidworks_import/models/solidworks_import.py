import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


def row_get(header_row, row, key):
    try:
        index = header_row.index(key)
        return row[index]
    except ValueError:
        return False


class SolidworksImport(models.Model):
    _name = "solidworks.import"
    _description = "Solidworks Import"
    _order = "create_date"

    # Solidworks CSV fields
    level = fields.Integer(default=0)
    title = fields.Char(required=True)
    description = fields.Char(required=True)
    item_type = fields.Selection(
        selection=[
            ("manufacture", "Manufacture"),
            ("purchase", "Purchase"),
        ],
        default="purchase",
    )
    co2_calculated_value = fields.Integer(default=0)

    # Module fields
    filename = fields.Char()
    product_template_id = fields.Many2one(comodel_name="product.template")
    processing_status = fields.Selection(
        selection=[
            ("pending", "Pending"),
            ("success", "Success"),
            ("failure", "Failure"),
        ],
        readonly=True,
        default="pending",
    )
    processing_status_message = fields.Text()
    created_from = fields.Selection(
        selection=[("ui", "User Interface"), ("api", "API")],
        readonly=True,
        default="ui",
    )

    def _create_boms(self, records):
        previous_rec = False
        for index, rec in enumerate(records):
            if previous_rec and previous_rec.level == rec.level - 1:
                previous_rec._ensure_bom_exists()
                bom = self.env["mrp.bom"].search(
                    [("code", "=", previous_rec.title)], limit=1
                )
                previous_rec._attach_products_to_bom(bom, rec.level, records[index:])
            previous_rec = rec

    def _attach_products_to_bom(self, bom, bom_product_ids_level, records):
        bom.bom_line_ids = [(5, 0, 0)]
        for rec in records:
            try:
                if rec.level == bom_product_ids_level:
                    self.env["mrp.bom.line"].create(
                        {
                            "bom_id": bom.id,
                            "product_id": rec.product_template_id.id,
                            "product_qty": 1,
                        }
                    )
                # Collect all level 1 items under level 0
                # but do not collect all level 2 items under level 1 item
                elif not bom_product_ids_level == 1:
                    break
            except Exception as e:
                _logger.error(e)

    @api.model_create_multi
    def create(self, vals_list):
        records = []
        for vals in vals_list:
            existing_import = self.env["solidworks.import"].search(
                [("title", "=", vals["title"])], limit=1
            )
            if len(existing_import) == 0:
                records.append(super().create(vals))
            else:
                existing_import.write(vals)
                records.append(existing_import)
        for rec in records:
            rec._ensure_product_exists()
        self._create_boms(records)
        return records

    def _ensure_product_exists(self):
        for rec in self:
            existing_product = self.env["product.template"].search(
                [("default_code", "=", rec.title)], limit=1
            )
            if len(existing_product) == 0:
                self.env["product.template"].create(
                    {
                        "name": rec.description,
                        "default_code": rec.title,
                    }
                )
                existing_product = self.env["product.template"].search(
                    [("default_code", "=", rec.title)], limit=1
                )

            for product in existing_product:
                rec.product_template_id = product.id
                product.write(
                    {
                        "name": rec.description,
                        "co2_emissions": rec.co2_calculated_value,
                        "mrp_product_qty": True
                        if rec.item_type == "manufacture"
                        else False,
                    }
                )

    def _ensure_bom_exists(self):
        for rec in self:
            existing_bom = self.env["mrp.bom"].search(
                [("code", "=", rec.title)], limit=1
            )
            if len(existing_bom) == 0:
                self.env["mrp.bom"].create(
                    {"product_tmpl_id": rec.product_template_id.id, "code": rec.title}
                )
                existing_bom = self.env["mrp.bom"].search(
                    [("code", "=", rec.title)], limit=1
                )
            rec.bom_ids = [(5, 0, 0)]
            rec.bom_ids = [(4, existing_bom.id)]
