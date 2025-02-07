UserWaypoint
============

.. py:class:: ansys.stk.core.stkobjects.aviator.UserWaypoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogWaypoint`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the user waypoint in the Aviator catalog.

.. py:currentmodule:: UserWaypoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypoint.copy_site`
              - Copy the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypoint.paste_site`
              - Paste the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypoint.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypoint.latitude`
              - Get or set the waypoint latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserWaypoint.longitude`
              - Get or set the waypoint longitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import UserWaypoint


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypoint.latitude
    :type: typing.Any

    Get or set the waypoint latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypoint.longitude
    :type: typing.Any

    Get or set the waypoint longitude.


Method detail
-------------





.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypoint.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypoint.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.UserWaypoint.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

