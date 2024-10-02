TimeToolTimeArrayStartStopTimes
===============================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeArrayStartStopTimes

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeArray`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

.. py:currentmodule:: TimeToolTimeArrayStartStopTimes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayStartStopTimes.start_stop_option`
              - The edge type. At least one of the two edge types must be selected.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeArrayStartStopTimes.reference_intervals`
              - The reference interval list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeArrayStartStopTimes


Property detail
---------------

.. py:property:: start_stop_option
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayStartStopTimes.start_stop_option
    :type: START_STOP_TYPE

    The edge type. At least one of the two edge types must be selected.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.TimeToolTimeArrayStartStopTimes.reference_intervals
    :type: ITimeToolTimeIntervalList

    The reference interval list.


