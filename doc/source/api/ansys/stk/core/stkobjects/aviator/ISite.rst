ISite
=====

.. py:class:: ansys.stk.core.stkobjects.aviator.ISite

   Interface to access Site options.

.. py:currentmodule:: ISite

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISite.name`
              - Get or set the name of the site.


Examples
--------

Rename a procedure and its site

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Rename the procedure
    procedure.name = "New Procedure"
    # Get the site corresponding to the procedure
    site = procedure.site
    # Rename the site
    site.name = "New Site"


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISite


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.ISite.name
    :type: str

    Get or set the name of the site.


