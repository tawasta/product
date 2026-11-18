.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================================================
Archive old Revision Products and link them to the new Revision
===============================================================

A scheduled action goes through the products whose Internal Reference has the
pattern "<code> <revision>", for example "12345 B". Products with the same
code are revisions of the same product.

* The newest revision stays active. The older revisions are archived and
  linked to it.
* The linked revisions are shown with the Revisions smart button of the
  newest revision. An archived revision shows its newest revision in the
  Recent product revision field (inventory administrators).
* The vendor prices of the previous revision are copied to the newest
  revision once, when the previous revision is linked to it.

A revision is DEV, 0, 1-9 or A-ZZ, optionally followed by a dot and a number,
for example A.001. The order is DEV and 0 first, then 1-9 or A-ZZ, then the
number after the dot. For example 12345 A, 12345 B and 12345 C are grouped as
12345 and ordered C, B, A. Then A and B are archived and linked to C.

If the two newest revisions of a code have the same order, for example two
products 12345 C, or 12345 1 and 12345 A, or 12345 DEV and 12345 0, the code
is skipped and a warning is logged.

Changes in 19.0
===============
Fixed compared to 17.0:

* A revision with letters after the dot, for example "A.B", stopped the
  whole scheduled action with an error. Such references are now ignored.
* Two products with the same newest reference, for example two "12345 C",
  stopped the whole scheduled action with an error. Now the old revisions of
  that code are left untouched and a warning is logged.
* The number after the dot was compared as a decimal, so A.10 was older than
  A.9. Now it is compared as a whole number.
* The vendor prices of the previous revision were copied again on every run,
  so a price changed on the newest revision got its old price back as a
  second line. Now the prices are copied only once.
* A vendor price of a specific variant of the old revision was copied with
  that variant, so the newest revision never used it in purchases. Now the
  copy applies to all variants of the newest revision.
* The setting code_is_digit was on with any value, also "False". Now 1, True
  or yes turns it on, 0, False or no turns it off, and another value stops
  the scheduled action with an error.
* An error in one product stopped the archiving of all products. Now the
  failing code is skipped and the error is logged.
* The Revisions smart button counted all linked revisions, but listed only
  the archived ones. Now it lists all of them.
* A duplicated archived revision kept the link to the newest revision. Now
  the link is not copied.
* The module did not depend on Inventory although its view uses the
  Inventory administrator group.

Price lines that 17.0 already duplicated are not removed.

Configuration
=============
The scheduled action Archive Old revision products is inactive after the
installation. Activate it to archive old revisions daily.

Optional system parameters:

* archive_code_len: only codes of this length are handled, for example 5.
* code_is_digit: set to 1 to handle only codes that contain only digits.

Usage
=====
Activate the scheduled action, or run it manually from Settings > Technical >
Scheduled Actions.

Known issues / Roadmap
======================
* Archiving is based only on the Internal Reference. Check the references
  before activating the scheduled action to avoid unwanted archiving.
* Products of different companies with the same code are handled as one
  product, as in 17.0. Then the vendor prices of one company can be copied to
  the product of another company.
* If the old revision had different prices for its variants with the same
  vendor and quantity, the newest revision gets all of them, and purchases
  use the cheapest.
* An archived newest revision is still the newest: the older revisions are
  archived and linked to it, as in 17.0.

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
