SiteVTOLPoint
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a VTOL Point site.

.. py:currentmodule:: SiteVTOLPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude`
              - Get or set the altitude for the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude_reference`
              - Get or set the altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.latitude`
              - Get or set the VTOL Point latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.longitude`
              - Get or set the VTOL Point longitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteVTOLPoint


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude
    :type: float

    Get or set the altitude for the site.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude_reference
    :type: AGLMSL

    Get or set the altitude reference.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.latitude
    :type: typing.Any

    Get or set the VTOL Point latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.longitude
    :type: typing.Any

    Get or set the VTOL Point longitude.


Method detail
-------------





.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`





