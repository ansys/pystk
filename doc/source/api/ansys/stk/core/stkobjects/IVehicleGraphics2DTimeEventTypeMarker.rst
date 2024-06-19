IVehicleGraphics2DTimeEventTypeMarker
=====================================

.. py:class:: IVehicleGraphics2DTimeEventTypeMarker

   object
   
   2D Graphics time event: marker type.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~color`
            * - :py:meth:`~marker_style`
            * - :py:meth:`~unique_id`
            * - :py:meth:`~event_interval`


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
    :type: IAgCrdnEventIntervalSmartInterval

    Event interval.


