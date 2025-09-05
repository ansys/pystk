AircraftVTOL
============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftVTOL

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the VTOL category of an Aviator aircraft.

.. py:currentmodule:: AircraftVTOL

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftVTOL.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftVTOL.get_vtol_by_name`
              - Get the VTOL model with the given name.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftVTOL



Method detail
-------------

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftVTOL.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

.. py:method:: get_vtol_by_name(self, name: str) -> AircraftVTOLModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftVTOL.get_vtol_by_name

    Get the VTOL model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftVTOLModel`

