IProcedureLaunchDynState
========================

.. py:class:: IProcedureLaunchDynState

   object
   
   Interface used to access the options for a dyn state launch procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_airspeed`
              - Set the launch airspeed.
            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~launch_time`
            * - :py:meth:`~coord_frame`
            * - :py:meth:`~bearing_reference`
            * - :py:meth:`~launch_bearing`
            * - :py:meth:`~launch_elevation`
            * - :py:meth:`~attitude_mode`
            * - :py:meth:`~specify_launch_airspeed`
            * - :py:meth:`~accel_g`
            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~airspeed`
            * - :py:meth:`~fuel_flow_type`
            * - :py:meth:`~override_fuel_flow`
            * - :py:meth:`~true_course_hint`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureLaunchDynState


Property detail
---------------

.. py:property:: launch_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.launch_time
    :type: typing.Any

    Gets or sets the launch time of the aircraft.

.. py:property:: coord_frame
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.coord_frame
    :type: "LAUNCH_DYN_STATE_COORD_FRAME"

    Gets or sets the reference coordinate frame for the dyn state launch procedure.

.. py:property:: bearing_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.bearing_reference
    :type: "LAUNCH_DYN_STATE_BEARING_REFERENCE"

    Gets or sets the bearing reference for the dyn state launch procedure.

.. py:property:: launch_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.launch_bearing
    :type: typing.Any

    Gets or sets the launch direction bearing.

.. py:property:: launch_elevation
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.launch_elevation
    :type: typing.Any

    Gets or sets the launch direction elevation.

.. py:property:: attitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.attitude_mode
    :type: "LAUNCH_ATTITUDE_MODE"

    Gets or sets the attitude mode during the launch.

.. py:property:: specify_launch_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.specify_launch_airspeed
    :type: bool

    Opt to specify a minimum launch speed the aircraft will accelerate to.

.. py:property:: accel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.accel_g
    :type: float

    Gets or sets the acceleration of the aircraft during the launch.

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.airspeed_type
    :type: "AIRSPEED_TYPE"

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: fuel_flow_type
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.fuel_flow_type
    :type: "FUEL_FLOW_TYPE"

    Gets or sets the fuel flow type of the aircraft during the launch.

.. py:property:: override_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.override_fuel_flow
    :type: float

    Gets or sets the fuel flow value for a fuel flow type set to Override.

.. py:property:: true_course_hint
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLaunchDynState.true_course_hint
    :type: typing.Any

    Gets or sets the true course used when the vehicle's direction vector is set to Zenith.


Method detail
-------------



















.. py:method:: set_airspeed(self, airspeedType:"AIRSPEED_TYPE", airspeed:float) -> None

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`







.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`

