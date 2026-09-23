.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Product: Exclude from Sale Invoice
==================================

* Adds a new computed field to products, enabling to always exclude 
  them from invoices when sale orders get invoiced.
* The field is managed by rules for product type + customer tax combinations
* Company-specific rules are supported in multicompany setups
* Intended for a specific use case where event tickets that are sold 
  with tax are processed entirely separately from those that are sold without
  tax. The module is probably not useful in very many situations in general.
  
  * VAT-less tickets' sales of organization/yhdistys are handled and invoiced as usual in Odoo
  * Ticket sales with VAT do not get invoices nor get processed in Accounting. A simple 
    summary export report is created of them from the related Sale Orders (not by this module)

Configuration
=============
* Create product type / tax combination rules via
  Invoicing - Configuration - Sale Invoice Exclusion Rules
  to define the combinations where products should not be
  invoiced from Sale Orders.

  * For example: Event Tickets with VAT 25.5%

* Note that when setting rules, each rule looks for an exact match,
  so if you happen to have multiple taxes defined for a product,
  also the rule should have them defined.
* Product templates' 'Exclude from Sale Invoices' field gets
    toggled on/off automatically based on the rules. 
* Sale order lines store the product's exclusion when the line is
  created (or its product is changed). Changing rules affects only
  sale order lines created afterwards.

Usage
=====
* Create invoice from a Sale Order that has an
  invoice-excluded product in it.
* The product will not appear on the invoice.

Known issues / Roadmap
======================
\-

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
