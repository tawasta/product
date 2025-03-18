.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================
Product Compliance
==================

* A module for managing various types of compliance for product templates
* Compliance types by default share the same possible values, which can be added/configured in settings (e.g. "Yes", "No", "Not Applicable"). You can also set 
  a value to be specific to only for a single compliance (e.g. REACH)
* You can also configure in settings which of the supported compliance type fields should be shown and which are irrelevant and can be hidden from users altogether
* Currently supported compliance types:

  * ATEX Compliant
  * REACH Compliant
  * RoHS Compliant
  * Composition Checked
  * MSDS (Material Safety Data Sheet) Checked
  * Work Safety Checked

Configuration
=============
* Enable which of the above compliance types you want to be shown to user by checking the relevant checkboxes in Sales -> Configuration -> Product Compliance Types
* Add the possible values that should be allowed for selection in Sales -> Configuration -> Product Compliance Values

Usage
=====
* Once configuration is done, open a product template's page and fill in the appropriate compliance values 

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Miika Nissi <miika.nissi@tawasta.fi>
* Valtteri Lattu <valtteri.lattu@tawasta.fi>
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: https://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: https://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
