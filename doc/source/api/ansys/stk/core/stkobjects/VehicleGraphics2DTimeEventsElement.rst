VehicleGraphics2DTimeEventsElement
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement

   2D Graphics time event.

.. py:currentmodule:: VehicleGraphics2DTimeEventsElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.set_time_event_type`
              - Type of time event graphics: line, marker or text.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.is_time_event_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.show_graphics`
              - Opt whether to display time event graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.time_event_type`
              - Type of time event graphics: line, marker or text.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.time_event_type_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.time_event_type_data`
              - Time event data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DTimeEventsElement


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.show_graphics
    :type: bool

    Opt whether to display time event graphics.

.. py:property:: time_event_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.time_event_type
    :type: VehicleGraphics2DTimeEventType

    Type of time event graphics: line, marker or text.

.. py:property:: time_event_type_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.time_event_type_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: time_event_type_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.time_event_type_data
    :type: IVehicleGraphics2DTimeEventType

    Time event data.


Method detail
-------------




.. py:method:: set_time_event_type(self, time_event_type: VehicleGraphics2DTimeEventType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.set_time_event_type

    Type of time event graphics: line, marker or text.

    :Parameters:

    **time_event_type** : :obj:`~VehicleGraphics2DTimeEventType`

    :Returns:

        :obj:`~None`

.. py:method:: is_time_event_type_supported(self, time_event_type: VehicleGraphics2DTimeEventType) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement.is_time_event_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **time_event_type** : :obj:`~VehicleGraphics2DTimeEventType`

    :Returns:

        :obj:`~bool`



