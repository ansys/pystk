TimeToolEventIntervalTimeOffset
===============================

.. py:class:: ansys.stk.core.vgt.TimeToolEventIntervalTimeOffset

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEventInterval`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval defined by shifting specified reference interval by fixed time offset.

.. py:currentmodule:: TimeToolEventIntervalTimeOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalTimeOffset.reference_interval`
              - The reference interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalTimeOffset.time_offset`
              - The time offset value.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventIntervalTimeOffset


Property detail
---------------

.. py:property:: reference_interval
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalTimeOffset.reference_interval
    :type: ITimeToolEventInterval

    The reference interval.

.. py:property:: time_offset
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalTimeOffset.time_offset
    :type: float

    The time offset value.


