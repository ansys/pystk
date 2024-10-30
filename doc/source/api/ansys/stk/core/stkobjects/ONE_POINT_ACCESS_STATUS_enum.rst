ONE_POINT_ACCESS_STATUS
=======================

.. py:class:: ansys.stk.core.stkobjects.ONE_POINT_ACCESS_STATUS

   IntEnum


.. py:currentmodule:: ONE_POINT_ACCESS_STATUS

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~MAXIMUM`
              - Constraint value violates max limit of the min-max constraint.

            * - :py:attr:`~MINIMUM`
              - Constraint value violates min limit of the min-max constraint.

            * - :py:attr:`~ZERO`
              - Constraint value violates limit of the zero threshold constraint.

            * - :py:attr:`~LOGICAL`
              - Constraint value violates limit of the logical threshold constraint.

            * - :py:attr:`~INCLUSION_INTERVAL`
              - Constraint value lies outside inclusion intervals.

            * - :py:attr:`~EXCLUSION_INTERVAL`
              - Constraint value lies outside exclusion intervals.

            * - :py:attr:`~OK`
              - Constraint value is within the constraint limits.

            * - :py:attr:`~NOT_COMPUTED`
              - Constraint value is not computed (may occur for constraints that are not evaluated in Fast mode).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ONE_POINT_ACCESS_STATUS


