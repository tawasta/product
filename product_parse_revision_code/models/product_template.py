from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _cron_update_revision_code(self):
        """Fill revision code from the last part of the default code."""
        for rec in self.env["product.template"].search([]):
            if rec.default_code and not rec.revision_code:
                parts = rec.default_code.split(" ")
                if len(parts) > 1:
                    rec.write({"revision_code": parts[-1]})
