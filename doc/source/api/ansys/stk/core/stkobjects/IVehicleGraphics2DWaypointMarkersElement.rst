IVehicleGraphics2DWaypointMarkersElement
========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement

   object
   
   2D Graphics properties of element of waypoint collection.

.. py:currentmodule:: IVehicleGraphics2DWaypointMarkersElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.is_label_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.label`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.use_veh_color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.marker_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DWaypointMarkersElement


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.time
    :type: typing.Any

    Time of the waypoint. Uses DateFormat Dimension.

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.is_visible
    :type: bool

    Opt whether to show the waypoint.

.. py:property:: is_label_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.is_label_visible
    :type: bool

    Opt whether to display a label for the waypoint.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.label
    :type: str

    Content of the waypoint label.

.. py:property:: use_veh_color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.use_veh_color
    :type: bool

    Opt whether to set the waypoint color to the color of the vehicle.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.color
    :type: agcolor.Color

    Color of the waypoint marker.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarkersElement.marker_style
    :type: str

    Style of the waypoint marker.


