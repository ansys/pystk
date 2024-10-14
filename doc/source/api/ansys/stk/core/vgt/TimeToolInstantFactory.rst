TimeToolInstantFactory
======================

.. py:class:: ansys.stk.core.vgt.TimeToolInstantFactory

   The factory creates events.

.. py:currentmodule:: TimeToolInstantFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create`
              - Create and registers an event using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_epoch`
              - Create an event set at a specified date/time.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_extremum`
              - Create an event that determines the time of global minimum or maximum of specified scalar calculation.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_start_stop_time`
              - Create an event that is either the start or stop time selected from a reference interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_signaled`
              - Create an event recorded on a specified clock via signal transmission from an original time instant recorded on different clock.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_time_offset`
              - Create an event at fixed offset from specified reference event.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_smart_epoch_from_time`
              - Create a smart epoch from STK epoch.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.create_smart_epoch_from_event`
              - Create a smart epoch from an event.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.is_type_supported`
              - Return whether the specified type is supported.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.today`
              - Returns Today time instant.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolInstantFactory.tomorrow`
              - Returns Tomorrow time instant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolInstantFactory


Property detail
---------------

.. py:property:: today
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.today
    :type: ITimeToolInstant

    Returns Today time instant.

.. py:property:: tomorrow
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.tomorrow
    :type: ITimeToolInstant

    Returns Tomorrow time instant.


Method detail
-------------



.. py:method:: create(self, name: str, description: str, type: TIME_EVENT_TYPE) -> ITimeToolInstant
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create

    Create and registers an event using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~TIME_EVENT_TYPE`

    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_epoch(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_epoch

    Create an event set at a specified date/time.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_extremum(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_extremum

    Create an event that determines the time of global minimum or maximum of specified scalar calculation.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_start_stop_time(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_start_stop_time

    Create an event that is either the start or stop time selected from a reference interval.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_signaled(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_signaled

    Create an event recorded on a specified clock via signal transmission from an original time instant recorded on different clock.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_time_offset(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_time_offset

    Create an event at fixed offset from specified reference event.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_smart_epoch_from_time(self, epoch: typing.Any) -> TimeToolInstantSmartEpoch
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_smart_epoch_from_time

    Create a smart epoch from STK epoch.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~TimeToolInstantSmartEpoch`

.. py:method:: create_smart_epoch_from_event(self, refEvent: ITimeToolInstant) -> TimeToolInstantSmartEpoch
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.create_smart_epoch_from_event

    Create a smart epoch from an event.

    :Parameters:

    **refEvent** : :obj:`~ITimeToolInstant`

    :Returns:

        :obj:`~TimeToolInstantSmartEpoch`

.. py:method:: is_type_supported(self, eType: TIME_EVENT_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.TimeToolInstantFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~TIME_EVENT_TYPE`

    :Returns:

        :obj:`~bool`

