AircraftBasicTakeoffModel
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic takeoff performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicTakeoffModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.set_takeoff_speed`
              - Set the takeoff speed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.set_departure_speed`
              - Set the departure speed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.takeoff_speed`
              - Get the speed to which the aircraft accelerates on its ground roll for takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.takeoff_speed_type`
              - Get the takeoff speed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.sea_level_ground_roll`
              - Get or set the distance the aircraft travels along the ground while accelerationg to takeoff at sea level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.departure_speed`
              - Get the aircraft's speed upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.departure_speed_type`
              - Get the departure speed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.use_aerodynamic_propulsion_fuel`
              - Get or set whether to use Aero/Propulsion fuel flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.scale_fuel_flow_by_non_std_density`
              - Get or set whether to scale fuel flow by non std density.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.acceleration_fuel_flow`
              - Get or set the aircraft's fuel flow rate while accelerating during takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.departure_fuel_flow`
              - Get or set the aircraft's fuel flow rate at departure speed.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicTakeoffModel


Property detail
---------------

.. py:property:: takeoff_speed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.takeoff_speed
    :type: float

    Get the speed to which the aircraft accelerates on its ground roll for takeoff.

.. py:property:: takeoff_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.takeoff_speed_type
    :type: AirspeedType

    Get the takeoff speed type.

.. py:property:: sea_level_ground_roll
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.sea_level_ground_roll
    :type: float

    Get or set the distance the aircraft travels along the ground while accelerationg to takeoff at sea level.

.. py:property:: departure_speed
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.departure_speed
    :type: float

    Get the aircraft's speed upon leaving the ground.

.. py:property:: departure_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.departure_speed_type
    :type: AirspeedType

    Get the departure speed type.

.. py:property:: use_aerodynamic_propulsion_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.use_aerodynamic_propulsion_fuel
    :type: bool

    Get or set whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Get or set whether to scale fuel flow by non std density.

.. py:property:: acceleration_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.acceleration_fuel_flow
    :type: float

    Get or set the aircraft's fuel flow rate while accelerating during takeoff.

.. py:property:: departure_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.departure_fuel_flow
    :type: float

    Get or set the aircraft's fuel flow rate at departure speed.


Method detail
-------------



.. py:method:: set_takeoff_speed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.set_takeoff_speed

    Set the takeoff speed of the aircraft.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`





.. py:method:: set_departure_speed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.set_departure_speed

    Set the departure speed of the aircraft.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`









.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicTakeoffModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

