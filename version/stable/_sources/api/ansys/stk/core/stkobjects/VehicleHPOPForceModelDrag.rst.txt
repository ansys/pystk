VehicleHPOPForceModelDrag
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag

   Class defining the HPOP atmospheric drag model.

.. py:currentmodule:: VehicleHPOPForceModelDrag

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.set_solar_flux_geo_magnitude_type`
              - Set the method for specifying solar and geomagnetic flux.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.set_drag_model_type`
              - Change the active drag model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.is_drag_model_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.use`
              - Opt whether to take account of atmospheric drag.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.atmospheric_density_model`
              - Select the atmospheric density model to be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.solar_flux_geo_magnitude_type`
              - Get the method for specifying solar and geomagnetic flux.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.solar_flux_geo_magnitude`
              - Solar and geomagnetic flux.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.drag_model_type`
              - Return a type of the active drag model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.drag_model_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.drag_model`
              - Return the active drag model.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.low_altitude_atmospheric_density_model`
              - Do not use this property, as it is deprecated. Use LowAltAtmosDensityModel instead. Select the low altitude atmospheric density model to be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.blending_range`
              - Atmospheric blending range: measured from the lower extent of the upper atmospheric model. Uses distance dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.low_altitude_atmosphere_density_model`
              - Select the low altitude atmospheric density model to be used.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleHPOPForceModelDrag


Property detail
---------------

.. py:property:: use
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.use
    :type: bool

    Opt whether to take account of atmospheric drag.

.. py:property:: atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.atmospheric_density_model
    :type: AtmosphericDensityModel

    Select the atmospheric density model to be used.

.. py:property:: solar_flux_geo_magnitude_type
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.solar_flux_geo_magnitude_type
    :type: VehicleSolarFluxGeomagneticType

    Get the method for specifying solar and geomagnetic flux.

.. py:property:: solar_flux_geo_magnitude
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.solar_flux_geo_magnitude
    :type: IVehicleSolarFluxGeoMagnitude

    Solar and geomagnetic flux.

.. py:property:: drag_model_type
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.drag_model_type
    :type: DragModel

    Return a type of the active drag model.

.. py:property:: drag_model_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.drag_model_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: drag_model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.drag_model
    :type: IVehicleHPOPDragModel

    Return the active drag model.

.. py:property:: low_altitude_atmospheric_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.low_altitude_atmospheric_density_model
    :type: AtmosphericDensityModel

    Do not use this property, as it is deprecated. Use LowAltAtmosDensityModel instead. Select the low altitude atmospheric density model to be used.

.. py:property:: blending_range
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.blending_range
    :type: float

    Atmospheric blending range: measured from the lower extent of the upper atmospheric model. Uses distance dimension.

.. py:property:: low_altitude_atmosphere_density_model
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.low_altitude_atmosphere_density_model
    :type: LowAltitudeAtmosphericDensityModel

    Select the low altitude atmospheric density model to be used.


Method detail
-------------






.. py:method:: set_solar_flux_geo_magnitude_type(self, solar_flux_geo_mag: VehicleSolarFluxGeomagneticType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.set_solar_flux_geo_magnitude_type

    Set the method for specifying solar and geomagnetic flux.

    :Parameters:

        **solar_flux_geo_mag** : :obj:`~VehicleSolarFluxGeomagneticType`


    :Returns:

        :obj:`~None`



.. py:method:: set_drag_model_type(self, drag_model: DragModel) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.set_drag_model_type

    Change the active drag model type.

    :Parameters:

        **drag_model** : :obj:`~DragModel`


    :Returns:

        :obj:`~None`

.. py:method:: is_drag_model_type_supported(self, drag_model: DragModel) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag.is_drag_model_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **drag_model** : :obj:`~DragModel`


    :Returns:

        :obj:`~bool`









