ITimeToolEventIntervalSmartInterval
===================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval

   object
   
   A smart interval.

.. py:currentmodule:: ITimeToolEventIntervalSmartInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_implicit_interval`
              - Set the reference interval and changes the state to Implicit.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.find_start_time`
              - Find a start time of the interval. An exception is thrown if the start time cannot be determined from the interval's current state.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.find_stop_time`
              - Find a stop time of the interval. An exception is thrown if the stop time cannot be determined from the interval's current state.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.get_start_epoch`
              - Return a copy of the start epoch. Changes to the epoch will not affect the state of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_epoch`
              - Set a start of the interval using specified epoch component.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.get_stop_epoch`
              - Return a copy of the stop epoch. Changes to the epoch will not affect the state of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_stop_epoch`
              - Set a stop of the interval using specified epoch component.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_explicit_interval`
              - Set the interval's start and the stop times changes the interval's state to explicit. Exception is thrown if specified start time is greater than stop time.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_and_stop_epochs`
              - Set the interval's start and stop epochs as two smart epoch components. Exception is thrown if specified start time is greater than stop time.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_and_stop_times`
              - Set the interval's start and stop epochs as explicit times. Exception is thrown if specified start time is greater than stop time.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_epoch_and_duration`
              - Set the interval's start epoch and the interval's duration.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_time_and_duration`
              - Set the interval's start time and the interval's duration.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.reference_interval`
              - The reference interval used to compute start/stop times of this interval if the state of the interval is set to implicit.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.duration_as_string`
              - The duration of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.state`
              - A state of the smart interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalSmartInterval


Property detail
---------------

.. py:property:: reference_interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.reference_interval
    :type: ITimeToolEventInterval

    The reference interval used to compute start/stop times of this interval if the state of the interval is set to implicit.

.. py:property:: duration_as_string
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.duration_as_string
    :type: str

    The duration of the interval.

.. py:property:: state
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.state
    :type: CRDN_SMART_INTERVAL_STATE

    A state of the smart interval.


Method detail
-------------






.. py:method:: set_implicit_interval(self, eventInterval: ITimeToolEventInterval) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_implicit_interval

    Set the reference interval and changes the state to Implicit.

    :Parameters:

    **eventInterval** : :obj:`~ITimeToolEventInterval`

    :Returns:

        :obj:`~None`

.. py:method:: find_start_time(self) -> typing.Any
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.find_start_time

    Find a start time of the interval. An exception is thrown if the start time cannot be determined from the interval's current state.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: find_stop_time(self) -> typing.Any
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.find_stop_time

    Find a stop time of the interval. An exception is thrown if the stop time cannot be determined from the interval's current state.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_start_epoch(self) -> ITimeToolEventSmartEpoch
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.get_start_epoch

    Return a copy of the start epoch. Changes to the epoch will not affect the state of the interval.

    :Returns:

        :obj:`~ITimeToolEventSmartEpoch`

.. py:method:: set_start_epoch(self, startEpoch: ITimeToolEventSmartEpoch) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_epoch

    Set a start of the interval using specified epoch component.

    :Parameters:

    **startEpoch** : :obj:`~ITimeToolEventSmartEpoch`

    :Returns:

        :obj:`~None`

.. py:method:: get_stop_epoch(self) -> ITimeToolEventSmartEpoch
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.get_stop_epoch

    Return a copy of the stop epoch. Changes to the epoch will not affect the state of the interval.

    :Returns:

        :obj:`~ITimeToolEventSmartEpoch`

.. py:method:: set_stop_epoch(self, stopEpoch: ITimeToolEventSmartEpoch) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_stop_epoch

    Set a stop of the interval using specified epoch component.

    :Parameters:

    **stopEpoch** : :obj:`~ITimeToolEventSmartEpoch`

    :Returns:

        :obj:`~None`

.. py:method:: set_explicit_interval(self, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_explicit_interval

    Set the interval's start and the stop times changes the interval's state to explicit. Exception is thrown if specified start time is greater than stop time.

    :Parameters:

    **start** : :obj:`~typing.Any`
    **stop** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_start_and_stop_epochs(self, refStartEpoch: ITimeToolEventSmartEpoch, refStopEpoch: ITimeToolEventSmartEpoch) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_and_stop_epochs

    Set the interval's start and stop epochs as two smart epoch components. Exception is thrown if specified start time is greater than stop time.

    :Parameters:

    **refStartEpoch** : :obj:`~ITimeToolEventSmartEpoch`
    **refStopEpoch** : :obj:`~ITimeToolEventSmartEpoch`

    :Returns:

        :obj:`~None`

.. py:method:: set_start_and_stop_times(self, startTime: typing.Any, stopTime: typing.Any) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_and_stop_times

    Set the interval's start and stop epochs as explicit times. Exception is thrown if specified start time is greater than stop time.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_start_epoch_and_duration(self, refStartEpoch: ITimeToolEventSmartEpoch, durationStr: str) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_epoch_and_duration

    Set the interval's start epoch and the interval's duration.

    :Parameters:

    **refStartEpoch** : :obj:`~ITimeToolEventSmartEpoch`
    **durationStr** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: set_start_time_and_duration(self, epoch: typing.Any, durationStr: str) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalSmartInterval.set_start_time_and_duration

    Set the interval's start time and the interval's duration.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **durationStr** : :obj:`~str`

    :Returns:

        :obj:`~None`

