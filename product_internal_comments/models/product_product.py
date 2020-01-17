from openerp import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    internal_comments = fields.Text("Internal Comments")
