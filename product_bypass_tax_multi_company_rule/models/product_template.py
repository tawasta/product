from odoo import fields, models
from datetime import timedelta


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        tax_rule = self.env.ref("account.tax_comp_rule").sudo()
        tax_rule.write({"active": False})

        result = super(ProductTemplate, self).write(vals)

        self._schedule_tax_rule_reactivation()
        return result

    def _schedule_tax_rule_reactivation(self):
        self.with_delay(
            eta=fields.Datetime.now() + timedelta(seconds=1)
        )._reactivate_tax_rule()

    def _reactivate_tax_rule(self):
        tax_rule = self.env.ref("account.tax_comp_rule").sudo()
        tax_rule.write({"active": True})
