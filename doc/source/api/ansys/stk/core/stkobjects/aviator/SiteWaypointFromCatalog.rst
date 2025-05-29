SiteWaypointFromCatalog
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a waypoint from catalog site.

.. py:currentmodule:: SiteWaypointFromCatalog

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog.get_catalog_waypoint`
              - Get the catalog waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog.set_catalog_waypoint`
              - Set the catalog waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog.get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteWaypointFromCatalog



Method detail
-------------

.. py:method:: get_catalog_waypoint(self) -> ICatalogWaypoint
    :canonical: ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog.get_catalog_waypoint

    Get the catalog waypoint.

    :Returns:

        :obj:`~ICatalogWaypoint`

.. py:method:: set_catalog_waypoint(self, value: ICatalogWaypoint) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog.set_catalog_waypoint

    Set the catalog waypoint.

    :Parameters:

        **value** : :obj:`~ICatalogWaypoint`


    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteWaypointFromCatalog.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

