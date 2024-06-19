CRITERIA
========

.. py:class:: CRITERIA

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~EQUALS`
              - The test parameter must be equal (within the specified tolerance) to the specified value.

            * - :py:attr:`~GREATER_THAN`
              - The test parameter must be greater than the specified value.

            * - :py:attr:`~GREATER_THAN_MINIMUM`
              - The current value for the calculation object is greater by the specified tolerance than the minimum reached by that object during the segment.

            * - :py:attr:`~LESS_THAN`
              - The test parameter must be less than the specified value.

            * - :py:attr:`~LESS_THAN_MAXIMUM`
              - The current value for the calculation object is less by the specified tolerance than the maximum reached by that object during the segment.

            * - :py:attr:`~NOT_EQUAL_TO`
              - The test parameter must be not equal (within the specified tolerance) to the specified value.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CRITERIA


