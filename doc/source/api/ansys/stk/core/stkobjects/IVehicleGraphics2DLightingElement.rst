IVehicleGraphics2DLightingElement
=================================

.. py:class:: IVehicleGraphics2DLightingElement

   object
   
   Lighting condition properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~visible`
            * - :py:meth:`~color`
            * - :py:meth:`~marker_style`
            * - :py:meth:`~line_style`
            * - :py:meth:`~line_width`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DLightingElement


Property detail
---------------

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLightingElement.visible
    :type: bool

    Opt whether to display the orbit and/or ground track in the color assigned to the specified lighting condition.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLightingElement.color
    :type: agcolor.Color

    Gets or sets the color of the line that will mark the region representing the selected lighting condition.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLightingElement.marker_style
    :type: str

    Gets or sets the object marker while the vehicle is within a particular region representing the selected lighting condition.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLightingElement.line_style
    :type: "LINE_STYLE"

    Gets or sets the type of line that will mark the region representing the selected lighting condition.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLightingElement.line_width
    :type: "LINE_WIDTH"

    Gets or sets the width of the line that will mark the region representing the selected lighting condition.


