IVehicleGraphics2DTimeEventTypeLine
===================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine

   object
   
   2D Graphics time event: line type.

.. py:currentmodule:: IVehicleGraphics2DTimeEventTypeLine

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.set_offset_type`
              - Offset direction (left or right).
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.is_offset_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.color`
              - Line color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.line_style`
              - Line style.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.line_width`
              - Line width.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.unique_id`
              - User-defined unique ID.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.offset_type`
              - Offset direction (left or right).
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.offset_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.offset_pixels`
              - Offset amount in pixels. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.event_interval`
              - Event interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeEventTypeLine


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.color
    :type: agcolor.Color

    Line color.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.line_style
    :type: LINE_STYLE

    Line style.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.line_width
    :type: LINE_WIDTH

    Line width.

.. py:property:: unique_id
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.unique_id
    :type: str

    User-defined unique ID.

.. py:property:: offset_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.offset_type
    :type: VEHICLE_GRAPHICS_2D_OFFSET

    Offset direction (left or right).

.. py:property:: offset_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.offset_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: offset_pixels
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.offset_pixels
    :type: int

    Offset amount in pixels. Dimensionless.

.. py:property:: event_interval
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.event_interval
    :type: ITimeToolEventIntervalSmartInterval

    Event interval.


Method detail
-------------










.. py:method:: set_offset_type(self, offset: VEHICLE_GRAPHICS_2D_OFFSET) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.set_offset_type

    Offset direction (left or right).

    :Parameters:

    **offset** : :obj:`~VEHICLE_GRAPHICS_2D_OFFSET`

    :Returns:

        :obj:`~None`

.. py:method:: is_offset_type_supported(self, offset: VEHICLE_GRAPHICS_2D_OFFSET) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeLine.is_offset_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **offset** : :obj:`~VEHICLE_GRAPHICS_2D_OFFSET`

    :Returns:

        :obj:`~bool`





