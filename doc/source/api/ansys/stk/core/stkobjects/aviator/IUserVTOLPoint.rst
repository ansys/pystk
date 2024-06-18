IUserVTOLPoint
==============

.. py:class:: IUserVTOLPoint

   object
   
   Interface used to access a user VTOL Point in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_terrain_altitude`
              - Set the VTOL Point altitude to the terrain altitude.
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

            * - :py:meth:`~altitude`
            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`


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

    Set the VTOL Point altitude to the terrain altitude.

    :Returns:

        :obj:`~float`





.. py:method:: copy_site(self) -> None

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

