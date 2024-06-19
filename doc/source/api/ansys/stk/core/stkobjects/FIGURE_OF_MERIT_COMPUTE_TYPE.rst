FIGURE_OF_MERIT_COMPUTE_TYPE
============================

.. py:class:: FIGURE_OF_MERIT_COMPUTE_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BEST4`
              - Compute the navigation accuracy based on the set of four satellites that yields the minimum GDOP.

            * - :py:attr:`~BEST_N`
              - Compute the navigation accuracy based on the specified number of satellites that yields the minimum GDOP.

            * - :py:attr:`~OVER_DETERMINED`
              - Compute the navigation accuracy based on all of the currently available assets.

            * - :py:attr:`~BEST_FOUR_ACC`
              - Compute the navigation accuracy based on the set of the set of four satellites that yields the minimum geometric uncertainty.

            * - :py:attr:`~BEST_N_ACC`
              - Compute the navigation accuracy based on the set of the specified number of satellites that yields the minimum geometric uncertainty.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_COMPUTE_TYPE


