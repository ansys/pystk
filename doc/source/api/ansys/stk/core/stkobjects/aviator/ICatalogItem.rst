ICatalogItem
============

.. py:class:: ansys.stk.core.stkobjects.aviator.ICatalogItem

   Interface used to access the options for a Catalog Item in the Aviator Catalog. Use this interface to Create, Remove, Duplicate, or Rename items in the catalog.

.. py:currentmodule:: ICatalogItem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.duplicate`
              - Duplicates the catalog item.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.remove`
              - Remove the catalog item.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.save`
              - Save the catalog item.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.get_child_item_by_name`
              - Get the child of the catalog item with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.add_default_child`
              - Create a new child with the given name and default type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.add_child_of_type`
              - Create a new child with the given name and specified type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.contains_child_item`
              - Get whether the catalog item is contains the given child item.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.name`
              - Gets or sets the name of the catalog item.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.description`
              - Get the description of the catalog item.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.is_read_only`
              - Get whether the catalog item is read only.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.child_names`
              - Get the child names of the catalog item.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICatalogItem.child_types`
              - Get the child types.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICatalogItem


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.name
    :type: str

    Gets or sets the name of the catalog item.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.description
    :type: str

    Get the description of the catalog item.

.. py:property:: is_read_only
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.is_read_only
    :type: bool

    Get whether the catalog item is read only.

.. py:property:: child_names
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.child_names
    :type: list

    Get the child names of the catalog item.

.. py:property:: child_types
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.child_types
    :type: list

    Get the child types.


Method detail
-------------




.. py:method:: duplicate(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.duplicate

    Duplicates the catalog item.

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: remove(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.remove

    Remove the catalog item.

    :Returns:

        :obj:`~None`

.. py:method:: save(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.save

    Save the catalog item.

    :Returns:

        :obj:`~None`



.. py:method:: get_child_item_by_name(self, child_name: str) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.get_child_item_by_name

    Get the child of the catalog item with the given name.

    :Parameters:

    **child_name** : :obj:`~str`

    :Returns:

        :obj:`~ICatalogItem`


.. py:method:: add_default_child(self, child_name: str) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.add_default_child

    Create a new child with the given name and default type.

    :Parameters:

    **child_name** : :obj:`~str`

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: add_child_of_type(self, child_type: str, child_name: str) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.add_child_of_type

    Create a new child with the given name and specified type.

    :Parameters:

    **child_type** : :obj:`~str`
    **child_name** : :obj:`~str`

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: contains_child_item(self, child_item: str) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.ICatalogItem.contains_child_item

    Get whether the catalog item is contains the given child item.

    :Parameters:

    **child_item** : :obj:`~str`

    :Returns:

        :obj:`~bool`

