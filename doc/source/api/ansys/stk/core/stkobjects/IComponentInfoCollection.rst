IComponentInfoCollection
========================

.. py:class:: ansys.stk.core.stkobjects.IComponentInfoCollection

   object
   
   The collection of components and component folders.

.. py:currentmodule:: IComponentInfoCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.item`
              - Allow the user to iterate through the components.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.get_folder`
              - Return the specified folder.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.remove`
              - Remove the named component from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.duplicate_component`
              - Duplicates and adds the component, with the supplied name or index, to the collection and then returns the duplicated component.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.load_component`
              - Load a component from a specified file (full path) into the current folder and then returns the loaded component.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.get_item_by_index`
              - Retrieve component info from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.get_item_by_name`
              - Retrieve component info from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.folder_count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.available_folders`
            * - :py:attr:`~ansys.stk.core.stkobjects.IComponentInfoCollection.folder_name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IComponentInfoCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the components.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.count
    :type: int

    Get the number of components available.

.. py:property:: folder_count
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.folder_count
    :type: int

    Get the number of folders available.

.. py:property:: available_folders
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.available_folders
    :type: list

    Returns an array of Folder names.

.. py:property:: folder_name
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.folder_name
    :type: str

    Get the current folder's name.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.item

    Allow the user to iterate through the components.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentInfo`



.. py:method:: get_folder(self, indexOrName: typing.Any) -> IComponentInfoCollection
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.get_folder

    Return the specified folder.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IComponentInfoCollection`




.. py:method:: remove(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.remove

    Remove the named component from the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: duplicate_component(self, indexOrComponentName: typing.Any, newComponentName: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.duplicate_component

    Duplicates and adds the component, with the supplied name or index, to the collection and then returns the duplicated component.

    :Parameters:

    **indexOrComponentName** : :obj:`~typing.Any`
    **newComponentName** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: load_component(self, fileName: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.load_component

    Load a component from a specified file (full path) into the current folder and then returns the loaded component.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_index(self, index: int) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.get_item_by_index

    Retrieve component info from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IComponentInfo`

.. py:method:: get_item_by_name(self, name: str) -> IComponentInfo
    :canonical: ansys.stk.core.stkobjects.IComponentInfoCollection.get_item_by_name

    Retrieve component info from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IComponentInfo`

