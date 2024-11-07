ScriptingSegmentCollection
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Scripting Segment Collection.

.. py:currentmodule:: ScriptingSegmentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.add`
              - Add an object property to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.remove`
              - Remove a object property.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.remove_all`
              - Remove all object properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.cut`
              - Copy the object property into the clipboard and removes the object property from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.paste`
              - Pastes the object property from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.insert_copy`
              - Copy the object property and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.get_item_by_index`
              - Retrieve a scripting segment in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.get_item_by_name`
              - Retrieve a scripting segment in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingSegmentCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> ScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ScriptingSegment`

.. py:method:: add(self, component_name: str) -> ScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.add

    Add an object property to the collection.

    :Parameters:

    **component_name** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingSegment`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.remove

    Remove a object property.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.remove_all

    Remove all object properties.

    :Returns:

        :obj:`~None`




.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.cut

    Copy the object property into the clipboard and removes the object property from the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> ScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.paste

    Pastes the object property from the clipboard and inserts into the list.

    :Returns:

        :obj:`~ScriptingSegment`

.. py:method:: insert_copy(self, obj_property: ScriptingSegment) -> ScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.insert_copy

    Copy the object property and inserts the copy into the list.

    :Parameters:

    **obj_property** : :obj:`~ScriptingSegment`

    :Returns:

        :obj:`~ScriptingSegment`

.. py:method:: get_item_by_index(self, index: int) -> ScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.get_item_by_index

    Retrieve a scripting segment in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScriptingSegment`

.. py:method:: get_item_by_name(self, name: str) -> ScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingSegmentCollection.get_item_by_name

    Retrieve a scripting segment in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingSegment`

