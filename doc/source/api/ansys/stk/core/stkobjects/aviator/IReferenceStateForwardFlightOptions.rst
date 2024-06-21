IReferenceStateForwardFlightOptions
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions

   object
   
   Interface used to access the forward flight options for a reference state procedure.

.. py:currentmodule:: IReferenceStateForwardFlightOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_airspeed`
              - Set the launch airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_longitudinal_accel`
              - Set the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_lateral_accel`
              - Set the lateral acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_attitude_rate`
              - Set the vertical attitude rate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.altitude_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.flight_path_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.tas_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.groundspeed_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.longitudinal_accel_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.heading`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.heading_is_magnetic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.course_is_magnetic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.heading_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.course_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.lateral_accel_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.roll_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.aoa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.sideslip`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.pitch_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.push_pull_g`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.attitude_rate_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IReferenceStateForwardFlightOptions


Property detail
---------------

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.altitude_rate
    :type: float

    Gets or sets the rate at which the aircraft will climb or descend.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.flight_path_angle
    :type: typing.Any

    Gets or sets the initial pitch angle of the flight path.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.longitudinal_accel_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.course
    :type: typing.Any

    Gets or sets the direction the aircraft is traveling.

.. py:property:: course_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.course_is_magnetic
    :type: bool

    Opt whether to specify the course using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.heading_dot
    :type: typing.Any

    Get the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.course_dot
    :type: typing.Any

    Get the course rate of change.

.. py:property:: lateral_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.lateral_accel_type
    :type: REFERENCE_STATE_LATERAL_ACCEL_MODE

    Get the mode to specify the lateral acceleration.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.roll_angle
    :type: typing.Any

    Gets or sets the aircraft's bank angle.

.. py:property:: aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.aoa
    :type: typing.Any

    Gets or sets the aircraft's angle of attack.

.. py:property:: sideslip
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.sideslip
    :type: typing.Any

    Gets or sets the aircraft's yaw angle.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.pitch_rate
    :type: typing.Any

    Get the aircraft's pitch rate.

.. py:property:: push_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.push_pull_g
    :type: float

    Get the G force on the aircraft resulting from its attitude.

.. py:property:: attitude_rate_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.attitude_rate_type
    :type: REFERENCE_STATE_ATTITUDE_MODE

    Get the mode to specify the vertical attitude rate.


Method detail
-------------



.. py:method:: set_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_airspeed

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`








.. py:method:: set_longitudinal_accel(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_longitudinal_accel

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`












.. py:method:: set_lateral_accel(self, accelType: REFERENCE_STATE_LATERAL_ACCEL_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_lateral_accel

    Set the lateral acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LATERAL_ACCEL_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`










.. py:method:: set_attitude_rate(self, attitudeRateType: REFERENCE_STATE_ATTITUDE_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateForwardFlightOptions.set_attitude_rate

    Set the vertical attitude rate.

    :Parameters:

    **attitudeRateType** : :obj:`~REFERENCE_STATE_ATTITUDE_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

