# -*- coding: utf-8 -*-

from openerp import api, fields, models


class AccountInvoiceRoyaltiesPO(models.TransientModel):

    _name = 'account.invoice.royalties'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
    )

    @api.multi
    def create_royalties_purchase_order(self):
        if 'active_ids' not in self._context:
            return False

        invoice_ids = self._context['active_ids']
        invoices = self.env['account.invoice'].browse(invoice_ids)

        po_lines = list()

        PurchaseOrder = self.env['purchase.order']
        PurchaseOrderLine = self.env['purchase.order.line']

        for invoice in invoices:
            for line in invoice.invoice_line:
                for royalty in line.product_id.royalties:
                    desc = '%(partner_name)s (%(role)s): %(product_name)s' % ({
                            'partner_name': royalty.recipient.name,
                            'role': royalty.role,
                            'product_name': line.product_id.name,
                    })

                    price = (royalty.percent/100) * line.price_subtotal

                    po_lines.append({
                        #'product_id': line.product_id.id,
                        'name': desc,
                        'price_unit': price,
                        'product_qty': 1,
                        'date_planned': fields.Date.today(),
                    })

        purchase_order = PurchaseOrder.create({
            'partner_id': self.partner_id.id,
            'location_id': self.partner_id.property_stock_supplier.id,
            'pricelist_id':
                self.partner_id.property_product_pricelist_purchase.id,
        })

        for po_line in po_lines:
            po_line['order_id'] = purchase_order.id
            PurchaseOrderLine.create(po_line)

        return {'active_ids': invoice_ids}
