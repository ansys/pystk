SolarFluxGeoMagneticFileSettings
================================

.. py:class:: ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitude`

   Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

.. py:currentmodule:: SolarFluxGeoMagneticFileSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings.file`
              - Path and name of flux/Ap file.
            * - :py:attr:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings.geomagnetic_flux_source`
              - Select a  method for updating the geomagnetic flux update rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings.geomagnetic_flux_update_rate`
              - Select a  method for updating the geomagnetic flux update rate.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SolarFluxGeoMagneticFileSettings


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings.file
    :type: str

    Path and name of flux/Ap file.

.. py:property:: geomagnetic_flux_source
    :canonical: ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings.geomagnetic_flux_source
    :type: VehicleGeomagneticFluxSourceType

    Select a  method for updating the geomagnetic flux update rate.

.. py:property:: geomagnetic_flux_update_rate
    :canonical: ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings.geomagnetic_flux_update_rate
    :type: VehicleGeomagneticFluxUpdateRateType

    Select a  method for updating the geomagnetic flux update rate.


