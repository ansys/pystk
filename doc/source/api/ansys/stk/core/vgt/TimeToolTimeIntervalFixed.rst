TimeToolTimeIntervalFixed
=========================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalFixed

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeInterval`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

.. py:currentmodule:: TimeToolTimeIntervalFixed

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixed.set_interval`
              - Set interval's start and stop times.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixed.start_time`
              - The start time of the interval.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalFixed.stop_time`
              - The stop time of the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalFixed


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFixed.start_time
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop_time
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFixed.stop_time
    :type: typing.Any

    The stop time of the interval.


Method detail
-------------



.. py:method:: set_interval(self, startEpoch: typing.Any, stopEpoch: typing.Any) -> None
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalFixed.set_interval

    Set interval's start and stop times.

    :Parameters:

    **startEpoch** : :obj:`~typing.Any`
    **stopEpoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

