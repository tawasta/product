##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2022 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    "name": "Product Materials",
    "summary": "Product Materials info for products and their packaging",
    "version": "14.0.3.6.10",
    "category": "Product",
    "website": "https://gitlab.com/tawasta/odoo/product",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock", "sale", "account_invoice_related_sale_order"],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "report/invoice_report.xml",
        "report/stock_report.xml",
        "views/product_material.xml",
        "views/product_material_class.xml",
        "views/product_material_composition.xml",
        "views/product_material_sublevel.xml",
        "views/product_material_waste_component.xml",
        "views/product_material_waste_endpoint.xml",
        "views/product_product.xml",
        "views/res_config_settings.xml",
        "views/sale_order.xml",
    ],
}
