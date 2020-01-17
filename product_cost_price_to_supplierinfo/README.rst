.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================================
Copy Product Cost Price to Supplierinfo
=======================================

* Creates product.supplierinfo lines from products' cost price
* Intended for situations where purchase price has previously been stored
  in the product form, but now FIFO is going to be used, so the prices should be
  stored elsewhere to avoid being overwritten.
* Logic of the copying process:
  
  1) If a supplierinfo row exists for some partner, create another with the cost
     price applied. The new one gets a higher priority (lower sequence). Old
     rows can be deleted manually later if so wanted.
  2) If a row does not exist, create one by finding what partner the product was 
     previously purchased from
  3) If no purchase orders exist, create the supplierinfo row with a placeholder
     supplier

* All supplierinfo rows created this way get flagged with 
  "Created from cost price = True" for later inspection / debugging

Configuration
=============
* Grant a user the "Can copy product cost price to supplierinfo" permission. 
  Granting it to others than the admin account is not recommended.

Usage
=====
* Open the product list, check the products you want to process (probably all of
  the purchasable ones), and click action -> Copy cost price to supplierinfo
* Click confirm.

Known issues / Roadmap
======================
* The module was created for a specific use case in mind: moving the prices
  just after a migration from a variantless 7.0 installation to 10.0 but before 
  starting to use FIFO valuation. 
* Usefulness of the module in other cases is probably quite limited, or at 
  least will require customization of the code.

Credits
=======

Contributors
------------
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: https://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: https://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
