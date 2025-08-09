ScriptingParameterCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Scripting Parameter Collection.

.. py:currentmodule:: ScriptingParameterCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.add`
              - Add a parameter to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.cut`
              - Copy the parameter into the clipboard and removes the parameter from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.get_item_by_index`
              - Retrieve a scripting parameter in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.get_item_by_name`
              - Retrieve a scripting parameter in the collection by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.insert_copy`
              - Copy the parameter and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.paste`
              - Pastes the parameter from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.remove`
              - Remove a parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.remove_all`
              - Remove all parameters.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.provide_runtime_type_info`
              - Return the RuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingParameterCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.provide_runtime_type_info
    :type: RuntimeTypeInfo

    Return the RuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: add(self, parameter_name: str) -> ScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.add

    Add a parameter to the collection.

    :Parameters:

        **parameter_name** : :obj:`~str`


    :Returns:

        :obj:`~ScriptingParameter`


.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.cut

    Copy the parameter into the clipboard and removes the parameter from the list.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_index(self, index: int) -> ScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.get_item_by_index

    Retrieve a scripting parameter in the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ScriptingParameter`

.. py:method:: get_item_by_name(self, name: str) -> ScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.get_item_by_name

    Retrieve a scripting parameter in the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ScriptingParameter`

.. py:method:: insert_copy(self, parameter: ScriptingParameter) -> ScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.insert_copy

    Copy the parameter and inserts the copy into the list.

    :Parameters:

        **parameter** : :obj:`~ScriptingParameter`


    :Returns:

        :obj:`~ScriptingParameter`

.. py:method:: item(self, index_or_name: typing.Any) -> ScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ScriptingParameter`

.. py:method:: paste(self) -> ScriptingParameter
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.paste

    Pastes the parameter from the clipboard and inserts into the list.

    :Returns:

        :obj:`~ScriptingParameter`


.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.remove

    Remove a parameter.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameterCollection.remove_all

    Remove all parameters.

    :Returns:

        :obj:`~None`


