AircraftTakeoff
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftTakeoff

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft takeoff category of an Aviator aircraft.

.. py:currentmodule:: AircraftTakeoff

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_advanced_takeoff_by_name`
              - Get the advanced Takeoff model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_basic_takeoff_by_name`
              - Get the basic Takeoff model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_built_in_model`
              - Get the built-in model.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftTakeoff



Method detail
-------------

.. py:method:: get_advanced_takeoff_by_name(self, name: str) -> AircraftAdvancedTakeoffModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_advanced_takeoff_by_name

    Get the advanced Takeoff model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftAdvancedTakeoffModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: get_basic_takeoff_by_name(self, name: str) -> AircraftBasicTakeoffModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_basic_takeoff_by_name

    Get the basic Takeoff model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftBasicTakeoffModel`

.. py:method:: get_built_in_model(self) -> AircraftBasicTakeoffModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTakeoff.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicTakeoffModel`

