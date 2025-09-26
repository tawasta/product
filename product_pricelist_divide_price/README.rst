.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================
Divide the result in pricelist rule
===================================

Adds Didide By -field to pricelist rule. This field divides the amount
in Based on -field and other calculations are done after the division.

Texts in example and info -fields are changed to show how Divide By -field
is used.

Note that the same result can be achieved by using 100 * (1 - 1/x) formula
for Discount field where x is the value in Divide by -field. But this is
not done, because Discount should be possible to be used together with
Divide By -field.

Configuration
=============
Create pricelists to use the module.

Usage
=====
Select a pricelist and its item. The Computation needs to be selected as
"Formula". Then write a number to Divide By -field and see how pricelist
item behaves now.

Known issues / Roadmap
======================
The module modifies the computing logic in pricelist. So be wary how
pricelist functions together with other modules, which try to change
the functionalities of pricelists.

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
