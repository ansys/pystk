ITimeToolEventArrayFiltered
===========================

.. py:class:: ITimeToolEventArrayFiltered

   object
   
   Defined by filtering times from original time array according to specified filtering method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~original_time_array`
            * - :py:meth:`~filter_type`
            * - :py:meth:`~count`
            * - :py:meth:`~step`
            * - :py:meth:`~include_interval_stop_times`
            * - :py:meth:`~filter_interval_list`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayFiltered


Property detail
---------------

.. py:property:: original_time_array
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFiltered.original_time_array
    :type: "IAgCrdnEventArray"

    The original time array.

.. py:property:: filter_type
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFiltered.filter_type
    :type: "CRDN_EVENT_ARRAY_FILTER_TYPE"

    Skip Time Steps filter type omits from filtered time array any times that fall within specified time step of last accepted time sample. Skip Count filter type omits specified number of time samples since last accepted time sample...

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFiltered.count
    :type: int

    Specify the number of times skipped between accepted samples when FilterType is set to Skip Count...

.. py:property:: step
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFiltered.step
    :type: float

    The number of steps skipped between accepted samples when FilterType is set to Skip Time Steps.

.. py:property:: include_interval_stop_times
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFiltered.include_interval_stop_times
    :type: bool

    If set to true, includes stop times of each interval from original time array.

.. py:property:: filter_interval_list
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayFiltered.filter_interval_list
    :type: "IAgCrdnEventIntervalList"

    The interval list used to filter samples when FilterType is set to Skip Intervals.


