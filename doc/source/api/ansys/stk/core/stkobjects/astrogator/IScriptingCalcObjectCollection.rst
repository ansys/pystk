IScriptingCalcObjectCollection
==============================

.. py:class:: IScriptingCalcObjectCollection

   object
   
   The list of calc objects that the script can interact with.

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
              - Add a calculation object to the collection.
            * - :py:meth:`~remove`
              - Remove a calculation object.
            * - :py:meth:`~remove_all`
              - Remove all calculation objects.
            * - :py:meth:`~cut`
              - Copy the calc object into the clipboard and removes the calc object from the list.
            * - :py:meth:`~paste`
              - Pastes the calc object from the clipboard and inserts into the list.
            * - :py:meth:`~insert_copy`
              - Copy the calc object and inserts the copy into the list.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a scripting calc object from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a scripting calc object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


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

.. py:method:: item(self, indexOrName:typing.Any) -> "IScriptingCalcObject"

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IScriptingCalcObject"`

.. py:method:: add(self, componentName:str) -> "IScriptingCalcObject"

    Add a calculation object to the collection.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~"IScriptingCalcObject"`

.. py:method:: remove(self, indexOrName:typing.Any) -> None

    Remove a calculation object.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all calculation objects.

    :Returns:

        :obj:`~None`



.. py:method:: cut(self, indexOrName:typing.Any) -> None

    Copy the calc object into the clipboard and removes the calc object from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> "IScriptingCalcObject"

    Pastes the calc object from the clipboard and inserts into the list.

    :Returns:

        :obj:`~"IScriptingCalcObject"`

.. py:method:: insert_copy(self, calcObj:"IScriptingCalcObject") -> "IScriptingCalcObject"

    Copy the calc object and inserts the copy into the list.

    :Parameters:

    **calcObj** : :obj:`~"IScriptingCalcObject"`

    :Returns:

        :obj:`~"IScriptingCalcObject"`

.. py:method:: get_item_by_index(self, index:int) -> "IScriptingCalcObject"

    Retrieve a scripting calc object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IScriptingCalcObject"`

.. py:method:: get_item_by_name(self, componentName:str) -> "IScriptingCalcObject"

    Retrieve a scripting calc object from the collection by name.

    :Parameters:

    **componentName** : :obj:`~str`

    :Returns:

        :obj:`~"IScriptingCalcObject"`

