ProcedureLaunchWaypoint
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a Launch Waypoint procedure.

.. py:currentmodule:: ProcedureLaunchWaypoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.set_airspeed`
              - Set the launch airspeed.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.acceleration_g`
              - Get or set the acceleration of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.airspeed`
              - Get the goal airspeed for the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.altitude_reference`
              - Get or set the launch altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.fuel_flow_type`
              - Get or set the fuel flow type of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_altitude`
              - Get or set the launch altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_elevation`
              - Get or set the launch direction elevation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_time`
              - Get or set the launch time of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_true_bearing`
              - Get or set the launch direction bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.override_fuel_flow`
              - Get or set the fuel flow value for a fuel flow type set to Override.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureLaunchWaypoint


Property detail
---------------

.. py:property:: acceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.acceleration_g
    :type: float

    Get or set the acceleration of the aircraft during the launch.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.airspeed_type
    :type: AirspeedType

    Get the airspeed type.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.altitude_reference
    :type: AltitudeReference

    Get or set the launch altitude reference.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.fuel_flow_type
    :type: FuelFlowType

    Get or set the fuel flow type of the aircraft during the launch.

.. py:property:: launch_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_altitude
    :type: float

    Get or set the launch altitude.

.. py:property:: launch_elevation
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_elevation
    :type: typing.Any

    Get or set the launch direction elevation.

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_time
    :type: typing.Any

    Get or set the launch time of the aircraft.

.. py:property:: launch_true_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.launch_true_bearing
    :type: typing.Any

    Get or set the launch direction bearing.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.override_fuel_flow
    :type: float

    Get or set the fuel flow value for a fuel flow type set to Override.


Method detail
-------------









.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`











.. py:method:: set_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchWaypoint.set_airspeed

    Set the launch airspeed.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`

