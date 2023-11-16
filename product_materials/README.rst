.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Product Materials
=================

* This module adds support for providing information about what materials (e.g. wood, cardboard, copper) either a) the product variant itself, 
  or b) the product variant's packaging consists of. (called "Material Compositions")
* The material hierarchy provided by this module is

  * Material Class (top level)
  * Material
  * Material Sublevel (bottom level)

* Supports configuring if you want to track

  * materials for both the product and its packaging, or just one of them
  * how much of the material weighs
  * how much of the material originates from recycled contents
  * what kind of waste results from each material

* Note: you may also want to install product_material_compliant which adds the possibility to define e.g. REACH, ROHS, Halogen compliances for each Material Composition

Configuration
=============
* Enable which material compositions you want to be shown to user by checking the relevant checkboxes in Inventory -> Configuration -> Settings
* In the same menu, configure if you want to 

  * track the material weights
  * track the amounts of recycled contents in materials
  * track the waste components of materials
  * give the user the option to show material info on sale and picking related printouts

* Add top level classes for the materials in Inventory -> Configuration -> Product Material Classes
* Add the materials and whether they are related to products or packaging or both in Inventory -> Configuration -> Product Materials
* Add the material sublevels in Inventory -> Configuration -> Product Material Sublevels
* Add the waste endpoints in Inventory -> Configuration -> Waste Components
* Add the waste components in Inventory -> Configuration -> Waste Components

Usage
=====
* Once configuration is done, open a product variant page and fill in the appropriate material and waste information
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
