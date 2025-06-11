UserVariableDefinitionCollection
================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection

   User Variable Definition Collection.

.. py:currentmodule:: UserVariableDefinitionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.add`
              - Add a user variable to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.remove`
              - Remove a user variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.remove_all`
              - Remove all user variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.get_item_by_index`
              - Retrieve a user variable definition in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.get_item_by_name`
              - Retrieve a user variable definition in the collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UserVariableDefinitionCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> UserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~UserVariableDefinition`

.. py:method:: add(self, parameter_name: str) -> UserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.add

    Add a user variable to the collection.

    :Parameters:

        **parameter_name** : :obj:`~str`


    :Returns:

        :obj:`~UserVariableDefinition`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.remove

    Remove a user variable.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.remove_all

    Remove all user variables.

    :Returns:

        :obj:`~None`



.. py:method:: get_item_by_index(self, index: int) -> UserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.get_item_by_index

    Retrieve a user variable definition in the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~UserVariableDefinition`

.. py:method:: get_item_by_name(self, name: str) -> UserVariableDefinition
    :canonical: ansys.stk.core.stkobjects.astrogator.UserVariableDefinitionCollection.get_item_by_name

    Retrieve a user variable definition in the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserVariableDefinition`

