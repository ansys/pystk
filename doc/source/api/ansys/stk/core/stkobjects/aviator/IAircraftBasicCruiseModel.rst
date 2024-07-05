IAircraftBasicCruiseModel
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel

   object
   
   Interface used to access the basic cruise model options for a cruise model of an aircraft in the Aviator catalog.

.. py:currentmodule:: IAircraftBasicCruiseModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.ceiling_altitude`
              - Gets or sets the maximum altitude above mean sea level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.default_cruise_altitude`
              - Gets or sets the aircraft's default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.use_aero_prop_fuel`
              - Opt to use the fuel flow calculated by the acceleration performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.scale_fuel_flow_by_non_std_density`
              - Opt to scale the fuel flow by the aircraft's actual altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.airspeed_type`
              - Gets or sets the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.min_airspeed`
              - Gets or sets the minimum cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_endurance_airspeed`
              - Gets or sets the cruising airspeed that will provide the maximum flying time for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_range_airspeed`
              - Gets or sets the maximum range cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_airspeed`
              - Gets or sets the maximum cruisng airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_perf_airspeed`
              - Gets or sets the custom performance airspeed that can be used to model specific flight conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.min_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the minimum cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_endurance_fuel_flow`
              - Gets or sets the fuel flow for the maximum endurance cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_range_fuel_flow`
              - Gets or sets the fuel flow for the maximum range cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the maximum cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_perf_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the maximum performance cruising airspeed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftBasicCruiseModel


Property detail
---------------

.. py:property:: ceiling_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.ceiling_altitude
    :type: float

    Gets or sets the maximum altitude above mean sea level.

.. py:property:: default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.default_cruise_altitude
    :type: float

    Gets or sets the aircraft's default cruise altitude.

.. py:property:: use_aero_prop_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.use_aero_prop_fuel
    :type: bool

    Opt to use the fuel flow calculated by the acceleration performance model.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Opt to scale the fuel flow by the aircraft's actual altitude.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.airspeed_type
    :type: AIRSPEED_TYPE

    Gets or sets the airspeed type.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.min_airspeed
    :type: float

    Gets or sets the minimum cruising airspeed.

.. py:property:: max_endurance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_endurance_airspeed
    :type: float

    Gets or sets the cruising airspeed that will provide the maximum flying time for the aircraft.

.. py:property:: max_range_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_range_airspeed
    :type: float

    Gets or sets the maximum range cruising airspeed.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_airspeed
    :type: float

    Gets or sets the maximum cruisng airspeed.

.. py:property:: max_perf_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_perf_airspeed
    :type: float

    Gets or sets the custom performance airspeed that can be used to model specific flight conditions.

.. py:property:: min_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.min_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the minimum cruising airspeed.

.. py:property:: max_endurance_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_endurance_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum endurance cruising airspeed.

.. py:property:: max_range_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_range_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum range cruising airspeed.

.. py:property:: max_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum cruising airspeed.

.. py:property:: max_perf_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.max_perf_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum performance cruising airspeed.


Method detail
-------------































.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicCruiseModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

