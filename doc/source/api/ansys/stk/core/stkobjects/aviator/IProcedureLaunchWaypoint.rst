IProcedureLaunchWaypoint
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint

   object
   
   Interface used to access the options for a waypoint launch procedure.

.. py:currentmodule:: IProcedureLaunchWaypoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.set_airspeed`
              - Set the launch airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.altitude_reference`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_true_bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_elevation`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.accel_g`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.fuel_flow_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.override_fuel_flow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureLaunchWaypoint


Property detail
---------------

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_time
    :type: typing.Any

    Gets or sets the launch time of the aircraft.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.altitude_reference
    :type: ALTITUDE_REFERENCE

    Gets or sets the launch altitude reference.

.. py:property:: launch_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_altitude
    :type: float

    Gets or sets the launch altitude.

.. py:property:: launch_true_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_true_bearing
    :type: typing.Any

    Gets or sets the launch direction bearing.

.. py:property:: launch_elevation
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.launch_elevation
    :type: typing.Any

    Gets or sets the launch direction elevation.

.. py:property:: accel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.accel_g
    :type: float

    Gets or sets the acceleration of the aircraft during the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.fuel_flow_type
    :type: FUEL_FLOW_TYPE

    Gets or sets the fuel flow type of the aircraft during the launch.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.override_fuel_flow
    :type: float

    Gets or sets the fuel flow value for a fuel flow type set to Override.


Method detail
-------------















.. py:method:: set_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.set_airspeed

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`





.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchWaypoint.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

