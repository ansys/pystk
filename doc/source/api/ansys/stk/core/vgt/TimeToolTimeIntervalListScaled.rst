TimeToolTimeIntervalListScaled
==============================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalListScaled

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval List defined by scaling every interval in original interval list using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval is removed from scaled list...

.. py:currentmodule:: TimeToolTimeIntervalListScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.original_intervals`
              - The original interval list.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.absolute_increment`
              - The absolute increment value which creates a new interval list by expanding (or shortening if negative) every interval in the original interval list by shifting interval's start/stop times equally by half of specified increment value.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.relative_increment`
              - The relative increment value from which absolute increment is obtained by multiplying relative value by interval duration...
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.use_absolute_increment`
              - Specify whether to use absolute or relative increment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalListScaled


Property detail
---------------

.. py:property:: original_intervals
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.original_intervals
    :type: ITimeToolTimeIntervalList

    The original interval list.

.. py:property:: absolute_increment
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.absolute_increment
    :type: float

    The absolute increment value which creates a new interval list by expanding (or shortening if negative) every interval in the original interval list by shifting interval's start/stop times equally by half of specified increment value.

.. py:property:: relative_increment
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.relative_increment
    :type: float

    The relative increment value from which absolute increment is obtained by multiplying relative value by interval duration...

.. py:property:: use_absolute_increment
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListScaled.use_absolute_increment
    :type: bool

    Specify whether to use absolute or relative increment.


