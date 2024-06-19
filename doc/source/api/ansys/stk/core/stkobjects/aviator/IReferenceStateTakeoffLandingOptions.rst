IReferenceStateTakeoffLandingOptions
====================================

.. py:class:: IReferenceStateTakeoffLandingOptions

   object
   
   Interface used to access the takeoff or landing options for a reference state procedure.

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
            * - :py:meth:`~set_longitudinal_accel`
              - Set the longitudinal acceleration.
            * - :py:meth:`~set_lateral_accel`
              - Set the lateral acceleration.
            * - :py:meth:`~set_attitude_rate`
              - Set the vertical attitude rate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~airspeed_type`
            * - :py:meth:`~airspeed`
            * - :py:meth:`~altitude_rate`
            * - :py:meth:`~flight_path_angle`
            * - :py:meth:`~tas_dot`
            * - :py:meth:`~groundspeed_dot`
            * - :py:meth:`~longitudinal_accel_type`
            * - :py:meth:`~heading`
            * - :py:meth:`~heading_is_magnetic`
            * - :py:meth:`~course`
            * - :py:meth:`~course_is_magnetic`
            * - :py:meth:`~heading_dot`
            * - :py:meth:`~course_dot`
            * - :py:meth:`~lateral_accel_type`
            * - :py:meth:`~roll_angle`
            * - :py:meth:`~aoa`
            * - :py:meth:`~sideslip`
            * - :py:meth:`~pitch_rate`
            * - :py:meth:`~push_pull_g`
            * - :py:meth:`~attitude_rate_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IReferenceStateTakeoffLandingOptions


Property detail
---------------

.. py:property:: airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type.

.. py:property:: airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.airspeed
    :type: float

    Get the goal airspeed for the launch.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.altitude_rate
    :type: float

    Gets or sets the rate at which the aircraft will climb or descend.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.flight_path_angle
    :type: typing.Any

    Gets or sets the initial pitch angle of the flight path.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.longitudinal_accel_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.course
    :type: typing.Any

    Gets or sets the direction the aircraft is traveling.

.. py:property:: course_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.course_is_magnetic
    :type: bool

    Opt whether to specify the course using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.heading_dot
    :type: typing.Any

    Get the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.course_dot
    :type: typing.Any

    Get the course rate of change.

.. py:property:: lateral_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.lateral_accel_type
    :type: REFERENCE_STATE_LATERAL_ACCEL_MODE

    Get the mode to specify the lateral acceleration.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.roll_angle
    :type: typing.Any

    Gets or sets the aircraft's bank angle.

.. py:property:: aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.aoa
    :type: typing.Any

    Gets or sets the aircraft's angle of attack.

.. py:property:: sideslip
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.sideslip
    :type: typing.Any

    Gets or sets the aircraft's yaw angle.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.pitch_rate
    :type: typing.Any

    Get the aircraft's pitch rate.

.. py:property:: push_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.push_pull_g
    :type: float

    Get the G force on the aircraft resulting from its attitude.

.. py:property:: attitude_rate_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.attitude_rate_type
    :type: REFERENCE_STATE_ATTITUDE_MODE

    Get the mode to specify the vertical attitude rate.


Method detail
-------------



.. py:method:: set_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.set_airspeed

    Set the launch airspeed.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`








.. py:method:: set_longitudinal_accel(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.set_longitudinal_accel

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`












.. py:method:: set_lateral_accel(self, accelType: REFERENCE_STATE_LATERAL_ACCEL_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.set_lateral_accel

    Set the lateral acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LATERAL_ACCEL_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`










.. py:method:: set_attitude_rate(self, attitudeRateType: REFERENCE_STATE_ATTITUDE_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateTakeoffLandingOptions.set_attitude_rate

    Set the vertical attitude rate.

    :Parameters:

    **attitudeRateType** : :obj:`~REFERENCE_STATE_ATTITUDE_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

