TimeToolTimeArrayFiltered
=========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeArray`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by filtering times from original time array according to specified filtering method.

.. py:currentmodule:: TimeToolTimeArrayFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.count`
              - Specify the number of times skipped between accepted samples when FilterType is set to Skip Count...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.filter_interval_list`
              - The interval list used to filter samples when FilterType is set to Skip Intervals.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.filter_type`
              - Skip Time Steps filter type omits from filtered time array any times that fall within specified time step of last accepted time sample. Skip Count filter type omits specified number of time samples since last accepted time sample...
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.include_interval_stop_times`
              - If set to true, includes stop times of each interval from original time array.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.original_time_array`
              - The original time array.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.step`
              - The number of steps skipped between accepted samples when FilterType is set to Skip Time Steps.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeArrayFiltered


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.count
    :type: int

    Specify the number of times skipped between accepted samples when FilterType is set to Skip Count...

.. py:property:: filter_interval_list
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.filter_interval_list
    :type: ITimeToolTimeIntervalList

    The interval list used to filter samples when FilterType is set to Skip Intervals.

.. py:property:: filter_type
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.filter_type
    :type: EventArrayFilterType

    Skip Time Steps filter type omits from filtered time array any times that fall within specified time step of last accepted time sample. Skip Count filter type omits specified number of time samples since last accepted time sample...

.. py:property:: include_interval_stop_times
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.include_interval_stop_times
    :type: bool

    If set to true, includes stop times of each interval from original time array.

.. py:property:: original_time_array
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.original_time_array
    :type: ITimeToolTimeArray

    The original time array.

.. py:property:: step
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeArrayFiltered.step
    :type: float

    The number of steps skipped between accepted samples when FilterType is set to Skip Time Steps.


