IObjectLinkCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.IObjectLinkCollection

   object
   
   IAgObjectLinkCollection represents a collection of names of STK objects that are available in the current scenario.

.. py:currentmodule:: IObjectLinkCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.add`
              - Add to the collection a link to an STK object with the given object path and name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.remove`
              - Remove from the collection a link to the STK object with the given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.remove_all`
              - Remove all links from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.remove_name`
              - Remove from the collection a link to an STK object with the given object path and name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.add_object`
              - Add to the collection a link to the given STK object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.remove_object`
              - Remove from the collection a link to the given STK object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.contains`
              - Determine whether the object with the given name is in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.index_of`
              - Search the collection for the specified object and returns a zero-based index of the first occurrence within the collection, if found; otherwise, -1.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IObjectLinkCollection.available_objects`
              - Returns an array of valid objects.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IObjectLinkCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_objects
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.available_objects
    :type: list

    Returns an array of valid objects.


Method detail
-------------



.. py:method:: item(self, index: int) -> IObjectLink
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IObjectLink`

.. py:method:: add(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.add

    Add to the collection a link to an STK object with the given object path and name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.remove

    Remove from the collection a link to the STK object with the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.remove_all

    Remove all links from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_name(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.remove_name

    Remove from the collection a link to an STK object with the given object path and name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: add_object(self, pObject: IStkObject) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.add_object

    Add to the collection a link to the given STK object.

    :Parameters:

    **pObject** : :obj:`~IStkObject`

    :Returns:

        :obj:`~None`

.. py:method:: remove_object(self, pObject: IStkObject) -> None
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.remove_object

    Remove from the collection a link to the given STK object.

    :Parameters:

    **pObject** : :obj:`~IStkObject`

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.contains

    Determine whether the object with the given name is in the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: index_of(self, name: str) -> int
    :canonical: ansys.stk.core.stkobjects.IObjectLinkCollection.index_of

    Search the collection for the specified object and returns a zero-based index of the first occurrence within the collection, if found; otherwise, -1.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~int`

