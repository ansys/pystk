PrimitiveIndicesOrderHint
=========================

.. py:class:: ansys.stk.core.graphics.PrimitiveIndicesOrderHint

   IntEnum


.. py:currentmodule:: PrimitiveIndicesOrderHint

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NOT_SORTED`
              - The indices passed to SetPartial are not sorted. Therefore, the primitive may sort them to improve performance of writing its geometry to video memory.

            * - :py:attr:`~SORTED_ASCENDING`
              - The indices passed to SetPartial are sorted in ascending order. Therefore, the primitive does not need to sort them. It is recommended to only use SortedAscending if it is easy and efficient for you to provide the indices in ascending order...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PrimitiveIndicesOrderHint


