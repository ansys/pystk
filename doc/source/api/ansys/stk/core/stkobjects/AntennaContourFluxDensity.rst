AntennaContourFluxDensity
=========================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourFluxDensity

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`

   Class defining an antenna flux density contour properties.

.. py:currentmodule:: AntennaContourFluxDensity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourFluxDensity.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourFluxDensity.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourFluxDensity.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourFluxDensity.max_elevation`
              - Gets the maximum elevation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourFluxDensity


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourFluxDensity.azimuth_resolution
    :type: typing.Any

    Gets the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourFluxDensity.elevation_resolution
    :type: typing.Any

    Gets the elevation resolution.

.. py:property:: max_elevation
    :canonical: ansys.stk.core.stkobjects.AntennaContourFluxDensity.max_elevation
    :type: typing.Any

    Gets the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuthResolution: float, elevationResolution: float, maxElevation: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourFluxDensity.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuthResolution** : :obj:`~float`
    **elevationResolution** : :obj:`~float`
    **maxElevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

