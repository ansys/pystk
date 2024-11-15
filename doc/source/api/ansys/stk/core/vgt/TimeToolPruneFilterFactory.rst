TimeToolPruneFilterFactory
==========================

.. py:class:: ansys.stk.core.vgt.TimeToolPruneFilterFactory

   The factory creates pruning filters.

.. py:currentmodule:: TimeToolPruneFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolPruneFilterFactory.create`
              - Create and initializes a new prune filter using default configuration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolPruneFilterFactory



Method detail
-------------

.. py:method:: create(self, filter: INTERVAL_PRUNE_FILTER_TYPE) -> ITimeToolPruneFilter
    :canonical: ansys.stk.core.vgt.TimeToolPruneFilterFactory.create

    Create and initializes a new prune filter using default configuration.

    :Parameters:

    **filter** : :obj:`~INTERVAL_PRUNE_FILTER_TYPE`

    :Returns:

        :obj:`~ITimeToolPruneFilter`

