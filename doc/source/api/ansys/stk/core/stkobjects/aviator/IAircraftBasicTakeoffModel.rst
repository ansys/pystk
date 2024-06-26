IAircraftBasicTakeoffModel
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel

   object
   
   Interface used to access the basic takeoff model options for a takeoff model of an aircraft in the Aviator catalog.

.. py:currentmodule:: IAircraftBasicTakeoffModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.set_takeoff_speed`
              - Set the takeoff speed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.set_departure_speed`
              - Set the departure speed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.takeoff_speed`
              - Get the speed to which the aircraft accelerates on its ground roll for takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.takeoff_speed_type`
              - Get the takeoff speed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.sea_level_ground_roll`
              - Gets or sets the distance the aircraft travels along the ground while accelerationg to takeoff at sea level.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.departure_speed`
              - Get the aircraft's speed upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.departure_speed_type`
              - Get the departure speed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.use_aero_prop_fuel`
              - Gets or sets whether to use Aero/Propulsion fuel flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.scale_fuel_flow_by_non_std_density`
              - Gets or sets whether to scale fuel flow by non std density.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.accel_fuel_flow`
              - Gets or sets the aircraft's fuel flow rate while accelerating during takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.departure_fuel_flow`
              - Gets or sets the aircraft's fuel flow rate at departure speed.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftBasicTakeoffModel


Property detail
---------------

.. py:property:: takeoff_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.takeoff_speed
    :type: float

    Get the speed to which the aircraft accelerates on its ground roll for takeoff.

.. py:property:: takeoff_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.takeoff_speed_type
    :type: AIRSPEED_TYPE

    Get the takeoff speed type.

.. py:property:: sea_level_ground_roll
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.sea_level_ground_roll
    :type: float

    Gets or sets the distance the aircraft travels along the ground while accelerationg to takeoff at sea level.

.. py:property:: departure_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.departure_speed
    :type: float

    Get the aircraft's speed upon leaving the ground.

.. py:property:: departure_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.departure_speed_type
    :type: AIRSPEED_TYPE

    Get the departure speed type.

.. py:property:: use_aero_prop_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.use_aero_prop_fuel
    :type: bool

    Gets or sets whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Gets or sets whether to scale fuel flow by non std density.

.. py:property:: accel_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.accel_fuel_flow
    :type: float

    Gets or sets the aircraft's fuel flow rate while accelerating during takeoff.

.. py:property:: departure_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.departure_fuel_flow
    :type: float

    Gets or sets the aircraft's fuel flow rate at departure speed.


Method detail
-------------



.. py:method:: set_takeoff_speed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.set_takeoff_speed

    Set the takeoff speed of the aircraft.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`





.. py:method:: set_departure_speed(self, airspeedType: AIRSPEED_TYPE, aispeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.set_departure_speed

    Set the departure speed of the aircraft.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`









.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicTakeoffModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

