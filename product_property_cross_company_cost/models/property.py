from odoo import api
from odoo import models


class Property(models.Model):

    _inherit = "ir.property"

    @api.model
    def get_multi(self, name, model, ids):
        if model == "product.product" and name == "standard_price":
            self = self.with_context(force_company=1)

        return super(Property, self).get_multi(name, model, ids)

    @api.model
    def set_multi(self, name, model, values, default_value=None):
        if model == "product.product" and name == "standard_price":
            self = self.with_context(force_company=1)
        return super(Property, self).set_multi(name, model, values, default_value)
