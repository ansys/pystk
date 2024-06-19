IVehicleGraphics2DAttributesBasic
=================================

.. py:class:: IVehicleGraphics2DAttributesBasic

   IVehicleGraphics2DAttributes
   
   Basic 2D Graphics Attributes for a vehicle.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit`
            * - :py:meth:`~is_visible`
            * - :py:meth:`~color`
            * - :py:meth:`~marker_style`
            * - :py:meth:`~label_visible`
            * - :py:meth:`~line`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesBasic


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic.inherit
    :type: bool

    Inherit certain 2D graphics settings from the scenario level.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic.is_visible
    :type: bool

    Show 2D Graphics for the vehicle.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic.color
    :type: agcolor.Color

    Color in which vehicle marker, label and tracks are displayed.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic.marker_style
    :type: str

    Style of marker used to represent vehicle.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic.label_visible
    :type: bool

    Opt whether to display the vehicle's label.

.. py:property:: line
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic.line
    :type: IAgVeGfxLine

    Get the line display properties for the vehicle.


