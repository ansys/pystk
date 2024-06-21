IUserVariableDefinitionCollection
=================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection

   object
   
   The list of User Variables accessed through the Driver.

.. py:currentmodule:: IUserVariableDefinitionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.add`
              - Add a user variable to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.remove`
              - Remove a user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.remove_all`
              - Remove all user variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.get_item_by_index`
              - Retrieve a user variable definition in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.get_item_by_name`
              - Retrieve a user variable definition in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IUserVariableDefinitionCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IUserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IUserVariableDefinition`

.. py:method:: add(self, parameterName: str) -> IUserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.add

    Add a user variable to the collection.

    :Parameters:

    **parameterName** : :obj:`~str`

    :Returns:

        :obj:`~IUserVariableDefinition`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.remove

    Remove a user variable.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.remove_all

    Remove all user variables.

    :Returns:

        :obj:`~None`



.. py:method:: get_item_by_index(self, index: int) -> IUserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.get_item_by_index

    Retrieve a user variable definition in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IUserVariableDefinition`

.. py:method:: get_item_by_name(self, name: str) -> IUserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableDefinitionCollection.get_item_by_name

    Retrieve a user variable definition in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserVariableDefinition`

