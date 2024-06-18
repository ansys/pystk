IVehicleGraphics2DWaypointMarker
================================

.. py:class:: IVehicleGraphics2DWaypointMarker

   object
   
   Display options for waypoint and turn markers in the 2D Graphics window.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_waypoint_markers_visible`
            * - :py:meth:`~is_turn_markers_visible`
            * - :py:meth:`~waypoint_markers`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DWaypointMarker


Property detail
---------------

.. py:property:: is_waypoint_markers_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarker.is_waypoint_markers_visible
    :type: bool

    Opt whether to display a marker in the 2D Graphics window at each waypoint along the vehicle's route.

.. py:property:: is_turn_markers_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarker.is_turn_markers_visible
    :type: bool

    If a turn radius is specified for the waypoint, opt whether to display tic marks at the beginning and end of the turn, together with a mark representing the center point of the turn.

.. py:property:: waypoint_markers
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DWaypointMarker.waypoint_markers
    :type: "IAgVeGfxWaypointMarkersCollection"

    Get the collection of waypoint markers.


