SensorGraphics3DTargetProjectionCollection
==========================================

.. py:class:: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection

   Time Dependent Target Projection List.

.. py:currentmodule:: SensorGraphics3DTargetProjectionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.add`
              - Add a new element to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorGraphics3DTargetProjectionCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> SensorGraphics3DProjectionElement
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~SensorGraphics3DProjectionElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self) -> SensorGraphics3DProjectionElement
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection.add

    Add a new element to the collection.

    :Returns:

        :obj:`~SensorGraphics3DProjectionElement`

