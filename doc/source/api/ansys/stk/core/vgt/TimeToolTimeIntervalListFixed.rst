TimeToolTimeIntervalListFixed
=============================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalListFixed

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Interval list defined by time ordered non-overlapping intervals each explicitly specified by its start and stop times. Stop date/time is required to be at or after start for each interval.

.. py:currentmodule:: TimeToolTimeIntervalListFixed

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFixed.get_intervals`
              - Get intervals with explicitly specified start and stop times from interval list. The method returns a one-dimensional array which elements are 2-tuples of intervals' start/stop times converted according to the current unit preferences.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFixed.set_intervals`
              - Set interval list from intervals with explicitly specified start and stop times. The method takes a one-dimensional array which elements are 2-tuples of intervals' start/stop times converted according to the current unit preferences.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalListFixed



Method detail
-------------

.. py:method:: get_intervals(self) -> list
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFixed.get_intervals

    Get intervals with explicitly specified start and stop times from interval list. The method returns a one-dimensional array which elements are 2-tuples of intervals' start/stop times converted according to the current unit preferences.

    :Returns:

        :obj:`~list`

.. py:method:: set_intervals(self, intervals: list) -> None
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFixed.set_intervals

    Set interval list from intervals with explicitly specified start and stop times. The method takes a one-dimensional array which elements are 2-tuples of intervals' start/stop times converted according to the current unit preferences.

    :Parameters:

    **intervals** : :obj:`~list`

    :Returns:

        :obj:`~None`

