Satellite
=========

.. py:class:: ansys.stk.core.stkobjects.Satellite

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`

   Satellite properties.

.. py:currentmodule:: Satellite

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.set_propagator_type`
              - Set the propagator type.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.set_attitude_type`
              - Set the attitude type.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.is_attitude_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.is_propagator_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.propagator_type`
              - Get the type of propagator used to define the satellite's orbit.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.propagator`
              - Get information for the propagator.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.attitude_type`
              - Get the type of the satellite's attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.attitude_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.attitude`
              - Get the Attitude properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.mass_properties`
              - Get the Mass properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.pass_break`
              - Get the Pass Break properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.ground_ellipses`
              - Get the Ground Ellipses properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.graphics`
              - Get the 2D Graphics properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.graphics_3d`
              - Get the 3D Graphics properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.access_constraints`
              - Get the constraints imposed on the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.eclipse_bodies`
              - Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.propagator_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.export_tools`
              - Return the IAgSaExportTools interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.space_environment`
              - Get the SpaceEnvironment properties of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.reference_vehicle`
              - Get the reference vehicle of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.radar_clutter_map`
              - Return the radar clutter map.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.radar_cross_section`
              - Return the radar cross sectoin.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.use_terrain_in_lighting_computations`
              - Opt whether to compute lighting using terrain data.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.lighting_maximum_step`
              - Do not use this property, as it is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.lighting_maximum_step_terrain`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.lighting_maximum_step_central_body_shape`
              - Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Satellite.get_eoir_settings`
              - Get the EOIR properties of the satellite.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Satellite


Property detail
---------------

.. py:property:: propagator_type
    :canonical: ansys.stk.core.stkobjects.Satellite.propagator_type
    :type: PropagatorType

    Get the type of propagator used to define the satellite's orbit.

.. py:property:: propagator
    :canonical: ansys.stk.core.stkobjects.Satellite.propagator
    :type: IPropagator

    Get information for the propagator.

.. py:property:: attitude_type
    :canonical: ansys.stk.core.stkobjects.Satellite.attitude_type
    :type: VehicleAttitude

    Get the type of the satellite's attitude.

.. py:property:: attitude_supported_types
    :canonical: ansys.stk.core.stkobjects.Satellite.attitude_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attitude
    :canonical: ansys.stk.core.stkobjects.Satellite.attitude
    :type: IVehicleAttitude

    Get the Attitude properties of the satellite.

.. py:property:: mass_properties
    :canonical: ansys.stk.core.stkobjects.Satellite.mass_properties
    :type: VehicleMassProperties

    Get the Mass properties of the satellite.

.. py:property:: pass_break
    :canonical: ansys.stk.core.stkobjects.Satellite.pass_break
    :type: PassBreak

    Get the Pass Break properties of the satellite.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.Satellite.ground_ellipses
    :type: VehicleGroundEllipsesCollection

    Get the Ground Ellipses properties of the satellite.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Satellite.graphics
    :type: SatelliteGraphics

    Get the 2D Graphics properties of the satellite.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Satellite.graphics_3d
    :type: SatelliteGraphics3D

    Get the 3D Graphics properties of the satellite.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.Satellite.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the satellite.

.. py:property:: eclipse_bodies
    :canonical: ansys.stk.core.stkobjects.Satellite.eclipse_bodies
    :type: VehicleEclipseBodies

    Get the customized list of Eclipse Bodies, which are central bodies used in lighting computations.

.. py:property:: propagator_supported_types
    :canonical: ansys.stk.core.stkobjects.Satellite.propagator_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: export_tools
    :canonical: ansys.stk.core.stkobjects.Satellite.export_tools
    :type: SatelliteExportTools

    Return the IAgSaExportTools interface.

.. py:property:: space_environment
    :canonical: ansys.stk.core.stkobjects.Satellite.space_environment
    :type: SpaceEnvironment

    Get the SpaceEnvironment properties of the satellite.

.. py:property:: reference_vehicle
    :canonical: ansys.stk.core.stkobjects.Satellite.reference_vehicle
    :type: LinkToObject

    Get the reference vehicle of the satellite.

.. py:property:: radar_clutter_map
    :canonical: ansys.stk.core.stkobjects.Satellite.radar_clutter_map
    :type: IRadarClutterMapInheritable

    Return the radar clutter map.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.Satellite.radar_cross_section
    :type: RadarCrossSectionInheritable

    Return the radar cross sectoin.

.. py:property:: use_terrain_in_lighting_computations
    :canonical: ansys.stk.core.stkobjects.Satellite.use_terrain_in_lighting_computations
    :type: bool

    Opt whether to compute lighting using terrain data.

.. py:property:: lighting_maximum_step
    :canonical: ansys.stk.core.stkobjects.Satellite.lighting_maximum_step
    :type: float

    Do not use this property, as it is deprecated. Use LightingMaxStepTerrain or LightingMaxStepCbShape as appropriate. The maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_maximum_step_terrain
    :canonical: ansys.stk.core.stkobjects.Satellite.lighting_maximum_step_terrain
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is true. Uses Time Dimension.

.. py:property:: lighting_maximum_step_central_body_shape
    :canonical: ansys.stk.core.stkobjects.Satellite.lighting_maximum_step_central_body_shape
    :type: float

    Get or set the maximum step size to use when computing lighting when UseTerrainInLightingComputations is false. Uses Time Dimension.

.. py:property:: get_eoir_settings
    :canonical: ansys.stk.core.stkobjects.Satellite.get_eoir_settings
    :type: IEOIR

    Get the EOIR properties of the satellite.


Method detail
-------------


.. py:method:: set_propagator_type(self, propagator: PropagatorType) -> None
    :canonical: ansys.stk.core.stkobjects.Satellite.set_propagator_type

    Set the propagator type.

    :Parameters:

    **propagator** : :obj:`~PropagatorType`

    :Returns:

        :obj:`~None`



.. py:method:: set_attitude_type(self, attitude: VehicleAttitude) -> None
    :canonical: ansys.stk.core.stkobjects.Satellite.set_attitude_type

    Set the attitude type.

    :Parameters:

    **attitude** : :obj:`~VehicleAttitude`

    :Returns:

        :obj:`~None`

.. py:method:: is_attitude_type_supported(self, attitude: VehicleAttitude) -> bool
    :canonical: ansys.stk.core.stkobjects.Satellite.is_attitude_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attitude** : :obj:`~VehicleAttitude`

    :Returns:

        :obj:`~bool`










.. py:method:: is_propagator_type_supported(self, propagator: PropagatorType) -> bool
    :canonical: ansys.stk.core.stkobjects.Satellite.is_propagator_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **propagator** : :obj:`~PropagatorType`

    :Returns:

        :obj:`~bool`
















