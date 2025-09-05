SolarFluxGeoMagneticValueSettings
=================================

.. py:class:: ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitude`

   Class defining the option to enter a vehicle's solar flux and/or GeoMag properties manually, depending on the selected atmospheric density model.

.. py:currentmodule:: SolarFluxGeoMagneticValueSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings.average_f107`
              - Average F10.7: 81-day averaged Ottawa 10.7 cm solar flux value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings.daily_f107`
              - Daily F10.7: daily Ottawa 10.7 cm solar flux value. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings.geomagnetic_index`
              - Geomagnetic Index (Kp): planetary geomagnetic flux index. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SolarFluxGeoMagneticValueSettings


Property detail
---------------

.. py:property:: average_f107
    :canonical: ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings.average_f107
    :type: float

    Average F10.7: 81-day averaged Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: daily_f107
    :canonical: ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings.daily_f107
    :type: float

    Daily F10.7: daily Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: geomagnetic_index
    :canonical: ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings.geomagnetic_index
    :type: float

    Geomagnetic Index (Kp): planetary geomagnetic flux index. Dimensionless.


