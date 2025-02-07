AircraftTerrainFollowModel
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel

   Class defining the TerrainFollow performance model of an aircraft.

.. py:currentmodule:: AircraftTerrainFollowModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.airspeed_type`
              - Get or set the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.use_aerodynamic_propulsion_fuel`
              - Opt to use the fuel flow calculated by the acceleration performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.scale_fuel_flow_by_non_std_density`
              - Opt to scale the fuel flow by the aircraft's actual altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.min_airspeed`
              - Get or set the minimum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_endurance_airspeed`
              - Get or set the airspeed that will provide the maximum flying time for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_range_airspeed`
              - Get or set the maximum range airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_airspeed`
              - Get or set the maximum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_performance_airspeed`
              - Get or set the custom performance airspeed that can be used to model specific flight conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.min_airspeed_fuel_flow`
              - Get or set the fuel flow for the minimum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_endurance_fuel_flow`
              - Get or set the fuel flow for the maximum endurance airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_range_fuel_flow`
              - Get or set the fuel flow for the maximum range airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_airspeed_fuel_flow`
              - Get or set the fuel flow for the maximum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_performance_airspeed_fuel_flow`
              - Get or set the fuel flow for the maximum performance airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_pitch_angle`
              - Get or set the maximum pitch angle the aircraft will be allowed to use.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.terrain_window`
              - Get or set the time interval over which terrain points are sampled.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_load_factor`
              - Get the maximum load factor - during straight and level flight - that the aircraft can bear.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftTerrainFollowModel


Property detail
---------------

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.airspeed_type
    :type: AirspeedType

    Get or set the airspeed type.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Opt to use the fuel flow calculated by the acceleration performance model.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Opt to scale the fuel flow by the aircraft's actual altitude.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.min_airspeed
    :type: float

    Get or set the minimum airspeed.

.. py:property:: max_endurance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_endurance_airspeed
    :type: float

    Get or set the airspeed that will provide the maximum flying time for the aircraft.

.. py:property:: max_range_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_range_airspeed
    :type: float

    Get or set the maximum range airspeed.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_airspeed
    :type: float

    Get or set the maximum airspeed.

.. py:property:: max_performance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_performance_airspeed
    :type: float

    Get or set the custom performance airspeed that can be used to model specific flight conditions.

.. py:property:: min_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.min_airspeed_fuel_flow
    :type: float

    Get or set the fuel flow for the minimum airspeed.

.. py:property:: max_endurance_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_endurance_fuel_flow
    :type: float

    Get or set the fuel flow for the maximum endurance airspeed.

.. py:property:: max_range_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_range_fuel_flow
    :type: float

    Get or set the fuel flow for the maximum range airspeed.

.. py:property:: max_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_airspeed_fuel_flow
    :type: float

    Get or set the fuel flow for the maximum airspeed.

.. py:property:: max_performance_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_performance_airspeed_fuel_flow
    :type: float

    Get or set the fuel flow for the maximum performance airspeed.

.. py:property:: max_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_pitch_angle
    :type: typing.Any

    Get or set the maximum pitch angle the aircraft will be allowed to use.

.. py:property:: terrain_window
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.terrain_window
    :type: float

    Get or set the time interval over which terrain points are sampled.

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftTerrainFollowModel.max_load_factor
    :type: float

    Get the maximum load factor - during straight and level flight - that the aircraft can bear.


