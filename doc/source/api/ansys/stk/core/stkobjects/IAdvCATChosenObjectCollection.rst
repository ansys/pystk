IAdvCATChosenObjectCollection
=============================

.. py:class:: IAdvCATChosenObjectCollection

   object
   
   Chosen object collection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns a chosen object in the collection.
            * - :py:meth:`~remove_at`
              - Remove an object from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new chosen object to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdvCATChosenObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObjectCollection.count
    :type: int

    Returns the number of chosen objects in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObjectCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAdvCATChosenObject
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObjectCollection.item

    Given an index, returns a chosen object in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAdvCATChosenObject`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObjectCollection.remove_at

    Remove an object from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObjectCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, object: str) -> IAdvCATChosenObject
    :canonical: ansys.stk.core.stkobjects.IAdvCATChosenObjectCollection.add

    Add a new chosen object to the collection.

    :Parameters:

    **object** : :obj:`~str`

    :Returns:

        :obj:`~IAdvCATChosenObject`

