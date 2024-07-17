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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.latitude`
              - Gets or sets the VTOL Point latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.longitude`
              - Gets or sets the VTOL Point longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude`
              - Gets or sets the altitude for the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude_reference`
              - Gets or sets the altitude reference.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteVTOLPoint


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.latitude
    :type: typing.Any

    Gets or sets the VTOL Point latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.longitude
    :type: typing.Any

    Gets or sets the VTOL Point longitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude
    :type: float

    Gets or sets the altitude for the site.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.altitude_reference
    :type: AGL_MSL

    Gets or sets the altitude reference.


Method detail
-------------









.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteVTOLPoint.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

