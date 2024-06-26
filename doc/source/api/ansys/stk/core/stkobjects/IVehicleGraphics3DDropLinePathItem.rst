IVehicleGraphics3DDropLinePathItem
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem

   object
   
   Interface for drop lines at intervals along the vehicle's path.

.. py:currentmodule:: IVehicleGraphics3DDropLinePathItem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.type`
              - Get the option for where to end the drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.is_visible`
              - Opt whether to display the drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.use_2d_color`
              - Opt whether to use the color in the vehicle's 2D attributes for the drop lines.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.color`
              - Gets or sets the color of the drop lines (if the 2D graphics color is not used).
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.line_width`
              - Gets or sets the width of the drop line from orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.interval`
              - Gets or sets the time interval between drop lines. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.line_style`
              - Gets or sets the line style of the drop line.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DDropLinePathItem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.type
    :type: VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE

    Get the option for where to end the drop lines.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.is_visible
    :type: bool

    Opt whether to display the drop lines.

.. py:property:: use_2d_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.use_2d_color
    :type: bool

    Opt whether to use the color in the vehicle's 2D attributes for the drop lines.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.color
    :type: agcolor.Color

    Gets or sets the color of the drop lines (if the 2D graphics color is not used).

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.line_width
    :type: LINE_WIDTH

    Gets or sets the width of the drop line from orbit.

.. py:property:: interval
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.interval
    :type: float

    Gets or sets the time interval between drop lines. Uses Time Dimension.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePathItem.line_style
    :type: LINE_STYLE

    Gets or sets the line style of the drop line.


