SensorHalfPowerPattern
======================

.. py:class:: ansys.stk.core.stkobjects.SensorHalfPowerPattern

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPattern`

   Class defining the half-power pattern for a Sensor.

.. py:currentmodule:: SensorHalfPowerPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorHalfPowerPattern.frequency`
              - The antenna's frequency in GHz. Uses Frequency Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorHalfPowerPattern.antenna_diameter`
              - The diameter of the antenna dish. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorHalfPowerPattern.half_angle`
              - Get the half angle of the cone for, calculated on the basis of the Frequency and AntennaDiameter properties. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorHalfPowerPattern.angular_resolution`
              - Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorHalfPowerPattern


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.SensorHalfPowerPattern.frequency
    :type: float

    The antenna's frequency in GHz. Uses Frequency Dimension.

.. py:property:: antenna_diameter
    :canonical: ansys.stk.core.stkobjects.SensorHalfPowerPattern.antenna_diameter
    :type: float

    The diameter of the antenna dish. Uses SmallDistanceUnit Dimension.

.. py:property:: half_angle
    :canonical: ansys.stk.core.stkobjects.SensorHalfPowerPattern.half_angle
    :type: typing.Any

    Get the half angle of the cone for, calculated on the basis of the Frequency and AntennaDiameter properties. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.SensorHalfPowerPattern.angular_resolution
    :type: typing.Any

    Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


