.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Product API (FastAPI)
=====================
An Odoo 17 module that provides a lightweight **FastAPI-based reporting API**
for products (``product.product``).  
The module also extends product categories with a field ``is_secondary`` and
the API report includes a dedicated summary for secondary products.

Key Features
============
* **FastAPI endpoint** for product reporting
* **Category filtering** (using ``child_of`` to include subcategories)
* **Secondary products support** (``product.category.is_secondary``, inherited from parent category)
* **Summary** of stock quantities for secondary products and a separate list of those product rows
* Automatically creates an **API user**, **group**, and **FastAPI endpoint** at installation

Installation
============

1. Install dependencies::

   - Odoo modules: ``fastapi``, ``product``
   - Python packages: ``fastapi``, ``pydantic`` (if not already available in your environment)

2. Install this module in Odoo (Apps → Install).

3. The data file automatically creates:
   - User: **Product Reports API User**  
     (login: ``product_reports_api_user`` — set a password in Odoo)  
   - Group: **Product Reports FastAPI Group**  
   - FastAPI endpoint with root path: ``/product_rest_api``  

Configuration
=============
* **Secondary products**: Go to *Products → Configuration → Product Categories* and
  tick ``Is Secondary`` for categories considered as secondary.  
  The flag also applies to subcategories.

* **Access rights**: The endpoint can be called by users who belong to the
  *Product Reports FastAPI Group*.  
  The provided API user is added automatically; additional users can be added if needed.

Endpoints
=========

Base path: ``/product_rest_api``

**GET /product/report**

Returns product rows and a summary of secondary products.

Query parameters:

- ``limit`` (int, default 500, range 1–5000)
- ``offset`` (int, default 0)
- ``category`` (int, optional) – filters by product category using ``child_of``,
  including all subcategories

Example response::

    {
        "count": 1520,
        "rows": [
            {
                "id": 1,
                "name": "Product A",
                "default_code": "PROD-A",
                "category": "All / Primary",
                "tags": [{"id": 5, "name": "Featured"}],
                "standard_price": 12.50,
                "qty_available": 24.0,
                "is_secondary": false
            },
            ...
        ],
        "secondary_on_hand": 42.0,
        "secondary_rows": [
            {"id": 12, "name": "Secondary Item", "default_code": "SEC-12", "category": "All / Secondary", "qty_available": 10.0},
            ...
        ]
    }

Known Issues / Roadmap
======================

* Currently supports only read access
* More endpoints and filtering options may be added in future

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: http://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: http://futural.fi/

This module is maintained by Futural Oy
