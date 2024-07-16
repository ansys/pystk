TimeToolEventIntervalBetweenTimeInstants
========================================

.. py:class:: ansys.stk.core.vgt.TimeToolEventIntervalBetweenTimeInstants

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEventInterval`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

.. py:currentmodule:: TimeToolEventIntervalBetweenTimeInstants

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalBetweenTimeInstants.start_time_instant`
              - The start time instant of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventIntervalBetweenTimeInstants.stop_time_instant`
              - The stop time instant of the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventIntervalBetweenTimeInstants


Property detail
---------------

.. py:property:: start_time_instant
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalBetweenTimeInstants.start_time_instant
    :type: ITimeToolEvent

    The start time instant of the interval.

.. py:property:: stop_time_instant
    :canonical: ansys.stk.core.vgt.TimeToolEventIntervalBetweenTimeInstants.stop_time_instant
    :type: ITimeToolEvent

    The stop time instant of the interval.


