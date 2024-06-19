IVehicleGraphics2DTimeEventsElement
===================================

.. py:class:: IVehicleGraphics2DTimeEventsElement

   object
   
   2D Graphics time event.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_time_event_type`
              - Type of time event graphics: line, marker or text.
            * - :py:meth:`~is_time_event_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~time_event_type`
            * - :py:meth:`~time_event_type_supported_types`
            * - :py:meth:`~time_event_type_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeEventsElement


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventsElement.is_visible
    :type: bool

    Opt whether to display time event graphics.

.. py:property:: time_event_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventsElement.time_event_type
    :type: VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE

    Type of time event graphics: line, marker or text.

.. py:property:: time_event_type_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventsElement.time_event_type_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: time_event_type_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventsElement.time_event_type_data
    :type: IAgVeGfxTimeEventType

    Time event data.


Method detail
-------------




.. py:method:: set_time_event_type(self, timeEventType: VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventsElement.set_time_event_type

    Type of time event graphics: line, marker or text.

    :Parameters:

    **timeEventType** : :obj:`~VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_time_event_type_supported(self, timeEventType: VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventsElement.is_time_event_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **timeEventType** : :obj:`~VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE`

    :Returns:

        :obj:`~bool`



