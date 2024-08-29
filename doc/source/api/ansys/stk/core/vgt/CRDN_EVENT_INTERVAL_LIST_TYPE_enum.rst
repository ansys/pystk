CRDN_EVENT_INTERVAL_LIST_TYPE
=============================

.. py:class:: ansys.stk.core.vgt.CRDN_EVENT_INTERVAL_LIST_TYPE

   IntEnum


.. py:currentmodule:: CRDN_EVENT_INTERVAL_LIST_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported interval list types.

            * - :py:attr:`~MERGED`
              - Interval list created by merging two constituent interval lists using specified logical operation.

            * - :py:attr:`~FILTERED`
              - Defined by filtering intervals from original interval list using specified filtering method.

            * - :py:attr:`~CONDITION`
              - Interval list containing intervals during which specified condition is satisfied (UI type name is Satisfaction).

            * - :py:attr:`~SCALED`
              - Interval List defined by scaling every interval in original interval list using either absolute or relative scale.

            * - :py:attr:`~SIGNALED`
              - Determine what interval list is recorded at target clock location by performing signal transmission of original interval list between base and target clock locations.

            * - :py:attr:`~TIME_OFFSET`
              - Interval List defined by shifting specified reference interval list by fixed time offset.

            * - :py:attr:`~FILE`
              - Interval list loaded from specified interval file.

            * - :py:attr:`~FIXED`
              - Interval list with individual intervals defined between explicitly specified start and stop times.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_EVENT_INTERVAL_LIST_TYPE


