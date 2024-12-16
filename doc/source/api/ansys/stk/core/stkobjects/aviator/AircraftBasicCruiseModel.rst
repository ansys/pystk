AircraftBasicCruiseModel
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic cruise performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicCruiseModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.ceiling_altitude`
              - Gets or sets the maximum altitude above mean sea level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.default_cruise_altitude`
              - Gets or sets the aircraft's default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.use_aerodynamic_propulsion_fuel`
              - Opt to use the fuel flow calculated by the acceleration performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.scale_fuel_flow_by_non_std_density`
              - Opt to scale the fuel flow by the aircraft's actual altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.airspeed_type`
              - Gets or sets the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.min_airspeed`
              - Gets or sets the minimum cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_endurance_airspeed`
              - Gets or sets the cruising airspeed that will provide the maximum flying time for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_range_airspeed`
              - Gets or sets the maximum range cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_airspeed`
              - Gets or sets the maximum cruisng airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_performance_airspeed`
              - Gets or sets the custom performance airspeed that can be used to model specific flight conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.min_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the minimum cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_endurance_fuel_flow`
              - Gets or sets the fuel flow for the maximum endurance cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_range_fuel_flow`
              - Gets or sets the fuel flow for the maximum range cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the maximum cruising airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_performance_airspeed_fuel_flow`
              - Gets or sets the fuel flow for the maximum performance cruising airspeed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicCruiseModel


Property detail
---------------

.. py:property:: ceiling_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.ceiling_altitude
    :type: float

    Gets or sets the maximum altitude above mean sea level.

.. py:property:: default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.default_cruise_altitude
    :type: float

    Gets or sets the aircraft's default cruise altitude.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Opt to use the fuel flow calculated by the acceleration performance model.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Opt to scale the fuel flow by the aircraft's actual altitude.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.airspeed_type
    :type: AirspeedType

    Gets or sets the airspeed type.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.min_airspeed
    :type: float

    Gets or sets the minimum cruising airspeed.

.. py:property:: max_endurance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_endurance_airspeed
    :type: float

    Gets or sets the cruising airspeed that will provide the maximum flying time for the aircraft.

.. py:property:: max_range_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_range_airspeed
    :type: float

    Gets or sets the maximum range cruising airspeed.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_airspeed
    :type: float

    Gets or sets the maximum cruisng airspeed.

.. py:property:: max_performance_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_performance_airspeed
    :type: float

    Gets or sets the custom performance airspeed that can be used to model specific flight conditions.

.. py:property:: min_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.min_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the minimum cruising airspeed.

.. py:property:: max_endurance_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_endurance_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum endurance cruising airspeed.

.. py:property:: max_range_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_range_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum range cruising airspeed.

.. py:property:: max_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum cruising airspeed.

.. py:property:: max_performance_airspeed_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.max_performance_airspeed_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum performance cruising airspeed.


Method detail
-------------































.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicCruiseModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

