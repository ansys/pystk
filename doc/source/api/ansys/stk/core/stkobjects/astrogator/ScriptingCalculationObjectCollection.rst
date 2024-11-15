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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection._new_enum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingCalculationObjectCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection._new_enum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: add(self, component_name: str) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.add

    Add a calculation object to the collection.

    :Parameters:

    **component_name** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: remove(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.remove

    Remove a calculation object.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.remove_all

    Remove all calculation objects.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.cut

    Copy the calc object into the clipboard and removes the calc object from the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.paste

    Pastes the calc object from the clipboard and inserts into the list.

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: insert_copy(self, calc_obj: ScriptingCalculationObject) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.insert_copy

    Copy the calc object and inserts the copy into the list.

    :Parameters:

    **calc_obj** : :obj:`~ScriptingCalculationObject`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: get_item_by_index(self, index: int) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.get_item_by_index

    Retrieve a scripting calc object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScriptingCalculationObject`

.. py:method:: get_item_by_name(self, component_name: str) -> ScriptingCalculationObject
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingCalculationObjectCollection.get_item_by_name

    Retrieve a scripting calc object from the collection by name.

    :Parameters:

    **component_name** : :obj:`~str`

    :Returns:

        :obj:`~ScriptingCalculationObject`

