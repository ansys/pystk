IStkObjectCollection
====================

.. py:class:: IStkObjectCollection

   object
   
   Represents a collection of STK objects.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:meth:`~new`
              - Create an STK object using specified class and instance name.
            * - :py:meth:`~unload`
              - Remove an STK object using specified object's type and name.
            * - :py:meth:`~get_elements`
              - Return a collection of objects of specified type.
            * - :py:meth:`~new_on_central_body`
              - Create an STK object using specified class, instance name and the central body.
            * - :py:meth:`~contains`
              - Check whether the collection contains an object with the given type and name.
            * - :py:meth:`~import_object`
              - Import object from external file and returns the pointer to the object.
            * - :py:meth:`~copy_object`
              - Copy and paste the specified object.
            * - :py:meth:`~get_item_by_index`
              - Retrieve an Stk object from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve an Stk object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~supported_child_types`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.

.. py:property:: supported_child_types
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.supported_child_types
    :type: list

    Returns the available objects that can be added to this object.


Method detail
-------------


.. py:method:: item(self, indexOrName: typing.Any) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.item

    Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IStkObject`


.. py:method:: new(self, eClassType: STK_OBJECT_TYPE, instName: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.new

    Create an STK object using specified class and instance name.

    :Parameters:

    **eClassType** : :obj:`~STK_OBJECT_TYPE`
    **instName** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: unload(self, eClassType: STK_OBJECT_TYPE, instName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.unload

    Remove an STK object using specified object's type and name.

    :Parameters:

    **eClassType** : :obj:`~STK_OBJECT_TYPE`
    **instName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_elements(self, eClassType: STK_OBJECT_TYPE) -> IStkObjectElementCollection
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.get_elements

    Return a collection of objects of specified type.

    :Parameters:

    **eClassType** : :obj:`~STK_OBJECT_TYPE`

    :Returns:

        :obj:`~IStkObjectElementCollection`

.. py:method:: new_on_central_body(self, eClassType: STK_OBJECT_TYPE, instName: str, centralBodyName: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.new_on_central_body

    Create an STK object using specified class, instance name and the central body.

    :Parameters:

    **eClassType** : :obj:`~STK_OBJECT_TYPE`
    **instName** : :obj:`~str`
    **centralBodyName** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`


.. py:method:: contains(self, eClassType: STK_OBJECT_TYPE, instName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.contains

    Check whether the collection contains an object with the given type and name.

    :Parameters:

    **eClassType** : :obj:`~STK_OBJECT_TYPE`
    **instName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: import_object(self, filePath: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.import_object

    Import object from external file and returns the pointer to the object.

    :Parameters:

    **filePath** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: copy_object(self, objectToClone: IStkObject, newObjectName: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.copy_object

    Copy and paste the specified object.

    :Parameters:

    **objectToClone** : :obj:`~IStkObject`
    **newObjectName** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: get_item_by_index(self, index: int) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.get_item_by_index

    Retrieve an Stk object from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: get_item_by_name(self, name: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.get_item_by_name

    Retrieve an Stk object from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

