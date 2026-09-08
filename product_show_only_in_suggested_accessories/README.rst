.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==========================================
Product Show only in Suggested accessories
==========================================

* Add a dot to the product shop settings to remove the product from /shop 
view and also from its searches / categories. The product will then only 
appear in Suggested Accessories.

Configuration
=============
\-

Usage
=====
\-

Known issues / Roadmap
======================
\-

Changelog
=========
* Changes during v17 -> v19 migration:
  - Added main to __init__.py in controllers, previously logic was not 
  loading at all.
  - Added the needed parameters to the _shop_lookup_products(), to 
  adhere to the v19 core changes.
  - Added filtering to actually hide the products from the /shop view.

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>
* Joonas Lahtinen <joonas.lahtinen@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
