KeyValueCollection
==================

.. py:class:: ansys.stk.core.stkobjects.KeyValueCollection

   A collection of keys and values associated with the keys.

.. py:currentmodule:: KeyValueCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.item`
              - Given a key, returns associated element.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.contains`
              - Determine whether the collection contains the specified key.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.remove_all`
              - Remove all elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.remove_key`
              - Remove an element associated with specified key.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.set`
              - Set the value associated with specified key.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.get_read_only`
              - Given a key, returns read-only flag.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.set_read_only`
              - Given a key, sets read-only flag.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection._NewEnum`
              - Returns an enumerator containing the keys in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.KeyValueCollection.keys`
              - Returns an array of keys of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import KeyValueCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator containing the keys in the collection.

.. py:property:: keys
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.keys
    :type: list

    Returns an array of keys of the collection.


Method detail
-------------


.. py:method:: item(self, key: str) -> str
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.item

    Given a key, returns associated element.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~str`


.. py:method:: contains(self, key: str) -> bool
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.contains

    Determine whether the collection contains the specified key.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.remove_all

    Remove all elements.

    :Returns:

        :obj:`~None`

.. py:method:: remove_key(self, key: str) -> bool
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.remove_key

    Remove an element associated with specified key.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: set(self, key: str, value: str) -> None
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.set

    Set the value associated with specified key.

    :Parameters:

    **key** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: get_read_only(self, key: str) -> bool
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.get_read_only

    Given a key, returns read-only flag.

    :Parameters:

    **key** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: set_read_only(self, key: str, isReadOnly: bool) -> None
    :canonical: ansys.stk.core.stkobjects.KeyValueCollection.set_read_only

    Given a key, sets read-only flag.

    :Parameters:

    **key** : :obj:`~str`
    **isReadOnly** : :obj:`~bool`

    :Returns:

        :obj:`~None`

