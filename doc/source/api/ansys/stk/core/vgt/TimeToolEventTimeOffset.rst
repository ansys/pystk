TimeToolEventTimeOffset
=======================

.. py:class:: ansys.stk.core.vgt.TimeToolEventTimeOffset

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEvent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Event at fixed offset from specified reference event.

.. py:currentmodule:: TimeToolEventTimeOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventTimeOffset.reference_time_instant`
              - The reference time instant.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventTimeOffset.time_offset2`
              - The time offset from the ReferenceTimeInstant. The value is in \'TimeUnit\' dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventTimeOffset


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.TimeToolEventTimeOffset.reference_time_instant
    :type: ITimeToolEvent

    The reference time instant.

.. py:property:: time_offset2
    :canonical: ansys.stk.core.vgt.TimeToolEventTimeOffset.time_offset2
    :type: float

    The time offset from the ReferenceTimeInstant. The value is in \'TimeUnit\' dimension.


