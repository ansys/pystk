IScriptingParameterCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection

   object
   
   The list of parameters that the script can interact with.

.. py:currentmodule:: IScriptingParameterCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.add`
              - Add a parameter to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.remove`
              - Remove a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.remove_all`
              - Remove all parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.cut`
              - Copy the parameter into the clipboard and removes the parameter from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.paste`
              - Pastes the parameter from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.insert_copy`
              - Copy the parameter and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.get_item_by_index`
              - Retrieve a scripting parameter in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.get_item_by_name`
              - Retrieve a scripting parameter in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.provide_runtime_type_info`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IScriptingParameterCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IScriptingParameter`

.. py:method:: add(self, parameterName: str) -> IScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.add

    Add a parameter to the collection.

    :Parameters:

    **parameterName** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingParameter`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.remove

    Remove a parameter.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.remove_all

    Remove all parameters.

    :Returns:

        :obj:`~None`




.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.cut

    Copy the parameter into the clipboard and removes the parameter from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.paste

    Pastes the parameter from the clipboard and inserts into the list.

    :Returns:

        :obj:`~IScriptingParameter`

.. py:method:: insert_copy(self, parameter: IScriptingParameter) -> IScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.insert_copy

    Copy the parameter and inserts the copy into the list.

    :Parameters:

    **parameter** : :obj:`~IScriptingParameter`

    :Returns:

        :obj:`~IScriptingParameter`

.. py:method:: get_item_by_index(self, index: int) -> IScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.get_item_by_index

    Retrieve a scripting parameter in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScriptingParameter`

.. py:method:: get_item_by_name(self, name: str) -> IScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameterCollection.get_item_by_name

    Retrieve a scripting parameter in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingParameter`

