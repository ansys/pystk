ISensorSARPattern
=================

.. py:class:: ansys.stk.core.stkobjects.ISensorSARPattern

   object
   
   IAgSnSARPattern Interface for the Synthetic Aperture Radar (SAR) sensor type, designed to model the field of regard of a SAR sensor with respect to the surface of the Earth.

.. py:currentmodule:: ISensorSARPattern

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.set_elevation_angles`
              - Set both the min and max elevation angle. Min/Max use Angle Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.parent_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.min_elevation_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.max_elevation_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.fore_exclusion_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.aft_exclusion_angle`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.angular_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorSARPattern.track_parent_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorSARPattern


Property detail
---------------

.. py:property:: parent_altitude
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.parent_altitude
    :type: float

    The altitude of the sensor's parent object (assumed to be constant). Uses Distance Dimension.

.. py:property:: min_elevation_angle
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.min_elevation_angle
    :type: typing.Any

    Minimum ground elevation angle to which the SAR sensor can provide coverage. Uses Angle Dimension.

.. py:property:: max_elevation_angle
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.max_elevation_angle
    :type: typing.Any

    Maximum ground elevation angle to which the SAR sensor can provide coverage. Uses Angle Dimension.

.. py:property:: fore_exclusion_angle
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.fore_exclusion_angle
    :type: typing.Any

    The minimum angle between the forward projection of the velocity vector and the vector to the target. Uses Angle Dimension.

.. py:property:: aft_exclusion_angle
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.aft_exclusion_angle
    :type: typing.Any

    The minimum angle between the aft projection of the velocity vector and the vector to the target. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.angular_resolution
    :type: typing.Any

    Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...

.. py:property:: track_parent_altitude
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.track_parent_altitude
    :type: bool

    Whether or not the SAR sensor tracks the altitude of the sensor's parent object.


Method detail
-------------











.. py:method:: set_elevation_angles(self, min: typing.Any, max: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorSARPattern.set_elevation_angles

    Set both the min and max elevation angle. Min/Max use Angle Dimension.

    :Parameters:

    **min** : :obj:`~typing.Any`
    **max** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`





