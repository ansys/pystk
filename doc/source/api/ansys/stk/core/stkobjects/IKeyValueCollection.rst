IKeyValueCollection
===================

.. py:class:: IKeyValueCollection

   object
   
   A collection of keys and values associated with the keys.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given a key, returns associated element.
            * - :py:meth:`~contains`
              - Determine whether the collection contains the specified key.
            * - :py:meth:`~remove_all`
              - Remove all elements.
            * - :py:meth:`~remove_key`
              - Remove an element associated with specified key.
            * - :py:meth:`~set`
              - Set the value associated with specified key.
            * - :py:meth:`~get_read_only`
              - Given a key, returns read-only flag.
            * - :py:meth:`~set_read_only`
              - Given a key, sets read-only flag.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~keys`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IKeyValueCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator containing the keys in the collection.

.. py:property:: keys
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.keys
    :type: list

    Returns an array of keys of the collection.


Method detail
-------------


.. py:method:: item(self, key: str) -> str
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.item

    Given a key, returns associated element.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~str`


.. py:method:: contains(self, key: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.contains

    Determine whether the collection contains the specified key.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.remove_all

    Remove all elements.

    :Returns:

        :obj:`~None`

.. py:method:: remove_key(self, key: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.remove_key

    Remove an element associated with specified key.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: set(self, key: str, value: str) -> None
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.set

    Set the value associated with specified key.

    :Parameters:

    **key** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: get_read_only(self, key: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.get_read_only

    Given a key, returns read-only flag.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: set_read_only(self, key: str, isReadOnly: bool) -> None
    :canonical: ansys.stk.core.stkobjects.IKeyValueCollection.set_read_only

    Given a key, sets read-only flag.

    :Parameters:

    **key** : :obj:`~str`
    **isReadOnly** : :obj:`~bool`

    :Returns:

        :obj:`~None`

