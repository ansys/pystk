TargeterGraphCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Targeter Graphs.

.. py:currentmodule:: TargeterGraphCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.add_graph`
              - Add a new targeter graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.remove_graph`
              - Remove a targeter graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.cut`
              - Copy a targeter graph to the clipboard and removes the targeter graph from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.paste`
              - Pastes a targeter graph from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.insert_copy`
              - Copy a targeter graph and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.get_item_by_index`
              - Retrieve a targeter graph from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.get_item_by_name`
              - Retrieve a targeter graph from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TargeterGraphCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~TargeterGraph`



.. py:method:: add_graph(self) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.add_graph

    Add a new targeter graph.

    :Returns:

        :obj:`~TargeterGraph`

.. py:method:: remove_graph(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.remove_graph

    Remove a targeter graph.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.cut

    Copy a targeter graph to the clipboard and removes the targeter graph from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.paste

    Pastes a targeter graph from the clipboard into the list.

    :Returns:

        :obj:`~TargeterGraph`

.. py:method:: insert_copy(self, graph: TargeterGraph) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.insert_copy

    Copy a targeter graph and inserts the copy into the list.

    :Parameters:

    **graph** : :obj:`~TargeterGraph`

    :Returns:

        :obj:`~TargeterGraph`

.. py:method:: get_item_by_index(self, index: int) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.get_item_by_index

    Retrieve a targeter graph from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~TargeterGraph`

.. py:method:: get_item_by_name(self, name: str) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.get_item_by_name

    Retrieve a targeter graph from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~TargeterGraph`

