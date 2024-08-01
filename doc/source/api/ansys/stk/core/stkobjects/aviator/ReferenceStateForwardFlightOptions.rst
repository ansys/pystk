ReferenceStateForwardFlightOptions
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions

   Bases: 

   Class defining the Forward Flight options for a Reference State procedure.

.. py:currentmodule:: ReferenceStateForwardFlightOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_airspeed`
              - Set the launch airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_longitudinal_acceleration`
              - Set the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_lateral_acceleration`
              - Set the lateral acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_attitude_rate`
              - Set the vertical attitude rate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.airspeed_type`
              - Get the airspeed type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.airspeed`
              - Get the goal airspeed for the launch.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.altitude_rate`
              - Gets or sets the rate at which the aircraft will climb or descend.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.flight_path_angle`
              - Gets or sets the initial pitch angle of the flight path.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.tas_dot`
              - Get the true airspeed acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.groundspeed_dot`
              - Get the groundspeed acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.longitudinal_acceleration_type`
              - Get the mode to specify the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.heading`
              - Gets or sets the direction the aircraft is pointing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.heading_is_magnetic`
              - Opt whether to specify the heading using magnetic North.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.course`
              - Gets or sets the direction the aircraft is traveling.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.course_is_magnetic`
              - Opt whether to specify the course using magnetic North.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.heading_dot`
              - Get the heading rate of change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.course_dot`
              - Get the course rate of change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.lateral_acceleration_type`
              - Get the mode to specify the lateral acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.roll_angle`
              - Gets or sets the aircraft's bank angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.aoa`
              - Gets or sets the aircraft's angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.sideslip`
              - Gets or sets the aircraft's yaw angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.pitch_rate`
              - Get the aircraft's pitch rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.push_pull_g`
              - Get the G force on the aircraft resulting from its attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.attitude_rate_type`
              - Get the mode to specify the vertical attitude rate.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ReferenceStateForwardFlightOptions


Property detail
---------------

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.altitude_rate
    :type: float

    Gets or sets the rate at which the aircraft will climb or descend.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.flight_path_angle
    :type: typing.Any

    Gets or sets the initial pitch angle of the flight path.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_acceleration_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.longitudinal_acceleration_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.course
    :type: typing.Any

    Gets or sets the direction the aircraft is traveling.

.. py:property:: course_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.course_is_magnetic
    :type: bool

    Opt whether to specify the course using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.heading_dot
    :type: typing.Any

    Get the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.course_dot
    :type: typing.Any

    Get the course rate of change.

.. py:property:: lateral_acceleration_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.lateral_acceleration_type
    :type: REFERENCE_STATE_LATERAL_ACCELERATION_MODE

    Get the mode to specify the lateral acceleration.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.roll_angle
    :type: typing.Any

    Gets or sets the aircraft's bank angle.

.. py:property:: aoa
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.aoa
    :type: typing.Any

    Gets or sets the aircraft's angle of attack.

.. py:property:: sideslip
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.sideslip
    :type: typing.Any

    Gets or sets the aircraft's yaw angle.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.pitch_rate
    :type: typing.Any

    Get the aircraft's pitch rate.

.. py:property:: push_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.push_pull_g
    :type: float

    Get the G force on the aircraft resulting from its attitude.

.. py:property:: attitude_rate_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.attitude_rate_type
    :type: REFERENCE_STATE_ATTITUDE_MODE

    Get the mode to specify the vertical attitude rate.


Method detail
-------------



.. py:method:: set_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_airspeed

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`








.. py:method:: set_longitudinal_acceleration(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_longitudinal_acceleration

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`












.. py:method:: set_lateral_acceleration(self, accelType: REFERENCE_STATE_LATERAL_ACCELERATION_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_lateral_acceleration

    Set the lateral acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LATERAL_ACCELERATION_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`










.. py:method:: set_attitude_rate(self, attitudeRateType: REFERENCE_STATE_ATTITUDE_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateForwardFlightOptions.set_attitude_rate

    Set the vertical attitude rate.

    :Parameters:

    **attitudeRateType** : :obj:`~REFERENCE_STATE_ATTITUDE_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

