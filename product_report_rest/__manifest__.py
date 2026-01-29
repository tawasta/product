##############################################################################
#
#    Author: Futural Oy
#    Copyright 2023- Futural Oy (http://www.futural.fi)
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
    "name": "Product Report REST (FastAPI)",
    "summary": "FastAPI endpoint for product reporting (API key protected)",
    "version": "17.0.1.0.0",
    "category": "Reporting",
    "website": "https://github.com/tawasta/product",
    "author": "Futural",
    "license": "AGPL-3",
    "data": [
        "data/fastapi_endpoint_data.xml",
        "views/product_category.xml",
    ],
    "depends": [
        "fastapi",
        "fastapi_auth_api_key",
        "auth_api_key",
        "product",
    ],
    "external_dependencies": {"python": ["fastapi", "pydantic"]},
    "application": False,
    "installable": True,
}
