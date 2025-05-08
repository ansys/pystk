EventIntervalType
=================

.. py:class:: ansys.stk.core.analysis_workbench.EventIntervalType

   IntEnum


.. py:currentmodule:: EventIntervalType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported interval types.

            * - :py:attr:`~FIXED`
              - Interval defined between two explicitly specified start and stop times.

            * - :py:attr:`~FIXED_DURATION`
              - Interval of fixed duration specified using start and stop offsets relative to specified reference time instant.

            * - :py:attr:`~BETWEEN_TIME_INSTANTS`
              - Interval between specified start and stop time instants.

            * - :py:attr:`~FROM_INTERVAL_LIST`
              - Interval created from specified interval list by using one of several selection methods.

            * - :py:attr:`~SCALED`
              - Interval defined by scaling original interval using either absolute or relative scale.

            * - :py:attr:`~SIGNALED`
              - Determine an interval recorded at a target clock location by performing signal transmission.

            * - :py:attr:`~TIME_OFFSET`
              - Interval defined by shifting specified reference interval by fixed time offset.

            * - :py:attr:`~SMART_INTERVAL`
              - A smart interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import EventIntervalType


