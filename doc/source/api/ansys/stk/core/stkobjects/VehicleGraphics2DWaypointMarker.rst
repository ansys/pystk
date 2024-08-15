VehicleGraphics2DWaypointMarker
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker

   Display options for waypoint and turn markers in the 2D Graphics window.

.. py:currentmodule:: VehicleGraphics2DWaypointMarker

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker.is_waypoint_markers_visible`
              - Opt whether to display a marker in the 2D Graphics window at each waypoint along the vehicle's route.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker.is_turn_markers_visible`
              - If a turn radius is specified for the waypoint, opt whether to display tic marks at the beginning and end of the turn, together with a mark representing the center point of the turn.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker.waypoint_markers`
              - Get the collection of waypoint markers.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DWaypointMarker


Property detail
---------------

.. py:property:: is_waypoint_markers_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker.is_waypoint_markers_visible
    :type: bool

    Opt whether to display a marker in the 2D Graphics window at each waypoint along the vehicle's route.

.. py:property:: is_turn_markers_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker.is_turn_markers_visible
    :type: bool

    If a turn radius is specified for the waypoint, opt whether to display tic marks at the beginning and end of the turn, together with a mark representing the center point of the turn.

.. py:property:: waypoint_markers
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker.waypoint_markers
    :type: VehicleGraphics2DWaypointMarkersCollection

    Get the collection of waypoint markers.


