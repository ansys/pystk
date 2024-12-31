CoverageAssetGrouping
=====================

.. py:class:: ansys.stk.core.stkobjects.CoverageAssetGrouping

   IntEnum


.. py:currentmodule:: CoverageAssetGrouping

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~SEPARATE`
              - Assets in a chain are treated separately for access purposes.

            * - :py:attr:`~GROUPED`
              - Assets in a chain are treated as a group, and are considered to be a single object for the purpose of counting the number of assets providing simultaneous coverage.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageAssetGrouping


