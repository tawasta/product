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
from odoo import fields, models, api
from odoo.addons import decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductProduct(models.Model):
    # 1. Private attributes
    _inherit = "product.product"

    # 2. Fields declaration
    qty_in_product = fields.Float(
        "Estimated quantity in complete Product",
        help="Estimated quantity used in complete product",
    )
    qty_available_in_product = fields.Float(
        "Estimated complete Products",
        compute="_compute_quantities",
        search="_search_qty_available",
        digits=dp.get_precision("Product Unit of Measure"),
        help="Current quantity of products divided by qty_used_in_product.\n"
        "In a context with a single Stock Location, this includes "
        "goods stored at this Location, or any of its children.\n"
        "In a context with a single Warehouse, this includes "
        "goods stored in the Stock Location of this Warehouse, or any "
        "of its children.\n"
        "stored in the Stock Location of the Warehouse of this Shop, "
        "or any of its children.\n"
        "Otherwise, this includes goods stored in any Stock Location "
        "with 'internal' type.",
    )
    virtual_available_in_product = fields.Float(
        "Estimated complete Products forecast",
        compute="_compute_quantities",
        search="_search_virtual_available",
        digits=dp.get_precision("Product Unit of Measure"),
        help="Forecast quantity (computed as Quantity On Hand "
        "- Outgoing + Incoming) divided by qty_used_in_product\n"
        "In a context with a single Stock Location, this includes "
        "goods stored in this location, or any of its children.\n"
        "In a context with a single Warehouse, this includes "
        "goods stored in the Stock Location of this Warehouse, or any "
        "of its children.\n"
        "Otherwise, this includes goods stored in any Stock Location "
        "with 'internal' type.",
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends("stock_move_ids.product_qty", "stock_move_ids.state")
    def _compute_quantities(self):
        res = super(ProductProduct, self)._compute_quantities()
        for product in self:
            if product.qty_used_in_product:
                product.qty_available_in_product = (
                    product.qty_available / product.qty_used_in_product
                )
                product.virtual_available_in_product = (
                    product.virtual_available / product.qty_used_in_product
                )
            else:
                product.qty_available_in_product = product.qty_available
                product.virtual_available_in_product = product.virtual_available
        return res

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods


class ProductTemplate(models.Model):
    # 1. Private attributes
    _inherit = "product.template"

    # 2. Fields declaration
    qty_used_in_product = fields.Float(
        "Estimated quantity in complete Product",
        help="Estimated quantity used in complete product",
    )
    qty_available_in_product = fields.Float(
        "Estimated complete Products",
        compute="_compute_quantities",
        search="_search_qty_available",
        digits=dp.get_precision("Product Unit of Measure"),
        help="Current quantity of products divided by qty_used_in_product.\n"
        "In a context with a single Stock Location, this includes "
        "goods stored at this Location, or any of its children.\n"
        "In a context with a single Warehouse, this includes "
        "goods stored in the Stock Location of this Warehouse, or any "
        "of its children.\n"
        "stored in the Stock Location of the Warehouse of this Shop, "
        "or any of its children.\n"
        "Otherwise, this includes goods stored in any Stock Location "
        "with 'internal' type.",
    )
    virtual_available_in_product = fields.Float(
        "Estimated complete Products forecast",
        compute="_compute_quantities",
        search="_search_virtual_available",
        digits=dp.get_precision("Product Unit of Measure"),
        help="Forecast quantity (computed as Quantity On Hand "
        "- Outgoing + Incoming) divided by qty_used_in_product\n"
        "In a context with a single Stock Location, this includes "
        "goods stored in this location, or any of its children.\n"
        "In a context with a single Warehouse, this includes "
        "goods stored in the Stock Location of this Warehouse, or any "
        "of its children.\n"
        "Otherwise, this includes goods stored in any Stock Location "
        "with 'internal' type.",
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends(
        "product_variant_ids",
        "product_variant_ids.stock_move_ids.product_qty",
        "product_variant_ids.stock_move_ids.state",
    )
    def _compute_quantities(self):
        res = super(ProductTemplate, self)._compute_quantities()
        for template in self:
            if template.qty_used_in_product:
                template.qty_available_in_product = (
                    template.qty_available / template.qty_used_in_product
                )
                template.virtual_available_in_product = (
                    template.virtual_available / template.qty_used_in_product
                )
            else:
                template.qty_available_in_product = template.qty_available
                template.virtual_available_in_product = template.virtual_available
        return res

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
