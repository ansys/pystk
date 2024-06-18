ICalcObjectCollection
=====================

.. py:class:: ICalcObjectCollection

   object
   
   Collection of calculation objects.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~add`
              - Add a calc object to the collection.
            * - :py:meth:`~item`
              - Return a calc object.
            * - :py:meth:`~remove`
              - Remove a calc object from the collection.
            * - :py:meth:`~cut`
              - Copy a calc object to the clipboard and removes the calc object from the list.
            * - :py:meth:`~paste`
              - Pastes a calc object from the clipboard into the list.
            * - :py:meth:`~insert_copy`
              - Copy a calc object and inserts the copy into the list.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a calc object found by the index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a calc object found by the name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICalcObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ICalcObjectCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, name:str) -> "IComponentInfo"

    Add a calc object to the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IComponentInfo"`

.. py:method:: item(self, indexOrName:typing.Any) -> "IComponentInfo"

    Return a calc object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IComponentInfo"`

.. py:method:: remove(self, indexOrName:typing.Any) -> None

    Remove a calc object from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName:typing.Any) -> None

    Copy a calc object to the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> "IComponentInfo"

    Pastes a calc object from the clipboard into the list.

    :Returns:

        :obj:`~"IComponentInfo"`

.. py:method:: insert_copy(self, calcObj:"IComponentInfo") -> "IComponentInfo"

    Copy a calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~"IComponentInfo"`

    :Returns:

        :obj:`~"IComponentInfo"`

.. py:method:: get_item_by_index(self, index:int) -> "IComponentInfo"

    Retrieve a calc object found by the index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IComponentInfo"`

.. py:method:: get_item_by_name(self, name:str) -> "IComponentInfo"

    Retrieve a calc object found by the name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IComponentInfo"`

