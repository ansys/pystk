ITimeToolEventIntervalFixed
===========================

.. py:class:: ITimeToolEventIntervalFixed

   object
   
   Interval defined between two explicitly specified start and stop times. Stop date/time is required to be at or after start.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_interval`
              - Set interval's start and stop times.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalFixed


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFixed.start_time
    :type: typing.Any

    The start time of the interval.

.. py:property:: stop_time
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalFixed.stop_time
    :type: typing.Any

    The stop time of the interval.


Method detail
-------------



.. py:method:: set_interval(self, startEpoch:typing.Any, stopEpoch:typing.Any) -> None

    Set interval's start and stop times.

    :Parameters:

    **startEpoch** : :obj:`~typing.Any`
    **stopEpoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

