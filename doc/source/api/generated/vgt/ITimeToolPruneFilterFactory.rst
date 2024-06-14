ITimeToolPruneFilterFactory
===========================

.. py:class:: ITimeToolPruneFilterFactory

   object
   
   The factory creates pruning filters.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and initializes a new prune filter using default configuration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolPruneFilterFactory



Method detail
-------------

.. py:method:: create(self, eFilter:"CRDN_PRUNE_FILTER") -> "ITimeToolPruneFilter"

    Create and initializes a new prune filter using default configuration.

    :Parameters:

    **eFilter** : :obj:`~"CRDN_PRUNE_FILTER"`

    :Returns:

        :obj:`~"ITimeToolPruneFilter"`

