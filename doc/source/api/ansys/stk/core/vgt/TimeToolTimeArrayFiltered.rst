TimeToolTimeArrayFiltered
=========================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeArrayFiltered

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeArray`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Defined by filtering times from original time array according to specified filtering method.

.. py:currentmodule:: TimeToolTimeArrayFiltered

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered.original_time_array`
              - The original time array.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered.filter_type`
              - Skip Time Steps filter type omits from filtered time array any times that fall within specified time step of last accepted time sample. Skip Count filter type omits specified number of time samples since last accepted time sample...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered.count`
              - Specify the number of times skipped between accepted samples when FilterType is set to Skip Count...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered.step`
              - The number of steps skipped between accepted samples when FilterType is set to Skip Time Steps.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered.include_interval_stop_times`
              - If set to true, includes stop times of each interval from original time array.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayFiltered.filter_interval_list`
              - The interval list used to filter samples when FilterType is set to Skip Intervals.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeArrayFiltered


Property detail
---------------

.. py:property:: original_time_array
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFiltered.original_time_array
    :type: ITimeToolTimeArray

    The original time array.

.. py:property:: filter_type
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFiltered.filter_type
    :type: EVENT_ARRAY_FILTER_TYPE

    Skip Time Steps filter type omits from filtered time array any times that fall within specified time step of last accepted time sample. Skip Count filter type omits specified number of time samples since last accepted time sample...

.. py:property:: count
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFiltered.count
    :type: int

    Specify the number of times skipped between accepted samples when FilterType is set to Skip Count...

.. py:property:: step
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFiltered.step
    :type: float

    The number of steps skipped between accepted samples when FilterType is set to Skip Time Steps.

.. py:property:: include_interval_stop_times
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFiltered.include_interval_stop_times
    :type: bool

    If set to true, includes stop times of each interval from original time array.

.. py:property:: filter_interval_list
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayFiltered.filter_interval_list
    :type: ITimeToolTimeIntervalList

    The interval list used to filter samples when FilterType is set to Skip Intervals.


