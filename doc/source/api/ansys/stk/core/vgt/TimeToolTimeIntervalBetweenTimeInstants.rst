TimeToolTimeIntervalBetweenTimeInstants
=======================================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalBetweenTimeInstants

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Interval between specified start and stop time instants. If start instant occurs after stop, then interval is undefined.

.. py:currentmodule:: TimeToolTimeIntervalBetweenTimeInstants

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalBetweenTimeInstants.start_time_instant`
              - The start time instant of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalBetweenTimeInstants.stop_time_instant`
              - The stop time instant of the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalBetweenTimeInstants


Property detail
---------------

.. py:property:: start_time_instant
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalBetweenTimeInstants.start_time_instant
    :type: ITimeToolInstant

    The start time instant of the interval.

.. py:property:: stop_time_instant
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalBetweenTimeInstants.stop_time_instant
    :type: ITimeToolInstant

    The stop time instant of the interval.


