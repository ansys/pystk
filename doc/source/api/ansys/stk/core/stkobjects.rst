
The ``stkobjects`` module
=========================


.. py:module:: ansys.stk.core.stkobjects


Summary
-------

.. tab-set::

    .. tab-item:: Subpackages

        .. list-table::
            :header-rows: 0
            :widths: auto
        
            * - :py:obj:`~ansys.stk.core.stkobjects.aviator`

    .. tab-item:: Submodules

        .. list-table::
            :header-rows: 0
            :widths: auto
        
            * - :py:mod:`~ansys.stk.core.stkobjects.astrogator`

             
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.IDataProviderInfo`
              - Provide methods for retrieving the information about data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.IDataProvider`
              - Represents the Sub Data Provider (i.e. ``Fixed`` in ``Cartesian Position`` group on satellites, or ``Cartesian Position`` on facilities).

            * - :py:class:`~ansys.stk.core.stkobjects.IStkObject`
              - Represents the instance of STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessInterval`
              - Base interface for IAgTimePeriod and IAgIntervalCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinition`
              - Figure of Merit definition.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.IStkObjectElementCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~ansys.stk.core.stkobjects.IStkObjectCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~ansys.stk.core.stkobjects.IAnimation`
              - Provide methods to control scenario animation.

            * - :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`
              - Interface for a component.

            * - :py:class:`~ansys.stk.core.stkobjects.ICloneable`
              - Interface for a component.

            * - :py:class:`~ansys.stk.core.stkobjects.IComponentLinkEmbedControl`
              - Interface for a control which manages the linking or embedding of a component from the component browser.

            * - :py:class:`~ansys.stk.core.stkobjects.IDisplayTimesData`
              - Base Interface IAgDisplayTimesData. IAgIntervalCollection, IAgDuringAccess and IAgDisplayTimesTimeComponent derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`
              - The display time interface.

            * - :py:class:`~ansys.stk.core.stkobjects.ITerrainNormData`
              - Base Interface IAgTerrainNormData. IAgTerrainNormSlopeAzimuth derives from this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`
              - Provide the information about the lifetime of the object.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLeadTrailData`
              - Base interface IAgVeLeadTrailData.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLeadTrailDataFraction`
              - The percentage of the leading or trailing portion of a vehicle's path that will display in the 2D or 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLeadTrailDataTime`
              - Configure the amount of time to display the vehicle's path in 2D or 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`
              - AgAccessConstraint used to access the AccessConstraint attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessConstraintMinMax`
              - Access Constraint used for min/max constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DMarkerData`
              - Base Interface IAgVOMarkerData.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModelData`
              - IAgVOModelData base interface. IAgVOModelFile and IAgVOModelCollection derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModel`
              - AgVOModel used to access the 3D model attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`
              - IAgVORefCrdn used to access the shared properties of all 3D RefCrdn.

            * - :py:class:`~ansys.stk.core.stkobjects.ILLAPosition`
              - Interface to set and retrieve the LLA position type.

            * - :py:class:`~ansys.stk.core.stkobjects.IClassicalSizeShape`
              - Base Interface for SizeShape property. IAgClassicalSizeShapeAltitude, IAgClassicalSizeShapeMeanMotion, IAgClassicalSizeShapePeriod, IAgClassicalSizeShapeRadius and IAgClassicalSizeShapeSemimajorAxis derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IOrientationAscNode`
              - Base Interface to IAgOrientationAscNodeLAN and IAgOrientationAscNodeRAAN.

            * - :py:class:`~ansys.stk.core.stkobjects.IClassicalLocation`
              - Base Interface of all IAgClassicalLocation* interfaces.

            * - :py:class:`~ansys.stk.core.stkobjects.IGeodeticSize`
              - Base Interface IAgGeodeticSize. IAgGeodeticSizeAltitude and IAgGeodeticSizeRadius derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IDelaunayActionVariable`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~ansys.stk.core.stkobjects.IFlightPathAngle`
              - Base Interface IAgFlightPathAngle. IAgMixedSphericalFPAHorizontal, IAgMixedSphericalFPAVertical, IAgSphericalFPAHorizontal and IAgSphericalFPAVertical derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`
              - Provide methods for accessing spatial information for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMap`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar clutter map.

            * - :py:class:`~ansys.stk.core.stkobjects.ITimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessAdvanced`
              - Interface for configuring advanced targeting access computation properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IRefractionModelBase`
              - A base interface for the Refraction Models.

            * - :py:class:`~ansys.stk.core.stkobjects.IDisplayDistance`
              - Base interface IAgDisplayDistance. IAgSnProjDisplayDistance, IAgSnProjConstantAlt and IAgSnProjObjectAlt derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance`
              - IAgSnProjDisplayDistance Interface for setting projection altitude options for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorPattern`
              - Base interface IAgSnPattern. IAgSnComplexConicPattern, IAgSnCustomPattern, IAgSnHalfPowerPattern, IAgSnRectangularPattern, IAgSnSARPattern, IAgSnEOIRPattern and IAgSnSimpleConicPattern implement this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorPointingTargetedBoresight`
              - Base interface IAgSnPtTrgtBsight. IAgSnPtTrgtBsightFixed and IAgSnPtTrgtBsightTrack derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`
              - Base interface IAgSnPointing. IAgSnPt3DModel, IAgSnPtExternal, IAgSnPtFixed, IAgSnPtFixedAxes, IAgSnPtGrazingAlt, IAgSnPtTargeted, IAgSnPtAlongVector and IAgSnPtSchedule implement this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IAzElMaskData`
              - Base interface IAgAzElMaskData. IAgSnAzElMaskFile implements this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapInheritable`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar inheritable clutter map.

            * - :py:class:`~ansys.stk.core.stkobjects.IPlatformRFEnvironment`
              - Provide access to the properties and methods defining the platform RF environment.

            * - :py:class:`~ansys.stk.core.stkobjects.IAreaTypeData`
              - Base interface IAgAreaTypeData. IAgAreaTypePatternCollection and IAgAreaTypeEllipse derive from it.

            * - :py:class:`~ansys.stk.core.stkobjects.IPositionSourceData`
              - Base interface to IAgPlPosCentralBody and IAgPlPosFile.

            * - :py:class:`~ansys.stk.core.stkobjects.IOrbitDisplayData`
              - IAgOrbitDisplayData Interface. IAgPlOrbitDisplayTime derives from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarization`
              - Provide the base interface for the a polarization object.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationElliptical`
              - Provide the interface for elliptical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationCrossPolLeakage`
              - Provide the interface for polarization cross pol leakage.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationLinear`
              - Provide the interface for linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationHorizontal`
              - Provide the interface for linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationVertical`
              - Provide the interface for linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPointingStrategy`
              - Provide the base interface for a pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IWaveform`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategy`
              - Provide the base interface for a waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IScatteringPointProvider`
              - Provide access to the properties and methods defining a scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.IScatteringPointModel`
              - Provide access to the properties and methods defining a scattering point model model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.IElementConfiguration`
              - Provide access to the properties and methods defining an element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon`
              - Provide access to the properties and methods defining a polygon element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.IBeamformer`
              - Provide access to the properties and methods defining a beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.IDirectionProvider`
              - Provide access to the properties and methods defining an direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaModelOpticalSimple`
              - Provide access to the properties and methods defining a simple optical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`
              - IAgAntennaContour Interface for a antenna's contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaBeamSelectionStrategy`
              - Provide access to a beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaBeam`
              - Provide access to an antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.IRFFilterModel`
              - Provide access to the properties and methods defining an RF filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.IModulatorModel`
              - Provide access to the properties and methods defining a modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`
              - Provide access to the properties and methods defining a transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ITransmitterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.IReTransmitterModel`
              - Provide access to the properties and methods defining a re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.IDemodulatorModel`
              - Provide access to the properties and methods defining a demodulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.IReceiverModel`
              - Provide access to the properties and methods defining a receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.IReceiverModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarActivity`
              - Provide access to the properties and methods defining radar activity.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarStcAttenuation`
              - Provide access to the properties and methods defining a radar STC attenuation.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarStcAttenuationMap`
              - Provide access to the properties and methods defining a radar STC attenuation map.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterGeometryModel`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointProvider interface instead. Provides access to the properties and methods defining a radar clutter geometry model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointProviderPlugin interface instead. Provides access to the properties and methods defining a radar clutter geometry plugin model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarContinuousWaveAnalysisMode`
              - Interface which defines an continuous wave analysis.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarPulseIntegration`
              - Interface which defines an integration method.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarWaveformSearchTrack`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarProbabilityOfDetection`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarProbabilityOfDetectionCFAR`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModel`
              - Provide access to the properties and methods defining a radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModeMonostatic`
              - Provide access to the properties and methods defining a monostatic mode.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter mode.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver mode.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapModel`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModel interface instead. Provides access to the properties and methods defining a radar clutter map model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapModelPlugin`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModelPlugin interface instead. Provides access to the properties and methods defining a radar clutter map plugin model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapModelConstantCoefficient`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModelConstantCoefficient interface instead. Provides access to the properties and methods defining a radar clutter map constant coefficient model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarCrossSectionComputeStrategy`
              - Provide access to the properties and methods defining a radar cross section compute Strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IModulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRainLossModel`
              - Provide access to the properties and methods a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IUrbanTerrestrialLossModel`
              - Provide access to the properties and methods for an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModel`
              - Provide access to the properties and methods for a TropoSpheric Scintillation Fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IIonosphericFadingLossModel`
              - Provide access to the properties and methods for an Ionospheric Fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModel`
              - Provide access to the properties and methods for Clouds and Fog loss models.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModel`
              - Provide access to the properties and methods an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelITURP676`
              - Provide access to the properties and methods of the ITU-R P676 atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTirem`
              - Provide access to the properties and methods of the TIREM atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.ISolarActivityConfiguration`
              - Provide access to the properties and methods defining the solar activity configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModel`
              - Provide access to the properties and methods for a laser atmospheric absorption loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ILaserTroposphericScintillationLossModel`
              - Provide access to the properties and methods for a laser tropospheric scintillation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericTurbulenceModel`
              - Provide access to a refractive index structure parameter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ILaserPropagationChannel`
              - Provide access to laser propagation loss models.

            * - :py:class:`~ansys.stk.core.stkobjects.ICommSystemLinkSelectionCriteria`
              - Provide access to a link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessEventDetection`
              - Provide access to the properties an access event detection algorithm.

            * - :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessSamplingMethod`
              - Provide access to the properties for the sampling method.

            * - :py:class:`~ansys.stk.core.stkobjects.ISRPModelBase`
              - A base interface for solar radiation pressure models.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleHPOPDragModel`
              - A base interface for drag models.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleSGP4LoadData`
              - Load Method Data interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitude`
              - Base Interface IAgVeSolarFluxGeoMag. IAgVeSolarFluxGeoMagEnterManually and IAgVeSolarFluxGeoMagUseFile derive from this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`
              - Base vehicle propagator interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReference`
              - Base interface for the altitude references.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleImpact`
              - Base Interface IAgVeImpact. IAgVeImpactLLA and IAgVeImpactLLR derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLaunchControl`
              - Base Interface IAgVeLaunchControl. IAgVeLaunchControlFixedApogeeAlt, IAgVeLaunchControlFixedDeltaV, IAgVeLaunchControlDixedDeltaVMinEcc and IAgVeLaunchControlTimeOfFlight derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLaunch`
              - Base interface IAgVeLaunch. IAgVeLaunchLLA and IAgVeLaunchLLR derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleImpactLocation`
              - Base interface IAgVeImpactLocation. IAgVeImpactLocationLaunchAzEl and IAgVeImpactLocationPoint derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacProperties`
              - A common base interface for GPS almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`
              - The base interface that all vehicle attitude profiles are derived from.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehiclePointing`
              - Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`
              - Base interface for vehicle attitude options.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`
              - Standard attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPass`
              - interface IAgVeGfxPass. IAgVeGfxPassShowPasses and IAgVeGfxPassResolution derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventType`
              - Base Interface IAgVeGfxTimeEventType. IAgVeGfxTimeEventTypeLine, IAgVeGfxTimeEventTypeMarker and IAgVeGfxTimeEventTypeText derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributes`
              - Base Interface for Vehicle 2D Graphics Attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic`
              - Basic 2D Graphics Attributes for a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesDisplayState`
              - Provide access to non-trivial properties of 2D vehicle attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DElevation`
              - Base Interface IAgVeGfxElevation. IAgVeGfxElevationGroundElevation, IAgVeGfxElevationsSwathHalfWidth and IAgVeGfxElevationsSwathHalfAngle derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase`
              - Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximityAreaObject`
              - A base class that defines methods and properties common to all proximity area objects.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximity`
              - Base Proximity graphics interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSigmaScale`
              - Base Interface IAgVeVOSigmaScale. IAgVeVOSigmaScaleScale and IAgVeVOSigmaScaleProbability derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DAttributes`
              - Base Interface IAgVeVOAttributes. IAgVeVOAttributesBasic and IAgVeVOAttributesIntervals derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTickData`
              - Base interface IAgVeVOTickData. IAgVeVOTickDataLine and IAgVeVOTickDataPoint derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics`
              - 2D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D`
              - 3D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`
              - A base interface for all Great Arc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPointPosition`
              - A base class for BPlane target point position interfaces.

            * - :py:class:`~ansys.stk.core.stkobjects.IEOIR`
              - Property used to access IAgEOIR interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleBreakAngle`
              - Base Interface IAgVeBreakAngle. IAgVeBreakAngleBreakByLatitude and IAgVeBreakAngleBreakByLongitude derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehiclePassNumbering`
              - Base Interaface IAgVePassNumbering. IAgVePassNumberingDateOfFirstPass and IAgVePassNumberingFirstPassNum derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleCoordinateAxes`
              - IAgVeCoordinateAxes.

            * - :py:class:`~ansys.stk.core.stkobjects.IChainTimePeriodBase`
              - Chain time period options.

            * - :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`
              - Base interface for IAgCvBoundsCustom, IAgCvBoundsGlobal, IAgCvBoundsLat, IAgCvBoundsLatLines, IAgCvBoundsLonLines, IAgCvBoundsCustomBoundary.

            * - :py:class:`~ansys.stk.core.stkobjects.ICoverageResolution`
              - Base interface for IAgCvResolutionArea, IAgCvResolutionDistance and IAgCvResolutionLatLon, used to define coverage resolution (spacing between grid points).

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritNavigationAccuracyMethod`
              - Navigation Accuracy Figure of Merit type.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionData`
              - IAgFmDefinitionData.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.IConstellationConstraintRestriction`
              - A base interface for all interfaces returned by the Restriction property of the IAgCnConstraints interface. It can be cast to IAgCnCnstrObjectRestriction.

            * - :py:class:`~ansys.stk.core.stkobjects.IEventDetectionStrategy`
              - Define a base interface for the event detection strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.ISamplingMethodStrategy`
              - Define a base interface for the sampling method strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewBase`
              - Represents an attitude slew base type.

            * - :py:class:`~ansys.stk.core.stkobjects.IVolumetricGridDefinition`
              - Base interface IAgVmGridDefinition. IAgVmGridSpatialCalculation and IAgVmExternalFile implement this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IEOIRShapeObject`
              - A shape object interface.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.StkObject`
              - Represents a generic STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.StkObjectRoot`
              - Top-level object in the Object Model Hierarchy.

            * - :py:class:`~ansys.stk.core.stkobjects.LevelAttribute`
              - Properties defining display of contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.LevelAttributeCollection`
              - Collection of properties defining display of contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.BasicAzElMask`
              - The Azimuth-Elevation Mask class.

            * - :py:class:`~ansys.stk.core.stkobjects.FacilityGraphics`
              - 2D Graphics properties of a Facility.

            * - :py:class:`~ansys.stk.core.stkobjects.PlaceGraphics`
              - 2D Graphics properties of a Place.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics2DRangeContours`
              - Class defining 2D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraint`
              - Class defining access constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCollection`
              - Collection of access constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DRangeContours`
              - Class defining 3D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetRotate`
              - Class defining rotation in the object body frame's X, Y and Z directions.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetTransformation`
              - Class defining model translation in the object body frame's X, Y and Z directions.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttach`
              - Class defining attach points for the attachment of lines to objects.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel`
              - Class defining the offset of the position of an object label in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffset`
              - Class defining 3D offset attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarkerShape`
              - Class defining the marker type that represents the object in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarkerFile`
              - Class defining 3D marker file attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarker`
              - Class defining the 3D marker to represent an object at a specified threshold.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold`
              - Class defining detail thresholds as an aid for improving performance when viewing in 3D.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelItem`
              - Class defining selection and display of 3D models.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelCollection`
              - Collection representing 3D model list.

            * - :py:class:`~ansys.stk.core.stkobjects.LabelNote`
              - Class defining label notes.

            * - :py:class:`~ansys.stk.core.stkobjects.LabelNoteCollection`
              - Collection representing label notes list.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DVector`
              - Class defining 3D vectors.

            * - :py:class:`~ansys.stk.core.stkobjects.FacilityGraphics3D`
              - 3D Graphics properties of a Facility.

            * - :py:class:`~ansys.stk.core.stkobjects.PlaceGraphics3D`
              - 3D Graphics properties of a Place.

            * - :py:class:`~ansys.stk.core.stkobjects.TerrainNormSlopeAzimuth`
              - Class defining Slope/Azimuth data for the TerrainNormal.

            * - :py:class:`~ansys.stk.core.stkobjects.IntervalCollection`
              - Class defining display intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.ImmutableIntervalCollection`
              - Read-only collection of intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.DuringAccess`
              - Class defining display intervals in terms of access to objects.

            * - :py:class:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent`
              - Provide methods to configure the display times using Timeline API components.

            * - :py:class:`~ansys.stk.core.stkobjects.StarGraphics3D`
              - Class defining 3D Graphics properties of a Star.

            * - :py:class:`~ansys.stk.core.stkobjects.StarGraphics`
              - Class defining 2D Graphics properties of a Star.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetGraphics3D`
              - Class defining 3D Graphics properties of a Planet.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetGraphics`
              - Class defining 2D Graphics properties of a Planet.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTypePattern`
              - Class defining coordinates of the AreaTarget AreaType.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTypePatternCollection`
              - Class defining the list of coordinates of the AreaTarget AreaType.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTypeEllipse`
              - Class defining the AreaTarget AreaType in terms of MajorAxis, MinorAxis and Bearing.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D`
              - Class to define the 3D attributes of an AreaTarget.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTargetGraphics`
              - Class to define the 2D attributes of an AreaTarget.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DAzElMask`
              - Class to define display labels and adjust the translucency of the 3D azimuth-elevation mask for a facility, place or target.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelArtic`
              - Class defining 3D model articulations.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection`
              - Collection of available transformations in a model.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelTransformation`
              - Class to modify transformation values.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelFile`
              - Class defining 3D model file.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetPositionFile`
              - Class defining the planetary ephemeris file.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody`
              - Class defining central body used to define Planet object.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetOrbitDisplayTime`
              - Class defining display time of a planet's orbit.

            * - :py:class:`~ansys.stk.core.stkobjects.Scenario`
              - Class defining the Scenario object.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioAnimation`
              - Class defining the animation properties of a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioEarthData`
              - Class defining the Earth Orientation Parameters of a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioGraphics`
              - Class defining the 2D Graphics properties of a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.TerrainCollection`
              - Collection of terrain data files available in the Scenario for visualization and analysis.

            * - :py:class:`~ansys.stk.core.stkobjects.Terrain`
              - Class defining terrain data for a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.TilesetCollection3D`
              - Collection of 3DTilesets available in the Scenario for analysis.

            * - :py:class:`~ansys.stk.core.stkobjects.Tileset3D`
              - Class defining Analytical 3DTileset for a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioGenDatabaseCollection`
              - Collection of Scenario database settings.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioGenDatabase`
              - Class defining database settings of the Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioGraphics3D`
              - Class defining 3D Graphics properties of the Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorComplexConicPattern`
              - Class defining the complex conic pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRPattern`
              - Class defining the EOIR pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorUnknownPattern`
              - Unsupported/unknown sensor pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection`
              - Class defining the band collection for an EOIR Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBand`
              - Class defining an EOIR band.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRRadiometricPair`
              - Class defining an Sensitivities item.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection`
              - Class defining the Sensitivities collection for an EOIR Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection`
              - Class defining the Saturations collection for an EOIR Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorCustomPattern`
              - Class defining the custom pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorHalfPowerPattern`
              - Class defining the half-power pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorRectangularPattern`
              - Class defining the rectangular pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorSARPattern`
              - Class defining the Synthetic Aperture Radar (SAR) pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorSimpleConicPattern`
              - Class defining the simple conic pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingFixed`
              - Class defining the fixed pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingFixedAxes`
              - Class defining the fixed in axes pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointing3DModel`
              - Class defining the 3D model pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingSpinning`
              - Class defining the spinning pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargeted`
              - Class defining the targeted pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingExternal`
              - Class defining the external file-defined pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack`
              - Class defining a targeted sensor with tracking boresight.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightFixed`
              - Class defining a targeted Sensor with fixed boresight.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorTargetCollection`
              - Class defining the target collection for a target-pointing Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorTarget`
              - Class defining a Sensor target.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTime`
              - Class for defining Sensor target times in terms of access.

            * - :py:class:`~ansys.stk.core.stkobjects.ScheduleTime`
              - Class for defining Sensor target times in terms of a specified schedule.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAzElMaskFile`
              - Class to define a Sensor's Azimuth-Elevation mask.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics`
              - Class defining the 2D Graphics properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjection`
              - Class defining the projection properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionDisplayDistance`
              - Class defining projection altitude options for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3D`
              - Class defining 3D Graphics properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse`
              - Class defining 3D pulse properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset`
              - Class defining 3D Graphics vertex offset properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintTimeSlipRange`
              - Class for controlling the use the Time Slip constraint for a missile or launch vehicle, used with the Close Approach Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintBackground`
              - Class related to the Background constraint, which constrains access periods based on whether the Earth is or is not in the background.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintGroundTrack`
              - Class related to the Ground Track constraint, which constrains access to the Ascending or Descending side of the Satellite's ground track.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintMinMax`
              - Class related to defining constraints in terms of minimum and/or maximum values.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCrdnConstellation`
              - Class related to Vector constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction`
              - Class defining constraints in terms of obstruction by a specified central body.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAngle`
              - Class defining Angle constraints, limiting access to intervals during which the selected angle is within the specified minimum and maximum limits.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCondition`
              - Class defining access constraints in terms of lighting conditions.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTimeCollection`
              - Collection of access times.

            * - :py:class:`~ansys.stk.core.stkobjects.ScheduleTimeCollection`
              - Collection of user-scheduled access times.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintIntervals`
              - Class defining the Intervals constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle`
              - Class defining the Object Exclusion Angle constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintZone`
              - Class defining the Exclusion Zone constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody`
              - Do not use this class, as it is deprecated. Use AgAccessCnstrCbObstruction instead. Class defining Central Body Obstruction constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection`
              - Collection of Exclusion Zones used in Exclusion Zone constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintGrazingAltitude`
              - Class defining the Grazing Altidude constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingGrazingAltitude`
              - Class defining Grazing Altitude pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTarget`
              - Class defining the AreaTarget object.

            * - :py:class:`~ansys.stk.core.stkobjects.Facility`
              - Class defining the Facility object.

            * - :py:class:`~ansys.stk.core.stkobjects.Target`
              - Class defining the Target object.

            * - :py:class:`~ansys.stk.core.stkobjects.Place`
              - Class defining the Place object.

            * - :py:class:`~ansys.stk.core.stkobjects.Planet`
              - Class defining the Planet object.

            * - :py:class:`~ansys.stk.core.stkobjects.Sensor`
              - Class defining the Sensor class.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorCommonTasks`
              - Class defining the Sensor Common class.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTargetCommonTasks`
              - Class defining the Area Target Common class.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetCommonTasks`
              - Class defining the Planet Common class.

            * - :py:class:`~ansys.stk.core.stkobjects.Swath`
              - Class defining Swath properties.

            * - :py:class:`~ansys.stk.core.stkobjects.Star`
              - Class defining the Star object.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderCollection`
              - Collection of data providers attached to the current STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResult`
              - Results returned by the data provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultSubSectionCollection`
              - Represents a collection of subsections returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultSubSection`
              - Represents a subsection in the data returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultIntervalCollection`
              - Represents a collection of intervals returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultInterval`
              - Represents a interval in the collection of intervals returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection`
              - Represents a collection of datasets in the interval returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultDataSet`
              - Represents a dataset in the collection of datasets returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderFixed`
              - Support for fixed data providers (i.e. non time-dependent like Facility position).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderTimeVarying`
              - Support for time-dependent data providers (e.g. Satellite position).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderInterval`
              - Support for interval data providers (e.g. Facility lighting times).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage`
              - Notification or failure messages returned by the data provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderGroup`
              - Group of sub data providers (e.g. ``Cartesian Position`` on Satellites).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderElements`
              - Elements returned by the data provider (e.g. ``x``, ``y``, ``z``).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderElement`
              - Class defining a data provider element.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviders`
              - Class defining data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.StkAccess`
              - Class defining Access.

            * - :py:class:`~ansys.stk.core.stkobjects.StkAccessGraphics`
              - Class defining 2D Graphics for Access.

            * - :py:class:`~ansys.stk.core.stkobjects.StkAccessAdvanced`
              - Class defining advanced Access settings.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTimeEventIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.StkObjectCoverage`
              - Class defining object coverage.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit`
              - Class defining the fom on the coverage object tool.

            * - :py:class:`~ansys.stk.core.stkobjects.Scenario3dFont`
              - Font properties for Scenario 3D Graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DBorderWall`
              - Class defining 3D Graphics border wall properties.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection`
              - Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolVector`
              - Class defining a reference vector (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolAxes`
              - Class defining a set of reference axes (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolAngle`
              - Class defining a reference angle (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPlane`
              - Class defining a reference plane (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolPoint`
              - Class defining a reference point (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.TargetGraphics`
              - Class defining 2D Graphics for a Target object.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetGraphics3D`
              - Class defining 3D Graphics for a Target object.

            * - :py:class:`~ansys.stk.core.stkobjects.PointTargetGraphics3DModel`
              - Point properties for a 3D model.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectLinkCollection`
              - Collection of names of STK objects that are available in the current Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectLink`
              - Class defining name of an STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.LinkToObject`
              - Class defining a link to an STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.LLAPosition`
              - Class defining position defined in terms of latitude, longitude and altitude (LLA).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement`
              - Class defining 3D Graphics data display element.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection`
              - Collection of 3D Graphics data display text.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInitialState`
              - Class defining the initial state of the vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity`
              - Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRadiationPressure`
              - Class defining solar radiation pressure on a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure`
              - Class defining HPOP solar radiation pressure properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeEnterManually`
              - Class defining the option to enter a vehicle's solar flux and/or GeoMag properties manually, depending on the selected atmospheric density model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSolarFluxGeoMagnitudeUseFile`
              - Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag`
              - Class defining the HPOP atmospheric drag model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions`
              - Class defining HPOP atmospheric drag options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureOptions`
              - Class defining HPOP solar radiation pressure options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleStatic`
              - Class defining static force model options for the HPOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSolidTides`
              - Class defining the contribution of solid tides.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleOceanTides`
              - Class defining the contribution of ocean tides.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePluginSettings`
              - Class defining force model plugin settings for HPOP.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePluginPropagator`
              - Class defining a propagator plugin for HPOP for customization of the accelerations used in the propagation of the satellite trajectory.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelMoreOptions`
              - Class defining additional force model options for HPOP.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel`
              - Class defining HPOP force models.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleStepSizeControl`
              - Class defining step size control for the HPOP integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTimeRegularization`
              - Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInterpolation`
              - Class defining interpolation for the HPOP integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleIntegrator`
              - Class defining the HPOP integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGravity`
              - Class defining gravity modeling options for a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePositionVelocityElement`
              - Class defining position and velocity elements for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePositionVelocityCollection`
              - Collection of position and velocity elements for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCorrelationListCollection`
              - Collection representing HPOP covariance matrix.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCorrelationListElement`
              - Class representing an element of an HPOP covariance matrix.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCovariance`
              - Class defining HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleJxInitialState`
              - Class defining initial state for the J2/4 propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity`
              - Class defining gravity options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleThirdBodyGravityElement`
              - Class defining third-body gravity options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleThirdBodyGravityCollection`
              - Collection of third-body gravity options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleExpDensModelParams`
              - Class defining the Exponential atmospheric density model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAdvanced`
              - Class defining advanced atmospheric density options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPForceModelDrag`
              - Class defining the atmospheric drag model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure`
              - Class defining the solar radiation pressure model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePhysicalData`
              - Class defining physical data for the LOP force model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPForceModel`
              - Class defining the force model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSegmentsCollection`
              - Collection of segments for a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP`
              - Class defining the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorJ2Perturbation`
              - Class defining the J2 perturbation propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorJ4Perturbation`
              - Class defining the J4 perturbation propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorLOP`
              - Class defining the Long-term Orbit Predictor (LOP).

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4`
              - Class defining the SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE`
              - Class defining the SPICE propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorStkExternal`
              - Class defining the STK External propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorTwoBody`
              - Class defining the two body propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal`
              - Class defining the user-external propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState`
              - Class defining launch vehicle initial state.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent`
              - Class defining the simple ascent propagator for a launch vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointsElement`
              - Class defining a waypoint for a Great Arc vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection`
              - Collection of waypoints for a Great Arc vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchLLA`
              - Class defining geodetic launch latitude, longitude and altitude for a Missile or LaunchVehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchLLR`
              - Class defining geocentric launch latitude, longitude and radius for a Missile or LaunchVehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLLA`
              - Class defining geodetic impact latitude, longitude and altitude for a Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLLR`
              - Class defining geocentric impact latitude, longitude and radius for a Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchControlFixedApogeeAltitude`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed apogee altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchControlFixedDeltaV`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchControlFixedDeltaVMinEccentricity`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V with minimum eccentricity.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchControlFixedTimeOfFlight`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed time of flight.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl`
              - Class defining the option to use azimuth and elevation to specify the Missile's impact location.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint`
              - Class defining a Missile's impact location.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorBallistic`
              - Class defining the ballistic propagator for a Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorGreatArc`
              - Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4SegmentCollection`
              - Set of Trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4Segment`
              - SGP4 propagator segment.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleThirdBodyGravity`
              - Third body gravity options for Long-range Orbit Predictor (LOP) propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection`
              - The Consider Analysis list for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSPICESegment`
              - SPICE propagator segment.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain`
              - Terrain altitude reference.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointAltitudeReference`
              - Altitude references.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4LoadFile`
              - SGP4 propagator. Allows the user to load segments from file.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4OnlineLoad`
              - SGP4 propagator. Allows the user to load segments from online.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4OnlineAutoLoad`
              - Do not use this class, as it is deprecated. Use AgVeSGP4OnlineLoad instead. SGP4 propagator. Allows the user to load the most current segment from online.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection`
              - List of Ground Ellipses.

            * - :py:class:`~ansys.stk.core.stkobjects.Satellite`
              - Satellite properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInertia`
              - Satellite inertia matrix parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleMassProperties`
              - Satellite Mass properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleDefinition`
              - Pass break definition properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePassNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePassNumberingFirstPassNum`
              - First pass number.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePassBreak`
              - Satellite Pass Break properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCentralBodies`
              - Satellite Central Bodies.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement`
              - Ground ellipse data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGroundEllipseElement`
              - Ground ellipse.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteGraphics3DModel`
              - All Satellite's VO Model properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEclipseBodies`
              - Satellite Eclipse Bodies, for defining the eclipse central body list used for lighting computations.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleVector`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRateOffset`
              - AgVeSpin Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileConstraintOffset`
              - Constraint offset for various attitude profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX`
              - Shared for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileSpinning`
              - Spinning attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileAlignmentOffset`
              - Alignment offset for various attitude profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleScheduleTimesCollection`
              - List of scheduled accesses.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleDuration`
              - Look ahead and look behind duration options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleStandardBasic`
              - Basic attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal`
              - External attitude (.a) file.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTime`
              - Real time attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeTrendControlAviator`
              - Trending controls for Aviator attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileAviator`
              - The profile used for Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetPointingCollection`
              - List of Attitude Targets.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTorque`
              - Torque file to use in defining integrated attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude`
              - Integrated Attitude generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard`
              - Standard attitude profile for launch vehicle or missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard`
              - Standard attitude profile for satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRouteAttitudeStandard`
              - Standard attitude profile for aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting`
              - Lighting.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationGroundElevation`
              - Ground elevation for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationSwathHalfWidth`
              - Half width for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath`
              - Vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadDataFraction`
              - 2D Graphics pass: fraction of leading portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadDataTime`
              - 2D Graphics pass: time-defined segment of leading portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrailDataFraction`
              - 2D Graphics pass: fraction of trailing portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrailDataTime`
              - 2D Graphics pass: time-defined segment of trailing portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData`
              - AgVeGfxPassData Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses`
              - Settings for satellite pass display graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevContours`
              - General settings regarding display of elevation contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsElement`
              - Pointable elements for 3D model pointing.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox`
              - Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DRouteProximity`
              - Proximity graphics for GreatArc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity`
              - Proximity graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DElevContours`
              - 3D elevation angle contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSAA`
              - 3D South Atlantic Anomaly contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSigmaScaleProbability`
              - Sigma probability for indirect sizing of covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSigmaScaleScale`
              - Sigma scale for direct sizing of covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement`
              - Intervals graphics for covariance pointing contour.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsCollection`
              - List of Intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic`
              - Basic 3D graphics for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesIntervals`
              - 3D graphics based on intervals for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSize`
              - 3D graphics vector size.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour`
              - Covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDataFraction`
              - Fraction for 3D track display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDataTime`
              - Time.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitPassData`
              - Satellite 3D ground and orbit track data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTrackData`
              - 3D leading/trailing track data for satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTickDataLine`
              - Line type tick marks.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTickDataPoint`
              - Point type tick mark.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks`
              - Tick mark for satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DPass`
              - 3D pass for satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance`
              - 3D position covariance ellipsoids.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance`
              - 3D velocity covariance ellipsoids.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryProximity`
              - AgVeTrajectoryProximity Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectory`
              - AgLvVOTrajectory Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryTrackData`
              - 3D leading/trailing track data for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryPassData`
              - 3D ground track and trajectory data for a launch vehicle or missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData`
              - AgLvVOTrajectory2 Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks`
              - Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersCollection`
              - Collection of Waypoint Markers .

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DRoute`
              - AgVeVORoute2 Class.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelPointing`
              - List of pointable model elements.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance`
              - Control the level of detail in labels and other screen objects at specified distances.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePositionItem`
              - Drop lines from the vehicle's current position.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem`
              - Drop lines at intervals along the vehicle's path.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection`
              - Collection of drop lines from the vehicle's orbit or trajectory.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitDropLines`
              - Droplines collections.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DRouteDropLines`
              - Droplines for great arc vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryDropLines`
              - Droplines for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTrajectoryGraphics3DModel`
              - Marker for launch vehicle or missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRouteGraphics3DModel`
              - 3D marker for great arc vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of IAgVeVOBPlaneTemplateDisplayCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate`
              - An element of IAgVeVOBPlaneTemplatesCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance`
              - An element in the IAgVeVOBPlanePointCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection`
              - AgVeVOBPlaneCollection Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicle`
              - Launch vehicle object.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicle`
              - Ground vehicle object.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicleGraphics3D`
              - AgGvVOVO Class.

            * - :py:class:`~ansys.stk.core.stkobjects.Missile`
              - Missile object.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileGraphics`
              - 2D Graphics for missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileGraphics3D`
              - 3D Graphics for missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.Aircraft`
              - Aircraft object.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.Ship`
              - Ship object.

            * - :py:class:`~ansys.stk.core.stkobjects.ShipGraphics`
              - 2D Graphics options for a ship.

            * - :py:class:`~ansys.stk.core.stkobjects.ShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoTrackPoint`
              - The points defined for the selected track.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoTrackPointCollection`
              - MTO track point list.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoTrack`
              - List of MTO tracks with basic information about each.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoTrackCollection`
              - MTO Track List.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoDefaultTrack`
              - Default MTO track.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGlobalTrackOptions`
              - Global MTO track options.

            * - :py:class:`~ansys.stk.core.stkobjects.Mto`
              - Multi-Track Object (MTO).

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DMarker`
              - Define the 2D graphics attributes of the selected MTO track or tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DLine`
              - MTO track line display options.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DFadeTimes`
              - MTO track fade times.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DLeadTrailTimes`
              - MTO track lead/trail times.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DTrack`
              - 2D graphics attributes for each track in the MTO.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoDefaultGraphics2DTrack`
              - 2D graphics attributes for default MTO tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics2DGlobalTrackOptions`
              - Global 2D graphics options for an MTO.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics`
              - MTO 2D Graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DMarker`
              - MTO 3D graphics marker options.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DPoint`
              - MTO track 3D marker point options.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DModel`
              - MTO track model options.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DSwapDistances`
              - MTO track 3D swap distances.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DDropLines`
              - MTO droplines.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DTrack`
              - 3D graphics properties for MTO tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoDefaultGraphics3DTrack`
              - 3D graphics properties for default MTO tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DGlobalTrackOptions`
              - Global 3D graphics MTO track options.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3D`
              - MTO 3D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.LLAGeocentric`
              - Geocentric LLA position.

            * - :py:class:`~ansys.stk.core.stkobjects.LLAGeodetic`
              - Geodetic LLA position.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetPoint`
              - Line Target Point.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetPointCollection`
              - The collection of points for the line target.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTarget`
              - Line Target Path properties.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetGraphics`
              - The AgLtGraphics class.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetGraphics3D`
              - The AgLtVO class.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageDefinition`
              - The AgCoverageDefinition class.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsCustomRegions`
              - Custom Regions.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLat`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLatLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLonLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLatLonRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGrid`
              - Grid Definition and resolution.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAssetListElement`
              - Coverage asset.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAssetListCollection`
              - Asset List.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageRegionFilesCollection`
              - Collection of Region Files.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection`
              - Collection of Area Targets.

            * - :py:class:`~ansys.stk.core.stkobjects.CoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoveragePointFileListCollection`
              - Point file list collection.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAdvanced`
              - Advanced Properties.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics3D`
              - AgCvVOStatic Class.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainTimePeriodBase`
              - Chain time period options.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConstraints`
              - Chain constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.Chain`
              - AgChain Class is used to access the methods and properties of the STK Chain Object.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConnection`
              - Class defining Chain connections.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConnectionCollection`
              - Class defining a collection of Chain connections.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainOptimalStrandOpts`
              - Class defining Chain optimal strand options.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics`
              - 2D graphics properties of a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod`
              - SCF Method.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataMinMax`
              - Minimum and maximum data values for navigation accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataMinAssets`
              - Minimum number of assets.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best 4 satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMerit`
              - Figure of Merit properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData`
              - System Age Of Data Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics`
              - AgFmGfxGraphics Class.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection`
              - Collection of Level Attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleProfileGPS`
              - GPS Attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.StkObjectModelContext`
              - AgStkObjectModelContext class provides methods to create instance of AgStkObjectRoot class.

            * - :py:class:`~ansys.stk.core.stkobjects.StdMilitary2525bSymbols`
              - AgStdMil2525bSymbols class provides methods to create 2525b symbols.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGridInspector`
              - AgCvGridInspector class provides methods to use the grid inspector tool for coverage definition.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector`
              - AgFmGridInspector class provides methods to use the grid inspector tool for FOM.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail`
              - Vapor trail attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintPluginMinMax`
              - Class related to defining access plugin constraints in terms of minimum and/or maximum values.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraints`
              - Class related to the constellation constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraintObjectRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraintRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~ansys.stk.core.stkobjects.Constellation`
              - Class represents the STK Constellation.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationGraphics`
              - 2D Graphics properties of the STK Constellation.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationRouting`
              - Routing properties of the STK Constellation.

            * - :py:class:`~ansys.stk.core.stkobjects.EventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :py:class:`~ansys.stk.core.stkobjects.EventDetectionSubSampling`
              - Event detection strategy involving subsampling.

            * - :py:class:`~ansys.stk.core.stkobjects.SamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :py:class:`~ansys.stk.core.stkobjects.SamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAccessAdvanced`
              - Sensor's advanced targeting access computation properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAccessAdvanced`
              - Vehicle advanced targeting access computation properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteExportTools`
              - The Satellite Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleExportTools`
              - The LaunchVehicle Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicleExportTools`
              - The GroundVehicle Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileExportTools`
              - The Missile Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftExportTools`
              - The Aircraft Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.ShipExportTools`
              - The Ship Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool`
              - AgVeEphemerisTypeCode500 Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool`
              - AgVeEphemerisTypeCCSDS Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool`
              - AgVeEphemerisTypeSTK Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisSpiceExportTool`
              - AgVeEphemerisTypeSpice Class.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolTimePeriod`
              - Specify Time Period.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool`
              - AgVeExternalFileAttitude Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagationDefinitionExportTool`
              - AgVeExternalFileAttitude Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCoordinateAxesCustom`
              - Custom.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolStepSize`
              - AgStepSize Class.

            * - :py:class:`~ansys.stk.core.stkobjects.PctCmpltEventArgs`
              - Represents a structure used by the Percent Complete events.

            * - :py:class:`~ansys.stk.core.stkobjects.StkObjectChangedEventArgs`
              - Contains information about the changes in the object's state.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies`
              - Eclipsing bodies.

            * - :py:class:`~ansys.stk.core.stkobjects.LocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :py:class:`~ansys.stk.core.stkobjects.TimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~ansys.stk.core.stkobjects.TimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :py:class:`~ansys.stk.core.stkobjects.SpatialState`
              - Represents a position and an attitude of an object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpatialInfo`
              - Represents a spatial information of the vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccess`
              - One Point Access.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessResult`
              - One Point Access Result.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessConstraint`
              - One Point Access Result.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorRealtime`
              - Realtime propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRealtimeCartesianPoints`
              - AgVeRealtimeCartesianPoint Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRealtimeLLAHPSPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRealtimeLLAPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :py:class:`~ansys.stk.core.stkobjects.SRPModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :py:class:`~ansys.stk.core.stkobjects.SRPModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :py:class:`~ansys.stk.core.stkobjects.SRPModelPlugin`
              - Plugin Light Reflection Model.

            * - :py:class:`~ansys.stk.core.stkobjects.SRPModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPSRPModel`
              - SRP Model Base CoClass.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModelSpherical`
              - Spherical Drag Pressure Model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModel`
              - HPOP Drag Model Base CoClass.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioAnimationTimePeriod`
              - Configure the scenario's animation time.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude`
              - Class defining projection altitude options for constant altitude for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionObjectAltitude`
              - Class defining projection altitude options for object altitude for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference`
              - Reference attitude profile for the incoming attitude data.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoAnalysis`
              - MTO Spatial State Info.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoAnalysisPosition`
              - MTO Position Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoAnalysisRange`
              - MTO Range Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoAnalysisFieldOfView`
              - MTO Field Of View Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoAnalysisVisibility`
              - MTO Visibility Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorGPS`
              - GPS propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.AvailableFeatures`
              - Class is used to check the availability of the features such as Astrogator, etc.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArgs`
              - Contains information about the changes in the object's state.

            * - :py:class:`~ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs`
              - Arguments for the OnStkObjectPreDelete event.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4CommonTasks`
              - Most commonly used functionality when working with SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdateProperties`
              - SGP4 AutoUpdate properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdateFileSource`
              - Configure the SGP4 automatic updates using file(s).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdateOnlineSource`
              - Configure the SGP4 automatic updates using online source (AGI server).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4AutoUpdate`
              - SGP4 AutoUpdate.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateProperties`
              - GPS AutoUpdate properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource`
              - GPS automatic updates using almanac file(s).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateOnlineSource`
              - GPS automatic updates using online source (AGI server).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdate`
              - GPS AutoUpdate.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSSpecifyAlmanac`
              - Specify a GPS almanac.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacProperties`
              - A common base for GPS almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSElement`
              - An element of the GPS element collection.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadEnergyMethodSpecify`
              - Set the electron and proton energies to consider.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadEnergyValues`
              - Energy values used by the Radiation Environment model.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment`
              - Radiation Environment model settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D`
              - Geomagnetic field graphics settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentScenarioExtGraphics3D`
              - 3D Graphics settings.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateElement`
              - Class defining dose rate information computed for a shielding thickness.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection`
              - Collection of dose rate elements computed for a shielding thickness.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentSAAContour`
              - SAA settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentVehTemperature`
              - Vehicle Temperature settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentParticleFlux`
              - Particle Flux settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagneticField`
              - Magnetic field settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadiation`
              - Radiation model settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for displaying magnetic field lines.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentGraphics`
              - Graphics settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGridPointSelection`
              - Represents a set of points selected with the grid inspector.

            * - :py:class:`~ansys.stk.core.stkobjects.CelestialBodyCollection`
              - Represents a collection of stars.

            * - :py:class:`~ansys.stk.core.stkobjects.CelestialBodyInfo`
              - Represents a celestial body information.

            * - :py:class:`~ansys.stk.core.stkobjects.StkCentralBodyEllipsoid`
              - Central body's ellipsoid information.

            * - :py:class:`~ansys.stk.core.stkobjects.StkCentralBody`
              - A central body coclass.

            * - :py:class:`~ansys.stk.core.stkobjects.StkCentralBodyCollection`
              - Central body collection coclass.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation`
              - Scalar Calculation Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptor`
              - 11-Param file definition.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagator11Param`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSP3File`
              - SP3 file data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisStkBinaryExportTool`
              - AgVeEphemerisTypeSTKBinary Class.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitState`
              - Class defining orbit state.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateCoordinateSystem`
              - Selection of coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateCartesian`
              - Cartesian coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalSizeShapeAltitude`
              - Orbit size and shape using altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalSizeShapeMeanMotion`
              - Orbit size and shape using Mean Motion and Eccentricity.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalSizeShapePeriod`
              - Orbit size and shape using Period and Eccentricity.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalSizeShapeRadius`
              - Orbit size and shape using Radius.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalSizeShapeSemimajorAxis`
              - Orbit size and shape using Semimajor Axis and Eccentricity.

            * - :py:class:`~ansys.stk.core.stkobjects.OrientationAscNodeLAN`
              - Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :py:class:`~ansys.stk.core.stkobjects.OrientationAscNodeRAAN`
              - Angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalOrientation`
              - Orbit orientation in the Classical (Keplerian) system.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationArgumentOfLatitude`
              - Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationEccentricAnomaly`
              - Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationMeanAnomaly`
              - Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationTimePastAN`
              - Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationTimePastPerigee`
              - Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationTrueAnomaly`
              - True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.GeodeticSizeAltitude`
              - Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :py:class:`~ansys.stk.core.stkobjects.GeodeticSizeRadius`
              - Radius and Radius Rate (for Geodetic coordinate type).

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateGeodetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayL`
              - Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayLOverSQRTmu`
              - Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayHOverSQRTmu`
              - Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayG`
              - Delaunay Variable G, the magnitude of the orbital angular momentum.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayGOverSQRTmu`
              - Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :py:class:`~ansys.stk.core.stkobjects.EquinoctialSizeShapeMeanMotion`
              - Mean Motion, an element of the Equinoctial coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.EquinoctialSizeShapeSemimajorAxis`
              - Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :py:class:`~ansys.stk.core.stkobjects.MixedSphericalFlightPathAngleHorizontal`
              - Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.MixedSphericalFlightPathAngleVertical`
              - Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.SphericalFlightPathAngleHorizontal`
              - Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.SphericalFlightPathAngleVertical`
              - Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :py:class:`~ansys.stk.core.stkobjects.StkPreferences`
              - Allow configuring STK preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.StkPreferencesVDF`
              - Allow configuring VDF preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeSlewFixedRate`
              - Fixed rate slew.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeSlewFixedTime`
              - Fixed time slew.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.MtoGraphics3DModelArtic`
              - Class defining MTO model articulations.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagatorAviator`
              - Class defining the Mission Modler propagator for an Aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSv2ExportTool`
              - The Ephemeris/Attitude Export Tool for CCSDSv2 Ephemeris type.

            * - :py:class:`~ansys.stk.core.stkobjects.StkPreferencesConnect`
              - Allow configuring connect preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.Antenna`
              - Class defining the antenna object.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModel`
              - Class defining a generic antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelOpticalSimple`
              - Class defining a simple optical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelOpticalGaussian`
              - Class defining a gaussian optical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGaussian`
              - Class defining a gaussian antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelParabolic`
              - Class defining a parabolic antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelSquareHorn`
              - Class defining a square horn antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelScriptPlugin`
              - Class defining a script plguin antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelExternal`
              - Class defining a external antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGimroc`
              - Class defining a GIMROC antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelRemcomUanFormat`
              - Class defining an antenna pattern Remcom uan model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat`
              - Class defining an antenna pattern ANSYS ffd model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelTicraGRASPFormat`
              - Class defining an antenna pattern Ticra GRASP model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelElevationAzimuthCuts`
              - Class defining a pattern elevation/azimuth cuts antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelIeee1979`
              - Class defining a IEEE 1979 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelDipole`
              - Class defining a dipole antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelHelix`
              - Class defining a helix antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelCosecantSquared`
              - Class defining a cosecant squared antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelHemispherical`
              - Class defining a hemispherical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelPencilBeam`
              - Class defining a pencil beam antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray`
              - Class defining a phased array antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray`
              - Class defining an HFSS EEP array antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelIsotropic`
              - Class defining a isotropic antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelIntelSat`
              - Class defining a IntelSat antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGpsGlobal`
              - Class defining a GPS global antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGpsFrpa`
              - Class defining a GPS FRPA antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuBO1213CoPolar`
              - Class defining a ITU-R BO1213 co-polar antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuBO1213CrossPolar`
              - Class defining a ITU-R BO1213 cross-polar antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuF1245`
              - Class defining a ITU-R F1245-3 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS580`
              - Class defining a ITU-R S580-6 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS465`
              - Class defining a ITU-R S465-6 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS731`
              - Class defining a ITU-R S731 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS1528R12Circular`
              - Class defining a ITU-R S1528 1.2 circular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS1528R13`
              - Class defining a ITU-R S1528 1.3 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS672Circular`
              - Class defining a ITU-R S672 circular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS1528R12Rectangular`
              - Class defining a ITU-R S1528 1.2 rectangular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelItuS672Rectangular`
              - Class defining a ITU-R S672-4 rectangular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosine`
              - Class defining a circular cosine aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform`
              - Class defining a circular uniform aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosineSquared`
              - Class defining a circular cosine squared aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBessel`
              - Class defining a circular bessel aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope`
              - Class defining a circular bessel envelope aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal`
              - Class defining a circular cosine pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosineSquaredPedestal`
              - Class defining a circular cosine squared pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularSincIntPower`
              - Class defining a circular sinc integer power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularSincRealPower`
              - Class defining a circular sinc real power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosine`
              - Class defining a rectangular cosine aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosinePedestal`
              - Class defining a rectangular cosine pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal`
              - Class defining a rectangular cosine squared pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularSincIntPower`
              - Class defining a rectangular sinc integer power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularSincRealPower`
              - Class defining a rectangular sinc real power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquared`
              - Class defining a rectangular cosine squared aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularUniform`
              - Class defining a rectangular uniform aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelRectangularPattern`
              - Class defining a rectangular pattern antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaControl`
              - Class defining the properties for a antenna control.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaGraphics3D`
              - Class defining 3D Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics`
              - Class defining 3D Volume Graphics properties of radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics3D`
              - Class defining 3D Graphics properties of radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics`
              - Class defining graphics properties of radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics`
              - Class defining 3D Volume Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourGraphics`
              - Class defining contour Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaGraphics`
              - Class defining 2D Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionContourLevelCollection`
              - Class defining a collection of radar cross section contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionContourLevel`
              - Class defining an radar cross section contour level.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeLevelCollection`
              - Class defining a collection of radar cross section volume levels.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeLevel`
              - Class defining an radar cross section volume level.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection`
              - Class defining a collection of antenna volume levels.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaVolumeLevel`
              - Class defining an antenna volume level.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourLevelCollection`
              - Class defining a collection of antenna contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourLevel`
              - Class defining an antenna contour level.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourGain`
              - Class defining an antenna gain contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourEirp`
              - Class defining an antenna eirp contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourRip`
              - Class defining an antenna rip contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourFluxDensity`
              - Class defining an antenna flux density contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity`
              - Class defining an antenna spectral flux density contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.Transmitter`
              - Class defining the transmitter object.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModel`
              - Class defining a generic transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelScriptPluginRF`
              - Class defining a RF script plugin transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelScriptPluginLaser`
              - Class defining a laser script plugin transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelCable`
              - Class defining a cable transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelSimple`
              - Class defining a simple transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelMedium`
              - Class defining a medium transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelComplex`
              - Class defining a complex transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam`
              - Class defining a multibeam transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelLaser`
              - Class defining a laser transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple`
              - Class defining a simple re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium`
              - Class defining a medium re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex`
              - Class defining a complex re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterGraphics3D`
              - Class defining 3D Graphics properties of a Transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterGraphics`
              - Class defining 2D Graphics properties of a Transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.Receiver`
              - Class defining the receiver object.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModel`
              - Class defining a generic receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelCable`
              - Class defining a cable receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelSimple`
              - Class defining a simple receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelMedium`
              - Class defining a medium receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelComplex`
              - Class defining a complex receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelMultibeam`
              - Class defining a mutibeam receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelLaser`
              - Class defining a laser receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelScriptPluginRF`
              - Class defining a RF script plugin receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelScriptPluginLaser`
              - Class defining a laser script plugin receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverGraphics3D`
              - Class defining 3D Graphics properties of a Receiver.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverGraphics`
              - Class defining 2D Graphics properties of a Receiver.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarDopplerClutterFilters`
              - Class defining the properties for doppler clutter filters.

            * - :py:class:`~ansys.stk.core.stkobjects.Waveform`
              - Class defining a waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformRectangular`
              - Class defining a rectangular waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformPulseDefinition`
              - Class defining the pulse definition for a rectangular waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMultifunctionWaveformStrategySettings`
              - Class defining the waveform selection strategy settings.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategy`
              - Class defining the waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategyFixed`
              - Class defining the waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategyRangeLimits`
              - Class defining the range limits waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.Radar`
              - Class defining the radar object.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModel`
              - Class defining a generic radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelMonostatic`
              - Class defining a monostatic radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelMultifunction`
              - Class defining a multifunction radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter`
              - Class defining a bistatic transmitter radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver`
              - Class defining a bistatic receiver radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarGraphics3D`
              - Class defining 3D Graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarGraphics`
              - Class defining 2D Graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarAccessGraphics`
              - Class defining access graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMultipathGraphics`
              - Class defining multipath graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeMonostatic`
              - Class defining a monostatic radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack`
              - Class defining a monostatic search/track radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeMonostaticSar`
              - Class defining a monostatic sar radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitter`
              - Class defining a bistatic transmitter radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack`
              - Class defining a bistatic transmitter search/track radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSar`
              - Class defining a bistatic transmitter sar radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiver`
              - Class defining a bistatic receiver radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack`
              - Class defining a bistatic receiver search/track radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSar`
              - Class defining a bistatic receiver sar radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous`
              - Class defining a monostatic continuous waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF`
              - Class defining a monostatic fixed PRF waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMultifunctionDetectionProcessing`
              - Class defining multifunction radar detection processing.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Class defining a bistatic transmitter continuous waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Class defining a bistatic transmitter fixed PRF waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous`
              - Class defining a bistatic receiver continuous waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Class defining a bistatic receiver fixed PRF waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSearchTrackPulseDefinition`
              - Class defining the pulse definition for a search track waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModulator`
              - Class defining a radar modulator.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetection`
              - Class defining the probability of detection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionCFAR`
              - Class defining the probability of detection cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionNonCFAR`
              - Class defining the non CFAR probability of detection cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionPlugin`
              - Class defining the probability of detection plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionCFARCellAveraging`
              - Class defining the probability of detection cell averaging cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionCFAROrderedStatistics`
              - Class defining the probability of detection ordered statistics cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarPulseIntegrationGoalSNR`
              - Class defining the goal SNR integration method.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarPulseIntegrationFixedNumberOfPulses`
              - Class defining the fixed number of pulses integration method.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarContinuousWaveAnalysisModeGoalSNR`
              - Class defining the continuous wave goal SNR analysis mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarContinuousWaveAnalysisModeFixedTime`
              - Class defining the continuous wave fixed time analysis mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition`
              - Class defining the pulse definition for a SAR waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseIntegration`
              - Class defining the pulse integration for a SAR waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarTransmitter`
              - Class defining the radar transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction`
              - Class defining the multifunction radar transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarReceiver`
              - Class defining the radar transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.AdditionalGainLoss`
              - Class defining additional gains and losses.

            * - :py:class:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection`
              - Class defining a collection of additional gains and losses.

            * - :py:class:`~ansys.stk.core.stkobjects.Polarization`
              - Class defining an polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationLHC`
              - Class defining a LHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationRHC`
              - Class defining a RHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationLHC`
              - Class defining a LHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationRHC`
              - Class defining a RHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationVertical`
              - Class defining a vertical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationVertical`
              - Class defining a receive vertical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarClutter`
              - Class defining a radar clutter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarClutterGeometry`
              - Class defining a radar clutter geometry.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollectionElement`
              - Class defining a scattering point provider collection element.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection`
              - Class defining an scattering point provider collection.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderList`
              - Class defining a scattering point provider list.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProvider`
              - Class defining a scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderSinglePoint`
              - Class defining a single point scattring point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointCollectionElement`
              - Class defining a scattering point collection element.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointCollection`
              - Class defining a collection of scattering points.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile`
              - Class defining a scattring point provider where the points are defined in an ascii text file.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderRangeOverCFARCells`
              - Class defining a range over CFAR cells scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderSmoothOblateEarth`
              - Class defining a smooth oblate earth scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderPlugin`
              - Class defining a plugin scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.CRPluginConfiguration`
              - Class defining plugin configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarJamming`
              - Class defining radar jamming.

            * - :py:class:`~ansys.stk.core.stkobjects.RFInterference`
              - Class defining radar jamming.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModel`
              - Class defining a generic RF filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelBessel`
              - Class defining a bessel filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelSincEnvSinc`
              - Class defining a Sinc Envelope Sinc filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelElliptic`
              - Class defining a elliptic filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelChebyshev`
              - Class defining a Chebyshev filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelCosineWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelGaussianWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelHammingWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelButterworth`
              - Class defining a butterworth filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelExternal`
              - Class defining a external filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelScriptPlugin`
              - Class defining a script plugin filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelSinc`
              - Class defining a sinc filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRaisedCosine`
              - Class defining a raised cosine filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRootRaisedCosine`
              - Class defining a root raised cosine filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRcLowPass`
              - Class defining a rc low pass filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRectangular`
              - Class defining a rectangular filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelFirBoxCar`
              - Class defining a FIR box car filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelIir`
              - Class defining a IIR box car filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelFir`
              - Class defining a FIR filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.SystemNoiseTemperature`
              - Class defining system noise temperature.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature`
              - Class defining antenna noise temperature.

            * - :py:class:`~ansys.stk.core.stkobjects.Atmosphere`
              - Class defining local atmosphere.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserPropagationLossModels`
              - Class defining the properties for laser propagatoin models.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModel`
              - Class defining an laser propagation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Class defining an laser propagation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModtranLookupTablePropagationModel`
              - Class defining an MODTRAN-based lookup table propagation model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModtranPropagationModel`
              - Class defining a MODTRAN propagation model.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModel`
              - Class defining an laser tropospheric scintillation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModel`
              - Class defining a atmospheric turbulence model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModelConstant`
              - Class defining a constant atmospheric turbulence model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModelHufnagelValley`
              - Class defining a Hufnagel Valley atmospheric turbulence model.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814`
              - Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModel`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelITURP676_9`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelVoacap`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelTirem320`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelTirem331`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelTirem550`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelSimpleSatcom`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelScriptPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelCOMPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModel`
              - Class defining a scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelPlugin`
              - Class defining a plugin scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelConstantCoefficient`
              - Class defining a constant coefficient scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelWindTurbine`
              - Class defining a wind turbine scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSection`
              - Class defining a radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionModel`
              - Class defining a radar cross section model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable`
              - Class defining a inheritable radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand`
              - Class defining a inheritable radar cross section frequency band.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection`
              - Class defining a inheritable radar cross section frequency band collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategy`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyConstantValue`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyScriptPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyExternalFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyAnsysCsvFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.CustomPropagationModel`
              - Class defining a custom propatation model.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagationChannel`
              - Class defining the propagation channel.

            * - :py:class:`~ansys.stk.core.stkobjects.RFEnvironment`
              - Class defining the RF environment.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectRFEnvironment`
              - Class defining the RF environment for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectLaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.PlatformLaserEnvironment`
              - Class defining the laser environment for an platform.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModel`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelITURP618_12`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelITURP618_13`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelITURP618_10`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelCrane1985`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelCrane1982`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelCCIR1983`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelScriptPlugin`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModel`
              - Class defining a clouds and fog fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840_6`
              - Class defining a clouds and fog Loss ITU-R P.840-6 model.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840_7`
              - Class defining a clouds and fog Loss ITU-R P.840-7 model.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModel`
              - Class defining a tropospheric scintillation fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_8`
              - Class defining a tropospheric scintillation fading loss P.618-8 model.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12`
              - Class defining a tropospheric scintillation fading loss P.618-12 model.

            * - :py:class:`~ansys.stk.core.stkobjects.IonosphericFadingLossModel`
              - Class defining a Ionospheric fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IonosphericFadingLossModelP531_13`
              - Class defining a Ionospheric fading loss P.531-13 model.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModel`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModelTwoRay`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModelWirelessInSite64`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.WirelessInSite64GeometryData`
              - Class defining the REMCOM Wireless InSite 64 geometry data.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategy`
              - Class defining a pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategyFixed`
              - Class defining a fixed pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategySpinning`
              - Class defining a spinning pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategyTargeted`
              - Class defining a targeted pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.CRLocation`
              - Class defining a location.

            * - :py:class:`~ansys.stk.core.stkobjects.CRComplex`
              - Class defining a complex number.

            * - :py:class:`~ansys.stk.core.stkobjects.CRComplexCollection`
              - Class defining a collection of complex numbers.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModel`
              - Class defining a modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelBpsk`
              - Class defining a BPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQpsk`
              - Class defining a QPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQam16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQam32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQam64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQam128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQam256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQam1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModel8psk`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModel16psk`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelMsk`
              - Class defining a MSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelBoc`
              - Class defining a BOC modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelDpsk`
              - Class defining a DPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelFsk`
              - Class defining a FSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelNfsk`
              - Class defining a NFSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelOqpsk`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelScriptPluginCustomPsd`
              - Class defining a custom PSD script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelScriptPluginIdealPsd`
              - Class defining a ideal PSD script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.LinkMargin`
              - Class defining a link margin computation object.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModel`
              - Class defining a demodulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelBpsk`
              - Class defining a BPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQpsk`
              - Class defining a QPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQam16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQam32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQam64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQam128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQam256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQam1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModel8psk`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModel16psk`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelMsk`
              - Class defining a MSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelBoc`
              - Class defining a BOC modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelDpsk`
              - Class defining a DPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelFsk`
              - Class defining a FSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelNfsk`
              - Class defining a NFSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelOqpsk`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelScriptPlugin`
              - Class defining a script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionPolynomialCollection`
              - Class defining a collection of polynomial coefficients.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTableRow`
              - Class defining a row of an input back off vs C/Im table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffCOverImTable`
              - Class defining an input back off vs C/Im table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTableRow`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable`
              - Class defining an input back off vs output back off table.

            * - :py:class:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayer`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection`
              - Class defining collection of Beer-Bouguer-Lamber Law atmosphere layers.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivity`
              - Class defining radar activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityAlwaysActive`
              - Class defining radar always active activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityAlwaysInactive`
              - Class defining radar always active inactivity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeComponentListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeComponentListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeComponentList`
              - Class defining a radar time component list activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalList`
              - Class defining a radar time component list activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarAntennaBeam`
              - Class defining a radar antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaSystem`
              - Class defining an antenna system.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeam`
              - Class defining an antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamTransmit`
              - Class defining a transmit antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamCollection`
              - Class defining an antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategy`
              - Class defining a beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyAggregate`
              - Class defining a aggregated beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyMaxGain`
              - Class defining a maximum gain beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyMinBoresightAngle`
              - Class defining a minimum boresight angle beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyScriptPlugin`
              - Class defining a script plugin beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystem`
              - Class defining a CommSystem object.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemGraphics`
              - Class defining 2D Graphics properties of a CommSystem.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemGraphics3D`
              - Class defining 3D Graphics properties of a CommSystem.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessOptions`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetection`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSamplesOnly`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethod`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteria`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaMinimumRange`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaMaximumElevation`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaScriptPlugin`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentDirectory`
              - Manages all components.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentInfo`
              - Class defining a component.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentInfoCollection`
              - The collection of components and component folders.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentAttrLinkEmbedControl`
              - Attribute based component link/embed control.

            * - :py:class:`~ansys.stk.core.stkobjects.Volumetric`
              - The AgVolumetric class.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGridSpatialCalculation`
              - Class defining the volume grid spatial calculation.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricExternalFile`
              - Class defining the volume external file.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricAnalysisInterval`
              - Class defining the volumetric analysis interval.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricAdvanced`
              - Class defining the volumetric Computed Data Save options.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3D`
              - Class defining 3D graphics properties of volumetric object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DGrid`
              - Class defining grid properties of 3D graphics for volumetric object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSection`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlane`
              - Class defining cross-section plane for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection`
              - Class defining collection of cross-section planes for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DVolume`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DActiveGridPoints`
              - Class defining Active Grid Points for Volumetric Object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevels`
              - Class defining Spatial Calculation Levels for Volumetric Object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevel`
              - Class defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection`
              - Class defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DLegend`
              - Class defining Boundary/Fill legend for volumetric object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricExportTool`
              - The Volumetric Export Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteCollection`
              - The AgSatelliteCollection class.

            * - :py:class:`~ansys.stk.core.stkobjects.Subset`
              - The AgSubset class.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfiguration`
              - Class defining an element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationCircular`
              - Class defining a circular element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationLinear`
              - Class defining a linear element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationAsciiFile`
              - Class defining a ascii file element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile`
              - Class defining an HFSS EEP file element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationPolygon`
              - Class defining a polygon element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationHexagon`
              - Class defining a hexagon element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarActivityConfiguration`
              - Class defining a solar activity configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarActivityConfigurationSunspotNumber`
              - Class defining sunspot number configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarActivityConfigurationSolarFlux`
              - Class defining the solar flux configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.Beamformer`
              - Class defining a beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerAsciiFile`
              - Class defining a beamformer ascii file.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerMvdr`
              - Class defining a beamformer mvdr.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerUniform`
              - Class defining a uniform tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerBlackmanHarris`
              - Class defining a Blackman-Harris tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerCosine`
              - Class defining a cosine tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerCosineX`
              - Class defining a cosine^X tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerCustomTaperFile`
              - Class defining a custom taper file beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerDolphChebyshev`
              - Class defining a Dolph-Chebyshev tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerHamming`
              - Class defining a Hamming tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerHann`
              - Class defining a Hann tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerRaisedCosine`
              - Class defining a raised cosine tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerRaisedCosineSquared`
              - Class defining a raised cosine squared tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerScript`
              - Class defining a beamformer script plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProvider`
              - Class defining a direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderAsciiFile`
              - Class defining an ascii file direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderObject`
              - Class defining an object direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderLink`
              - Class defining an link direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderScript`
              - Class defining an script plugin direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.Element`
              - Class defining a phased array element.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementCollection`
              - Class defining a phased array element collection.

            * - :py:class:`~ansys.stk.core.stkobjects.KeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuation`
              - Class defining an radar stc.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuationDecayFactor`
              - Class defining an radar decay factor stc.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuationDecaySlope`
              - Class defining an radar decay slope stc.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuationMapRange`
              - Class defining an radar stc range map.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuationMapAzimuthRange`
              - Class defining an radar stc azimuth-range map.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuationMapElevationRange`
              - Class defining an radar stc elevation-range map.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarStcAttenuationPlugin`
              - Class defining an radar stc Com Plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingAlongVector`
              - Class defining the along vector pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingSchedule`
              - Allow to schedule a sensor to point at a specific location at a specific time.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection`
              - Collection of Analysis Workbench constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbench`
              - Class related to Analysis Workbench constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DArticulationFile`
              - Class defining the vo articulation file.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultStatisticResult`
              - Results returned by statistics computation.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult`
              - Results returned by time varying extremum computation.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultStatistics`
              - Class used to compute statistics and time varying extremum on data provider result data sets.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelGltfImageBased`
              - Class defining glTF Reflection Settings.

            * - :py:class:`~ansys.stk.core.stkobjects.StkObjectCutCopyPasteEventArgs`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

            * - :py:class:`~ansys.stk.core.stkobjects.StkPreferencesPythonPlugins`
              - Allow configuring Python plugin preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.PathCollection`
              - Allow adding and removing of paths.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCAT`
              - AdvCAT properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection`
              - Read-only collection of available objects.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATChosenObject`
              - A chosen object.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection`
              - The chosen object collection.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATPreFilters`
              - AdvCAT pre-filters properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATAdvancedEllipsoid`
              - AdvCAT advanced ellipsoid properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATAdvanced`
              - AdvCAT advanced properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeObject`
              - Represents a generic shape object.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeBox`
              - Box shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCone`
              - Cone shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCylinder`
              - Cylinder shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapePlate`
              - Plate shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeSphere`
              - Sphere shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCoupler`
              - Coupler shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeNone`
              - None shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeGEOComm`
              - GEOComm shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeLEOComm`
              - LEOComm shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeLEOImaging`
              - LEOImaging shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCustomMesh`
              - CustomMesh shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeTargetSignature`
              - TargetSignature shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRStagePlume`
              - Plume shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShape`
              - AgEOIRShape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCollection`
              - Collection of shapes.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRMaterialElement`
              - AgEOIRMaterialElement class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRMaterialElementCollection`
              - Collection of material elements.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRStage`
              - Stage base class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIR`
              - AgEOIR interface class.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileEOIR`
              - AgMsEOIR interface class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEOIR`
              - AgVeEOIR interface class.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.CONSTANTS`
              - AgEConstants contains base IDs for various structures.

            * - :py:class:`~ansys.stk.core.stkobjects.HELP_CONTEXT_IDS`
              - Help context IDs.

            * - :py:class:`~ansys.stk.core.stkobjects.ERROR_CODES`
              - Error codes.

            * - :py:class:`~ansys.stk.core.stkobjects.ABERRATION_TYPE`
              - The model of aberration to be used in access computations.

            * - :py:class:`~ansys.stk.core.stkobjects.ANIMATION_MODES`
              - Animation modes.

            * - :py:class:`~ansys.stk.core.stkobjects.ANIMATION_OPTIONS`
              - Animation Options.

            * - :py:class:`~ansys.stk.core.stkobjects.ANIMATION_ACTIONS`
              - Animation action options.

            * - :py:class:`~ansys.stk.core.stkobjects.ANIMATION_DIRECTIONS`
              - Animation direction options.

            * - :py:class:`~ansys.stk.core.stkobjects.AZ_EL_MASK_TYPE`
              - Obscura types of the facility, place or target for AzElMask definition.

            * - :py:class:`~ansys.stk.core.stkobjects.ACTION_TYPE`
              - Specify the action type for the Interval Access Constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AXIS_OFFSET`
              - Specify the axis offset for the sensor 3D Vertex Offset.

            * - :py:class:`~ansys.stk.core.stkobjects.DATA_PROVIDER_RESULT_CATEGORIES`
              - Specify the category of results returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DATA_PROVIDER_TYPE`
              - Specify the type of the result returned by data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DATA_PROVIDER_ELEMENT_TYPE`
              - Specify the type of data returned by data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.ACCESS_TIME_TYPE`
              - The time period to use for the access computation.

            * - :py:class:`~ansys.stk.core.stkobjects.ALTITUDE_REFERENCE_TYPE`
              - Altitude reference options.

            * - :py:class:`~ansys.stk.core.stkobjects.TERRAIN_NORM_TYPE`
              - Methods of defining the slope of the local terrain for the facility, place or target.

            * - :py:class:`~ansys.stk.core.stkobjects.LIGHTING_OBSTRUCTION_MODEL_TYPE`
              - Obstruction model used in lighting computations.

            * - :py:class:`~ansys.stk.core.stkobjects.DISPLAY_TIMES_TYPE`
              - Display times options for the object.

            * - :py:class:`~ansys.stk.core.stkobjects.AREA_TYPE`
              - Methods of defining the area target's boundaries.

            * - :py:class:`~ansys.stk.core.stkobjects.TRAJECTORY_TYPE`
              - Trajectory type for a point.

            * - :py:class:`~ansys.stk.core.stkobjects.OFFSET_FRAME_TYPE`
              - Frame options for label offset.

            * - :py:class:`~ansys.stk.core.stkobjects.SCENARIO_3D_POINT_SIZE`
              - Font size in points.

            * - :py:class:`~ansys.stk.core.stkobjects.TERRAIN_FILE_TYPE`
              - Terrain file type options.

            * - :py:class:`~ansys.stk.core.stkobjects.TILESET_3D_SOURCE_TYPE`
              - 3DTileset source type options.

            * - :py:class:`~ansys.stk.core.stkobjects.MARKER_TYPE`
              - Marker style options for a waypoint.

            * - :py:class:`~ansys.stk.core.stkobjects.VECTOR_AXES_CONNECT_TYPE`
              - Methods for connecting geometric elements.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_MARKER_ORIGIN_TYPE`
              - Options for the AgVOMarker X or Y Origin property.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_LABEL_SWAP_DISTANCE`
              - Label swap distance options.

            * - :py:class:`~ansys.stk.core.stkobjects.PLANET_POSITION_SOURCE_TYPE`
              - Options for defining a planet.

            * - :py:class:`~ansys.stk.core.stkobjects.EPHEM_SOURCE_TYPE`
              - Central body ephemeris sources.

            * - :py:class:`~ansys.stk.core.stkobjects.PLANET_ORBIT_DISPLAY_TYPE`
              - Orbit display options for a planet.

            * - :py:class:`~ansys.stk.core.stkobjects.SCENARIO_END_LOOP_TYPE`
              - Scenario animation cycle options.

            * - :py:class:`~ansys.stk.core.stkobjects.SCENARIO_REFRESH_DELTA_TYPE`
              - Scenario animation refresh update options.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_PATTERN`
              - Sensor patterns.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_POINTING`
              - Sensor pointing options.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_POINTING_TARGETED_BORESIGHT_TYPE`
              - Boresight types for sensors of targeted pointing type.

            * - :py:class:`~ansys.stk.core.stkobjects.BORESIGHT_TYPE`
              - About boresight options for sensors of targeted pointing type.

            * - :py:class:`~ansys.stk.core.stkobjects.TRACK_MODE_TYPE`
              - Track mode options for tracking boresights.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE`
              - Primary boresight axis for Sensor Az-El mask.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_REFRACTION_TYPE`
              - Sensor refraction models.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_PROJECTION_DISTANCE_TYPE`
              - Sensor 2D Graphics Projection 'Project To' options.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_LOCATION`
              - Sensor Location Type options.

            * - :py:class:`~ansys.stk.core.stkobjects.SCENARIO_TIME_STEP_TYPE`
              - Scenario animation time step options.

            * - :py:class:`~ansys.stk.core.stkobjects.NOTE_SHOW_TYPE`
              - Options for specifying when a label note displays.

            * - :py:class:`~ansys.stk.core.stkobjects.GEOMETRIC_ELEM_TYPE`
              - Options for the VORefCrdn Type.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_SCAN_MODE`
              - Options for the Sensor Spinning Scan Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.CONSTRAINT_BACKGROUND`
              - Options for the Background constraint, and Advanced vehicle constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.CONSTRAINT_GROUND_TRACK`
              - Options for the Ground Track constraint, an Advanced vehicle constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.INTERSECTION_TYPE`
              - Intersection display options for sensor projection.

            * - :py:class:`~ansys.stk.core.stkobjects.CONSTRAINT_LIGHTING`
              - Options for the Lighting access constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_PROJECTION_TYPE`
              - Options for a sensor's 3D Graphics Projection Type.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_PULSE_STYLE`
              - Options for a sensor's 3D Graphics Pulse Style.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET`
              - Options for a sensor's 3D Graphics Pulse Frequency presets.

            * - :py:class:`~ansys.stk.core.stkobjects.LINE_WIDTH`
              - Line widths.

            * - :py:class:`~ansys.stk.core.stkobjects.STK_OBJECT_TYPE`
              - STK objects.

            * - :py:class:`~ansys.stk.core.stkobjects.ACCESS_CONSTRAINTS`
              - Available Access Constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE`
              - Border Wall upper and lower edge altitude references.

            * - :py:class:`~ansys.stk.core.stkobjects.SHADOW_MODEL`
              - Shadow model options for solar radiation pressure.

            * - :py:class:`~ansys.stk.core.stkobjects.METHOD_TO_COMPUTE_SUN_POSITION`
              - Methods to compute sun position.

            * - :py:class:`~ansys.stk.core.stkobjects.ATMOSPHERIC_DENSITY_MODEL`
              - Atmospheric density models.

            * - :py:class:`~ansys.stk.core.stkobjects.MARKER_SHAPE_3D`
              - 3D marker shapes.

            * - :py:class:`~ansys.stk.core.stkobjects.LEAD_TRAIL_DATA`
              - Lead and trail types for track display.

            * - :py:class:`~ansys.stk.core.stkobjects.TICK_DATA`
              - Tick mark options. Tick marks represent milestones at specified intervals along a vehicle's track in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.LOAD_METHOD_TYPE`
              - TLE load options.

            * - :py:class:`~ansys.stk.core.stkobjects.LLA_POSITION_TYPE`
              - LLA Position Types.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_PASS`
              - Pass display options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_VISIBLE_SIDES`
              - Pass display direction options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_OFFSET`
              - Options for offset direction for 2D time events graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE`
              - 2D Graphics time event graphics options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_ATTRIBUTES`
              - Criteria for displaying a vehicle's 2D Graphics attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_ELEVATION`
              - Options for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_2D_OPTIONS`
              - Display options for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.MODEL_TYPE`
              - Display options 3D model.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE`
              - Options for where to end drop lines.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_3D_SIGMA_SCALE`
              - Sigma scale options for sizing covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_3D_ATTRIBUTES`
              - Options for 3D graphics for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.ROUTE_GRAPHICS_3D_MARKER_TYPE`
              - Waypoint marker options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_ELLIPSE_OPTIONS`
              - Elliptical motion modeling options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_PROPAGATOR_TYPE`
              - Vehicle propagators (available for vehicle types listed in parentheses).

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SGP4_SWITCH_METHOD`
              - TLE Switch method for the SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SGP4TLE_SELECTION`
              - TLE Selection method for the SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SGP4_AUTO_UPDATE_SOURCE`
              - The TLE sources where the SGP4 propagator retrieves TLEs from automatically upon propagation.

            * - :py:class:`~ansys.stk.core.stkobjects.THIRD_BODY_GRAV_SOURCE_TYPE`
              - Sources for 3rd body gravitation data.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GEOMAG_FLUX_SRC`
              - GeomagFluxSrc.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GEOMAG_FLUX_UPDATE_RATE`
              - Geomagnetic flux update rate options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE`
              - Options for specifying solar and geomagnetic flux.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_INTEGRATION_MODEL`
              - Integration methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_PREDICTOR_CORRECTOR_SCHEME`
              - Predictor Corrector schemes.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_METHOD`
              - Step size control options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_INTERPOLATION_METHOD`
              - Interpolation methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_FRAME`
              - Frame options for covariance matrix.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_CORRELATION_LIST_TYPE`
              - Correlation List row and column values.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_CONSIDER_ANALYSIS_TYPE`
              - Consider parameters for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_WAYPOINT_COMP_METHOD`
              - Methods for computing waypoints.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_ALTITUDE_REFERENCE`
              - Reference altitude options for waypoints.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_WAYPOINT_INTERPOLATION_METHOD`
              - Interpolation methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_LAUNCH`
              - Options for launch coordinates.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_IMPACT`
              - Impact location options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_LAUNCH_CONTROL`
              - Flight parameters for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_IMPACT_LOCATION`
              - Options for specifying missile impact point.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_PASS_NUMBERING`
              - Pass numbering options.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_PARTIAL_PASS_MEASUREMENT`
              - Partial Pass Measurement methods (typically used for reporting data).

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_COORDINATE_SYSTEM`
              - Coordinate system used for measurement of latitude and longitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_BREAK_ANGLE_TYPE`
              - Definition options for setting pass breaks:.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_DIRECTION`
              - Direction of latitude crossing at the beginning of a pass.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_LOCATION`
              - Location options for the display of textual data in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_X_ORIGIN`
              - X origin options for positioning data display.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_Y_ORIGIN`
              - Y origin options for positioning data display.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_FONT_SIZE`
              - Font size for data display.

            * - :py:class:`~ansys.stk.core.stkobjects.AIRCRAFT_WGS84_WARNING_TYPE`
              - Display mode options for aircraft mission modeler WGS84 warning.

            * - :py:class:`~ansys.stk.core.stkobjects.SURFACE_REFERENCE`
              - Options for surface reference of earth globes.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_FORMAT`
              - Font format for data display.

            * - :py:class:`~ansys.stk.core.stkobjects.ATTITUDE_STANDARD_TYPE`
              - AgEAttitudeStandardType tells the user which interface to cast to. eRouteAttitudeStandard -> IAgVeRouteAttitudeStandard, eTrajectoryAttitudeStandard -> IAgVeTrajectoryAttitudeStandard, eOrbitAttitudeStanard -> IAgVeOrbitAttitudeStandard.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_ATTITUDE`
              - Available attitude types.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_PROFILE`
              - Predefined attitude profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_LOOK_AHEAD_METHOD`
              - Look ahead duration methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_ALTITUDE_CROSSING_SIDES`
              - Options for specifying which crossings are computed and displayed in the 2D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_ALTITUDE_CROSSING_DIRECTION`
              - Options for specifying the direction in which the sensor's field of view crosses the specified altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_INHERIT_FROM_2D`
              - Options for how projection distances that are computed based on 2D Graphics projection settings are displayed in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE`
              - Options optimizing the visual appearance of projections.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_TIME_PERIOD_TYPE`
              - Compute Time Period Type.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_CONST_CONSTRAINTS_MODE`
              - Constellation Constraints Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_COV_ASSET_MODE`
              - Chain Cov Asset Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_PARENT_PLATFORM_RESTRICTION`
              - Options for a chain's From and To Parent Platform Restriction.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_OPTIMAL_STRAND_METRIC_TYPE`
              - Chain optimal strand metric type.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE`
              - Chain optimal strand calculation scalar type.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE`
              - Chain optimal strand link comparison type.

            * - :py:class:`~ansys.stk.core.stkobjects.CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE`
              - Chain optimal strand link comparison type.

            * - :py:class:`~ansys.stk.core.stkobjects.DATA_SAVE_MODE`
              - Access Save Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_BOUNDS`
              - Coverage bounds options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_POINT_LOC_METHOD`
              - Point location method.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_POINT_ALTITUDE_METHOD`
              - Custom point altitude method.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_GRID_CLASS`
              - Classes of objects that can be used as templates to associate access constraints, basic object properties and, in some cases, altitude with points in the grid.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_ALTITUDE_METHOD`
              - Method for specifying the altitude of a grid point.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_GROUND_ALTITUDE_METHOD`
              - Method for specifying the ground altitude of a grid point.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_DATA_RETENTION`
              - Data retention options.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_REGION_ACCESS_ACCELERATION`
              - Regional acceleration options.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_RESOLUTION`
              - Coverage grid resolution options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_ASSET_STATUS`
              - Coverage asset status.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_ASSET_GROUPING`
              - Coverage asset grouping options.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_DEFINITION_TYPE`
              - Figure of Merit types: values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_SATISFACTION_TYPE`
              - Satisfaction options: determine whether satisfaction is achieved based on the value of the figure of merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_CONSTRAINT_NAME`
              - Available constraints to use for the Access Constraint Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_COMPUTE`
              - Figure of Merit compute options.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_ACROSS_ASSETS`
              - Across Assets options: specify which value of the constraint is to be selected based on all currently available assets.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_COMPUTE_TYPE`
              - Allowed number of assets for the navigation solution.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_METHOD`
              - Dilution of Precision method.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_END_GAP_OPTION`
              - End gap options: control consideration of gaps at ends of analysis intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE`
              - Contour fill options.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD`
              - Methods for assigning colors to contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT`
              - Format options for floating point numbers.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION`
              - Level order display options for the contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION`
              - Accumulation options: control the sense and persistence of animation graphics for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE`
              - Options for uncertainty in one-way range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.IV_CLOCK_HOST`
              - Clock host options for access. Time values are reported with a clock colocated with the clock host object.

            * - :py:class:`~ansys.stk.core.stkobjects.IV_TIME_SENSE`
              - Mode of signal transmission of the designated clock host.

            * - :py:class:`~ansys.stk.core.stkobjects.GPS_ATTITUDE_MODEL_TYPE`
              - GPS attitude profile model types.

            * - :py:class:`~ansys.stk.core.stkobjects.CONSTELLATION_CONSTRAINT_RESTRICTION`
              - The values of the enumeration are used to define constellation constraints that allow you to specify the criteria to be used when constellations are combined with other objects in a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.EVENT_DETECTION`
              - Available event detection strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.SAMPLING_METHOD`
              - Available sampling methods.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_SATISFACTION_TYPE`
              - The condition on the number of assets covering a grid point that must be satisfied for a valid access.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDS_REFERENCE_FRAME`
              - Reference Frame.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDS_DATE_FORMAT`
              - The date format of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDS_EPHEM_FORMAT`
              - The ephemeris format of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDS_TIME_SYSTEM`
              - Time System.

            * - :py:class:`~ansys.stk.core.stkobjects.STK_EPHEM_COORDINATE_SYSTEM`
              - The Coordinate System of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.STK_EPHEM_COVARIANCE_TYPE`
              - The covariance data export type.

            * - :py:class:`~ansys.stk.core.stkobjects.EXPORT_TOOL_VERSION_FORMAT`
              - The version format of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.EXPORT_TOOL_TIME_PERIOD`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.SPICE_INTERPOLATION`
              - The SPICE interpolation type.

            * - :py:class:`~ansys.stk.core.stkobjects.ATTITUDE_COORDINATE_AXES`
              - Attitude export options.

            * - :py:class:`~ansys.stk.core.stkobjects.ATTITUDE_INCLUDE`
              - Details to include in an exported Attitude file.

            * - :py:class:`~ansys.stk.core.stkobjects.EXPORT_TOOL_STEP_SIZE`
              - The Step Size type for an attitude file.

            * - :py:class:`~ansys.stk.core.stkobjects.TEXT_OUTLINE_STYLE`
              - The text outline style for 2D graphics display.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO_RANGE_MODE`
              - MTO Range Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO_TRACK_EVAL`
              - MTO Track Eval Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO_ENTIRETY`
              - MTO Entirety Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO_VISIBILITY_MODE`
              - MTO Visibility Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO_OBJECT_INTERVAL`
              - MTO object interval type.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO_INPUT_DATA_TYPE`
              - MTO Input Data Type.

            * - :py:class:`~ansys.stk.core.stkobjects.SOLID_TIDE`
              - The Solid Tide Type for force modeling.

            * - :py:class:`~ansys.stk.core.stkobjects.TIME_PERIOD_VALUE_TYPE`
              - Time value types.

            * - :py:class:`~ansys.stk.core.stkobjects.ONE_POINT_ACCESS_STATUS`
              - One point access status.

            * - :py:class:`~ansys.stk.core.stkobjects.ONE_POINT_ACCESS_SUMMARY`
              - One point access summary type.

            * - :py:class:`~ansys.stk.core.stkobjects.LOOK_AHEAD_PROPAGATOR`
              - Propagators used for calculating ephemeris for look ahead purposes. The enumeration is used with realtime propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.GRAPHICS_3D_MARKER_ORIENTATION`
              - 3D graphics marker orientations.

            * - :py:class:`~ansys.stk.core.stkobjects.SRP_MODEL`
              - Solar radiation pressure model types.

            * - :py:class:`~ansys.stk.core.stkobjects.DRAG_MODEL`
              - Drag model types.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_PROPAGATION_FRAME`
              - Propagation frames used by J2/J4/TwoBody propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.STAR_REFERENCE_FRAME`
              - Star reference frame types.

            * - :py:class:`~ansys.stk.core.stkobjects.GPS_REFERENCE_WEEK`
              - GPS almanac reference week.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_CUSTOM_REGION_ALGORITHM`
              - The enumerations are used to enable/disable the special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GPS_SWITCH_METHOD`
              - GPS Switch method for the GPS propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GPS_ELEM_SELECTION`
              - GPS Selection method for the GPS propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GPS_AUTO_UPDATE_SOURCE`
              - The sources to retrieve GPS elements from upon propagation.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_GPS_ALMANAC_TYPE`
              - GPS Almanac types.

            * - :py:class:`~ansys.stk.core.stkobjects.STK_EXTERNAL_EPHEMERIS_FORMAT`
              - Ephemeris file formats supported by the Stk external propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.STK_EXTERNAL_FILE_MESSAGE_LEVEL`
              - Ephemeris file message level used by the Stk external propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.COVERAGE_3D_DRAW_AT_ALTITUDE_MODE`
              - Coverage definition drawing modes for filled graphics when showing at altitude in 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.DISTANCE_ON_SPHERE`
              - Type of line which connects the two points.

            * - :py:class:`~ansys.stk.core.stkobjects.FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE`
              - Invalid Value Action: Controls consideration of time samples usage for computing navigation solution when insufficient number of assets are available at one or more of the time samples used.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SLEW_TIMING_BETWEEN_TARGETS`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SLEW_MODE`
              - Target slew modes.

            * - :py:class:`~ansys.stk.core.stkobjects.COMPONENT`
              - The different types of components in the component browser.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_DEFINITION_TYPE`
              - Volume grid definition types.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_SPATIAL_CALC_EVAL_TYPE`
              - Evaluation of Spatial Calculation types.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_SAVE_COMPUTED_DATA_TYPE`
              - Save Computed Data types.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_DISPLAY_VOLUME_TYPE`
              - Graphics volume display type.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_DISPLAY_QUALITY_TYPE`
              - Quality of the graphics display types.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_LEGEND_NUMERIC_NOTATION`
              - Legend numeric notation types.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_LEVEL_ORDER`
              - Legend level display order.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_PROCESSING_LEVELS`
              - EOIR processing levels.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_JITTER_TYPES`
              - EOIR jitter type.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_SCAN_MODES`
              - EOIR sensor scan mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_IMAGE_QUALITY`
              - EOIR band image quality levels.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_SPECTRAL_SHAPE`
              - EOIR overall system spectral shape determination.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE`
              - EOIR spatial input parameter specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS`
              - EOIR spectral relative system response units specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE`
              - EOIR optical input parameter specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE`
              - EOIR optical transmission parameter specification mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_RAD_PARAM_LEVEL`
              - EOIR radiometric detector parameter level of specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_QE_MODE`
              - EOIR quantum efficiency specification mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_QUANTIZATION_MODE`
              - EOIR mode of determining quantization step size.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_WAVELENGTH_TYPE`
              - EOIR band diffraction wavelength reference type.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_EOIR_BAND_SATURATION_MODE`
              - EOIR band irradiance or radiance reference mode.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_VOLUME_GRID_EXPORT_TYPE`
              - Volumetric data export types.

            * - :py:class:`~ansys.stk.core.stkobjects.VOLUMETRIC_DATA_EXPORT_FORMAT_TYPE`
              - Volumetric data export format types.

            * - :py:class:`~ansys.stk.core.stkobjects.CONSTELLATION_FROM_TO_PARENT_CONSTRAINT`
              - Options for a chain's From and To Parent Constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS`
              - Available Analysis Workbench Access Constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.STATISTICS`
              - The different statistics that might be available for a data set.

            * - :py:class:`~ansys.stk.core.stkobjects.TIME_VARYING_EXTREMUM`
              - The different time varying extremum that might be available for a data set.

            * - :py:class:`~ansys.stk.core.stkobjects.MODEL_GLTF_REFLECTION_MAP_TYPE`
              - Settings for glTF Reflection.

            * - :py:class:`~ansys.stk.core.stkobjects.SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE`
              - The different ways to determine the sensor's space projection distance in the 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.LOP_ATMOSPHERIC_DENSITY_MODEL`
              - LOP Atmospheric density models.

            * - :py:class:`~ansys.stk.core.stkobjects.LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL`
              - Low Altitude Atmospheric density models.

            * - :py:class:`~ansys.stk.core.stkobjects.EPHEM_EXPORT_TOOL_FILE_FORMAT`
              - Ephemeris Export Tool file formats.

            * - :py:class:`~ansys.stk.core.stkobjects.ADV_CAT_ELLIPSOID_CLASS`
              - Method for determining Ellipsoid Sizing method (class).

            * - :py:class:`~ansys.stk.core.stkobjects.ADV_CAT_CONJUNCTION_TYPE`
              - Mode for computing events involving conjunction TCA.

            * - :py:class:`~ansys.stk.core.stkobjects.ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE`
              - Type of visible Secondary Ellipsoids.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIR_SHAPE_TYPE`
              - The object geometry which will be rendered in the synthetic scene window.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE`
              - Designation of how material properties are specified.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIR_THERMAL_MODEL_TYPE`
              - EOIR thermal models.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIR_FLIGHT_TYPE`
              - EOIR Flight Types.

            * - :py:class:`~ansys.stk.core.stkobjects.COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE`
              - Component link/embed control reference type.

            * - :py:class:`~ansys.stk.core.stkobjects.SWATH_COMPUTATIONAL_METHOD`
              - Computationals methods for generating swaths.

            * - :py:class:`~ansys.stk.core.stkobjects.CLASSICAL_LOCATION`
              - Classical (Keplerian) element used to specify the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ORIENTATION_ASC_NODE`
              - Ascending node-related options for use in specifying orbit orientation.

            * - :py:class:`~ansys.stk.core.stkobjects.GEODETIC_SIZE`
              - Size options for the Geodetic coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.DELAUNAY_L_TYPE`
              - Select whether to use the default representation of Delaunay L or L/SQRT(mu).

            * - :py:class:`~ansys.stk.core.stkobjects.DELAUNAY_H_TYPE`
              - Select whether to use the default representation of Delaunay H or H/SQRT(mu).

            * - :py:class:`~ansys.stk.core.stkobjects.DELAUNAY_G_TYPE`
              - Select whether to use the default representation of Delaunay G or G/SQRT(mu).

            * - :py:class:`~ansys.stk.core.stkobjects.EQUINOCTIAL_SIZE_SHAPE`
              - Opt whether to use Mean Motion or Semimajor Axis to specify the orbit size (Equinoctial coordinate type).

            * - :py:class:`~ansys.stk.core.stkobjects.MIXED_SPHERICAL_FLIGHT_PATH_ANGLE`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~ansys.stk.core.stkobjects.SPHERICAL_FLIGHT_PATH_ANGLE`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~ansys.stk.core.stkobjects.CLASSICAL_SIZE_SHAPE`
              - Pairs of Classical (Keplerian) elements used to specify orbit size and shape.

            * - :py:class:`~ansys.stk.core.stkobjects.EQUINOCTIAL_FORMULATION`
              - Formulation: retrograde or posigrade.

            * - :py:class:`~ansys.stk.core.stkobjects.SCATTERING_POINT_PROVIDER_TYPE`
              - Scattering point provider type.

            * - :py:class:`~ansys.stk.core.stkobjects.SCATTERING_POINT_MODEL_TYPE`
              - Scattering point model type.

            * - :py:class:`~ansys.stk.core.stkobjects.SCATTERING_POINT_PROVIDER_LIST_TYPE`
              - Scattering Point Provider List Type.

            * - :py:class:`~ansys.stk.core.stkobjects.POLARIZATION_TYPE`
              - Polarization Type.

            * - :py:class:`~ansys.stk.core.stkobjects.POLARIZATION_REFERENCE_AXIS`
              - Polarization reference axis.

            * - :py:class:`~ansys.stk.core.stkobjects.NOISE_TEMP_COMPUTE_TYPE`
              - System noise temperature compute type.

            * - :py:class:`~ansys.stk.core.stkobjects.POINTING_STRATEGY_TYPE`
              - Pointing strategy type.

            * - :py:class:`~ansys.stk.core.stkobjects.WAVEFORM_TYPE`
              - Waveform types.

            * - :py:class:`~ansys.stk.core.stkobjects.FREQUENCY_SPEC`
              - Frequency Specification Type.

            * - :py:class:`~ansys.stk.core.stkobjects.PRF_MODE`
              - Radar search/track prf modes.

            * - :py:class:`~ansys.stk.core.stkobjects.PULSE_WIDTH_MODE`
              - Radar search/track pulse width modes.

            * - :py:class:`~ansys.stk.core.stkobjects.WAVEFORM_SELECTION_STRATEGY_TYPE`
              - Waveform selection strategy type.

            * - :py:class:`~ansys.stk.core.stkobjects.ANTENNA_CONTROL_REFERENCE_TYPE`
              - Antenna control reference type.

            * - :py:class:`~ansys.stk.core.stkobjects.ANTENNA_MODEL_TYPE`
              - Antenna model types.

            * - :py:class:`~ansys.stk.core.stkobjects.ANTENNA_CONTOUR_TYPE`
              - Antenna contour types.

            * - :py:class:`~ansys.stk.core.stkobjects.CIRCULAR_APERTURE_INPUT_TYPE`
              - Circular aperture antenna input type.

            * - :py:class:`~ansys.stk.core.stkobjects.RECTANGULAR_APERTURE_INPUT_TYPE`
              - Rectangular aperture antenna input type.

            * - :py:class:`~ansys.stk.core.stkobjects.DIRECTION_PROVIDER_TYPE`
              - Direction Provider types.

            * - :py:class:`~ansys.stk.core.stkobjects.BEAMFORMER_TYPE`
              - Beamformer types.

            * - :py:class:`~ansys.stk.core.stkobjects.ELEMENT_CONFIGURATION_TYPE`
              - Element configuration types.

            * - :py:class:`~ansys.stk.core.stkobjects.LATTICE_TYPE`
              - Lattice types.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACING_UNIT`
              - Spacing Units.

            * - :py:class:`~ansys.stk.core.stkobjects.LIMITS_EXCEEDED_BEHAVIOR_TYPE`
              - Limits Exceeded Behavior types.

            * - :py:class:`~ansys.stk.core.stkobjects.ANTENNA_GRAPHICS_COORDINATE_SYSTEM`
              - Coordinate system for defining antenna graphics resolution.

            * - :py:class:`~ansys.stk.core.stkobjects.ANTENNA_MODEL_INPUT_TYPE`
              - Diameter computation input type.

            * - :py:class:`~ansys.stk.core.stkobjects.HFSS_FFD_GAIN_TYPE`
              - Gain type.

            * - :py:class:`~ansys.stk.core.stkobjects.ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE`
              - Cosecant Squared antenna sidelobe selection types.

            * - :py:class:`~ansys.stk.core.stkobjects.BEAM_SELECTION_STRATEGY_TYPE`
              - Beam selection strategy types.

            * - :py:class:`~ansys.stk.core.stkobjects.TRANSMITTER_MODEL_TYPE`
              - Transmitter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.TRANSFER_FUNCTION_TYPE`
              - Transmitter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.RE_TRANSMITTER_OP_MODE`
              - Re-Transmitter operational mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RECEIVER_MODEL_TYPE`
              - Receiver model types.

            * - :py:class:`~ansys.stk.core.stkobjects.LINK_MARGIN_TYPE`
              - Link margin types.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_STC_ATTENUATION_TYPE`
              - Stc Attenuation Type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_FREQUENCY_SPEC`
              - SNR Contour Type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SNR_CONTOUR_TYPE`
              - SNR Contour Type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_MODEL_TYPE`
              - Radar system types.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_MODE_TYPE`
              - Radar mode types.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_WAVEFORM_SEARCH_TRACK_TYPE`
              - Radar search/track waveform types.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SEARCH_TRACK_PRF_MODE`
              - Radar search/track prf modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE`
              - Radar search/track pulse width modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SAR_PRF_MODE`
              - Radar SAR prf modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SAR_RANGE_RESOLUTION_MODE`
              - Radar SAR range resolution modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SAR_PCR_MODE`
              - Radar SAR pulse compression ratio modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE`
              - Radar sar pulse integration mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_P_DET_TYPE`
              - Radar probability of detection type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_PULSE_INTEGRATION_TYPE`
              - Radar pulse integration type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_PULSE_INTEGRATOR_TYPE`
              - Radar pulse integrator type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE`
              - Radar continuous wave analysis mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_CLUTTER_GEOMETRY_MODEL_TYPE`
              - Radar clutter geometry model type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_CLUTTER_MAP_MODEL_TYPE`
              - Radar clutter map model type.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_SWERLING_CASE`
              - Radar swerling case.

            * - :py:class:`~ansys.stk.core.stkobjects.RCS_COMPUTE_STRATEGY`
              - Radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_ACTIVITY_TYPE`
              - Radar activity times strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION`
              - Radar cross section contour graphics polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.RF_FILTER_MODEL_TYPE`
              - RF filter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.MODULATOR_MODEL_TYPE`
              - Modulator model types.

            * - :py:class:`~ansys.stk.core.stkobjects.DEMODULATOR_MODEL_TYPE`
              - Demodulator model types.

            * - :py:class:`~ansys.stk.core.stkobjects.RAIN_LOSS_MODEL_TYPE`
              - Rain loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.ATMOSPHERIC_ABSORPTION_MODEL_TYPE`
              - Atmospheric absorption model types.

            * - :py:class:`~ansys.stk.core.stkobjects.URBAN_TERRESTRIAL_LOSS_MODEL_TYPE`
              - urban/terrestrial loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE`
              - Clouds and Fog loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.CLOUDS_AND_FOG_LIQUID_WATER_CHOICES`
              - Clouds and Fog loss model liquid water content choices.

            * - :py:class:`~ansys.stk.core.stkobjects.IONOSPHERIC_FADING_LOSS_MODEL_TYPE`
              - Ionospheric loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE`
              - TropoScintillation loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES`
              - TroposphericScintillation loss model average time choices.

            * - :py:class:`~ansys.stk.core.stkobjects.PROJECTION_HORIZONTAL_DATUM_TYPE`
              - REMCOM Wireless InSite RT project/horizontal datum type.

            * - :py:class:`~ansys.stk.core.stkobjects.BUILD_HEIGHT_REFERENCE_METHOD`
              - REMCOM Wireless InSite RT building height reference method.

            * - :py:class:`~ansys.stk.core.stkobjects.BUILD_HEIGHT_UNIT`
              - REMCOM Wireless InSite RT building height unit.

            * - :py:class:`~ansys.stk.core.stkobjects.TIREM_POLARIZATION_TYPE`
              - TIREM polarization type.

            * - :py:class:`~ansys.stk.core.stkobjects.VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE`
              - VOACAP solar activity configuration type.

            * - :py:class:`~ansys.stk.core.stkobjects.VOACAP_COEFFICIENT_DATA_TYPE`
              - VOACAP coefficient data type.

            * - :py:class:`~ansys.stk.core.stkobjects.LASER_PROPAGATION_LOSS_MODEL_TYPE`
              - Laser propagation loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE`
              - Laser tropospheric scintillation loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.ATMOSPHERIC_TURBULENCE_MODEL_TYPE`
              - Refractive index structure parameter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.MODTRAN_AEROSOL_MODEL_TYPE`
              - MODTRAN-derived lookup table aerosol model extinction types.

            * - :py:class:`~ansys.stk.core.stkobjects.MODTRAN_CLOUD_MODEL_TYPE`
              - MODTRAN Cloud model types.

            * - :py:class:`~ansys.stk.core.stkobjects.COMM_SYSTEM_REFERENCE_BANDWIDTH`
              - CommSystem reference bandwidth.

            * - :py:class:`~ansys.stk.core.stkobjects.COMM_SYSTEM_CONSTRAINING_ROLE`
              - CommSystem constraining role.

            * - :py:class:`~ansys.stk.core.stkobjects.COMM_SYSTEM_SAVE_MODE`
              - CommSystem save mode.

            * - :py:class:`~ansys.stk.core.stkobjects.COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE`
              - CommSystem access options event detection type.

            * - :py:class:`~ansys.stk.core.stkobjects.COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE`
              - CommSystem access options sampling method type.

            * - :py:class:`~ansys.stk.core.stkobjects.COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE`
              - Link selection strategy types.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY`
              - Activity level for the NASA models NASAELE and NASAPRO.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY`
              - Activity level for CRRESPRO model.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY`
              - Activity level for CRRESRAD model.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE`
              - Mode by which color is assigned.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE`
              - Scaling of magnetic field to use when assigning color/translucency.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD`
              - Main magnetic field.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD`
              - External magnetic field.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_SAA_CHANNEL`
              - Energy level for SAA protons.

            * - :py:class:`~ansys.stk.core.stkobjects.SPACE_ENVIRONMENT_SAA_FLUX_LEVEL`
              - Flux level for SAA contour.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL`
              - Thermal shape model.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE`
              - Mode for computing 13-month average F10.7.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_MATERIAL`
              - Material.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE`
              - Models that are to be included when modeling radiation.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL`
              - Dose channel.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY`
              - Detector geometry.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE`
              - Detector material.

            * - :py:class:`~ansys.stk.core.stkobjects.VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE`
              - Mode for computing 15 day average Ap.

            * - :py:class:`~ansys.stk.core.stkobjects.NOTIFICATION_FILTER_MASK`
              - The notification flags are used to enable/disable STK Object Model event notifications.



Description
-----------

The following is an overview of the classes, interfaces and enumerations of the STK Object Model.


.. py:currentmodule:: ansys.stk.core.stkobjects


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🖿 aviator<stkobjects/aviator>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🗎 astrogator<stkobjects/astrogator>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IDataProviderInfo<stkobjects/IDataProviderInfo>
     IDataProvider<stkobjects/IDataProvider>
     IStkObject<stkobjects/IStkObject>
     IAccessInterval<stkobjects/IAccessInterval>
     IFigureOfMeritDefinition<stkobjects/IFigureOfMeritDefinition>
     IFigureOfMeritDefinitionCompute<stkobjects/IFigureOfMeritDefinitionCompute>
     IStkObjectElementCollection<stkobjects/IStkObjectElementCollection>
     IStkObjectCollection<stkobjects/IStkObjectCollection>
     IAnimation<stkobjects/IAnimation>
     IComponentInfo<stkobjects/IComponentInfo>
     ICloneable<stkobjects/ICloneable>
     IComponentLinkEmbedControl<stkobjects/IComponentLinkEmbedControl>
     IDisplayTimesData<stkobjects/IDisplayTimesData>
     IDisplayTime<stkobjects/IDisplayTime>
     ITerrainNormData<stkobjects/ITerrainNormData>
     ILifetimeInformation<stkobjects/ILifetimeInformation>
     IVehicleLeadTrailData<stkobjects/IVehicleLeadTrailData>
     IVehicleLeadTrailDataFraction<stkobjects/IVehicleLeadTrailDataFraction>
     IVehicleLeadTrailDataTime<stkobjects/IVehicleLeadTrailDataTime>
     IAccessConstraint<stkobjects/IAccessConstraint>
     IAccessConstraintMinMax<stkobjects/IAccessConstraintMinMax>
     IGraphics3DMarkerData<stkobjects/IGraphics3DMarkerData>
     IGraphics3DModelData<stkobjects/IGraphics3DModelData>
     IGraphics3DModel<stkobjects/IGraphics3DModel>
     IGraphics3DReferenceAnalysisWorkbenchComponent<stkobjects/IGraphics3DReferenceAnalysisWorkbenchComponent>
     ILLAPosition<stkobjects/ILLAPosition>
     IClassicalSizeShape<stkobjects/IClassicalSizeShape>
     IOrientationAscNode<stkobjects/IOrientationAscNode>
     IClassicalLocation<stkobjects/IClassicalLocation>
     IGeodeticSize<stkobjects/IGeodeticSize>
     IDelaunayActionVariable<stkobjects/IDelaunayActionVariable>
     IFlightPathAngle<stkobjects/IFlightPathAngle>
     IProvideSpatialInfo<stkobjects/IProvideSpatialInfo>
     IRadarClutterMap<stkobjects/IRadarClutterMap>
     ITimePeriod<stkobjects/ITimePeriod>
     IAccessAdvanced<stkobjects/IAccessAdvanced>
     IRefractionModelBase<stkobjects/IRefractionModelBase>
     IDisplayDistance<stkobjects/IDisplayDistance>
     ISensorProjectionDisplayDistance<stkobjects/ISensorProjectionDisplayDistance>
     ISensorPattern<stkobjects/ISensorPattern>
     ISensorPointingTargetedBoresight<stkobjects/ISensorPointingTargetedBoresight>
     ISensorPointing<stkobjects/ISensorPointing>
     IAzElMaskData<stkobjects/IAzElMaskData>
     IRadarClutterMapInheritable<stkobjects/IRadarClutterMapInheritable>
     IPlatformRFEnvironment<stkobjects/IPlatformRFEnvironment>
     IAreaTypeData<stkobjects/IAreaTypeData>
     IPositionSourceData<stkobjects/IPositionSourceData>
     IOrbitDisplayData<stkobjects/IOrbitDisplayData>
     IPolarization<stkobjects/IPolarization>
     IPolarizationElliptical<stkobjects/IPolarizationElliptical>
     IPolarizationCrossPolLeakage<stkobjects/IPolarizationCrossPolLeakage>
     IPolarizationLinear<stkobjects/IPolarizationLinear>
     IPolarizationHorizontal<stkobjects/IPolarizationHorizontal>
     IPolarizationVertical<stkobjects/IPolarizationVertical>
     IPointingStrategy<stkobjects/IPointingStrategy>
     IWaveform<stkobjects/IWaveform>
     IWaveformSelectionStrategy<stkobjects/IWaveformSelectionStrategy>
     IScatteringPointProvider<stkobjects/IScatteringPointProvider>
     IScatteringPointModel<stkobjects/IScatteringPointModel>
     IAntennaModel<stkobjects/IAntennaModel>
     IElementConfiguration<stkobjects/IElementConfiguration>
     IElementConfigurationPolygon<stkobjects/IElementConfigurationPolygon>
     IBeamformer<stkobjects/IBeamformer>
     IDirectionProvider<stkobjects/IDirectionProvider>
     IAntennaModelOpticalSimple<stkobjects/IAntennaModelOpticalSimple>
     IAntennaContour<stkobjects/IAntennaContour>
     IAntennaBeamSelectionStrategy<stkobjects/IAntennaBeamSelectionStrategy>
     IAntennaBeam<stkobjects/IAntennaBeam>
     IRFFilterModel<stkobjects/IRFFilterModel>
     IModulatorModel<stkobjects/IModulatorModel>
     ITransmitterModel<stkobjects/ITransmitterModel>
     ITransmitterModelScriptPlugin<stkobjects/ITransmitterModelScriptPlugin>
     IReTransmitterModel<stkobjects/IReTransmitterModel>
     IDemodulatorModel<stkobjects/IDemodulatorModel>
     IReceiverModel<stkobjects/IReceiverModel>
     IReceiverModelScriptPlugin<stkobjects/IReceiverModelScriptPlugin>
     IRadarActivity<stkobjects/IRadarActivity>
     IRadarStcAttenuation<stkobjects/IRadarStcAttenuation>
     IRadarStcAttenuationMap<stkobjects/IRadarStcAttenuationMap>
     IRadarClutterGeometryModel<stkobjects/IRadarClutterGeometryModel>
     IRadarClutterGeometryModelPlugin<stkobjects/IRadarClutterGeometryModelPlugin>
     IRadarContinuousWaveAnalysisMode<stkobjects/IRadarContinuousWaveAnalysisMode>
     IRadarPulseIntegration<stkobjects/IRadarPulseIntegration>
     IRadarWaveformSearchTrack<stkobjects/IRadarWaveformSearchTrack>
     IRadarProbabilityOfDetection<stkobjects/IRadarProbabilityOfDetection>
     IRadarProbabilityOfDetectionCFAR<stkobjects/IRadarProbabilityOfDetectionCFAR>
     IRadarModel<stkobjects/IRadarModel>
     IRadarModeMonostatic<stkobjects/IRadarModeMonostatic>
     IRadarModeBistaticTransmitter<stkobjects/IRadarModeBistaticTransmitter>
     IRadarModeBistaticReceiver<stkobjects/IRadarModeBistaticReceiver>
     IRadarClutterMapModel<stkobjects/IRadarClutterMapModel>
     IRadarClutterMapModelPlugin<stkobjects/IRadarClutterMapModelPlugin>
     IRadarClutterMapModelConstantCoefficient<stkobjects/IRadarClutterMapModelConstantCoefficient>
     IRadarCrossSectionComputeStrategy<stkobjects/IRadarCrossSectionComputeStrategy>
     IModulatorModelScriptPlugin<stkobjects/IModulatorModelScriptPlugin>
     IRainLossModel<stkobjects/IRainLossModel>
     IUrbanTerrestrialLossModel<stkobjects/IUrbanTerrestrialLossModel>
     ITroposphericScintillationFadingLossModel<stkobjects/ITroposphericScintillationFadingLossModel>
     IIonosphericFadingLossModel<stkobjects/IIonosphericFadingLossModel>
     ICloudsAndFogFadingLossModel<stkobjects/ICloudsAndFogFadingLossModel>
     IAtmosphericAbsorptionModel<stkobjects/IAtmosphericAbsorptionModel>
     IAtmosphericAbsorptionModelITURP676<stkobjects/IAtmosphericAbsorptionModelITURP676>
     IAtmosphericAbsorptionModelTirem<stkobjects/IAtmosphericAbsorptionModelTirem>
     ISolarActivityConfiguration<stkobjects/ISolarActivityConfiguration>
     ILaserAtmosphericLossModel<stkobjects/ILaserAtmosphericLossModel>
     ILaserTroposphericScintillationLossModel<stkobjects/ILaserTroposphericScintillationLossModel>
     IAtmosphericTurbulenceModel<stkobjects/IAtmosphericTurbulenceModel>
     ILaserPropagationChannel<stkobjects/ILaserPropagationChannel>
     ICommSystemLinkSelectionCriteria<stkobjects/ICommSystemLinkSelectionCriteria>
     ICommSystemAccessEventDetection<stkobjects/ICommSystemAccessEventDetection>
     ICommSystemAccessSamplingMethod<stkobjects/ICommSystemAccessSamplingMethod>
     ISRPModelBase<stkobjects/ISRPModelBase>
     IVehicleHPOPDragModel<stkobjects/IVehicleHPOPDragModel>
     IVehicleSGP4LoadData<stkobjects/IVehicleSGP4LoadData>
     IVehicleSolarFluxGeoMagnitude<stkobjects/IVehicleSolarFluxGeoMagnitude>
     IVehiclePropagator<stkobjects/IVehiclePropagator>
     IVehicleWaypointAltitudeReference<stkobjects/IVehicleWaypointAltitudeReference>
     IVehicleImpact<stkobjects/IVehicleImpact>
     IVehicleLaunchControl<stkobjects/IVehicleLaunchControl>
     IVehicleLaunch<stkobjects/IVehicleLaunch>
     IVehicleImpactLocation<stkobjects/IVehicleImpactLocation>
     IVehicleGPSAlmanacProperties<stkobjects/IVehicleGPSAlmanacProperties>
     IVehicleAttitudeProfile<stkobjects/IVehicleAttitudeProfile>
     IVehiclePointing<stkobjects/IVehiclePointing>
     IVehicleAttitude<stkobjects/IVehicleAttitude>
     IVehicleAttitudeStandard<stkobjects/IVehicleAttitudeStandard>
     IVehicleGraphics2DPass<stkobjects/IVehicleGraphics2DPass>
     IVehicleGraphics2DTimeEventType<stkobjects/IVehicleGraphics2DTimeEventType>
     IVehicleGraphics2DAttributes<stkobjects/IVehicleGraphics2DAttributes>
     IVehicleGraphics2DAttributesBasic<stkobjects/IVehicleGraphics2DAttributesBasic>
     IVehicleGraphics2DAttributesDisplayState<stkobjects/IVehicleGraphics2DAttributesDisplayState>
     IVehicleGraphics2DElevation<stkobjects/IVehicleGraphics2DElevation>
     IVehicleGraphics2DTimeComponentsElement<stkobjects/IVehicleGraphics2DTimeComponentsElement>
     IVehicleGraphics3DSystemsElementBase<stkobjects/IVehicleGraphics3DSystemsElementBase>
     IVehicleGraphics3DProximityAreaObject<stkobjects/IVehicleGraphics3DProximityAreaObject>
     IVehicleGraphics3DProximity<stkobjects/IVehicleGraphics3DProximity>
     IVehicleGraphics3DSigmaScale<stkobjects/IVehicleGraphics3DSigmaScale>
     IVehicleGraphics3DAttributes<stkobjects/IVehicleGraphics3DAttributes>
     IVehicleGraphics3DTickData<stkobjects/IVehicleGraphics3DTickData>
     IGreatArcGraphics<stkobjects/IGreatArcGraphics>
     IGreatArcGraphics3D<stkobjects/IGreatArcGraphics3D>
     IGreatArcVehicle<stkobjects/IGreatArcVehicle>
     IVehicleGraphics3DBPlaneTargetPointPosition<stkobjects/IVehicleGraphics3DBPlaneTargetPointPosition>
     IEOIR<stkobjects/IEOIR>
     IVehicleBreakAngle<stkobjects/IVehicleBreakAngle>
     IVehiclePassNumbering<stkobjects/IVehiclePassNumbering>
     IVehicleCoordinateAxes<stkobjects/IVehicleCoordinateAxes>
     IChainTimePeriodBase<stkobjects/IChainTimePeriodBase>
     ICoverageBounds<stkobjects/ICoverageBounds>
     ICoverageResolution<stkobjects/ICoverageResolution>
     IFigureOfMeritGraphics2DContours<stkobjects/IFigureOfMeritGraphics2DContours>
     IFigureOfMeritGraphics2DAttributes<stkobjects/IFigureOfMeritGraphics2DAttributes>
     IFigureOfMeritNavigationAccuracyMethod<stkobjects/IFigureOfMeritNavigationAccuracyMethod>
     IFigureOfMeritDefinitionData<stkobjects/IFigureOfMeritDefinitionData>
     IFigureOfMeritDefinitionResponseTime<stkobjects/IFigureOfMeritDefinitionResponseTime>
     IFigureOfMeritDefinitionDilutionOfPrecision<stkobjects/IFigureOfMeritDefinitionDilutionOfPrecision>
     IConstellationConstraintRestriction<stkobjects/IConstellationConstraintRestriction>
     IEventDetectionStrategy<stkobjects/IEventDetectionStrategy>
     ISamplingMethodStrategy<stkobjects/ISamplingMethodStrategy>
     IVehicleAttitudeSlewBase<stkobjects/IVehicleAttitudeSlewBase>
     IVolumetricGridDefinition<stkobjects/IVolumetricGridDefinition>
     IEOIRShapeObject<stkobjects/IEOIRShapeObject>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     StkObject<stkobjects/StkObject>
     StkObjectRoot<stkobjects/StkObjectRoot>
     LevelAttribute<stkobjects/LevelAttribute>
     LevelAttributeCollection<stkobjects/LevelAttributeCollection>
     BasicAzElMask<stkobjects/BasicAzElMask>
     FacilityGraphics<stkobjects/FacilityGraphics>
     PlaceGraphics<stkobjects/PlaceGraphics>
     Graphics2DRangeContours<stkobjects/Graphics2DRangeContours>
     AccessConstraint<stkobjects/AccessConstraint>
     AccessConstraintCollection<stkobjects/AccessConstraintCollection>
     Graphics3DRangeContours<stkobjects/Graphics3DRangeContours>
     Graphics3DOffsetRotate<stkobjects/Graphics3DOffsetRotate>
     Graphics3DOffsetTransformation<stkobjects/Graphics3DOffsetTransformation>
     Graphics3DOffsetAttach<stkobjects/Graphics3DOffsetAttach>
     Graphics3DOffsetLabel<stkobjects/Graphics3DOffsetLabel>
     Graphics3DOffset<stkobjects/Graphics3DOffset>
     Graphics3DMarkerShape<stkobjects/Graphics3DMarkerShape>
     Graphics3DMarkerFile<stkobjects/Graphics3DMarkerFile>
     Graphics3DMarker<stkobjects/Graphics3DMarker>
     Graphics3DDetailThreshold<stkobjects/Graphics3DDetailThreshold>
     Graphics3DModelItem<stkobjects/Graphics3DModelItem>
     Graphics3DModelCollection<stkobjects/Graphics3DModelCollection>
     LabelNote<stkobjects/LabelNote>
     LabelNoteCollection<stkobjects/LabelNoteCollection>
     Graphics3DVector<stkobjects/Graphics3DVector>
     FacilityGraphics3D<stkobjects/FacilityGraphics3D>
     PlaceGraphics3D<stkobjects/PlaceGraphics3D>
     TerrainNormSlopeAzimuth<stkobjects/TerrainNormSlopeAzimuth>
     IntervalCollection<stkobjects/IntervalCollection>
     ImmutableIntervalCollection<stkobjects/ImmutableIntervalCollection>
     DuringAccess<stkobjects/DuringAccess>
     DisplayTimesTimeComponent<stkobjects/DisplayTimesTimeComponent>
     StarGraphics3D<stkobjects/StarGraphics3D>
     StarGraphics<stkobjects/StarGraphics>
     PlanetGraphics3D<stkobjects/PlanetGraphics3D>
     PlanetGraphics<stkobjects/PlanetGraphics>
     AreaTypePattern<stkobjects/AreaTypePattern>
     AreaTypePatternCollection<stkobjects/AreaTypePatternCollection>
     AreaTypeEllipse<stkobjects/AreaTypeEllipse>
     AreaTargetGraphics3D<stkobjects/AreaTargetGraphics3D>
     AreaTargetGraphics<stkobjects/AreaTargetGraphics>
     Graphics3DAzElMask<stkobjects/Graphics3DAzElMask>
     Graphics3DModelArtic<stkobjects/Graphics3DModelArtic>
     Graphics3DModelTransformationCollection<stkobjects/Graphics3DModelTransformationCollection>
     Graphics3DModelTransformation<stkobjects/Graphics3DModelTransformation>
     Graphics3DModelFile<stkobjects/Graphics3DModelFile>
     PlanetPositionFile<stkobjects/PlanetPositionFile>
     PlanetPositionCentralBody<stkobjects/PlanetPositionCentralBody>
     PlanetOrbitDisplayTime<stkobjects/PlanetOrbitDisplayTime>
     Scenario<stkobjects/Scenario>
     ScenarioAnimation<stkobjects/ScenarioAnimation>
     ScenarioEarthData<stkobjects/ScenarioEarthData>
     ScenarioGraphics<stkobjects/ScenarioGraphics>
     TerrainCollection<stkobjects/TerrainCollection>
     Terrain<stkobjects/Terrain>
     TilesetCollection3D<stkobjects/TilesetCollection3D>
     Tileset3D<stkobjects/Tileset3D>
     ScenarioGenDatabaseCollection<stkobjects/ScenarioGenDatabaseCollection>
     ScenarioGenDatabase<stkobjects/ScenarioGenDatabase>
     ScenarioGraphics3D<stkobjects/ScenarioGraphics3D>
     SensorComplexConicPattern<stkobjects/SensorComplexConicPattern>
     SensorEOIRPattern<stkobjects/SensorEOIRPattern>
     SensorUnknownPattern<stkobjects/SensorUnknownPattern>
     SensorEOIRBandCollection<stkobjects/SensorEOIRBandCollection>
     SensorEOIRBand<stkobjects/SensorEOIRBand>
     SensorEOIRRadiometricPair<stkobjects/SensorEOIRRadiometricPair>
     SensorEOIRSensitivityCollection<stkobjects/SensorEOIRSensitivityCollection>
     SensorEOIRSaturationCollection<stkobjects/SensorEOIRSaturationCollection>
     SensorCustomPattern<stkobjects/SensorCustomPattern>
     SensorHalfPowerPattern<stkobjects/SensorHalfPowerPattern>
     SensorRectangularPattern<stkobjects/SensorRectangularPattern>
     SensorSARPattern<stkobjects/SensorSARPattern>
     SensorSimpleConicPattern<stkobjects/SensorSimpleConicPattern>
     SensorPointingFixed<stkobjects/SensorPointingFixed>
     SensorPointingFixedAxes<stkobjects/SensorPointingFixedAxes>
     SensorPointing3DModel<stkobjects/SensorPointing3DModel>
     SensorPointingSpinning<stkobjects/SensorPointingSpinning>
     SensorPointingTargeted<stkobjects/SensorPointingTargeted>
     SensorPointingExternal<stkobjects/SensorPointingExternal>
     SensorPointingTargetedBoresightTrack<stkobjects/SensorPointingTargetedBoresightTrack>
     SensorPointingTargetedBoresightFixed<stkobjects/SensorPointingTargetedBoresightFixed>
     SensorTargetCollection<stkobjects/SensorTargetCollection>
     SensorTarget<stkobjects/SensorTarget>
     AccessTime<stkobjects/AccessTime>
     ScheduleTime<stkobjects/ScheduleTime>
     SensorAzElMaskFile<stkobjects/SensorAzElMaskFile>
     SensorGraphics<stkobjects/SensorGraphics>
     SensorProjection<stkobjects/SensorProjection>
     SensorProjectionDisplayDistance<stkobjects/SensorProjectionDisplayDistance>
     SensorGraphics3D<stkobjects/SensorGraphics3D>
     SensorGraphics3DPulse<stkobjects/SensorGraphics3DPulse>
     SensorGraphics3DOffset<stkobjects/SensorGraphics3DOffset>
     AccessConstraintTimeSlipRange<stkobjects/AccessConstraintTimeSlipRange>
     AccessConstraintBackground<stkobjects/AccessConstraintBackground>
     AccessConstraintGroundTrack<stkobjects/AccessConstraintGroundTrack>
     AccessConstraintMinMax<stkobjects/AccessConstraintMinMax>
     AccessConstraintCrdnConstellation<stkobjects/AccessConstraintCrdnConstellation>
     AccessConstraintCentralBodyObstruction<stkobjects/AccessConstraintCentralBodyObstruction>
     AccessConstraintAngle<stkobjects/AccessConstraintAngle>
     AccessConstraintCondition<stkobjects/AccessConstraintCondition>
     AccessTimeCollection<stkobjects/AccessTimeCollection>
     ScheduleTimeCollection<stkobjects/ScheduleTimeCollection>
     AccessConstraintIntervals<stkobjects/AccessConstraintIntervals>
     AccessConstraintObjExAngle<stkobjects/AccessConstraintObjExAngle>
     AccessConstraintZone<stkobjects/AccessConstraintZone>
     AccessConstraintThirdBody<stkobjects/AccessConstraintThirdBody>
     AccessConstraintExclZonesCollection<stkobjects/AccessConstraintExclZonesCollection>
     AccessConstraintGrazingAltitude<stkobjects/AccessConstraintGrazingAltitude>
     SensorPointingGrazingAltitude<stkobjects/SensorPointingGrazingAltitude>
     AreaTarget<stkobjects/AreaTarget>
     Facility<stkobjects/Facility>
     Target<stkobjects/Target>
     Place<stkobjects/Place>
     Planet<stkobjects/Planet>
     Sensor<stkobjects/Sensor>
     SensorCommonTasks<stkobjects/SensorCommonTasks>
     AreaTargetCommonTasks<stkobjects/AreaTargetCommonTasks>
     PlanetCommonTasks<stkobjects/PlanetCommonTasks>
     Swath<stkobjects/Swath>
     Star<stkobjects/Star>
     DataProviderCollection<stkobjects/DataProviderCollection>
     DataProviderResultTimeArrayElements<stkobjects/DataProviderResultTimeArrayElements>
     DataProviderResult<stkobjects/DataProviderResult>
     DataProviderResultSubSectionCollection<stkobjects/DataProviderResultSubSectionCollection>
     DataProviderResultSubSection<stkobjects/DataProviderResultSubSection>
     DataProviderResultIntervalCollection<stkobjects/DataProviderResultIntervalCollection>
     DataProviderResultInterval<stkobjects/DataProviderResultInterval>
     DataProviderResultDataSetCollection<stkobjects/DataProviderResultDataSetCollection>
     DataProviderResultDataSet<stkobjects/DataProviderResultDataSet>
     DataProviderFixed<stkobjects/DataProviderFixed>
     DataProviderTimeVarying<stkobjects/DataProviderTimeVarying>
     DataProviderInterval<stkobjects/DataProviderInterval>
     DataProviderResultTextMessage<stkobjects/DataProviderResultTextMessage>
     DataProviderGroup<stkobjects/DataProviderGroup>
     DataProviderElements<stkobjects/DataProviderElements>
     DataProviderElement<stkobjects/DataProviderElement>
     DataProviders<stkobjects/DataProviders>
     StkAccess<stkobjects/StkAccess>
     StkAccessGraphics<stkobjects/StkAccessGraphics>
     StkAccessAdvanced<stkobjects/StkAccessAdvanced>
     AccessTimePeriod<stkobjects/AccessTimePeriod>
     AccessTimeEventIntervals<stkobjects/AccessTimeEventIntervals>
     StkObjectCoverage<stkobjects/StkObjectCoverage>
     ObjectCoverageFigureOfMerit<stkobjects/ObjectCoverageFigureOfMerit>
     Scenario3dFont<stkobjects/Scenario3dFont>
     Graphics3DBorderWall<stkobjects/Graphics3DBorderWall>
     Graphics3DReferenceAnalysisWorkbenchCollection<stkobjects/Graphics3DReferenceAnalysisWorkbenchCollection>
     Graphics3DReferenceVectorGeometryToolVector<stkobjects/Graphics3DReferenceVectorGeometryToolVector>
     Graphics3DReferenceVectorGeometryToolAxes<stkobjects/Graphics3DReferenceVectorGeometryToolAxes>
     Graphics3DReferenceVectorGeometryToolAngle<stkobjects/Graphics3DReferenceVectorGeometryToolAngle>
     Graphics3DReferenceVectorGeometryToolPlane<stkobjects/Graphics3DReferenceVectorGeometryToolPlane>
     Graphics3DReferenceVectorGeometryToolPoint<stkobjects/Graphics3DReferenceVectorGeometryToolPoint>
     TargetGraphics<stkobjects/TargetGraphics>
     TargetGraphics3D<stkobjects/TargetGraphics3D>
     PointTargetGraphics3DModel<stkobjects/PointTargetGraphics3DModel>
     ObjectLinkCollection<stkobjects/ObjectLinkCollection>
     ObjectLink<stkobjects/ObjectLink>
     LinkToObject<stkobjects/LinkToObject>
     LLAPosition<stkobjects/LLAPosition>
     Graphics3DDataDisplayElement<stkobjects/Graphics3DDataDisplayElement>
     Graphics3DDataDisplayCollection<stkobjects/Graphics3DDataDisplayCollection>
     VehicleInitialState<stkobjects/VehicleInitialState>
     VehicleHPOPCentralBodyGravity<stkobjects/VehicleHPOPCentralBodyGravity>
     VehicleRadiationPressure<stkobjects/VehicleRadiationPressure>
     VehicleHPOPSolarRadiationPressure<stkobjects/VehicleHPOPSolarRadiationPressure>
     VehicleSolarFluxGeoMagnitudeEnterManually<stkobjects/VehicleSolarFluxGeoMagnitudeEnterManually>
     VehicleSolarFluxGeoMagnitudeUseFile<stkobjects/VehicleSolarFluxGeoMagnitudeUseFile>
     VehicleHPOPForceModelDrag<stkobjects/VehicleHPOPForceModelDrag>
     VehicleHPOPForceModelDragOptions<stkobjects/VehicleHPOPForceModelDragOptions>
     VehicleHPOPSolarRadiationPressureOptions<stkobjects/VehicleHPOPSolarRadiationPressureOptions>
     VehicleStatic<stkobjects/VehicleStatic>
     VehicleSolidTides<stkobjects/VehicleSolidTides>
     VehicleOceanTides<stkobjects/VehicleOceanTides>
     VehiclePluginSettings<stkobjects/VehiclePluginSettings>
     VehiclePluginPropagator<stkobjects/VehiclePluginPropagator>
     VehicleHPOPForceModelMoreOptions<stkobjects/VehicleHPOPForceModelMoreOptions>
     VehicleHPOPForceModel<stkobjects/VehicleHPOPForceModel>
     VehicleStepSizeControl<stkobjects/VehicleStepSizeControl>
     VehicleTimeRegularization<stkobjects/VehicleTimeRegularization>
     VehicleInterpolation<stkobjects/VehicleInterpolation>
     VehicleIntegrator<stkobjects/VehicleIntegrator>
     VehicleGravity<stkobjects/VehicleGravity>
     VehiclePositionVelocityElement<stkobjects/VehiclePositionVelocityElement>
     VehiclePositionVelocityCollection<stkobjects/VehiclePositionVelocityCollection>
     VehicleCorrelationListCollection<stkobjects/VehicleCorrelationListCollection>
     VehicleCorrelationListElement<stkobjects/VehicleCorrelationListElement>
     VehicleCovariance<stkobjects/VehicleCovariance>
     VehicleJxInitialState<stkobjects/VehicleJxInitialState>
     VehicleLOPCentralBodyGravity<stkobjects/VehicleLOPCentralBodyGravity>
     VehicleThirdBodyGravityElement<stkobjects/VehicleThirdBodyGravityElement>
     VehicleThirdBodyGravityCollection<stkobjects/VehicleThirdBodyGravityCollection>
     VehicleExpDensModelParams<stkobjects/VehicleExpDensModelParams>
     VehicleAdvanced<stkobjects/VehicleAdvanced>
     VehicleLOPForceModelDrag<stkobjects/VehicleLOPForceModelDrag>
     VehicleLOPSolarRadiationPressure<stkobjects/VehicleLOPSolarRadiationPressure>
     VehiclePhysicalData<stkobjects/VehiclePhysicalData>
     VehicleLOPForceModel<stkobjects/VehicleLOPForceModel>
     VehicleSegmentsCollection<stkobjects/VehicleSegmentsCollection>
     VehiclePropagatorHPOP<stkobjects/VehiclePropagatorHPOP>
     VehiclePropagatorJ2Perturbation<stkobjects/VehiclePropagatorJ2Perturbation>
     VehiclePropagatorJ4Perturbation<stkobjects/VehiclePropagatorJ4Perturbation>
     VehiclePropagatorLOP<stkobjects/VehiclePropagatorLOP>
     VehiclePropagatorSGP4<stkobjects/VehiclePropagatorSGP4>
     VehiclePropagatorSPICE<stkobjects/VehiclePropagatorSPICE>
     VehiclePropagatorStkExternal<stkobjects/VehiclePropagatorStkExternal>
     VehiclePropagatorTwoBody<stkobjects/VehiclePropagatorTwoBody>
     VehiclePropagatorUserExternal<stkobjects/VehiclePropagatorUserExternal>
     VehicleLaunchVehicleInitialState<stkobjects/VehicleLaunchVehicleInitialState>
     VehiclePropagatorSimpleAscent<stkobjects/VehiclePropagatorSimpleAscent>
     VehicleWaypointsElement<stkobjects/VehicleWaypointsElement>
     VehicleWaypointsCollection<stkobjects/VehicleWaypointsCollection>
     VehicleLaunchLLA<stkobjects/VehicleLaunchLLA>
     VehicleLaunchLLR<stkobjects/VehicleLaunchLLR>
     VehicleImpactLLA<stkobjects/VehicleImpactLLA>
     VehicleImpactLLR<stkobjects/VehicleImpactLLR>
     VehicleLaunchControlFixedApogeeAltitude<stkobjects/VehicleLaunchControlFixedApogeeAltitude>
     VehicleLaunchControlFixedDeltaV<stkobjects/VehicleLaunchControlFixedDeltaV>
     VehicleLaunchControlFixedDeltaVMinEccentricity<stkobjects/VehicleLaunchControlFixedDeltaVMinEccentricity>
     VehicleLaunchControlFixedTimeOfFlight<stkobjects/VehicleLaunchControlFixedTimeOfFlight>
     VehicleImpactLocationLaunchAzEl<stkobjects/VehicleImpactLocationLaunchAzEl>
     VehicleImpactLocationPoint<stkobjects/VehicleImpactLocationPoint>
     VehiclePropagatorBallistic<stkobjects/VehiclePropagatorBallistic>
     VehiclePropagatorGreatArc<stkobjects/VehiclePropagatorGreatArc>
     VehicleSGP4SegmentCollection<stkobjects/VehicleSGP4SegmentCollection>
     VehicleSGP4Segment<stkobjects/VehicleSGP4Segment>
     VehicleThirdBodyGravity<stkobjects/VehicleThirdBodyGravity>
     VehicleConsiderAnalysisCollectionElement<stkobjects/VehicleConsiderAnalysisCollectionElement>
     VehicleConsiderAnalysisCollection<stkobjects/VehicleConsiderAnalysisCollection>
     VehicleSPICESegment<stkobjects/VehicleSPICESegment>
     VehicleWaypointAltitudeReferenceTerrain<stkobjects/VehicleWaypointAltitudeReferenceTerrain>
     VehicleWaypointAltitudeReference<stkobjects/VehicleWaypointAltitudeReference>
     VehicleSGP4LoadFile<stkobjects/VehicleSGP4LoadFile>
     VehicleSGP4OnlineLoad<stkobjects/VehicleSGP4OnlineLoad>
     VehicleSGP4OnlineAutoLoad<stkobjects/VehicleSGP4OnlineAutoLoad>
     VehicleGroundEllipsesCollection<stkobjects/VehicleGroundEllipsesCollection>
     Satellite<stkobjects/Satellite>
     VehicleInertia<stkobjects/VehicleInertia>
     VehicleMassProperties<stkobjects/VehicleMassProperties>
     VehicleBreakAngleBreakByLatitude<stkobjects/VehicleBreakAngleBreakByLatitude>
     VehicleBreakAngleBreakByLongitude<stkobjects/VehicleBreakAngleBreakByLongitude>
     VehicleDefinition<stkobjects/VehicleDefinition>
     VehicleRepeatGroundTrackNumbering<stkobjects/VehicleRepeatGroundTrackNumbering>
     VehiclePassNumberingDateOfFirstPass<stkobjects/VehiclePassNumberingDateOfFirstPass>
     VehiclePassNumberingFirstPassNum<stkobjects/VehiclePassNumberingFirstPassNum>
     VehiclePassBreak<stkobjects/VehiclePassBreak>
     VehicleCentralBodies<stkobjects/VehicleCentralBodies>
     SatelliteGraphics<stkobjects/SatelliteGraphics>
     SatelliteGraphics3D<stkobjects/SatelliteGraphics3D>
     VehicleEllipseDataElement<stkobjects/VehicleEllipseDataElement>
     VehicleEllipseDataCollection<stkobjects/VehicleEllipseDataCollection>
     VehicleGroundEllipseElement<stkobjects/VehicleGroundEllipseElement>
     SatelliteGraphics3DModel<stkobjects/SatelliteGraphics3DModel>
     VehicleEclipseBodies<stkobjects/VehicleEclipseBodies>
     VehicleVector<stkobjects/VehicleVector>
     VehicleRateOffset<stkobjects/VehicleRateOffset>
     VehicleProfileAlignedAndConstrained<stkobjects/VehicleProfileAlignedAndConstrained>
     VehicleProfileInertial<stkobjects/VehicleProfileInertial>
     VehicleProfileConstraintOffset<stkobjects/VehicleProfileConstraintOffset>
     VehicleProfileFixedInAxes<stkobjects/VehicleProfileFixedInAxes>
     VehicleProfilePrecessingSpin<stkobjects/VehicleProfilePrecessingSpin>
     VehicleProfileSpinAboutXXX<stkobjects/VehicleProfileSpinAboutXXX>
     VehicleProfileSpinning<stkobjects/VehicleProfileSpinning>
     VehicleProfileAlignmentOffset<stkobjects/VehicleProfileAlignmentOffset>
     VehicleScheduleTimesCollection<stkobjects/VehicleScheduleTimesCollection>
     VehicleTargetTimes<stkobjects/VehicleTargetTimes>
     VehicleAttitudePointing<stkobjects/VehicleAttitudePointing>
     VehicleDuration<stkobjects/VehicleDuration>
     VehicleStandardBasic<stkobjects/VehicleStandardBasic>
     VehicleAttitudeExternal<stkobjects/VehicleAttitudeExternal>
     VehicleAttitudeRealTime<stkobjects/VehicleAttitudeRealTime>
     VehicleProfileCoordinatedTurn<stkobjects/VehicleProfileCoordinatedTurn>
     VehicleProfileYawToNadir<stkobjects/VehicleProfileYawToNadir>
     VehicleAttitudeTrendControlAviator<stkobjects/VehicleAttitudeTrendControlAviator>
     VehicleProfileAviator<stkobjects/VehicleProfileAviator>
     VehicleTargetPointingElement<stkobjects/VehicleTargetPointingElement>
     VehicleTargetPointingCollection<stkobjects/VehicleTargetPointingCollection>
     VehicleTorque<stkobjects/VehicleTorque>
     VehicleIntegratedAttitude<stkobjects/VehicleIntegratedAttitude>
     VehicleScheduleTimesElement<stkobjects/VehicleScheduleTimesElement>
     VehicleTrajectoryAttitudeStandard<stkobjects/VehicleTrajectoryAttitudeStandard>
     VehicleOrbitAttitudeStandard<stkobjects/VehicleOrbitAttitudeStandard>
     VehicleRouteAttitudeStandard<stkobjects/VehicleRouteAttitudeStandard>
     VehicleGraphics2DLine<stkobjects/VehicleGraphics2DLine>
     VehicleGraphics2DIntervalsCollection<stkobjects/VehicleGraphics2DIntervalsCollection>
     VehicleGraphics2DAttributesAccess<stkobjects/VehicleGraphics2DAttributesAccess>
     VehicleGraphics2DAttributesCustom<stkobjects/VehicleGraphics2DAttributesCustom>
     VehicleGraphics2DAttributesRealtime<stkobjects/VehicleGraphics2DAttributesRealtime>
     VehicleGraphics2DLightingElement<stkobjects/VehicleGraphics2DLightingElement>
     VehicleGraphics2DLighting<stkobjects/VehicleGraphics2DLighting>
     VehicleGraphics2DElevationGroundElevation<stkobjects/VehicleGraphics2DElevationGroundElevation>
     VehicleGraphics2DElevationSwathHalfWidth<stkobjects/VehicleGraphics2DElevationSwathHalfWidth>
     VehicleGraphics2DElevationVehicleHalfAngle<stkobjects/VehicleGraphics2DElevationVehicleHalfAngle>
     VehicleGraphics2DSwath<stkobjects/VehicleGraphics2DSwath>
     VehicleGraphics2DLeadDataFraction<stkobjects/VehicleGraphics2DLeadDataFraction>
     VehicleGraphics2DLeadDataTime<stkobjects/VehicleGraphics2DLeadDataTime>
     VehicleGraphics2DTrailDataFraction<stkobjects/VehicleGraphics2DTrailDataFraction>
     VehicleGraphics2DTrailDataTime<stkobjects/VehicleGraphics2DTrailDataTime>
     VehicleGraphics2DRoutePassData<stkobjects/VehicleGraphics2DRoutePassData>
     VehicleGraphics2DLeadTrailData<stkobjects/VehicleGraphics2DLeadTrailData>
     VehicleGraphics2DOrbitPassData<stkobjects/VehicleGraphics2DOrbitPassData>
     VehicleGraphics2DTrajectoryPassData<stkobjects/VehicleGraphics2DTrajectoryPassData>
     VehicleGraphics2DTrajectoryResolution<stkobjects/VehicleGraphics2DTrajectoryResolution>
     VehicleGraphics2DGroundEllipsesCollection<stkobjects/VehicleGraphics2DGroundEllipsesCollection>
     VehicleGraphics2DTimeEventTypeLine<stkobjects/VehicleGraphics2DTimeEventTypeLine>
     VehicleGraphics2DTimeEventTypeMarker<stkobjects/VehicleGraphics2DTimeEventTypeMarker>
     VehicleGraphics2DTimeEventTypeText<stkobjects/VehicleGraphics2DTimeEventTypeText>
     VehicleGraphics2DTimeEventsElement<stkobjects/VehicleGraphics2DTimeEventsElement>
     VehicleGraphics2DTimeEventsCollection<stkobjects/VehicleGraphics2DTimeEventsCollection>
     VehicleGraphics2DPassShowPasses<stkobjects/VehicleGraphics2DPassShowPasses>
     VehicleGraphics2DPasses<stkobjects/VehicleGraphics2DPasses>
     VehicleGraphics2DSAA<stkobjects/VehicleGraphics2DSAA>
     VehicleGraphics2DElevationsElement<stkobjects/VehicleGraphics2DElevationsElement>
     VehicleGraphics2DElevationsCollection<stkobjects/VehicleGraphics2DElevationsCollection>
     VehicleGraphics2DElevContours<stkobjects/VehicleGraphics2DElevContours>
     VehicleGraphics2DRouteResolution<stkobjects/VehicleGraphics2DRouteResolution>
     VehicleGraphics2DWaypointMarkersElement<stkobjects/VehicleGraphics2DWaypointMarkersElement>
     VehicleGraphics2DWaypointMarkersCollection<stkobjects/VehicleGraphics2DWaypointMarkersCollection>
     VehicleGraphics2DWaypointMarker<stkobjects/VehicleGraphics2DWaypointMarker>
     VehicleGraphics2DInterval<stkobjects/VehicleGraphics2DInterval>
     VehicleGraphics2DPassResolution<stkobjects/VehicleGraphics2DPassResolution>
     VehicleGraphics2DGroundEllipsesElement<stkobjects/VehicleGraphics2DGroundEllipsesElement>
     VehicleGraphics2DAttributesRoute<stkobjects/VehicleGraphics2DAttributesRoute>
     VehicleGraphics2DAttributesTrajectory<stkobjects/VehicleGraphics2DAttributesTrajectory>
     VehicleGraphics2DAttributesOrbit<stkobjects/VehicleGraphics2DAttributesOrbit>
     Graphics3DPointableElementsElement<stkobjects/Graphics3DPointableElementsElement>
     Graphics3DPointableElementsCollection<stkobjects/Graphics3DPointableElementsCollection>
     VehicleGraphics3DSystemsElement<stkobjects/VehicleGraphics3DSystemsElement>
     VehicleGraphics3DSystemsSpecialElement<stkobjects/VehicleGraphics3DSystemsSpecialElement>
     VehicleGraphics3DSystemsCollection<stkobjects/VehicleGraphics3DSystemsCollection>
     VehicleGraphics3DEllipsoid<stkobjects/VehicleGraphics3DEllipsoid>
     VehicleGraphics3DControlBox<stkobjects/VehicleGraphics3DControlBox>
     VehicleGraphics3DBearingBox<stkobjects/VehicleGraphics3DBearingBox>
     VehicleGraphics3DBearingEllipse<stkobjects/VehicleGraphics3DBearingEllipse>
     VehicleGraphics3DLineOfBearing<stkobjects/VehicleGraphics3DLineOfBearing>
     VehicleGraphics3DGeoBox<stkobjects/VehicleGraphics3DGeoBox>
     VehicleGraphics3DRouteProximity<stkobjects/VehicleGraphics3DRouteProximity>
     VehicleGraphics3DOrbitProximity<stkobjects/VehicleGraphics3DOrbitProximity>
     VehicleGraphics3DElevContours<stkobjects/VehicleGraphics3DElevContours>
     VehicleGraphics3DSAA<stkobjects/VehicleGraphics3DSAA>
     VehicleGraphics3DSigmaScaleProbability<stkobjects/VehicleGraphics3DSigmaScaleProbability>
     VehicleGraphics3DSigmaScaleScale<stkobjects/VehicleGraphics3DSigmaScaleScale>
     VehicleGraphics3DDefaultAttributes<stkobjects/VehicleGraphics3DDefaultAttributes>
     VehicleGraphics3DIntervalsElement<stkobjects/VehicleGraphics3DIntervalsElement>
     VehicleGraphics3DIntervalsCollection<stkobjects/VehicleGraphics3DIntervalsCollection>
     VehicleGraphics3DAttributesBasic<stkobjects/VehicleGraphics3DAttributesBasic>
     VehicleGraphics3DAttributesIntervals<stkobjects/VehicleGraphics3DAttributesIntervals>
     VehicleGraphics3DSize<stkobjects/VehicleGraphics3DSize>
     VehicleGraphics3DCovariancePointingContour<stkobjects/VehicleGraphics3DCovariancePointingContour>
     VehicleGraphics3DDataFraction<stkobjects/VehicleGraphics3DDataFraction>
     VehicleGraphics3DDataTime<stkobjects/VehicleGraphics3DDataTime>
     VehicleGraphics3DOrbitPassData<stkobjects/VehicleGraphics3DOrbitPassData>
     VehicleGraphics3DOrbitTrackData<stkobjects/VehicleGraphics3DOrbitTrackData>
     VehicleGraphics3DTickDataLine<stkobjects/VehicleGraphics3DTickDataLine>
     VehicleGraphics3DTickDataPoint<stkobjects/VehicleGraphics3DTickDataPoint>
     VehicleGraphics3DOrbitTickMarks<stkobjects/VehicleGraphics3DOrbitTickMarks>
     VehicleGraphics3DPass<stkobjects/VehicleGraphics3DPass>
     VehicleGraphics3DCovariance<stkobjects/VehicleGraphics3DCovariance>
     VehicleGraphics3DVelCovariance<stkobjects/VehicleGraphics3DVelCovariance>
     VehicleGraphics3DTrajectoryProximity<stkobjects/VehicleGraphics3DTrajectoryProximity>
     VehicleGraphics3DTrajectory<stkobjects/VehicleGraphics3DTrajectory>
     VehicleGraphics3DTrajectoryTrackData<stkobjects/VehicleGraphics3DTrajectoryTrackData>
     VehicleGraphics3DTrajectoryPassData<stkobjects/VehicleGraphics3DTrajectoryPassData>
     VehicleGraphics3DLeadTrailData<stkobjects/VehicleGraphics3DLeadTrailData>
     VehicleGraphics3DTrajectoryTickMarks<stkobjects/VehicleGraphics3DTrajectoryTickMarks>
     VehicleGraphics3DPathTickMarks<stkobjects/VehicleGraphics3DPathTickMarks>
     VehicleGraphics3DWaypointMarkersElement<stkobjects/VehicleGraphics3DWaypointMarkersElement>
     VehicleGraphics3DWaypointMarkersCollection<stkobjects/VehicleGraphics3DWaypointMarkersCollection>
     VehicleGraphics3DRoute<stkobjects/VehicleGraphics3DRoute>
     Graphics3DModelPointing<stkobjects/Graphics3DModelPointing>
     Graphics3DLabelSwapDistance<stkobjects/Graphics3DLabelSwapDistance>
     VehicleGraphics3DDropLinePositionItem<stkobjects/VehicleGraphics3DDropLinePositionItem>
     VehicleGraphics3DDropLinePositionItemCollection<stkobjects/VehicleGraphics3DDropLinePositionItemCollection>
     VehicleGraphics3DDropLinePathItem<stkobjects/VehicleGraphics3DDropLinePathItem>
     VehicleGraphics3DDropLinePathItemCollection<stkobjects/VehicleGraphics3DDropLinePathItemCollection>
     VehicleGraphics3DOrbitDropLines<stkobjects/VehicleGraphics3DOrbitDropLines>
     VehicleGraphics3DRouteDropLines<stkobjects/VehicleGraphics3DRouteDropLines>
     VehicleGraphics3DTrajectoryDropLines<stkobjects/VehicleGraphics3DTrajectoryDropLines>
     VehicleTrajectoryGraphics3DModel<stkobjects/VehicleTrajectoryGraphics3DModel>
     VehicleRouteGraphics3DModel<stkobjects/VehicleRouteGraphics3DModel>
     VehicleGraphics3DBPlaneTemplateDisplayElement<stkobjects/VehicleGraphics3DBPlaneTemplateDisplayElement>
     VehicleGraphics3DBPlaneTemplateDisplayCollection<stkobjects/VehicleGraphics3DBPlaneTemplateDisplayCollection>
     VehicleGraphics3DBPlaneTemplate<stkobjects/VehicleGraphics3DBPlaneTemplate>
     VehicleGraphics3DBPlaneTemplatesCollection<stkobjects/VehicleGraphics3DBPlaneTemplatesCollection>
     VehicleGraphics3DBPlaneEvent<stkobjects/VehicleGraphics3DBPlaneEvent>
     VehicleGraphics3DBPlanePoint<stkobjects/VehicleGraphics3DBPlanePoint>
     VehicleGraphics3DBPlaneTargetPointPositionCartesian<stkobjects/VehicleGraphics3DBPlaneTargetPointPositionCartesian>
     VehicleGraphics3DBPlaneTargetPointPositionPolar<stkobjects/VehicleGraphics3DBPlaneTargetPointPositionPolar>
     VehicleGraphics3DBPlaneTargetPoint<stkobjects/VehicleGraphics3DBPlaneTargetPoint>
     VehicleGraphics3DBPlaneInstance<stkobjects/VehicleGraphics3DBPlaneInstance>
     VehicleGraphics3DBPlaneInstancesCollection<stkobjects/VehicleGraphics3DBPlaneInstancesCollection>
     VehicleGraphics3DBPlanePointCollection<stkobjects/VehicleGraphics3DBPlanePointCollection>
     VehicleGraphics3DBPlanes<stkobjects/VehicleGraphics3DBPlanes>
     LaunchVehicle<stkobjects/LaunchVehicle>
     LaunchVehicleGraphics<stkobjects/LaunchVehicleGraphics>
     LaunchVehicleGraphics3D<stkobjects/LaunchVehicleGraphics3D>
     GroundVehicle<stkobjects/GroundVehicle>
     GroundVehicleGraphics<stkobjects/GroundVehicleGraphics>
     GroundVehicleGraphics3D<stkobjects/GroundVehicleGraphics3D>
     Missile<stkobjects/Missile>
     MissileGraphics<stkobjects/MissileGraphics>
     MissileGraphics3D<stkobjects/MissileGraphics3D>
     Aircraft<stkobjects/Aircraft>
     AircraftGraphics<stkobjects/AircraftGraphics>
     AircraftGraphics3D<stkobjects/AircraftGraphics3D>
     Ship<stkobjects/Ship>
     ShipGraphics<stkobjects/ShipGraphics>
     ShipGraphics3D<stkobjects/ShipGraphics3D>
     MtoTrackPoint<stkobjects/MtoTrackPoint>
     MtoTrackPointCollection<stkobjects/MtoTrackPointCollection>
     MtoTrack<stkobjects/MtoTrack>
     MtoTrackCollection<stkobjects/MtoTrackCollection>
     MtoDefaultTrack<stkobjects/MtoDefaultTrack>
     MtoGlobalTrackOptions<stkobjects/MtoGlobalTrackOptions>
     Mto<stkobjects/Mto>
     MtoGraphics2DMarker<stkobjects/MtoGraphics2DMarker>
     MtoGraphics2DLine<stkobjects/MtoGraphics2DLine>
     MtoGraphics2DFadeTimes<stkobjects/MtoGraphics2DFadeTimes>
     MtoGraphics2DLeadTrailTimes<stkobjects/MtoGraphics2DLeadTrailTimes>
     MtoGraphics2DTrack<stkobjects/MtoGraphics2DTrack>
     MtoGraphics2DTrackCollection<stkobjects/MtoGraphics2DTrackCollection>
     MtoDefaultGraphics2DTrack<stkobjects/MtoDefaultGraphics2DTrack>
     MtoGraphics2DGlobalTrackOptions<stkobjects/MtoGraphics2DGlobalTrackOptions>
     MtoGraphics<stkobjects/MtoGraphics>
     MtoGraphics3DMarker<stkobjects/MtoGraphics3DMarker>
     MtoGraphics3DPoint<stkobjects/MtoGraphics3DPoint>
     MtoGraphics3DModel<stkobjects/MtoGraphics3DModel>
     MtoGraphics3DSwapDistances<stkobjects/MtoGraphics3DSwapDistances>
     MtoGraphics3DDropLines<stkobjects/MtoGraphics3DDropLines>
     MtoGraphics3DTrack<stkobjects/MtoGraphics3DTrack>
     MtoGraphics3DTrackCollection<stkobjects/MtoGraphics3DTrackCollection>
     MtoDefaultGraphics3DTrack<stkobjects/MtoDefaultGraphics3DTrack>
     MtoGraphics3DGlobalTrackOptions<stkobjects/MtoGraphics3DGlobalTrackOptions>
     MtoGraphics3D<stkobjects/MtoGraphics3D>
     LLAGeocentric<stkobjects/LLAGeocentric>
     LLAGeodetic<stkobjects/LLAGeodetic>
     LineTargetPoint<stkobjects/LineTargetPoint>
     LineTargetPointCollection<stkobjects/LineTargetPointCollection>
     LineTarget<stkobjects/LineTarget>
     LineTargetGraphics<stkobjects/LineTargetGraphics>
     LineTargetGraphics3D<stkobjects/LineTargetGraphics3D>
     CoverageDefinition<stkobjects/CoverageDefinition>
     CoverageBoundsCustomRegions<stkobjects/CoverageBoundsCustomRegions>
     CoverageBoundsCustomBoundary<stkobjects/CoverageBoundsCustomBoundary>
     CoverageBoundsGlobal<stkobjects/CoverageBoundsGlobal>
     CoverageBoundsLat<stkobjects/CoverageBoundsLat>
     CoverageBoundsLatLine<stkobjects/CoverageBoundsLatLine>
     CoverageBoundsLonLine<stkobjects/CoverageBoundsLonLine>
     CoverageBoundsLatLonRegion<stkobjects/CoverageBoundsLatLonRegion>
     CoverageGrid<stkobjects/CoverageGrid>
     CoverageAssetListElement<stkobjects/CoverageAssetListElement>
     CoverageAssetListCollection<stkobjects/CoverageAssetListCollection>
     CoverageRegionFilesCollection<stkobjects/CoverageRegionFilesCollection>
     CoverageAreaTargetsCollection<stkobjects/CoverageAreaTargetsCollection>
     CoveragePointDefinition<stkobjects/CoveragePointDefinition>
     CoveragePointFileListCollection<stkobjects/CoveragePointFileListCollection>
     CoverageAdvanced<stkobjects/CoverageAdvanced>
     CoverageInterval<stkobjects/CoverageInterval>
     CoverageResolutionArea<stkobjects/CoverageResolutionArea>
     CoverageResolutionDistance<stkobjects/CoverageResolutionDistance>
     CoverageResolutionLatLon<stkobjects/CoverageResolutionLatLon>
     CoverageGraphics2DStatic<stkobjects/CoverageGraphics2DStatic>
     CoverageGraphics2DAnimation<stkobjects/CoverageGraphics2DAnimation>
     CoverageGraphics2DProgress<stkobjects/CoverageGraphics2DProgress>
     CoverageGraphics<stkobjects/CoverageGraphics>
     CoverageGraphics3D<stkobjects/CoverageGraphics3D>
     CoverageGraphics3DAttributes<stkobjects/CoverageGraphics3DAttributes>
     ChainTimePeriodBase<stkobjects/ChainTimePeriodBase>
     ChainUserSpecifiedTimePeriod<stkobjects/ChainUserSpecifiedTimePeriod>
     ChainConstraints<stkobjects/ChainConstraints>
     Chain<stkobjects/Chain>
     ChainConnection<stkobjects/ChainConnection>
     ChainConnectionCollection<stkobjects/ChainConnectionCollection>
     ChainOptimalStrandOpts<stkobjects/ChainOptimalStrandOpts>
     ChainGraphics2DStatic<stkobjects/ChainGraphics2DStatic>
     ChainGraphics2DAnimation<stkobjects/ChainGraphics2DAnimation>
     ChainGraphics<stkobjects/ChainGraphics>
     ChainGraphics3D<stkobjects/ChainGraphics3D>
     RefractionCoefficients<stkobjects/RefractionCoefficients>
     RefractionModelEffectiveRadiusMethod<stkobjects/RefractionModelEffectiveRadiusMethod>
     RefractionModelITURP8344<stkobjects/RefractionModelITURP8344>
     RefractionModelSCFMethod<stkobjects/RefractionModelSCFMethod>
     FigureOfMeritDefinitionCompute<stkobjects/FigureOfMeritDefinitionCompute>
     FigureOfMeritDefinitionDataMinMax<stkobjects/FigureOfMeritDefinitionDataMinMax>
     FigureOfMeritDefinitionDataMinAssets<stkobjects/FigureOfMeritDefinitionDataMinAssets>
     FigureOfMeritDefinitionDataPercentLevel<stkobjects/FigureOfMeritDefinitionDataPercentLevel>
     FigureOfMeritDefinitionDataBestN<stkobjects/FigureOfMeritDefinitionDataBestN>
     FigureOfMeritDefinitionDataBest4<stkobjects/FigureOfMeritDefinitionDataBest4>
     FigureOfMeritDefinitionAccessConstraint<stkobjects/FigureOfMeritDefinitionAccessConstraint>
     FigureOfMeritSatisfaction<stkobjects/FigureOfMeritSatisfaction>
     FigureOfMerit<stkobjects/FigureOfMerit>
     FigureOfMeritDefinitionAccessSeparation<stkobjects/FigureOfMeritDefinitionAccessSeparation>
     FigureOfMeritDefinitionDilutionOfPrecision<stkobjects/FigureOfMeritDefinitionDilutionOfPrecision>
     FigureOfMeritDefinitionNavigationAccuracy<stkobjects/FigureOfMeritDefinitionNavigationAccuracy>
     FigureOfMeritAssetListElement<stkobjects/FigureOfMeritAssetListElement>
     FigureOfMeritAssetListCollection<stkobjects/FigureOfMeritAssetListCollection>
     FigureOfMeritUncertainties<stkobjects/FigureOfMeritUncertainties>
     FigureOfMeritDefinitionResponseTime<stkobjects/FigureOfMeritDefinitionResponseTime>
     FigureOfMeritDefinitionRevisitTime<stkobjects/FigureOfMeritDefinitionRevisitTime>
     FigureOfMeritDefinitionSimpleCoverage<stkobjects/FigureOfMeritDefinitionSimpleCoverage>
     FigureOfMeritDefinitionTimeAverageGap<stkobjects/FigureOfMeritDefinitionTimeAverageGap>
     FigureOfMeritDefinitionSystemAgeOfData<stkobjects/FigureOfMeritDefinitionSystemAgeOfData>
     FigureOfMeritGraphics2DContours<stkobjects/FigureOfMeritGraphics2DContours>
     FigureOfMeritGraphics2DAttributes<stkobjects/FigureOfMeritGraphics2DAttributes>
     FigureOfMeritGraphics2DContoursAnimation<stkobjects/FigureOfMeritGraphics2DContoursAnimation>
     FigureOfMeritGraphics2DAttributesAnimation<stkobjects/FigureOfMeritGraphics2DAttributesAnimation>
     FigureOfMeritGraphics<stkobjects/FigureOfMeritGraphics>
     FigureOfMeritGraphics2DRampColor<stkobjects/FigureOfMeritGraphics2DRampColor>
     FigureOfMeritGraphics2DLevelAttributesElement<stkobjects/FigureOfMeritGraphics2DLevelAttributesElement>
     FigureOfMeritGraphics2DLevelAttributesCollection<stkobjects/FigureOfMeritGraphics2DLevelAttributesCollection>
     FigureOfMeritGraphics2DPositionOnMap<stkobjects/FigureOfMeritGraphics2DPositionOnMap>
     FigureOfMeritGraphics2DColorOptions<stkobjects/FigureOfMeritGraphics2DColorOptions>
     FigureOfMeritGraphics2DLegendWindow<stkobjects/FigureOfMeritGraphics2DLegendWindow>
     FigureOfMeritGraphics3DLegendWindow<stkobjects/FigureOfMeritGraphics3DLegendWindow>
     FigureOfMeritGraphics2DTextOptions<stkobjects/FigureOfMeritGraphics2DTextOptions>
     FigureOfMeritGraphics2DRangeColorOptions<stkobjects/FigureOfMeritGraphics2DRangeColorOptions>
     FigureOfMeritGraphics2DLegend<stkobjects/FigureOfMeritGraphics2DLegend>
     FigureOfMeritNavigationAccuracyMethodElevationAngle<stkobjects/FigureOfMeritNavigationAccuracyMethodElevationAngle>
     FigureOfMeritNavigationAccuracyMethodConstant<stkobjects/FigureOfMeritNavigationAccuracyMethodConstant>
     FigureOfMeritGraphics3DAttributes<stkobjects/FigureOfMeritGraphics3DAttributes>
     FigureOfMeritGraphics3D<stkobjects/FigureOfMeritGraphics3D>
     VehicleProfileGPS<stkobjects/VehicleProfileGPS>
     StkObjectModelContext<stkobjects/StkObjectModelContext>
     StdMilitary2525bSymbols<stkobjects/StdMilitary2525bSymbols>
     CoverageGridInspector<stkobjects/CoverageGridInspector>
     FigureOfMeritGridInspector<stkobjects/FigureOfMeritGridInspector>
     Graphics3DVaporTrail<stkobjects/Graphics3DVaporTrail>
     VehicleTargetPointingIntervalCollection<stkobjects/VehicleTargetPointingIntervalCollection>
     AccessConstraintPluginMinMax<stkobjects/AccessConstraintPluginMinMax>
     ConstellationConstraints<stkobjects/ConstellationConstraints>
     ConstellationConstraintObjectRestriction<stkobjects/ConstellationConstraintObjectRestriction>
     ConstellationConstraintRestriction<stkobjects/ConstellationConstraintRestriction>
     Constellation<stkobjects/Constellation>
     ConstellationGraphics<stkobjects/ConstellationGraphics>
     ConstellationRouting<stkobjects/ConstellationRouting>
     EventDetectionNoSubSampling<stkobjects/EventDetectionNoSubSampling>
     EventDetectionSubSampling<stkobjects/EventDetectionSubSampling>
     SamplingMethodAdaptive<stkobjects/SamplingMethodAdaptive>
     SamplingMethodFixedStep<stkobjects/SamplingMethodFixedStep>
     SensorAccessAdvanced<stkobjects/SensorAccessAdvanced>
     VehicleAccessAdvanced<stkobjects/VehicleAccessAdvanced>
     AccessSampling<stkobjects/AccessSampling>
     AccessEventDetection<stkobjects/AccessEventDetection>
     SensorGraphics3DProjectionElement<stkobjects/SensorGraphics3DProjectionElement>
     SensorGraphics3DSpaceProjectionCollection<stkobjects/SensorGraphics3DSpaceProjectionCollection>
     SensorGraphics3DTargetProjectionCollection<stkobjects/SensorGraphics3DTargetProjectionCollection>
     CentralBodyTerrainCollectionElement<stkobjects/CentralBodyTerrainCollectionElement>
     CentralBodyTerrainCollection<stkobjects/CentralBodyTerrainCollection>
     SatelliteExportTools<stkobjects/SatelliteExportTools>
     LaunchVehicleExportTools<stkobjects/LaunchVehicleExportTools>
     GroundVehicleExportTools<stkobjects/GroundVehicleExportTools>
     MissileExportTools<stkobjects/MissileExportTools>
     AircraftExportTools<stkobjects/AircraftExportTools>
     ShipExportTools<stkobjects/ShipExportTools>
     VehicleEphemerisCode500ExportTool<stkobjects/VehicleEphemerisCode500ExportTool>
     VehicleEphemerisCCSDSExportTool<stkobjects/VehicleEphemerisCCSDSExportTool>
     VehicleEphemerisStkExportTool<stkobjects/VehicleEphemerisStkExportTool>
     VehicleEphemerisSpiceExportTool<stkobjects/VehicleEphemerisSpiceExportTool>
     ExportToolTimePeriod<stkobjects/ExportToolTimePeriod>
     VehicleAttitudeExportTool<stkobjects/VehicleAttitudeExportTool>
     VehiclePropagationDefinitionExportTool<stkobjects/VehiclePropagationDefinitionExportTool>
     VehicleCoordinateAxesCustom<stkobjects/VehicleCoordinateAxesCustom>
     ExportToolStepSize<stkobjects/ExportToolStepSize>
     PctCmpltEventArgs<stkobjects/PctCmpltEventArgs>
     StkObjectChangedEventArgs<stkobjects/StkObjectChangedEventArgs>
     VehicleEclipsingBodies<stkobjects/VehicleEclipsingBodies>
     LocationVectorGeometryToolPoint<stkobjects/LocationVectorGeometryToolPoint>
     TimePeriod<stkobjects/TimePeriod>
     TimePeriodValue<stkobjects/TimePeriodValue>
     SpatialState<stkobjects/SpatialState>
     VehicleSpatialInfo<stkobjects/VehicleSpatialInfo>
     OnePointAccess<stkobjects/OnePointAccess>
     OnePointAccessResultCollection<stkobjects/OnePointAccessResultCollection>
     OnePointAccessResult<stkobjects/OnePointAccessResult>
     OnePointAccessConstraintCollection<stkobjects/OnePointAccessConstraintCollection>
     OnePointAccessConstraint<stkobjects/OnePointAccessConstraint>
     VehiclePropagatorRealtime<stkobjects/VehiclePropagatorRealtime>
     VehicleRealtimePointBuilder<stkobjects/VehicleRealtimePointBuilder>
     VehicleRealtimeCartesianPoints<stkobjects/VehicleRealtimeCartesianPoints>
     VehicleRealtimeLLAHPSPoints<stkobjects/VehicleRealtimeLLAHPSPoints>
     VehicleRealtimeLLAPoints<stkobjects/VehicleRealtimeLLAPoints>
     VehicleRealtimeUTMPoints<stkobjects/VehicleRealtimeUTMPoints>
     SRPModelGPS<stkobjects/SRPModelGPS>
     SRPModelSpherical<stkobjects/SRPModelSpherical>
     SRPModelPlugin<stkobjects/SRPModelPlugin>
     SRPModelPluginSettings<stkobjects/SRPModelPluginSettings>
     VehicleHPOPSRPModel<stkobjects/VehicleHPOPSRPModel>
     VehicleHPOPDragModelSpherical<stkobjects/VehicleHPOPDragModelSpherical>
     VehicleHPOPDragModelPlugin<stkobjects/VehicleHPOPDragModelPlugin>
     VehicleHPOPDragModelPluginSettings<stkobjects/VehicleHPOPDragModelPluginSettings>
     VehicleHPOPDragModel<stkobjects/VehicleHPOPDragModel>
     ScenarioAnimationTimePeriod<stkobjects/ScenarioAnimationTimePeriod>
     SensorProjectionConstantAltitude<stkobjects/SensorProjectionConstantAltitude>
     SensorProjectionObjectAltitude<stkobjects/SensorProjectionObjectAltitude>
     VehicleAttitudeRealTimeDataReference<stkobjects/VehicleAttitudeRealTimeDataReference>
     MtoAnalysis<stkobjects/MtoAnalysis>
     MtoAnalysisPosition<stkobjects/MtoAnalysisPosition>
     MtoAnalysisRange<stkobjects/MtoAnalysisRange>
     MtoAnalysisFieldOfView<stkobjects/MtoAnalysisFieldOfView>
     MtoAnalysisVisibility<stkobjects/MtoAnalysisVisibility>
     VehiclePropagatorGPS<stkobjects/VehiclePropagatorGPS>
     AvailableFeatures<stkobjects/AvailableFeatures>
     ScenarioBeforeSaveEventArgs<stkobjects/ScenarioBeforeSaveEventArgs>
     StkObjectPreDeleteEventArgs<stkobjects/StkObjectPreDeleteEventArgs>
     VehiclePropagatorSGP4CommonTasks<stkobjects/VehiclePropagatorSGP4CommonTasks>
     VehicleSGP4AutoUpdateProperties<stkobjects/VehicleSGP4AutoUpdateProperties>
     VehicleSGP4AutoUpdateFileSource<stkobjects/VehicleSGP4AutoUpdateFileSource>
     VehicleSGP4AutoUpdateOnlineSource<stkobjects/VehicleSGP4AutoUpdateOnlineSource>
     VehicleSGP4AutoUpdate<stkobjects/VehicleSGP4AutoUpdate>
     VehicleSGP4PropagatorSettings<stkobjects/VehicleSGP4PropagatorSettings>
     VehicleGPSAutoUpdateProperties<stkobjects/VehicleGPSAutoUpdateProperties>
     VehicleGPSAutoUpdateFileSource<stkobjects/VehicleGPSAutoUpdateFileSource>
     VehicleGPSAutoUpdateOnlineSource<stkobjects/VehicleGPSAutoUpdateOnlineSource>
     VehicleGPSAutoUpdate<stkobjects/VehicleGPSAutoUpdate>
     VehicleGPSSpecifyAlmanac<stkobjects/VehicleGPSSpecifyAlmanac>
     VehicleGPSAlmanacProperties<stkobjects/VehicleGPSAlmanacProperties>
     VehicleGPSAlmanacPropertiesSEM<stkobjects/VehicleGPSAlmanacPropertiesSEM>
     VehicleGPSAlmanacPropertiesYUMA<stkobjects/VehicleGPSAlmanacPropertiesYUMA>
     VehicleGPSAlmanacPropertiesSP3<stkobjects/VehicleGPSAlmanacPropertiesSP3>
     VehicleGPSElementCollection<stkobjects/VehicleGPSElementCollection>
     VehicleGPSElement<stkobjects/VehicleGPSElement>
     SpaceEnvironmentRadEnergyMethodSpecify<stkobjects/SpaceEnvironmentRadEnergyMethodSpecify>
     SpaceEnvironmentRadEnergyValues<stkobjects/SpaceEnvironmentRadEnergyValues>
     SpaceEnvironmentRadiationEnvironment<stkobjects/SpaceEnvironmentRadiationEnvironment>
     SpaceEnvironmentMagnitudeFieldGraphics2D<stkobjects/SpaceEnvironmentMagnitudeFieldGraphics2D>
     SpaceEnvironmentScenarioExtGraphics3D<stkobjects/SpaceEnvironmentScenarioExtGraphics3D>
     ScenSpaceEnvironment<stkobjects/ScenSpaceEnvironment>
     VehicleSpaceEnvironmentRadDoseRateElement<stkobjects/VehicleSpaceEnvironmentRadDoseRateElement>
     VehicleSpaceEnvironmentRadDoseRateCollection<stkobjects/VehicleSpaceEnvironmentRadDoseRateCollection>
     SpaceEnvironmentSAAContour<stkobjects/SpaceEnvironmentSAAContour>
     VehicleSpaceEnvironmentVehTemperature<stkobjects/VehicleSpaceEnvironmentVehTemperature>
     VehicleSpaceEnvironmentParticleFlux<stkobjects/VehicleSpaceEnvironmentParticleFlux>
     VehicleSpaceEnvironmentMagneticField<stkobjects/VehicleSpaceEnvironmentMagneticField>
     VehicleSpaceEnvironmentRadiation<stkobjects/VehicleSpaceEnvironmentRadiation>
     VehicleSpaceEnvironmentMagnitudeFieldLine<stkobjects/VehicleSpaceEnvironmentMagnitudeFieldLine>
     VehicleSpaceEnvironmentGraphics<stkobjects/VehicleSpaceEnvironmentGraphics>
     VehicleSpaceEnvironment<stkobjects/VehicleSpaceEnvironment>
     CoverageSelectedGridPoint<stkobjects/CoverageSelectedGridPoint>
     CoverageGridPointSelection<stkobjects/CoverageGridPointSelection>
     CelestialBodyCollection<stkobjects/CelestialBodyCollection>
     CelestialBodyInfo<stkobjects/CelestialBodyInfo>
     StkCentralBodyEllipsoid<stkobjects/StkCentralBodyEllipsoid>
     StkCentralBody<stkobjects/StkCentralBody>
     StkCentralBodyCollection<stkobjects/StkCentralBodyCollection>
     FigureOfMeritDefinitionSystemResponseTime<stkobjects/FigureOfMeritDefinitionSystemResponseTime>
     FigureOfMeritDefinitionAgeOfData<stkobjects/FigureOfMeritDefinitionAgeOfData>
     FigureOfMeritDefinitionScalarCalculation<stkobjects/FigureOfMeritDefinitionScalarCalculation>
     VehiclePropagator11ParamDescriptor<stkobjects/VehiclePropagator11ParamDescriptor>
     VehiclePropagator11ParamDescriptorCollection<stkobjects/VehiclePropagator11ParamDescriptorCollection>
     VehiclePropagator11Param<stkobjects/VehiclePropagator11Param>
     VehiclePropagatorSP3File<stkobjects/VehiclePropagatorSP3File>
     VehiclePropagatorSP3FileCollection<stkobjects/VehiclePropagatorSP3FileCollection>
     VehiclePropagatorSP3<stkobjects/VehiclePropagatorSP3>
     VehicleEphemerisStkBinaryExportTool<stkobjects/VehicleEphemerisStkBinaryExportTool>
     OrbitState<stkobjects/OrbitState>
     OrbitStateCoordinateSystem<stkobjects/OrbitStateCoordinateSystem>
     OrbitStateCartesian<stkobjects/OrbitStateCartesian>
     ClassicalSizeShapeAltitude<stkobjects/ClassicalSizeShapeAltitude>
     ClassicalSizeShapeMeanMotion<stkobjects/ClassicalSizeShapeMeanMotion>
     ClassicalSizeShapePeriod<stkobjects/ClassicalSizeShapePeriod>
     ClassicalSizeShapeRadius<stkobjects/ClassicalSizeShapeRadius>
     ClassicalSizeShapeSemimajorAxis<stkobjects/ClassicalSizeShapeSemimajorAxis>
     OrientationAscNodeLAN<stkobjects/OrientationAscNodeLAN>
     OrientationAscNodeRAAN<stkobjects/OrientationAscNodeRAAN>
     ClassicalOrientation<stkobjects/ClassicalOrientation>
     ClassicalLocationArgumentOfLatitude<stkobjects/ClassicalLocationArgumentOfLatitude>
     ClassicalLocationEccentricAnomaly<stkobjects/ClassicalLocationEccentricAnomaly>
     ClassicalLocationMeanAnomaly<stkobjects/ClassicalLocationMeanAnomaly>
     ClassicalLocationTimePastAN<stkobjects/ClassicalLocationTimePastAN>
     ClassicalLocationTimePastPerigee<stkobjects/ClassicalLocationTimePastPerigee>
     ClassicalLocationTrueAnomaly<stkobjects/ClassicalLocationTrueAnomaly>
     OrbitStateClassical<stkobjects/OrbitStateClassical>
     GeodeticSizeAltitude<stkobjects/GeodeticSizeAltitude>
     GeodeticSizeRadius<stkobjects/GeodeticSizeRadius>
     OrbitStateGeodetic<stkobjects/OrbitStateGeodetic>
     DelaunayL<stkobjects/DelaunayL>
     DelaunayLOverSQRTmu<stkobjects/DelaunayLOverSQRTmu>
     DelaunayH<stkobjects/DelaunayH>
     DelaunayHOverSQRTmu<stkobjects/DelaunayHOverSQRTmu>
     DelaunayG<stkobjects/DelaunayG>
     DelaunayGOverSQRTmu<stkobjects/DelaunayGOverSQRTmu>
     OrbitStateDelaunay<stkobjects/OrbitStateDelaunay>
     EquinoctialSizeShapeMeanMotion<stkobjects/EquinoctialSizeShapeMeanMotion>
     EquinoctialSizeShapeSemimajorAxis<stkobjects/EquinoctialSizeShapeSemimajorAxis>
     OrbitStateEquinoctial<stkobjects/OrbitStateEquinoctial>
     MixedSphericalFlightPathAngleHorizontal<stkobjects/MixedSphericalFlightPathAngleHorizontal>
     MixedSphericalFlightPathAngleVertical<stkobjects/MixedSphericalFlightPathAngleVertical>
     OrbitStateMixedSpherical<stkobjects/OrbitStateMixedSpherical>
     SphericalFlightPathAngleHorizontal<stkobjects/SphericalFlightPathAngleHorizontal>
     SphericalFlightPathAngleVertical<stkobjects/SphericalFlightPathAngleVertical>
     OrbitStateSpherical<stkobjects/OrbitStateSpherical>
     VehicleGraphics2DTimeComponentsEventElement<stkobjects/VehicleGraphics2DTimeComponentsEventElement>
     VehicleGraphics2DTimeComponentsEventCollectionElement<stkobjects/VehicleGraphics2DTimeComponentsEventCollectionElement>
     VehicleGraphics2DTimeComponentsCollection<stkobjects/VehicleGraphics2DTimeComponentsCollection>
     VehicleGraphics2DAttributesTimeComponents<stkobjects/VehicleGraphics2DAttributesTimeComponents>
     StkPreferences<stkobjects/StkPreferences>
     StkPreferencesVDF<stkobjects/StkPreferencesVDF>
     VehicleAttitudeMaximumSlewRate<stkobjects/VehicleAttitudeMaximumSlewRate>
     VehicleAttitudeMaximumSlewAcceleration<stkobjects/VehicleAttitudeMaximumSlewAcceleration>
     VehicleAttitudeSlewConstrained<stkobjects/VehicleAttitudeSlewConstrained>
     VehicleAttitudeSlewFixedRate<stkobjects/VehicleAttitudeSlewFixedRate>
     VehicleAttitudeSlewFixedTime<stkobjects/VehicleAttitudeSlewFixedTime>
     VehicleAttitudeTargetSlew<stkobjects/VehicleAttitudeTargetSlew>
     MtoGraphics3DModelArtic<stkobjects/MtoGraphics3DModelArtic>
     VehiclePropagatorAviator<stkobjects/VehiclePropagatorAviator>
     VehicleEphemerisCCSDSv2ExportTool<stkobjects/VehicleEphemerisCCSDSv2ExportTool>
     StkPreferencesConnect<stkobjects/StkPreferencesConnect>
     Antenna<stkobjects/Antenna>
     AntennaModel<stkobjects/AntennaModel>
     AntennaModelOpticalSimple<stkobjects/AntennaModelOpticalSimple>
     AntennaModelOpticalGaussian<stkobjects/AntennaModelOpticalGaussian>
     AntennaModelGaussian<stkobjects/AntennaModelGaussian>
     AntennaModelParabolic<stkobjects/AntennaModelParabolic>
     AntennaModelSquareHorn<stkobjects/AntennaModelSquareHorn>
     AntennaModelScriptPlugin<stkobjects/AntennaModelScriptPlugin>
     AntennaModelExternal<stkobjects/AntennaModelExternal>
     AntennaModelGimroc<stkobjects/AntennaModelGimroc>
     AntennaModelRemcomUanFormat<stkobjects/AntennaModelRemcomUanFormat>
     AntennaModelANSYSffdFormat<stkobjects/AntennaModelANSYSffdFormat>
     AntennaModelTicraGRASPFormat<stkobjects/AntennaModelTicraGRASPFormat>
     AntennaModelElevationAzimuthCuts<stkobjects/AntennaModelElevationAzimuthCuts>
     AntennaModelIeee1979<stkobjects/AntennaModelIeee1979>
     AntennaModelDipole<stkobjects/AntennaModelDipole>
     AntennaModelHelix<stkobjects/AntennaModelHelix>
     AntennaModelCosecantSquared<stkobjects/AntennaModelCosecantSquared>
     AntennaModelHemispherical<stkobjects/AntennaModelHemispherical>
     AntennaModelPencilBeam<stkobjects/AntennaModelPencilBeam>
     AntennaModelPhasedArray<stkobjects/AntennaModelPhasedArray>
     AntennaModelHfssEepArray<stkobjects/AntennaModelHfssEepArray>
     AntennaModelIsotropic<stkobjects/AntennaModelIsotropic>
     AntennaModelIntelSat<stkobjects/AntennaModelIntelSat>
     AntennaModelGpsGlobal<stkobjects/AntennaModelGpsGlobal>
     AntennaModelGpsFrpa<stkobjects/AntennaModelGpsFrpa>
     AntennaModelItuBO1213CoPolar<stkobjects/AntennaModelItuBO1213CoPolar>
     AntennaModelItuBO1213CrossPolar<stkobjects/AntennaModelItuBO1213CrossPolar>
     AntennaModelItuF1245<stkobjects/AntennaModelItuF1245>
     AntennaModelItuS580<stkobjects/AntennaModelItuS580>
     AntennaModelItuS465<stkobjects/AntennaModelItuS465>
     AntennaModelItuS731<stkobjects/AntennaModelItuS731>
     AntennaModelItuS1528R12Circular<stkobjects/AntennaModelItuS1528R12Circular>
     AntennaModelItuS1528R13<stkobjects/AntennaModelItuS1528R13>
     AntennaModelItuS672Circular<stkobjects/AntennaModelItuS672Circular>
     AntennaModelItuS1528R12Rectangular<stkobjects/AntennaModelItuS1528R12Rectangular>
     AntennaModelItuS672Rectangular<stkobjects/AntennaModelItuS672Rectangular>
     AntennaModelApertureCircularCosine<stkobjects/AntennaModelApertureCircularCosine>
     AntennaModelApertureCircularUniform<stkobjects/AntennaModelApertureCircularUniform>
     AntennaModelApertureCircularCosineSquared<stkobjects/AntennaModelApertureCircularCosineSquared>
     AntennaModelApertureCircularBessel<stkobjects/AntennaModelApertureCircularBessel>
     AntennaModelApertureCircularBesselEnvelope<stkobjects/AntennaModelApertureCircularBesselEnvelope>
     AntennaModelApertureCircularCosinePedestal<stkobjects/AntennaModelApertureCircularCosinePedestal>
     AntennaModelApertureCircularCosineSquaredPedestal<stkobjects/AntennaModelApertureCircularCosineSquaredPedestal>
     AntennaModelApertureCircularSincIntPower<stkobjects/AntennaModelApertureCircularSincIntPower>
     AntennaModelApertureCircularSincRealPower<stkobjects/AntennaModelApertureCircularSincRealPower>
     AntennaModelApertureRectangularCosine<stkobjects/AntennaModelApertureRectangularCosine>
     AntennaModelApertureRectangularCosinePedestal<stkobjects/AntennaModelApertureRectangularCosinePedestal>
     AntennaModelApertureRectangularCosineSquaredPedestal<stkobjects/AntennaModelApertureRectangularCosineSquaredPedestal>
     AntennaModelApertureRectangularSincIntPower<stkobjects/AntennaModelApertureRectangularSincIntPower>
     AntennaModelApertureRectangularSincRealPower<stkobjects/AntennaModelApertureRectangularSincRealPower>
     AntennaModelApertureRectangularCosineSquared<stkobjects/AntennaModelApertureRectangularCosineSquared>
     AntennaModelApertureRectangularUniform<stkobjects/AntennaModelApertureRectangularUniform>
     AntennaModelRectangularPattern<stkobjects/AntennaModelRectangularPattern>
     AntennaControl<stkobjects/AntennaControl>
     AntennaGraphics3D<stkobjects/AntennaGraphics3D>
     RadarCrossSectionVolumeGraphics<stkobjects/RadarCrossSectionVolumeGraphics>
     RadarCrossSectionGraphics3D<stkobjects/RadarCrossSectionGraphics3D>
     RadarCrossSectionGraphics<stkobjects/RadarCrossSectionGraphics>
     AntennaVolumeGraphics<stkobjects/AntennaVolumeGraphics>
     AntennaContourGraphics<stkobjects/AntennaContourGraphics>
     AntennaGraphics<stkobjects/AntennaGraphics>
     RadarCrossSectionContourLevelCollection<stkobjects/RadarCrossSectionContourLevelCollection>
     RadarCrossSectionContourLevel<stkobjects/RadarCrossSectionContourLevel>
     RadarCrossSectionVolumeLevelCollection<stkobjects/RadarCrossSectionVolumeLevelCollection>
     RadarCrossSectionVolumeLevel<stkobjects/RadarCrossSectionVolumeLevel>
     AntennaVolumeLevelCollection<stkobjects/AntennaVolumeLevelCollection>
     AntennaVolumeLevel<stkobjects/AntennaVolumeLevel>
     AntennaContourLevelCollection<stkobjects/AntennaContourLevelCollection>
     AntennaContourLevel<stkobjects/AntennaContourLevel>
     AntennaContourGain<stkobjects/AntennaContourGain>
     AntennaContourEirp<stkobjects/AntennaContourEirp>
     AntennaContourRip<stkobjects/AntennaContourRip>
     AntennaContourFluxDensity<stkobjects/AntennaContourFluxDensity>
     AntennaContourSpectralFluxDensity<stkobjects/AntennaContourSpectralFluxDensity>
     Transmitter<stkobjects/Transmitter>
     TransmitterModel<stkobjects/TransmitterModel>
     TransmitterModelScriptPluginRF<stkobjects/TransmitterModelScriptPluginRF>
     TransmitterModelScriptPluginLaser<stkobjects/TransmitterModelScriptPluginLaser>
     TransmitterModelCable<stkobjects/TransmitterModelCable>
     TransmitterModelSimple<stkobjects/TransmitterModelSimple>
     TransmitterModelMedium<stkobjects/TransmitterModelMedium>
     TransmitterModelComplex<stkobjects/TransmitterModelComplex>
     TransmitterModelMultibeam<stkobjects/TransmitterModelMultibeam>
     TransmitterModelLaser<stkobjects/TransmitterModelLaser>
     ReTransmitterModelSimple<stkobjects/ReTransmitterModelSimple>
     ReTransmitterModelMedium<stkobjects/ReTransmitterModelMedium>
     ReTransmitterModelComplex<stkobjects/ReTransmitterModelComplex>
     TransmitterGraphics3D<stkobjects/TransmitterGraphics3D>
     TransmitterGraphics<stkobjects/TransmitterGraphics>
     Receiver<stkobjects/Receiver>
     ReceiverModel<stkobjects/ReceiverModel>
     ReceiverModelCable<stkobjects/ReceiverModelCable>
     ReceiverModelSimple<stkobjects/ReceiverModelSimple>
     ReceiverModelMedium<stkobjects/ReceiverModelMedium>
     ReceiverModelComplex<stkobjects/ReceiverModelComplex>
     ReceiverModelMultibeam<stkobjects/ReceiverModelMultibeam>
     ReceiverModelLaser<stkobjects/ReceiverModelLaser>
     ReceiverModelScriptPluginRF<stkobjects/ReceiverModelScriptPluginRF>
     ReceiverModelScriptPluginLaser<stkobjects/ReceiverModelScriptPluginLaser>
     ReceiverGraphics3D<stkobjects/ReceiverGraphics3D>
     ReceiverGraphics<stkobjects/ReceiverGraphics>
     RadarDopplerClutterFilters<stkobjects/RadarDopplerClutterFilters>
     Waveform<stkobjects/Waveform>
     WaveformRectangular<stkobjects/WaveformRectangular>
     WaveformPulseDefinition<stkobjects/WaveformPulseDefinition>
     RadarMultifunctionWaveformStrategySettings<stkobjects/RadarMultifunctionWaveformStrategySettings>
     WaveformSelectionStrategy<stkobjects/WaveformSelectionStrategy>
     WaveformSelectionStrategyFixed<stkobjects/WaveformSelectionStrategyFixed>
     WaveformSelectionStrategyRangeLimits<stkobjects/WaveformSelectionStrategyRangeLimits>
     Radar<stkobjects/Radar>
     RadarModel<stkobjects/RadarModel>
     RadarModelMonostatic<stkobjects/RadarModelMonostatic>
     RadarModelMultifunction<stkobjects/RadarModelMultifunction>
     RadarModelBistaticTransmitter<stkobjects/RadarModelBistaticTransmitter>
     RadarModelBistaticReceiver<stkobjects/RadarModelBistaticReceiver>
     RadarGraphics3D<stkobjects/RadarGraphics3D>
     RadarGraphics<stkobjects/RadarGraphics>
     RadarAccessGraphics<stkobjects/RadarAccessGraphics>
     RadarMultipathGraphics<stkobjects/RadarMultipathGraphics>
     RadarModeMonostatic<stkobjects/RadarModeMonostatic>
     RadarModeMonostaticSearchTrack<stkobjects/RadarModeMonostaticSearchTrack>
     RadarModeMonostaticSar<stkobjects/RadarModeMonostaticSar>
     RadarModeBistaticTransmitter<stkobjects/RadarModeBistaticTransmitter>
     RadarModeBistaticTransmitterSearchTrack<stkobjects/RadarModeBistaticTransmitterSearchTrack>
     RadarModeBistaticTransmitterSar<stkobjects/RadarModeBistaticTransmitterSar>
     RadarModeBistaticReceiver<stkobjects/RadarModeBistaticReceiver>
     RadarModeBistaticReceiverSearchTrack<stkobjects/RadarModeBistaticReceiverSearchTrack>
     RadarModeBistaticReceiverSar<stkobjects/RadarModeBistaticReceiverSar>
     RadarWaveformMonostaticSearchTrackContinuous<stkobjects/RadarWaveformMonostaticSearchTrackContinuous>
     RadarWaveformMonostaticSearchTrackFixedPRF<stkobjects/RadarWaveformMonostaticSearchTrackFixedPRF>
     RadarMultifunctionDetectionProcessing<stkobjects/RadarMultifunctionDetectionProcessing>
     RadarWaveformBistaticTransmitterSearchTrackContinuous<stkobjects/RadarWaveformBistaticTransmitterSearchTrackContinuous>
     RadarWaveformBistaticTransmitterSearchTrackFixedPRF<stkobjects/RadarWaveformBistaticTransmitterSearchTrackFixedPRF>
     RadarWaveformBistaticReceiverSearchTrackContinuous<stkobjects/RadarWaveformBistaticReceiverSearchTrackContinuous>
     RadarWaveformBistaticReceiverSearchTrackFixedPRF<stkobjects/RadarWaveformBistaticReceiverSearchTrackFixedPRF>
     RadarWaveformSearchTrackPulseDefinition<stkobjects/RadarWaveformSearchTrackPulseDefinition>
     RadarModulator<stkobjects/RadarModulator>
     RadarProbabilityOfDetection<stkobjects/RadarProbabilityOfDetection>
     RadarProbabilityOfDetectionCFAR<stkobjects/RadarProbabilityOfDetectionCFAR>
     RadarProbabilityOfDetectionNonCFAR<stkobjects/RadarProbabilityOfDetectionNonCFAR>
     RadarProbabilityOfDetectionPlugin<stkobjects/RadarProbabilityOfDetectionPlugin>
     RadarProbabilityOfDetectionCFARCellAveraging<stkobjects/RadarProbabilityOfDetectionCFARCellAveraging>
     RadarProbabilityOfDetectionCFAROrderedStatistics<stkobjects/RadarProbabilityOfDetectionCFAROrderedStatistics>
     RadarPulseIntegrationGoalSNR<stkobjects/RadarPulseIntegrationGoalSNR>
     RadarPulseIntegrationFixedNumberOfPulses<stkobjects/RadarPulseIntegrationFixedNumberOfPulses>
     RadarContinuousWaveAnalysisModeGoalSNR<stkobjects/RadarContinuousWaveAnalysisModeGoalSNR>
     RadarContinuousWaveAnalysisModeFixedTime<stkobjects/RadarContinuousWaveAnalysisModeFixedTime>
     RadarWaveformSarPulseDefinition<stkobjects/RadarWaveformSarPulseDefinition>
     RadarWaveformSarPulseIntegration<stkobjects/RadarWaveformSarPulseIntegration>
     RadarTransmitter<stkobjects/RadarTransmitter>
     RadarTransmitterMultifunction<stkobjects/RadarTransmitterMultifunction>
     RadarReceiver<stkobjects/RadarReceiver>
     AdditionalGainLoss<stkobjects/AdditionalGainLoss>
     AdditionalGainLossCollection<stkobjects/AdditionalGainLossCollection>
     Polarization<stkobjects/Polarization>
     PolarizationElliptical<stkobjects/PolarizationElliptical>
     ReceivePolarizationElliptical<stkobjects/ReceivePolarizationElliptical>
     PolarizationLHC<stkobjects/PolarizationLHC>
     PolarizationRHC<stkobjects/PolarizationRHC>
     ReceivePolarizationLHC<stkobjects/ReceivePolarizationLHC>
     ReceivePolarizationRHC<stkobjects/ReceivePolarizationRHC>
     PolarizationLinear<stkobjects/PolarizationLinear>
     ReceivePolarizationLinear<stkobjects/ReceivePolarizationLinear>
     PolarizationHorizontal<stkobjects/PolarizationHorizontal>
     ReceivePolarizationHorizontal<stkobjects/ReceivePolarizationHorizontal>
     PolarizationVertical<stkobjects/PolarizationVertical>
     ReceivePolarizationVertical<stkobjects/ReceivePolarizationVertical>
     RadarClutter<stkobjects/RadarClutter>
     RadarClutterGeometry<stkobjects/RadarClutterGeometry>
     ScatteringPointProviderCollectionElement<stkobjects/ScatteringPointProviderCollectionElement>
     ScatteringPointProviderCollection<stkobjects/ScatteringPointProviderCollection>
     ScatteringPointProviderList<stkobjects/ScatteringPointProviderList>
     ScatteringPointProvider<stkobjects/ScatteringPointProvider>
     ScatteringPointProviderSinglePoint<stkobjects/ScatteringPointProviderSinglePoint>
     ScatteringPointCollectionElement<stkobjects/ScatteringPointCollectionElement>
     ScatteringPointCollection<stkobjects/ScatteringPointCollection>
     ScatteringPointProviderPointsFile<stkobjects/ScatteringPointProviderPointsFile>
     ScatteringPointProviderRangeOverCFARCells<stkobjects/ScatteringPointProviderRangeOverCFARCells>
     ScatteringPointProviderSmoothOblateEarth<stkobjects/ScatteringPointProviderSmoothOblateEarth>
     ScatteringPointProviderPlugin<stkobjects/ScatteringPointProviderPlugin>
     CRPluginConfiguration<stkobjects/CRPluginConfiguration>
     RadarJamming<stkobjects/RadarJamming>
     RFInterference<stkobjects/RFInterference>
     RFFilterModel<stkobjects/RFFilterModel>
     RFFilterModelBessel<stkobjects/RFFilterModelBessel>
     RFFilterModelSincEnvSinc<stkobjects/RFFilterModelSincEnvSinc>
     RFFilterModelElliptic<stkobjects/RFFilterModelElliptic>
     RFFilterModelChebyshev<stkobjects/RFFilterModelChebyshev>
     RFFilterModelCosineWindow<stkobjects/RFFilterModelCosineWindow>
     RFFilterModelGaussianWindow<stkobjects/RFFilterModelGaussianWindow>
     RFFilterModelHammingWindow<stkobjects/RFFilterModelHammingWindow>
     RFFilterModelButterworth<stkobjects/RFFilterModelButterworth>
     RFFilterModelExternal<stkobjects/RFFilterModelExternal>
     RFFilterModelScriptPlugin<stkobjects/RFFilterModelScriptPlugin>
     RFFilterModelSinc<stkobjects/RFFilterModelSinc>
     RFFilterModelRaisedCosine<stkobjects/RFFilterModelRaisedCosine>
     RFFilterModelRootRaisedCosine<stkobjects/RFFilterModelRootRaisedCosine>
     RFFilterModelRcLowPass<stkobjects/RFFilterModelRcLowPass>
     RFFilterModelRectangular<stkobjects/RFFilterModelRectangular>
     RFFilterModelFirBoxCar<stkobjects/RFFilterModelFirBoxCar>
     RFFilterModelIir<stkobjects/RFFilterModelIir>
     RFFilterModelFir<stkobjects/RFFilterModelFir>
     SystemNoiseTemperature<stkobjects/SystemNoiseTemperature>
     AntennaNoiseTemperature<stkobjects/AntennaNoiseTemperature>
     Atmosphere<stkobjects/Atmosphere>
     LaserPropagationLossModels<stkobjects/LaserPropagationLossModels>
     LaserAtmosphericLossModel<stkobjects/LaserAtmosphericLossModel>
     LaserAtmosphericLossModelBeerBouguerLambertLaw<stkobjects/LaserAtmosphericLossModelBeerBouguerLambertLaw>
     ModtranLookupTablePropagationModel<stkobjects/ModtranLookupTablePropagationModel>
     ModtranPropagationModel<stkobjects/ModtranPropagationModel>
     LaserTroposphericScintillationLossModel<stkobjects/LaserTroposphericScintillationLossModel>
     AtmosphericTurbulenceModel<stkobjects/AtmosphericTurbulenceModel>
     AtmosphericTurbulenceModelConstant<stkobjects/AtmosphericTurbulenceModelConstant>
     AtmosphericTurbulenceModelHufnagelValley<stkobjects/AtmosphericTurbulenceModelHufnagelValley>
     LaserTroposphericScintillationLossModelITURP1814<stkobjects/LaserTroposphericScintillationLossModelITURP1814>
     AtmosphericAbsorptionModel<stkobjects/AtmosphericAbsorptionModel>
     AtmosphericAbsorptionModelITURP676_9<stkobjects/AtmosphericAbsorptionModelITURP676_9>
     AtmosphericAbsorptionModelVoacap<stkobjects/AtmosphericAbsorptionModelVoacap>
     AtmosphericAbsorptionModelTirem320<stkobjects/AtmosphericAbsorptionModelTirem320>
     AtmosphericAbsorptionModelTirem331<stkobjects/AtmosphericAbsorptionModelTirem331>
     AtmosphericAbsorptionModelTirem550<stkobjects/AtmosphericAbsorptionModelTirem550>
     AtmosphericAbsorptionModelSimpleSatcom<stkobjects/AtmosphericAbsorptionModelSimpleSatcom>
     AtmosphericAbsorptionModelScriptPlugin<stkobjects/AtmosphericAbsorptionModelScriptPlugin>
     AtmosphericAbsorptionModelCOMPlugin<stkobjects/AtmosphericAbsorptionModelCOMPlugin>
     ScatteringPointModel<stkobjects/ScatteringPointModel>
     ScatteringPointModelPlugin<stkobjects/ScatteringPointModelPlugin>
     ScatteringPointModelConstantCoefficient<stkobjects/ScatteringPointModelConstantCoefficient>
     ScatteringPointModelWindTurbine<stkobjects/ScatteringPointModelWindTurbine>
     RadarCrossSection<stkobjects/RadarCrossSection>
     RadarCrossSectionModel<stkobjects/RadarCrossSectionModel>
     RadarCrossSectionInheritable<stkobjects/RadarCrossSectionInheritable>
     RadarCrossSectionFrequencyBand<stkobjects/RadarCrossSectionFrequencyBand>
     RadarCrossSectionFrequencyBandCollection<stkobjects/RadarCrossSectionFrequencyBandCollection>
     RadarCrossSectionComputeStrategy<stkobjects/RadarCrossSectionComputeStrategy>
     RadarCrossSectionComputeStrategyConstantValue<stkobjects/RadarCrossSectionComputeStrategyConstantValue>
     RadarCrossSectionComputeStrategyScriptPlugin<stkobjects/RadarCrossSectionComputeStrategyScriptPlugin>
     RadarCrossSectionComputeStrategyExternalFile<stkobjects/RadarCrossSectionComputeStrategyExternalFile>
     RadarCrossSectionComputeStrategyAnsysCsvFile<stkobjects/RadarCrossSectionComputeStrategyAnsysCsvFile>
     RadarCrossSectionComputeStrategyPlugin<stkobjects/RadarCrossSectionComputeStrategyPlugin>
     CustomPropagationModel<stkobjects/CustomPropagationModel>
     PropagationChannel<stkobjects/PropagationChannel>
     RFEnvironment<stkobjects/RFEnvironment>
     LaserEnvironment<stkobjects/LaserEnvironment>
     ObjectRFEnvironment<stkobjects/ObjectRFEnvironment>
     ObjectLaserEnvironment<stkobjects/ObjectLaserEnvironment>
     PlatformLaserEnvironment<stkobjects/PlatformLaserEnvironment>
     RainLossModel<stkobjects/RainLossModel>
     RainLossModelITURP618_12<stkobjects/RainLossModelITURP618_12>
     RainLossModelITURP618_13<stkobjects/RainLossModelITURP618_13>
     RainLossModelITURP618_10<stkobjects/RainLossModelITURP618_10>
     RainLossModelCrane1985<stkobjects/RainLossModelCrane1985>
     RainLossModelCrane1982<stkobjects/RainLossModelCrane1982>
     RainLossModelCCIR1983<stkobjects/RainLossModelCCIR1983>
     RainLossModelScriptPlugin<stkobjects/RainLossModelScriptPlugin>
     CloudsAndFogFadingLossModel<stkobjects/CloudsAndFogFadingLossModel>
     CloudsAndFogFadingLossModelP840_6<stkobjects/CloudsAndFogFadingLossModelP840_6>
     CloudsAndFogFadingLossModelP840_7<stkobjects/CloudsAndFogFadingLossModelP840_7>
     TroposphericScintillationFadingLossModel<stkobjects/TroposphericScintillationFadingLossModel>
     TroposphericScintillationFadingLossModelP618_8<stkobjects/TroposphericScintillationFadingLossModelP618_8>
     TroposphericScintillationFadingLossModelP618_12<stkobjects/TroposphericScintillationFadingLossModelP618_12>
     IonosphericFadingLossModel<stkobjects/IonosphericFadingLossModel>
     IonosphericFadingLossModelP531_13<stkobjects/IonosphericFadingLossModelP531_13>
     UrbanTerrestrialLossModel<stkobjects/UrbanTerrestrialLossModel>
     UrbanTerrestrialLossModelTwoRay<stkobjects/UrbanTerrestrialLossModelTwoRay>
     UrbanTerrestrialLossModelWirelessInSite64<stkobjects/UrbanTerrestrialLossModelWirelessInSite64>
     WirelessInSite64GeometryData<stkobjects/WirelessInSite64GeometryData>
     PointingStrategy<stkobjects/PointingStrategy>
     PointingStrategyFixed<stkobjects/PointingStrategyFixed>
     PointingStrategySpinning<stkobjects/PointingStrategySpinning>
     PointingStrategyTargeted<stkobjects/PointingStrategyTargeted>
     CRLocation<stkobjects/CRLocation>
     CRComplex<stkobjects/CRComplex>
     CRComplexCollection<stkobjects/CRComplexCollection>
     ModulatorModel<stkobjects/ModulatorModel>
     ModulatorModelBpsk<stkobjects/ModulatorModelBpsk>
     ModulatorModelQpsk<stkobjects/ModulatorModelQpsk>
     ModulatorModelExternalSource<stkobjects/ModulatorModelExternalSource>
     ModulatorModelExternal<stkobjects/ModulatorModelExternal>
     ModulatorModelQam16<stkobjects/ModulatorModelQam16>
     ModulatorModelQam32<stkobjects/ModulatorModelQam32>
     ModulatorModelQam64<stkobjects/ModulatorModelQam64>
     ModulatorModelQam128<stkobjects/ModulatorModelQam128>
     ModulatorModelQam256<stkobjects/ModulatorModelQam256>
     ModulatorModelQam1024<stkobjects/ModulatorModelQam1024>
     ModulatorModel8psk<stkobjects/ModulatorModel8psk>
     ModulatorModel16psk<stkobjects/ModulatorModel16psk>
     ModulatorModelMsk<stkobjects/ModulatorModelMsk>
     ModulatorModelBoc<stkobjects/ModulatorModelBoc>
     ModulatorModelDpsk<stkobjects/ModulatorModelDpsk>
     ModulatorModelFsk<stkobjects/ModulatorModelFsk>
     ModulatorModelNfsk<stkobjects/ModulatorModelNfsk>
     ModulatorModelOqpsk<stkobjects/ModulatorModelOqpsk>
     ModulatorModelNarrowbandUniform<stkobjects/ModulatorModelNarrowbandUniform>
     ModulatorModelWidebandUniform<stkobjects/ModulatorModelWidebandUniform>
     ModulatorModelWidebandGaussian<stkobjects/ModulatorModelWidebandGaussian>
     ModulatorModelPulsedSignal<stkobjects/ModulatorModelPulsedSignal>
     ModulatorModelScriptPluginCustomPsd<stkobjects/ModulatorModelScriptPluginCustomPsd>
     ModulatorModelScriptPluginIdealPsd<stkobjects/ModulatorModelScriptPluginIdealPsd>
     LinkMargin<stkobjects/LinkMargin>
     DemodulatorModel<stkobjects/DemodulatorModel>
     DemodulatorModelBpsk<stkobjects/DemodulatorModelBpsk>
     DemodulatorModelQpsk<stkobjects/DemodulatorModelQpsk>
     DemodulatorModelExternalSource<stkobjects/DemodulatorModelExternalSource>
     DemodulatorModelExternal<stkobjects/DemodulatorModelExternal>
     DemodulatorModelQam16<stkobjects/DemodulatorModelQam16>
     DemodulatorModelQam32<stkobjects/DemodulatorModelQam32>
     DemodulatorModelQam64<stkobjects/DemodulatorModelQam64>
     DemodulatorModelQam128<stkobjects/DemodulatorModelQam128>
     DemodulatorModelQam256<stkobjects/DemodulatorModelQam256>
     DemodulatorModelQam1024<stkobjects/DemodulatorModelQam1024>
     DemodulatorModel8psk<stkobjects/DemodulatorModel8psk>
     DemodulatorModel16psk<stkobjects/DemodulatorModel16psk>
     DemodulatorModelMsk<stkobjects/DemodulatorModelMsk>
     DemodulatorModelBoc<stkobjects/DemodulatorModelBoc>
     DemodulatorModelDpsk<stkobjects/DemodulatorModelDpsk>
     DemodulatorModelFsk<stkobjects/DemodulatorModelFsk>
     DemodulatorModelNfsk<stkobjects/DemodulatorModelNfsk>
     DemodulatorModelOqpsk<stkobjects/DemodulatorModelOqpsk>
     DemodulatorModelNarrowbandUniform<stkobjects/DemodulatorModelNarrowbandUniform>
     DemodulatorModelWidebandUniform<stkobjects/DemodulatorModelWidebandUniform>
     DemodulatorModelWidebandGaussian<stkobjects/DemodulatorModelWidebandGaussian>
     DemodulatorModelPulsedSignal<stkobjects/DemodulatorModelPulsedSignal>
     DemodulatorModelScriptPlugin<stkobjects/DemodulatorModelScriptPlugin>
     TransferFunctionPolynomialCollection<stkobjects/TransferFunctionPolynomialCollection>
     TransferFunctionInputBackOffCOverImTableRow<stkobjects/TransferFunctionInputBackOffCOverImTableRow>
     TransferFunctionInputBackOffCOverImTable<stkobjects/TransferFunctionInputBackOffCOverImTable>
     TransferFunctionInputBackOffOutputBackOffTableRow<stkobjects/TransferFunctionInputBackOffOutputBackOffTableRow>
     TransferFunctionInputBackOffOutputBackOffTable<stkobjects/TransferFunctionInputBackOffOutputBackOffTable>
     BeerBouguerLambertLawLayer<stkobjects/BeerBouguerLambertLawLayer>
     BeerBouguerLambertLawLayerCollection<stkobjects/BeerBouguerLambertLawLayerCollection>
     RadarActivity<stkobjects/RadarActivity>
     RadarActivityAlwaysActive<stkobjects/RadarActivityAlwaysActive>
     RadarActivityAlwaysInactive<stkobjects/RadarActivityAlwaysInactive>
     RadarActivityTimeComponentListElement<stkobjects/RadarActivityTimeComponentListElement>
     RadarActivityTimeComponentListCollection<stkobjects/RadarActivityTimeComponentListCollection>
     RadarActivityTimeComponentList<stkobjects/RadarActivityTimeComponentList>
     RadarActivityTimeIntervalListElement<stkobjects/RadarActivityTimeIntervalListElement>
     RadarActivityTimeIntervalListCollection<stkobjects/RadarActivityTimeIntervalListCollection>
     RadarActivityTimeIntervalList<stkobjects/RadarActivityTimeIntervalList>
     RadarAntennaBeam<stkobjects/RadarAntennaBeam>
     RadarAntennaBeamCollection<stkobjects/RadarAntennaBeamCollection>
     AntennaSystem<stkobjects/AntennaSystem>
     AntennaBeam<stkobjects/AntennaBeam>
     AntennaBeamTransmit<stkobjects/AntennaBeamTransmit>
     AntennaBeamCollection<stkobjects/AntennaBeamCollection>
     AntennaBeamSelectionStrategy<stkobjects/AntennaBeamSelectionStrategy>
     AntennaBeamSelectionStrategyAggregate<stkobjects/AntennaBeamSelectionStrategyAggregate>
     AntennaBeamSelectionStrategyMaxGain<stkobjects/AntennaBeamSelectionStrategyMaxGain>
     AntennaBeamSelectionStrategyMinBoresightAngle<stkobjects/AntennaBeamSelectionStrategyMinBoresightAngle>
     AntennaBeamSelectionStrategyScriptPlugin<stkobjects/AntennaBeamSelectionStrategyScriptPlugin>
     CommSystem<stkobjects/CommSystem>
     CommSystemGraphics<stkobjects/CommSystemGraphics>
     CommSystemGraphics3D<stkobjects/CommSystemGraphics3D>
     CommSystemAccessOptions<stkobjects/CommSystemAccessOptions>
     CommSystemAccessEventDetection<stkobjects/CommSystemAccessEventDetection>
     CommSystemAccessEventDetectionSubsample<stkobjects/CommSystemAccessEventDetectionSubsample>
     CommSystemAccessEventDetectionSamplesOnly<stkobjects/CommSystemAccessEventDetectionSamplesOnly>
     CommSystemAccessSamplingMethod<stkobjects/CommSystemAccessSamplingMethod>
     CommSystemAccessSamplingMethodFixed<stkobjects/CommSystemAccessSamplingMethodFixed>
     CommSystemAccessSamplingMethodAdaptive<stkobjects/CommSystemAccessSamplingMethodAdaptive>
     CommSystemLinkSelectionCriteria<stkobjects/CommSystemLinkSelectionCriteria>
     CommSystemLinkSelectionCriteriaMinimumRange<stkobjects/CommSystemLinkSelectionCriteriaMinimumRange>
     CommSystemLinkSelectionCriteriaMaximumElevation<stkobjects/CommSystemLinkSelectionCriteriaMaximumElevation>
     CommSystemLinkSelectionCriteriaScriptPlugin<stkobjects/CommSystemLinkSelectionCriteriaScriptPlugin>
     ComponentDirectory<stkobjects/ComponentDirectory>
     ComponentInfo<stkobjects/ComponentInfo>
     ComponentInfoCollection<stkobjects/ComponentInfoCollection>
     ComponentAttrLinkEmbedControl<stkobjects/ComponentAttrLinkEmbedControl>
     Volumetric<stkobjects/Volumetric>
     VolumetricGridSpatialCalculation<stkobjects/VolumetricGridSpatialCalculation>
     VolumetricExternalFile<stkobjects/VolumetricExternalFile>
     VolumetricAnalysisInterval<stkobjects/VolumetricAnalysisInterval>
     VolumetricAdvanced<stkobjects/VolumetricAdvanced>
     VolumetricGraphics3D<stkobjects/VolumetricGraphics3D>
     VolumetricGraphics3DGrid<stkobjects/VolumetricGraphics3DGrid>
     VolumetricGraphics3DCrossSection<stkobjects/VolumetricGraphics3DCrossSection>
     VolumetricGraphics3DCrossSectionPlane<stkobjects/VolumetricGraphics3DCrossSectionPlane>
     VolumetricGraphics3DCrossSectionPlaneCollection<stkobjects/VolumetricGraphics3DCrossSectionPlaneCollection>
     VolumetricGraphics3DVolume<stkobjects/VolumetricGraphics3DVolume>
     VolumetricGraphics3DActiveGridPoints<stkobjects/VolumetricGraphics3DActiveGridPoints>
     VolumetricGraphics3DSpatialCalculationLevels<stkobjects/VolumetricGraphics3DSpatialCalculationLevels>
     VolumetricGraphics3DSpatialCalculationLevel<stkobjects/VolumetricGraphics3DSpatialCalculationLevel>
     VolumetricGraphics3DSpatialCalculationLevelCollection<stkobjects/VolumetricGraphics3DSpatialCalculationLevelCollection>
     VolumetricGraphics3DLegend<stkobjects/VolumetricGraphics3DLegend>
     VolumetricExportTool<stkobjects/VolumetricExportTool>
     SatelliteCollection<stkobjects/SatelliteCollection>
     Subset<stkobjects/Subset>
     ElementConfiguration<stkobjects/ElementConfiguration>
     ElementConfigurationCircular<stkobjects/ElementConfigurationCircular>
     ElementConfigurationLinear<stkobjects/ElementConfigurationLinear>
     ElementConfigurationAsciiFile<stkobjects/ElementConfigurationAsciiFile>
     ElementConfigurationHfssEepFile<stkobjects/ElementConfigurationHfssEepFile>
     ElementConfigurationPolygon<stkobjects/ElementConfigurationPolygon>
     ElementConfigurationHexagon<stkobjects/ElementConfigurationHexagon>
     SolarActivityConfiguration<stkobjects/SolarActivityConfiguration>
     SolarActivityConfigurationSunspotNumber<stkobjects/SolarActivityConfigurationSunspotNumber>
     SolarActivityConfigurationSolarFlux<stkobjects/SolarActivityConfigurationSolarFlux>
     Beamformer<stkobjects/Beamformer>
     BeamformerAsciiFile<stkobjects/BeamformerAsciiFile>
     BeamformerMvdr<stkobjects/BeamformerMvdr>
     BeamformerUniform<stkobjects/BeamformerUniform>
     BeamformerBlackmanHarris<stkobjects/BeamformerBlackmanHarris>
     BeamformerCosine<stkobjects/BeamformerCosine>
     BeamformerCosineX<stkobjects/BeamformerCosineX>
     BeamformerCustomTaperFile<stkobjects/BeamformerCustomTaperFile>
     BeamformerDolphChebyshev<stkobjects/BeamformerDolphChebyshev>
     BeamformerHamming<stkobjects/BeamformerHamming>
     BeamformerHann<stkobjects/BeamformerHann>
     BeamformerRaisedCosine<stkobjects/BeamformerRaisedCosine>
     BeamformerRaisedCosineSquared<stkobjects/BeamformerRaisedCosineSquared>
     BeamformerScript<stkobjects/BeamformerScript>
     DirectionProvider<stkobjects/DirectionProvider>
     DirectionProviderAsciiFile<stkobjects/DirectionProviderAsciiFile>
     DirectionProviderObject<stkobjects/DirectionProviderObject>
     DirectionProviderLink<stkobjects/DirectionProviderLink>
     DirectionProviderScript<stkobjects/DirectionProviderScript>
     Element<stkobjects/Element>
     ElementCollection<stkobjects/ElementCollection>
     KeyValueCollection<stkobjects/KeyValueCollection>
     RadarStcAttenuation<stkobjects/RadarStcAttenuation>
     RadarStcAttenuationDecayFactor<stkobjects/RadarStcAttenuationDecayFactor>
     RadarStcAttenuationDecaySlope<stkobjects/RadarStcAttenuationDecaySlope>
     RadarStcAttenuationMapRange<stkobjects/RadarStcAttenuationMapRange>
     RadarStcAttenuationMapAzimuthRange<stkobjects/RadarStcAttenuationMapAzimuthRange>
     RadarStcAttenuationMapElevationRange<stkobjects/RadarStcAttenuationMapElevationRange>
     RadarStcAttenuationPlugin<stkobjects/RadarStcAttenuationPlugin>
     SensorPointingAlongVector<stkobjects/SensorPointingAlongVector>
     SensorPointingSchedule<stkobjects/SensorPointingSchedule>
     AccessConstraintAnalysisWorkbenchCollection<stkobjects/AccessConstraintAnalysisWorkbenchCollection>
     AccessConstraintAnalysisWorkbench<stkobjects/AccessConstraintAnalysisWorkbench>
     Graphics3DArticulationFile<stkobjects/Graphics3DArticulationFile>
     DataProviderResultStatisticResult<stkobjects/DataProviderResultStatisticResult>
     DataProviderResultTimeVaryingExtremumResult<stkobjects/DataProviderResultTimeVaryingExtremumResult>
     DataProviderResultStatistics<stkobjects/DataProviderResultStatistics>
     Graphics3DModelGltfImageBased<stkobjects/Graphics3DModelGltfImageBased>
     StkObjectCutCopyPasteEventArgs<stkobjects/StkObjectCutCopyPasteEventArgs>
     StkPreferencesPythonPlugins<stkobjects/StkPreferencesPythonPlugins>
     PathCollection<stkobjects/PathCollection>
     AdvCAT<stkobjects/AdvCAT>
     AdvCATAvailableObjectCollection<stkobjects/AdvCATAvailableObjectCollection>
     AdvCATChosenObject<stkobjects/AdvCATChosenObject>
     AdvCATChosenObjectCollection<stkobjects/AdvCATChosenObjectCollection>
     AdvCATPreFilters<stkobjects/AdvCATPreFilters>
     AdvCATAdvancedEllipsoid<stkobjects/AdvCATAdvancedEllipsoid>
     AdvCATAdvanced<stkobjects/AdvCATAdvanced>
     AdvCATGraphics3D<stkobjects/AdvCATGraphics3D>
     EOIRShapeObject<stkobjects/EOIRShapeObject>
     EOIRShapeBox<stkobjects/EOIRShapeBox>
     EOIRShapeCone<stkobjects/EOIRShapeCone>
     EOIRShapeCylinder<stkobjects/EOIRShapeCylinder>
     EOIRShapePlate<stkobjects/EOIRShapePlate>
     EOIRShapeSphere<stkobjects/EOIRShapeSphere>
     EOIRShapeCoupler<stkobjects/EOIRShapeCoupler>
     EOIRShapeNone<stkobjects/EOIRShapeNone>
     EOIRShapeGEOComm<stkobjects/EOIRShapeGEOComm>
     EOIRShapeLEOComm<stkobjects/EOIRShapeLEOComm>
     EOIRShapeLEOImaging<stkobjects/EOIRShapeLEOImaging>
     EOIRShapeCustomMesh<stkobjects/EOIRShapeCustomMesh>
     EOIRShapeTargetSignature<stkobjects/EOIRShapeTargetSignature>
     EOIRStagePlume<stkobjects/EOIRStagePlume>
     EOIRShape<stkobjects/EOIRShape>
     EOIRShapeCollection<stkobjects/EOIRShapeCollection>
     EOIRMaterialElement<stkobjects/EOIRMaterialElement>
     EOIRMaterialElementCollection<stkobjects/EOIRMaterialElementCollection>
     EOIRStage<stkobjects/EOIRStage>
     EOIR<stkobjects/EOIR>
     MissileEOIR<stkobjects/MissileEOIR>
     VehicleEOIR<stkobjects/VehicleEOIR>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CONSTANTS<stkobjects/CONSTANTS_enum>
    ≔ HELP_CONTEXT_IDS<stkobjects/HELP_CONTEXT_IDS_enum>
    ≔ ERROR_CODES<stkobjects/ERROR_CODES_enum>
    ≔ ABERRATION_TYPE<stkobjects/ABERRATION_TYPE_enum>
    ≔ ANIMATION_MODES<stkobjects/ANIMATION_MODES_enum>
    ≔ ANIMATION_OPTIONS<stkobjects/ANIMATION_OPTIONS_enum>
    ≔ ANIMATION_ACTIONS<stkobjects/ANIMATION_ACTIONS_enum>
    ≔ ANIMATION_DIRECTIONS<stkobjects/ANIMATION_DIRECTIONS_enum>
    ≔ AZ_EL_MASK_TYPE<stkobjects/AZ_EL_MASK_TYPE_enum>
    ≔ ACTION_TYPE<stkobjects/ACTION_TYPE_enum>
    ≔ AXIS_OFFSET<stkobjects/AXIS_OFFSET_enum>
    ≔ DATA_PROVIDER_RESULT_CATEGORIES<stkobjects/DATA_PROVIDER_RESULT_CATEGORIES_enum>
    ≔ DATA_PROVIDER_TYPE<stkobjects/DATA_PROVIDER_TYPE_enum>
    ≔ DATA_PROVIDER_ELEMENT_TYPE<stkobjects/DATA_PROVIDER_ELEMENT_TYPE_enum>
    ≔ ACCESS_TIME_TYPE<stkobjects/ACCESS_TIME_TYPE_enum>
    ≔ ALTITUDE_REFERENCE_TYPE<stkobjects/ALTITUDE_REFERENCE_TYPE_enum>
    ≔ TERRAIN_NORM_TYPE<stkobjects/TERRAIN_NORM_TYPE_enum>
    ≔ LIGHTING_OBSTRUCTION_MODEL_TYPE<stkobjects/LIGHTING_OBSTRUCTION_MODEL_TYPE_enum>
    ≔ DISPLAY_TIMES_TYPE<stkobjects/DISPLAY_TIMES_TYPE_enum>
    ≔ AREA_TYPE<stkobjects/AREA_TYPE_enum>
    ≔ TRAJECTORY_TYPE<stkobjects/TRAJECTORY_TYPE_enum>
    ≔ OFFSET_FRAME_TYPE<stkobjects/OFFSET_FRAME_TYPE_enum>
    ≔ SCENARIO_3D_POINT_SIZE<stkobjects/SCENARIO_3D_POINT_SIZE_enum>
    ≔ TERRAIN_FILE_TYPE<stkobjects/TERRAIN_FILE_TYPE_enum>
    ≔ TILESET_3D_SOURCE_TYPE<stkobjects/TILESET_3D_SOURCE_TYPE_enum>
    ≔ MARKER_TYPE<stkobjects/MARKER_TYPE_enum>
    ≔ VECTOR_AXES_CONNECT_TYPE<stkobjects/VECTOR_AXES_CONNECT_TYPE_enum>
    ≔ GRAPHICS_3D_MARKER_ORIGIN_TYPE<stkobjects/GRAPHICS_3D_MARKER_ORIGIN_TYPE_enum>
    ≔ GRAPHICS_3D_LABEL_SWAP_DISTANCE<stkobjects/GRAPHICS_3D_LABEL_SWAP_DISTANCE_enum>
    ≔ PLANET_POSITION_SOURCE_TYPE<stkobjects/PLANET_POSITION_SOURCE_TYPE_enum>
    ≔ EPHEM_SOURCE_TYPE<stkobjects/EPHEM_SOURCE_TYPE_enum>
    ≔ PLANET_ORBIT_DISPLAY_TYPE<stkobjects/PLANET_ORBIT_DISPLAY_TYPE_enum>
    ≔ SCENARIO_END_LOOP_TYPE<stkobjects/SCENARIO_END_LOOP_TYPE_enum>
    ≔ SCENARIO_REFRESH_DELTA_TYPE<stkobjects/SCENARIO_REFRESH_DELTA_TYPE_enum>
    ≔ SENSOR_PATTERN<stkobjects/SENSOR_PATTERN_enum>
    ≔ SENSOR_POINTING<stkobjects/SENSOR_POINTING_enum>
    ≔ SENSOR_POINTING_TARGETED_BORESIGHT_TYPE<stkobjects/SENSOR_POINTING_TARGETED_BORESIGHT_TYPE_enum>
    ≔ BORESIGHT_TYPE<stkobjects/BORESIGHT_TYPE_enum>
    ≔ TRACK_MODE_TYPE<stkobjects/TRACK_MODE_TYPE_enum>
    ≔ SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE<stkobjects/SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE_enum>
    ≔ SENSOR_REFRACTION_TYPE<stkobjects/SENSOR_REFRACTION_TYPE_enum>
    ≔ SENSOR_PROJECTION_DISTANCE_TYPE<stkobjects/SENSOR_PROJECTION_DISTANCE_TYPE_enum>
    ≔ SENSOR_LOCATION<stkobjects/SENSOR_LOCATION_enum>
    ≔ SCENARIO_TIME_STEP_TYPE<stkobjects/SCENARIO_TIME_STEP_TYPE_enum>
    ≔ NOTE_SHOW_TYPE<stkobjects/NOTE_SHOW_TYPE_enum>
    ≔ GEOMETRIC_ELEM_TYPE<stkobjects/GEOMETRIC_ELEM_TYPE_enum>
    ≔ SENSOR_SCAN_MODE<stkobjects/SENSOR_SCAN_MODE_enum>
    ≔ CONSTRAINT_BACKGROUND<stkobjects/CONSTRAINT_BACKGROUND_enum>
    ≔ CONSTRAINT_GROUND_TRACK<stkobjects/CONSTRAINT_GROUND_TRACK_enum>
    ≔ INTERSECTION_TYPE<stkobjects/INTERSECTION_TYPE_enum>
    ≔ CONSTRAINT_LIGHTING<stkobjects/CONSTRAINT_LIGHTING_enum>
    ≔ SENSOR_GRAPHICS_3D_PROJECTION_TYPE<stkobjects/SENSOR_GRAPHICS_3D_PROJECTION_TYPE_enum>
    ≔ SENSOR_GRAPHICS_3D_PULSE_STYLE<stkobjects/SENSOR_GRAPHICS_3D_PULSE_STYLE_enum>
    ≔ SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET<stkobjects/SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET_enum>
    ≔ LINE_WIDTH<stkobjects/LINE_WIDTH_enum>
    ≔ STK_OBJECT_TYPE<stkobjects/STK_OBJECT_TYPE_enum>
    ≔ ACCESS_CONSTRAINTS<stkobjects/ACCESS_CONSTRAINTS_enum>
    ≔ BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE<stkobjects/BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE_enum>
    ≔ SHADOW_MODEL<stkobjects/SHADOW_MODEL_enum>
    ≔ METHOD_TO_COMPUTE_SUN_POSITION<stkobjects/METHOD_TO_COMPUTE_SUN_POSITION_enum>
    ≔ ATMOSPHERIC_DENSITY_MODEL<stkobjects/ATMOSPHERIC_DENSITY_MODEL_enum>
    ≔ MARKER_SHAPE_3D<stkobjects/MARKER_SHAPE_3D_enum>
    ≔ LEAD_TRAIL_DATA<stkobjects/LEAD_TRAIL_DATA_enum>
    ≔ TICK_DATA<stkobjects/TICK_DATA_enum>
    ≔ LOAD_METHOD_TYPE<stkobjects/LOAD_METHOD_TYPE_enum>
    ≔ LLA_POSITION_TYPE<stkobjects/LLA_POSITION_TYPE_enum>
    ≔ VEHICLE_GRAPHICS_2D_PASS<stkobjects/VEHICLE_GRAPHICS_2D_PASS_enum>
    ≔ VEHICLE_GRAPHICS_2D_VISIBLE_SIDES<stkobjects/VEHICLE_GRAPHICS_2D_VISIBLE_SIDES_enum>
    ≔ VEHICLE_GRAPHICS_2D_OFFSET<stkobjects/VEHICLE_GRAPHICS_2D_OFFSET_enum>
    ≔ VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE<stkobjects/VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE_enum>
    ≔ VEHICLE_GRAPHICS_2D_ATTRIBUTES<stkobjects/VEHICLE_GRAPHICS_2D_ATTRIBUTES_enum>
    ≔ VEHICLE_GRAPHICS_2D_ELEVATION<stkobjects/VEHICLE_GRAPHICS_2D_ELEVATION_enum>
    ≔ VEHICLE_GRAPHICS_2D_OPTIONS<stkobjects/VEHICLE_GRAPHICS_2D_OPTIONS_enum>
    ≔ MODEL_TYPE<stkobjects/MODEL_TYPE_enum>
    ≔ VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE<stkobjects/VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE_enum>
    ≔ VEHICLE_GRAPHICS_3D_SIGMA_SCALE<stkobjects/VEHICLE_GRAPHICS_3D_SIGMA_SCALE_enum>
    ≔ VEHICLE_GRAPHICS_3D_ATTRIBUTES<stkobjects/VEHICLE_GRAPHICS_3D_ATTRIBUTES_enum>
    ≔ ROUTE_GRAPHICS_3D_MARKER_TYPE<stkobjects/ROUTE_GRAPHICS_3D_MARKER_TYPE_enum>
    ≔ VEHICLE_ELLIPSE_OPTIONS<stkobjects/VEHICLE_ELLIPSE_OPTIONS_enum>
    ≔ VEHICLE_PROPAGATOR_TYPE<stkobjects/VEHICLE_PROPAGATOR_TYPE_enum>
    ≔ VEHICLE_SGP4_SWITCH_METHOD<stkobjects/VEHICLE_SGP4_SWITCH_METHOD_enum>
    ≔ VEHICLE_SGP4TLE_SELECTION<stkobjects/VEHICLE_SGP4TLE_SELECTION_enum>
    ≔ VEHICLE_SGP4_AUTO_UPDATE_SOURCE<stkobjects/VEHICLE_SGP4_AUTO_UPDATE_SOURCE_enum>
    ≔ THIRD_BODY_GRAV_SOURCE_TYPE<stkobjects/THIRD_BODY_GRAV_SOURCE_TYPE_enum>
    ≔ VEHICLE_GEOMAG_FLUX_SRC<stkobjects/VEHICLE_GEOMAG_FLUX_SRC_enum>
    ≔ VEHICLE_GEOMAG_FLUX_UPDATE_RATE<stkobjects/VEHICLE_GEOMAG_FLUX_UPDATE_RATE_enum>
    ≔ VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE<stkobjects/VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE_enum>
    ≔ VEHICLE_INTEGRATION_MODEL<stkobjects/VEHICLE_INTEGRATION_MODEL_enum>
    ≔ VEHICLE_PREDICTOR_CORRECTOR_SCHEME<stkobjects/VEHICLE_PREDICTOR_CORRECTOR_SCHEME_enum>
    ≔ VEHICLE_METHOD<stkobjects/VEHICLE_METHOD_enum>
    ≔ VEHICLE_INTERPOLATION_METHOD<stkobjects/VEHICLE_INTERPOLATION_METHOD_enum>
    ≔ VEHICLE_FRAME<stkobjects/VEHICLE_FRAME_enum>
    ≔ VEHICLE_CORRELATION_LIST_TYPE<stkobjects/VEHICLE_CORRELATION_LIST_TYPE_enum>
    ≔ VEHICLE_CONSIDER_ANALYSIS_TYPE<stkobjects/VEHICLE_CONSIDER_ANALYSIS_TYPE_enum>
    ≔ VEHICLE_WAYPOINT_COMP_METHOD<stkobjects/VEHICLE_WAYPOINT_COMP_METHOD_enum>
    ≔ VEHICLE_ALTITUDE_REFERENCE<stkobjects/VEHICLE_ALTITUDE_REFERENCE_enum>
    ≔ VEHICLE_WAYPOINT_INTERPOLATION_METHOD<stkobjects/VEHICLE_WAYPOINT_INTERPOLATION_METHOD_enum>
    ≔ VEHICLE_LAUNCH<stkobjects/VEHICLE_LAUNCH_enum>
    ≔ VEHICLE_IMPACT<stkobjects/VEHICLE_IMPACT_enum>
    ≔ VEHICLE_LAUNCH_CONTROL<stkobjects/VEHICLE_LAUNCH_CONTROL_enum>
    ≔ VEHICLE_IMPACT_LOCATION<stkobjects/VEHICLE_IMPACT_LOCATION_enum>
    ≔ VEHICLE_PASS_NUMBERING<stkobjects/VEHICLE_PASS_NUMBERING_enum>
    ≔ VEHICLE_PARTIAL_PASS_MEASUREMENT<stkobjects/VEHICLE_PARTIAL_PASS_MEASUREMENT_enum>
    ≔ VEHICLE_COORDINATE_SYSTEM<stkobjects/VEHICLE_COORDINATE_SYSTEM_enum>
    ≔ VEHICLE_BREAK_ANGLE_TYPE<stkobjects/VEHICLE_BREAK_ANGLE_TYPE_enum>
    ≔ VEHICLE_DIRECTION<stkobjects/VEHICLE_DIRECTION_enum>
    ≔ GRAPHICS_3D_LOCATION<stkobjects/GRAPHICS_3D_LOCATION_enum>
    ≔ GRAPHICS_3D_X_ORIGIN<stkobjects/GRAPHICS_3D_X_ORIGIN_enum>
    ≔ GRAPHICS_3D_Y_ORIGIN<stkobjects/GRAPHICS_3D_Y_ORIGIN_enum>
    ≔ GRAPHICS_3D_FONT_SIZE<stkobjects/GRAPHICS_3D_FONT_SIZE_enum>
    ≔ AIRCRAFT_WGS84_WARNING_TYPE<stkobjects/AIRCRAFT_WGS84_WARNING_TYPE_enum>
    ≔ SURFACE_REFERENCE<stkobjects/SURFACE_REFERENCE_enum>
    ≔ GRAPHICS_3D_FORMAT<stkobjects/GRAPHICS_3D_FORMAT_enum>
    ≔ ATTITUDE_STANDARD_TYPE<stkobjects/ATTITUDE_STANDARD_TYPE_enum>
    ≔ VEHICLE_ATTITUDE<stkobjects/VEHICLE_ATTITUDE_enum>
    ≔ VEHICLE_PROFILE<stkobjects/VEHICLE_PROFILE_enum>
    ≔ VEHICLE_LOOK_AHEAD_METHOD<stkobjects/VEHICLE_LOOK_AHEAD_METHOD_enum>
    ≔ VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION<stkobjects/VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION_enum>
    ≔ SENSOR_ALTITUDE_CROSSING_SIDES<stkobjects/SENSOR_ALTITUDE_CROSSING_SIDES_enum>
    ≔ SENSOR_ALTITUDE_CROSSING_DIRECTION<stkobjects/SENSOR_ALTITUDE_CROSSING_DIRECTION_enum>
    ≔ SENSOR_GRAPHICS_3D_INHERIT_FROM_2D<stkobjects/SENSOR_GRAPHICS_3D_INHERIT_FROM_2D_enum>
    ≔ SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE<stkobjects/SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE_enum>
    ≔ CHAIN_TIME_PERIOD_TYPE<stkobjects/CHAIN_TIME_PERIOD_TYPE_enum>
    ≔ CHAIN_CONST_CONSTRAINTS_MODE<stkobjects/CHAIN_CONST_CONSTRAINTS_MODE_enum>
    ≔ CHAIN_COV_ASSET_MODE<stkobjects/CHAIN_COV_ASSET_MODE_enum>
    ≔ CHAIN_PARENT_PLATFORM_RESTRICTION<stkobjects/CHAIN_PARENT_PLATFORM_RESTRICTION_enum>
    ≔ CHAIN_OPTIMAL_STRAND_METRIC_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_METRIC_TYPE_enum>
    ≔ CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE_enum>
    ≔ CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE_enum>
    ≔ CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE_enum>
    ≔ DATA_SAVE_MODE<stkobjects/DATA_SAVE_MODE_enum>
    ≔ COVERAGE_BOUNDS<stkobjects/COVERAGE_BOUNDS_enum>
    ≔ COVERAGE_POINT_LOC_METHOD<stkobjects/COVERAGE_POINT_LOC_METHOD_enum>
    ≔ COVERAGE_POINT_ALTITUDE_METHOD<stkobjects/COVERAGE_POINT_ALTITUDE_METHOD_enum>
    ≔ COVERAGE_GRID_CLASS<stkobjects/COVERAGE_GRID_CLASS_enum>
    ≔ COVERAGE_ALTITUDE_METHOD<stkobjects/COVERAGE_ALTITUDE_METHOD_enum>
    ≔ COVERAGE_GROUND_ALTITUDE_METHOD<stkobjects/COVERAGE_GROUND_ALTITUDE_METHOD_enum>
    ≔ COVERAGE_DATA_RETENTION<stkobjects/COVERAGE_DATA_RETENTION_enum>
    ≔ COVERAGE_REGION_ACCESS_ACCELERATION<stkobjects/COVERAGE_REGION_ACCESS_ACCELERATION_enum>
    ≔ COVERAGE_RESOLUTION<stkobjects/COVERAGE_RESOLUTION_enum>
    ≔ COVERAGE_ASSET_STATUS<stkobjects/COVERAGE_ASSET_STATUS_enum>
    ≔ COVERAGE_ASSET_GROUPING<stkobjects/COVERAGE_ASSET_GROUPING_enum>
    ≔ FIGURE_OF_MERIT_DEFINITION_TYPE<stkobjects/FIGURE_OF_MERIT_DEFINITION_TYPE_enum>
    ≔ FIGURE_OF_MERIT_SATISFACTION_TYPE<stkobjects/FIGURE_OF_MERIT_SATISFACTION_TYPE_enum>
    ≔ FIGURE_OF_MERIT_CONSTRAINT_NAME<stkobjects/FIGURE_OF_MERIT_CONSTRAINT_NAME_enum>
    ≔ FIGURE_OF_MERIT_COMPUTE<stkobjects/FIGURE_OF_MERIT_COMPUTE_enum>
    ≔ FIGURE_OF_MERIT_ACROSS_ASSETS<stkobjects/FIGURE_OF_MERIT_ACROSS_ASSETS_enum>
    ≔ FIGURE_OF_MERIT_COMPUTE_TYPE<stkobjects/FIGURE_OF_MERIT_COMPUTE_TYPE_enum>
    ≔ FIGURE_OF_MERIT_METHOD<stkobjects/FIGURE_OF_MERIT_METHOD_enum>
    ≔ FIGURE_OF_MERIT_END_GAP_OPTION<stkobjects/FIGURE_OF_MERIT_END_GAP_OPTION_enum>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE_enum>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD_enum>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT_enum>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION_enum>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION_enum>
    ≔ FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE<stkobjects/FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE_enum>
    ≔ IV_CLOCK_HOST<stkobjects/IV_CLOCK_HOST_enum>
    ≔ IV_TIME_SENSE<stkobjects/IV_TIME_SENSE_enum>
    ≔ GPS_ATTITUDE_MODEL_TYPE<stkobjects/GPS_ATTITUDE_MODEL_TYPE_enum>
    ≔ CONSTELLATION_CONSTRAINT_RESTRICTION<stkobjects/CONSTELLATION_CONSTRAINT_RESTRICTION_enum>
    ≔ EVENT_DETECTION<stkobjects/EVENT_DETECTION_enum>
    ≔ SAMPLING_METHOD<stkobjects/SAMPLING_METHOD_enum>
    ≔ COVERAGE_SATISFACTION_TYPE<stkobjects/COVERAGE_SATISFACTION_TYPE_enum>
    ≔ CCSDS_REFERENCE_FRAME<stkobjects/CCSDS_REFERENCE_FRAME_enum>
    ≔ CCSDS_DATE_FORMAT<stkobjects/CCSDS_DATE_FORMAT_enum>
    ≔ CCSDS_EPHEM_FORMAT<stkobjects/CCSDS_EPHEM_FORMAT_enum>
    ≔ CCSDS_TIME_SYSTEM<stkobjects/CCSDS_TIME_SYSTEM_enum>
    ≔ STK_EPHEM_COORDINATE_SYSTEM<stkobjects/STK_EPHEM_COORDINATE_SYSTEM_enum>
    ≔ STK_EPHEM_COVARIANCE_TYPE<stkobjects/STK_EPHEM_COVARIANCE_TYPE_enum>
    ≔ EXPORT_TOOL_VERSION_FORMAT<stkobjects/EXPORT_TOOL_VERSION_FORMAT_enum>
    ≔ EXPORT_TOOL_TIME_PERIOD<stkobjects/EXPORT_TOOL_TIME_PERIOD_enum>
    ≔ SPICE_INTERPOLATION<stkobjects/SPICE_INTERPOLATION_enum>
    ≔ ATTITUDE_COORDINATE_AXES<stkobjects/ATTITUDE_COORDINATE_AXES_enum>
    ≔ ATTITUDE_INCLUDE<stkobjects/ATTITUDE_INCLUDE_enum>
    ≔ EXPORT_TOOL_STEP_SIZE<stkobjects/EXPORT_TOOL_STEP_SIZE_enum>
    ≔ TEXT_OUTLINE_STYLE<stkobjects/TEXT_OUTLINE_STYLE_enum>
    ≔ MTO_RANGE_MODE<stkobjects/MTO_RANGE_MODE_enum>
    ≔ MTO_TRACK_EVAL<stkobjects/MTO_TRACK_EVAL_enum>
    ≔ MTO_ENTIRETY<stkobjects/MTO_ENTIRETY_enum>
    ≔ MTO_VISIBILITY_MODE<stkobjects/MTO_VISIBILITY_MODE_enum>
    ≔ MTO_OBJECT_INTERVAL<stkobjects/MTO_OBJECT_INTERVAL_enum>
    ≔ MTO_INPUT_DATA_TYPE<stkobjects/MTO_INPUT_DATA_TYPE_enum>
    ≔ SOLID_TIDE<stkobjects/SOLID_TIDE_enum>
    ≔ TIME_PERIOD_VALUE_TYPE<stkobjects/TIME_PERIOD_VALUE_TYPE_enum>
    ≔ ONE_POINT_ACCESS_STATUS<stkobjects/ONE_POINT_ACCESS_STATUS_enum>
    ≔ ONE_POINT_ACCESS_SUMMARY<stkobjects/ONE_POINT_ACCESS_SUMMARY_enum>
    ≔ LOOK_AHEAD_PROPAGATOR<stkobjects/LOOK_AHEAD_PROPAGATOR_enum>
    ≔ GRAPHICS_3D_MARKER_ORIENTATION<stkobjects/GRAPHICS_3D_MARKER_ORIENTATION_enum>
    ≔ SRP_MODEL<stkobjects/SRP_MODEL_enum>
    ≔ DRAG_MODEL<stkobjects/DRAG_MODEL_enum>
    ≔ VEHICLE_PROPAGATION_FRAME<stkobjects/VEHICLE_PROPAGATION_FRAME_enum>
    ≔ STAR_REFERENCE_FRAME<stkobjects/STAR_REFERENCE_FRAME_enum>
    ≔ GPS_REFERENCE_WEEK<stkobjects/GPS_REFERENCE_WEEK_enum>
    ≔ COVERAGE_CUSTOM_REGION_ALGORITHM<stkobjects/COVERAGE_CUSTOM_REGION_ALGORITHM_enum>
    ≔ VEHICLE_GPS_SWITCH_METHOD<stkobjects/VEHICLE_GPS_SWITCH_METHOD_enum>
    ≔ VEHICLE_GPS_ELEM_SELECTION<stkobjects/VEHICLE_GPS_ELEM_SELECTION_enum>
    ≔ VEHICLE_GPS_AUTO_UPDATE_SOURCE<stkobjects/VEHICLE_GPS_AUTO_UPDATE_SOURCE_enum>
    ≔ VEHICLE_GPS_ALMANAC_TYPE<stkobjects/VEHICLE_GPS_ALMANAC_TYPE_enum>
    ≔ STK_EXTERNAL_EPHEMERIS_FORMAT<stkobjects/STK_EXTERNAL_EPHEMERIS_FORMAT_enum>
    ≔ STK_EXTERNAL_FILE_MESSAGE_LEVEL<stkobjects/STK_EXTERNAL_FILE_MESSAGE_LEVEL_enum>
    ≔ COVERAGE_3D_DRAW_AT_ALTITUDE_MODE<stkobjects/COVERAGE_3D_DRAW_AT_ALTITUDE_MODE_enum>
    ≔ DISTANCE_ON_SPHERE<stkobjects/DISTANCE_ON_SPHERE_enum>
    ≔ FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE<stkobjects/FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE_enum>
    ≔ VEHICLE_SLEW_TIMING_BETWEEN_TARGETS<stkobjects/VEHICLE_SLEW_TIMING_BETWEEN_TARGETS_enum>
    ≔ VEHICLE_SLEW_MODE<stkobjects/VEHICLE_SLEW_MODE_enum>
    ≔ COMPONENT<stkobjects/COMPONENT_enum>
    ≔ VOLUMETRIC_DEFINITION_TYPE<stkobjects/VOLUMETRIC_DEFINITION_TYPE_enum>
    ≔ VOLUMETRIC_SPATIAL_CALC_EVAL_TYPE<stkobjects/VOLUMETRIC_SPATIAL_CALC_EVAL_TYPE_enum>
    ≔ VOLUMETRIC_SAVE_COMPUTED_DATA_TYPE<stkobjects/VOLUMETRIC_SAVE_COMPUTED_DATA_TYPE_enum>
    ≔ VOLUMETRIC_DISPLAY_VOLUME_TYPE<stkobjects/VOLUMETRIC_DISPLAY_VOLUME_TYPE_enum>
    ≔ VOLUMETRIC_DISPLAY_QUALITY_TYPE<stkobjects/VOLUMETRIC_DISPLAY_QUALITY_TYPE_enum>
    ≔ VOLUMETRIC_LEGEND_NUMERIC_NOTATION<stkobjects/VOLUMETRIC_LEGEND_NUMERIC_NOTATION_enum>
    ≔ VOLUMETRIC_LEVEL_ORDER<stkobjects/VOLUMETRIC_LEVEL_ORDER_enum>
    ≔ SENSOR_EOIR_PROCESSING_LEVELS<stkobjects/SENSOR_EOIR_PROCESSING_LEVELS_enum>
    ≔ SENSOR_EOIR_JITTER_TYPES<stkobjects/SENSOR_EOIR_JITTER_TYPES_enum>
    ≔ SENSOR_EOIR_SCAN_MODES<stkobjects/SENSOR_EOIR_SCAN_MODES_enum>
    ≔ SENSOR_EOIR_BAND_IMAGE_QUALITY<stkobjects/SENSOR_EOIR_BAND_IMAGE_QUALITY_enum>
    ≔ SENSOR_EOIR_BAND_SPECTRAL_SHAPE<stkobjects/SENSOR_EOIR_BAND_SPECTRAL_SHAPE_enum>
    ≔ SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE<stkobjects/SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE_enum>
    ≔ SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS<stkobjects/SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS_enum>
    ≔ SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE<stkobjects/SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE_enum>
    ≔ SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE<stkobjects/SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE_enum>
    ≔ SENSOR_EOIR_BAND_RAD_PARAM_LEVEL<stkobjects/SENSOR_EOIR_BAND_RAD_PARAM_LEVEL_enum>
    ≔ SENSOR_EOIR_BAND_QE_MODE<stkobjects/SENSOR_EOIR_BAND_QE_MODE_enum>
    ≔ SENSOR_EOIR_BAND_QUANTIZATION_MODE<stkobjects/SENSOR_EOIR_BAND_QUANTIZATION_MODE_enum>
    ≔ SENSOR_EOIR_BAND_WAVELENGTH_TYPE<stkobjects/SENSOR_EOIR_BAND_WAVELENGTH_TYPE_enum>
    ≔ SENSOR_EOIR_BAND_SATURATION_MODE<stkobjects/SENSOR_EOIR_BAND_SATURATION_MODE_enum>
    ≔ VOLUMETRIC_VOLUME_GRID_EXPORT_TYPE<stkobjects/VOLUMETRIC_VOLUME_GRID_EXPORT_TYPE_enum>
    ≔ VOLUMETRIC_DATA_EXPORT_FORMAT_TYPE<stkobjects/VOLUMETRIC_DATA_EXPORT_FORMAT_TYPE_enum>
    ≔ CONSTELLATION_FROM_TO_PARENT_CONSTRAINT<stkobjects/CONSTELLATION_FROM_TO_PARENT_CONSTRAINT_enum>
    ≔ ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS<stkobjects/ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS_enum>
    ≔ STATISTICS<stkobjects/STATISTICS_enum>
    ≔ TIME_VARYING_EXTREMUM<stkobjects/TIME_VARYING_EXTREMUM_enum>
    ≔ MODEL_GLTF_REFLECTION_MAP_TYPE<stkobjects/MODEL_GLTF_REFLECTION_MAP_TYPE_enum>
    ≔ SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE<stkobjects/SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE_enum>
    ≔ LOP_ATMOSPHERIC_DENSITY_MODEL<stkobjects/LOP_ATMOSPHERIC_DENSITY_MODEL_enum>
    ≔ LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL<stkobjects/LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL_enum>
    ≔ EPHEM_EXPORT_TOOL_FILE_FORMAT<stkobjects/EPHEM_EXPORT_TOOL_FILE_FORMAT_enum>
    ≔ ADV_CAT_ELLIPSOID_CLASS<stkobjects/ADV_CAT_ELLIPSOID_CLASS_enum>
    ≔ ADV_CAT_CONJUNCTION_TYPE<stkobjects/ADV_CAT_CONJUNCTION_TYPE_enum>
    ≔ ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE<stkobjects/ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE_enum>
    ≔ EOIR_SHAPE_TYPE<stkobjects/EOIR_SHAPE_TYPE_enum>
    ≔ EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE<stkobjects/EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE_enum>
    ≔ EOIR_THERMAL_MODEL_TYPE<stkobjects/EOIR_THERMAL_MODEL_TYPE_enum>
    ≔ EOIR_FLIGHT_TYPE<stkobjects/EOIR_FLIGHT_TYPE_enum>
    ≔ COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE<stkobjects/COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE_enum>
    ≔ SWATH_COMPUTATIONAL_METHOD<stkobjects/SWATH_COMPUTATIONAL_METHOD_enum>
    ≔ CLASSICAL_LOCATION<stkobjects/CLASSICAL_LOCATION_enum>
    ≔ ORIENTATION_ASC_NODE<stkobjects/ORIENTATION_ASC_NODE_enum>
    ≔ GEODETIC_SIZE<stkobjects/GEODETIC_SIZE_enum>
    ≔ DELAUNAY_L_TYPE<stkobjects/DELAUNAY_L_TYPE_enum>
    ≔ DELAUNAY_H_TYPE<stkobjects/DELAUNAY_H_TYPE_enum>
    ≔ DELAUNAY_G_TYPE<stkobjects/DELAUNAY_G_TYPE_enum>
    ≔ EQUINOCTIAL_SIZE_SHAPE<stkobjects/EQUINOCTIAL_SIZE_SHAPE_enum>
    ≔ MIXED_SPHERICAL_FLIGHT_PATH_ANGLE<stkobjects/MIXED_SPHERICAL_FLIGHT_PATH_ANGLE_enum>
    ≔ SPHERICAL_FLIGHT_PATH_ANGLE<stkobjects/SPHERICAL_FLIGHT_PATH_ANGLE_enum>
    ≔ CLASSICAL_SIZE_SHAPE<stkobjects/CLASSICAL_SIZE_SHAPE_enum>
    ≔ EQUINOCTIAL_FORMULATION<stkobjects/EQUINOCTIAL_FORMULATION_enum>
    ≔ SCATTERING_POINT_PROVIDER_TYPE<stkobjects/SCATTERING_POINT_PROVIDER_TYPE_enum>
    ≔ SCATTERING_POINT_MODEL_TYPE<stkobjects/SCATTERING_POINT_MODEL_TYPE_enum>
    ≔ SCATTERING_POINT_PROVIDER_LIST_TYPE<stkobjects/SCATTERING_POINT_PROVIDER_LIST_TYPE_enum>
    ≔ POLARIZATION_TYPE<stkobjects/POLARIZATION_TYPE_enum>
    ≔ POLARIZATION_REFERENCE_AXIS<stkobjects/POLARIZATION_REFERENCE_AXIS_enum>
    ≔ NOISE_TEMP_COMPUTE_TYPE<stkobjects/NOISE_TEMP_COMPUTE_TYPE_enum>
    ≔ POINTING_STRATEGY_TYPE<stkobjects/POINTING_STRATEGY_TYPE_enum>
    ≔ WAVEFORM_TYPE<stkobjects/WAVEFORM_TYPE_enum>
    ≔ FREQUENCY_SPEC<stkobjects/FREQUENCY_SPEC_enum>
    ≔ PRF_MODE<stkobjects/PRF_MODE_enum>
    ≔ PULSE_WIDTH_MODE<stkobjects/PULSE_WIDTH_MODE_enum>
    ≔ WAVEFORM_SELECTION_STRATEGY_TYPE<stkobjects/WAVEFORM_SELECTION_STRATEGY_TYPE_enum>
    ≔ ANTENNA_CONTROL_REFERENCE_TYPE<stkobjects/ANTENNA_CONTROL_REFERENCE_TYPE_enum>
    ≔ ANTENNA_MODEL_TYPE<stkobjects/ANTENNA_MODEL_TYPE_enum>
    ≔ ANTENNA_CONTOUR_TYPE<stkobjects/ANTENNA_CONTOUR_TYPE_enum>
    ≔ CIRCULAR_APERTURE_INPUT_TYPE<stkobjects/CIRCULAR_APERTURE_INPUT_TYPE_enum>
    ≔ RECTANGULAR_APERTURE_INPUT_TYPE<stkobjects/RECTANGULAR_APERTURE_INPUT_TYPE_enum>
    ≔ DIRECTION_PROVIDER_TYPE<stkobjects/DIRECTION_PROVIDER_TYPE_enum>
    ≔ BEAMFORMER_TYPE<stkobjects/BEAMFORMER_TYPE_enum>
    ≔ ELEMENT_CONFIGURATION_TYPE<stkobjects/ELEMENT_CONFIGURATION_TYPE_enum>
    ≔ LATTICE_TYPE<stkobjects/LATTICE_TYPE_enum>
    ≔ SPACING_UNIT<stkobjects/SPACING_UNIT_enum>
    ≔ LIMITS_EXCEEDED_BEHAVIOR_TYPE<stkobjects/LIMITS_EXCEEDED_BEHAVIOR_TYPE_enum>
    ≔ ANTENNA_GRAPHICS_COORDINATE_SYSTEM<stkobjects/ANTENNA_GRAPHICS_COORDINATE_SYSTEM_enum>
    ≔ ANTENNA_MODEL_INPUT_TYPE<stkobjects/ANTENNA_MODEL_INPUT_TYPE_enum>
    ≔ HFSS_FFD_GAIN_TYPE<stkobjects/HFSS_FFD_GAIN_TYPE_enum>
    ≔ ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE<stkobjects/ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE_enum>
    ≔ BEAM_SELECTION_STRATEGY_TYPE<stkobjects/BEAM_SELECTION_STRATEGY_TYPE_enum>
    ≔ TRANSMITTER_MODEL_TYPE<stkobjects/TRANSMITTER_MODEL_TYPE_enum>
    ≔ TRANSFER_FUNCTION_TYPE<stkobjects/TRANSFER_FUNCTION_TYPE_enum>
    ≔ RE_TRANSMITTER_OP_MODE<stkobjects/RE_TRANSMITTER_OP_MODE_enum>
    ≔ RECEIVER_MODEL_TYPE<stkobjects/RECEIVER_MODEL_TYPE_enum>
    ≔ LINK_MARGIN_TYPE<stkobjects/LINK_MARGIN_TYPE_enum>
    ≔ RADAR_STC_ATTENUATION_TYPE<stkobjects/RADAR_STC_ATTENUATION_TYPE_enum>
    ≔ RADAR_FREQUENCY_SPEC<stkobjects/RADAR_FREQUENCY_SPEC_enum>
    ≔ RADAR_SNR_CONTOUR_TYPE<stkobjects/RADAR_SNR_CONTOUR_TYPE_enum>
    ≔ RADAR_MODEL_TYPE<stkobjects/RADAR_MODEL_TYPE_enum>
    ≔ RADAR_MODE_TYPE<stkobjects/RADAR_MODE_TYPE_enum>
    ≔ RADAR_WAVEFORM_SEARCH_TRACK_TYPE<stkobjects/RADAR_WAVEFORM_SEARCH_TRACK_TYPE_enum>
    ≔ RADAR_SEARCH_TRACK_PRF_MODE<stkobjects/RADAR_SEARCH_TRACK_PRF_MODE_enum>
    ≔ RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE<stkobjects/RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE_enum>
    ≔ RADAR_SAR_PRF_MODE<stkobjects/RADAR_SAR_PRF_MODE_enum>
    ≔ RADAR_SAR_RANGE_RESOLUTION_MODE<stkobjects/RADAR_SAR_RANGE_RESOLUTION_MODE_enum>
    ≔ RADAR_SAR_PCR_MODE<stkobjects/RADAR_SAR_PCR_MODE_enum>
    ≔ RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE<stkobjects/RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE_enum>
    ≔ RADAR_P_DET_TYPE<stkobjects/RADAR_P_DET_TYPE_enum>
    ≔ RADAR_PULSE_INTEGRATION_TYPE<stkobjects/RADAR_PULSE_INTEGRATION_TYPE_enum>
    ≔ RADAR_PULSE_INTEGRATOR_TYPE<stkobjects/RADAR_PULSE_INTEGRATOR_TYPE_enum>
    ≔ RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE<stkobjects/RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE_enum>
    ≔ RADAR_CLUTTER_GEOMETRY_MODEL_TYPE<stkobjects/RADAR_CLUTTER_GEOMETRY_MODEL_TYPE_enum>
    ≔ RADAR_CLUTTER_MAP_MODEL_TYPE<stkobjects/RADAR_CLUTTER_MAP_MODEL_TYPE_enum>
    ≔ RADAR_SWERLING_CASE<stkobjects/RADAR_SWERLING_CASE_enum>
    ≔ RCS_COMPUTE_STRATEGY<stkobjects/RCS_COMPUTE_STRATEGY_enum>
    ≔ RADAR_ACTIVITY_TYPE<stkobjects/RADAR_ACTIVITY_TYPE_enum>
    ≔ RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION<stkobjects/RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION_enum>
    ≔ RF_FILTER_MODEL_TYPE<stkobjects/RF_FILTER_MODEL_TYPE_enum>
    ≔ MODULATOR_MODEL_TYPE<stkobjects/MODULATOR_MODEL_TYPE_enum>
    ≔ DEMODULATOR_MODEL_TYPE<stkobjects/DEMODULATOR_MODEL_TYPE_enum>
    ≔ RAIN_LOSS_MODEL_TYPE<stkobjects/RAIN_LOSS_MODEL_TYPE_enum>
    ≔ ATMOSPHERIC_ABSORPTION_MODEL_TYPE<stkobjects/ATMOSPHERIC_ABSORPTION_MODEL_TYPE_enum>
    ≔ URBAN_TERRESTRIAL_LOSS_MODEL_TYPE<stkobjects/URBAN_TERRESTRIAL_LOSS_MODEL_TYPE_enum>
    ≔ CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE<stkobjects/CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE_enum>
    ≔ CLOUDS_AND_FOG_LIQUID_WATER_CHOICES<stkobjects/CLOUDS_AND_FOG_LIQUID_WATER_CHOICES_enum>
    ≔ IONOSPHERIC_FADING_LOSS_MODEL_TYPE<stkobjects/IONOSPHERIC_FADING_LOSS_MODEL_TYPE_enum>
    ≔ TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE<stkobjects/TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE_enum>
    ≔ TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES<stkobjects/TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES_enum>
    ≔ PROJECTION_HORIZONTAL_DATUM_TYPE<stkobjects/PROJECTION_HORIZONTAL_DATUM_TYPE_enum>
    ≔ BUILD_HEIGHT_REFERENCE_METHOD<stkobjects/BUILD_HEIGHT_REFERENCE_METHOD_enum>
    ≔ BUILD_HEIGHT_UNIT<stkobjects/BUILD_HEIGHT_UNIT_enum>
    ≔ TIREM_POLARIZATION_TYPE<stkobjects/TIREM_POLARIZATION_TYPE_enum>
    ≔ VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE<stkobjects/VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE_enum>
    ≔ VOACAP_COEFFICIENT_DATA_TYPE<stkobjects/VOACAP_COEFFICIENT_DATA_TYPE_enum>
    ≔ LASER_PROPAGATION_LOSS_MODEL_TYPE<stkobjects/LASER_PROPAGATION_LOSS_MODEL_TYPE_enum>
    ≔ LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE<stkobjects/LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE_enum>
    ≔ ATMOSPHERIC_TURBULENCE_MODEL_TYPE<stkobjects/ATMOSPHERIC_TURBULENCE_MODEL_TYPE_enum>
    ≔ MODTRAN_AEROSOL_MODEL_TYPE<stkobjects/MODTRAN_AEROSOL_MODEL_TYPE_enum>
    ≔ MODTRAN_CLOUD_MODEL_TYPE<stkobjects/MODTRAN_CLOUD_MODEL_TYPE_enum>
    ≔ COMM_SYSTEM_REFERENCE_BANDWIDTH<stkobjects/COMM_SYSTEM_REFERENCE_BANDWIDTH_enum>
    ≔ COMM_SYSTEM_CONSTRAINING_ROLE<stkobjects/COMM_SYSTEM_CONSTRAINING_ROLE_enum>
    ≔ COMM_SYSTEM_SAVE_MODE<stkobjects/COMM_SYSTEM_SAVE_MODE_enum>
    ≔ COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE<stkobjects/COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE_enum>
    ≔ COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE<stkobjects/COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE_enum>
    ≔ COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE<stkobjects/COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE_enum>
    ≔ SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY<stkobjects/SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY_enum>
    ≔ SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY<stkobjects/SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY_enum>
    ≔ SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY<stkobjects/SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY_enum>
    ≔ SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE<stkobjects/SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE_enum>
    ≔ SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE<stkobjects/SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE_enum>
    ≔ SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD<stkobjects/SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD_enum>
    ≔ SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD<stkobjects/SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD_enum>
    ≔ SPACE_ENVIRONMENT_SAA_CHANNEL<stkobjects/SPACE_ENVIRONMENT_SAA_CHANNEL_enum>
    ≔ SPACE_ENVIRONMENT_SAA_FLUX_LEVEL<stkobjects/SPACE_ENVIRONMENT_SAA_FLUX_LEVEL_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL<stkobjects/VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_MATERIAL<stkobjects/VEHICLE_SPACE_ENVIRONMENT_MATERIAL_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL<stkobjects/VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY<stkobjects/VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE_enum>
    ≔ VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE_enum>
    ≔ NOTIFICATION_FILTER_MASK<stkobjects/NOTIFICATION_FILTER_MASK_enum>

