ScriptingCalcObjectCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection

   Calc Object Collection.

.. py:currentmodule:: ScriptingCalcObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.add`
              - Add a calculation object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.remove`
              - Remove a calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.remove_all`
              - Remove all calculation objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.cut`
              - Copy the calc object into the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.paste`
              - Pastes the calc object from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.insert_copy`
              - Copy the calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.get_item_by_index`
              - Retrieve a scripting calc object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.get_item_by_name`
              - Retrieve a scripting calc object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingCalcObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> ScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ScriptingCalcObject`

.. py:method:: add(self, componentName: str) -> ScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.add

    Add a calculation object to the collection.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingCalcObject`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.remove

    Remove a calculation object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.remove_all

    Remove all calculation objects.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.cut

    Copy the calc object into the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> ScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.paste

    Pastes the calc object from the clipboard and inserts into the list.

    :Returns:

        :obj:`~ScriptingCalcObject`

.. py:method:: insert_copy(self, calcObj: ScriptingCalcObject) -> ScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.insert_copy

    Copy the calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~ScriptingCalcObject`

    :Returns:

        :obj:`~ScriptingCalcObject`

.. py:method:: get_item_by_index(self, index: int) -> ScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.get_item_by_index

    Retrieve a scripting calc object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScriptingCalcObject`

.. py:method:: get_item_by_name(self, componentName: str) -> ScriptingCalcObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalcObjectCollection.get_item_by_name

    Retrieve a scripting calc object from the collection by name.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingCalcObject`

