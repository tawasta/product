.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================================================
Archive old Revision Products and link them to the new Revision
===============================================================

::

    Go through products with similar internal reference patterns.
    This kind of search is used to identify old revisions of a product.
    Then the found old revisions is archived.

    Internal reference needs to have a similar pattern. Right now
    the pattern needs to be "12345 A", meaning first 5 characters
    in a string needs to be a number and the character after it
    needs to be a letter.

    The old revisions are linked to the new product revision.
    These can be seen in product template form view with
    Revision smart button.

    The previous revision copies its vendor pricelist to the
    newest product revision.

Configuration
=============
::

    A scheduled action is first set as inactive. Activate it to
    periodically archive old revisions.

Usage
=====
::

    Use the added scheduled action to archve old revisions of a product.

Known issues / Roadmap
======================
::

    This module does not break anything. Understand when archiving
    happens to avoid unwanted behaviour.

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
