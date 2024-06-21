IUserVTOLPoint
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint

   object
   
   Interface used to access a user VTOL Point in the Aviator catalog.

.. py:currentmodule:: IUserVTOLPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.get_terrain_altitude`
              - Set the VTOL Point altitude to the terrain altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.copy_site`
              - Copy the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.paste_site`
              - Paste the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.longitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserVTOLPoint


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.altitude
    :type: float

    Gets or sets the VTOL Point altitude.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.latitude
    :type: typing.Any

    Gets or sets the VTOL Point latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.longitude
    :type: typing.Any

    Gets or sets the VTOL Point longitude.


Method detail
-------------



.. py:method:: get_terrain_altitude(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.get_terrain_altitude

    Set the VTOL Point altitude to the terrain altitude.

    :Returns:

        :obj:`~float`





.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IUserVTOLPoint.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

