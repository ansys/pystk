AntennaContourRip
=================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourRip

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`

   Class defining an antenna rip contour properties.

.. py:currentmodule:: AntennaContourRip

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRip.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRip.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRip.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRip.max_elevation`
              - Gets the maximum elevation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourRip


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourRip.azimuth_resolution
    :type: typing.Any

    Gets the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourRip.elevation_resolution
    :type: typing.Any

    Gets the elevation resolution.

.. py:property:: max_elevation
    :canonical: ansys.stk.core.stkobjects.AntennaContourRip.max_elevation
    :type: typing.Any

    Gets the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuthResolution: float, elevationResolution: float, maxElevation: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourRip.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuthResolution** : :obj:`~float`
    **elevationResolution** : :obj:`~float`
    **maxElevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

