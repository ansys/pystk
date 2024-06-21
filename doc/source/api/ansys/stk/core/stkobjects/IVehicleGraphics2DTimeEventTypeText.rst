IVehicleGraphics2DTimeEventTypeText
===================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText

   object
   
   2D Graphics time event: text type.

.. py:currentmodule:: IVehicleGraphics2DTimeEventTypeText

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.set_offset_type`
              - Offset direction: left or right.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.is_offset_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.text`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.unique_id`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.offset_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.offset_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.offset_pixels`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.event_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DTimeEventTypeText


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.color
    :type: agcolor.Color

    Text color.

.. py:property:: text
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.text
    :type: str

    Text.

.. py:property:: unique_id
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.unique_id
    :type: str

    User-defined unique ID.

.. py:property:: offset_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.offset_type
    :type: VEHICLE_GRAPHICS_2D_OFFSET

    Offset direction: left or right.

.. py:property:: offset_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.offset_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: offset_pixels
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.offset_pixels
    :type: int

    Offsets the position of the text to the right or the left of the ground track.

.. py:property:: event_interval
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.event_interval
    :type: ITimeToolEventIntervalSmartInterval

    Event interval.


Method detail
-------------








.. py:method:: set_offset_type(self, offset: VEHICLE_GRAPHICS_2D_OFFSET) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.set_offset_type

    Offset direction: left or right.

    :Parameters:

    **offset** : :obj:`~VEHICLE_GRAPHICS_2D_OFFSET`

    :Returns:

        :obj:`~None`

.. py:method:: is_offset_type_supported(self, offset: VEHICLE_GRAPHICS_2D_OFFSET) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventTypeText.is_offset_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **offset** : :obj:`~VEHICLE_GRAPHICS_2D_OFFSET`

    :Returns:

        :obj:`~bool`





