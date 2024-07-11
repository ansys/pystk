ISiteRunway
===========

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteRunway

   object
   
   Interface used to access the options for a Runway site type.

.. py:currentmodule:: ISiteRunway

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.add_to_catalog`
              - Add the runway to the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.copy_from_catalog`
              - Copy the information from the runway stored in the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.altitude`
              - Gets or sets the runway altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.latitude`
              - Gets or sets the runway latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.longitude`
              - Gets or sets the runway longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.length`
              - Gets or sets the length of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.altitude_reference`
              - Gets or sets the altitude reference for the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.low_end_heading`
              - Gets or sets the low end heading of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.high_end_heading`
              - Gets or sets the high end heading of the runway.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteRunway.is_magnetic`
              - Opt whether to use a magnetic heading for the runway heading.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteRunway


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.altitude
    :type: float

    Gets or sets the runway altitude.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.latitude
    :type: typing.Any

    Gets or sets the runway latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.longitude
    :type: typing.Any

    Gets or sets the runway longitude.

.. py:property:: length
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.length
    :type: float

    Gets or sets the length of the runway.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.altitude_reference
    :type: AGL_MSL

    Gets or sets the altitude reference for the runway.

.. py:property:: low_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.low_end_heading
    :type: typing.Any

    Gets or sets the low end heading of the runway.

.. py:property:: high_end_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.high_end_heading
    :type: typing.Any

    Gets or sets the high end heading of the runway.

.. py:property:: is_magnetic
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.is_magnetic
    :type: bool

    Opt whether to use a magnetic heading for the runway heading.


Method detail
-------------

















.. py:method:: add_to_catalog(self, overwrite: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.add_to_catalog

    Add the runway to the catalog.

    :Parameters:

    **overwrite** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: copy_from_catalog(self, runway: ICatalogRunway) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.copy_from_catalog

    Copy the information from the runway stored in the catalog.

    :Parameters:

    **runway** : :obj:`~ICatalogRunway`

    :Returns:

        :obj:`~None`

.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteRunway.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

