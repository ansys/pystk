IScriptingCalcObjectCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection

   object
   
   The list of calc objects that the script can interact with.

.. py:currentmodule:: IScriptingCalcObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.add`
              - Add a calculation object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.remove`
              - Remove a calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.remove_all`
              - Remove all calculation objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.cut`
              - Copy the calc object into the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.paste`
              - Pastes the calc object from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.insert_copy`
              - Copy the calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.get_item_by_index`
              - Retrieve a scripting calc object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.get_item_by_name`
              - Retrieve a scripting calc object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IScriptingCalcObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IScriptingCalcObject`

.. py:method:: add(self, componentName: str) -> IScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.add

    Add a calculation object to the collection.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingCalcObject`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.remove

    Remove a calculation object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.remove_all

    Remove all calculation objects.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.cut

    Copy the calc object into the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> IScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.paste

    Pastes the calc object from the clipboard and inserts into the list.

    :Returns:

        :obj:`~IScriptingCalcObject`

.. py:method:: insert_copy(self, calcObj: IScriptingCalcObject) -> IScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.insert_copy

    Copy the calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~IScriptingCalcObject`

    :Returns:

        :obj:`~IScriptingCalcObject`

.. py:method:: get_item_by_index(self, index: int) -> IScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.get_item_by_index

    Retrieve a scripting calc object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScriptingCalcObject`

.. py:method:: get_item_by_name(self, componentName: str) -> IScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingCalcObjectCollection.get_item_by_name

    Retrieve a scripting calc object from the collection by name.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~IScriptingCalcObject`

