UserWaypointSource
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.UserWaypointSource

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining the user waypoint source in the Aviator catalog.

.. py:currentmodule:: UserWaypointSource

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypointSource.get_user_waypoint`
              - Get the user waypoint with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypointSource.add_user_waypoint`
              - Create a new user waypoint with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypointSource.get_as_catalog_source`
              - Get the catalog source interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import UserWaypointSource



Method detail
-------------

.. py:method:: get_user_waypoint(self, name: str) -> UserWaypoint
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypointSource.get_user_waypoint

    Get the user waypoint with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserWaypoint`

.. py:method:: add_user_waypoint(self, name: str) -> UserWaypoint
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypointSource.add_user_waypoint

    Create a new user waypoint with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~UserWaypoint`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypointSource.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

