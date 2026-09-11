.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================================
Direct to Invetory Adjustment from Update Quantity
==================================================

With this module, a user is directed to an inventory adjustment form view
upon clicking on Update Quantity functionality on the product (the
"Update Quantity" button in the forecasted view and the On Hand quantity
link on the product form).

OCA's stock_inventory module is used to create the inventory adjustment.

Configuration
=============
\-

Usage
=====
* Install this Module from Apps

Known issues / Roadmap
======================
\-

Credits
=======

Changelog
=========
* Changes during migration v17 -> v19:
   * Python changes:
      * Added stock dependency
      * Overrode action_open_quants to accommodate changes in core stock module
   * View changes:
      * procudt_view.xml deleted, none of the inherited views exist in v19

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@futural.fi>
* Joonas Lahtinen <joonas.lahtinen@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/
   
This module is maintained by Futural Oy
