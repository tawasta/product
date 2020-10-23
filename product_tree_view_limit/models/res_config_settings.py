from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    tree_view_limit = fields.Integer(
        related='company_id.tree_view_limit',
        readonly=False,
    )

    @api.multi
    def write(self, values):
        res = super(ResConfigSettings, self).write(values)
        limit = self.tree_view_limit
        self.env.ref('stock.product_template_action_product').limit = limit
        self.env.ref('stock.stock_product_normal_action').limit = limit
        self.env.ref('purchase.product_normal_action_puchased').limit = limit
        self.env.ref('product.product_template_action').limit = limit
        self.env.ref('purchase.product_product_action').limit = limit
        self.env.ref('sale.product_template_action').limit = limit
        self.env.ref('product.product_normal_action_sell').limit = limit
        self.env.ref('mrp.product_template_action').limit = limit
        self.env.ref('mrp.mrp_product_variant_action').limit = limit
        return res
