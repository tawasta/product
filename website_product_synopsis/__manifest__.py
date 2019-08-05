##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Website - Product Synopsis',
    'category': 'Website',
    'version': '12.0.1.0.0',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': [
        'website_sale'
    ],
    'description': """
Website - Product Synopsis
==========================
 * Adds a new field for a short description about a product. The text is shown in website's product grid view

""",
    'data': [
        'view/product_template.xml',
        'views/product_synopsis.xml',
    ]
    
}
