# -*- coding: utf-8 -*-
from openerp import models, fields

class product_template(models.Model):      

    _inherit = "product.template"

    website_synopsis = fields.Char(string="Synopsis for Website", translate=True)
    