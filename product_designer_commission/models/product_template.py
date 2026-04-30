from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    designer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Designer",
        domain=[("is_a_designer", "=", True)],
        help="Designer responsible for this product.",
    )