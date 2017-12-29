.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================================
Incoming Shipments Quality Checks
=================================

* Extends the functionality of the Product Quality Instructions module
* When incoming shipments arrive, quality checks have to be completed according to the products' quality instructions before goods can be marked as received
* Completion is marked by checking a checkbox for each quality instruction related to the incoming products

Configuration
=============
* Add some quality instructions to products from product form view or Warehouse -> Products -> Quality instructions

Usage
=====
* Mark all quality checks as completed in the Quality Checks tab in the Receipt form when receiving goods
* If the Transfer button is clicked before completing all checks, an error message is shown
* The required quality checks are calculated when the Receipt document is generated
* If you e.g. add new quality instructions to product or edit the receipt's lines, you can click the Reset Quality Checks button on the Receipt form to reload the list

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
