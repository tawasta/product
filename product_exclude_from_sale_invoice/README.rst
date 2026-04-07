.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Product: Exclude from Sale Invoice
==================================

* Adds a new field to products, enabling to always exclude 
  them from invoices when sale orders get invoiced.

Configuration
=============
* Set the "Exclude from Sale Invoices" toggle on the product 
  templates of your choice

Usage
=====
* Create invoice from a Sale Order that has an
  invoice-excluded product in it.
* The product will not appear on the invoice.

Known issues / Roadmap
======================
* The module is created for a very specific use case where you 
  want e.g. an event ticket to show up with full price on 
  website, but not have it get invoiced. It is probably not
  useful in very many situations in general.

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
