# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
# 4. Imports from Odoo modules:
from openerp.osv import expression

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductProduct(models.Model):

    # 1. Private attributes
    _inherit = "product.product"

    # 2. Fields declaration

    # 3. Default methods
    @api.multi
    def name_get(self):
        records = list()

        for record in self:
            name = record.name

            attributes = ""
            for attribute in record.attribute_value_ids:
                if (
                    attribute.attribute_id.name == "Laji"
                    or attribute.attribute_id.name == "Kokoonpano"
                ):
                    attributes += attribute.name + ", "

            if attributes:
                name = "{} ({})".format(name, attributes.rstrip(" ").rstrip(","))

            records.append((record.id, name))

        return records

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        domain = [
            "|",
            "|",
            ("name", "ilike", name),
            ("default_code", "ilike", name),
            ("attribute_line_ids.value_ids.name", "ilike", name),
        ]

        products = self.search(expression.AND([domain, args]))

        return products.name_get()

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
