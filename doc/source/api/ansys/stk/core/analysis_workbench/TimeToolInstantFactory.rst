TimeToolInstantFactory
======================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolInstantFactory

   The factory creates events.

.. py:currentmodule:: TimeToolInstantFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create`
              - Create and registers an event using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_epoch`
              - Create an event set at a specified date/time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_extremum`
              - Create an event that determines the time of global minimum or maximum of specified scalar calculation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_start_stop_time`
              - Create an event that is either the start or stop time selected from a reference interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_signaled`
              - Create an event recorded on a specified clock via signal transmission from an original time instant recorded on different clock.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_time_offset`
              - Create an event at fixed offset from specified reference event.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_smart_epoch_from_time`
              - Create a smart epoch from STK epoch.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_smart_epoch_from_event`
              - Create a smart epoch from an event.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.is_type_supported`
              - Return whether the specified type is supported.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.today`
              - Return Today time instant.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantFactory.tomorrow`
              - Return Tomorrow time instant.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolInstantFactory


Property detail
---------------

.. py:property:: today
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.today
    :type: ITimeToolInstant

    Return Today time instant.

.. py:property:: tomorrow
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.tomorrow
    :type: ITimeToolInstant

    Return Tomorrow time instant.


Method detail
-------------



.. py:method:: create(self, name: str, description: str, type: TimeEventType) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create

    Create and registers an event using specified name, description, and type.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`

        **type** : :obj:`~TimeEventType`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_epoch(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_epoch

    Create an event set at a specified date/time.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_extremum(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_extremum

    Create an event that determines the time of global minimum or maximum of specified scalar calculation.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_start_stop_time(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_start_stop_time

    Create an event that is either the start or stop time selected from a reference interval.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_signaled(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_signaled

    Create an event recorded on a specified clock via signal transmission from an original time instant recorded on different clock.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_time_offset(self, name: str, description: str) -> ITimeToolInstant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_time_offset

    Create an event at fixed offset from specified reference event.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ITimeToolInstant`

.. py:method:: create_smart_epoch_from_time(self, epoch: typing.Any) -> TimeToolInstantSmartEpoch
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_smart_epoch_from_time

    Create a smart epoch from STK epoch.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~TimeToolInstantSmartEpoch`

.. py:method:: create_smart_epoch_from_event(self, ref_event: ITimeToolInstant) -> TimeToolInstantSmartEpoch
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.create_smart_epoch_from_event

    Create a smart epoch from an event.

    :Parameters:

        **ref_event** : :obj:`~ITimeToolInstant`


    :Returns:

        :obj:`~TimeToolInstantSmartEpoch`

.. py:method:: is_type_supported(self, type: TimeEventType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

        **type** : :obj:`~TimeEventType`


    :Returns:

        :obj:`~bool`

