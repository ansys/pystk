IAircraftModels
===============

.. py:class:: IAircraftModels

   object
   
   Interface for the User Aircraft Models in the Aviator Catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_aircraft`
              - Get the aircraft with the given name.
            * - :py:meth:`~add_aircraft`
              - Create a new aircraft with the given name.
            * - :py:meth:`~get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftModels



Method detail
-------------

.. py:method:: get_aircraft(self, aircraftName: str) -> IAircraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModels.get_aircraft

    Get the aircraft with the given name.

    :Parameters:

    **aircraftName** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftModel`

.. py:method:: add_aircraft(self, aircraftName: str) -> IAircraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModels.add_aircraft

    Create a new aircraft with the given name.

    :Parameters:

    **aircraftName** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

