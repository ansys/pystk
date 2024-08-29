TimeToolEventArrayStartStopTimes
================================

.. py:class:: ansys.stk.core.vgt.TimeToolEventArrayStartStopTimes

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEventArray`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

.. py:currentmodule:: TimeToolEventArrayStartStopTimes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventArrayStartStopTimes.start_stop_option`
              - The edge type. At least one of the two edge types must be selected.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventArrayStartStopTimes.reference_intervals`
              - The reference interval list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventArrayStartStopTimes


Property detail
---------------

.. py:property:: start_stop_option
    :canonical: ansys.stk.core.vgt.TimeToolEventArrayStartStopTimes.start_stop_option
    :type: CRDN_START_STOP_OPTION

    The edge type. At least one of the two edge types must be selected.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.TimeToolEventArrayStartStopTimes.reference_intervals
    :type: ITimeToolEventIntervalList

    The reference interval list.


