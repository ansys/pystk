SiteRunwayFromCatalog
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a runway from catalog site.

.. py:currentmodule:: SiteRunwayFromCatalog

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog.get_catalog_runway`
              - Get the catalog runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog.set_catalog_runway`
              - Set the catalog runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog.get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteRunwayFromCatalog



Method detail
-------------

.. py:method:: get_catalog_runway(self) -> ICatalogRunway
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog.get_catalog_runway

    Get the catalog runway.

    :Returns:

        :obj:`~ICatalogRunway`

.. py:method:: set_catalog_runway(self, value: ICatalogRunway) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog.set_catalog_runway

    Set the catalog runway.

    :Parameters:

        **value** : :obj:`~ICatalogRunway`


    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunwayFromCatalog.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

