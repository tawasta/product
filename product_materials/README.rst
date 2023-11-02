.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Product Materials
=================

* This module adds support for providing information about what materials (e.g. wood, cardboard, copper) either a) the product itself, 
  or b) the product's packaging consists of. (called "Material Compositions")
* Supports configuring if you want to keep track of materials for both the product and its packaging, or just one of them
* Supports configuring if you want to track how much of the material originates from recycled contents
* Note: the module depends on product_compliant to add additional compliances that are managed at Material Composition level:

  * Halogen Compliant
  * Conflict Minerals Compliant


Configuration
=============
* Enable which material compositions you want to be shown to user by checking the relevant checkboxes in Inventory -> Configuration -> Settings
* In the same menu, configure if you want to track the amounts of recycled material
* In the same menu, configure if you want to give the user the option to show material info on sale and picking related printouts
* In the same menu, configure if you want to track the waste components
* Add top level classes for the materials in Inventory -> Configuration -> Product Material Classes
* Add the materials and whether they are related to products or packaging or both in Inventory -> Configuration -> Product Materials
* Add top level classes for the waste components in Inventory -> Configuration -> Waste Components Classes
* Add the individual Waste Components in Inventory -> Configuration -> Waste Components

Usage
=====
* Once configuration is done, open a product template page and fill in the appropriate material and waste information
* When entering a Sale Order (and the "Show materials on reports" feature is enabled), select on the Sale Order page if the SO's related prints should contain the product material information.
  This will affect the Invoice print and the Delivery Slip print

Known issues / Roadmap
======================
* Support toggling off if you want to track and categorize the type of waste components that result from the materials 
* Print-related features still work-in-progress

Credits
=======

Contributors
------------
* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
