AircraftModel
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IAviatorVehicle`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining an aircraft in Aviator.

.. py:currentmodule:: AircraftModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.performance_model_types`
              - Get the types of performance models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.acceleration`
              - Get the acceleration interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.climb`
              - Get the climb interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.cruise`
              - Get the cruise interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.descent`
              - Get the descent interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.landing`
              - Get the landing interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.takeoff`
              - Get the takeoff interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.default_configuration`
              - Get the aircraft's default configuration as saved in the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.advanced_fixed_wing_tool`
              - Get the Advanced Fixed Wing Tool for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.vtol`
              - Get the VTOL interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModel.terrain_follow`
              - Get the TerrainFollow interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftModel


Property detail
---------------

.. py:property:: performance_model_types
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.performance_model_types
    :type: list

    Get the types of performance models.

.. py:property:: acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.acceleration
    :type: IAircraftAcceleration

    Get the acceleration interface.

.. py:property:: climb
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.climb
    :type: IAircraftClimb

    Get the climb interface.

.. py:property:: cruise
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.cruise
    :type: IAircraftCruise

    Get the cruise interface.

.. py:property:: descent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.descent
    :type: IAircraftDescent

    Get the descent interface.

.. py:property:: landing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.landing
    :type: IAircraftLanding

    Get the landing interface.

.. py:property:: takeoff
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.takeoff
    :type: IAircraftTakeoff

    Get the takeoff interface.

.. py:property:: default_configuration
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.default_configuration
    :type: IConfiguration

    Get the aircraft's default configuration as saved in the catalog.

.. py:property:: advanced_fixed_wing_tool
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.advanced_fixed_wing_tool
    :type: IAdvancedFixedWingTool

    Get the Advanced Fixed Wing Tool for the aircraft.

.. py:property:: vtol
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.vtol
    :type: IAircraftVTOL

    Get the VTOL interface.

.. py:property:: terrain_follow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.terrain_follow
    :type: IAircraftTerrainFollow

    Get the TerrainFollow interface.


Method detail
-------------










.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`



