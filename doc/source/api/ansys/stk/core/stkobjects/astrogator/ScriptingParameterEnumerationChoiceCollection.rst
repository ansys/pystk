ScriptingParameterEnumerationChoiceCollection
=============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Scripting Parameter Enumeration Choice Collection.

.. py:currentmodule:: ScriptingParameterEnumerationChoiceCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.add`
              - Add an enumeration choice to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.remove`
              - Remove an enumeration choice.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.cut`
              - Copy the enumeration choice into the clipboard and removes the enumeration choice from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.paste`
              - Pastes the enumeration choice from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.insert_copy`
              - Copy the enumeration choice and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.get_item_by_index`
              - Retrieve a scripting parameter enumeration choice in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.get_item_by_name`
              - Retrieve a scripting parameter enumeration choice in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.provide_runtime_type_info`
              - Return the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingParameterEnumerationChoiceCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Return the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> ScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ScriptingParameterEnumerationChoice`

.. py:method:: add(self, choice_name: str) -> ScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.add

    Add an enumeration choice to the collection.

    :Parameters:

    **choice_name** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingParameterEnumerationChoice`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.remove

    Remove an enumeration choice.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.cut

    Copy the enumeration choice into the clipboard and removes the enumeration choice from the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> ScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.paste

    Pastes the enumeration choice from the clipboard and inserts into the list.

    :Returns:

        :obj:`~ScriptingParameterEnumerationChoice`

.. py:method:: insert_copy(self, choice: ScriptingParameterEnumerationChoice) -> ScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.insert_copy

    Copy the enumeration choice and inserts the copy into the list.

    :Parameters:

    **choice** : :obj:`~ScriptingParameterEnumerationChoice`

    :Returns:

        :obj:`~ScriptingParameterEnumerationChoice`


.. py:method:: get_item_by_index(self, index: int) -> ScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.get_item_by_index

    Retrieve a scripting parameter enumeration choice in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScriptingParameterEnumerationChoice`

.. py:method:: get_item_by_name(self, name: str) -> ScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterEnumerationChoiceCollection.get_item_by_name

    Retrieve a scripting parameter enumeration choice in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingParameterEnumerationChoice`

