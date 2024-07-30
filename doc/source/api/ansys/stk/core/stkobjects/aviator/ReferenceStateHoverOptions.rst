ReferenceStateHoverOptions
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions

   Bases: 

   Class defining the Hover options for a Reference State procedure.

.. py:currentmodule:: ReferenceStateHoverOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.set_longitudinal_acceleration`
              - Set the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.set_attitude_rate`
              - Set the vertical attitude rate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.groundspeed`
              - Gets or sets the aircraft's speed relative to the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.altitude_rate`
              - Gets or sets the rate at which the aircraft will climb or descend.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.tas_dot`
              - Get the true airspeed acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.groundspeed_dot`
              - Get the groundspeed acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.longitudinal_acceleration_type`
              - Get the mode to specify the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.heading`
              - Gets or sets the direction the aircraft is pointing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.heading_is_magnetic`
              - Opt whether to specify the heading using magnetic North.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.course`
              - Gets or sets the direction the aircraft is traveling.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.course_is_magnetic`
              - Opt whether to specify the course using magnetic North.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.heading_dot`
              - Gets or sets the heading rate of change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.course_dot`
              - Gets or sets the course rate of change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.roll_angle`
              - Gets or sets the aircraft's bank angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.aoa`
              - Gets or sets the aircraft's angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.pitch_rate`
              - Get the aircraft's pitch rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.push_pull_g`
              - Get the G force on the aircraft resulting from its attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.attitude_rate_type`
              - Get the mode to specify the vertical attitude rate.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ReferenceStateHoverOptions


Property detail
---------------

.. py:property:: groundspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.groundspeed
    :type: float

    Gets or sets the aircraft's speed relative to the ground.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.altitude_rate
    :type: float

    Gets or sets the rate at which the aircraft will climb or descend.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_acceleration_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.longitudinal_acceleration_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.course
    :type: typing.Any

    Gets or sets the direction the aircraft is traveling.

.. py:property:: course_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.course_is_magnetic
    :type: bool

    Opt whether to specify the course using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.heading_dot
    :type: typing.Any

    Gets or sets the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.course_dot
    :type: typing.Any

    Gets or sets the course rate of change.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.roll_angle
    :type: typing.Any

    Gets or sets the aircraft's bank angle.

.. py:property:: aoa
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.aoa
    :type: typing.Any

    Gets or sets the aircraft's angle of attack.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.pitch_rate
    :type: typing.Any

    Get the aircraft's pitch rate.

.. py:property:: push_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.push_pull_g
    :type: float

    Get the G force on the aircraft resulting from its attitude.

.. py:property:: attitude_rate_type
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.attitude_rate_type
    :type: REFERENCE_STATE_ATTITUDE_MODE

    Get the mode to specify the vertical attitude rate.


Method detail
-------------








.. py:method:: set_longitudinal_acceleration(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.set_longitudinal_acceleration

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCELERATION_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`




















.. py:method:: set_attitude_rate(self, attitudeRateType: REFERENCE_STATE_ATTITUDE_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ReferenceStateHoverOptions.set_attitude_rate

    Set the vertical attitude rate.

    :Parameters:

    **attitudeRateType** : :obj:`~REFERENCE_STATE_ATTITUDE_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

