##############################################################################
#
#    Author: Futural Oy
#    Copyright 2025 Futural Oy (https://futural.fi)
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
    "name": "Control version codes of a product",
    "summary": "Define and search version codes of products",
    "version": "17.0.1.0.0",
    "category": "Product",
    "website": "https://github.com/tawasta/product",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
        "sale",
        "stock",
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_code_version.xml",
        "views/product_view.xml",
        "views/sale_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "product_code_version_control/static/src/js/search.esm.js",
        ],
    },
}
