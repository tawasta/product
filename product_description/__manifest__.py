##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2019 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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

{
    "name": "Product Description for form view (DEPRECATED)",
    "summary": "Adds a  ecommerce desciption field for product template (deprecated)",
    "version": "17.0.1.0.1",
    "category": "Product",
    "website": "https://gitlab.com/tawasta/odoo/product",
    "author": "Oy Tawasta Technologies Ltd.",
    "license": "AGPL-3",
    "application": False,
    "installable": False,
    "depends": ["product", "website_sale"],
    "data": ["views/product_template_desc.xml"],
}
