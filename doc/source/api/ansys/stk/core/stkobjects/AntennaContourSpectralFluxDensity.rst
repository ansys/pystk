AntennaContourSpectralFluxDensity
=================================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`

   Class defining an antenna spectral flux density contour properties.

.. py:currentmodule:: AntennaContourSpectralFluxDensity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.azimuth_resolution`
              - Get the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.elevation_resolution`
              - Get the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.maximum_elevation_angle`
              - Get the maximum elevation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourSpectralFluxDensity


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.azimuth_resolution
    :type: typing.Any

    Get the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.elevation_resolution
    :type: typing.Any

    Get the elevation resolution.

.. py:property:: maximum_elevation_angle
    :canonical: ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.maximum_elevation_angle
    :type: typing.Any

    Get the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuth_resolution: float, elevation_resolution: float, max_elevation: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuth_resolution** : :obj:`~float`
    **elevation_resolution** : :obj:`~float`
    **max_elevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

