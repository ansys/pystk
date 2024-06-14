IScriptingParameterCollection
=============================

.. py:class:: IScriptingParameterCollection

   object
   
   The list of parameters that the script can interact with.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~add`
              - Add a parameter to the collection.
            * - :py:meth:`~remove`
              - Remove a parameter.
            * - :py:meth:`~remove_all`
              - Remove all parameters.
            * - :py:meth:`~cut`
              - Copy the parameter into the clipboard and removes the parameter from the list.
            * - :py:meth:`~paste`
              - Pastes the parameter from the clipboard and inserts into the list.
            * - :py:meth:`~insert_copy`
              - Copy the parameter and inserts the copy into the list.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a scripting parameter in the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a scripting parameter in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`
            * - :py:meth:`~provide_runtime_type_info`


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
    :type: "IAgRuntimeTypeInfo"

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName:typing.Any) -> "IScriptingParameter"

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IScriptingParameter"`

.. py:method:: add(self, parameterName:str) -> "IScriptingParameter"

    Add a parameter to the collection.

    :Parameters:

    **parameterName** : :obj:`~str`

    :Returns:

        :obj:`~"IScriptingParameter"`

.. py:method:: remove(self, indexOrName:typing.Any) -> None

    Remove a parameter.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all parameters.

    :Returns:

        :obj:`~None`




.. py:method:: cut(self, indexOrName:typing.Any) -> None

    Copy the parameter into the clipboard and removes the parameter from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> "IScriptingParameter"

    Pastes the parameter from the clipboard and inserts into the list.

    :Returns:

        :obj:`~"IScriptingParameter"`

.. py:method:: insert_copy(self, parameter:"IScriptingParameter") -> "IScriptingParameter"

    Copy the parameter and inserts the copy into the list.

    :Parameters:

    **parameter** : :obj:`~"IScriptingParameter"`

    :Returns:

        :obj:`~"IScriptingParameter"`

.. py:method:: get_item_by_index(self, index:int) -> "IScriptingParameter"

    Retrieve a scripting parameter in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IScriptingParameter"`

.. py:method:: get_item_by_name(self, name:str) -> "IScriptingParameter"

    Retrieve a scripting parameter in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IScriptingParameter"`

