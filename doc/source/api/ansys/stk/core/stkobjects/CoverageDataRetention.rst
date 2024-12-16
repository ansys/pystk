CoverageDataRetention
=====================

.. py:class:: ansys.stk.core.stkobjects.CoverageDataRetention

   IntEnum


.. py:currentmodule:: CoverageDataRetention

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown data retention method.

            * - :py:attr:`~ALL_DATA`
              - All Data - Retains start and stop times for all accesses in virtual memory.

            * - :py:attr:`~STATIC_DATA_ONLY`
              - Static Only - As access is computed for each point, STK also computes the static value for each figure of merit. Raw access data is then deleted to minimize memory usage.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageDataRetention


