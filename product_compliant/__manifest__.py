##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2021 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    "name": "Product Compliance",
    "summary": "Add fields for product compliance (REACH, RoHS, Work Safety etc)",
    "version": "14.0.1.2.1",
    "category": "Product",
    "website": "https://gitlab.com/tawasta/odoo/product",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["sale"],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/product_compliant.xml",
        "views/product_template.xml",
        "views/res_config_settings.xml",
    ],
}
