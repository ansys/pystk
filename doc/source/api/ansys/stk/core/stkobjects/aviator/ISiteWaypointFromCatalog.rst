ISiteWaypointFromCatalog
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog

   object
   
   Interface used to access the options for a waypoint From Catalog site type.

.. py:currentmodule:: ISiteWaypointFromCatalog

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog.get_catalog_waypoint`
              - Get the catalog waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog.set_catalog_waypoint`
              - Set the catalog waypoint.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog.get_as_site`
              - Get the site interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteWaypointFromCatalog



Method detail
-------------

.. py:method:: get_catalog_waypoint(self) -> ICatalogWaypoint
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog.get_catalog_waypoint

    Get the catalog waypoint.

    :Returns:

        :obj:`~ICatalogWaypoint`

.. py:method:: set_catalog_waypoint(self, pVal: ICatalogWaypoint) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog.set_catalog_waypoint

    Set the catalog waypoint.

    :Parameters:

    **pVal** : :obj:`~ICatalogWaypoint`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteWaypointFromCatalog.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

