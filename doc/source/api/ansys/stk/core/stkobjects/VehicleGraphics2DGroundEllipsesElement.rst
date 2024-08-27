VehicleGraphics2DGroundEllipsesElement
======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement

   Ground ellipse 2D graphics properties.

.. py:currentmodule:: VehicleGraphics2DGroundEllipsesElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.ellipse_set_name`
              - Name of the ellipse set.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.static_graphics_2d`
              - Opt whether to display static graphics: all ellipses are displayed in the graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.dynamic_graphics_2d`
              - Opt whether to display dynamic graphics: an ellipse is interpolated between all specified ellipses, linearly interpolating semimajor/minor axes and bearings. Position is interpolated between the ellipses with the closest times to the animation time.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.interpolate`
              - Opt whether to interpolate between time points or the last known size and orientation for dynamic graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.is_name_visible`
              - Opt whether to display the name of the ellipse set at the center of each ellipse in the ellipse set.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.is_center_visible`
              - Opt whether to display the point marker for each ellipse in the ellipse set.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.color`
              - Color of the ellipse set name and ellipse graphics for all ellipses in the set.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.line_width`
              - Line width of ellipses in the set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DGroundEllipsesElement


Property detail
---------------

.. py:property:: ellipse_set_name
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.ellipse_set_name
    :type: str

    Name of the ellipse set.

.. py:property:: static_graphics_2d
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.static_graphics_2d
    :type: bool

    Opt whether to display static graphics: all ellipses are displayed in the graphics windows.

.. py:property:: dynamic_graphics_2d
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.dynamic_graphics_2d
    :type: bool

    Opt whether to display dynamic graphics: an ellipse is interpolated between all specified ellipses, linearly interpolating semimajor/minor axes and bearings. Position is interpolated between the ellipses with the closest times to the animation time.

.. py:property:: interpolate
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.interpolate
    :type: bool

    Opt whether to interpolate between time points or the last known size and orientation for dynamic graphics.

.. py:property:: is_name_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.is_name_visible
    :type: bool

    Opt whether to display the name of the ellipse set at the center of each ellipse in the ellipse set.

.. py:property:: is_center_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.is_center_visible
    :type: bool

    Opt whether to display the point marker for each ellipse in the ellipse set.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.color
    :type: agcolor.Color

    Color of the ellipse set name and ellipse graphics for all ellipses in the set.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement.line_width
    :type: LINE_WIDTH

    Line width of ellipses in the set.


