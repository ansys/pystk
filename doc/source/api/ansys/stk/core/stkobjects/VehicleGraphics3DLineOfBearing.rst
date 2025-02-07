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
              - Get or set the bearing value, relative to North. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_latitude`
              - Specify the latitude for the origin of the line of bearing. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_longitude`
              - Specify the longitude for the origin of the line of bearing. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_altitude`
              - Specify the altitude for the origin of the line of bearing. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.length`
              - Get or set the length of the line of bearing. The value must be greater than 0. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing_error`
              - Get or set the margin of error in either direction of the Line of Bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_color`
              - Get or set the color of the bearing error lines. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_line_width`
              - Get or set the line width of the bearing error lines.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DLineOfBearing


Property detail
---------------

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing
    :type: float

    Get or set the bearing value, relative to North. Uses Angle Dimension.

.. py:property:: origin_latitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_latitude
    :type: float

    Specify the latitude for the origin of the line of bearing. Uses Angle Dimension.

.. py:property:: origin_longitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_longitude
    :type: float

    Specify the longitude for the origin of the line of bearing. Uses Angle Dimension.

.. py:property:: origin_altitude
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.origin_altitude
    :type: float

    Specify the altitude for the origin of the line of bearing. Uses Distance Dimension.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.length
    :type: float

    Get or set the length of the line of bearing. The value must be greater than 0. Uses Distance Dimension.

.. py:property:: bearing_error
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.bearing_error
    :type: float

    Get or set the margin of error in either direction of the Line of Bearing.

.. py:property:: error_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_color
    :type: agcolor.Color

    Get or set the color of the bearing error lines. Dimensionless.

.. py:property:: error_line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing.error_line_width
    :type: LineWidth

    Get or set the line width of the bearing error lines.


