.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================================
Product – Ignore minimium quantity when choosing a vendor
=========================================================

The module changes how vendors are selected from a product.
Normally a purchase order line needs to have a quantity that
is at least the same as minimium quantity set on vendor pricelist
of a chosen product. Installing this module changes this behaviour
and the minimium quantity is ignored. Then a seller is chosen
by other criteria and the quantity can be whatever.

Configuration
=============
None needed

Usage
=====
Just install the module and create a purchase order which has a product
with minimium quantity set on its related vendor pricelist. Change
the minimium quantity and see that it does change how a vendor is chosen.

Known issues / Roadmap
======================
This module changes the behaviour of choosing a record from vendor pricelist.
Use this module if you know what you are doing.

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
