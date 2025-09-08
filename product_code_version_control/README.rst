.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Control version codes of a product
==================================

Create version control codes for a product. This module is meant to be used
to refer earlier version codes and this functionality is used in searching
products with possible old product codes.

At this moment the module works in sales and in product views.

In sales form the written search term is added to "Searched code" field with
JavaScript code.

Configuration
=============
No special configuration is required, but version code records are needed
to be created to use this module. Do this after installing the module.

Usage
=====
Select a product and click on "Version codes" button. Begin creating a version
control record and try to refer to an existing product code. Write this to Code
version -field. Different checks are in use to prevent creating a duplicate
version control record. Also the user is noted if a product which is meant to
be referenced does not exist with the particular code.

Go then to product tree view and search products with added Code version information.
The product with the created version control record is shown on that list. The similar
behaviour happend in sale order form.

Known issues / Roadmap
======================
There are no known issues with this module.

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
