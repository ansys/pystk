SiteRunway
==========

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteRunway

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a runway site.

.. py:currentmodule:: SiteRunway

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.add_to_catalog`
              - Add the runway to the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.copy_from_catalog`
              - Copy the information from the runway stored in the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.altitude`
              - Get or set the runway altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.latitude`
              - Get or set the runway latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.longitude`
              - Get or set the runway longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.length`
              - Get or set the length of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.altitude_reference`
              - Get or set the altitude reference for the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.low_end_heading`
              - Get or set the low end heading of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.high_end_heading`
              - Get or set the high end heading of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRunway.is_magnetic`
              - Opt whether to use a magnetic heading for the runway heading.



Examples
--------

Configure a runway site

.. code-block:: python

    # SiteRunway runway: Runway object
    # Set the latitude, longitude, and altitude
    runway.latitude = 41
    runway.longitude = 77
    runway.altitude = 5

    # Set the altitude reference
    runway.altitude_reference = AGLMSL.ALTITUDE_MSL

    # Set the heading
    runway.high_end_heading = 195
    # Opt to use true heading
    runway.is_magnetic = False

    # Set the length of the runway
    runway.length = 5

    # Rename the runway
    runway.name = "New User Runway"
    # Add the runway to the catalog to use it for next time
    runway.add_to_catalog(1)


Configure a runway site from a runway in the Aviator catalog

.. code-block:: python

    # SiteRunway runway: Runway object
    # Catalog catalog: Aviator catalog object
    # Get the source of user runways
    userRunways = catalog.runway_category.user_runways
    # Check that the runway exists in the catalog
    if userRunways.contains("New User Runway") is True:
        # If so, get the user runway with the given name
        runwayFromCatalog = userRunways.get_user_runway("New User Runway")
        # Copy the parameters of that runway
        runway.copy_from_catalog(runwayFromCatalog)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteRunway


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.altitude
    :type: float

    Get or set the runway altitude.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.latitude
    :type: typing.Any

    Get or set the runway latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.longitude
    :type: typing.Any

    Get or set the runway longitude.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.length
    :type: float

    Get or set the length of the runway.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.altitude_reference
    :type: AGLMSL

    Get or set the altitude reference for the runway.

.. py:property:: low_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.low_end_heading
    :type: typing.Any

    Get or set the low end heading of the runway.

.. py:property:: high_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.high_end_heading
    :type: typing.Any

    Get or set the high end heading of the runway.

.. py:property:: is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.is_magnetic
    :type: bool

    Opt whether to use a magnetic heading for the runway heading.


Method detail
-------------

















.. py:method:: add_to_catalog(self, overwrite: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.add_to_catalog

    Add the runway to the catalog.

    :Parameters:

    **overwrite** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: copy_from_catalog(self, runway: ICatalogRunway) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.copy_from_catalog

    Copy the information from the runway stored in the catalog.

    :Parameters:

    **runway** : :obj:`~ICatalogRunway`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRunway.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

