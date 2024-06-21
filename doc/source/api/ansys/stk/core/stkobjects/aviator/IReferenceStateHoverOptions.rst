IReferenceStateHoverOptions
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions

   object
   
   Interface used to access the hover options for a reference state procedure.

.. py:currentmodule:: IReferenceStateHoverOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.set_longitudinal_accel`
              - Set the longitudinal acceleration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.set_attitude_rate`
              - Set the vertical attitude rate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.groundspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.altitude_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.tas_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.groundspeed_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.longitudinal_accel_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.heading`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.heading_is_magnetic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.course_is_magnetic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.heading_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.course_dot`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.roll_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.aoa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.pitch_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.push_pull_g`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.attitude_rate_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IReferenceStateHoverOptions


Property detail
---------------

.. py:property:: groundspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.groundspeed
    :type: float

    Gets or sets the aircraft's speed relative to the ground.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.altitude_rate
    :type: float

    Gets or sets the rate at which the aircraft will climb or descend.

.. py:property:: tas_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.tas_dot
    :type: float

    Get the true airspeed acceleration.

.. py:property:: groundspeed_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.groundspeed_dot
    :type: float

    Get the groundspeed acceleration.

.. py:property:: longitudinal_accel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.longitudinal_accel_type
    :type: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE

    Get the mode to specify the longitudinal acceleration.

.. py:property:: heading
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.heading
    :type: typing.Any

    Gets or sets the direction the aircraft is pointing.

.. py:property:: heading_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.heading_is_magnetic
    :type: bool

    Opt whether to specify the heading using magnetic North.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.course
    :type: typing.Any

    Gets or sets the direction the aircraft is traveling.

.. py:property:: course_is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.course_is_magnetic
    :type: bool

    Opt whether to specify the course using magnetic North.

.. py:property:: heading_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.heading_dot
    :type: typing.Any

    Gets or sets the heading rate of change.

.. py:property:: course_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.course_dot
    :type: typing.Any

    Gets or sets the course rate of change.

.. py:property:: roll_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.roll_angle
    :type: typing.Any

    Gets or sets the aircraft's bank angle.

.. py:property:: aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.aoa
    :type: typing.Any

    Gets or sets the aircraft's angle of attack.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.pitch_rate
    :type: typing.Any

    Get the aircraft's pitch rate.

.. py:property:: push_pull_g
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.push_pull_g
    :type: float

    Get the G force on the aircraft resulting from its attitude.

.. py:property:: attitude_rate_type
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.attitude_rate_type
    :type: REFERENCE_STATE_ATTITUDE_MODE

    Get the mode to specify the vertical attitude rate.


Method detail
-------------








.. py:method:: set_longitudinal_accel(self, accelType: REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE, value: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.set_longitudinal_accel

    Set the longitudinal acceleration.

    :Parameters:

    **accelType** : :obj:`~REFERENCE_STATE_LONGITUDINAL_ACCEL_MODE`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`




















.. py:method:: set_attitude_rate(self, attitudeRateType: REFERENCE_STATE_ATTITUDE_MODE, value: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IReferenceStateHoverOptions.set_attitude_rate

    Set the vertical attitude rate.

    :Parameters:

    **attitudeRateType** : :obj:`~REFERENCE_STATE_ATTITUDE_MODE`
    **value** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

