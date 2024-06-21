IPropagatorFunctionCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection

   object
   
   The list of propagator functions - affecting forces that you want to model for orbit propagation.

.. py:currentmodule:: IPropagatorFunctionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.add`
              - Add a function to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.remove`
              - Remove the specified function from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.remove_all`
              - Remove all functions from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.cut`
              - Copy a propagator function to the clipboard and removes the propagator function from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.paste`
              - Pastes a propagator function from the clipboard into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.insert_copy`
              - Copy a propagator function and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.get_item_by_index`
              - Retrieve a propagator function from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.get_item_by_name`
              - Retrieve a propagator function from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPropagatorFunctionCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: add(self, resultName: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.add

    Add a function to the collection.

    :Parameters:

    **resultName** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: item(self, indexOrName: typing.Any) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.remove

    Remove the specified function from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.remove_all

    Remove all functions from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.cut

    Copy a propagator function to the clipboard and removes the propagator function from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.paste

    Pastes a propagator function from the clipboard into the list.

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: insert_copy(self, propFunc: IComponentInfo) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.insert_copy

    Copy a propagator function and inserts the copy into the list.

    :Parameters:

    **propFunc** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_index(self, index: int) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.get_item_by_index

    Retrieve a propagator function from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_name(self, name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.astrogator.IPropagatorFunctionCollection.get_item_by_name

    Retrieve a propagator function from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

