IStkObjectCollection
====================

.. py:class:: ansys.stk.core.stkobjects.IStkObjectCollection

   Represents a collection of STK objects.

.. py:currentmodule:: IStkObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.item`
              - Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.new`
              - Create an STK object using specified class and instance name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.unload`
              - Remove an STK object using specified object's type and name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.get_elements`
              - Return a collection of objects of specified type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.new_on_central_body`
              - Create an STK object using specified class, instance name and the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.contains`
              - Check whether the collection contains an object with the given type and name.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.import_object`
              - Import object from external file and returns the pointer to the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.copy_object`
              - Copy and paste the specified object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.get_item_by_index`
              - Retrieve an Stk object from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.get_item_by_name`
              - Retrieve an Stk object from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection._new_enum`
              - Returns an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectCollection.supported_child_types`
              - Returns the available objects that can be added to this object.


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

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.

.. py:property:: supported_child_types
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.supported_child_types
    :type: list

    Returns the available objects that can be added to this object.


Method detail
-------------


.. py:method:: item(self, index_or_name: typing.Any) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.item

    Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IStkObject`


.. py:method:: new(self, class_type: STKObjectType, inst_name: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.new

    Create an STK object using specified class and instance name.

    :Parameters:

    **class_type** : :obj:`~STKObjectType`
    **inst_name** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: unload(self, class_type: STKObjectType, inst_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.unload

    Remove an STK object using specified object's type and name.

    :Parameters:

    **class_type** : :obj:`~STKObjectType`
    **inst_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_elements(self, class_type: STKObjectType) -> IStkObjectElementCollection
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.get_elements

    Return a collection of objects of specified type.

    :Parameters:

    **class_type** : :obj:`~STKObjectType`

    :Returns:

        :obj:`~IStkObjectElementCollection`

.. py:method:: new_on_central_body(self, class_type: STKObjectType, inst_name: str, central_body_name: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.new_on_central_body

    Create an STK object using specified class, instance name and the central body.

    :Parameters:

    **class_type** : :obj:`~STKObjectType`
    **inst_name** : :obj:`~str`
    **central_body_name** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`


.. py:method:: contains(self, class_type: STKObjectType, inst_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.contains

    Check whether the collection contains an object with the given type and name.

    :Parameters:

    **class_type** : :obj:`~STKObjectType`
    **inst_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: import_object(self, file_path: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.import_object

    Import object from external file and returns the pointer to the object.

    :Parameters:

    **file_path** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: copy_object(self, object_to_clone: IStkObject, new_object_name: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.IStkObjectCollection.copy_object

    Copy and paste the specified object.

    :Parameters:

    **object_to_clone** : :obj:`~IStkObject`
    **new_object_name** : :obj:`~str`

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

