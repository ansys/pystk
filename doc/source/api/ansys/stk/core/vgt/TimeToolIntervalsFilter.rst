TimeToolIntervalsFilter
=======================

.. py:class:: ansys.stk.core.vgt.TimeToolIntervalsFilter

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolPruneFilter`

   The filter selects intervals of at least/most certain duration.

.. py:currentmodule:: TimeToolIntervalsFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalsFilter.duration_type`
              - Choose a duration type (at least/at most).
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalsFilter.interval_duration`
              - The interval duration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolIntervalsFilter


Property detail
---------------

.. py:property:: duration_type
    :canonical: ansys.stk.core.vgt.TimeToolIntervalsFilter.duration_type
    :type: INTERVAL_DURATION_TYPE

    Choose a duration type (at least/at most).

.. py:property:: interval_duration
    :canonical: ansys.stk.core.vgt.TimeToolIntervalsFilter.interval_duration
    :type: float

    The interval duration.


