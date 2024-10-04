INTERVAL_PRUNE_FILTER_TYPE
==========================

.. py:class:: ansys.stk.core.vgt.INTERVAL_PRUNE_FILTER_TYPE

   IntEnum


.. py:currentmodule:: INTERVAL_PRUNE_FILTER_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported prune filter.

            * - :py:attr:`~FIRST_INTERVALS`
              - Select specified number of first intervals from original list.

            * - :py:attr:`~LAST_INTERVALS`
              - Select specified number of last intervals from original list.

            * - :py:attr:`~INTERVALS`
              - Select intervals which satisfy additional duration condition.

            * - :py:attr:`~GAPS`
              - Select gaps between intervals which satisfy additional duration condition.

            * - :py:attr:`~SATISFACTION_INTERVALS`
              - Satisfaction Intervals selects intervals which satisfy additional condition and duration.

            * - :py:attr:`~RELATIVE_SATISFACTION_INTERVALS`
              - Relative Satisfaction Intervals selects intervals which satisfy additional condition and duration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import INTERVAL_PRUNE_FILTER_TYPE


