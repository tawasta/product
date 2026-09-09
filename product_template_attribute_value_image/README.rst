.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================
Product Template Attribute Value Image
======================================

* Adds an "Attribute Images" section on the product template's
  "Attributes & Variants" tab, where one image can be uploaded per
  attribute value (e.g. one image per lampshade color) instead of one
  image per variant.
* Adds ``product.product._get_attribute_value_image()``, which resolves
  a variant's image from its own attribute values via the images
  configured on its template. Not wired into any report or view by
  itself - that is a separate follow-up task.

Configuration
=============
* None needed

Usage
=====
* Open a product template, go to "Attributes & Variants", and add rows
  to "Attribute Images": one image per relevant attribute value.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/web/image/website/1/logo/Futural
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
