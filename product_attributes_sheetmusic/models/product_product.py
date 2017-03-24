# -*- coding: utf-8 -*-

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
    _inherit = 'product.product'

    # 2. Fields declaration

    # 3. Default methods
    @api.multi
    def name_get(self):
        records = list()

        for record in self:
            name = record.name

            attributes = ""
            for attribute in record.attribute_value_ids:
                if attribute.attribute_id.name == 'Laji' or attribute.attribute_id.name == 'Kokoonpano':
                    attributes += attribute.name + ", "

            if attributes:
                name = "%s (%s)" % (name, attributes.rstrip(" ").rstrip(","))

            records.append((record.id, name))

        #res = super(ProductProduct, self).name_get()

        return records

    def name_get2(self, cr, user, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        if not len(ids):
            return []

        def _name_get(d):
            name = d.get('name','')
            code = context.get('display_default_code', True) and d.get('default_code',False) or False
            if code:
                name = '[%s] %s' % (code,name)
            return (d['id'], name)


    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
