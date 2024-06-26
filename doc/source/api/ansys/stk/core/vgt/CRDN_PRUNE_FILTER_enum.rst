CRDN_PRUNE_FILTER
=================

.. py:class:: ansys.stk.core.vgt.CRDN_PRUNE_FILTER

   IntEnum


.. py:currentmodule:: CRDN_PRUNE_FILTER

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

    from ansys.stk.core.vgt import CRDN_PRUNE_FILTER


