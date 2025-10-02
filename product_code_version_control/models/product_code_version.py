from odoo import api, exceptions, fields, models


class ProductCodeVersion(models.Model):
    _name = "product.code.version"
    _description = "Product code version"
    _order = "sequence, id"

    name = fields.Char(string="Code version", copy=False, required=True)
    product_id = fields.Many2one(
        "product.product",
        string="Related product",
        domain="[('product_tmpl_id', '=', product_tmpl_id)]",
    )
    product_tmpl_id = fields.Many2one(
        "product.template",
        string="Related product template",
        required=True,
    )
    sequence = fields.Integer()
    remarks = fields.Text(copy=False)

    @api.onchange("name")
    def onchange_name(self):
        """Search duplicate code version name. Also note a user if a product code
        does not exist in odoo, but the user tries to write it as 'Code version'."""

        duplicate_code_name = self.env["product.code.version"].search(
            [
                ("name", "=", self.name),
                ("product_tmpl_id", "=", self.product_tmpl_id.id),
            ]
        )

        if duplicate_code_name:
            msg = (
                "A code version %s already exists with this name for this product.\n"
                "Please choose another name."
            ) % self.name
            raise exceptions.UserError(msg)

        code = self.name

        code_exists = code and (
            self.env["product.product"].search([("default_code", "=", code)])
            or self.env["product.template"].search([("default_code", "=", code)])
        )

        if code and not code_exists:
            message = (
                f"There is no product with code {code}. Are you sure you want "
                "to create this version code?"
            )
            return {
                "warning": {
                    "title": "No existing product code found",
                    "message": message,
                }
            }
