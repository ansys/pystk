IAircraftVTOLModel
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel

   object
   
   Interface used to access the options for a VTOL performance model of an aircraft.

.. py:currentmodule:: IAircraftVTOLModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.set_forward_flight_airspeed`
              - Set the speed at which the aircraft can begin forward flight.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.max_hover_altitude`
              - Gets or sets the maximum altitude at which the aircraft is capable of hovering.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.use_aero_prop_fuel`
              - Gets or sets whether to use Aero/Propulsion fuel flow.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.scale_fuel_flow_by_non_std_density`
              - Gets or sets whether to scale fuel flow by non std density.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.hover_fuel`
              - Gets or sets the aircraft's fuel flow rate while hovering.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.heading_rate`
              - Gets or sets the rate at which the aircraft can change heading while hovering.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.heading_transition_time`
              - Gets or sets the time required to transition from another maneuvering mode to heading change maneuver mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.vertical_rate`
              - Gets or sets the aircraft's vertical rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.vertical_transition_time`
              - Gets or sets the time required to transition from another maneuvering mode to vertical maneuver mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.translation_rate`
              - Gets or sets the rate at which the aircraft can translate while hovering.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.translation_transition_time`
              - Gets or sets the time required to transition from another maneuvering mode to translation maneuver mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.forward_flight_airspeed`
              - Get the speed at which the aircraft can begin forward flight.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.forward_flight_airspeed_type`
              - Get the forward flight airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.forward_flight_transition_time`
              - Gets or sets the time required to transition from another maneuvering mode to forward flight at sea level.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftVTOLModel


Property detail
---------------

.. py:property:: max_hover_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.max_hover_altitude
    :type: float

    Gets or sets the maximum altitude at which the aircraft is capable of hovering.

.. py:property:: use_aero_prop_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.use_aero_prop_fuel
    :type: bool

    Gets or sets whether to use Aero/Propulsion fuel flow.

.. py:property:: scale_fuel_flow_by_non_std_density
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.scale_fuel_flow_by_non_std_density
    :type: bool

    Gets or sets whether to scale fuel flow by non std density.

.. py:property:: hover_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.hover_fuel
    :type: float

    Gets or sets the aircraft's fuel flow rate while hovering.

.. py:property:: heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.heading_rate
    :type: typing.Any

    Gets or sets the rate at which the aircraft can change heading while hovering.

.. py:property:: heading_transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.heading_transition_time
    :type: float

    Gets or sets the time required to transition from another maneuvering mode to heading change maneuver mode.

.. py:property:: vertical_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.vertical_rate
    :type: float

    Gets or sets the aircraft's vertical rate.

.. py:property:: vertical_transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.vertical_transition_time
    :type: float

    Gets or sets the time required to transition from another maneuvering mode to vertical maneuver mode.

.. py:property:: translation_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.translation_rate
    :type: float

    Gets or sets the rate at which the aircraft can translate while hovering.

.. py:property:: translation_transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.translation_transition_time
    :type: float

    Gets or sets the time required to transition from another maneuvering mode to translation maneuver mode.

.. py:property:: forward_flight_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.forward_flight_airspeed
    :type: float

    Get the speed at which the aircraft can begin forward flight.

.. py:property:: forward_flight_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.forward_flight_airspeed_type
    :type: AIRSPEED_TYPE

    Get the forward flight airspeed type.

.. py:property:: forward_flight_transition_time
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.forward_flight_transition_time
    :type: float

    Gets or sets the time required to transition from another maneuvering mode to forward flight at sea level.


Method detail
-------------























.. py:method:: set_forward_flight_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOLModel.set_forward_flight_airspeed

    Set the speed at which the aircraft can begin forward flight.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



