IVehicleHPOPForceModelDrag
==========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag

   object
   
   Atmospheric Drag interface.

.. py:currentmodule:: IVehicleHPOPForceModelDrag

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.set_solar_flux_geo_magnitude_type`
              - Set the method for specifying solar and geomagnetic flux.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.set_drag_model_type`
              - Change the active drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.is_drag_model_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.use`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.atmospheric_density_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.solar_flux_geo_magnitude_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.solar_flux_geo_magnitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.drag_model_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.drag_model_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.drag_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.low_altitude_atmospheric_density_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.blending_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.low_altitude_atmos_density_model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPForceModelDrag


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.use
    :type: bool

    Opt whether to take account of atmospheric drag.

.. py:property:: atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.atmospheric_density_model
    :type: ATMOSPHERIC_DENSITY_MODEL

    Select the atmospheric density model to be used.

.. py:property:: solar_flux_geo_magnitude_type
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.solar_flux_geo_magnitude_type
    :type: VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE

    Get the method for specifying solar and geomagnetic flux.

.. py:property:: solar_flux_geo_magnitude
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.solar_flux_geo_magnitude
    :type: IVehicleSolarFluxGeoMagnitude

    Solar and geomagnetic flux.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.drag_model_type
    :type: DRAG_MODEL

    Returns a type of the active drag model.

.. py:property:: drag_model_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.drag_model_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: drag_model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.drag_model
    :type: IVehicleHPOPDragModel

    Returns the active drag model.

.. py:property:: low_altitude_atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.low_altitude_atmospheric_density_model
    :type: ATMOSPHERIC_DENSITY_MODEL

    This property is deprecated. Use LowAltAtmosDensityModel instead. Select the low altitude atmospheric density model to be used.

.. py:property:: blending_range
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.blending_range
    :type: float

    Atmospheric blending range: measured from the lower extent of the upper atmospheric model. Uses distance dimension.

.. py:property:: low_altitude_atmos_density_model
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.low_altitude_atmos_density_model
    :type: LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL

    Select the low altitude atmospheric density model to be used.


Method detail
-------------






.. py:method:: set_solar_flux_geo_magnitude_type(self, solarFluxGeoMag: VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.set_solar_flux_geo_magnitude_type

    Set the method for specifying solar and geomagnetic flux.

    :Parameters:

    **solarFluxGeoMag** : :obj:`~VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE`

    :Returns:

        :obj:`~None`



.. py:method:: set_drag_model_type(self, dragModel: DRAG_MODEL) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.set_drag_model_type

    Change the active drag model type.

    :Parameters:

    **dragModel** : :obj:`~DRAG_MODEL`

    :Returns:

        :obj:`~None`

.. py:method:: is_drag_model_type_supported(self, dragModel: DRAG_MODEL) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModelDrag.is_drag_model_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **dragModel** : :obj:`~DRAG_MODEL`

    :Returns:

        :obj:`~bool`









