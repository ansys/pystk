CRDN_EVENT_ARRAY_TYPE
=====================

.. py:class:: CRDN_EVENT_ARRAY_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported time array types.

            * - :py:attr:`~EXTREMA`
              - Determine time of local minimum and/or maximum of specified scalar calculation.

            * - :py:attr:`~START_STOP_TIMES`
              - Defined by taking start and/or stop times of every interval in specified reference interval list and adding them to array.

            * - :py:attr:`~MERGED`
              - Defined by merging times from two other arrays by creating union of bounding intervals from two constituent arrays.

            * - :py:attr:`~FILTERED`
              - Defined by filtering times from original time array according to specified filtering method.

            * - :py:attr:`~FIXED_STEP`
              - Defined by taking fixed time steps from specified time reference and adding sampled times to array if they fall within specified bounding interval list.

            * - :py:attr:`~CONDITION_CROSSINGS`
              - Time array containing times at which specified condition changes its satisfaction status.

            * - :py:attr:`~SIGNALED`
              - Determine what time array is recorded at target clock location by performing signal transmission of original time array between base and target clock locations.

            * - :py:attr:`~FIXED_TIMES`
              - Time array containing specific times.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_EVENT_ARRAY_TYPE


