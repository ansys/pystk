IVehicleSolarFluxGeoMagnitudeEnterManually
==========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually

   object
   
   Interface for specifying solar and geomagnetic flux directly.

.. py:currentmodule:: IVehicleSolarFluxGeoMagnitudeEnterManually

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually.daily_f107`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually.average_f107`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually.geomagnetic_index`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSolarFluxGeoMagnitudeEnterManually


Property detail
---------------

.. py:property:: daily_f107
    :canonical: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually.daily_f107
    :type: float

    Daily F10.7: daily Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: average_f107
    :canonical: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually.average_f107
    :type: float

    Average F10.7: 81-day averaged Ottawa 10.7 cm solar flux value. Dimensionless.

.. py:property:: geomagnetic_index
    :canonical: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeEnterManually.geomagnetic_index
    :type: float

    Geomagnetic Index (Kp): planetary geomagnetic flux index. Dimensionless.


