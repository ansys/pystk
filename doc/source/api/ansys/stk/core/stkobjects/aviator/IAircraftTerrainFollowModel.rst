IAircraftTerrainFollowModel
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel

   object
   
   Interface used to access the options for a TerrainFollow performance model of an aircraft.

.. py:currentmodule:: IAircraftTerrainFollowModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.airspeed_type`
              - Gets or sets the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.use_aero_prop_fuel`
              - Opt to use the fuel flow calculated by the acceleration performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.scale_fuel_flow_by_non_std_density`
              - Opt to scale the fuel flow by the aircraft's actual altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.min_airspeed`
              - Gets or sets the minimum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_endurance_airspeed`
              - Gets or sets the airspeed that will provide the maximum flying time for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_range_airspeed`
              - Gets or sets the maximum range airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_airspeed`
              - Gets or sets the maximum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_perf_airspeed`
              - Gets or sets the custom performance airspeed that can be used to model specific flight conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.min_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the minimum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_endurance_fuel_flow`
              - Gets or sets the fuel flow for the maximum endurance airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_range_fuel_flow`
              - Gets or sets the fuel flow for the maximum range airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the maximum airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_perf_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the maximum performance airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_pitch_angle`
              - Gets or sets the maximum pitch angle the aircraft will be allowed to use.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.terrain_window`
              - Gets or sets the time interval over which terrain points are sampled.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_load_factor`
              - Get the maximum load factor - during straight and level flight - that the aircraft can bear.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftTerrainFollowModel


Property detail
---------------

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.airspeed_type
    :type: AIRSPEED_TYPE

    Gets or sets the airspeed type.

.. py:property:: use_aero_prop_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.use_aero_prop_fuel
    :type: bool

    Opt to use the fuel flow calculated by the acceleration performance model.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Opt to scale the fuel flow by the aircraft's actual altitude.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.min_airspeed
    :type: float

    Gets or sets the minimum airspeed.

.. py:property:: max_endurance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_endurance_airspeed
    :type: float

    Gets or sets the airspeed that will provide the maximum flying time for the aircraft.

.. py:property:: max_range_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_range_airspeed
    :type: float

    Gets or sets the maximum range airspeed.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_airspeed
    :type: float

    Gets or sets the maximum airspeed.

.. py:property:: max_perf_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_perf_airspeed
    :type: float

    Gets or sets the custom performance airspeed that can be used to model specific flight conditions.

.. py:property:: min_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.min_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the minimum airspeed.

.. py:property:: max_endurance_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_endurance_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum endurance airspeed.

.. py:property:: max_range_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_range_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum range airspeed.

.. py:property:: max_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum airspeed.

.. py:property:: max_perf_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_perf_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum performance airspeed.

.. py:property:: max_pitch_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_pitch_angle
    :type: typing.Any

    Gets or sets the maximum pitch angle the aircraft will be allowed to use.

.. py:property:: terrain_window
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.terrain_window
    :type: float

    Gets or sets the time interval over which terrain points are sampled.

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftTerrainFollowModel.max_load_factor
    :type: float

    Get the maximum load factor - during straight and level flight - that the aircraft can bear.


