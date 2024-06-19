CONSTELLATION_CONSTRAINT_RESTRICTION
====================================

.. py:class:: CONSTELLATION_CONSTRAINT_RESTRICTION

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or not supported criterion.

            * - :py:attr:`~ALL_OF`
              - AND criterion. The constraint is satisfied if all objects in the constellation meet the conditions for chain access.

            * - :py:attr:`~ANY_OF`
              - EITHER/OR criterion. The constraint is satisfied if any one object in the constellation meets the conditions for chain access.

            * - :py:attr:`~AT_LEAST_N`
              - AND/OR criterion. The constraint is satisfied if at least the specified number of objects in the constellation meet the conditions for chain access.

            * - :py:attr:`~EXACTLY_N`
              - ONLY criterion. This constraint is satisfied if the exact specified number of objects in the constellation meet the conditions for chain access.

            * - :py:attr:`~NONE_OF`
              - ONLY criterion. The constraint is satisfied if NO objects in the constellation meet the conditions for chain access.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CONSTELLATION_CONSTRAINT_RESTRICTION


