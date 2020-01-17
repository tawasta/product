.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Product Primary Vendor Info
===========================

* New fields for indicating product's primary vendor's info: vendor's name,
  product code and price
* Shows the fields also in product treeview
* Fields can be utilized as helpers to show the data also in other models
  (e.g. purchase request lines or BOM lines)
* Also adds an informational "Cost Price (vendor based)" field to product form
  that converts the primary vendor's price to the default currency, and does
  conversion from purchase UoM to product's own UoM. I.e. it tells what does 
  it cost in company currency to buy one <UoM> of the product. This does not
  affect stock valuation, and is only additional information

Configuration
=============
\-

Usage
=====
* Add some vendor info rows to products and open the product tree view

Known issues / Roadmap
======================
* Variant support not implemented

Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: https://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: https://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
