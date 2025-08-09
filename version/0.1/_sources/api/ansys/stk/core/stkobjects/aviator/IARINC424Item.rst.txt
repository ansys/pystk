IARINC424Item
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.IARINC424Item

   Interface used to access the options for an ARINC424 Item found in the Aviator catalog.

.. py:currentmodule:: IARINC424Item

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Item.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Item.get_value`
              - Get the value of the field with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Item.get_all_fields`
              - Get all the field names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Item.get_all_fields_and_values`
              - Get all the field names along with the corresponding value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IARINC424Item.copy_site`
              - Copy the site to the clipboard.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IARINC424Item



Method detail
-------------

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Item.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: get_value(self, field_name: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Item.get_value

    Get the value of the field with the given name.

    :Parameters:

        **field_name** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_all_fields(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Item.get_all_fields

    Get all the field names.

    :Returns:

        :obj:`~list`

.. py:method:: get_all_fields_and_values(self) -> list
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Item.get_all_fields_and_values

    Get all the field names along with the corresponding value.

    :Returns:

        :obj:`~list`

.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IARINC424Item.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

