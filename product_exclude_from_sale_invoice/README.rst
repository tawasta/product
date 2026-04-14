.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Product: Exclude from Sale Invoice
==================================

* Adds a new field to products, enabling to always exclude 
  them from invoices when sale orders get invoiced.
* Supports either manual configuration for each product, or configuring
  rules for product type + customer tax combinations
* Company-specific rules are supported in multicompany setups

Configuration
=============
* Optionally: Create product type / tax combination rules via 
  Invoicing - Configuration - Sale Invoice Exclusion Rules
  to define the combinations where products should not be 
  invoiced from Sale Orders. 

  * If this is done, product templates' 'Exclude from Sale Invoices'
    field gets toggled on/off automatically based on the rules
    without any manual control from user.
  * If this is NOT done, you will manage all product templates' 
    'Exclude from Sale Invoices' fields manually
* Note that when setting rules, each rule looks for an exact match,
  so if you happen to have multiple taxes defined for a product,
  also the rule should have them defined.
* A simple example combination could be e.g.  "Event Ticket" / "25,5% VAT".

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
