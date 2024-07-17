TimeToolPruneFilterFactory
==========================

.. py:class:: ansys.stk.core.vgt.TimeToolPruneFilterFactory

   Bases: 

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

.. py:method:: create(self, eFilter: CRDN_PRUNE_FILTER) -> ITimeToolPruneFilter
    :canonical: ansys.stk.core.vgt.TimeToolPruneFilterFactory.create

    Create and initializes a new prune filter using default configuration.

    :Parameters:

    **eFilter** : :obj:`~CRDN_PRUNE_FILTER`

    :Returns:

        :obj:`~ITimeToolPruneFilter`

