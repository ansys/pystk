VehicleGraphics2DTimeEventTypeMarker
====================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventType`

   2D Graphics time event: marker type.

.. py:currentmodule:: VehicleGraphics2DTimeEventTypeMarker

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.color`
              - Marker color.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.marker_style`
              - Marker style.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.unique_identifer`
              - Gets or sets the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.event_interval`
              - Event interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DTimeEventTypeMarker


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.color
    :type: agcolor.Color

    Marker color.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.marker_style
    :type: str

    Marker style.

.. py:property:: unique_identifer
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.unique_identifer
    :type: str

    Gets or sets the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.

.. py:property:: event_interval
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker.event_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Event interval.


