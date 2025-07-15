VehicleGraphics2DTimeEventTypeText
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventType`

   2D Graphics time event: text type.

.. py:currentmodule:: VehicleGraphics2DTimeEventTypeText

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.set_offset_type`
              - Offset direction: left or right.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.is_offset_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.color`
              - Text color.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.text`
              - Text.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.unique_identifer`
              - User-defined unique ID.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_type`
              - Offset direction: left or right.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_pixels`
              - Offsets the position of the text to the right or the left of the ground track.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.event_interval`
              - Event interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DTimeEventTypeText


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.color
    :type: Color

    Text color.

.. py:property:: text
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.text
    :type: str

    Text.

.. py:property:: unique_identifer
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.unique_identifer
    :type: str

    User-defined unique ID.

.. py:property:: offset_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_type
    :type: VehicleGraphics2DOffset

    Offset direction: left or right.

.. py:property:: offset_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: offset_pixels
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.offset_pixels
    :type: int

    Offsets the position of the text to the right or the left of the ground track.

.. py:property:: event_interval
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.event_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Event interval.


Method detail
-------------








.. py:method:: set_offset_type(self, offset: VehicleGraphics2DOffset) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.set_offset_type

    Offset direction: left or right.

    :Parameters:

        **offset** : :obj:`~VehicleGraphics2DOffset`


    :Returns:

        :obj:`~None`

.. py:method:: is_offset_type_supported(self, offset: VehicleGraphics2DOffset) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText.is_offset_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **offset** : :obj:`~VehicleGraphics2DOffset`


    :Returns:

        :obj:`~bool`





