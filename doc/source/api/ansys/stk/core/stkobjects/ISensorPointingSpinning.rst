ISensorPointingSpinning
=======================

.. py:class:: ansys.stk.core.stkobjects.ISensorPointingSpinning

   object
   
   IAgSnPtSpinning Interface for defining the pointing properties of a spinning sensor.

.. py:currentmodule:: ISensorPointingSpinning

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.set_clock_angles`
              - Set both the start and stop clock angles. Start/Stop use Angle Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_axis_azimuth`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_axis_elevation`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_axis_cone_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.scan_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.clock_angle_start`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.clock_angle_stop`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingSpinning.offset_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorPointingSpinning


Property detail
---------------

.. py:property:: spin_axis_azimuth
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_axis_azimuth
    :type: typing.Any

    The azimuth of the spin axis, i.e. the angle from the parent object's +X axis about the +Z axis in a right-handed sense. Uses Angle Dimension.

.. py:property:: spin_axis_elevation
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_axis_elevation
    :type: typing.Any

    The elevation of the spin axis, i.e. the angle between the spin axis and the parent object's body-fixed XY plane, measured as positive in the direction of the parent object's body-fixed +Z axis. Uses Angle Dimension.

.. py:property:: spin_axis_cone_angle
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_axis_cone_angle
    :type: typing.Any

    The cone angle used in defining the spin axis, i.e. the angle between the spin axis and the sensor boresight. As the boresight spins about the spin axis, it maintains this angular distance away from the spin axis. Uses Angle Dimension.

.. py:property:: scan_mode
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.scan_mode
    :type: SENSOR_SCAN_MODE

    The scan mode of the sensor, a member of the AgESnScanMode enumeration.

.. py:property:: clock_angle_start
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.clock_angle_start
    :type: typing.Any

    The start angle, i.e. the angle about the sensor's spin axis at which scanning begins. Zero is relative to the X axis in the spin axis coordinate frame. Uses Angle Dimension.

.. py:property:: clock_angle_stop
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.clock_angle_stop
    :type: typing.Any

    The stop angle, i.e. the angle about the sensor's spin axis at which scanning ends and/or reverses direction. Uses Angle Dimension.

.. py:property:: spin_rate
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.spin_rate
    :type: float

    Rate at which the boresight spins about the spin axis, measured in revolutions per minute. The spin is positive in a right-handed sense about the spin axis. Negative rate can be used to create a spin in the opposite direction. Uses AngleRate Dimension.

.. py:property:: offset_angle
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.offset_angle
    :type: typing.Any

    The initial offset angle, i.e. the angle about the spin axis where the sensor boresight is at time zero. Uses Angle Dimension.


Method detail
-------------

















.. py:method:: set_clock_angles(self, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorPointingSpinning.set_clock_angles

    Set both the start and stop clock angles. Start/Stop use Angle Dimension.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

