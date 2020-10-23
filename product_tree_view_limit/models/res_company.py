from odoo import fields, models


class ResCompany(models.Model):

    _inherit = 'res.company'

    tree_view_limit = fields.Integer(
        string="Product Tree view limit",
        help="Change the number of records shown on product tree view per page"
    )
