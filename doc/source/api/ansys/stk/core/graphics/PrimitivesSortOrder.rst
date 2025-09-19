PrimitivesSortOrder
===================

.. py:class:: ansys.stk.core.graphics.PrimitivesSortOrder

   IntEnum


.. py:currentmodule:: PrimitivesSortOrder

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BY_STATE`
              - Primitives are sorted by their internal state before rendering. This provides good performance but can lead to blending artifacts with translucent primitives along the same line of sight.

            * - :py:attr:`~BACK_TO_FRONT`
              - Primitives are sorted in back to front order before rendering. For translucent primitives, this enables correct blending results. This may not perform as well as PrimitivesSortOrderByState since the CPU has to sort the primitives before rendering.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PrimitivesSortOrder


