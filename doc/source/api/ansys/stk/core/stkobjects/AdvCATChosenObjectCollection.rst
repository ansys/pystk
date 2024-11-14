AdvCATChosenObjectCollection
============================

.. py:class:: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection

   The chosen object collection.

.. py:currentmodule:: AdvCATChosenObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.item`
              - Given an index, returns a chosen object in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.remove_at`
              - Remove an object from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.add`
              - Add a new chosen object to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.count`
              - Returns the number of chosen objects in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AdvCATChosenObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.count
    :type: int

    Returns the number of chosen objects in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AdvCATChosenObject
    :canonical: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.item

    Given an index, returns a chosen object in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AdvCATChosenObject`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.remove_at

    Remove an object from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, object: str) -> AdvCATChosenObject
    :canonical: ansys.stk.core.stkobjects.AdvCATChosenObjectCollection.add

    Add a new chosen object to the collection.

    :Parameters:

    **object** : :obj:`~str`

    :Returns:

        :obj:`~AdvCATChosenObject`

