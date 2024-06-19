IUserWaypoint
=============

.. py:class:: IUserWaypoint

   object
   
   Interface used to access a user waypoint in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~copy_site`
              - Copy the site to the clipboard.
            * - :py:meth:`~paste_site`
              - Paste the site to the clipboard.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserWaypoint


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypoint.latitude
    :type: typing.Any

    Gets or sets the waypoint latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypoint.longitude
    :type: typing.Any

    Gets or sets the waypoint longitude.


Method detail
-------------





.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypoint.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypoint.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IUserWaypoint.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

