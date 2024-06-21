IScriptingParameterEnumerationChoiceCollection
==============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection

   object
   
   The list of enumeration choices available when parameter type is Enumeration.

.. py:currentmodule:: IScriptingParameterEnumerationChoiceCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.add`
              - Add an enumeration choice to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.remove`
              - Remove an enumeration choice.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.cut`
              - Copy the enumeration choice into the clipboard and removes the enumeration choice from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.paste`
              - Pastes the enumeration choice from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.insert_copy`
              - Copy the enumeration choice and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.get_item_by_index`
              - Retrieve a scripting parameter enumeration choice in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.get_item_by_name`
              - Retrieve a scripting parameter enumeration choice in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IScriptingParameterEnumerationChoiceCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IScriptingParameterEnumerationChoice`

.. py:method:: add(self, choiceName: str) -> IScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.add

    Add an enumeration choice to the collection.

    :Parameters:

    **choiceName** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingParameterEnumerationChoice`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.remove

    Remove an enumeration choice.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.cut

    Copy the enumeration choice into the clipboard and removes the enumeration choice from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.paste

    Pastes the enumeration choice from the clipboard and inserts into the list.

    :Returns:

        :obj:`~IScriptingParameterEnumerationChoice`

.. py:method:: insert_copy(self, choice: IScriptingParameterEnumerationChoice) -> IScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.insert_copy

    Copy the enumeration choice and inserts the copy into the list.

    :Parameters:

    **choice** : :obj:`~IScriptingParameterEnumerationChoice`

    :Returns:

        :obj:`~IScriptingParameterEnumerationChoice`


.. py:method:: get_item_by_index(self, index: int) -> IScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.get_item_by_index

    Retrieve a scripting parameter enumeration choice in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScriptingParameterEnumerationChoice`

.. py:method:: get_item_by_name(self, name: str) -> IScriptingParameterEnumerationChoice
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterEnumerationChoiceCollection.get_item_by_name

    Retrieve a scripting parameter enumeration choice in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingParameterEnumerationChoice`

