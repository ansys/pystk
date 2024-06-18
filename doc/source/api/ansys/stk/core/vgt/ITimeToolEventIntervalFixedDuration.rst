ITimeToolEventIntervalFixedDuration
===================================

.. py:class:: ITimeToolEventIntervalFixedDuration

   object
   
   Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_time_instant`
            * - :py:meth:`~start_offset`
            * - :py:meth:`~stop_offset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalFixedDuration


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFixedDuration.reference_time_instant
    :type: "IAgCrdnEvent"

    The reference time instant.

.. py:property:: start_offset
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFixedDuration.start_offset
    :type: float

    The start time offset value.

.. py:property:: stop_offset
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFixedDuration.stop_offset
    :type: float

    The stop time offset value.


