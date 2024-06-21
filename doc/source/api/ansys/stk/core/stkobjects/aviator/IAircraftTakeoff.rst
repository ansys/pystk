IAircraftTakeoff
================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftTakeoff

   object
   
   Interface used to access the takeoff options for an aircraft in the Aviator catalog.

.. py:currentmodule:: IAircraftTakeoff

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_basic_takeoff_by_name`
              - Get the basic Takeoff model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_advanced_takeoff_by_name`
              - Get the advanced Takeoff model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftTakeoff



Method detail
-------------

.. py:method:: get_built_in_model(self) -> IAircraftBasicTakeoffModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~IAircraftBasicTakeoffModel`

.. py:method:: get_basic_takeoff_by_name(self, name: str) -> IAircraftBasicTakeoffModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_basic_takeoff_by_name

    Get the basic Takeoff model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftBasicTakeoffModel`

.. py:method:: get_advanced_takeoff_by_name(self, name: str) -> IAircraftAdvancedTakeoffModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_advanced_takeoff_by_name

    Get the advanced Takeoff model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftAdvancedTakeoffModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTakeoff.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

