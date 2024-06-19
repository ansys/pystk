ICompositePrimitive
===================

.. py:class:: ICompositePrimitive

   object
   
   A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a primitive to the composite.
            * - :py:meth:`~remove`
              - Remove a primitive from the composite.
            * - :py:meth:`~contains`
              - Determine whether the composite contains a primitive.
            * - :py:meth:`~clear`
              - Remove all primitives from the composite.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~translucent_primitives_sort_order`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICompositePrimitive


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ICompositePrimitive.count
    :type: int

    Gets the number of primitives in the composite.

.. py:property:: translucent_primitives_sort_order
    :canonical: ansys.stk.core.graphics.ICompositePrimitive.translucent_primitives_sort_order
    :type: PRIMITIVES_SORT_ORDER

    Gets or sets the sort order for translucent primitives in this composite. This determines a trade-off between rendering speed and quality...

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.ICompositePrimitive._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection. The order of the primitives is not guaranteed to be the order that the primitives were added.


Method detail
-------------




.. py:method:: add(self, primitive: IPrimitive) -> None
    :canonical: ansys.stk.core.graphics.ICompositePrimitive.add

    Add a primitive to the composite.

    :Parameters:

    **primitive** : :obj:`~IPrimitive`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, primitive: IPrimitive) -> None
    :canonical: ansys.stk.core.graphics.ICompositePrimitive.remove

    Remove a primitive from the composite.

    :Parameters:

    **primitive** : :obj:`~IPrimitive`

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, primitive: IPrimitive) -> bool
    :canonical: ansys.stk.core.graphics.ICompositePrimitive.contains

    Determine whether the composite contains a primitive.

    :Parameters:

    **primitive** : :obj:`~IPrimitive`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.ICompositePrimitive.clear

    Remove all primitives from the composite.

    :Returns:

        :obj:`~None`


