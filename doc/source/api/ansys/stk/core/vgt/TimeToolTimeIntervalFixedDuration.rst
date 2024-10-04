TimeToolTimeIntervalFixedDuration
=================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

.. py:currentmodule:: TimeToolTimeIntervalFixedDuration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration.reference_time_instant`
              - The reference time instant.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration.start_offset`
              - The start time offset value.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration.stop_offset`
              - The stop time offset value.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalFixedDuration


Property detail
---------------

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration.reference_time_instant
    :type: ITimeToolInstant

    The reference time instant.

.. py:property:: start_offset
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration.start_offset
    :type: float

    The start time offset value.

.. py:property:: stop_offset
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFixedDuration.stop_offset
    :type: float

    The stop time offset value.


