IScriptingSegmentCollection
===========================

.. py:class:: IScriptingSegmentCollection

   object
   
   The list of object properties that the script can interact with.

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
              - Add an object property to the collection.
            * - :py:meth:`~remove`
              - Remove a object property.
            * - :py:meth:`~remove_all`
              - Remove all object properties.
            * - :py:meth:`~cut`
              - Copy the object property into the clipboard and removes the object property from the list.
            * - :py:meth:`~paste`
              - Pastes the object property from the clipboard and inserts into the list.
            * - :py:meth:`~insert_copy`
              - Copy the object property and inserts the copy into the list.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a scripting segment in the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a scripting segment in the collection by name.

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

    from ansys.stk.core.stkobjects.astrogator import IScriptingSegmentCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.provide_runtime_type_info
    :type: IAgRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IScriptingSegment`

.. py:method:: add(self, componentName: str) -> IScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.add

    Add an object property to the collection.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingSegment`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.remove

    Remove a object property.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.remove_all

    Remove all object properties.

    :Returns:

        :obj:`~None`




.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.cut

    Copy the object property into the clipboard and removes the object property from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.paste

    Pastes the object property from the clipboard and inserts into the list.

    :Returns:

        :obj:`~IScriptingSegment`

.. py:method:: insert_copy(self, objProperty: IScriptingSegment) -> IScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.insert_copy

    Copy the object property and inserts the copy into the list.

    :Parameters:

    **objProperty** : :obj:`~IScriptingSegment`

    :Returns:

        :obj:`~IScriptingSegment`

.. py:method:: get_item_by_index(self, index: int) -> IScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.get_item_by_index

    Retrieve a scripting segment in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScriptingSegment`

.. py:method:: get_item_by_name(self, name: str) -> IScriptingSegment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingSegmentCollection.get_item_by_name

    Retrieve a scripting segment in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingSegment`

