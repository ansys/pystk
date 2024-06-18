ITimeToolEventArrayStartStopTimes
=================================

.. py:class:: ITimeToolEventArrayStartStopTimes

   object
   
   Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array. The array is then bounded by single interval spanning specified reference interval list...

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_stop_option`
            * - :py:meth:`~reference_intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayStartStopTimes


Property detail
---------------

.. py:property:: start_stop_option
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes.start_stop_option
    :type: "CRDN_START_STOP_OPTION"

    The edge type. At least one of the two edge types must be selected.

.. py:property:: reference_intervals
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayStartStopTimes.reference_intervals
    :type: "IAgCrdnEventIntervalList"

    The reference interval list.


