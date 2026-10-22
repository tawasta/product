import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _action_open_solidworks_import(self):
        _logger.error("HERE:")
