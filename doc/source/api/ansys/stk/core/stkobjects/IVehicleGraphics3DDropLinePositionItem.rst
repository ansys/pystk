IVehicleGraphics3DDropLinePositionItem
======================================

.. py:class:: IVehicleGraphics3DDropLinePositionItem

   object
   
   Interface for drop lines from the vehicle's current position.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~is_visible`
            * - :py:meth:`~use_2d_color`
            * - :py:meth:`~color`
            * - :py:meth:`~line_width`
            * - :py:meth:`~line_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DDropLinePositionItem


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItem.type
    :type: VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE

    Get the option for where to end the drop line.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItem.is_visible
    :type: bool

    Opt whether to display the drop line.

.. py:property:: use_2d_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItem.use_2d_color
    :type: bool

    Opt whether to use the color in the vehicle's 2D attributes for the drop line.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItem.color
    :type: agcolor.Color

    Gets or sets the color of the drop line (if the 2D graphics color is not used).

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItem.line_width
    :type: LINE_WIDTH

    Gets or sets the line width of the drop line.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DDropLinePositionItem.line_style
    :type: LINE_STYLE

    Gets or sets the line style of the drop line.


