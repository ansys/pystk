ChainConnectionCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.ChainConnectionCollection

   Class defining a collection of Chain connections.

.. py:currentmodule:: ChainConnectionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.add`
              - Add and returns a new connection with the corresponding values.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.add_with_parent_restriction`
              - Add with the option for a parent restriction and returns a new connection with the corresponding values. A Constellation or Subset must be one of the input objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.clear`
              - Clear all connections values from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.item_by_from_to_objects`
              - Given the From and To objects of a connection, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.remove`
              - Remove the connection for the input from-to object pair.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.remove_at`
              - Remove the connection with the input index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConnectionCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainConnectionCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add(self, from_object: ISTKObject, to_object: ISTKObject, min_num_uses: int, max_num_uses: int) -> ChainConnection
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.add

    Add and returns a new connection with the corresponding values.

    :Parameters:

        **from_object** : :obj:`~ISTKObject`

        **to_object** : :obj:`~ISTKObject`

        **min_num_uses** : :obj:`~int`

        **max_num_uses** : :obj:`~int`


    :Returns:

        :obj:`~ChainConnection`

.. py:method:: add_with_parent_restriction(self, from_object: ISTKObject, to_object: ISTKObject, min_num_uses: int, max_num_uses: int, parent_restriction: ChainParentPlatformRestriction) -> ChainConnection
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.add_with_parent_restriction

    Add with the option for a parent restriction and returns a new connection with the corresponding values. A Constellation or Subset must be one of the input objects.

    :Parameters:

        **from_object** : :obj:`~ISTKObject`

        **to_object** : :obj:`~ISTKObject`

        **min_num_uses** : :obj:`~int`

        **max_num_uses** : :obj:`~int`

        **parent_restriction** : :obj:`~ChainParentPlatformRestriction`


    :Returns:

        :obj:`~ChainConnection`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.clear

    Clear all connections values from the collection.

    :Returns:

        :obj:`~None`


.. py:method:: item(self, index: int) -> ChainConnection
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ChainConnection`

.. py:method:: item_by_from_to_objects(self, from_object: ISTKObject, to_object: ISTKObject) -> ChainConnection
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.item_by_from_to_objects

    Given the From and To objects of a connection, returns the element in the collection.

    :Parameters:

        **from_object** : :obj:`~ISTKObject`

        **to_object** : :obj:`~ISTKObject`


    :Returns:

        :obj:`~ChainConnection`

.. py:method:: remove(self, from_object: ISTKObject, to_object: ISTKObject) -> None
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.remove

    Remove the connection for the input from-to object pair.

    :Parameters:

        **from_object** : :obj:`~ISTKObject`

        **to_object** : :obj:`~ISTKObject`


    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ChainConnectionCollection.remove_at

    Remove the connection with the input index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


