CRDN_INTERVAL_SELECTION
=======================

.. py:class:: ansys.stk.core.vgt.CRDN_INTERVAL_SELECTION

   IntEnum


.. py:currentmodule:: CRDN_INTERVAL_SELECTION

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FROM_START`
              - Select an interval by counting a specified number from the first interval.

            * - :py:attr:`~FROM_END`
              - Select an interval by counting a specified number back from the last interval.

            * - :py:attr:`~MAX_DURATION`
              - Select the interval with the largest duration.

            * - :py:attr:`~MIN_DURATION`
              - Select the interval with the smallest duration.

            * - :py:attr:`~MAX_GAP`
              - Select the largest gap between intervals.

            * - :py:attr:`~MIN_GAP`
              - Select the largest gap between intervals.

            * - :py:attr:`~SPAN`
              - Select the interval that is the span of the interval list.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_INTERVAL_SELECTION


