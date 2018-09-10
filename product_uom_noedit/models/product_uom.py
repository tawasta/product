# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import AccessError


class ProductUom(models.Model):

    _inherit = 'product.uom'

    @api.model
    def check_access_rights(self, operation, raise_exception=True):
        if operation == 'read' or self.env.user.has_group('base.group_system'):
            return super(ProductUom, self).check_access_rights(operation, raise_exception)

        # Disallow editing UoM:s for non-admins
        if raise_exception:
            msg = _('Only administrators can edit units of measure')
            raise AccessError(msg)

        return
