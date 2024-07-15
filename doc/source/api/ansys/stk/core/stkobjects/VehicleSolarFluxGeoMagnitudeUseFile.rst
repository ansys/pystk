VehicleSolarFluxGeoMagnitudeUseFile
===================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitude`

   Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

.. py:currentmodule:: VehicleSolarFluxGeoMagnitudeUseFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile.file`
              - Path and name of flux/Ap file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile.geomag_flux_update_rate`
              - Select a  method for updating the geomagnetic flux update rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile.geomag_flux_src`
              - Select a  method for updating the geomagnetic flux update rate.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSolarFluxGeoMagnitudeUseFile


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile.file
    :type: str

    Path and name of flux/Ap file.

.. py:property:: geomag_flux_update_rate
    :canonical: ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile.geomag_flux_update_rate
    :type: VEHICLE_GEOMAG_FLUX_UPDATE_RATE

    Select a  method for updating the geomagnetic flux update rate.

.. py:property:: geomag_flux_src
    :canonical: ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile.geomag_flux_src
    :type: VEHICLE_GEOMAG_FLUX_SRC

    Select a  method for updating the geomagnetic flux update rate.


