.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

============================
Product Materials Compliance
============================

* A module for managing various types of compliance for Product Material Compositions
* Extends the functionality of product_compliant module that provides the concept of Compliance values (e.g. REACH Certified = yes) and enables linking them to Products. 
  Install this module only if you need to go to a more specific level and link the Compliance values to invididual Product Material Compositions.
* Currently supported compliance types for materials:

  * Chemicals Compliant
  * Conflict Area Minerals Compliant
  * Halogen Compliant
  * POP (Persistent Organic Pollutants) Compliant
  * REACH Compliant
  * RoHS Compliant
  * SCIP (Substances of Concern in Products) Compliant

Configuration
=============
* Enable which of the above compliance types you want to be shown to user by checking the relevant checkboxes in Sales -> Configuration -> Product Compliance Types
  
  * Note: pay attention to if you're enabling the compliance type for the Product or the Product Material, as both settings are present in the view

* Add the possible values that should be allowed for selection in Sales -> Configuration -> Product Compliance Values
* In the same view, drag the Compliance Values into their correct order. The one that is highest up for each "Selectable For" gets suggested as default in material's compliancy dropdowns.

Usage
=====
* Once configuration is done, open a product variant's page and fill in the appropriate compliance values for its Product Material Composition lines

Known issues / Roadmap
======================
* Consider making it possible to toggle on/off defaulting to the compliancy with lowest sequence (currently always on) 

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
