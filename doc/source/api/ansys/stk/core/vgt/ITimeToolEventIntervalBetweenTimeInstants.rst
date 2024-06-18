ITimeToolEventIntervalBetweenTimeInstants
=========================================

.. py:class:: ITimeToolEventIntervalBetweenTimeInstants

   object
   
   Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time_instant`
            * - :py:meth:`~stop_time_instant`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalBetweenTimeInstants


Property detail
---------------

.. py:property:: start_time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalBetweenTimeInstants.start_time_instant
    :type: "IAgCrdnEvent"

    The start time instant of the interval.

.. py:property:: stop_time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalBetweenTimeInstants.stop_time_instant
    :type: "IAgCrdnEvent"

    The stop time instant of the interval.


