UserRunway
==========

.. py:class:: ansys.stk.core.stkobjects.aviator.UserRunway

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogRunway`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogWaypoint`

   Class defining the user runway in the Aviator catalog.

.. py:currentmodule:: UserRunway

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.get_terrain_altitude`
              - Set the runway altitude to the terrain altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.copy_site`
              - Copy the site to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.paste_site`
              - Paste the site to the clipboard.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.altitude`
              - Get or set the runway altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.latitude`
              - Get or set the runway latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.longitude`
              - Get or set the runway longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.length`
              - Get or set the length of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.low_end_heading`
              - Get or set the low end heading of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.high_end_heading`
              - Get or set the high end heading of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.UserRunway.is_magnetic`
              - Opt whether to use a magnetic heading for the runway heading.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import UserRunway


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.altitude
    :type: float

    Get or set the runway altitude.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.latitude
    :type: typing.Any

    Get or set the runway latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.longitude
    :type: typing.Any

    Get or set the runway longitude.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.length
    :type: float

    Get or set the length of the runway.

.. py:property:: low_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.low_end_heading
    :type: typing.Any

    Get or set the low end heading of the runway.

.. py:property:: high_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.high_end_heading
    :type: typing.Any

    Get or set the high end heading of the runway.

.. py:property:: is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.is_magnetic
    :type: bool

    Opt whether to use a magnetic heading for the runway heading.


Method detail
-------------

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`



.. py:method:: get_terrain_altitude(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.get_terrain_altitude

    Set the runway altitude to the terrain altitude.

    :Returns:

        :obj:`~float`













.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.UserRunway.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

