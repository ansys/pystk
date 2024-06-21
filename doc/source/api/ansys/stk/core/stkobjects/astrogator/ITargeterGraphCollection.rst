ITargeterGraphCollection
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection

   object
   
   The list of User Variables accessed through the Driver.

.. py:currentmodule:: ITargeterGraphCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.add_graph`
              - Add a new targeter graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.remove_graph`
              - Remove a targeter graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.cut`
              - Copy a targeter graph to the clipboard and removes the targeter graph from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.paste`
              - Pastes a targeter graph from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.insert_copy`
              - Copy a targeter graph and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.get_item_by_index`
              - Retrieve a targeter graph from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.get_item_by_name`
              - Retrieve a targeter graph from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ITargeterGraphCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> ITargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITargeterGraph`



.. py:method:: add_graph(self) -> ITargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.add_graph

    Add a new targeter graph.

    :Returns:

        :obj:`~ITargeterGraph`

.. py:method:: remove_graph(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.remove_graph

    Remove a targeter graph.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.cut

    Copy a targeter graph to the clipboard and removes the targeter graph from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> ITargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.paste

    Pastes a targeter graph from the clipboard into the list.

    :Returns:

        :obj:`~ITargeterGraph`

.. py:method:: insert_copy(self, graph: ITargeterGraph) -> ITargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.insert_copy

    Copy a targeter graph and inserts the copy into the list.

    :Parameters:

    **graph** : :obj:`~ITargeterGraph`

    :Returns:

        :obj:`~ITargeterGraph`

.. py:method:: get_item_by_index(self, index: int) -> ITargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.get_item_by_index

    Retrieve a targeter graph from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITargeterGraph`

.. py:method:: get_item_by_name(self, name: str) -> ITargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.ITargeterGraphCollection.get_item_by_name

    Retrieve a targeter graph from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ITargeterGraph`

