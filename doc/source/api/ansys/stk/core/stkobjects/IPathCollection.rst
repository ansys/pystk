IPathCollection
===============

.. py:class:: IPathCollection

   object
   
   Collection to add and remove paths.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection. Must be the full path to the file.
            * - :py:meth:`~remove`
              - Remove an element from the collection given a filename.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPathCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IPathCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IPathCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.IPathCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IPathCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IPathCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPathCollection.add

    Add a new element to the collection. Must be the full path to the file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.IPathCollection.remove

    Remove an element from the collection given a filename.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

