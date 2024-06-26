ISensorRectangularPattern
=========================

.. py:class:: ansys.stk.core.stkobjects.ISensorRectangularPattern

   object
   
   IAgSnRectangularPattern Interface for rectangular sensor types typically used with satellites or aircraft for modeling the field of view of instruments such as push broom sensors and star trackers.

.. py:currentmodule:: ISensorRectangularPattern

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorRectangularPattern.vertical_half_angle`
              - The angle from the boresight (Z) direction to the edge of the sensor in the YZ plane of the sensor's coordinate system. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorRectangularPattern.horizontal_half_angle`
              - The angle from the boresight (Z) direction to the edge of the sensor in the XZ plane of the sensor's coordinate system. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorRectangularPattern.angular_resolution`
              - Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorRectangularPattern


Property detail
---------------

.. py:property:: vertical_half_angle
    :canonical: ansys.stk.core.stkobjects.ISensorRectangularPattern.vertical_half_angle
    :type: typing.Any

    The angle from the boresight (Z) direction to the edge of the sensor in the YZ plane of the sensor's coordinate system. Uses Angle Dimension.

.. py:property:: horizontal_half_angle
    :canonical: ansys.stk.core.stkobjects.ISensorRectangularPattern.horizontal_half_angle
    :type: typing.Any

    The angle from the boresight (Z) direction to the edge of the sensor in the XZ plane of the sensor's coordinate system. Uses Angle Dimension.

.. py:property:: angular_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorRectangularPattern.angular_resolution
    :type: typing.Any

    Allows a user to set the angular separation between the pattern data points. This is an advanced user field, available only through STK's object model interface. The default value for the number of pattern samples is...


