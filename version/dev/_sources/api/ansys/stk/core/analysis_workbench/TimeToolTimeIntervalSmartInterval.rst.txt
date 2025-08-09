TimeToolTimeIntervalSmartInterval
=================================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A smart interval.

.. py:currentmodule:: TimeToolTimeIntervalSmartInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.find_start_time`
              - Find a start time of the interval. An exception is thrown if the start time cannot be determined from the interval's current state.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.find_stop_time`
              - Find a stop time of the interval. An exception is thrown if the stop time cannot be determined from the interval's current state.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.get_start_epoch`
              - Return a copy of the start epoch. Changes to the epoch will not affect the state of the interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.get_stop_epoch`
              - Return a copy of the stop epoch. Changes to the epoch will not affect the state of the interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_explicit_interval`
              - Set the interval's start and the stop times changes the interval's state to explicit. Exception is thrown if specified start time is greater than stop time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_implicit_interval`
              - Set the reference interval and changes the state to Implicit.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_and_stop_epochs`
              - Set the interval's start and stop epochs as two smart epoch components. Exception is thrown if specified start time is greater than stop time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_and_stop_times`
              - Set the interval's start and stop epochs as explicit times. Exception is thrown if specified start time is greater than stop time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_epoch`
              - Set a start of the interval using specified epoch component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_epoch_and_duration`
              - Set the interval's start epoch and the interval's duration.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_time_and_duration`
              - Set the interval's start time and the interval's duration.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_stop_epoch`
              - Set a stop of the interval using specified epoch component.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.duration_as_string`
              - The duration of the interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.reference_interval`
              - The reference interval used to compute start/stop times of this interval if the state of the interval is set to implicit.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.state`
              - A state of the smart interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalSmartInterval


Property detail
---------------

.. py:property:: duration_as_string
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.duration_as_string
    :type: str

    The duration of the interval.

.. py:property:: reference_interval
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.reference_interval
    :type: ITimeToolTimeInterval

    The reference interval used to compute start/stop times of this interval if the state of the interval is set to implicit.

.. py:property:: state
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.state
    :type: SmartIntervalState

    A state of the smart interval.


Method detail
-------------



.. py:method:: find_start_time(self) -> typing.Any
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.find_start_time

    Find a start time of the interval. An exception is thrown if the start time cannot be determined from the interval's current state.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: find_stop_time(self) -> typing.Any
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.find_stop_time

    Find a stop time of the interval. An exception is thrown if the stop time cannot be determined from the interval's current state.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_start_epoch(self) -> TimeToolInstantSmartEpoch
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.get_start_epoch

    Return a copy of the start epoch. Changes to the epoch will not affect the state of the interval.

    :Returns:

        :obj:`~TimeToolInstantSmartEpoch`

.. py:method:: get_stop_epoch(self) -> TimeToolInstantSmartEpoch
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.get_stop_epoch

    Return a copy of the stop epoch. Changes to the epoch will not affect the state of the interval.

    :Returns:

        :obj:`~TimeToolInstantSmartEpoch`


.. py:method:: set_explicit_interval(self, start: typing.Any, stop: typing.Any) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_explicit_interval

    Set the interval's start and the stop times changes the interval's state to explicit. Exception is thrown if specified start time is greater than stop time.

    :Parameters:

        **start** : :obj:`~typing.Any`

        **stop** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: set_implicit_interval(self, event_interval: ITimeToolTimeInterval) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_implicit_interval

    Set the reference interval and changes the state to Implicit.

    :Parameters:

        **event_interval** : :obj:`~ITimeToolTimeInterval`


    :Returns:

        :obj:`~None`

.. py:method:: set_start_and_stop_epochs(self, ref_start_epoch: TimeToolInstantSmartEpoch, ref_stop_epoch: TimeToolInstantSmartEpoch) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_and_stop_epochs

    Set the interval's start and stop epochs as two smart epoch components. Exception is thrown if specified start time is greater than stop time.

    :Parameters:

        **ref_start_epoch** : :obj:`~TimeToolInstantSmartEpoch`

        **ref_stop_epoch** : :obj:`~TimeToolInstantSmartEpoch`


    :Returns:

        :obj:`~None`

.. py:method:: set_start_and_stop_times(self, start_time: typing.Any, stop_time: typing.Any) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_and_stop_times

    Set the interval's start and stop epochs as explicit times. Exception is thrown if specified start time is greater than stop time.

    :Parameters:

        **start_time** : :obj:`~typing.Any`

        **stop_time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: set_start_epoch(self, start_epoch: TimeToolInstantSmartEpoch) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_epoch

    Set a start of the interval using specified epoch component.

    :Parameters:

        **start_epoch** : :obj:`~TimeToolInstantSmartEpoch`


    :Returns:

        :obj:`~None`

.. py:method:: set_start_epoch_and_duration(self, ref_start_epoch: TimeToolInstantSmartEpoch, duration_str: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_epoch_and_duration

    Set the interval's start epoch and the interval's duration.

    :Parameters:

        **ref_start_epoch** : :obj:`~TimeToolInstantSmartEpoch`

        **duration_str** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_start_time_and_duration(self, epoch: typing.Any, duration_str: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_start_time_and_duration

    Set the interval's start time and the interval's duration.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **duration_str** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: set_stop_epoch(self, stop_epoch: TimeToolInstantSmartEpoch) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalSmartInterval.set_stop_epoch

    Set a stop of the interval using specified epoch component.

    :Parameters:

        **stop_epoch** : :obj:`~TimeToolInstantSmartEpoch`


    :Returns:

        :obj:`~None`



