IUserWaypointSource
===================

.. py:class:: IUserWaypointSource

   object
   
   Interface used to access the user waypoints in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_user_waypoint`
              - Get the user waypoint with the given name.
            * - :py:meth:`~add_user_waypoint`
              - Create a new user waypoint with the given name.
            * - :py:meth:`~get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserWaypointSource



Method detail
-------------

.. py:method:: get_user_waypoint(self, name: str) -> IUserWaypoint
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypointSource.get_user_waypoint

    Get the user waypoint with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserWaypoint`

.. py:method:: add_user_waypoint(self, name: str) -> IUserWaypoint
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypointSource.add_user_waypoint

    Create a new user waypoint with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserWaypoint`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypointSource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

