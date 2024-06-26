ITimeToolEventIntervalScaled
============================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalScaled

   object
   
   Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

.. py:currentmodule:: ITimeToolEventIntervalScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalScaled.original_interval`
              - The original interval.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalScaled.absolute_increment`
              - The absolute increment value which creates a interval by expanding (or shortening if negative) the original interval by shifting its start/stop times equally by half of specified increment value.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalScaled.relative_increment`
              - The relative increment value from which absolute increment is obtained by multiplying relative value by interval duration...
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalScaled.use_absolute_increment`
              - Specify whether to use absolute or relative increment.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalScaled


Property detail
---------------

.. py:property:: original_interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalScaled.original_interval
    :type: ITimeToolEventInterval

    The original interval.

.. py:property:: absolute_increment
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalScaled.absolute_increment
    :type: float

    The absolute increment value which creates a interval by expanding (or shortening if negative) the original interval by shifting its start/stop times equally by half of specified increment value.

.. py:property:: relative_increment
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalScaled.relative_increment
    :type: float

    The relative increment value from which absolute increment is obtained by multiplying relative value by interval duration...

.. py:property:: use_absolute_increment
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalScaled.use_absolute_increment
    :type: bool

    Specify whether to use absolute or relative increment.


