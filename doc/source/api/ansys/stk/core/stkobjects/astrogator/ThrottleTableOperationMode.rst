ThrottleTableOperationMode
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ThrottleTableOperationMode

   IntEnum


.. py:currentmodule:: ThrottleTableOperationMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ENGINE_OPERATION_REG_POLY`
              - Interpolation of engine performance data based on a regression polynomial model.

            * - :py:attr:`~ENGINE_OPERATION_PIECEWISE_LINEAR`
              - Interpolation of engine performance data based on a piecewise linear model.

            * - :py:attr:`~ENGINE_OPERATION_DISCRETE`
              - Discrete engine operation: piecewise constant engine performance as a function of available power.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ThrottleTableOperationMode


