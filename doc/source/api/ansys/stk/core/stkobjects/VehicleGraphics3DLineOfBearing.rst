VehicleGraphics3DLineOfBearing
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximityAreaObject`

   Define a line of bearing which is drawn from an origin in the direction of a bearing.

.. py:currentmodule:: VehicleGraphics3DLineOfBearing

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing`
              - Gets or sets the bearing value, relative to North. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_latitude`
              - Specifies the latitude for the origin of the line of bearing. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_longitude`
              - Specifies the longitude for the origin of the line of bearing. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_altitude`
              - Specifies the altitude for the origin of the line of bearing. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.length`
              - Gets or sets the length of the line of bearing. The value must be greater than 0. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing_error`
              - Gets or sets the margin of error in either direction of the Line of Bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_color`
              - Gets or sets the color of the bearing error lines. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_line_width`
              - Gets or sets the line width of the bearing error lines.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DLineOfBearing


Property detail
---------------

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing
    :type: float

    Gets or sets the bearing value, relative to North. Uses Angle Dimension.

.. py:property:: origin_latitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_latitude
    :type: float

    Specifies the latitude for the origin of the line of bearing. Uses Angle Dimension.

.. py:property:: origin_longitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_longitude
    :type: float

    Specifies the longitude for the origin of the line of bearing. Uses Angle Dimension.

.. py:property:: origin_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_altitude
    :type: float

    Specifies the altitude for the origin of the line of bearing. Uses Distance Dimension.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.length
    :type: float

    Gets or sets the length of the line of bearing. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: bearing_error
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing_error
    :type: float

    Gets or sets the margin of error in either direction of the Line of Bearing.

.. py:property:: error_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_color
    :type: agcolor.Color

    Gets or sets the color of the bearing error lines. Dimensionless.

.. py:property:: error_line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_line_width
    :type: LineWidth

    Gets or sets the line width of the bearing error lines.


