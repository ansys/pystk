ISensorHalfPowerPattern
=======================

.. py:class:: ansys.stk.core.stkobjects.ISensorHalfPowerPattern

   object
   
   IAgSnHalfPowerPattern Interface for half power sensors designed to model parabolic antennas.

.. py:currentmodule:: ISensorHalfPowerPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorHalfPowerPattern.frequency`
              - The antenna's frequency in GHz. Uses Frequency Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorHalfPowerPattern.antenna_diameter`
              - The diameter of the antenna dish. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorHalfPowerPattern.half_angle`
              - Get the half angle of the cone for, calculated on the basis of the Frequency and AntennaDiameter properties. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorHalfPowerPattern.angular_resolution`
              - Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorHalfPowerPattern


Property detail
---------------

.. py:property:: frequency
    :canonical: ansys.stk.core.stkobjects.ISensorHalfPowerPattern.frequency
    :type: float

    The antenna's frequency in GHz. Uses Frequency Dimension.

.. py:property:: antenna_diameter
    :canonical: ansys.stk.core.stkobjects.ISensorHalfPowerPattern.antenna_diameter
    :type: float

    The diameter of the antenna dish. Uses SmallDistanceUnit Dimension.

.. py:property:: half_angle
    :canonical: ansys.stk.core.stkobjects.ISensorHalfPowerPattern.half_angle
    :type: typing.Any

    Get the half angle of the cone for, calculated on the basis of the Frequency and AntennaDiameter properties. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorHalfPowerPattern.angular_resolution
    :type: typing.Any

    Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


