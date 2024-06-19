IUserRunway
===========

.. py:class:: IUserRunway

   object
   
   Interface used to access a user runway in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.
            * - :py:meth:`~get_terrain_altitude`
              - Set the runway altitude to the terrain altitude.
            * - :py:meth:`~copy_site`
              - Copy the site to the clipboard.
            * - :py:meth:`~paste_site`
              - Paste the site to the clipboard.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude`
            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`
            * - :py:meth:`~length`
            * - :py:meth:`~low_end_heading`
            * - :py:meth:`~high_end_heading`
            * - :py:meth:`~is_magnetic`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IUserRunway


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.altitude
    :type: float

    Gets or sets the runway altitude.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.latitude
    :type: typing.Any

    Gets or sets the runway latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.longitude
    :type: typing.Any

    Gets or sets the runway longitude.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.length
    :type: float

    Gets or sets the length of the runway.

.. py:property:: low_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.low_end_heading
    :type: typing.Any

    Gets or sets the low end heading of the runway.

.. py:property:: high_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.high_end_heading
    :type: typing.Any

    Gets or sets the high end heading of the runway.

.. py:property:: is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.is_magnetic
    :type: bool

    Opt whether to use a magnetic heading for the runway heading.


Method detail
-------------

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`



.. py:method:: get_terrain_altitude(self) -> float
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.get_terrain_altitude

    Set the runway altitude to the terrain altitude.

    :Returns:

        :obj:`~float`













.. py:method:: copy_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.copy_site

    Copy the site to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: paste_site(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IUserRunway.paste_site

    Paste the site to the clipboard.

    :Returns:

        :obj:`~None`

