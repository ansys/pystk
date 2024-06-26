IVehicleGraphics2DTimeEventTypeMarker
=====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker

   object
   
   2D Graphics time event: marker type.

.. py:currentmodule:: IVehicleGraphics2DTimeEventTypeMarker

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.color`
              - Marker color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.marker_style`
              - Marker style.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.unique_id`
              - Gets or sets the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.event_interval`
              - Event interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeEventTypeMarker


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.color
    :type: agcolor.Color

    Marker color.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.marker_style
    :type: str

    Marker style.

.. py:property:: unique_id
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.unique_id
    :type: str

    Gets or sets the Unique ID is a unique identifier for each time event. The default is TimeEvent<number>. The unique ID is required when modifying time event data using the Graphics TimeEvent Connect command.

.. py:property:: event_interval
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeMarker.event_interval
    :type: ITimeToolEventIntervalSmartInterval

    Event interval.


