.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================================================
Product Materials: show on product template form
================================================

* Brings the Material Compositions (that are normally variant-specific and only shown on the variant form) to be shown in the Product Template form view
* Important: this module is ONLY needed if the Odoo installation is not using Product Variants. Otherwise do not install it, as it expects there to be a single variant per product template.

Configuration
=============
* Just install the module

Usage
=====
* Open a product template form, and the Material Composition fields show up in a new notebook tab.

Known issues / Roadmap
======================
* Consider making the "editable=bottom" setting toggleable on/off. Currently it is always on, since in current use cases for template-based material info there are not many fields being shown.

Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
