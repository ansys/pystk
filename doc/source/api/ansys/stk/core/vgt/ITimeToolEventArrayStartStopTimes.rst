ITimeToolEventArrayStartStopTimes
=================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes

   object
   
   Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

.. py:currentmodule:: ITimeToolEventArrayStartStopTimes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes.start_stop_option`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes.reference_intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayStartStopTimes


Property detail
---------------

.. py:property:: start_stop_option
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes.start_stop_option
    :type: CRDN_START_STOP_OPTION

    The edge type. At least one of the two edge types must be selected.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes.reference_intervals
    :type: ITimeToolEventIntervalList

    The reference interval list.


