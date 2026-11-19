.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================================
Product Materials on Product template
=====================================

Enable to set materials also on product templates.

* The product form has a Materials tab with the product material and the
  packaging material compositions of the product template
* A material added to a product with one variant is linked also to the variant
* A material added to a product with several variants is linked only to the
  product template
* The material composition list has a Product Template column

This is meant to be merged later with product_materials module, but this merge
needs to be checked so that already created materials on variants will not be
affected by this change.

Configuration
=============
Enable product materials and/or packaging materials in the product materials
settings. Set materials the same way as is done in product variants.

Usage
=====
Select a product and create materials for it on the Materials tab.

An administrator can fill in missing links on previously created materials:
select the materials in the Product Material Composition list and run
Action > Update Product Template.

* A material with only a variant gets the product template of the variant
* A material with only a product template gets the variant, if the product has
  one variant
* Links that are already set are never removed

Changes in 19.0
===============
The following bugs of the 17.0 version were fixed in 19.0. Each was tested in
the 17.0 user interface before the fix.

* **Product and packaging materials were mixed on the product template.**
  In 17.0 both lists on the Materials tab showed all materials of the product
  template, so a product material was also shown as a packaging material and
  the other way round. In 19.0 the lists are filtered by the material type, as
  they are on product variants.
* **The delivery package flag of the product template was not updated.**
  In 17.0 the value was computed only when the product template was created.
  In 19.0 it follows the delivery package flag of the variant of a product with
  one active variant (an archived product with one variant keeps its value).
  Existing values are recomputed when the module is upgraded.
* **The product material list was shown without permission.** In 17.0 a user
  who could manage only packaging materials saw also the product material list
  (without its heading) on the Materials tab. In 19.0 the list is shown only to
  users who can manage product materials, like the packaging material list.

Known issues / Roadmap
======================
* Consider merging this module with product_materials.
* Materials that the 17.0 Update Product Template action has already detached
  from their products cannot be relinked automatically.

Credits
=======

Contributors
------------

* Timo Kekäläinen <timo.kekalainen@tawasta.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy.
