IPrimitiveManager
=================

.. py:class:: ansys.stk.core.graphics.IPrimitiveManager

   object
   
   The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

.. py:currentmodule:: IPrimitiveManager

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.add`
              - Add a primitive to the manager. Primitives must be added to the manager to be rendered.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.remove`
              - Remove a primitive from the manager. The primitive is no longer rendered unless it is added back into the manager.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.contains`
              - Determine whether the manager contains a primitive.
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.clear`
              - Remove all primitives from the manager.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.count`
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.precision_exponent`
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager.translucent_primitives_sort_order`
            * - :py:attr:`~ansys.stk.core.graphics.IPrimitiveManager._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPrimitiveManager


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.count
    :type: int

    Gets the number of primitives in the manager.

.. py:property:: precision_exponent
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.precision_exponent
    :type: int

    This property is deprecated. This property is no longer in use Gets or sets the exponent used to compute the maximum precision for primitive rendering. For example, a value of -3 indicates the maximum precision of 2^-3, 0.125 m along the x, y, or z axis...

.. py:property:: translucent_primitives_sort_order
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.translucent_primitives_sort_order
    :type: PRIMITIVES_SORT_ORDER

    Gets or sets the sort order for translucent primitives in the primitive manager. This determines a trade-off between rendering speed and quality...

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IPrimitiveManager._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection. The order of the primitives is not guaranteed to be the order that the primitives were added.


Method detail
-------------






.. py:method:: add(self, primitive: IPrimitive) -> None
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.add

    Add a primitive to the manager. Primitives must be added to the manager to be rendered.

    :Parameters:

    **primitive** : :obj:`~IPrimitive`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, primitive: IPrimitive) -> None
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.remove

    Remove a primitive from the manager. The primitive is no longer rendered unless it is added back into the manager.

    :Parameters:

    **primitive** : :obj:`~IPrimitive`

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, primitive: IPrimitive) -> bool
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.contains

    Determine whether the manager contains a primitive.

    :Parameters:

    **primitive** : :obj:`~IPrimitive`

    :Returns:

        :obj:`~bool`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.IPrimitiveManager.clear

    Remove all primitives from the manager.

    :Returns:

        :obj:`~None`


