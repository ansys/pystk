ComponentInfoCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.ComponentInfoCollection

   The collection of components and component folders.

.. py:currentmodule:: ComponentInfoCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.item`
              - Allow the user to iterate through the components.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.get_folder`
              - Return the specified folder.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.remove`
              - Remove the named component from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.duplicate_component`
              - Duplicates and adds the component, with the supplied name or index, to the collection and then returns the duplicated component.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.load_component`
              - Load a component from a specified file (full path) into the current folder and then returns the loaded component.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.get_item_by_index`
              - Retrieve component info from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.get_item_by_name`
              - Retrieve component info from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection._new_enum`
              - Enumerates through the components.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.count`
              - Get the number of components available.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.folder_count`
              - Get the number of folders available.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.available_folders`
              - Return an array of Folder names.
            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentInfoCollection.folder_name`
              - Get the current folder's name.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ComponentInfoCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the components.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.count
    :type: int

    Get the number of components available.

.. py:property:: folder_count
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.folder_count
    :type: int

    Get the number of folders available.

.. py:property:: available_folders
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.available_folders
    :type: list

    Return an array of Folder names.

.. py:property:: folder_name
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.folder_name
    :type: str

    Get the current folder's name.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.item

    Allow the user to iterate through the components.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IComponentInfo`



.. py:method:: get_folder(self, index_or_name: typing.Any) -> ComponentInfoCollection
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.get_folder

    Return the specified folder.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~ComponentInfoCollection`




.. py:method:: remove(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.remove

    Remove the named component from the collection.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: duplicate_component(self, index_or_component_name: typing.Any, new_component_name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.duplicate_component

    Duplicates and adds the component, with the supplied name or index, to the collection and then returns the duplicated component.

    :Parameters:

        **index_or_component_name** : :obj:`~typing.Any`

        **new_component_name** : :obj:`~str`


    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: load_component(self, file_name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.load_component

    Load a component from a specified file (full path) into the current folder and then returns the loaded component.

    :Parameters:

        **file_name** : :obj:`~str`


    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_index(self, index: int) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.get_item_by_index

    Retrieve component info from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_name(self, name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.ComponentInfoCollection.get_item_by_name

    Retrieve component info from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IComponentInfo`

