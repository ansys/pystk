VehicleGraphics3DDropLinePathItem
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem

   Drop lines at intervals along the vehicle's path.

.. py:currentmodule:: VehicleGraphics3DDropLinePathItem

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.type`
              - Get the option for where to end the drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.show_graphics`
              - Opt whether to display the drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.use_2d_color`
              - Opt whether to use the color in the vehicle's 2D attributes for the drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.color`
              - Get or set the color of the drop lines (if the 2D graphics color is not used).
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.line_width`
              - Get or set the width of the drop line from orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.interval`
              - Get or set the time interval between drop lines. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.line_style`
              - Get or set the line style of the drop line.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DDropLinePathItem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.type
    :type: VehicleGraphics3DDropLineType

    Get the option for where to end the drop lines.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.show_graphics
    :type: bool

    Opt whether to display the drop lines.

.. py:property:: use_2d_color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.use_2d_color
    :type: bool

    Opt whether to use the color in the vehicle's 2D attributes for the drop lines.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.color
    :type: agcolor.Color

    Get or set the color of the drop lines (if the 2D graphics color is not used).

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.line_width
    :type: LineWidth

    Get or set the width of the drop line from orbit.

.. py:property:: interval
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.interval
    :type: float

    Get or set the time interval between drop lines. Uses Time Dimension.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem.line_style
    :type: LineStyle

    Get or set the line style of the drop line.


