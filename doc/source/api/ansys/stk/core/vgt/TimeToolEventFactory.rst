TimeToolEventFactory
====================

.. py:class:: ansys.stk.core.vgt.TimeToolEventFactory

   Bases: 

   The factory creates events.

.. py:currentmodule:: TimeToolEventFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create`
              - Create and registers an event using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_event_epoch`
              - Create an event set at a specified date/time.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_event_extremum`
              - Create an event that determines the time of global minimum or maximum of specified scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_event_start_stop_time`
              - Create an event that is either the start or stop time selected from a reference interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_event_signaled`
              - Create an event recorded on a specified clock via signal transmission from an original time instant recorded on different clock.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_event_time_offset`
              - Create an event at fixed offset from specified reference event.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_smart_epoch_from_time`
              - Create a smart epoch from STK epoch.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.create_smart_epoch_from_event`
              - Create a smart epoch from an event.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.is_type_supported`
              - Return whether the specified type is supported.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.today`
              - Returns Today time instant.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventFactory.tomorrow`
              - Returns Tomorrow time instant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventFactory


Property detail
---------------

.. py:property:: today
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.today
    :type: ITimeToolEvent

    Returns Today time instant.

.. py:property:: tomorrow
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.tomorrow
    :type: ITimeToolEvent

    Returns Tomorrow time instant.


Method detail
-------------



.. py:method:: create(self, name: str, description: str, type: CRDN_EVENT_TYPE) -> ITimeToolEvent
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create

    Create and registers an event using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_EVENT_TYPE`

    :Returns:

        :obj:`~ITimeToolEvent`

.. py:method:: create_event_epoch(self, name: str, description: str) -> ITimeToolEvent
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_event_epoch

    Create an event set at a specified date/time.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEvent`

.. py:method:: create_event_extremum(self, name: str, description: str) -> ITimeToolEvent
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_event_extremum

    Create an event that determines the time of global minimum or maximum of specified scalar calculation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEvent`

.. py:method:: create_event_start_stop_time(self, name: str, description: str) -> ITimeToolEvent
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_event_start_stop_time

    Create an event that is either the start or stop time selected from a reference interval.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEvent`

.. py:method:: create_event_signaled(self, name: str, description: str) -> ITimeToolEvent
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_event_signaled

    Create an event recorded on a specified clock via signal transmission from an original time instant recorded on different clock.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEvent`

.. py:method:: create_event_time_offset(self, name: str, description: str) -> ITimeToolEvent
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_event_time_offset

    Create an event at fixed offset from specified reference event.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEvent`

.. py:method:: create_smart_epoch_from_time(self, epoch: typing.Any) -> TimeToolEventSmartEpoch
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_smart_epoch_from_time

    Create a smart epoch from STK epoch.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~TimeToolEventSmartEpoch`

.. py:method:: create_smart_epoch_from_event(self, refEvent: ITimeToolEvent) -> TimeToolEventSmartEpoch
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.create_smart_epoch_from_event

    Create a smart epoch from an event.

    :Parameters:

    **refEvent** : :obj:`~ITimeToolEvent`

    :Returns:

        :obj:`~TimeToolEventSmartEpoch`

.. py:method:: is_type_supported(self, eType: CRDN_EVENT_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolEventFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_EVENT_TYPE`

    :Returns:

        :obj:`~bool`

