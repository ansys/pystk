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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.add_graph`
              - Add a new targeter graph.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.cut`
              - Copy a targeter graph to the clipboard and removes the targeter graph from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.get_item_by_index`
              - Retrieve a targeter graph from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.get_item_by_name`
              - Retrieve a targeter graph from the collection by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.insert_copy`
              - Copy a targeter graph and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.paste`
              - Pastes a targeter graph from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.remove_graph`
              - Remove a targeter graph.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.provide_runtime_type_info`
              - Return the RuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TargeterGraphCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.provide_runtime_type_info
    :type: RuntimeTypeInfo

    Return the RuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: add_graph(self) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.add_graph

    Add a new targeter graph.

    :Returns:

        :obj:`~TargeterGraph`


.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.cut

    Copy a targeter graph to the clipboard and removes the targeter graph from the list.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

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

.. py:method:: insert_copy(self, graph: TargeterGraph) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.insert_copy

    Copy a targeter graph and inserts the copy into the list.

    :Parameters:

        **graph** : :obj:`~TargeterGraph`


    :Returns:

        :obj:`~TargeterGraph`

.. py:method:: item(self, index_or_name: typing.Any) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~TargeterGraph`

.. py:method:: paste(self) -> TargeterGraph
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.paste

    Pastes a targeter graph from the clipboard into the list.

    :Returns:

        :obj:`~TargeterGraph`


.. py:method:: remove_graph(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.TargeterGraphCollection.remove_graph

    Remove a targeter graph.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`


