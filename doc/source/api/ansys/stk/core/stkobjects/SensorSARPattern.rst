SensorSARPattern
================

.. py:class:: ansys.stk.core.stkobjects.SensorSARPattern

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPattern`

   Class defining the Synthetic Aperture Radar (SAR) pattern for a Sensor.

.. py:currentmodule:: SensorSARPattern

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.set_elevation_angles`
              - Set both the min and max elevation angle. Min/Max use Angle Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.parent_altitude`
              - The altitude of the sensor's parent object (assumed to be constant). Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.minimum_elevation_angle`
              - Minimum ground elevation angle to which the SAR sensor can provide coverage. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.maximum_elevation_angle`
              - Maximum ground elevation angle to which the SAR sensor can provide coverage. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.fore_exclusion_angle`
              - The minimum angle between the forward projection of the velocity vector and the vector to the target. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.aft_exclusion_angle`
              - The minimum angle between the aft projection of the velocity vector and the vector to the target. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.angular_resolution`
              - Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorSARPattern.track_parent_altitude`
              - Whether or not the SAR sensor tracks the altitude of the sensor's parent object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorSARPattern


Property detail
---------------

.. py:property:: parent_altitude
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.parent_altitude
    :type: float

    The altitude of the sensor's parent object (assumed to be constant). Uses Distance Dimension.

.. py:property:: minimum_elevation_angle
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.minimum_elevation_angle
    :type: typing.Any

    Minimum ground elevation angle to which the SAR sensor can provide coverage. Uses Angle Dimension.

.. py:property:: maximum_elevation_angle
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.maximum_elevation_angle
    :type: typing.Any

    Maximum ground elevation angle to which the SAR sensor can provide coverage. Uses Angle Dimension.

.. py:property:: fore_exclusion_angle
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.fore_exclusion_angle
    :type: typing.Any

    The minimum angle between the forward projection of the velocity vector and the vector to the target. Uses Angle Dimension.

.. py:property:: aft_exclusion_angle
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.aft_exclusion_angle
    :type: typing.Any

    The minimum angle between the aft projection of the velocity vector and the vector to the target. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.angular_resolution
    :type: typing.Any

    Allow a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: track_parent_altitude
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.track_parent_altitude
    :type: bool

    Whether or not the SAR sensor tracks the altitude of the sensor's parent object.


Method detail
-------------











.. py:method:: set_elevation_angles(self, min: typing.Any, max: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.SensorSARPattern.set_elevation_angles

    Set both the min and max elevation angle. Min/Max use Angle Dimension.

    :Parameters:

        **min** : :obj:`~typing.Any`

        **max** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`





