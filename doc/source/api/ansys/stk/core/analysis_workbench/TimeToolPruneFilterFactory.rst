TimeToolPruneFilterFactory
==========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolPruneFilterFactory

   The factory creates pruning filters.

.. py:currentmodule:: TimeToolPruneFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolPruneFilterFactory.create`
              - Create and initializes a new prune filter using default configuration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolPruneFilterFactory



Method detail
-------------

.. py:method:: create(self, filter: IntervalPruneFilterType) -> ITimeToolPruneFilter
    :canonical: ansys.stk.core.analysis_workbench.TimeToolPruneFilterFactory.create

    Create and initializes a new prune filter using default configuration.

    :Parameters:

        **filter** : :obj:`~IntervalPruneFilterType`


    :Returns:

        :obj:`~ITimeToolPruneFilter`

