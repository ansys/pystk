IARINC424Item
=============

.. py:class:: IARINC424Item

   object
   
   Interface used to access the options for an ARINC424 Item found in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:meth:`~get_value`
              - Get the value of the field with the given name.
            * - :py:meth:`~get_all_fields`
              - Get all the field names.
            * - :py:meth:`~get_all_fields_and_values`
              - Get all the field names along with the corresponding value.
            * - :py:meth:`~copy_site`
              - Copy the site to the clipboard.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IARINC424Item



Method detail
-------------

.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

.. py:method:: get_value(self, fieldName:str) -> typing.Any

    Get the value of the field with the given name.

    :Parameters:

    **fieldName** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_all_fields(self) -> list

    Get all the field names.

    :Returns:

        :obj:`~list`

.. py:method:: get_all_fields_and_values(self) -> list

    Get all the field names along with the corresponding value.

    :Returns:

        :obj:`~list`

.. py:method:: copy_site(self) -> None

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

