ISiteVTOLPointFromCatalog
=========================

.. py:class:: ISiteVTOLPointFromCatalog

   object
   
   Interface used to access the options for a VTOL Point From Catalog site type.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_catalog_vtol_point`
              - Get the catalog VTOL point.
            * - :py:meth:`~set_catalog_vtol_point`
              - Set the catalog VTOL point.
            * - :py:meth:`~get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteVTOLPointFromCatalog



Method detail
-------------

.. py:method:: get_catalog_vtol_point(self) -> ICatalogVTOLPoint
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPointFromCatalog.get_catalog_vtol_point

    Get the catalog VTOL point.

    :Returns:

        :obj:`~ICatalogVTOLPoint`

.. py:method:: set_catalog_vtol_point(self, pVal: ICatalogVTOLPoint) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPointFromCatalog.set_catalog_vtol_point

    Set the catalog VTOL point.

    :Parameters:

    **pVal** : :obj:`~ICatalogVTOLPoint`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPointFromCatalog.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

