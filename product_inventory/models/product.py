from odoo import fields, models, api


class ProductTemplate(models.Model):

    _inherit = "product.template"

    

class ProductProduct(models.Model):
    _inherit="product.product"

    inventory_date = fields.Date(compute='_compute_inventory_date', store=True, index=True)

    stock_inventory_line_ids = fields.One2many('stock.inventory.line', 'product_id', help='Technical: used to compute lines.')

    @api.depends('stock_move_ids', 'stock_inventory_line_ids')
    def _compute_inventory_date(self):
        for record in self:

            move_lines = self.env['stock.move.line'].search([
                ('product_id', '=', record.id),
                ('date', '!=', False)
            ], limit=1, order='date DESC')

            inventory_lines = self.env['stock.inventory.line'].search([
                ('product_id', '=', record.id),
                ('inventory_date', '!=', False)
            ], limit=1, order='inventory_date DESC')

            dates = [line.date for line in move_lines] + [line.inventory_date for line in inventory_lines]
            record.inventory_date = dates and max(dates) or False

    def action_view_inventory_lines(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("product_inventory.stock_inventory_line_action")
        action['domain'] = [('product_id', '=', self.id)]
        return action
