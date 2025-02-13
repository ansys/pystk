PropagatorFunctionCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection

   Propagator Function Collection.

.. py:currentmodule:: PropagatorFunctionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.add`
              - Add a function to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.remove`
              - Remove the specified function from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.remove_all`
              - Remove all functions from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.cut`
              - Copy a propagator function to the clipboard and removes the propagator function from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.paste`
              - Pastes a propagator function from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.insert_copy`
              - Copy a propagator function and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.get_item_by_index`
              - Retrieve a propagator function from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.get_item_by_name`
              - Retrieve a propagator function from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import PropagatorFunctionCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: add(self, result_name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.add

    Add a function to the collection.

    :Parameters:

    **result_name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: item(self, index_or_name: typing.Any) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.remove

    Remove the specified function from the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.remove_all

    Remove all functions from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.cut

    Copy a propagator function to the clipboard and removes the propagator function from the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.paste

    Pastes a propagator function from the clipboard into the list.

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: insert_copy(self, prop_func: IComponentInfo) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.insert_copy

    Copy a propagator function and inserts the copy into the list.

    :Parameters:

    **prop_func** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_index(self, index: int) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.get_item_by_index

    Retrieve a propagator function from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_name(self, name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.PropagatorFunctionCollection.get_item_by_name

    Retrieve a propagator function from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

