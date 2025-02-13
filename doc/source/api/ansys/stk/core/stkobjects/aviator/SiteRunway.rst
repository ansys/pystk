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

