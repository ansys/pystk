AircraftCruise
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftCruise

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft cruise category of an Aviator aircraft.

.. py:currentmodule:: AircraftCruise

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_basic_cruise_by_name`
              - Get the basic cruise model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_advanced_cruise_by_name`
              - Get the advanced cruise model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCruise.get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftCruise



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicCruiseModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicCruiseModel`

.. py:method:: get_basic_cruise_by_name(self, name: str) -> AircraftBasicCruiseModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_basic_cruise_by_name

    Get the basic cruise model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftBasicCruiseModel`

.. py:method:: get_advanced_cruise_by_name(self, name: str) -> AircraftAdvancedCruiseModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_advanced_cruise_by_name

    Get the advanced cruise model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftAdvancedCruiseModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCruise.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

