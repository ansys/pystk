IAntennaContourSpectralFluxDensity
==================================

.. py:class:: IAntennaContourSpectralFluxDensity

   object
   
   IAgAntennaContourSpectralFluxDensity Interface for a antenna's spectral flux density contour properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~azimuth_resolution`
            * - :py:meth:`~elevation_resolution`
            * - :py:meth:`~max_elevation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourSpectralFluxDensity


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourSpectralFluxDensity.azimuth_resolution
    :type: typing.Any

    Gets the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourSpectralFluxDensity.elevation_resolution
    :type: typing.Any

    Gets the elevation resolution.

.. py:property:: max_elevation
    :canonical: ansys.stk.core.stkobjects.IAntennaContourSpectralFluxDensity.max_elevation
    :type: typing.Any

    Gets the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuthResolution:float, elevationResolution:float, maxElevation:float) -> None

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuthResolution** : :obj:`~float`
    **elevationResolution** : :obj:`~float`
    **maxElevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

