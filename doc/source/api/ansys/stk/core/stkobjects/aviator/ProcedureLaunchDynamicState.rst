ProcedureLaunchDynamicState
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a Launch Dyn State procedure.

.. py:currentmodule:: ProcedureLaunchDynamicState

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.set_airspeed`
              - Set the launch airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.launch_time`
              - Gets or sets the launch time of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.coord_frame`
              - Gets or sets the reference coordinate frame for the dyn state launch procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.bearing_reference`
              - Gets or sets the bearing reference for the dyn state launch procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.launch_bearing`
              - Gets or sets the launch direction bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.launch_elevation`
              - Gets or sets the launch direction elevation.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.attitude_mode`
              - Gets or sets the attitude mode during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.specify_launch_airspeed`
              - Opt to specify a minimum launch speed the aircraft will accelerate to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.acceleration_g`
              - Gets or sets the acceleration of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.airspeed`
              - Get the goal airspeed for the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.fuel_flow_type`
              - Gets or sets the fuel flow type of the aircraft during the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.override_fuel_flow`
              - Gets or sets the fuel flow value for a fuel flow type set to Override.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.true_course_hint`
              - Gets or sets the true course used when the vehicle's direction vector is set to Zenith.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureLaunchDynamicState


Property detail
---------------

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.launch_time
    :type: typing.Any

    Gets or sets the launch time of the aircraft.

.. py:property:: coord_frame
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.coord_frame
    :type: LAUNCH_DYNAMIC_STATE_COORD_FRAME

    Gets or sets the reference coordinate frame for the dyn state launch procedure.

.. py:property:: bearing_reference
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.bearing_reference
    :type: LAUNCH_DYNAMIC_STATE_BEARING_REFERENCE

    Gets or sets the bearing reference for the dyn state launch procedure.

.. py:property:: launch_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.launch_bearing
    :type: typing.Any

    Gets or sets the launch direction bearing.

.. py:property:: launch_elevation
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.launch_elevation
    :type: typing.Any

    Gets or sets the launch direction elevation.

.. py:property:: attitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.attitude_mode
    :type: LAUNCH_ATTITUDE_MODE

    Gets or sets the attitude mode during the launch.

.. py:property:: specify_launch_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.specify_launch_airspeed
    :type: bool

    Opt to specify a minimum launch speed the aircraft will accelerate to.

.. py:property:: acceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.acceleration_g
    :type: float

    Gets or sets the acceleration of the aircraft during the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.fuel_flow_type
    :type: FUEL_FLOW_TYPE

    Gets or sets the fuel flow type of the aircraft during the launch.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.override_fuel_flow
    :type: float

    Gets or sets the fuel flow value for a fuel flow type set to Override.

.. py:property:: true_course_hint
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.true_course_hint
    :type: typing.Any

    Gets or sets the true course used when the vehicle's direction vector is set to Zenith.


Method detail
-------------



















.. py:method:: set_airspeed(self, airspeed_type: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.set_airspeed

    Set the launch airspeed.

    :Parameters:

    **airspeed_type** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`







.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureLaunchDynamicState.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

