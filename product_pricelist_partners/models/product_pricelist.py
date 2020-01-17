# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo import:
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductPricelist(models.Model):

    # 1. Private attributes
    _inherit = "product.pricelist"

    # 2. Fields declaration
    partner_ids = fields.One2many(
        string="Partners using this pricelist",
        comodel_name="res.partner",
        inverse_name="property_product_pricelist",
    )

    # 3. Default methods

    # 4. Compute and search fields

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
