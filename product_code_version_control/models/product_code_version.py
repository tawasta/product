
from odoo import api, exceptions, fields, models


class ProductCodeVersion(models.Model):

    _name = 'product.code.version'
    _description = 'Product code version'
    _order = "sequence, id"

    name = fields.Char(string="Code version", copy=False, required=True)
    product_id = fields.Many2one(
        'product.product',
        string="Related product",
        domain="[('product_tmpl_id', '=', product_tmpl_id)]",
    )
    product_tmpl_id = fields.Many2one('product.template', string="Related product template", required=True)
    sequence = fields.Integer('Sequence')

    @api.onchange("name")
    def search_duplicate_code_version_name(self):
        duplicate_code_name = self.env["product.code.version"].search([
            ("name", "=", self.name),
            ("product_tmpl_id", "=", self.product_tmpl_id.id),
        ])

        if duplicate_code_name:
            msg = (
                "A code version %s already exists with this name for this product.\n"
                "Please choose another name."
            ) % self.name
            raise exceptions.UserError(msg)

 #   @api.model
 #   def default_get(self, fields_list):
 #       values = super().default_get(fields_list)

 #       print("DEFAULT VALUES", values)
 #       print("FIELDS LIST", fields_list)

 #       product_id = values.get('product_id', False)

 #       if "product_id" in fields_list and self.env["product.product"].sudo().browse(
 #           False
 #           #product_id
 #       ):

 #       return values
