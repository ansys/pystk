Criterion
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.Criterion

   IntEnum


.. py:currentmodule:: Criterion

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CROSS_DECREASING`
              - The Cross Decreasing criterion - the stopping condition is satisfied when the parameter reaches a value equal to the trip value while decreasing.

            * - :py:attr:`~CROSS_EITHER`
              - The Cross Either criterion - the stopping condition is satisfied when either of the above situations occurs.

            * - :py:attr:`~CROSS_INCREASING`
              - The Cross Increasing criterion - the stopping condition is satisfied when the parameter reaches a value equal to the trip value while increasing.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import Criterion


