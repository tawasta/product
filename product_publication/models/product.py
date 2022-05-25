##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2021- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductTemplate(models.Model):

    # 1. Private attributes
    _inherit = "product.template"

    # 2. Fields declaration
    is_publication_product = fields.Boolean(
        string="Is a publication product",
        help="Is product a publication (i.e. book, video)?",
    )
    publication_isbn = fields.Char(
        string="ISBN", help="International Standard Book Number"
    )
    publication_authors = fields.Char(
        string="Authors", help="Authors of the publication"
    )
    publication_publisher = fields.Char(
        string="Publisher", help="Publisher of the publication"
    )
    publication_publishing_year = fields.Integer(
        string="Publishing year", help="Publishing year of the publication"
    )
    publication_binding_form = fields.Char(
        string="Binding form",
        help="Binding form of the publication (i.e. paperback, hard cover)",
    )
    publication_edition = fields.Char(
        string="Edition", help="Edition of the publication"
    )
    publication_size = fields.Char(string="Size", help="Size of the publication")
    publication_breadth = fields.Char(
        string="Breadth", help="Breadth of the publication"
    )
    publication_quantity = fields.Integer(
        string="Quantity", help="Quantity of the publication"
    )
    publication_duration = fields.Float(
        string="Duration", help="Duration of the publication"
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.constrains("publication_publishing_year")
    def _check_year(self):
        # make sure publishing year is not negative nor far in the future
        if (
            self.publication_publishing_year < 0
            or self.publication_publishing_year > 2040
        ):
            raise ValidationError(
                _("Publishing year is invalid: %s" % self.publication_publishing_year)
            )

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
