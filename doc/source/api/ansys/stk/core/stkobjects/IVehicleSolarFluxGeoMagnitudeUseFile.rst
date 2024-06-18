IVehicleSolarFluxGeoMagnitudeUseFile
====================================

.. py:class:: IVehicleSolarFluxGeoMagnitudeUseFile

   object
   
   Interface for specifying solar and geomagnetic flux via a file.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~file`
            * - :py:meth:`~geomag_flux_update_rate`
            * - :py:meth:`~geomag_flux_src`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSolarFluxGeoMagnitudeUseFile


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeUseFile.file
    :type: str

    Path and name of flux/Ap file.

.. py:property:: geomag_flux_update_rate
    :canonical: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeUseFile.geomag_flux_update_rate
    :type: "VEHICLE_GEOMAG_FLUX_UPDATE_RATE"

    Select a  method for updating the geomagnetic flux update rate.

.. py:property:: geomag_flux_src
    :canonical: ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitudeUseFile.geomag_flux_src
    :type: "VEHICLE_GEOMAG_FLUX_SRC"

    Select a  method for updating the geomagnetic flux update rate.


