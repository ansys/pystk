ScriptingCalculationObjectCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection

   Calc Object Collection.

.. py:currentmodule:: ScriptingCalculationObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.add`
              - Add a calculation object to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.remove`
              - Remove a calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.remove_all`
              - Remove all calculation objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.cut`
              - Copy the calc object into the clipboard and removes the calc object from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.paste`
              - Pastes the calc object from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.insert_copy`
              - Copy the calc object and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.get_item_by_index`
              - Retrieve a scripting calc object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.get_item_by_name`
              - Retrieve a scripting calc object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingCalculationObjectCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: add(self, componentName: str) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.add

    Add a calculation object to the collection.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.remove

    Remove a calculation object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.remove_all

    Remove all calculation objects.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.cut

    Copy the calc object into the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.paste

    Pastes the calc object from the clipboard and inserts into the list.

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: insert_copy(self, calcObj: ScriptingCalculationObject) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.insert_copy

    Copy the calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~ScriptingCalculationObject`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: get_item_by_index(self, index: int) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.get_item_by_index

    Retrieve a scripting calc object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: get_item_by_name(self, componentName: str) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.get_item_by_name

    Retrieve a scripting calc object from the collection by name.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingCalculationObject`

