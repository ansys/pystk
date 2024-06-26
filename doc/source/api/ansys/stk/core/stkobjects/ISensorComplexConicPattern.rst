ISensorComplexConicPattern
==========================

.. py:class:: ansys.stk.core.stkobjects.ISensorComplexConicPattern

   object
   
   IAgSnComplexConicPattern Interface for defining sensor patterns by the inner and outer half angles and minimum and maximum clock angles of the sensor's cone.

.. py:currentmodule:: ISensorComplexConicPattern

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.set_clock_angles`
              - Set both the min and max clock angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.set_cone_half_angles`
              - Set both the inner and outer cone half angles.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.inner_cone_half_angle`
              - Inner half angle to define the angular radius of the cone measured from the boresight. When an inner cone is specified, the inner region is considered to be a region of exclusion. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.outer_cone_half_angle`
              - Outer half angle to define the angular radius of the cone measured from the boresight. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.minimum_clock_angle`
              - Minimum clock angle to define the range of rotation about the boresight relative to the up vector. Clock angles correspond to azimuth angles, which are defined in the sensor pointing direction. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.maximum_clock_angle`
              - Maximum clock angle to define the range of rotation about the boresight relative to the up vector. Clock angles correspond to azimuth angles, which are defined in the sensor pointing direction. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorComplexConicPattern.angular_resolution`
              - Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorComplexConicPattern


Property detail
---------------

.. py:property:: inner_cone_half_angle
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.inner_cone_half_angle
    :type: typing.Any

    Inner half angle to define the angular radius of the cone measured from the boresight. When an inner cone is specified, the inner region is considered to be a region of exclusion. Uses Angle Dimension.

.. py:property:: outer_cone_half_angle
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.outer_cone_half_angle
    :type: typing.Any

    Outer half angle to define the angular radius of the cone measured from the boresight. Uses Angle Dimension.

.. py:property:: minimum_clock_angle
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.minimum_clock_angle
    :type: typing.Any

    Minimum clock angle to define the range of rotation about the boresight relative to the up vector. Clock angles correspond to azimuth angles, which are defined in the sensor pointing direction. Uses Angle Dimension.

.. py:property:: maximum_clock_angle
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.maximum_clock_angle
    :type: typing.Any

    Maximum clock angle to define the range of rotation about the boresight relative to the up vector. Clock angles correspond to azimuth angles, which are defined in the sensor pointing direction. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.angular_resolution
    :type: typing.Any

    Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


Method detail
-------------









.. py:method:: set_clock_angles(self, min: typing.Any, max: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.set_clock_angles

    Set both the min and max clock angle.

    :Parameters:

    **min** : :obj:`~typing.Any`
    **max** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: set_cone_half_angles(self, inner: typing.Any, outer: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorComplexConicPattern.set_cone_half_angles

    Set both the inner and outer cone half angles.

    :Parameters:

    **inner** : :obj:`~typing.Any`
    **outer** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

