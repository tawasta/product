.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================================================================
Product: 'On Hand Quantity' Button Opens Readonly View by Default
=================================================================

* Only users in a specific access group see core's editable list view,
  other users get redirected to a readonly view
* Intended for situations where you want to limit that the inventory
  adjustments should be done via the Physical Inventory menu

Configuration
=============
* If you want the Odoo standard On Hand Quantity button to show for
  some users, add them to the new 'Allow Updating On Hand 
  Quantity from Product View' group

Usage
=====
* Go to product template or variant form view and click the 
  On Hand button. A readonly or editable view will open,
  based on the groups you are in.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
