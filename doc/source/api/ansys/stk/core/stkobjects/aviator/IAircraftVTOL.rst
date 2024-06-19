IAircraftVTOL
=============

.. py:class:: IAircraftVTOL

   object
   
   Interface used to access the VTOL options for an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_vtol_by_name`
              - Get the VTOL model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftVTOL



Method detail
-------------

.. py:method:: get_vtol_by_name(self, name: str) -> IAircraftVTOLModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOL.get_vtol_by_name

    Get the VTOL model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftVTOLModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftVTOL.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

