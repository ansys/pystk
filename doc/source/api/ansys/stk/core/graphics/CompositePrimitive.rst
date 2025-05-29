CompositePrimitive
==================

.. py:class:: ansys.stk.core.graphics.CompositePrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

.. py:currentmodule:: CompositePrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive.add`
              - Add a primitive to the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive.remove`
              - Remove a primitive from the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive.contains`
              - Determine whether the composite contains a primitive.
            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive.clear`
              - Remove all primitives from the composite.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive.count`
              - Get the number of primitives in the composite.
            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive.translucent_primitives_sort_order`
              - Get or set the sort order for translucent primitives in this composite. This determines a trade-off between rendering speed and quality...
            * - :py:attr:`~ansys.stk.core.graphics.CompositePrimitive._new_enum`
              - Return an enumerator that iterates through the collection. The order of the primitives is not guaranteed to be the order that the primitives were added.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CompositePrimitive


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.CompositePrimitive.count
    :type: int

    Get the number of primitives in the composite.

.. py:property:: translucent_primitives_sort_order
    :canonical: ansys.stk.core.graphics.CompositePrimitive.translucent_primitives_sort_order
    :type: PrimitivesSortOrder

    Get or set the sort order for translucent primitives in this composite. This determines a trade-off between rendering speed and quality...

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.CompositePrimitive._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection. The order of the primitives is not guaranteed to be the order that the primitives were added.


Method detail
-------------




.. py:method:: add(self, primitive: IPrimitive) -> None
    :canonical: ansys.stk.core.graphics.CompositePrimitive.add

    Add a primitive to the composite.

    :Parameters:

        **primitive** : :obj:`~IPrimitive`


    :Returns:

        :obj:`~None`

.. py:method:: remove(self, primitive: IPrimitive) -> None
    :canonical: ansys.stk.core.graphics.CompositePrimitive.remove

    Remove a primitive from the composite.

    :Parameters:

        **primitive** : :obj:`~IPrimitive`


    :Returns:

        :obj:`~None`

.. py:method:: contains(self, primitive: IPrimitive) -> bool
    :canonical: ansys.stk.core.graphics.CompositePrimitive.contains

    Determine whether the composite contains a primitive.

    :Parameters:

        **primitive** : :obj:`~IPrimitive`


    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.CompositePrimitive.clear

    Remove all primitives from the composite.

    :Returns:

        :obj:`~None`


