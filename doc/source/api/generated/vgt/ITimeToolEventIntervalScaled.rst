ITimeToolEventIntervalScaled
============================

.. py:class:: ITimeToolEventIntervalScaled

   object
   
   Interval defined by scaling original interval using either absolute or relative scale. If resulting interval's start becomes after its stop, the interval becomes undefined.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~original_interval`
            * - :py:meth:`~absolute_increment`
            * - :py:meth:`~relative_increment`
            * - :py:meth:`~use_absolute_increment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalScaled


Property detail
---------------

.. py:property:: original_interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalScaled.original_interval
    :type: "IAgCrdnEventInterval"

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


