UserVTOLPoint
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.UserVTOLPoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogVTOLPoint`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogWaypoint`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the user VTOL Point in the Aviator catalog.

.. py:currentmodule:: UserVTOLPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.get_terrain_altitude`
              - Set the VTOL Point altitude to the terrain altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.copy_site`
              - Copy the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.paste_site`
              - Paste the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.altitude`
              - Get or set the VTOL Point altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.latitude`
              - Get or set the VTOL Point latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserVTOLPoint.longitude`
              - Get or set the VTOL Point longitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import UserVTOLPoint


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.altitude
    :type: float

    Get or set the VTOL Point altitude.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.latitude
    :type: typing.Any

    Get or set the VTOL Point latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.longitude
    :type: typing.Any

    Get or set the VTOL Point longitude.


Method detail
-------------



.. py:method:: get_terrain_altitude(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.get_terrain_altitude

    Set the VTOL Point altitude to the terrain altitude.

    :Returns:

        :obj:`~float`





.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.UserVTOLPoint.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

