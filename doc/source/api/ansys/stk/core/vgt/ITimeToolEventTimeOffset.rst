ITimeToolEventTimeOffset
========================

.. py:class:: ITimeToolEventTimeOffset

   object
   
   Event at fixed offset from specified reference event.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_time_instant`
            * - :py:meth:`~time_offset2`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventTimeOffset


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventTimeOffset.reference_time_instant
    :type: "IAgCrdnEvent"

    The reference time instant.

.. py:property:: time_offset2
    :canonical: ansys.stk.core.vgt.ITimeToolEventTimeOffset.time_offset2
    :type: float

    The time offset from the ReferenceTimeInstant. The value is in \'TimeUnit\' dimension.


