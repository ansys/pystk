
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
        

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessAdvanced`
              - Interface for configuring advanced targeting access computation properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessConstraint`
              - AccessConstraint used to access the AccessConstraint attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessConstraintMinMaxBase`
              - Access Constraint used for min/max constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.IAccessInterval`
              - Base interface for ITimePeriod and TimeIntervalCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.IAnimation`
              - Provide methods to control scenario animation.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaBeam`
              - Provide access to an antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaBeamSelectionStrategy`
              - Provide access to a beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`
              - IAntennaContour Interface for a antenna's contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAntennaModelOpticalSimple`
              - Provide access to the properties and methods defining a simple optical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAreaTypeData`
              - Base interface IAreaTypeData. AreaTypePatternCollection and AreaTypeEllipse derive from it.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModel`
              - Provide access to the properties and methods an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelITURP676`
              - Provide access to the properties and methods of the ITU-R P676 atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelTIREM`
              - Provide access to the properties and methods of the TIREM atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAtmosphericTurbulenceModel`
              - Provide access to a refractive index structure parameter model.

            * - :py:class:`~ansys.stk.core.stkobjects.IAzElMaskData`
              - Base interface IAzElMaskData. SensorAzElMaskFile implements this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IBeamformer`
              - Provide access to the properties and methods defining a beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.ICelestialBodyInformation`
              - The interface represents information associated with a celestial body.

            * - :py:class:`~ansys.stk.core.stkobjects.ICelestialBodyInformationCollection`
              - Represents a collection of celestial bodies.

            * - :py:class:`~ansys.stk.core.stkobjects.IChainTimePeriod`
              - Chain time period options.

            * - :py:class:`~ansys.stk.core.stkobjects.IClassicalLocation`
              - Base Interface of all IClassicalLocation* interfaces.

            * - :py:class:`~ansys.stk.core.stkobjects.IClassicalSizeShape`
              - Base Interface for SizeShape property. ClassicalSizeShapeAltitude, ClassicalSizeShapeMeanMotion, ClassicalSizeShapePeriod, ClassicalSizeShapeRadius and ClassicalSizeShapeSemimajorAxis derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.ICloneable`
              - Interface for a component.

            * - :py:class:`~ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModel`
              - Provide access to the properties and methods for Clouds and Fog loss models.

            * - :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessEventDetection`
              - Provide access to the properties an access event detection algorithm.

            * - :py:class:`~ansys.stk.core.stkobjects.ICommSystemAccessSamplingMethod`
              - Provide access to the properties for the sampling method.

            * - :py:class:`~ansys.stk.core.stkobjects.ICommSystemLinkSelectionCriteria`
              - Provide access to a link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`
              - Interface for a component.

            * - :py:class:`~ansys.stk.core.stkobjects.IComponentLinkEmbedControl`
              - Interface for a control which manages the linking or embedding of a component from the component browser.

            * - :py:class:`~ansys.stk.core.stkobjects.IConstellationConstraintRestriction`
              - A base interface for all interfaces returned by the Restriction property of the ConstellationConstraints interface. It can be cast to ConstellationConstraintObjectRestriction.

            * - :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`
              - Base interface for ICoverageBoundsCustom, CoverageBoundsGlobal, CoverageBoundsLatitude, CoverageBoundsLatitudeLines, CoverageBoundsLongitudeLines, CoverageBoundsCustomBoundary.

            * - :py:class:`~ansys.stk.core.stkobjects.ICoverageResolution`
              - Base interface for CoverageResolutionArea, CoverageResolutionDistance and CoverageResolutionLatLon, used to define coverage resolution (spacing between grid points).

            * - :py:class:`~ansys.stk.core.stkobjects.IDataProvider`
              - Represents the Sub Data Provider (i.e. ``Fixed`` in ``Cartesian Position`` group on satellites, or ``Cartesian Position`` on facilities).

            * - :py:class:`~ansys.stk.core.stkobjects.IDataProviderInfo`
              - Provide methods for retrieving the information about data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.IDelaunayActionVariable`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~ansys.stk.core.stkobjects.IDemodulatorModel`
              - Provide access to the properties and methods defining a demodulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.IDirectionProvider`
              - Provide access to the properties and methods defining an direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.IDisplayDistance`
              - Base interface IDisplayDistance. ISensorProjectionDisplayDistance, SensorProjectionConstantAltitude and SensorProjectionObjectAltitude derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IDisplayTime`
              - The display time interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IDisplayTimesData`
              - Base Interface IDisplayTimesData. TimeIntervalCollection, DisplayTimesDuringAccess and DisplayTimesTimeComponent derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IElementConfiguration`
              - Provide access to the properties and methods defining an element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.IElementConfigurationPolygon`
              - Provide access to the properties and methods defining a polygon element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.IEOIR`
              - Property used to access IEOIR interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IEOIRShapeObject`
              - A shape object interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IEventDetectionStrategy`
              - Define a base interface for the event detection strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinition`
              - Figure of Merit definition.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionData`
              - IFigureOfMeritDefinitionData.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritNavigationAccuracyMethod`
              - Navigation Accuracy Figure of Merit type.

            * - :py:class:`~ansys.stk.core.stkobjects.IFlightPathAngle`
              - Base Interface IFlightPathAngle. MixedSphericalFlightPathAngleHorizontal, MixedSphericalFlightPathAngleVertical, SphericalFlightPathAngleHorizontal and SphericalFlightPathAngleVertical derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IGeodeticSize`
              - Base Interface IGeodeticSize. DeticSizeAltitude and DeticSizeRadius derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DMarkerData`
              - Base Interface IGraphics3DMarkerData.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModel`
              - IGraphics3DModel used to access the 3D model attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DModelData`
              - IGraphics3DModelData base interface. Graphics3DModelFile and Graphics3DModelCollection derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`
              - IGraphics3DReferenceAnalysisWorkbenchComponent used to access the shared properties of all 3D RefCrdn.

            * - :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics`
              - 2D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.IGreatArcGraphics3D`
              - 3D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.IGreatArcVehicle`
              - A base interface for all Great Arc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.IIonosphericFadingLossModel`
              - Provide access to the properties and methods for an Ionospheric Fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ILaserAtmosphericLossModel`
              - Provide access to the properties and methods for a laser atmospheric absorption loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ILaserPropagationChannel`
              - Provide access to laser propagation loss models.

            * - :py:class:`~ansys.stk.core.stkobjects.ILaserTroposphericScintillationLossModel`
              - Provide access to the properties and methods for a laser tropospheric scintillation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition`
              - Interface to set and retrieve the LLA position type.

            * - :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`
              - Provide the information about the lifetime of the object.

            * - :py:class:`~ansys.stk.core.stkobjects.IModulatorModel`
              - Provide access to the properties and methods defining a modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.IModulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.IOrbitDisplayData`
              - IOrbitDisplayData Interface. PlanetOrbitDisplayTime derives from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IOrientationAscNode`
              - Base Interface to OrientationLongitudeOfAscending and OrientationRightAscensionOfAscendingNode.

            * - :py:class:`~ansys.stk.core.stkobjects.IPlatformRFEnvironment`
              - Provide access to the properties and methods defining the platform RF environment.

            * - :py:class:`~ansys.stk.core.stkobjects.IPointingStrategy`
              - Provide the base interface for a pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarization`
              - Provide the base interface for the a polarization object.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationCrossPolLeakage`
              - Provide the interface for polarization cross pol leakage.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationElliptical`
              - Provide the interface for elliptical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationHorizontal`
              - Provide the interface for linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationLinear`
              - Provide the interface for linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPolarizationVertical`
              - Provide the interface for linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.IPositionSourceData`
              - Base interface to PlanetPositionCentralBody and PlanetPositionFile.

            * - :py:class:`~ansys.stk.core.stkobjects.IPropagator`
              - Base vehicle propagator interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IPropagatorSGP4LoadData`
              - Load Method Data interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IProvideSpatialInfo`
              - Provide methods for accessing spatial information for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarActivity`
              - Provide access to the properties and methods defining radar activity.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterGeometryModel`
              - Do not use this interface, as it is deprecated. Use IScatteringPointProvider interface instead. Provides access to the properties and methods defining a radar clutter geometry model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterGeometryModelPlugin`
              - Do not use this interface, as it is deprecated. Use ScatteringPointProviderPlugin interface instead. Provides access to the properties and methods defining a radar clutter geometry plugin model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMap`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar clutter map.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapInheritable`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar inheritable clutter map.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapModel`
              - Do not use this interface, as it is deprecated. Use IScatteringPointModel interface instead. Provides access to the properties and methods defining a radar clutter map model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapModelConstantCoefficient`
              - Do not use this interface, as it is deprecated. Use ScatteringPointModelConstantCoefficient interface instead. Provides access to the properties and methods defining a radar clutter map constant coefficient model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarClutterMapModelPlugin`
              - Do not use this interface, as it is deprecated. Use ScatteringPointModelPlugin interface instead. Provides access to the properties and methods defining a radar clutter map plugin model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarContinuousWaveAnalysisMode`
              - Interface which defines an continuous wave analysis.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarCrossSectionComputeStrategy`
              - Provide access to the properties and methods defining a radar cross section compute Strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver mode.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModeBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter mode.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModel`
              - Provide access to the properties and methods defining a radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarModeMonostatic`
              - Provide access to the properties and methods defining a monostatic mode.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarProbabilityOfDetection`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarProbabilityOfDetectionCFAR`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarPulseIntegration`
              - Interface which defines an integration method.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarSTCAttenuation`
              - Provide access to the properties and methods defining a radar STC attenuation.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarSTCAttenuationMap`
              - Provide access to the properties and methods defining a radar STC attenuation map.

            * - :py:class:`~ansys.stk.core.stkobjects.IRadarWaveformSearchTrack`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.IRainLossModel`
              - Provide access to the properties and methods a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IReceiverModel`
              - Provide access to the properties and methods defining a receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.IReceiverModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRefractionModelBase`
              - A base interface for the Refraction Models.

            * - :py:class:`~ansys.stk.core.stkobjects.IReTransmitterModel`
              - Provide access to the properties and methods defining a re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.IRFFilterModel`
              - Provide access to the properties and methods defining an RF filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ISamplingMethodStrategy`
              - Define a base interface for the sampling method strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.IScatteringPointModel`
              - Provide access to the properties and methods defining a scattering point model model.

            * - :py:class:`~ansys.stk.core.stkobjects.IScatteringPointProvider`
              - Provide access to the properties and methods defining a scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorPattern`
              - Base interface ISensorPattern. SensorComplexConicPattern, SensorCustomPattern, SensorHalfPowerPattern, SensorRectangularPattern, SensorSARPattern, SensorEOIRPattern and SensorSimpleConicPattern implement this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`
              - Base interface ISensorPointing. SensorPointing3DModel, SensorPointingExternal, SensorPointingFixed, SensorPointingFixedInAxes, SensorPointingGrazingAltitude, SensorPointingTargeted, SensorPointingAlongVector and SensorPointingSchedule implement this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorPointingTargetedBoresight`
              - Base interface ISensorPointingTargetedBoresight. SensorPointingTargetedBoresightFixed and SensorPointingTargetedBoresightTrack derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.ISensorProjectionDisplayDistance`
              - ISensorProjectionDisplayDistance Interface for setting projection altitude options for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.ISolarActivityConfiguration`
              - Provide access to the properties and methods defining the solar activity configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ISRPModelBase`
              - A base interface for solar radiation pressure models.

            * - :py:class:`~ansys.stk.core.stkobjects.ISTKObject`
              - Represents the instance of STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.ISTKObjectCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~ansys.stk.core.stkobjects.ISTKObjectElementCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~ansys.stk.core.stkobjects.ITargetSelectionMethod`
              - Provide access to the properties and methods defining a target selection method.

            * - :py:class:`~ansys.stk.core.stkobjects.ITerrainNormData`
              - Base Interface ITerrainNormData. TerrainNormalSlopeAzimuth derives from this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.ITimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~ansys.stk.core.stkobjects.ITransmitterModel`
              - Provide access to the properties and methods defining a transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ITransmitterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModel`
              - Provide access to the properties and methods for a TropoSpheric Scintillation Fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IUrbanTerrestrialLossModel`
              - Provide access to the properties and methods for an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`
              - Base interface for vehicle attitude options.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`
              - The base interface that all vehicle attitude profiles are derived from.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewBase`
              - Represents an attitude slew base type.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`
              - Standard attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleBreakAngle`
              - Base Interface IVehicleBreakAngle. VehicleBreakAngleBreakByLatitude and VehicleBreakAngleBreakByLongitude derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleCoordinateAxes`
              - IVehicleCoordinateAxes.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGPSAlmanacProperties`
              - A common base interface for GPS almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributes`
              - Base Interface for Vehicle 2D Graphics Attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesBasic`
              - Basic 2D Graphics Attributes for a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesDisplayState`
              - Provide access to non-trivial properties of 2D vehicle attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DElevation`
              - Base Interface IVehicleGraphics2DElevation. VehicleGraphics2DElevationGroundElevation, IVehicleGraphics2DElevationsSwathHalfWidth and IVehicleGraphics2DElevationsSwathHalfAngle derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DPass`
              - interface IVehicleGraphics2DPass. VehicleGraphics2DPassShowPasses and VehicleGraphics2DPassResolution derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeComponentsElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DTimeEventType`
              - Base Interface IVehicleGraphics2DTimeEventType. VehicleGraphics2DTimeEventTypeLine, VehicleGraphics2DTimeEventTypeMarker and VehicleGraphics2DTimeEventTypeText derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DAttributes`
              - Base Interface IVehicleGraphics3DAttributes. VehicleGraphics3DAttributesBasic and VehicleGraphics3DAttributesIntervals derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTargetPointPosition`
              - A base class for BPlane target point position interfaces.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximity`
              - Base Proximity graphics interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DProximityAreaObject`
              - A base class that defines methods and properties common to all proximity area objects.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSigmaScale`
              - Base Interface IVehicleGraphics3DSigmaScale. VehicleGraphics3DSigmaScaleScale and VehicleGraphics3DSigmaScaleProbability derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DSystemsElementBase`
              - Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTickData`
              - Base interface IVehicleGraphics3DTickData. VehicleGraphics3DTickDataLine and VehicleGraphics3DTickDataPoint derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleHPOPDragModel`
              - A base interface for drag models.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleImpact`
              - Base Interface IVehicleImpact. VehicleImpactLocationDetic and VehicleImpactLocationCentric derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleImpactLocation`
              - Base interface IVehicleImpactLocation. VehicleImpactLocationLaunchAzEl and VehicleImpactLocationPoint derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLaunch`
              - Base interface IVehicleLaunch. LaunchVehicleLocationDetic and LaunchVehicleLocationCentric derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLaunchControl`
              - Base Interface IVehicleLaunchControl. LaunchVehicleControlFixedApogeeAltitude, LaunchVehicleControlFixedDeltaV, IVehicleLaunchControlDixedDeltaVMinEcc and IVehicleLaunchControlTimeOfFlight derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLeadTrailData`
              - Base interface IVehicleLeadTrailData.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLeadTrailDataFraction`
              - The percentage of the leading or trailing portion of a vehicle's path that will display in the 2D or 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleLeadTrailDataTime`
              - Configure the amount of time to display the vehicle's path in 2D or 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehiclePassNumbering`
              - Base Interaface IVehiclePassNumbering. PassBreakNumberingDateOfFirstPass and PassBreakNumberingFirstPassNumber derive from this.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehiclePointing`
              - Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleSolarFluxGeoMagnitude`
              - Base Interface IVehicleSolarFluxGeoMagnitude. SolarFluxGeoMagneticValueSettings and SolarFluxGeoMagneticFileSettings derive from this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReference`
              - Base interface for the altitude references.

            * - :py:class:`~ansys.stk.core.stkobjects.IVolumetricGridDefinition`
              - Base interface IVolumetricGridDefinition. VolumetricGridSpatialCalculation and VolumetricExternalFile implement this interface.

            * - :py:class:`~ansys.stk.core.stkobjects.IWaveform`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.IWaveformSelectionStrategy`
              - Provide the base interface for a waveform selection strategy.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.Access`
              - Class defining Access.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessAdvancedSettings`
              - Class defining advanced Access settings.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessAllowedTimeIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraint`
              - Class defining access constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbench`
              - Class related to Analysis Workbench constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchCollection`
              - Collection of Analysis Workbench constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAnalysisWorkbenchComponent`
              - Class related to Vector constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintAngle`
              - Class defining Angle constraints, limiting access to intervals during which the selected angle is within the specified minimum and maximum limits.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintBackground`
              - Class related to the Background constraint, which constrains access periods based on whether the Earth is or is not in the background.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCentralBodyObstruction`
              - Class defining constraints in terms of obstruction by a specified central body.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCollection`
              - Collection of access constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintCondition`
              - Class defining access constraints in terms of lighting conditions.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintExclZonesCollection`
              - Collection of Exclusion Zones used in Exclusion Zone constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintGrazingAltitude`
              - Class defining the Grazing Altidude constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintGroundTrack`
              - Class related to the Ground Track constraint, which constrains access to the Ascending or Descending side of the Satellite's ground track.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintIntervals`
              - Class defining the Intervals constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintLatitudeLongitudeZone`
              - Class defining the Exclusion Zone constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintMinMaxBase`
              - Class related to defining constraints in terms of minimum and/or maximum values.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintObjExAngle`
              - Class defining the Object Exclusion Angle constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintPluginMinMax`
              - Class related to defining access plugin constraints in terms of minimum and/or maximum values.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintThirdBody`
              - Do not use this class, as it is deprecated. Use AccessConstraintCentralBodyObstruction instead. Class defining Central Body Obstruction constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintTimeSlipRange`
              - Class for controlling the use the Time Slip constraint for a missile or launch vehicle, used with the Close Approach Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessGraphics`
              - Class defining 2D Graphics for Access.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTargetTime`
              - Class for defining Sensor target times in terms of access.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTargetTimesCollection`
              - Collection of access times.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :py:class:`~ansys.stk.core.stkobjects.AdditionalGainLoss`
              - Class defining additional gains and losses.

            * - :py:class:`~ansys.stk.core.stkobjects.AdditionalGainLossCollection`
              - Class defining a collection of additional gains and losses.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCAT`
              - AdvCAT properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATAdvancedEllipsoid`
              - AdvCAT advanced ellipsoid properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATAdvancedSettings`
              - AdvCAT advanced properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATAvailableObjectCollection`
              - Read-only collection of available objects.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATChosenObject`
              - A chosen object.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATChosenObjectCollection`
              - The chosen object collection.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATPreFilters`
              - AdvCAT pre-filters properties.

            * - :py:class:`~ansys.stk.core.stkobjects.Aircraft`
              - Aircraft object.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftExportTools`
              - The Aircraft Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.Antenna`
              - Class defining the antenna object.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeam`
              - Class defining an antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamCollection`
              - Class defining an antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategy`
              - Class defining a beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyAggregate`
              - Class defining a aggregated beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyMaximumGain`
              - Class defining a maximum gain beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyMinimumBoresightAngle`
              - Class defining a minimum boresight angle beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamSelectionStrategyScriptPlugin`
              - Class defining a script plugin beam selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaBeamTransmit`
              - Class defining a transmit antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourEIRP`
              - Class defining an antenna eirp contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourFluxDensity`
              - Class defining an antenna flux density contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourGain`
              - Class defining an antenna gain contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourGraphics`
              - Class defining contour Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourLevel`
              - Class defining an antenna contour level.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourLevelCollection`
              - Class defining a collection of antenna contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourRIP`
              - Class defining an antenna rip contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourSpectralFluxDensity`
              - Class defining an antenna spectral flux density contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaControl`
              - Class defining the properties for a antenna control.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaGraphics`
              - Class defining 2D Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaGraphics3D`
              - Class defining 3D Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModel`
              - Class defining a generic antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelANSYSffdFormat`
              - Class defining an antenna pattern ANSYS ffd model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBessel`
              - Class defining a circular bessel aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularBesselEnvelope`
              - Class defining a circular bessel envelope aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosine`
              - Class defining a circular cosine aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal`
              - Class defining a circular cosine pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosineSquared`
              - Class defining a circular cosine squared aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosineSquaredPedestal`
              - Class defining a circular cosine squared pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularSincIntegerPower`
              - Class defining a circular sinc integer power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularSincRealPower`
              - Class defining a circular sinc real power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularUniform`
              - Class defining a circular uniform aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosine`
              - Class defining a rectangular cosine aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosinePedestal`
              - Class defining a rectangular cosine pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquared`
              - Class defining a rectangular cosine squared aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal`
              - Class defining a rectangular cosine squared pedestal aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularSincIntegerPower`
              - Class defining a rectangular sinc integer power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularSincRealPower`
              - Class defining a rectangular sinc real power aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularUniform`
              - Class defining a rectangular uniform aperture antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelCosecantSquared`
              - Class defining a cosecant squared antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelDipole`
              - Class defining a dipole antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelElevationAzimuthCuts`
              - Class defining a pattern elevation/azimuth cuts antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelExternal`
              - Class defining a external antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGaussian`
              - Class defining a gaussian antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGIMROC`
              - Class defining a GIMROC antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGPSFRPA`
              - Class defining a GPS FRPA antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelGPSGlobal`
              - Class defining a GPS global antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelHelix`
              - Class defining a helix antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelHemispherical`
              - Class defining a hemispherical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelHfssEepArray`
              - Class defining an HFSS EEP array antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelIEEE1979`
              - Class defining a IEEE 1979 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelIntelSat`
              - Class defining a IntelSat antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelIsotropic`
              - Class defining a isotropic antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUBO1213CoPolar`
              - Class defining a ITU-R BO1213 co-polar antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUBO1213CrossPolar`
              - Class defining a ITU-R BO1213 cross-polar antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUF1245`
              - Class defining a ITU-R F1245-3 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS1528R12Circular`
              - Class defining a ITU-R S1528 1.2 circular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS1528R12Rectangular`
              - Class defining a ITU-R S1528 1.2 rectangular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS1528R13`
              - Class defining a ITU-R S1528 1.3 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS465`
              - Class defining a ITU-R S465-6 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS580`
              - Class defining a ITU-R S580-6 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS672Circular`
              - Class defining a ITU-R S672 circular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS672Rectangular`
              - Class defining a ITU-R S672-4 rectangular antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelITUS731`
              - Class defining a ITU-R S731 antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelOpticalGaussian`
              - Class defining a gaussian optical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelOpticalSimple`
              - Class defining a simple optical antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelParabolic`
              - Class defining a parabolic antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelPencilBeam`
              - Class defining a pencil beam antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelPhasedArray`
              - Class defining a phased array antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelRectangularPattern`
              - Class defining a rectangular pattern antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelRemcomUanFormat`
              - Class defining an antenna pattern Remcom uan model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelScriptPlugin`
              - Class defining a script plguin antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelSquareHorn`
              - Class defining a square horn antenna model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelTicraGRASPFormat`
              - Class defining an antenna pattern Ticra GRASP model.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaNoiseTemperature`
              - Class defining antenna noise temperature.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaSystem`
              - Class defining an antenna system.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaVolumeGraphics`
              - Class defining 3D Volume Graphics properties of a Antenna.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaVolumeLevel`
              - Class defining an antenna volume level.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaVolumeLevelCollection`
              - Class defining a collection of antenna volume levels.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTarget`
              - Class defining the AreaTarget object.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTargetCommonTasks`
              - Class defining the Area Target Common class.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTargetGraphics`
              - Class to define the 2D attributes of an AreaTarget.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTargetGraphics3D`
              - Class to define the 3D attributes of an AreaTarget.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTypeEllipse`
              - Class defining the AreaTarget AreaType in terms of MajorAxis, MinorAxis and Bearing.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTypePattern`
              - Class defining coordinates of the AreaTarget AreaType.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaTypePatternCollection`
              - Class defining the list of coordinates of the AreaTarget AreaType.

            * - :py:class:`~ansys.stk.core.stkobjects.Atmosphere`
              - Class defining local atmosphere.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModel`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelCOMPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelITURP676Version13`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelITURP676Version9`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelScriptPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelSimpleSatcom`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelTIREM320`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelTIREM331`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelTIREM550`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModel`
              - Class defining a atmospheric turbulence model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModelConstant`
              - Class defining a constant atmospheric turbulence model.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModelHufnagelValley`
              - Class defining a Hufnagel Valley atmospheric turbulence model.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileAlignmentOffset`
              - Alignment offset for various attitude profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileAviator`
              - The profile used for Aviator aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileConstraintOffset`
              - Constraint offset for various attitude profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileGPS`
              - GPS Attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileSpinAboutSettings`
              - Shared for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileSpinning`
              - Spinning attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesCollection`
              - List of scheduled accesses.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeStandardBasic`
              - Basic attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeStandardOrbit`
              - Standard attitude profile for satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeStandardRoute`
              - Standard attitude profile for aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeStandardTrajectory`
              - Standard attitude profile for launch vehicle or missile.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeTorque`
              - Torque file to use in defining integrated attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.AvailableFeatures`
              - Class is used to check the availability of the features such as Astrogator, etc.

            * - :py:class:`~ansys.stk.core.stkobjects.BasicAzElMask`
              - The Azimuth-Elevation Mask class.

            * - :py:class:`~ansys.stk.core.stkobjects.Beamformer`
              - Class defining a beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerASCIIFile`
              - Class defining a beamformer ascii file.

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

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerMVDR`
              - Class defining a beamformer mvdr.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerRaisedCosine`
              - Class defining a raised cosine tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerRaisedCosineSquared`
              - Class defining a raised cosine squared tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerScript`
              - Class defining a beamformer script plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerTaylor`
              - Class defining a Taylor tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerUniform`
              - Class defining a uniform tapered beamformer.

            * - :py:class:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayer`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~ansys.stk.core.stkobjects.BeerBouguerLambertLawLayerCollection`
              - Class defining collection of Beer-Bouguer-Lamber Law atmosphere layers.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBody`
              - A central body coclass.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBodyCollection`
              - Central body collection coclass.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid`
              - Central body's ellipsoid information.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :py:class:`~ansys.stk.core.stkobjects.CentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :py:class:`~ansys.stk.core.stkobjects.Chain`
              - Chain Class is used to access the methods and properties of the STK Chain Object.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConnection`
              - Class defining Chain connections.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConnectionCollection`
              - Class defining a collection of Chain connections.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConstraints`
              - Chain constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics`
              - 2D graphics properties of a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainOptimalStrandOpts`
              - Class defining Chain optimal strand options.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainTimePeriod`
              - Chain time period options.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationArgumentOfLatitude`
              - Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationEccentricAnomaly`
              - Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationMeanAnomaly`
              - Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationTimePastAscendingNode`
              - Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationTimePastPerigee`
              - Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocationTrueAnomaly`
              - True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalOrientation`
              - Orbit orientation in the Classical (Keplerian) system.

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

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModel`
              - Class defining a clouds and fog fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6`
              - Class defining a clouds and fog Loss ITU-R P.840-6 model.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version7`
              - Class defining a clouds and fog Loss ITU-R P.840-7 model.

            * - :py:class:`~ansys.stk.core.stkobjects.CommRadCartesianLocation`
              - Class defining a location.

            * - :py:class:`~ansys.stk.core.stkobjects.CommRadComplexNumber`
              - Class defining a complex number.

            * - :py:class:`~ansys.stk.core.stkobjects.CommRadComplexNumberCollection`
              - Class defining a collection of complex numbers.

            * - :py:class:`~ansys.stk.core.stkobjects.CommRadPluginConfiguration`
              - Class defining plugin configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystem`
              - Class defining a CommSystem object.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetection`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSamplesOnly`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionSubsample`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessOptions`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethod`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodAdaptive`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodFixed`
              - Class defining a CommSystem access options.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemGraphics`
              - Class defining 2D Graphics properties of a CommSystem.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemGraphics3D`
              - Class defining 3D Graphics properties of a CommSystem.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteria`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaMaximumElevation`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaMinimumRange`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaScriptPlugin`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentAttrLinkEmbedControl`
              - Attribute based component link/embed control.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentDirectory`
              - Manages all components.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentInfo`
              - Class defining a component.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentInfoCollection`
              - The collection of components and component folders.

            * - :py:class:`~ansys.stk.core.stkobjects.Constellation`
              - Class represents the STK Constellation.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraintObjectRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraintRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraints`
              - Class related to the constellation constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationGraphics`
              - 2D Graphics properties of the STK Constellation.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationRouting`
              - Routing properties of the STK Constellation.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAdvancedSettings`
              - Advanced Properties.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection`
              - Collection of Area Targets.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAssetListCollection`
              - Asset List.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAssetListElement`
              - Coverage asset.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsCustomRegions`
              - Custom Regions.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLatitude`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLatitudeLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLatitudeLongitudeRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBoundsLongitudeLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageDefinition`
              - The CoverageDefinition class.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageEllipse`
              - Elliptical area of interest.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageEllipseCollection`
              - Collection of elliptical areas of interest.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics3D`
              - CoverageGraphics3DStatic Class.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGrid`
              - Grid Definition and resolution.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGridInspector`
              - CoverageGridInspector class provides methods to use the grid inspector tool for coverage definition.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGridPointSelection`
              - Represents a set of points selected with the grid inspector.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageLatLonBox`
              - Latitude/longitude box area of interest.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageLatLonBoxCollection`
              - Collection of latitude/longitude boxes of interest.

            * - :py:class:`~ansys.stk.core.stkobjects.CoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoveragePointFileListCollection`
              - Point file list collection.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageRegionFilesCollection`
              - Collection of Region Files.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :py:class:`~ansys.stk.core.stkobjects.CustomPropagationModel`
              - Class defining a custom propatation model.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderCollection`
              - Collection of data providers attached to the current STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderElement`
              - Class defining a data provider element.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderElements`
              - Elements returned by the data provider (e.g. ``x``, ``y``, ``z``).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderFixed`
              - Support for fixed data providers (i.e. non time-dependent like Facility position).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderGroup`
              - Group of sub data providers (e.g. ``Cartesian Position`` on Satellites).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderInterval`
              - Support for interval data providers (e.g. Facility lighting times).

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResult`
              - Results returned by the data provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultDataSet`
              - Represents a dataset in the collection of datasets returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection`
              - Represents a collection of datasets in the interval returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultInterval`
              - Represents a interval in the collection of intervals returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultIntervalCollection`
              - Represents a collection of intervals returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultStatisticResult`
              - Results returned by statistics computation.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultStatistics`
              - Class used to compute statistics and time varying extremum on data provider result data sets.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultSubSection`
              - Represents a subsection in the data returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultSubSectionCollection`
              - Represents a collection of subsections returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage`
              - Notification or failure messages returned by the data provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult`
              - Results returned by time varying extremum computation.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviders`
              - Class defining data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderTimeVarying`
              - Support for time-dependent data providers (e.g. Satellite position).

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayG`
              - Delaunay Variable G, the magnitude of the orbital angular momentum.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayGOverSQRTmu`
              - Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayHOverSQRTmu`
              - Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayL`
              - Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayLOverSQRTmu`
              - Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModel`
              - Class defining a demodulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModel16PSK`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModel8PSK`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelBOC`
              - Class defining a BOC modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelBPSK`
              - Class defining a BPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelDPSK`
              - Class defining a DPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelFSK`
              - Class defining a FSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelMSK`
              - Class defining a MSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelNFSK`
              - Class defining a NFSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelOQPSK`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQAM1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQAM128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQAM16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQAM256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQAM32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQAM64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelQPSK`
              - Class defining a QPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelScriptPlugin`
              - Class defining a script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.DeticSizeAltitude`
              - Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :py:class:`~ansys.stk.core.stkobjects.DeticSizeRadius`
              - Radius and Radius Rate (for Geodetic coordinate type).

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProvider`
              - Class defining a direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderASCIIFile`
              - Class defining an ascii file direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderLink`
              - Class defining an link direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderObject`
              - Class defining an object direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderScript`
              - Class defining an script plugin direction provider.

            * - :py:class:`~ansys.stk.core.stkobjects.DisplayTimesDuringAccess`
              - Class defining display intervals in terms of access to objects.

            * - :py:class:`~ansys.stk.core.stkobjects.DisplayTimesTimeComponent`
              - Provide methods to configure the display times using Timeline API components.

            * - :py:class:`~ansys.stk.core.stkobjects.Element`
              - Class defining a phased array element.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementCollection`
              - Class defining a phased array element collection.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfiguration`
              - Class defining an element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationASCIIFile`
              - Class defining a ascii file element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationCircular`
              - Class defining a circular element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationHexagon`
              - Class defining a hexagon element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationHfssEepFile`
              - Class defining an HFSS EEP file element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationLinear`
              - Class defining a linear element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationPolygon`
              - Class defining a polygon element configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIR`
              - EOIR interface class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRMaterialElement`
              - EOIRMaterialElement class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRMaterialElementCollection`
              - Collection of material elements.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShape`
              - EOIRShape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeBox`
              - Box shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCollection`
              - Collection of shapes.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCone`
              - Cone shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCoupler`
              - Coupler shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCustomMesh`
              - CustomMesh shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeCylinder`
              - Cylinder shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeGEOComm`
              - GEOComm shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeLEOComm`
              - LEOComm shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeLEOImaging`
              - LEOImaging shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeNone`
              - None shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeObject`
              - Represents a generic shape object.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapePlate`
              - Plate shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeSphere`
              - Sphere shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeTargetSignature`
              - TargetSignature shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRStage`
              - Stage base class.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRStagePlume`
              - Plume shape class.

            * - :py:class:`~ansys.stk.core.stkobjects.EquinoctialSizeShapeMeanMotion`
              - Mean Motion, an element of the Equinoctial coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.EquinoctialSizeShapeSemimajorAxis`
              - Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.EventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :py:class:`~ansys.stk.core.stkobjects.EventDetectionSubSampling`
              - Event detection strategy involving subsampling.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolStepSize`
              - ExportToolStepSize Class.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolTimePeriod`
              - Specify Time Period.

            * - :py:class:`~ansys.stk.core.stkobjects.Facility`
              - Class defining the Facility object.

            * - :py:class:`~ansys.stk.core.stkobjects.FacilityGraphics`
              - 2D Graphics properties of a Facility.

            * - :py:class:`~ansys.stk.core.stkobjects.FacilityGraphics3D`
              - 3D Graphics properties of a Facility.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMerit`
              - Figure of Merit properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best 4 satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataMinimumMaximum`
              - Minimum and maximum data values for navigation accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataMinimumNumberOfAssets`
              - Minimum number of assets.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionScalarCalculation`
              - Scalar Calculation Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData`
              - System Age Of Data Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics`
              - FigureOfMeritGraphics Class.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesCollection`
              - Collection of Level Attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGridInspector`
              - FigureOfMeritGridInspector class provides methods to use the grid inspector tool for FOM.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics2DRangeContours`
              - Class defining 2D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DArticulationFile`
              - Class defining the vo articulation file.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DAzElMask`
              - Class to define display labels and adjust the translucency of the 3D azimuth-elevation mask for a facility, place or target.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DBorderWall`
              - Class defining 3D Graphics border wall properties.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection`
              - Collection of 3D Graphics data display text.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayElement`
              - Class defining 3D Graphics data display element.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DDetailThreshold`
              - Class defining detail thresholds as an aid for improving performance when viewing in 3D.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DLabelSwapDistance`
              - Control the level of detail in labels and other screen objects at specified distances.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarker`
              - Class defining the 3D marker to represent an object at a specified threshold.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarkerFile`
              - Class defining 3D marker file attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarkerShape`
              - Class defining the marker type that represents the object in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelArticulation`
              - Class defining 3D model articulations.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelCollection`
              - Collection representing 3D model list.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelFile`
              - Class defining 3D model file.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelglTFImageBased`
              - Class defining glTF Reflection Settings.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelItem`
              - Class defining selection and display of 3D models.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelPointing`
              - List of pointable model elements.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelTransformation`
              - Class to modify transformation values.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection`
              - Collection of available transformations in a model.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffset`
              - Class defining 3D offset attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttachment`
              - Class defining attach points for the attachment of lines to objects.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel`
              - Class defining the offset of the position of an object label in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetRotate`
              - Class defining rotation in the object body frame's X, Y and Z directions.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DOffsetTransformation`
              - Class defining model translation in the object body frame's X, Y and Z directions.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DPointableElementsElement`
              - Pointable elements for 3D model pointing.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DRangeContours`
              - Class defining 3D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceAngle`
              - Class defining a reference angle (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceAxes`
              - Class defining a set of reference axes (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferencePlane`
              - Class defining a reference plane (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferencePoint`
              - Class defining a reference point (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVector`
              - Class defining a reference vector (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection`
              - Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail`
              - Vapor trail attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DVector`
              - Class defining 3D vectors.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicle`
              - Ground vehicle object.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicleExportTools`
              - The GroundVehicle Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.GroundVehicleGraphics3D`
              - GroundVehicleGraphics3DVO Class.

            * - :py:class:`~ansys.stk.core.stkobjects.IntegratorStepSizeControl`
              - Class defining step size control for the HPOP integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.IntegratorTimeRegularization`
              - Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

            * - :py:class:`~ansys.stk.core.stkobjects.IonosphericFadingLossModel`
              - Class defining a Ionospheric fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.IonosphericFadingLossModelP531Version13`
              - Class defining a Ionospheric fading loss P.531-13 model.

            * - :py:class:`~ansys.stk.core.stkobjects.KeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :py:class:`~ansys.stk.core.stkobjects.LabelNote`
              - Class defining label notes.

            * - :py:class:`~ansys.stk.core.stkobjects.LabelNoteCollection`
              - Collection representing label notes list.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModel`
              - Class defining an laser propagation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Class defining an laser propagation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserPropagationLossModels`
              - Class defining the properties for laser propagatoin models.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModel`
              - Class defining an laser tropospheric scintillation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814`
              - Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeCentric`
              - Geocentric LLA position.

            * - :py:class:`~ansys.stk.core.stkobjects.LatitudeLongitudeAltitudeDetic`
              - Geodetic LLA position.

            * - :py:class:`~ansys.stk.core.stkobjects.LatitudeLongitudeAltitudePosition`
              - Class defining position defined in terms of latitude, longitude and altitude (LLA).

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicle`
              - Launch vehicle object.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleControlFixedApogeeAltitude`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed apogee altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleControlFixedDeltaV`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleControlFixedDeltaVMinimumEccentricity`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V with minimum eccentricity.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleControlFixedTimeOfFlight`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed time of flight.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleExportTools`
              - The LaunchVehicle Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleInitialState`
              - Class defining launch vehicle initial state.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleLocationCentric`
              - Class defining geocentric launch latitude, longitude and radius for a Missile or LaunchVehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.LaunchVehicleLocationDetic`
              - Class defining geodetic launch latitude, longitude and altitude for a Missile or LaunchVehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.LevelAttribute`
              - Properties defining display of contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.LevelAttributeCollection`
              - Collection of properties defining display of contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTarget`
              - Line Target Path properties.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetGraphics`
              - The LineTargetGraphics class.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetGraphics3D`
              - The LineTargetGraphics3D class.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetPoint`
              - Line Target Point.

            * - :py:class:`~ansys.stk.core.stkobjects.LineTargetPointCollection`
              - The collection of points for the line target.

            * - :py:class:`~ansys.stk.core.stkobjects.LinkMargin`
              - Class defining a link margin computation object.

            * - :py:class:`~ansys.stk.core.stkobjects.LinkToObject`
              - Class defining a link to an STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.LocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :py:class:`~ansys.stk.core.stkobjects.MilitaryStandard2525bSymbols`
              - MilitaryStandard2525bSymbols class provides methods to create 2525b symbols.

            * - :py:class:`~ansys.stk.core.stkobjects.Missile`
              - Missile object.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileEOIR`
              - MissileEOIR interface class.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileExportTools`
              - The Missile Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileGraphics`
              - 2D Graphics for missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.MissileGraphics3D`
              - 3D Graphics for missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.MixedSphericalFlightPathAngleHorizontal`
              - Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.MixedSphericalFlightPathAngleVertical`
              - Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.MODTRANLookupTablePropagationModel`
              - Class defining an MODTRAN-based lookup table propagation model.

            * - :py:class:`~ansys.stk.core.stkobjects.MODTRANPropagationModel`
              - Class defining a MODTRAN propagation model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModel`
              - Class defining a modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModel16PSK`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModel8PSK`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelBOC`
              - Class defining a BOC modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelBPSK`
              - Class defining a BPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelDPSK`
              - Class defining a DPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelFSK`
              - Class defining a FSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelMSK`
              - Class defining a MSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelNFSK`
              - Class defining a NFSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelOQPSK`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQAM1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQAM128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQAM16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQAM256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQAM32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQAM64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelQPSK`
              - Class defining a QPSK modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelScriptPluginCustomPSD`
              - Class defining a custom PSD script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelScriptPluginIdealPSD`
              - Class defining a ideal PSD script plugin modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~ansys.stk.core.stkobjects.MTO`
              - Multi-Track Object (MTO).

            * - :py:class:`~ansys.stk.core.stkobjects.MTOAnalysis`
              - MTO Spatial State Info.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOAnalysisFieldOfView`
              - MTO Field Of View Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOAnalysisPosition`
              - MTO Position Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOAnalysisRange`
              - MTO Range Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOAnalysisVisibility`
              - MTO Visibility Computation.

            * - :py:class:`~ansys.stk.core.stkobjects.MTODefaultGraphics2DTrack`
              - 2D graphics attributes for default MTO tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MTODefaultGraphics3DTrack`
              - 3D graphics properties for default MTO tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MTODefaultTrack`
              - Default MTO track.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGlobalTrackOptions`
              - Global MTO track options.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics`
              - MTO 2D Graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DFadeTimes`
              - MTO track fade times.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DGlobalTrackOptions`
              - Global 2D graphics options for an MTO.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DLeadTrailTimes`
              - MTO track lead/trail times.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DLine`
              - MTO track line display options.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DMarker`
              - Define the 2D graphics attributes of the selected MTO track or tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DTrack`
              - 2D graphics attributes for each track in the MTO.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3D`
              - MTO 3D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DDropLines`
              - MTO droplines.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DGlobalTrackOptions`
              - Global 3D graphics MTO track options.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DMarker`
              - MTO 3D graphics marker options.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DModel`
              - MTO track model options.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DModelArticulation`
              - Class defining MTO model articulations.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DPoint`
              - MTO track 3D marker point options.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DSwapDistances`
              - MTO track 3D swap distances.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DTrack`
              - 3D graphics properties for MTO tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOTrack`
              - List of MTO tracks with basic information about each.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOTrackCollection`
              - MTO Track List.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOTrackPoint`
              - The points defined for the selected track.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOTrackPointCollection`
              - MTO track point list.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectCoverage`
              - Class defining object coverage.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectCoverageFigureOfMerit`
              - Class defining the fom on the coverage object tool.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectLaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectLink`
              - Class defining name of an STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectLinkCollection`
              - Collection of names of STK objects that are available in the current Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ObjectRFEnvironment`
              - Class defining the RF environment for an object.

            * - :py:class:`~ansys.stk.core.stkobjects.OceanTides`
              - Class defining the contribution of ocean tides.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccess`
              - One Point Access.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessConstraint`
              - One Point Access Result.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessResult`
              - One Point Access Result.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitState`
              - Class defining orbit state.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateCartesian`
              - Cartesian coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateCoordinateSystem`
              - Selection of coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateDetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.OrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :py:class:`~ansys.stk.core.stkobjects.OrientationLongitudeOfAscending`
              - Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :py:class:`~ansys.stk.core.stkobjects.OrientationRightAscensionOfAscendingNode`
              - Angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :py:class:`~ansys.stk.core.stkobjects.PassBreak`
              - Satellite Pass Break properties.

            * - :py:class:`~ansys.stk.core.stkobjects.PassBreakNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :py:class:`~ansys.stk.core.stkobjects.PassBreakNumberingFirstPassNumber`
              - First pass number.

            * - :py:class:`~ansys.stk.core.stkobjects.PathCollection`
              - Allow adding and removing of paths.

            * - :py:class:`~ansys.stk.core.stkobjects.Place`
              - Class defining the Place object.

            * - :py:class:`~ansys.stk.core.stkobjects.PlaceGraphics`
              - 2D Graphics properties of a Place.

            * - :py:class:`~ansys.stk.core.stkobjects.PlaceGraphics3D`
              - 3D Graphics properties of a Place.

            * - :py:class:`~ansys.stk.core.stkobjects.Planet`
              - Class defining the Planet object.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetCommonTasks`
              - Class defining the Planet Common class.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetGraphics`
              - Class defining 2D Graphics properties of a Planet.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetGraphics3D`
              - Class defining 3D Graphics properties of a Planet.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetOrbitDisplayTime`
              - Class defining display time of a planet's orbit.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetPositionCentralBody`
              - Class defining central body used to define Planet object.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetPositionFile`
              - Class defining the planetary ephemeris file.

            * - :py:class:`~ansys.stk.core.stkobjects.PlatformLaserEnvironment`
              - Class defining the laser environment for an platform.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategy`
              - Class defining a pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategyFixed`
              - Class defining a fixed pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategySpinning`
              - Class defining a spinning pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategyTargeted`
              - Class defining a targeted pointing strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.PointTargetGraphics3DModel`
              - Point properties for a 3D model.

            * - :py:class:`~ansys.stk.core.stkobjects.Polarization`
              - Class defining an polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationLeftHandCircular`
              - Class defining a LHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationRightHandCircular`
              - Class defining a RHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationVertical`
              - Class defining a vertical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.Preferences`
              - Allow configuring STK preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.PreferencesConnect`
              - Allow configuring connect preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.PreferencesPythonPlugins`
              - Allow configuring Python plugin preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.PreferencesVDF`
              - Allow configuring VDF preferences.

            * - :py:class:`~ansys.stk.core.stkobjects.Priority`
              - Class defining a target priority.

            * - :py:class:`~ansys.stk.core.stkobjects.PriorityCollection`
              - Class defining a priority data collection.

            * - :py:class:`~ansys.stk.core.stkobjects.ProgressBarEventArguments`
              - Represents a structure used by the Percent Complete events.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagationChannel`
              - Class defining the propagation channel.

            * - :py:class:`~ansys.stk.core.stkobjects.Propagator11Parameters`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :py:class:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptor`
              - 11-Param file definition.

            * - :py:class:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorAviator`
              - Class defining the Mission Modler propagator for an Aircraft.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorBallistic`
              - Class defining the ballistic propagator for a Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorDefinitionExportTool`
              - PropagatorDefinitionExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorGPS`
              - GPS propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorGreatArc`
              - Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorHPOP`
              - Class defining the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorHPOPStaticForceModelSettings`
              - Class defining static force model options for the HPOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityCollection`
              - Collection of third-body gravity options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement`
              - Class defining third-body gravity options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation`
              - Class defining the J2 perturbation propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorJ4Perturbation`
              - Class defining the J4 perturbation propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorLOP`
              - Class defining the Long-term Orbit Predictor (LOP).

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorLOPThirdBodyGravity`
              - Third body gravity options for Long-range Orbit Predictor (LOP) propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorRealtime`
              - Realtime propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorRealtimeCartesianPoints`
              - PropagatorRealtimeCartesianPoints Class.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorRealtimeDeticPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorRealtimeHeadingPitch`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4`
              - Class defining the SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdate`
              - SGP4 AutoUpdate.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdateFileSource`
              - Configure the SGP4 automatic updates using file(s).

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdateOnlineSource`
              - Configure the SGP4 automatic updates using online source (AGI server).

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4AutoUpdateProperties`
              - SGP4 AutoUpdate properties.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4CommonTasks`
              - Most commonly used functionality when working with SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4LoadFile`
              - SGP4 propagator. Allows the user to load segments from file.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineAutoLoad`
              - Do not use this class, as it is deprecated. Use PropagatorSGP4OnlineLoad instead. SGP4 propagator. Allows the user to load the most current segment from online.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4OnlineLoad`
              - SGP4 propagator. Allows the user to load segments from online.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4Segment`
              - SGP4 propagator segment.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4SegmentCollection`
              - Set of Trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSimpleAscent`
              - Class defining the simple ascent propagator for a launch vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSP3File`
              - SP3 file data.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSPICE`
              - Class defining the SPICE propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSPICESegment`
              - SPICE propagator segment.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSPICESegmentsCollection`
              - Collection of segments for a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSTKExternal`
              - Class defining the STK External propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorTwoBody`
              - Class defining the two body propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorUserExternal`
              - Class defining the user-external propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.Radar`
              - Class defining the radar object.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarAccessGraphics`
              - Class defining access graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivity`
              - Class defining radar activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityAlwaysActive`
              - Class defining radar always active activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityAlwaysInactive`
              - Class defining radar always active inactivity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeComponentList`
              - Class defining a radar time component list activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeComponentListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeComponentListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalList`
              - Class defining a radar time component list activity.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityTimeIntervalListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarAntennaBeam`
              - Class defining a radar antenna beam.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarAntennaBeamCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarClutter`
              - Class defining a radar clutter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarClutterGeometry`
              - Class defining a radar clutter geometry.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarContinuousWaveAnalysisModeFixedTime`
              - Class defining the continuous wave fixed time analysis mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarContinuousWaveAnalysisModeGoalSNR`
              - Class defining the continuous wave goal SNR analysis mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSection`
              - Class defining a radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategy`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyAnsysCSVFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyConstantValue`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyExternalFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionComputeStrategyScriptPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionContourLevel`
              - Class defining an radar cross section contour level.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionContourLevelCollection`
              - Class defining a collection of radar cross section contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand`
              - Class defining a inheritable radar cross section frequency band.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBandCollection`
              - Class defining a inheritable radar cross section frequency band collection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics`
              - Class defining graphics properties of radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionGraphics3D`
              - Class defining 3D Graphics properties of radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionInheritable`
              - Class defining a inheritable radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionModel`
              - Class defining a radar cross section model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeGraphics`
              - Class defining 3D Volume Graphics properties of radar cross section.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeLevel`
              - Class defining an radar cross section volume level.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionVolumeLevelCollection`
              - Class defining a collection of radar cross section volume levels.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarDopplerClutterFilters`
              - Class defining the properties for doppler clutter filters.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarGraphics`
              - Class defining 2D Graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarGraphics3D`
              - Class defining 3D Graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarJamming`
              - Class defining radar jamming.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiver`
              - Class defining a bistatic receiver radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSAR`
              - Class defining a bistatic receiver sar radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticReceiverSearchTrack`
              - Class defining a bistatic receiver search/track radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitter`
              - Class defining a bistatic transmitter radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSAR`
              - Class defining a bistatic transmitter sar radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeBistaticTransmitterSearchTrack`
              - Class defining a bistatic transmitter search/track radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModel`
              - Class defining a generic radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelBistaticReceiver`
              - Class defining a bistatic receiver radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelBistaticTransmitter`
              - Class defining a bistatic transmitter radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelMonostatic`
              - Class defining a monostatic radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelMultifunction`
              - Class defining a multifunction radar model.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeMonostatic`
              - Class defining a monostatic radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeMonostaticSAR`
              - Class defining a monostatic sar radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModeMonostaticSearchTrack`
              - Class defining a monostatic search/track radar mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModulator`
              - Class defining a radar modulator.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMultifunctionDetectionProcessing`
              - Class defining multifunction radar detection processing.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMultifunctionWaveformStrategySettings`
              - Class defining the waveform selection strategy settings.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMultipathGraphics`
              - Class defining multipath graphics properties of a Radar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetection`
              - Class defining the probability of detection.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionCFAR`
              - Class defining the probability of detection cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionCFARCellAveraging`
              - Class defining the probability of detection cell averaging cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionCFAROrderedStatistics`
              - Class defining the probability of detection ordered statistics cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionNonCFAR`
              - Class defining the non CFAR probability of detection cfar.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionPlugin`
              - Class defining the probability of detection plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarPulseIntegrationFixedNumberOfPulses`
              - Class defining the fixed number of pulses integration method.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarPulseIntegrationGoalSNR`
              - Class defining the goal SNR integration method.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarReceiver`
              - Class defining the radar transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuation`
              - Class defining an radar stc.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationDecayFactor`
              - Class defining an radar decay factor stc.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationDecaySlope`
              - Class defining an radar decay slope stc.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationMapAzimuthRange`
              - Class defining an radar stc azimuth-range map.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationMapElevationRange`
              - Class defining an radar stc elevation-range map.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationMapRange`
              - Class defining an radar stc range map.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationPlugin`
              - Class defining an radar stc Com Plugin.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarTransmitter`
              - Class defining the radar transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarTransmitterMultifunction`
              - Class defining the multifunction radar transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackContinuous`
              - Class defining a bistatic receiver continuous waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Class defining a bistatic receiver fixed PRF waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Class defining a bistatic transmitter continuous waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Class defining a bistatic transmitter fixed PRF waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackContinuous`
              - Class defining a monostatic continuous waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformMonostaticSearchTrackFixedPRF`
              - Class defining a monostatic fixed PRF waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseDefinition`
              - Class defining the pulse definition for a SAR waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSarPulseIntegration`
              - Class defining the pulse integration for a SAR waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSearchTrackPulseDefinition`
              - Class defining the pulse definition for a search track waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.RadiationPressure`
              - Class defining solar radiation pressure on a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModel`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelCCIR1983`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelCrane1982`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelCrane1985`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelITURP618Version10`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelITURP618Version12`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelITURP618Version13`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelScriptPlugin`
              - Class defining a rain loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationLeftHandCircular`
              - Class defining a LHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationRightHandCircular`
              - Class defining a RHC polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceivePolarizationVertical`
              - Class defining a receive vertical polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.Receiver`
              - Class defining the receiver object.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverGraphics`
              - Class defining 2D Graphics properties of a Receiver.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverGraphics3D`
              - Class defining 3D Graphics properties of a Receiver.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModel`
              - Class defining a generic receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelCable`
              - Class defining a cable receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelComplex`
              - Class defining a complex receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelLaser`
              - Class defining a laser receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelMedium`
              - Class defining a medium receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelMultibeam`
              - Class defining a mutibeam receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelScriptPluginLaser`
              - Class defining a laser script plugin receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelScriptPluginRF`
              - Class defining a RF script plugin receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelSimple`
              - Class defining a simple receiver model.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :py:class:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod`
              - SCF Method.

            * - :py:class:`~ansys.stk.core.stkobjects.RepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterModelComplex`
              - Class defining a complex re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterModelMedium`
              - Class defining a medium re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterModelSimple`
              - Class defining a simple re-transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFEnvironment`
              - Class defining the RF environment.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModel`
              - Class defining a generic RF filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelBessel`
              - Class defining a bessel filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelButterworth`
              - Class defining a butterworth filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelChebyshev`
              - Class defining a Chebyshev filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelCosineWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelElliptic`
              - Class defining a elliptic filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelExternal`
              - Class defining a external filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelFIR`
              - Class defining a FIR filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelFIRBoxCar`
              - Class defining a FIR box car filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelGaussianWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelHammingWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelIIR`
              - Class defining a IIR box car filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRaisedCosine`
              - Class defining a raised cosine filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRCLowPass`
              - Class defining a rc low pass filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRectangular`
              - Class defining a rectangular filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelRootRaisedCosine`
              - Class defining a root raised cosine filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelScriptPlugin`
              - Class defining a script plugin filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelSinc`
              - Class defining a sinc filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelSincEnvelopeSinc`
              - Class defining a Sinc Envelope Sinc filter model.

            * - :py:class:`~ansys.stk.core.stkobjects.RFInterference`
              - Class defining radar jamming.

            * - :py:class:`~ansys.stk.core.stkobjects.RotationRateAndOffset`
              - RotationRateAndOffset Class.

            * - :py:class:`~ansys.stk.core.stkobjects.SamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :py:class:`~ansys.stk.core.stkobjects.SamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :py:class:`~ansys.stk.core.stkobjects.Satellite`
              - Satellite properties.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteCollection`
              - The SatelliteCollection class.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteExportTools`
              - The Satellite Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.SatelliteGraphics3DModel`
              - All Satellite's VO Model properties.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointCollection`
              - Class defining a collection of scattering points.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointCollectionElement`
              - Class defining a scattering point collection element.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModel`
              - Class defining a scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelConstantCoefficient`
              - Class defining a constant coefficient scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelPlugin`
              - Class defining a plugin scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelWindTurbine`
              - Class defining a wind turbine scattering point model.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProvider`
              - Class defining a scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection`
              - Class defining an scattering point provider collection.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollectionElement`
              - Class defining a scattering point provider collection element.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderList`
              - Class defining a scattering point provider list.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderPlugin`
              - Class defining a plugin scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile`
              - Class defining a scattring point provider where the points are defined in an ascii text file.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderRangeOverCFARCells`
              - Class defining a range over CFAR cells scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderSinglePoint`
              - Class defining a single point scattring point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderSmoothOblateEarth`
              - Class defining a smooth oblate earth scattering point provider.

            * - :py:class:`~ansys.stk.core.stkobjects.Scenario`
              - Class defining the Scenario object.

            * - :py:class:`~ansys.stk.core.stkobjects.Scenario3dFont`
              - Font properties for Scenario 3D Graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioAnimation`
              - Class defining the animation properties of a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioAnimationTimePeriod`
              - Configure the scenario's animation time.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioBeforeSaveEventArguments`
              - Contains information about the changes in the object's state.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioDatabase`
              - Class defining database settings of the Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioDatabaseCollection`
              - Collection of Scenario database settings.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioEarthData`
              - Class defining the Earth Orientation Parameters of a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioGraphics`
              - Class defining the 2D Graphics properties of a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioGraphics3D`
              - Class defining 3D Graphics properties of the Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~ansys.stk.core.stkobjects.ScheduleTime`
              - Class for defining Sensor target times in terms of a specified schedule.

            * - :py:class:`~ansys.stk.core.stkobjects.ScheduleTimeCollection`
              - Collection of user-scheduled access times.

            * - :py:class:`~ansys.stk.core.stkobjects.Sensor`
              - Class defining the Sensor class.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAccessAdvancedSettings`
              - Sensor's advanced targeting access computation properties.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAzElMaskFile`
              - Class to define a Sensor's Azimuth-Elevation mask.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorCommonTasks`
              - Class defining the Sensor Common class.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorComplexConicPattern`
              - Class defining the complex conic pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorCustomPattern`
              - Class defining the custom pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBand`
              - Class defining an EOIR band.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandCollection`
              - Class defining the band collection for an EOIR Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRPattern`
              - Class defining the EOIR pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRRadiometricPair`
              - Class defining an Sensitivities item.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRSaturationCollection`
              - Class defining the Saturations collection for an EOIR Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRSensitivityCollection`
              - Class defining the Sensitivities collection for an EOIR Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics`
              - Class defining the 2D Graphics properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3D`
              - Class defining 3D Graphics properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset`
              - Class defining 3D Graphics vertex offset properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DPulse`
              - Class defining 3D pulse properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorHalfPowerPattern`
              - Class defining the half-power pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointing3DModel`
              - Class defining the 3D model pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingAlongVector`
              - Class defining the along vector pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingExternal`
              - Class defining the external file-defined pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingFixed`
              - Class defining the fixed pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingFixedInAxes`
              - Class defining the fixed in axes pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingGrazingAltitude`
              - Class defining Grazing Altitude pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingSchedule`
              - Allow to schedule a sensor to point at a specific location at a specific time.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingSpinning`
              - Class defining the spinning pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargeted`
              - Class defining the targeted pointing type for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightFixed`
              - Class defining a targeted Sensor with fixed boresight.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightTrack`
              - Class defining a targeted sensor with tracking boresight.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjection`
              - Class defining the projection properties of a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionConstantAltitude`
              - Class defining projection altitude options for constant altitude for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionDisplayDistance`
              - Class defining projection altitude options for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionObjectAltitude`
              - Class defining projection altitude options for object altitude for a sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorRectangularPattern`
              - Class defining the rectangular pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorSARPattern`
              - Class defining the Synthetic Aperture Radar (SAR) pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorSimpleConicPattern`
              - Class defining the simple conic pattern for a Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorTarget`
              - Class defining a Sensor target.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorTargetCollection`
              - Class defining the target collection for a target-pointing Sensor.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorUnknownPattern`
              - Unsupported/unknown sensor pattern.

            * - :py:class:`~ansys.stk.core.stkobjects.Ship`
              - Ship object.

            * - :py:class:`~ansys.stk.core.stkobjects.ShipExportTools`
              - The Ship Export Tools.

            * - :py:class:`~ansys.stk.core.stkobjects.ShipGraphics`
              - 2D Graphics options for a ship.

            * - :py:class:`~ansys.stk.core.stkobjects.ShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarActivityConfiguration`
              - Class defining a solar activity configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarActivityConfigurationSolarFlux`
              - Class defining the solar flux configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarActivityConfigurationSunspotNumber`
              - Class defining sunspot number configuration.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticFileSettings`
              - Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarFluxGeoMagneticValueSettings`
              - Class defining the option to enter a vehicle's solar flux and/or GeoMag properties manually, depending on the selected atmospheric density model.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarRadiationPressureModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarRadiationPressureModelPlugin`
              - Plugin Light Reflection Model.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarRadiationPressureModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarRadiationPressureModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :py:class:`~ansys.stk.core.stkobjects.SolidTides`
              - Class defining the contribution of solid tides.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentGraphics`
              - Graphics settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagneticField`
              - Magnetic field settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldGraphics2D`
              - Geomagnetic field graphics settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for displaying magnetic field lines.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentParticleFlux`
              - Particle Flux settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiation`
              - Radiation model settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection`
              - Collection of dose rate elements computed for a shielding thickness.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateElement`
              - Class defining dose rate information computed for a shielding thickness.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnergyMethodEnergies`
              - Set the electron and proton energies to consider.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnergyValues`
              - Energy values used by the Radiation Environment model.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationEnvironment`
              - Radiation Environment model settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentSAAContour`
              - SAA settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentScenarioGraphics3D`
              - 3D Graphics settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentVehicleTemperature`
              - Vehicle Temperature settings.

            * - :py:class:`~ansys.stk.core.stkobjects.SpatialState`
              - Represents a position and an attitude of an object.

            * - :py:class:`~ansys.stk.core.stkobjects.SphericalFlightPathAngleHorizontal`
              - Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.SphericalFlightPathAngleVertical`
              - Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.Star`
              - Class defining the Star object.

            * - :py:class:`~ansys.stk.core.stkobjects.StarCollection`
              - Represents a collection of stars.

            * - :py:class:`~ansys.stk.core.stkobjects.StarGraphics`
              - Class defining 2D Graphics properties of a Star.

            * - :py:class:`~ansys.stk.core.stkobjects.StarGraphics3D`
              - Class defining 3D Graphics properties of a Star.

            * - :py:class:`~ansys.stk.core.stkobjects.StarInformation`
              - Represents a celestial body information.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObject`
              - Represents a generic STK object.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObjectChangedEventArguments`
              - Contains information about the changes in the object's state.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObjectCutCopyPasteEventArguments`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObjectModelContext`
              - STKObjectModelContext class provides methods to create instance of STKObjectRoot class.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObjectPreDeleteEventArguments`
              - Arguments for the OnStkObjectPreDelete event.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObjectRoot`
              - Top-level object in the Object Model Hierarchy.

            * - :py:class:`~ansys.stk.core.stkobjects.Subset`
              - The Subset class.

            * - :py:class:`~ansys.stk.core.stkobjects.Swath`
              - Class defining Swath properties.

            * - :py:class:`~ansys.stk.core.stkobjects.SystemNoiseTemperature`
              - Class defining system noise temperature.

            * - :py:class:`~ansys.stk.core.stkobjects.Target`
              - Class defining the Target object.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetGraphics`
              - Class defining 2D Graphics for a Target object.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetGraphics3D`
              - Class defining 3D Graphics for a Target object.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetSelectionMethod`
              - Class defining a target selection method.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetSelectionMethodClosingVelocity`
              - Class defining a closing velocity-based target selection method.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetSelectionMethodPriority`
              - Class defining a priority-based target selection method.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetSelectionMethodRange`
              - Class defining a range-based target selection method.

            * - :py:class:`~ansys.stk.core.stkobjects.Terrain`
              - Class defining terrain data for a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.TerrainCollection`
              - Collection of terrain data files available in the Scenario for visualization and analysis.

            * - :py:class:`~ansys.stk.core.stkobjects.TerrainNormalSlopeAzimuth`
              - Class defining Slope/Azimuth data for the TerrainNormal.

            * - :py:class:`~ansys.stk.core.stkobjects.Tileset3D`
              - Class defining Analytical 3DTileset for a Scenario.

            * - :py:class:`~ansys.stk.core.stkobjects.Tileset3DCollection`
              - Collection of 3DTilesets available in the Scenario for analysis.

            * - :py:class:`~ansys.stk.core.stkobjects.TimeIntervalCollection`
              - Class defining display intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.TimeIntervalCollectionReadOnly`
              - Read-only collection of intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.TimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~ansys.stk.core.stkobjects.TimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTable`
              - Class defining an input back off vs output back off table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffOutputBackOffTableRow`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTable`
              - Class defining an input back off vs C/Im table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionInputBackOffVsCOverImTableRow`
              - Class defining a row of an input back off vs C/Im table.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionPolynomialCollection`
              - Class defining a collection of polynomial coefficients.

            * - :py:class:`~ansys.stk.core.stkobjects.Transmitter`
              - Class defining the transmitter object.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterGraphics`
              - Class defining 2D Graphics properties of a Transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterGraphics3D`
              - Class defining 3D Graphics properties of a Transmitter.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModel`
              - Class defining a generic transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelCable`
              - Class defining a cable transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelComplex`
              - Class defining a complex transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelLaser`
              - Class defining a laser transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelMedium`
              - Class defining a medium transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelMultibeam`
              - Class defining a multibeam transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelScriptPluginLaser`
              - Class defining a laser script plugin transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelScriptPluginRF`
              - Class defining a RF script plugin transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelSimple`
              - Class defining a simple transmitter model.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModel`
              - Class defining a tropospheric scintillation fading loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12`
              - Class defining a tropospheric scintillation fading loss P.618-12 model.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version8`
              - Class defining a tropospheric scintillation fading loss P.618-8 model.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModel`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModelTwoRay`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModelWirelessInSite64`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAccessAdvancedSettings`
              - Vehicle advanced targeting access computation properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool`
              - VehicleAttitudeExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeExternal`
              - External attitude (.a) file.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTime`
              - Real time attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference`
              - Reference attitude profile for the incoming attitude data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeSlewFixedRate`
              - Fixed rate slew.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeSlewFixedTime`
              - Fixed time slew.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitudeTrendingControlAviator`
              - Trending controls for Aviator attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCentralBodies`
              - Satellite Central Bodies.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollection`
              - The Consider Analysis list for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCoordinateAxesCustom`
              - Custom.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCorrelationListCollection`
              - Collection representing HPOP covariance matrix.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCorrelationListElement`
              - Class representing an element of an HPOP covariance matrix.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCovariance`
              - Class defining HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleDefinition`
              - Pass break definition properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleDuration`
              - Look ahead and look behind duration options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEclipseBodies`
              - Satellite Eclipse Bodies, for defining the eclipse central body list used for lighting computations.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEclipsingBodies`
              - Eclipsing bodies.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEllipseDataElement`
              - Ground ellipse data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEOIR`
              - VehicleEOIR interface class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool`
              - VehicleEphemerisBinaryExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool`
              - VehicleEphemerisCCSDSExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSv2ExportTool`
              - The Ephemeris/Attitude Export Tool for CCSDSv2 Ephemeris type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool`
              - VehicleEphemerisCode500ExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisExportTool`
              - VehicleEphemerisExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEphemerisSPICEExportTool`
              - VehicleEphemerisSPICEExportTool Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleExponentialDensityModelParameters`
              - Class defining the Exponential atmospheric density model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacProperties`
              - A common base for GPS almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdate`
              - GPS AutoUpdate.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateFileSource`
              - GPS automatic updates using almanac file(s).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateOnlineSource`
              - GPS automatic updates using online source (AGI server).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutoUpdateProperties`
              - GPS AutoUpdate properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSElement`
              - An element of the GPS element collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSSpecifyAlmanac`
              - Specify a GPS almanac.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationContours`
              - General settings regarding display of elevation contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationGroundElevation`
              - Ground elevation for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationSwathHalfWidth`
              - Half width for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadDataFraction`
              - 2D Graphics pass: fraction of leading portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadDataTime`
              - 2D Graphics pass: time-defined segment of leading portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLighting`
              - Lighting.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DOrbitPassData`
              - VehicleGraphics2DOrbitPassData Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPasses`
              - Settings for satellite pass display graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath`
              - Vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrailDataFraction`
              - 2D Graphics pass: fraction of trailing portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrailDataTime`
              - 2D Graphics pass: time-defined segment of trailing portion of vehicle track to display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesBasic`
              - Basic 3D graphics for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributesIntervals`
              - 3D graphics based on intervals for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstance`
              - An element in the VehicleGraphics3DBPlanePointCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanePointCollection`
              - VehicleGraphics3DBPlanePointCollection Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplate`
              - An element of VehicleGraphics3DBPlaneTemplatesCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of VehicleGraphics3DBPlaneTemplateDisplayCollection.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance`
              - 3D position covariance ellipsoids.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour`
              - Covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDataFraction`
              - Fraction for 3D track display.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDataTime`
              - Time.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItem`
              - Drop lines at intervals along the vehicle's path.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection`
              - Collection of drop lines from the vehicle's orbit or trajectory.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePositionItem`
              - Drop lines from the vehicle's current position.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DElevationContours`
              - 3D elevation angle contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DGeoBox`
              - Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsCollection`
              - List of Intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DIntervalsElement`
              - Intervals graphics for covariance pointing contour.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData`
              - LaunchVehicleGraphics3DTrajectory2 Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelRoute`
              - 3D marker for great arc vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DModelTrajectory`
              - Marker for launch vehicle or missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitDropLines`
              - Droplines collections.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitPassData`
              - Satellite 3D ground and orbit track data.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitProximity`
              - Proximity graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTickMarks`
              - Tick mark for satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DOrbitTrackData`
              - 3D leading/trailing track data for satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DPass`
              - 3D pass for satellites.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks`
              - Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DRoute`
              - VehicleGraphics3DRoute2 Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DRouteDropLines`
              - Droplines for great arc vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DRouteProximity`
              - Proximity graphics for GreatArc Vehicles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSAA`
              - 3D South Atlantic Anomaly contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSigmaScaleProbability`
              - Sigma probability for indirect sizing of covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSigmaScaleScale`
              - Sigma scale for direct sizing of covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSize`
              - 3D graphics vector size.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTickDataLine`
              - Line type tick marks.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTickDataPoint`
              - Point type tick mark.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectory`
              - LaunchVehicleGraphics3DTrajectory Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryDropLines`
              - Droplines for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryPassData`
              - 3D ground track and trajectory data for a launch vehicle or missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryProximity`
              - VehicleGraphics3DTrajectoryProximity Class.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DTrajectoryTrackData`
              - 3D leading/trailing track data for launch vehicles and missiles.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance`
              - 3D velocity covariance ellipsoids.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersCollection`
              - Collection of Waypoint Markers .

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGravity`
              - Class defining gravity modeling options for a vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGroundEllipseElement`
              - Ground ellipse.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGroundEllipsesCollection`
              - List of Ground Ellipses.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPCentralBodyGravity`
              - Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModel`
              - HPOP Drag Model Base CoClass.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPDragModelSpherical`
              - Spherical Drag Pressure Model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel`
              - Class defining HPOP force models.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDrag`
              - Class defining the HPOP atmospheric drag model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelDragOptions`
              - Class defining HPOP atmospheric drag options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPForceModelMoreOptions`
              - Class defining additional force model options for HPOP.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressure`
              - Class defining HPOP solar radiation pressure properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureModel`
              - SRP Model Base CoClass.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleHPOPSolarRadiationPressureOptions`
              - Class defining HPOP solar radiation pressure options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocationCentric`
              - Class defining geocentric impact latitude, longitude and radius for a Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocationDetic`
              - Class defining geodetic impact latitude, longitude and altitude for a Missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl`
              - Class defining the option to use azimuth and elevation to specify the Missile's impact location.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocationPoint`
              - Class defining a Missile's impact location.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInertia`
              - Satellite inertia matrix parameters.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInitialState`
              - Class defining the initial state of the vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleIntegratedAttitude`
              - Integrated Attitude generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleIntegrator`
              - Class defining the HPOP integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInterpolation`
              - Class defining interpolation for the HPOP integrator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPCentralBodyGravity`
              - Class defining gravity options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPDragSettings`
              - Class defining advanced atmospheric density options for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPForceModel`
              - Class defining the force model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPForceModelDrag`
              - Class defining the atmospheric drag model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLOPSolarRadiationPressure`
              - Class defining the solar radiation pressure model for the LOP propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleMassProperties`
              - Satellite Mass properties.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePhysicalData`
              - Class defining physical data for the LOP force model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePluginPropagator`
              - Class defining a propagator plugin for HPOP for customization of the accelerations used in the propagation of the satellite trajectory.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePluginSettings`
              - Class defining force model plugin settings for HPOP.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePositionVelocityCollection`
              - Collection of position and velocity elements for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePositionVelocityElement`
              - Class defining position and velocity elements for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpatialInformation`
              - Represents a spatial information of the vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetPointingCollection`
              - List of Attitude Targets.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleVector`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointAltitudeReference`
              - Altitude references.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain`
              - Terrain altitude reference.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointsCollection`
              - Collection of waypoints for a Great Arc vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointsElement`
              - Class defining a waypoint for a Great Arc vehicle.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleZonalPropagatorInitialState`
              - Class defining initial state for the J2/4 propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.Volumetric`
              - The Volumetric class.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricAdvancedSettings`
              - Class defining the volumetric Computed Data Save options.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricAnalysisInterval`
              - Class defining the volumetric analysis interval.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricExportTool`
              - The Volumetric Export Tool.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricExternalFile`
              - Class defining the volume external file.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3D`
              - Class defining 3D graphics properties of volumetric object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DActiveGridPoints`
              - Class defining Active Grid Points for Volumetric Object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSection`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlane`
              - Class defining cross-section plane for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection`
              - Class defining collection of cross-section planes for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DGrid`
              - Class defining grid properties of 3D graphics for volumetric object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DLegend`
              - Class defining Boundary/Fill legend for volumetric object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevel`
              - Class defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection`
              - Class defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevels`
              - Class defining Spatial Calculation Levels for Volumetric Object.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGraphics3DVolume`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricGridSpatialCalculation`
              - Class defining the volume grid spatial calculation.

            * - :py:class:`~ansys.stk.core.stkobjects.Waveform`
              - Class defining a waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformPulseDefinition`
              - Class defining the pulse definition for a rectangular waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformRectangular`
              - Class defining a rectangular waveform.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategy`
              - Class defining the waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategyFixed`
              - Class defining the waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategyRangeLimits`
              - Class defining the range limits waveform selection strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.WirelessInSite64GeometryData`
              - Class defining the REMCOM Wireless InSite 64 geometry data.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkobjects.AberrationType`
              - The model of aberration to be used in access computations.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessConstraintType`
              - Available Access Constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AccessTimeType`
              - The time period to use for the access computation.

            * - :py:class:`~ansys.stk.core.stkobjects.ActionType`
              - Specify the action type for the Interval Access Constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATConjunctionType`
              - Mode for computing events involving conjunction TCA.

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATEllipsoidClassType`
              - Method for determining Ellipsoid Sizing method (class).

            * - :py:class:`~ansys.stk.core.stkobjects.AdvCATSecondaryEllipsoidsVisibilityType`
              - Type of visible Secondary Ellipsoids.

            * - :py:class:`~ansys.stk.core.stkobjects.AircraftWGS84WarningType`
              - Display mode options for aircraft mission modeler WGS84 warning.

            * - :py:class:`~ansys.stk.core.stkobjects.AltitudeReferenceType`
              - Altitude reference options.

            * - :py:class:`~ansys.stk.core.stkobjects.AnalysisWorkbenchAccessConstraintType`
              - Available Analysis Workbench Access Constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.AnimationActionType`
              - Animation action options.

            * - :py:class:`~ansys.stk.core.stkobjects.AnimationDirectionType`
              - Animation direction options.

            * - :py:class:`~ansys.stk.core.stkobjects.AnimationEndTimeMode`
              - Animation modes.

            * - :py:class:`~ansys.stk.core.stkobjects.AnimationOptionType`
              - Animation Options.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaContourType`
              - Antenna contour types.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaControlReferenceType`
              - Antenna control reference type.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaGraphicsCoordinateSystem`
              - Coordinate system for defining antenna graphics resolution.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelCosecantSquaredSidelobeType`
              - Cosecant Squared antenna sidelobe selection types.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelInputType`
              - Diameter computation input type.

            * - :py:class:`~ansys.stk.core.stkobjects.AntennaModelType`
              - Antenna model types.

            * - :py:class:`~ansys.stk.core.stkobjects.AreaType`
              - Methods of defining the area target's boundaries.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelType`
              - Atmospheric absorption model types.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericDensityModel`
              - Atmospheric density models.

            * - :py:class:`~ansys.stk.core.stkobjects.AtmosphericTurbulenceModelType`
              - Refractive index structure parameter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeCoordinateAxes`
              - Attitude export options.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeInclude`
              - Details to include in an exported Attitude file.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeProfile`
              - Predefined attitude profiles.

            * - :py:class:`~ansys.stk.core.stkobjects.AttitudeStandardType`
              - AttitudeStandardType tells the user which interface to cast to. eRouteAttitudeStandard -> AttitudeStandardRoute, eTrajectoryAttitudeStandard -> AttitudeStandardTrajectory, eOrbitAttitudeStanard -> AttitudeStandardOrbit.

            * - :py:class:`~ansys.stk.core.stkobjects.AxisOffset`
              - Specify the axis offset for the sensor 3D Vertex Offset.

            * - :py:class:`~ansys.stk.core.stkobjects.AzElMaskType`
              - Obscura types of the facility, place or target for AzElMask definition.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamformerType`
              - Beamformer types.

            * - :py:class:`~ansys.stk.core.stkobjects.BeamSelectionStrategyType`
              - Beam selection strategy types.

            * - :py:class:`~ansys.stk.core.stkobjects.BorderWallUpperLowerEdgeAltitudeReference`
              - Border Wall upper and lower edge altitude references.

            * - :py:class:`~ansys.stk.core.stkobjects.BoresightType`
              - About boresight options for sensors of targeted pointing type.

            * - :py:class:`~ansys.stk.core.stkobjects.BuildHeightReferenceMethod`
              - REMCOM Wireless InSite RT building height reference method.

            * - :py:class:`~ansys.stk.core.stkobjects.BuildingHeightUnit`
              - REMCOM Wireless InSite RT building height unit.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDSDateFormat`
              - The date format of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDSEphemerisFormatType`
              - The ephemeris format of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDSReferenceFrame`
              - Reference Frame.

            * - :py:class:`~ansys.stk.core.stkobjects.CCSDSTimeSystem`
              - Time System.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainConstellationConstraintsMode`
              - Constellation Constraints Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainCoverageAssetMode`
              - Chain Cov Asset Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainOptimalStrandCalculationScalarMetricType`
              - Chain optimal strand calculation scalar type.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainOptimalStrandCompareStrandsType`
              - Chain optimal strand link comparison type.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainOptimalStrandLinkCompareType`
              - Chain optimal strand link comparison type.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainOptimalStrandMetricType`
              - Chain optimal strand metric type.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainParentPlatformRestriction`
              - Options for a chain's From and To Parent Platform Restriction.

            * - :py:class:`~ansys.stk.core.stkobjects.ChainTimePeriodType`
              - Compute Time Period Type.

            * - :py:class:`~ansys.stk.core.stkobjects.CircularApertureInputType`
              - Circular aperture antenna input type.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalLocation`
              - Classical (Keplerian) element used to specify the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ansys.stk.core.stkobjects.ClassicalSizeShape`
              - Pairs of Classical (Keplerian) elements used to specify orbit size and shape.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelType`
              - Clouds and Fog loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.CloudsAndFogLiquidWaterChoiceType`
              - Clouds and Fog loss model liquid water content choices.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessEventDetectionType`
              - CommSystem access options event detection type.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemAccessSamplingMethodType`
              - CommSystem access options sampling method type.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemConstrainingRole`
              - CommSystem constraining role.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemLinkSelectionCriteriaType`
              - Link selection strategy types.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemReferenceBandwidth`
              - CommSystem reference bandwidth.

            * - :py:class:`~ansys.stk.core.stkobjects.CommSystemSaveMode`
              - CommSystem save mode.

            * - :py:class:`~ansys.stk.core.stkobjects.Component`
              - The different types of components in the component browser.

            * - :py:class:`~ansys.stk.core.stkobjects.ComponentLinkEmbedControlReferenceType`
              - Component link/embed control reference type.

            * - :py:class:`~ansys.stk.core.stkobjects.Constants`
              - Constants contains base IDs for various structures.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationConstraintRestrictionType`
              - The values of the enumeration are used to define constellation constraints that allow you to specify the criteria to be used when constellations are combined with other objects in a chain.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstellationFromToParentConstraint`
              - Options for a chain's From and To Parent Constraints.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstraintBackground`
              - Options for the Background constraint, and Advanced vehicle constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstraintGroundTrack`
              - Options for the Ground Track constraint, an Advanced vehicle constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.ConstraintLighting`
              - Options for the Lighting access constraint.

            * - :py:class:`~ansys.stk.core.stkobjects.Coverage3dDrawAtAltitudeMode`
              - Coverage definition drawing modes for filled graphics when showing at altitude in 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAltitudeMethod`
              - Method for specifying the altitude of a grid point.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAssetGrouping`
              - Coverage asset grouping options.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageAssetStatus`
              - Coverage asset status.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageBounds`
              - Coverage bounds options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageCustomRegionAlgorithm`
              - The enumerations are used to enable/disable the special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageDataRetention`
              - Data retention options.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGridClass`
              - Classes of objects that can be used as templates to associate access constraints, basic object properties and, in some cases, altitude with points in the grid.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageGroundAltitudeMethod`
              - Method for specifying the ground altitude of a grid point.

            * - :py:class:`~ansys.stk.core.stkobjects.CoveragePointAltitudeMethod`
              - Custom point altitude method.

            * - :py:class:`~ansys.stk.core.stkobjects.CoveragePointLocationMethod`
              - Point location method.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageRegionAccessAccelerationType`
              - Regional acceleration options.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageResolution`
              - Coverage grid resolution options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.CoverageSatisfactionType`
              - The condition on the number of assets covering a grid point that must be satisfied for a valid access.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderElementType`
              - Specify the type of data returned by data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderResultCategory`
              - Specify the category of results returned by the data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataProviderType`
              - Specify the type of the result returned by data providers.

            * - :py:class:`~ansys.stk.core.stkobjects.DataSaveMode`
              - Access Save Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayGType`
              - Select whether to use the default representation of Delaunay G or G/SQRT(mu).

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayHType`
              - Select whether to use the default representation of Delaunay H or H/SQRT(mu).

            * - :py:class:`~ansys.stk.core.stkobjects.DelaunayLType`
              - Select whether to use the default representation of Delaunay L or L/SQRT(mu).

            * - :py:class:`~ansys.stk.core.stkobjects.DemodulatorModelType`
              - Demodulator model types.

            * - :py:class:`~ansys.stk.core.stkobjects.DeticPositionType`
              - LLA Position Types.

            * - :py:class:`~ansys.stk.core.stkobjects.DirectionProviderType`
              - Direction Provider types.

            * - :py:class:`~ansys.stk.core.stkobjects.DisplayTimesType`
              - Display times options for the object.

            * - :py:class:`~ansys.stk.core.stkobjects.DistanceOnSphere`
              - Type of line which connects the two points.

            * - :py:class:`~ansys.stk.core.stkobjects.DragModel`
              - Drag model types.

            * - :py:class:`~ansys.stk.core.stkobjects.ElementConfigurationType`
              - Element configuration types.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRFlightType`
              - EOIR Flight Types.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeMaterialSpecificationType`
              - Designation of how material properties are specified.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRShapeType`
              - The object geometry which will be rendered in the synthetic scene window.

            * - :py:class:`~ansys.stk.core.stkobjects.EOIRThermalModelType`
              - EOIR thermal models.

            * - :py:class:`~ansys.stk.core.stkobjects.EphemerisCoordinateSystemType`
              - The Coordinate System of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.EphemerisCovarianceType`
              - The covariance data export type.

            * - :py:class:`~ansys.stk.core.stkobjects.EphemExportToolFileFormat`
              - Ephemeris Export Tool file formats.

            * - :py:class:`~ansys.stk.core.stkobjects.EphemSourceType`
              - Central body ephemeris sources.

            * - :py:class:`~ansys.stk.core.stkobjects.EquinoctialFormulation`
              - Formulation: retrograde or posigrade.

            * - :py:class:`~ansys.stk.core.stkobjects.EquinoctialSizeShape`
              - Opt whether to use Mean Motion or Semimajor Axis to specify the orbit size (Equinoctial coordinate type).

            * - :py:class:`~ansys.stk.core.stkobjects.ErrorCode`
              - Error codes.

            * - :py:class:`~ansys.stk.core.stkobjects.EventDetection`
              - Available event detection strategies.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolStepSizeType`
              - The Step Size type for an attitude file.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolTimePeriodType`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.ExportToolVersionFormat`
              - The version format of the file.

            * - :py:class:`~ansys.stk.core.stkobjects.ExternalEphemerisFormatType`
              - Ephemeris file formats supported by the Stk external propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.ExternalFileMessageLevelType`
              - Ephemeris file message level used by the Stk external propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritAcrossAssets`
              - Across Assets options: specify which value of the constraint is to be selected based on all currently available assets.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritCompute`
              - Figure of Merit compute options.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritConstraintName`
              - Available constraints to use for the Access Constraint Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionType`
              - Figure of Merit types: values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritEndGapOption`
              - End gap options: control consideration of gaps at ends of analysis intervals.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DAccumulation`
              - Accumulation options: control the sense and persistence of animation graphics for a Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DColorMethod`
              - Methods for assigning colors to contour levels.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DContourType`
              - Contour fill options.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DDirection`
              - Level order display options for the contour legend.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics2DFloatingPointFormat`
              - Format options for floating point numbers.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritInvalidValueActionType`
              - Invalid Value Action: Controls consideration of time samples usage for computing navigation solution when insufficient number of assets are available at one or more of the time samples used.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritMethod`
              - Dilution of Precision method.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritNavigationAccuracyMethod`
              - Options for uncertainty in one-way range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritNavigationComputeType`
              - Allowed number of assets for the navigation solution.

            * - :py:class:`~ansys.stk.core.stkobjects.FigureOfMeritSatisfactionType`
              - Satisfaction options: determine whether satisfaction is achieved based on the value of the figure of merit.

            * - :py:class:`~ansys.stk.core.stkobjects.FrequencySpecificationType`
              - Frequency Specification Type.

            * - :py:class:`~ansys.stk.core.stkobjects.GeodeticSize`
              - Size options for the Geodetic coordinate type.

            * - :py:class:`~ansys.stk.core.stkobjects.GeometricElementType`
              - Options for the VORefCrdn Type.

            * - :py:class:`~ansys.stk.core.stkobjects.GPSAttitudeModelType`
              - GPS attitude profile model types.

            * - :py:class:`~ansys.stk.core.stkobjects.GPSReferenceWeek`
              - GPS almanac reference week.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DACAPCoefficientDataType`
              - VOACAP coefficient data type.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DACAPSolarActivityConfigurationType`
              - VOACAP solar activity configuration type.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DFontSize`
              - Font size for data display.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DFormat`
              - Font format for data display.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DLabelSwapDistanceType`
              - Label swap distance options.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DLocation`
              - Location options for the display of textual data in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarkerOrientation`
              - 3D graphics marker orientations.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DMarkerOriginType`
              - Options for the Graphics3DMarker X or Y Origin property.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DXOrigin`
              - X origin options for positioning data display.

            * - :py:class:`~ansys.stk.core.stkobjects.Graphics3DYOrigin`
              - Y origin options for positioning data display.

            * - :py:class:`~ansys.stk.core.stkobjects.HelpContextIdentifierType`
              - Help context IDs.

            * - :py:class:`~ansys.stk.core.stkobjects.HFSSFarFieldDataGainType`
              - Gain type.

            * - :py:class:`~ansys.stk.core.stkobjects.IntersectionType`
              - Intersection display options for sensor projection.

            * - :py:class:`~ansys.stk.core.stkobjects.IonosphericFadingLossModelType`
              - Ionospheric loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.IvClockHost`
              - Clock host options for access. Time values are reported with a clock colocated with the clock host object.

            * - :py:class:`~ansys.stk.core.stkobjects.IvTimeSense`
              - Mode of signal transmission of the designated clock host.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserPropagationLossModelType`
              - Laser propagation loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.LaserTroposphericScintillationLossModelType`
              - Laser tropospheric scintillation loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.LatticeType`
              - Lattice types.

            * - :py:class:`~ansys.stk.core.stkobjects.LeadTrailData`
              - Lead and trail types for track display.

            * - :py:class:`~ansys.stk.core.stkobjects.LightingObstructionModelType`
              - Obstruction model used in lighting computations.

            * - :py:class:`~ansys.stk.core.stkobjects.LimitsExceededBehaviorType`
              - Limits Exceeded Behavior types.

            * - :py:class:`~ansys.stk.core.stkobjects.LineWidth`
              - Line widths.

            * - :py:class:`~ansys.stk.core.stkobjects.LinkMarginType`
              - Link margin types.

            * - :py:class:`~ansys.stk.core.stkobjects.LoadMethod`
              - TLE load options.

            * - :py:class:`~ansys.stk.core.stkobjects.LookAheadPropagator`
              - Propagators used for calculating ephemeris for look ahead purposes. The enumeration is used with realtime propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.LOPAtmosphericDensityModel`
              - LOP Atmospheric density models.

            * - :py:class:`~ansys.stk.core.stkobjects.LowAltitudeAtmosphericDensityModel`
              - Low Altitude Atmospheric density models.

            * - :py:class:`~ansys.stk.core.stkobjects.MarkerShape3d`
              - 3D marker shapes.

            * - :py:class:`~ansys.stk.core.stkobjects.MarkerType`
              - Marker style options for a waypoint.

            * - :py:class:`~ansys.stk.core.stkobjects.MethodToComputeSunPosition`
              - Methods to compute sun position.

            * - :py:class:`~ansys.stk.core.stkobjects.MixedSphericalFlightPathAngleType`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~ansys.stk.core.stkobjects.ModelGltfReflectionMapType`
              - Settings for glTF Reflection.

            * - :py:class:`~ansys.stk.core.stkobjects.ModelType`
              - Display options 3D model.

            * - :py:class:`~ansys.stk.core.stkobjects.ModtranAerosolModelType`
              - MODTRAN-derived lookup table aerosol model extinction types.

            * - :py:class:`~ansys.stk.core.stkobjects.ModtranCloudModelType`
              - MODTRAN Cloud model types.

            * - :py:class:`~ansys.stk.core.stkobjects.ModulatorModelType`
              - Modulator model types.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOEntirety`
              - MTO Entirety Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOInputDataType`
              - MTO Input Data Type.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOObjectInterval`
              - MTO object interval type.

            * - :py:class:`~ansys.stk.core.stkobjects.MTORangeMode`
              - MTO Range Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOTrackEvaluationType`
              - MTO Track Eval Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.MTOVisibilityMode`
              - MTO Visibility Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.NoiseTemperatureComputeType`
              - System noise temperature compute type.

            * - :py:class:`~ansys.stk.core.stkobjects.NoteShowType`
              - Options for specifying when a label note displays.

            * - :py:class:`~ansys.stk.core.stkobjects.NotificationFilterMask`
              - The notification flags are used to enable/disable STK Object Model event notifications.

            * - :py:class:`~ansys.stk.core.stkobjects.OffsetFrameType`
              - Frame options for label offset.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessStatus`
              - One point access status.

            * - :py:class:`~ansys.stk.core.stkobjects.OnePointAccessSummary`
              - One point access summary type.

            * - :py:class:`~ansys.stk.core.stkobjects.OrientationAscNode`
              - Ascending node-related options for use in specifying orbit orientation.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetOrbitDisplayType`
              - Orbit display options for a planet.

            * - :py:class:`~ansys.stk.core.stkobjects.PlanetPositionSourceType`
              - Options for defining a planet.

            * - :py:class:`~ansys.stk.core.stkobjects.PointingStrategyType`
              - Pointing strategy type.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationReferenceAxis`
              - Polarization reference axis.

            * - :py:class:`~ansys.stk.core.stkobjects.PolarizationType`
              - Polarization Type.

            * - :py:class:`~ansys.stk.core.stkobjects.PRFMode`
              - Radar search/track prf modes.

            * - :py:class:`~ansys.stk.core.stkobjects.ProjectionHorizontalDatumType`
              - REMCOM Wireless InSite RT project/horizontal datum type.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorDisplayCoordinateType`
              - Propagator Display Coordinate Types.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorSGP4SwitchMethod`
              - TLE Switch method for the SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.PropagatorType`
              - Vehicle propagators (available for vehicle types listed in parentheses).

            * - :py:class:`~ansys.stk.core.stkobjects.PulseWidthMode`
              - Radar search/track pulse width modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarActivityType`
              - Radar activity times strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarClutterGeometryModelType`
              - Radar clutter geometry model type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarClutterMapModelType`
              - Radar clutter map model type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarContinuousWaveAnalysisMode`
              - Radar continuous wave analysis mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarCrossSectionContourGraphicsPolarization`
              - Radar cross section contour graphics polarization.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarFrequencySpecificationType`
              - SNR Contour Type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarMode`
              - Radar mode types.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarModelType`
              - Radar system types.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarProbabilityOfDetectionType`
              - Radar probability of detection type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarPulseIntegrationType`
              - Radar pulse integration type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarPulseIntegratorType`
              - Radar pulse integrator type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSarPcrMode`
              - Radar SAR pulse compression ratio modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSarPRFMode`
              - Radar SAR prf modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSARPulseIntegrationAnalysisMode`
              - Radar sar pulse integration mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSarRangeResolutionMode`
              - Radar SAR range resolution modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSearchTrackPRFMode`
              - Radar search/track prf modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSearchTrackPulseWidthMode`
              - Radar search/track pulse width modes.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSNRContourType`
              - SNR Contour Type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSTCAttenuationType`
              - Stc Attenuation Type.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarSwerlingCase`
              - Radar swerling case.

            * - :py:class:`~ansys.stk.core.stkobjects.RadarWaveformSearchTrackType`
              - Radar search/track waveform types.

            * - :py:class:`~ansys.stk.core.stkobjects.RainLossModelType`
              - Rain loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.RCSComputeStrategy`
              - Radar cross section compute strategy.

            * - :py:class:`~ansys.stk.core.stkobjects.ReceiverModelType`
              - Receiver model types.

            * - :py:class:`~ansys.stk.core.stkobjects.RectangularApertureInputType`
              - Rectangular aperture antenna input type.

            * - :py:class:`~ansys.stk.core.stkobjects.ReTransmitterOpMode`
              - Re-Transmitter operational mode.

            * - :py:class:`~ansys.stk.core.stkobjects.RFFilterModelType`
              - RF filter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.RouteGraphics3DMarkerType`
              - Waypoint marker options.

            * - :py:class:`~ansys.stk.core.stkobjects.SamplingMethod`
              - Available sampling methods.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointModelType`
              - Scattering point model type.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderListType`
              - Scattering Point Provider List Type.

            * - :py:class:`~ansys.stk.core.stkobjects.ScatteringPointProviderType`
              - Scattering point provider type.

            * - :py:class:`~ansys.stk.core.stkobjects.Scenario3dPointSize`
              - Font size in points.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioEndLoopType`
              - Scenario animation cycle options.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioRefreshDeltaType`
              - Scenario animation refresh update options.

            * - :py:class:`~ansys.stk.core.stkobjects.ScenarioTimeStepType`
              - Scenario animation time step options.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAltitudeCrossingDirection`
              - Options for specifying the direction in which the sensor's field of view crosses the specified altitude.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAltitudeCrossingSideType`
              - Options for specifying which crossings are computed and displayed in the 2D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorAzElBoresightAxisType`
              - Primary boresight axis for Sensor Az-El mask.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandImageQuality`
              - EOIR band image quality levels.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandOpticalInputMode`
              - EOIR optical input parameter specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandOpticalTransmissionMode`
              - EOIR optical transmission parameter specification mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandQuantizationMode`
              - EOIR mode of determining quantization step size.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandQuantumEfficiencyMode`
              - EOIR quantum efficiency specification mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandRadiometricParameterLevelType`
              - EOIR radiometric detector parameter level of specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandSaturationMode`
              - EOIR band irradiance or radiance reference mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandSpatialInputMode`
              - EOIR spatial input parameter specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandSpectralRelativeSystemResponseUnitsType`
              - EOIR spectral relative system response units specification.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandSpectralShape`
              - EOIR overall system spectral shape determination.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRBandWavelengthType`
              - EOIR band diffraction wavelength reference type.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRJitterType`
              - EOIR jitter type.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRProcessingLevelType`
              - EOIR processing levels.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorEOIRScanMode`
              - EOIR sensor scan mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DInheritFrom2D`
              - Options for how projection distances that are computed based on 2D Graphics projection settings are displayed in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DProjectionTimeDependencyType`
              - The different ways to determine the sensor's space projection distance in the 3D window.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DProjectionType`
              - Options for a sensor's 3D Graphics Projection Type.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DPulseFrequencyPreset`
              - Options for a sensor's 3D Graphics Pulse Frequency presets.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DPulseStyle`
              - Options for a sensor's 3D Graphics Pulse Style.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorGraphics3DVisualAppearance`
              - Options optimizing the visual appearance of projections.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorLocation`
              - Sensor Location Type options.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPattern`
              - Sensor patterns.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointing`
              - Sensor pointing options.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorPointingTargetedBoresightType`
              - Boresight types for sensors of targeted pointing type.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorProjectionDistanceType`
              - Sensor 2D Graphics Projection 'Project To' options.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorRefractionType`
              - Sensor refraction models.

            * - :py:class:`~ansys.stk.core.stkobjects.SensorScanMode`
              - Options for the Sensor Spinning Scan Mode.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarRadiationPressureModelType`
              - Solar radiation pressure model types.

            * - :py:class:`~ansys.stk.core.stkobjects.SolarRadiationPressureShadowModelType`
              - Shadow model options for solar radiation pressure.

            * - :py:class:`~ansys.stk.core.stkobjects.SolidTide`
              - The Solid Tide Type for force modeling.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentCrresProtonActivity`
              - Activity level for CRRESPRO model.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentCrresRadiationActivity`
              - Activity level for CRRESRAD model.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagneticExternalField`
              - External magnetic field.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagneticFieldColorMode`
              - Mode by which color is assigned.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagneticFieldColorScaleType`
              - Scaling of magnetic field to use when assigning color/translucency.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentMagneticMainField`
              - Main magnetic field.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentNasaModelsActivity`
              - Activity level for the NASA models NASAELE and NASAPRO.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentSAAChannel`
              - Energy level for SAA protons.

            * - :py:class:`~ansys.stk.core.stkobjects.SpaceEnvironmentSAAFluxLevel`
              - Flux level for SAA contour.

            * - :py:class:`~ansys.stk.core.stkobjects.SpacingUnit`
              - Spacing Units.

            * - :py:class:`~ansys.stk.core.stkobjects.SphericalFlightPathAzimuthType`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~ansys.stk.core.stkobjects.SpiceInterpolation`
              - The SPICE interpolation type.

            * - :py:class:`~ansys.stk.core.stkobjects.StarReferenceFrame`
              - Star reference frame types.

            * - :py:class:`~ansys.stk.core.stkobjects.StatisticType`
              - The different statistics that might be available for a data set.

            * - :py:class:`~ansys.stk.core.stkobjects.STKObjectType`
              - STK objects.

            * - :py:class:`~ansys.stk.core.stkobjects.SurfaceReference`
              - Options for surface reference of earth globes.

            * - :py:class:`~ansys.stk.core.stkobjects.SwathComputationalMethod`
              - Computationals methods for generating swaths.

            * - :py:class:`~ansys.stk.core.stkobjects.TargetSelectionMethod`
              - Target Selection Method types.

            * - :py:class:`~ansys.stk.core.stkobjects.TerrainFileType`
              - Terrain file type options.

            * - :py:class:`~ansys.stk.core.stkobjects.TerrainNormalType`
              - Methods of defining the slope of the local terrain for the facility, place or target.

            * - :py:class:`~ansys.stk.core.stkobjects.TextOutlineStyle`
              - The text outline style for 2D graphics display.

            * - :py:class:`~ansys.stk.core.stkobjects.ThirdBodyGravitySourceType`
              - Sources for 3rd body gravitation data.

            * - :py:class:`~ansys.stk.core.stkobjects.TickData`
              - Tick mark options. Tick marks represent milestones at specified intervals along a vehicle's track in the 3D Graphics window.

            * - :py:class:`~ansys.stk.core.stkobjects.Tileset3DSourceType`
              - 3DTileset source type options.

            * - :py:class:`~ansys.stk.core.stkobjects.TimePeriodValueType`
              - Time value types.

            * - :py:class:`~ansys.stk.core.stkobjects.TimeVaryingExtremum`
              - The different time varying extremum that might be available for a data set.

            * - :py:class:`~ansys.stk.core.stkobjects.TIREMPolarizationType`
              - TIREM polarization type.

            * - :py:class:`~ansys.stk.core.stkobjects.TrackMode`
              - Track mode options for tracking boresights.

            * - :py:class:`~ansys.stk.core.stkobjects.TrajectoryType`
              - Trajectory type for a point.

            * - :py:class:`~ansys.stk.core.stkobjects.TransferFunctionType`
              - Transmitter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.TransmitterModelType`
              - Transmitter model types.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationAverageTimeChoiceType`
              - TroposphericScintillation loss model average time choices.

            * - :py:class:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelType`
              - TropoScintillation loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.UrbanTerrestrialLossModelType`
              - urban/terrestrial loss model types.

            * - :py:class:`~ansys.stk.core.stkobjects.VectorAxesConnectType`
              - Methods for connecting geometric elements.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAltitudeReference`
              - Reference altitude options for waypoints.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleAttitude`
              - Available attitude types.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleBreakAngleType`
              - Definition options for setting pass breaks:.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleConsiderAnalysisType`
              - Consider parameters for HPOP covariance.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCoordinateSystem`
              - Coordinate system used for measurement of latitude and longitude.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleCorrelationListType`
              - Correlation List row and column values.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleDirection`
              - Direction of latitude crossing at the beginning of a pass.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleEllipseOptionType`
              - Elliptical motion modeling options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleFrame`
              - Frame options for covariance matrix.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGeomagneticFluxSourceType`
              - GeomagFluxSrc.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGeomagneticFluxUpdateRateType`
              - Geomagnetic flux update rate options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAlmanacType`
              - GPS Almanac types.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSAutomaticUpdateSourceType`
              - The sources to retrieve GPS elements from upon propagation.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSElementSelectionType`
              - GPS Selection method for the GPS propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGPSSwitchMethod`
              - GPS Switch method for the GPS propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributeType`
              - Criteria for displaying a vehicle's 2D Graphics attributes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DElevation`
              - Options for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DOffset`
              - Options for offset direction for 2D time events graphics.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DOptionType`
              - Display options for vehicle swath.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DPass`
              - Pass display options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DTimeEventType`
              - 2D Graphics time event graphics options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics2DVisibleSideType`
              - Pass display direction options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DAttributeType`
              - Options for 3D graphics for covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DBPlaneTargetPointPosition`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLineType`
              - Options for where to end drop lines.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleGraphics3DSigmaScale`
              - Sigma scale options for sizing covariance pointing contours.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpact`
              - Impact location options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleImpactLocation`
              - Options for specifying missile impact point.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleIntegrationModel`
              - Integration methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleInterpolationMethod`
              - Interpolation methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunch`
              - Options for launch coordinates.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLaunchControl`
              - Flight parameters for a missile.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleLookAheadMethod`
              - Look ahead duration methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleMethod`
              - Step size control options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePartialPassMeasurement`
              - Partial Pass Measurement methods (typically used for reporting data).

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePassNumbering`
              - Pass numbering options.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePredictorCorrectorScheme`
              - Predictor Corrector schemes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehiclePropagationFrame`
              - Propagation frames used by J2/J4/TwoBody propagators.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4AutomaticUpdateSourceType`
              - The TLE sources where the SGP4 propagator retrieves TLEs from automatically upon propagation.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSGP4TLESelectionType`
              - TLE Selection method for the SGP4 propagator.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSlewMode`
              - Target slew modes.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSlewTimingBetweenTargetType`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSolarFluxGeomagneticType`
              - Options for specifying solar and geomagnetic flux.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentApSource`
              - Mode for computing 15 day average Ap.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentComputationMode`
              - Models that are to be included when modeling radiation.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentDetectorGeometry`
              - Detector geometry.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentDetectorType`
              - Detector material.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentDoseChannel`
              - Dose channel.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentF10P7SourceType`
              - Mode for computing 13-month average F10.7.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentMaterial`
              - Material.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentShapeModel`
              - Thermal shape model.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointComputationMethod`
              - Methods for computing waypoints.

            * - :py:class:`~ansys.stk.core.stkobjects.VehicleWaypointInterpolationMethod`
              - Interpolation methods.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricDataExportFormatType`
              - Volumetric data export format types.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricDefinitionType`
              - Volume grid definition types.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricDisplayQualityType`
              - Quality of the graphics display types.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricDisplayVolumeType`
              - Graphics volume display type.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricLegendNumericNotationType`
              - Legend numeric notation types.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricLevelOrder`
              - Legend level display order.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricSaveComputedDataType`
              - Save Computed Data types.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricSpatialCalculationEvaluationType`
              - Evaluation of Spatial Calculation types.

            * - :py:class:`~ansys.stk.core.stkobjects.VolumetricVolumeGridExportType`
              - Volumetric data export types.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformSelectionStrategyType`
              - Waveform selection strategy type.

            * - :py:class:`~ansys.stk.core.stkobjects.WaveformType`
              - Waveform types.



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

     IAccessAdvanced<stkobjects/IAccessAdvanced>
     IAccessConstraint<stkobjects/IAccessConstraint>
     IAccessConstraintMinMaxBase<stkobjects/IAccessConstraintMinMaxBase>
     IAccessInterval<stkobjects/IAccessInterval>
     IAnimation<stkobjects/IAnimation>
     IAntennaBeam<stkobjects/IAntennaBeam>
     IAntennaBeamSelectionStrategy<stkobjects/IAntennaBeamSelectionStrategy>
     IAntennaContour<stkobjects/IAntennaContour>
     IAntennaModel<stkobjects/IAntennaModel>
     IAntennaModelOpticalSimple<stkobjects/IAntennaModelOpticalSimple>
     IAreaTypeData<stkobjects/IAreaTypeData>
     IAtmosphericAbsorptionModel<stkobjects/IAtmosphericAbsorptionModel>
     IAtmosphericAbsorptionModelITURP676<stkobjects/IAtmosphericAbsorptionModelITURP676>
     IAtmosphericAbsorptionModelTIREM<stkobjects/IAtmosphericAbsorptionModelTIREM>
     IAtmosphericTurbulenceModel<stkobjects/IAtmosphericTurbulenceModel>
     IAzElMaskData<stkobjects/IAzElMaskData>
     IBeamformer<stkobjects/IBeamformer>
     ICelestialBodyInformation<stkobjects/ICelestialBodyInformation>
     ICelestialBodyInformationCollection<stkobjects/ICelestialBodyInformationCollection>
     IChainTimePeriod<stkobjects/IChainTimePeriod>
     IClassicalLocation<stkobjects/IClassicalLocation>
     IClassicalSizeShape<stkobjects/IClassicalSizeShape>
     ICloneable<stkobjects/ICloneable>
     ICloudsAndFogFadingLossModel<stkobjects/ICloudsAndFogFadingLossModel>
     ICommSystemAccessEventDetection<stkobjects/ICommSystemAccessEventDetection>
     ICommSystemAccessSamplingMethod<stkobjects/ICommSystemAccessSamplingMethod>
     ICommSystemLinkSelectionCriteria<stkobjects/ICommSystemLinkSelectionCriteria>
     IComponentInfo<stkobjects/IComponentInfo>
     IComponentLinkEmbedControl<stkobjects/IComponentLinkEmbedControl>
     IConstellationConstraintRestriction<stkobjects/IConstellationConstraintRestriction>
     ICoverageBounds<stkobjects/ICoverageBounds>
     ICoverageResolution<stkobjects/ICoverageResolution>
     IDataProvider<stkobjects/IDataProvider>
     IDataProviderInfo<stkobjects/IDataProviderInfo>
     IDelaunayActionVariable<stkobjects/IDelaunayActionVariable>
     IDemodulatorModel<stkobjects/IDemodulatorModel>
     IDirectionProvider<stkobjects/IDirectionProvider>
     IDisplayDistance<stkobjects/IDisplayDistance>
     IDisplayTime<stkobjects/IDisplayTime>
     IDisplayTimesData<stkobjects/IDisplayTimesData>
     IElementConfiguration<stkobjects/IElementConfiguration>
     IElementConfigurationPolygon<stkobjects/IElementConfigurationPolygon>
     IEOIR<stkobjects/IEOIR>
     IEOIRShapeObject<stkobjects/IEOIRShapeObject>
     IEventDetectionStrategy<stkobjects/IEventDetectionStrategy>
     IFigureOfMeritDefinition<stkobjects/IFigureOfMeritDefinition>
     IFigureOfMeritDefinitionCompute<stkobjects/IFigureOfMeritDefinitionCompute>
     IFigureOfMeritDefinitionData<stkobjects/IFigureOfMeritDefinitionData>
     IFigureOfMeritDefinitionDilutionOfPrecision<stkobjects/IFigureOfMeritDefinitionDilutionOfPrecision>
     IFigureOfMeritDefinitionResponseTime<stkobjects/IFigureOfMeritDefinitionResponseTime>
     IFigureOfMeritGraphics2DAttributes<stkobjects/IFigureOfMeritGraphics2DAttributes>
     IFigureOfMeritGraphics2DContours<stkobjects/IFigureOfMeritGraphics2DContours>
     IFigureOfMeritNavigationAccuracyMethod<stkobjects/IFigureOfMeritNavigationAccuracyMethod>
     IFlightPathAngle<stkobjects/IFlightPathAngle>
     IGeodeticSize<stkobjects/IGeodeticSize>
     IGraphics3DMarkerData<stkobjects/IGraphics3DMarkerData>
     IGraphics3DModel<stkobjects/IGraphics3DModel>
     IGraphics3DModelData<stkobjects/IGraphics3DModelData>
     IGraphics3DReferenceAnalysisWorkbenchComponent<stkobjects/IGraphics3DReferenceAnalysisWorkbenchComponent>
     IGreatArcGraphics<stkobjects/IGreatArcGraphics>
     IGreatArcGraphics3D<stkobjects/IGreatArcGraphics3D>
     IGreatArcVehicle<stkobjects/IGreatArcVehicle>
     IIonosphericFadingLossModel<stkobjects/IIonosphericFadingLossModel>
     ILaserAtmosphericLossModel<stkobjects/ILaserAtmosphericLossModel>
     ILaserPropagationChannel<stkobjects/ILaserPropagationChannel>
     ILaserTroposphericScintillationLossModel<stkobjects/ILaserTroposphericScintillationLossModel>
     ILatitudeLongitudeAltitudePosition<stkobjects/ILatitudeLongitudeAltitudePosition>
     ILifetimeInformation<stkobjects/ILifetimeInformation>
     IModulatorModel<stkobjects/IModulatorModel>
     IModulatorModelScriptPlugin<stkobjects/IModulatorModelScriptPlugin>
     IOrbitDisplayData<stkobjects/IOrbitDisplayData>
     IOrientationAscNode<stkobjects/IOrientationAscNode>
     IPlatformRFEnvironment<stkobjects/IPlatformRFEnvironment>
     IPointingStrategy<stkobjects/IPointingStrategy>
     IPolarization<stkobjects/IPolarization>
     IPolarizationCrossPolLeakage<stkobjects/IPolarizationCrossPolLeakage>
     IPolarizationElliptical<stkobjects/IPolarizationElliptical>
     IPolarizationHorizontal<stkobjects/IPolarizationHorizontal>
     IPolarizationLinear<stkobjects/IPolarizationLinear>
     IPolarizationVertical<stkobjects/IPolarizationVertical>
     IPositionSourceData<stkobjects/IPositionSourceData>
     IPropagator<stkobjects/IPropagator>
     IPropagatorSGP4LoadData<stkobjects/IPropagatorSGP4LoadData>
     IProvideSpatialInfo<stkobjects/IProvideSpatialInfo>
     IRadarActivity<stkobjects/IRadarActivity>
     IRadarClutterGeometryModel<stkobjects/IRadarClutterGeometryModel>
     IRadarClutterGeometryModelPlugin<stkobjects/IRadarClutterGeometryModelPlugin>
     IRadarClutterMap<stkobjects/IRadarClutterMap>
     IRadarClutterMapInheritable<stkobjects/IRadarClutterMapInheritable>
     IRadarClutterMapModel<stkobjects/IRadarClutterMapModel>
     IRadarClutterMapModelConstantCoefficient<stkobjects/IRadarClutterMapModelConstantCoefficient>
     IRadarClutterMapModelPlugin<stkobjects/IRadarClutterMapModelPlugin>
     IRadarContinuousWaveAnalysisMode<stkobjects/IRadarContinuousWaveAnalysisMode>
     IRadarCrossSectionComputeStrategy<stkobjects/IRadarCrossSectionComputeStrategy>
     IRadarModeBistaticReceiver<stkobjects/IRadarModeBistaticReceiver>
     IRadarModeBistaticTransmitter<stkobjects/IRadarModeBistaticTransmitter>
     IRadarModel<stkobjects/IRadarModel>
     IRadarModeMonostatic<stkobjects/IRadarModeMonostatic>
     IRadarProbabilityOfDetection<stkobjects/IRadarProbabilityOfDetection>
     IRadarProbabilityOfDetectionCFAR<stkobjects/IRadarProbabilityOfDetectionCFAR>
     IRadarPulseIntegration<stkobjects/IRadarPulseIntegration>
     IRadarSTCAttenuation<stkobjects/IRadarSTCAttenuation>
     IRadarSTCAttenuationMap<stkobjects/IRadarSTCAttenuationMap>
     IRadarWaveformSearchTrack<stkobjects/IRadarWaveformSearchTrack>
     IRainLossModel<stkobjects/IRainLossModel>
     IReceiverModel<stkobjects/IReceiverModel>
     IReceiverModelScriptPlugin<stkobjects/IReceiverModelScriptPlugin>
     IRefractionModelBase<stkobjects/IRefractionModelBase>
     IReTransmitterModel<stkobjects/IReTransmitterModel>
     IRFFilterModel<stkobjects/IRFFilterModel>
     ISamplingMethodStrategy<stkobjects/ISamplingMethodStrategy>
     IScatteringPointModel<stkobjects/IScatteringPointModel>
     IScatteringPointProvider<stkobjects/IScatteringPointProvider>
     ISensorPattern<stkobjects/ISensorPattern>
     ISensorPointing<stkobjects/ISensorPointing>
     ISensorPointingTargetedBoresight<stkobjects/ISensorPointingTargetedBoresight>
     ISensorProjectionDisplayDistance<stkobjects/ISensorProjectionDisplayDistance>
     ISolarActivityConfiguration<stkobjects/ISolarActivityConfiguration>
     ISRPModelBase<stkobjects/ISRPModelBase>
     ISTKObject<stkobjects/ISTKObject>
     ISTKObjectCollection<stkobjects/ISTKObjectCollection>
     ISTKObjectElementCollection<stkobjects/ISTKObjectElementCollection>
     ITargetSelectionMethod<stkobjects/ITargetSelectionMethod>
     ITerrainNormData<stkobjects/ITerrainNormData>
     ITimePeriod<stkobjects/ITimePeriod>
     ITransmitterModel<stkobjects/ITransmitterModel>
     ITransmitterModelScriptPlugin<stkobjects/ITransmitterModelScriptPlugin>
     ITroposphericScintillationFadingLossModel<stkobjects/ITroposphericScintillationFadingLossModel>
     IUrbanTerrestrialLossModel<stkobjects/IUrbanTerrestrialLossModel>
     IVehicleAttitude<stkobjects/IVehicleAttitude>
     IVehicleAttitudeProfile<stkobjects/IVehicleAttitudeProfile>
     IVehicleAttitudeSlewBase<stkobjects/IVehicleAttitudeSlewBase>
     IVehicleAttitudeStandard<stkobjects/IVehicleAttitudeStandard>
     IVehicleBreakAngle<stkobjects/IVehicleBreakAngle>
     IVehicleCoordinateAxes<stkobjects/IVehicleCoordinateAxes>
     IVehicleGPSAlmanacProperties<stkobjects/IVehicleGPSAlmanacProperties>
     IVehicleGraphics2DAttributes<stkobjects/IVehicleGraphics2DAttributes>
     IVehicleGraphics2DAttributesBasic<stkobjects/IVehicleGraphics2DAttributesBasic>
     IVehicleGraphics2DAttributesDisplayState<stkobjects/IVehicleGraphics2DAttributesDisplayState>
     IVehicleGraphics2DElevation<stkobjects/IVehicleGraphics2DElevation>
     IVehicleGraphics2DPass<stkobjects/IVehicleGraphics2DPass>
     IVehicleGraphics2DTimeComponentsElement<stkobjects/IVehicleGraphics2DTimeComponentsElement>
     IVehicleGraphics2DTimeEventType<stkobjects/IVehicleGraphics2DTimeEventType>
     IVehicleGraphics3DAttributes<stkobjects/IVehicleGraphics3DAttributes>
     IVehicleGraphics3DBPlaneTargetPointPosition<stkobjects/IVehicleGraphics3DBPlaneTargetPointPosition>
     IVehicleGraphics3DProximity<stkobjects/IVehicleGraphics3DProximity>
     IVehicleGraphics3DProximityAreaObject<stkobjects/IVehicleGraphics3DProximityAreaObject>
     IVehicleGraphics3DSigmaScale<stkobjects/IVehicleGraphics3DSigmaScale>
     IVehicleGraphics3DSystemsElementBase<stkobjects/IVehicleGraphics3DSystemsElementBase>
     IVehicleGraphics3DTickData<stkobjects/IVehicleGraphics3DTickData>
     IVehicleHPOPDragModel<stkobjects/IVehicleHPOPDragModel>
     IVehicleImpact<stkobjects/IVehicleImpact>
     IVehicleImpactLocation<stkobjects/IVehicleImpactLocation>
     IVehicleLaunch<stkobjects/IVehicleLaunch>
     IVehicleLaunchControl<stkobjects/IVehicleLaunchControl>
     IVehicleLeadTrailData<stkobjects/IVehicleLeadTrailData>
     IVehicleLeadTrailDataFraction<stkobjects/IVehicleLeadTrailDataFraction>
     IVehicleLeadTrailDataTime<stkobjects/IVehicleLeadTrailDataTime>
     IVehiclePassNumbering<stkobjects/IVehiclePassNumbering>
     IVehiclePointing<stkobjects/IVehiclePointing>
     IVehicleSolarFluxGeoMagnitude<stkobjects/IVehicleSolarFluxGeoMagnitude>
     IVehicleWaypointAltitudeReference<stkobjects/IVehicleWaypointAltitudeReference>
     IVolumetricGridDefinition<stkobjects/IVolumetricGridDefinition>
     IWaveform<stkobjects/IWaveform>
     IWaveformSelectionStrategy<stkobjects/IWaveformSelectionStrategy>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     Access<stkobjects/Access>
     AccessAdvancedSettings<stkobjects/AccessAdvancedSettings>
     AccessAllowedTimeIntervals<stkobjects/AccessAllowedTimeIntervals>
     AccessConstraint<stkobjects/AccessConstraint>
     AccessConstraintAnalysisWorkbench<stkobjects/AccessConstraintAnalysisWorkbench>
     AccessConstraintAnalysisWorkbenchCollection<stkobjects/AccessConstraintAnalysisWorkbenchCollection>
     AccessConstraintAnalysisWorkbenchComponent<stkobjects/AccessConstraintAnalysisWorkbenchComponent>
     AccessConstraintAngle<stkobjects/AccessConstraintAngle>
     AccessConstraintBackground<stkobjects/AccessConstraintBackground>
     AccessConstraintCentralBodyObstruction<stkobjects/AccessConstraintCentralBodyObstruction>
     AccessConstraintCollection<stkobjects/AccessConstraintCollection>
     AccessConstraintCondition<stkobjects/AccessConstraintCondition>
     AccessConstraintExclZonesCollection<stkobjects/AccessConstraintExclZonesCollection>
     AccessConstraintGrazingAltitude<stkobjects/AccessConstraintGrazingAltitude>
     AccessConstraintGroundTrack<stkobjects/AccessConstraintGroundTrack>
     AccessConstraintIntervals<stkobjects/AccessConstraintIntervals>
     AccessConstraintLatitudeLongitudeZone<stkobjects/AccessConstraintLatitudeLongitudeZone>
     AccessConstraintMinMaxBase<stkobjects/AccessConstraintMinMaxBase>
     AccessConstraintObjExAngle<stkobjects/AccessConstraintObjExAngle>
     AccessConstraintPluginMinMax<stkobjects/AccessConstraintPluginMinMax>
     AccessConstraintThirdBody<stkobjects/AccessConstraintThirdBody>
     AccessConstraintTimeSlipRange<stkobjects/AccessConstraintTimeSlipRange>
     AccessEventDetection<stkobjects/AccessEventDetection>
     AccessGraphics<stkobjects/AccessGraphics>
     AccessSampling<stkobjects/AccessSampling>
     AccessTargetTime<stkobjects/AccessTargetTime>
     AccessTargetTimesCollection<stkobjects/AccessTargetTimesCollection>
     AccessTimePeriod<stkobjects/AccessTimePeriod>
     AdditionalGainLoss<stkobjects/AdditionalGainLoss>
     AdditionalGainLossCollection<stkobjects/AdditionalGainLossCollection>
     AdvCAT<stkobjects/AdvCAT>
     AdvCATAdvancedEllipsoid<stkobjects/AdvCATAdvancedEllipsoid>
     AdvCATAdvancedSettings<stkobjects/AdvCATAdvancedSettings>
     AdvCATAvailableObjectCollection<stkobjects/AdvCATAvailableObjectCollection>
     AdvCATChosenObject<stkobjects/AdvCATChosenObject>
     AdvCATChosenObjectCollection<stkobjects/AdvCATChosenObjectCollection>
     AdvCATGraphics3D<stkobjects/AdvCATGraphics3D>
     AdvCATPreFilters<stkobjects/AdvCATPreFilters>
     Aircraft<stkobjects/Aircraft>
     AircraftExportTools<stkobjects/AircraftExportTools>
     AircraftGraphics<stkobjects/AircraftGraphics>
     AircraftGraphics3D<stkobjects/AircraftGraphics3D>
     Antenna<stkobjects/Antenna>
     AntennaBeam<stkobjects/AntennaBeam>
     AntennaBeamCollection<stkobjects/AntennaBeamCollection>
     AntennaBeamSelectionStrategy<stkobjects/AntennaBeamSelectionStrategy>
     AntennaBeamSelectionStrategyAggregate<stkobjects/AntennaBeamSelectionStrategyAggregate>
     AntennaBeamSelectionStrategyMaximumGain<stkobjects/AntennaBeamSelectionStrategyMaximumGain>
     AntennaBeamSelectionStrategyMinimumBoresightAngle<stkobjects/AntennaBeamSelectionStrategyMinimumBoresightAngle>
     AntennaBeamSelectionStrategyScriptPlugin<stkobjects/AntennaBeamSelectionStrategyScriptPlugin>
     AntennaBeamTransmit<stkobjects/AntennaBeamTransmit>
     AntennaContourEIRP<stkobjects/AntennaContourEIRP>
     AntennaContourFluxDensity<stkobjects/AntennaContourFluxDensity>
     AntennaContourGain<stkobjects/AntennaContourGain>
     AntennaContourGraphics<stkobjects/AntennaContourGraphics>
     AntennaContourLevel<stkobjects/AntennaContourLevel>
     AntennaContourLevelCollection<stkobjects/AntennaContourLevelCollection>
     AntennaContourRIP<stkobjects/AntennaContourRIP>
     AntennaContourSpectralFluxDensity<stkobjects/AntennaContourSpectralFluxDensity>
     AntennaControl<stkobjects/AntennaControl>
     AntennaGraphics<stkobjects/AntennaGraphics>
     AntennaGraphics3D<stkobjects/AntennaGraphics3D>
     AntennaModel<stkobjects/AntennaModel>
     AntennaModelANSYSffdFormat<stkobjects/AntennaModelANSYSffdFormat>
     AntennaModelApertureCircularBessel<stkobjects/AntennaModelApertureCircularBessel>
     AntennaModelApertureCircularBesselEnvelope<stkobjects/AntennaModelApertureCircularBesselEnvelope>
     AntennaModelApertureCircularCosine<stkobjects/AntennaModelApertureCircularCosine>
     AntennaModelApertureCircularCosinePedestal<stkobjects/AntennaModelApertureCircularCosinePedestal>
     AntennaModelApertureCircularCosineSquared<stkobjects/AntennaModelApertureCircularCosineSquared>
     AntennaModelApertureCircularCosineSquaredPedestal<stkobjects/AntennaModelApertureCircularCosineSquaredPedestal>
     AntennaModelApertureCircularSincIntegerPower<stkobjects/AntennaModelApertureCircularSincIntegerPower>
     AntennaModelApertureCircularSincRealPower<stkobjects/AntennaModelApertureCircularSincRealPower>
     AntennaModelApertureCircularUniform<stkobjects/AntennaModelApertureCircularUniform>
     AntennaModelApertureRectangularCosine<stkobjects/AntennaModelApertureRectangularCosine>
     AntennaModelApertureRectangularCosinePedestal<stkobjects/AntennaModelApertureRectangularCosinePedestal>
     AntennaModelApertureRectangularCosineSquared<stkobjects/AntennaModelApertureRectangularCosineSquared>
     AntennaModelApertureRectangularCosineSquaredPedestal<stkobjects/AntennaModelApertureRectangularCosineSquaredPedestal>
     AntennaModelApertureRectangularSincIntegerPower<stkobjects/AntennaModelApertureRectangularSincIntegerPower>
     AntennaModelApertureRectangularSincRealPower<stkobjects/AntennaModelApertureRectangularSincRealPower>
     AntennaModelApertureRectangularUniform<stkobjects/AntennaModelApertureRectangularUniform>
     AntennaModelCosecantSquared<stkobjects/AntennaModelCosecantSquared>
     AntennaModelDipole<stkobjects/AntennaModelDipole>
     AntennaModelElevationAzimuthCuts<stkobjects/AntennaModelElevationAzimuthCuts>
     AntennaModelExternal<stkobjects/AntennaModelExternal>
     AntennaModelGaussian<stkobjects/AntennaModelGaussian>
     AntennaModelGIMROC<stkobjects/AntennaModelGIMROC>
     AntennaModelGPSFRPA<stkobjects/AntennaModelGPSFRPA>
     AntennaModelGPSGlobal<stkobjects/AntennaModelGPSGlobal>
     AntennaModelHelix<stkobjects/AntennaModelHelix>
     AntennaModelHemispherical<stkobjects/AntennaModelHemispherical>
     AntennaModelHfssEepArray<stkobjects/AntennaModelHfssEepArray>
     AntennaModelIEEE1979<stkobjects/AntennaModelIEEE1979>
     AntennaModelIntelSat<stkobjects/AntennaModelIntelSat>
     AntennaModelIsotropic<stkobjects/AntennaModelIsotropic>
     AntennaModelITUBO1213CoPolar<stkobjects/AntennaModelITUBO1213CoPolar>
     AntennaModelITUBO1213CrossPolar<stkobjects/AntennaModelITUBO1213CrossPolar>
     AntennaModelITUF1245<stkobjects/AntennaModelITUF1245>
     AntennaModelITUS1528R12Circular<stkobjects/AntennaModelITUS1528R12Circular>
     AntennaModelITUS1528R12Rectangular<stkobjects/AntennaModelITUS1528R12Rectangular>
     AntennaModelITUS1528R13<stkobjects/AntennaModelITUS1528R13>
     AntennaModelITUS465<stkobjects/AntennaModelITUS465>
     AntennaModelITUS580<stkobjects/AntennaModelITUS580>
     AntennaModelITUS672Circular<stkobjects/AntennaModelITUS672Circular>
     AntennaModelITUS672Rectangular<stkobjects/AntennaModelITUS672Rectangular>
     AntennaModelITUS731<stkobjects/AntennaModelITUS731>
     AntennaModelOpticalGaussian<stkobjects/AntennaModelOpticalGaussian>
     AntennaModelOpticalSimple<stkobjects/AntennaModelOpticalSimple>
     AntennaModelParabolic<stkobjects/AntennaModelParabolic>
     AntennaModelPencilBeam<stkobjects/AntennaModelPencilBeam>
     AntennaModelPhasedArray<stkobjects/AntennaModelPhasedArray>
     AntennaModelRectangularPattern<stkobjects/AntennaModelRectangularPattern>
     AntennaModelRemcomUanFormat<stkobjects/AntennaModelRemcomUanFormat>
     AntennaModelScriptPlugin<stkobjects/AntennaModelScriptPlugin>
     AntennaModelSquareHorn<stkobjects/AntennaModelSquareHorn>
     AntennaModelTicraGRASPFormat<stkobjects/AntennaModelTicraGRASPFormat>
     AntennaNoiseTemperature<stkobjects/AntennaNoiseTemperature>
     AntennaSystem<stkobjects/AntennaSystem>
     AntennaVolumeGraphics<stkobjects/AntennaVolumeGraphics>
     AntennaVolumeLevel<stkobjects/AntennaVolumeLevel>
     AntennaVolumeLevelCollection<stkobjects/AntennaVolumeLevelCollection>
     AreaTarget<stkobjects/AreaTarget>
     AreaTargetCommonTasks<stkobjects/AreaTargetCommonTasks>
     AreaTargetGraphics<stkobjects/AreaTargetGraphics>
     AreaTargetGraphics3D<stkobjects/AreaTargetGraphics3D>
     AreaTypeEllipse<stkobjects/AreaTypeEllipse>
     AreaTypePattern<stkobjects/AreaTypePattern>
     AreaTypePatternCollection<stkobjects/AreaTypePatternCollection>
     Atmosphere<stkobjects/Atmosphere>
     AtmosphericAbsorptionModel<stkobjects/AtmosphericAbsorptionModel>
     AtmosphericAbsorptionModelCOMPlugin<stkobjects/AtmosphericAbsorptionModelCOMPlugin>
     AtmosphericAbsorptionModelGraphics3DACAP<stkobjects/AtmosphericAbsorptionModelGraphics3DACAP>
     AtmosphericAbsorptionModelITURP676Version13<stkobjects/AtmosphericAbsorptionModelITURP676Version13>
     AtmosphericAbsorptionModelITURP676Version9<stkobjects/AtmosphericAbsorptionModelITURP676Version9>
     AtmosphericAbsorptionModelScriptPlugin<stkobjects/AtmosphericAbsorptionModelScriptPlugin>
     AtmosphericAbsorptionModelSimpleSatcom<stkobjects/AtmosphericAbsorptionModelSimpleSatcom>
     AtmosphericAbsorptionModelTIREM320<stkobjects/AtmosphericAbsorptionModelTIREM320>
     AtmosphericAbsorptionModelTIREM331<stkobjects/AtmosphericAbsorptionModelTIREM331>
     AtmosphericAbsorptionModelTIREM550<stkobjects/AtmosphericAbsorptionModelTIREM550>
     AtmosphericTurbulenceModel<stkobjects/AtmosphericTurbulenceModel>
     AtmosphericTurbulenceModelConstant<stkobjects/AtmosphericTurbulenceModelConstant>
     AtmosphericTurbulenceModelHufnagelValley<stkobjects/AtmosphericTurbulenceModelHufnagelValley>
     AttitudeProfileAlignedAndConstrained<stkobjects/AttitudeProfileAlignedAndConstrained>
     AttitudeProfileAlignmentOffset<stkobjects/AttitudeProfileAlignmentOffset>
     AttitudeProfileAviator<stkobjects/AttitudeProfileAviator>
     AttitudeProfileConstraintOffset<stkobjects/AttitudeProfileConstraintOffset>
     AttitudeProfileCoordinatedTurn<stkobjects/AttitudeProfileCoordinatedTurn>
     AttitudeProfileFixedInAxes<stkobjects/AttitudeProfileFixedInAxes>
     AttitudeProfileGPS<stkobjects/AttitudeProfileGPS>
     AttitudeProfileInertial<stkobjects/AttitudeProfileInertial>
     AttitudeProfilePrecessingSpin<stkobjects/AttitudeProfilePrecessingSpin>
     AttitudeProfileSpinAboutSettings<stkobjects/AttitudeProfileSpinAboutSettings>
     AttitudeProfileSpinning<stkobjects/AttitudeProfileSpinning>
     AttitudeProfileYawToNadir<stkobjects/AttitudeProfileYawToNadir>
     AttitudeScheduleTimesCollection<stkobjects/AttitudeScheduleTimesCollection>
     AttitudeScheduleTimesElement<stkobjects/AttitudeScheduleTimesElement>
     AttitudeStandardBasic<stkobjects/AttitudeStandardBasic>
     AttitudeStandardOrbit<stkobjects/AttitudeStandardOrbit>
     AttitudeStandardRoute<stkobjects/AttitudeStandardRoute>
     AttitudeStandardTrajectory<stkobjects/AttitudeStandardTrajectory>
     AttitudeTorque<stkobjects/AttitudeTorque>
     AvailableFeatures<stkobjects/AvailableFeatures>
     BasicAzElMask<stkobjects/BasicAzElMask>
     Beamformer<stkobjects/Beamformer>
     BeamformerASCIIFile<stkobjects/BeamformerASCIIFile>
     BeamformerBlackmanHarris<stkobjects/BeamformerBlackmanHarris>
     BeamformerCosine<stkobjects/BeamformerCosine>
     BeamformerCosineX<stkobjects/BeamformerCosineX>
     BeamformerCustomTaperFile<stkobjects/BeamformerCustomTaperFile>
     BeamformerDolphChebyshev<stkobjects/BeamformerDolphChebyshev>
     BeamformerHamming<stkobjects/BeamformerHamming>
     BeamformerHann<stkobjects/BeamformerHann>
     BeamformerMVDR<stkobjects/BeamformerMVDR>
     BeamformerRaisedCosine<stkobjects/BeamformerRaisedCosine>
     BeamformerRaisedCosineSquared<stkobjects/BeamformerRaisedCosineSquared>
     BeamformerScript<stkobjects/BeamformerScript>
     BeamformerTaylor<stkobjects/BeamformerTaylor>
     BeamformerUniform<stkobjects/BeamformerUniform>
     BeerBouguerLambertLawLayer<stkobjects/BeerBouguerLambertLawLayer>
     BeerBouguerLambertLawLayerCollection<stkobjects/BeerBouguerLambertLawLayerCollection>
     CentralBody<stkobjects/CentralBody>
     CentralBodyCollection<stkobjects/CentralBodyCollection>
     CentralBodyEllipsoid<stkobjects/CentralBodyEllipsoid>
     CentralBodyTerrainCollection<stkobjects/CentralBodyTerrainCollection>
     CentralBodyTerrainCollectionElement<stkobjects/CentralBodyTerrainCollectionElement>
     Chain<stkobjects/Chain>
     ChainConnection<stkobjects/ChainConnection>
     ChainConnectionCollection<stkobjects/ChainConnectionCollection>
     ChainConstraints<stkobjects/ChainConstraints>
     ChainGraphics<stkobjects/ChainGraphics>
     ChainGraphics2DAnimation<stkobjects/ChainGraphics2DAnimation>
     ChainGraphics2DStatic<stkobjects/ChainGraphics2DStatic>
     ChainGraphics3D<stkobjects/ChainGraphics3D>
     ChainOptimalStrandOpts<stkobjects/ChainOptimalStrandOpts>
     ChainTimePeriod<stkobjects/ChainTimePeriod>
     ChainUserSpecifiedTimePeriod<stkobjects/ChainUserSpecifiedTimePeriod>
     ClassicalLocationArgumentOfLatitude<stkobjects/ClassicalLocationArgumentOfLatitude>
     ClassicalLocationEccentricAnomaly<stkobjects/ClassicalLocationEccentricAnomaly>
     ClassicalLocationMeanAnomaly<stkobjects/ClassicalLocationMeanAnomaly>
     ClassicalLocationTimePastAscendingNode<stkobjects/ClassicalLocationTimePastAscendingNode>
     ClassicalLocationTimePastPerigee<stkobjects/ClassicalLocationTimePastPerigee>
     ClassicalLocationTrueAnomaly<stkobjects/ClassicalLocationTrueAnomaly>
     ClassicalOrientation<stkobjects/ClassicalOrientation>
     ClassicalSizeShapeAltitude<stkobjects/ClassicalSizeShapeAltitude>
     ClassicalSizeShapeMeanMotion<stkobjects/ClassicalSizeShapeMeanMotion>
     ClassicalSizeShapePeriod<stkobjects/ClassicalSizeShapePeriod>
     ClassicalSizeShapeRadius<stkobjects/ClassicalSizeShapeRadius>
     ClassicalSizeShapeSemimajorAxis<stkobjects/ClassicalSizeShapeSemimajorAxis>
     CloudsAndFogFadingLossModel<stkobjects/CloudsAndFogFadingLossModel>
     CloudsAndFogFadingLossModelP840Version6<stkobjects/CloudsAndFogFadingLossModelP840Version6>
     CloudsAndFogFadingLossModelP840Version7<stkobjects/CloudsAndFogFadingLossModelP840Version7>
     CommRadCartesianLocation<stkobjects/CommRadCartesianLocation>
     CommRadComplexNumber<stkobjects/CommRadComplexNumber>
     CommRadComplexNumberCollection<stkobjects/CommRadComplexNumberCollection>
     CommRadPluginConfiguration<stkobjects/CommRadPluginConfiguration>
     CommSystem<stkobjects/CommSystem>
     CommSystemAccessEventDetection<stkobjects/CommSystemAccessEventDetection>
     CommSystemAccessEventDetectionSamplesOnly<stkobjects/CommSystemAccessEventDetectionSamplesOnly>
     CommSystemAccessEventDetectionSubsample<stkobjects/CommSystemAccessEventDetectionSubsample>
     CommSystemAccessOptions<stkobjects/CommSystemAccessOptions>
     CommSystemAccessSamplingMethod<stkobjects/CommSystemAccessSamplingMethod>
     CommSystemAccessSamplingMethodAdaptive<stkobjects/CommSystemAccessSamplingMethodAdaptive>
     CommSystemAccessSamplingMethodFixed<stkobjects/CommSystemAccessSamplingMethodFixed>
     CommSystemGraphics<stkobjects/CommSystemGraphics>
     CommSystemGraphics3D<stkobjects/CommSystemGraphics3D>
     CommSystemLinkSelectionCriteria<stkobjects/CommSystemLinkSelectionCriteria>
     CommSystemLinkSelectionCriteriaMaximumElevation<stkobjects/CommSystemLinkSelectionCriteriaMaximumElevation>
     CommSystemLinkSelectionCriteriaMinimumRange<stkobjects/CommSystemLinkSelectionCriteriaMinimumRange>
     CommSystemLinkSelectionCriteriaScriptPlugin<stkobjects/CommSystemLinkSelectionCriteriaScriptPlugin>
     ComponentAttrLinkEmbedControl<stkobjects/ComponentAttrLinkEmbedControl>
     ComponentDirectory<stkobjects/ComponentDirectory>
     ComponentInfo<stkobjects/ComponentInfo>
     ComponentInfoCollection<stkobjects/ComponentInfoCollection>
     Constellation<stkobjects/Constellation>
     ConstellationConstraintObjectRestriction<stkobjects/ConstellationConstraintObjectRestriction>
     ConstellationConstraintRestriction<stkobjects/ConstellationConstraintRestriction>
     ConstellationConstraints<stkobjects/ConstellationConstraints>
     ConstellationGraphics<stkobjects/ConstellationGraphics>
     ConstellationRouting<stkobjects/ConstellationRouting>
     CoverageAdvancedSettings<stkobjects/CoverageAdvancedSettings>
     CoverageAreaTargetsCollection<stkobjects/CoverageAreaTargetsCollection>
     CoverageAssetListCollection<stkobjects/CoverageAssetListCollection>
     CoverageAssetListElement<stkobjects/CoverageAssetListElement>
     CoverageBoundsCustomBoundary<stkobjects/CoverageBoundsCustomBoundary>
     CoverageBoundsCustomRegions<stkobjects/CoverageBoundsCustomRegions>
     CoverageBoundsGlobal<stkobjects/CoverageBoundsGlobal>
     CoverageBoundsLatitude<stkobjects/CoverageBoundsLatitude>
     CoverageBoundsLatitudeLine<stkobjects/CoverageBoundsLatitudeLine>
     CoverageBoundsLatitudeLongitudeRegion<stkobjects/CoverageBoundsLatitudeLongitudeRegion>
     CoverageBoundsLongitudeLine<stkobjects/CoverageBoundsLongitudeLine>
     CoverageDefinition<stkobjects/CoverageDefinition>
     CoverageEllipse<stkobjects/CoverageEllipse>
     CoverageEllipseCollection<stkobjects/CoverageEllipseCollection>
     CoverageGraphics<stkobjects/CoverageGraphics>
     CoverageGraphics2DAnimation<stkobjects/CoverageGraphics2DAnimation>
     CoverageGraphics2DProgress<stkobjects/CoverageGraphics2DProgress>
     CoverageGraphics2DStatic<stkobjects/CoverageGraphics2DStatic>
     CoverageGraphics3D<stkobjects/CoverageGraphics3D>
     CoverageGraphics3DAttributes<stkobjects/CoverageGraphics3DAttributes>
     CoverageGrid<stkobjects/CoverageGrid>
     CoverageGridInspector<stkobjects/CoverageGridInspector>
     CoverageGridPointSelection<stkobjects/CoverageGridPointSelection>
     CoverageInterval<stkobjects/CoverageInterval>
     CoverageLatLonBox<stkobjects/CoverageLatLonBox>
     CoverageLatLonBoxCollection<stkobjects/CoverageLatLonBoxCollection>
     CoveragePointDefinition<stkobjects/CoveragePointDefinition>
     CoveragePointFileListCollection<stkobjects/CoveragePointFileListCollection>
     CoverageRegionFilesCollection<stkobjects/CoverageRegionFilesCollection>
     CoverageResolutionArea<stkobjects/CoverageResolutionArea>
     CoverageResolutionDistance<stkobjects/CoverageResolutionDistance>
     CoverageResolutionLatLon<stkobjects/CoverageResolutionLatLon>
     CoverageSelectedGridPoint<stkobjects/CoverageSelectedGridPoint>
     CustomPropagationModel<stkobjects/CustomPropagationModel>
     DataProviderCollection<stkobjects/DataProviderCollection>
     DataProviderElement<stkobjects/DataProviderElement>
     DataProviderElements<stkobjects/DataProviderElements>
     DataProviderFixed<stkobjects/DataProviderFixed>
     DataProviderGroup<stkobjects/DataProviderGroup>
     DataProviderInterval<stkobjects/DataProviderInterval>
     DataProviderResult<stkobjects/DataProviderResult>
     DataProviderResultDataSet<stkobjects/DataProviderResultDataSet>
     DataProviderResultDataSetCollection<stkobjects/DataProviderResultDataSetCollection>
     DataProviderResultInterval<stkobjects/DataProviderResultInterval>
     DataProviderResultIntervalCollection<stkobjects/DataProviderResultIntervalCollection>
     DataProviderResultStatisticResult<stkobjects/DataProviderResultStatisticResult>
     DataProviderResultStatistics<stkobjects/DataProviderResultStatistics>
     DataProviderResultSubSection<stkobjects/DataProviderResultSubSection>
     DataProviderResultSubSectionCollection<stkobjects/DataProviderResultSubSectionCollection>
     DataProviderResultTextMessage<stkobjects/DataProviderResultTextMessage>
     DataProviderResultTimeArrayElements<stkobjects/DataProviderResultTimeArrayElements>
     DataProviderResultTimeVaryingExtremumResult<stkobjects/DataProviderResultTimeVaryingExtremumResult>
     DataProviders<stkobjects/DataProviders>
     DataProviderTimeVarying<stkobjects/DataProviderTimeVarying>
     DelaunayG<stkobjects/DelaunayG>
     DelaunayGOverSQRTmu<stkobjects/DelaunayGOverSQRTmu>
     DelaunayH<stkobjects/DelaunayH>
     DelaunayHOverSQRTmu<stkobjects/DelaunayHOverSQRTmu>
     DelaunayL<stkobjects/DelaunayL>
     DelaunayLOverSQRTmu<stkobjects/DelaunayLOverSQRTmu>
     DemodulatorModel<stkobjects/DemodulatorModel>
     DemodulatorModel16PSK<stkobjects/DemodulatorModel16PSK>
     DemodulatorModel8PSK<stkobjects/DemodulatorModel8PSK>
     DemodulatorModelBOC<stkobjects/DemodulatorModelBOC>
     DemodulatorModelBPSK<stkobjects/DemodulatorModelBPSK>
     DemodulatorModelDPSK<stkobjects/DemodulatorModelDPSK>
     DemodulatorModelExternal<stkobjects/DemodulatorModelExternal>
     DemodulatorModelExternalSource<stkobjects/DemodulatorModelExternalSource>
     DemodulatorModelFSK<stkobjects/DemodulatorModelFSK>
     DemodulatorModelMSK<stkobjects/DemodulatorModelMSK>
     DemodulatorModelNarrowbandUniform<stkobjects/DemodulatorModelNarrowbandUniform>
     DemodulatorModelNFSK<stkobjects/DemodulatorModelNFSK>
     DemodulatorModelOQPSK<stkobjects/DemodulatorModelOQPSK>
     DemodulatorModelPulsedSignal<stkobjects/DemodulatorModelPulsedSignal>
     DemodulatorModelQAM1024<stkobjects/DemodulatorModelQAM1024>
     DemodulatorModelQAM128<stkobjects/DemodulatorModelQAM128>
     DemodulatorModelQAM16<stkobjects/DemodulatorModelQAM16>
     DemodulatorModelQAM256<stkobjects/DemodulatorModelQAM256>
     DemodulatorModelQAM32<stkobjects/DemodulatorModelQAM32>
     DemodulatorModelQAM64<stkobjects/DemodulatorModelQAM64>
     DemodulatorModelQPSK<stkobjects/DemodulatorModelQPSK>
     DemodulatorModelScriptPlugin<stkobjects/DemodulatorModelScriptPlugin>
     DemodulatorModelWidebandGaussian<stkobjects/DemodulatorModelWidebandGaussian>
     DemodulatorModelWidebandUniform<stkobjects/DemodulatorModelWidebandUniform>
     DeticSizeAltitude<stkobjects/DeticSizeAltitude>
     DeticSizeRadius<stkobjects/DeticSizeRadius>
     DirectionProvider<stkobjects/DirectionProvider>
     DirectionProviderASCIIFile<stkobjects/DirectionProviderASCIIFile>
     DirectionProviderLink<stkobjects/DirectionProviderLink>
     DirectionProviderObject<stkobjects/DirectionProviderObject>
     DirectionProviderScript<stkobjects/DirectionProviderScript>
     DisplayTimesDuringAccess<stkobjects/DisplayTimesDuringAccess>
     DisplayTimesTimeComponent<stkobjects/DisplayTimesTimeComponent>
     Element<stkobjects/Element>
     ElementCollection<stkobjects/ElementCollection>
     ElementConfiguration<stkobjects/ElementConfiguration>
     ElementConfigurationASCIIFile<stkobjects/ElementConfigurationASCIIFile>
     ElementConfigurationCircular<stkobjects/ElementConfigurationCircular>
     ElementConfigurationHexagon<stkobjects/ElementConfigurationHexagon>
     ElementConfigurationHfssEepFile<stkobjects/ElementConfigurationHfssEepFile>
     ElementConfigurationLinear<stkobjects/ElementConfigurationLinear>
     ElementConfigurationPolygon<stkobjects/ElementConfigurationPolygon>
     EOIR<stkobjects/EOIR>
     EOIRMaterialElement<stkobjects/EOIRMaterialElement>
     EOIRMaterialElementCollection<stkobjects/EOIRMaterialElementCollection>
     EOIRShape<stkobjects/EOIRShape>
     EOIRShapeBox<stkobjects/EOIRShapeBox>
     EOIRShapeCollection<stkobjects/EOIRShapeCollection>
     EOIRShapeCone<stkobjects/EOIRShapeCone>
     EOIRShapeCoupler<stkobjects/EOIRShapeCoupler>
     EOIRShapeCustomMesh<stkobjects/EOIRShapeCustomMesh>
     EOIRShapeCylinder<stkobjects/EOIRShapeCylinder>
     EOIRShapeGEOComm<stkobjects/EOIRShapeGEOComm>
     EOIRShapeLEOComm<stkobjects/EOIRShapeLEOComm>
     EOIRShapeLEOImaging<stkobjects/EOIRShapeLEOImaging>
     EOIRShapeNone<stkobjects/EOIRShapeNone>
     EOIRShapeObject<stkobjects/EOIRShapeObject>
     EOIRShapePlate<stkobjects/EOIRShapePlate>
     EOIRShapeSphere<stkobjects/EOIRShapeSphere>
     EOIRShapeTargetSignature<stkobjects/EOIRShapeTargetSignature>
     EOIRStage<stkobjects/EOIRStage>
     EOIRStagePlume<stkobjects/EOIRStagePlume>
     EquinoctialSizeShapeMeanMotion<stkobjects/EquinoctialSizeShapeMeanMotion>
     EquinoctialSizeShapeSemimajorAxis<stkobjects/EquinoctialSizeShapeSemimajorAxis>
     EventDetectionNoSubSampling<stkobjects/EventDetectionNoSubSampling>
     EventDetectionSubSampling<stkobjects/EventDetectionSubSampling>
     ExportToolStepSize<stkobjects/ExportToolStepSize>
     ExportToolTimePeriod<stkobjects/ExportToolTimePeriod>
     Facility<stkobjects/Facility>
     FacilityGraphics<stkobjects/FacilityGraphics>
     FacilityGraphics3D<stkobjects/FacilityGraphics3D>
     FigureOfMerit<stkobjects/FigureOfMerit>
     FigureOfMeritAssetListCollection<stkobjects/FigureOfMeritAssetListCollection>
     FigureOfMeritAssetListElement<stkobjects/FigureOfMeritAssetListElement>
     FigureOfMeritDefinitionAccessConstraint<stkobjects/FigureOfMeritDefinitionAccessConstraint>
     FigureOfMeritDefinitionAccessSeparation<stkobjects/FigureOfMeritDefinitionAccessSeparation>
     FigureOfMeritDefinitionAgeOfData<stkobjects/FigureOfMeritDefinitionAgeOfData>
     FigureOfMeritDefinitionCompute<stkobjects/FigureOfMeritDefinitionCompute>
     FigureOfMeritDefinitionDataBest4<stkobjects/FigureOfMeritDefinitionDataBest4>
     FigureOfMeritDefinitionDataBestN<stkobjects/FigureOfMeritDefinitionDataBestN>
     FigureOfMeritDefinitionDataMinimumMaximum<stkobjects/FigureOfMeritDefinitionDataMinimumMaximum>
     FigureOfMeritDefinitionDataMinimumNumberOfAssets<stkobjects/FigureOfMeritDefinitionDataMinimumNumberOfAssets>
     FigureOfMeritDefinitionDataPercentLevel<stkobjects/FigureOfMeritDefinitionDataPercentLevel>
     FigureOfMeritDefinitionDilutionOfPrecision<stkobjects/FigureOfMeritDefinitionDilutionOfPrecision>
     FigureOfMeritDefinitionNavigationAccuracy<stkobjects/FigureOfMeritDefinitionNavigationAccuracy>
     FigureOfMeritDefinitionResponseTime<stkobjects/FigureOfMeritDefinitionResponseTime>
     FigureOfMeritDefinitionRevisitTime<stkobjects/FigureOfMeritDefinitionRevisitTime>
     FigureOfMeritDefinitionScalarCalculation<stkobjects/FigureOfMeritDefinitionScalarCalculation>
     FigureOfMeritDefinitionSimpleCoverage<stkobjects/FigureOfMeritDefinitionSimpleCoverage>
     FigureOfMeritDefinitionSystemAgeOfData<stkobjects/FigureOfMeritDefinitionSystemAgeOfData>
     FigureOfMeritDefinitionSystemResponseTime<stkobjects/FigureOfMeritDefinitionSystemResponseTime>
     FigureOfMeritDefinitionTimeAverageGap<stkobjects/FigureOfMeritDefinitionTimeAverageGap>
     FigureOfMeritGraphics<stkobjects/FigureOfMeritGraphics>
     FigureOfMeritGraphics2DAttributes<stkobjects/FigureOfMeritGraphics2DAttributes>
     FigureOfMeritGraphics2DAttributesAnimation<stkobjects/FigureOfMeritGraphics2DAttributesAnimation>
     FigureOfMeritGraphics2DColorOptions<stkobjects/FigureOfMeritGraphics2DColorOptions>
     FigureOfMeritGraphics2DContours<stkobjects/FigureOfMeritGraphics2DContours>
     FigureOfMeritGraphics2DContoursAnimation<stkobjects/FigureOfMeritGraphics2DContoursAnimation>
     FigureOfMeritGraphics2DLegend<stkobjects/FigureOfMeritGraphics2DLegend>
     FigureOfMeritGraphics2DLegendWindow<stkobjects/FigureOfMeritGraphics2DLegendWindow>
     FigureOfMeritGraphics2DLevelAttributesCollection<stkobjects/FigureOfMeritGraphics2DLevelAttributesCollection>
     FigureOfMeritGraphics2DLevelAttributesElement<stkobjects/FigureOfMeritGraphics2DLevelAttributesElement>
     FigureOfMeritGraphics2DPositionOnMap<stkobjects/FigureOfMeritGraphics2DPositionOnMap>
     FigureOfMeritGraphics2DRampColor<stkobjects/FigureOfMeritGraphics2DRampColor>
     FigureOfMeritGraphics2DRangeColorOptions<stkobjects/FigureOfMeritGraphics2DRangeColorOptions>
     FigureOfMeritGraphics2DTextOptions<stkobjects/FigureOfMeritGraphics2DTextOptions>
     FigureOfMeritGraphics3D<stkobjects/FigureOfMeritGraphics3D>
     FigureOfMeritGraphics3DAttributes<stkobjects/FigureOfMeritGraphics3DAttributes>
     FigureOfMeritGraphics3DLegendWindow<stkobjects/FigureOfMeritGraphics3DLegendWindow>
     FigureOfMeritGridInspector<stkobjects/FigureOfMeritGridInspector>
     FigureOfMeritNavigationAccuracyMethodConstant<stkobjects/FigureOfMeritNavigationAccuracyMethodConstant>
     FigureOfMeritNavigationAccuracyMethodElevationAngle<stkobjects/FigureOfMeritNavigationAccuracyMethodElevationAngle>
     FigureOfMeritSatisfaction<stkobjects/FigureOfMeritSatisfaction>
     FigureOfMeritUncertainties<stkobjects/FigureOfMeritUncertainties>
     Graphics2DRangeContours<stkobjects/Graphics2DRangeContours>
     Graphics3DArticulationFile<stkobjects/Graphics3DArticulationFile>
     Graphics3DAzElMask<stkobjects/Graphics3DAzElMask>
     Graphics3DBorderWall<stkobjects/Graphics3DBorderWall>
     Graphics3DDataDisplayCollection<stkobjects/Graphics3DDataDisplayCollection>
     Graphics3DDataDisplayElement<stkobjects/Graphics3DDataDisplayElement>
     Graphics3DDetailThreshold<stkobjects/Graphics3DDetailThreshold>
     Graphics3DLabelSwapDistance<stkobjects/Graphics3DLabelSwapDistance>
     Graphics3DMarker<stkobjects/Graphics3DMarker>
     Graphics3DMarkerFile<stkobjects/Graphics3DMarkerFile>
     Graphics3DMarkerShape<stkobjects/Graphics3DMarkerShape>
     Graphics3DModelArticulation<stkobjects/Graphics3DModelArticulation>
     Graphics3DModelCollection<stkobjects/Graphics3DModelCollection>
     Graphics3DModelFile<stkobjects/Graphics3DModelFile>
     Graphics3DModelglTFImageBased<stkobjects/Graphics3DModelglTFImageBased>
     Graphics3DModelItem<stkobjects/Graphics3DModelItem>
     Graphics3DModelPointing<stkobjects/Graphics3DModelPointing>
     Graphics3DModelTransformation<stkobjects/Graphics3DModelTransformation>
     Graphics3DModelTransformationCollection<stkobjects/Graphics3DModelTransformationCollection>
     Graphics3DOffset<stkobjects/Graphics3DOffset>
     Graphics3DOffsetAttachment<stkobjects/Graphics3DOffsetAttachment>
     Graphics3DOffsetLabel<stkobjects/Graphics3DOffsetLabel>
     Graphics3DOffsetRotate<stkobjects/Graphics3DOffsetRotate>
     Graphics3DOffsetTransformation<stkobjects/Graphics3DOffsetTransformation>
     Graphics3DPointableElementsCollection<stkobjects/Graphics3DPointableElementsCollection>
     Graphics3DPointableElementsElement<stkobjects/Graphics3DPointableElementsElement>
     Graphics3DRangeContours<stkobjects/Graphics3DRangeContours>
     Graphics3DReferenceAngle<stkobjects/Graphics3DReferenceAngle>
     Graphics3DReferenceAxes<stkobjects/Graphics3DReferenceAxes>
     Graphics3DReferencePlane<stkobjects/Graphics3DReferencePlane>
     Graphics3DReferencePoint<stkobjects/Graphics3DReferencePoint>
     Graphics3DReferenceVector<stkobjects/Graphics3DReferenceVector>
     Graphics3DReferenceVectorGeometryToolComponentCollection<stkobjects/Graphics3DReferenceVectorGeometryToolComponentCollection>
     Graphics3DVaporTrail<stkobjects/Graphics3DVaporTrail>
     Graphics3DVector<stkobjects/Graphics3DVector>
     GroundVehicle<stkobjects/GroundVehicle>
     GroundVehicleExportTools<stkobjects/GroundVehicleExportTools>
     GroundVehicleGraphics<stkobjects/GroundVehicleGraphics>
     GroundVehicleGraphics3D<stkobjects/GroundVehicleGraphics3D>
     IntegratorStepSizeControl<stkobjects/IntegratorStepSizeControl>
     IntegratorTimeRegularization<stkobjects/IntegratorTimeRegularization>
     IonosphericFadingLossModel<stkobjects/IonosphericFadingLossModel>
     IonosphericFadingLossModelP531Version13<stkobjects/IonosphericFadingLossModelP531Version13>
     KeyValueCollection<stkobjects/KeyValueCollection>
     LabelNote<stkobjects/LabelNote>
     LabelNoteCollection<stkobjects/LabelNoteCollection>
     LaserAtmosphericLossModel<stkobjects/LaserAtmosphericLossModel>
     LaserAtmosphericLossModelBeerBouguerLambertLaw<stkobjects/LaserAtmosphericLossModelBeerBouguerLambertLaw>
     LaserEnvironment<stkobjects/LaserEnvironment>
     LaserPropagationLossModels<stkobjects/LaserPropagationLossModels>
     LaserTroposphericScintillationLossModel<stkobjects/LaserTroposphericScintillationLossModel>
     LaserTroposphericScintillationLossModelITURP1814<stkobjects/LaserTroposphericScintillationLossModelITURP1814>
     LatitudeLongitudeAltitudeCentric<stkobjects/LatitudeLongitudeAltitudeCentric>
     LatitudeLongitudeAltitudeDetic<stkobjects/LatitudeLongitudeAltitudeDetic>
     LatitudeLongitudeAltitudePosition<stkobjects/LatitudeLongitudeAltitudePosition>
     LaunchVehicle<stkobjects/LaunchVehicle>
     LaunchVehicleControlFixedApogeeAltitude<stkobjects/LaunchVehicleControlFixedApogeeAltitude>
     LaunchVehicleControlFixedDeltaV<stkobjects/LaunchVehicleControlFixedDeltaV>
     LaunchVehicleControlFixedDeltaVMinimumEccentricity<stkobjects/LaunchVehicleControlFixedDeltaVMinimumEccentricity>
     LaunchVehicleControlFixedTimeOfFlight<stkobjects/LaunchVehicleControlFixedTimeOfFlight>
     LaunchVehicleExportTools<stkobjects/LaunchVehicleExportTools>
     LaunchVehicleGraphics<stkobjects/LaunchVehicleGraphics>
     LaunchVehicleGraphics3D<stkobjects/LaunchVehicleGraphics3D>
     LaunchVehicleInitialState<stkobjects/LaunchVehicleInitialState>
     LaunchVehicleLocationCentric<stkobjects/LaunchVehicleLocationCentric>
     LaunchVehicleLocationDetic<stkobjects/LaunchVehicleLocationDetic>
     LevelAttribute<stkobjects/LevelAttribute>
     LevelAttributeCollection<stkobjects/LevelAttributeCollection>
     LineTarget<stkobjects/LineTarget>
     LineTargetGraphics<stkobjects/LineTargetGraphics>
     LineTargetGraphics3D<stkobjects/LineTargetGraphics3D>
     LineTargetPoint<stkobjects/LineTargetPoint>
     LineTargetPointCollection<stkobjects/LineTargetPointCollection>
     LinkMargin<stkobjects/LinkMargin>
     LinkToObject<stkobjects/LinkToObject>
     LocationVectorGeometryToolPoint<stkobjects/LocationVectorGeometryToolPoint>
     MilitaryStandard2525bSymbols<stkobjects/MilitaryStandard2525bSymbols>
     Missile<stkobjects/Missile>
     MissileEOIR<stkobjects/MissileEOIR>
     MissileExportTools<stkobjects/MissileExportTools>
     MissileGraphics<stkobjects/MissileGraphics>
     MissileGraphics3D<stkobjects/MissileGraphics3D>
     MixedSphericalFlightPathAngleHorizontal<stkobjects/MixedSphericalFlightPathAngleHorizontal>
     MixedSphericalFlightPathAngleVertical<stkobjects/MixedSphericalFlightPathAngleVertical>
     MODTRANLookupTablePropagationModel<stkobjects/MODTRANLookupTablePropagationModel>
     MODTRANPropagationModel<stkobjects/MODTRANPropagationModel>
     ModulatorModel<stkobjects/ModulatorModel>
     ModulatorModel16PSK<stkobjects/ModulatorModel16PSK>
     ModulatorModel8PSK<stkobjects/ModulatorModel8PSK>
     ModulatorModelBOC<stkobjects/ModulatorModelBOC>
     ModulatorModelBPSK<stkobjects/ModulatorModelBPSK>
     ModulatorModelDPSK<stkobjects/ModulatorModelDPSK>
     ModulatorModelExternal<stkobjects/ModulatorModelExternal>
     ModulatorModelExternalSource<stkobjects/ModulatorModelExternalSource>
     ModulatorModelFSK<stkobjects/ModulatorModelFSK>
     ModulatorModelMSK<stkobjects/ModulatorModelMSK>
     ModulatorModelNarrowbandUniform<stkobjects/ModulatorModelNarrowbandUniform>
     ModulatorModelNFSK<stkobjects/ModulatorModelNFSK>
     ModulatorModelOQPSK<stkobjects/ModulatorModelOQPSK>
     ModulatorModelPulsedSignal<stkobjects/ModulatorModelPulsedSignal>
     ModulatorModelQAM1024<stkobjects/ModulatorModelQAM1024>
     ModulatorModelQAM128<stkobjects/ModulatorModelQAM128>
     ModulatorModelQAM16<stkobjects/ModulatorModelQAM16>
     ModulatorModelQAM256<stkobjects/ModulatorModelQAM256>
     ModulatorModelQAM32<stkobjects/ModulatorModelQAM32>
     ModulatorModelQAM64<stkobjects/ModulatorModelQAM64>
     ModulatorModelQPSK<stkobjects/ModulatorModelQPSK>
     ModulatorModelScriptPluginCustomPSD<stkobjects/ModulatorModelScriptPluginCustomPSD>
     ModulatorModelScriptPluginIdealPSD<stkobjects/ModulatorModelScriptPluginIdealPSD>
     ModulatorModelWidebandGaussian<stkobjects/ModulatorModelWidebandGaussian>
     ModulatorModelWidebandUniform<stkobjects/ModulatorModelWidebandUniform>
     MTO<stkobjects/MTO>
     MTOAnalysis<stkobjects/MTOAnalysis>
     MTOAnalysisFieldOfView<stkobjects/MTOAnalysisFieldOfView>
     MTOAnalysisPosition<stkobjects/MTOAnalysisPosition>
     MTOAnalysisRange<stkobjects/MTOAnalysisRange>
     MTOAnalysisVisibility<stkobjects/MTOAnalysisVisibility>
     MTODefaultGraphics2DTrack<stkobjects/MTODefaultGraphics2DTrack>
     MTODefaultGraphics3DTrack<stkobjects/MTODefaultGraphics3DTrack>
     MTODefaultTrack<stkobjects/MTODefaultTrack>
     MTOGlobalTrackOptions<stkobjects/MTOGlobalTrackOptions>
     MTOGraphics<stkobjects/MTOGraphics>
     MTOGraphics2DFadeTimes<stkobjects/MTOGraphics2DFadeTimes>
     MTOGraphics2DGlobalTrackOptions<stkobjects/MTOGraphics2DGlobalTrackOptions>
     MTOGraphics2DLeadTrailTimes<stkobjects/MTOGraphics2DLeadTrailTimes>
     MTOGraphics2DLine<stkobjects/MTOGraphics2DLine>
     MTOGraphics2DMarker<stkobjects/MTOGraphics2DMarker>
     MTOGraphics2DTrack<stkobjects/MTOGraphics2DTrack>
     MTOGraphics2DTrackCollection<stkobjects/MTOGraphics2DTrackCollection>
     MTOGraphics3D<stkobjects/MTOGraphics3D>
     MTOGraphics3DDropLines<stkobjects/MTOGraphics3DDropLines>
     MTOGraphics3DGlobalTrackOptions<stkobjects/MTOGraphics3DGlobalTrackOptions>
     MTOGraphics3DMarker<stkobjects/MTOGraphics3DMarker>
     MTOGraphics3DModel<stkobjects/MTOGraphics3DModel>
     MTOGraphics3DModelArticulation<stkobjects/MTOGraphics3DModelArticulation>
     MTOGraphics3DPoint<stkobjects/MTOGraphics3DPoint>
     MTOGraphics3DSwapDistances<stkobjects/MTOGraphics3DSwapDistances>
     MTOGraphics3DTrack<stkobjects/MTOGraphics3DTrack>
     MTOGraphics3DTrackCollection<stkobjects/MTOGraphics3DTrackCollection>
     MTOTrack<stkobjects/MTOTrack>
     MTOTrackCollection<stkobjects/MTOTrackCollection>
     MTOTrackPoint<stkobjects/MTOTrackPoint>
     MTOTrackPointCollection<stkobjects/MTOTrackPointCollection>
     ObjectCoverage<stkobjects/ObjectCoverage>
     ObjectCoverageFigureOfMerit<stkobjects/ObjectCoverageFigureOfMerit>
     ObjectLaserEnvironment<stkobjects/ObjectLaserEnvironment>
     ObjectLink<stkobjects/ObjectLink>
     ObjectLinkCollection<stkobjects/ObjectLinkCollection>
     ObjectRFEnvironment<stkobjects/ObjectRFEnvironment>
     OceanTides<stkobjects/OceanTides>
     OnePointAccess<stkobjects/OnePointAccess>
     OnePointAccessConstraint<stkobjects/OnePointAccessConstraint>
     OnePointAccessConstraintCollection<stkobjects/OnePointAccessConstraintCollection>
     OnePointAccessResult<stkobjects/OnePointAccessResult>
     OnePointAccessResultCollection<stkobjects/OnePointAccessResultCollection>
     OrbitState<stkobjects/OrbitState>
     OrbitStateCartesian<stkobjects/OrbitStateCartesian>
     OrbitStateClassical<stkobjects/OrbitStateClassical>
     OrbitStateCoordinateSystem<stkobjects/OrbitStateCoordinateSystem>
     OrbitStateDelaunay<stkobjects/OrbitStateDelaunay>
     OrbitStateDetic<stkobjects/OrbitStateDetic>
     OrbitStateEquinoctial<stkobjects/OrbitStateEquinoctial>
     OrbitStateMixedSpherical<stkobjects/OrbitStateMixedSpherical>
     OrbitStateSpherical<stkobjects/OrbitStateSpherical>
     OrientationLongitudeOfAscending<stkobjects/OrientationLongitudeOfAscending>
     OrientationRightAscensionOfAscendingNode<stkobjects/OrientationRightAscensionOfAscendingNode>
     PassBreak<stkobjects/PassBreak>
     PassBreakNumberingDateOfFirstPass<stkobjects/PassBreakNumberingDateOfFirstPass>
     PassBreakNumberingFirstPassNumber<stkobjects/PassBreakNumberingFirstPassNumber>
     PathCollection<stkobjects/PathCollection>
     Place<stkobjects/Place>
     PlaceGraphics<stkobjects/PlaceGraphics>
     PlaceGraphics3D<stkobjects/PlaceGraphics3D>
     Planet<stkobjects/Planet>
     PlanetCommonTasks<stkobjects/PlanetCommonTasks>
     PlanetGraphics<stkobjects/PlanetGraphics>
     PlanetGraphics3D<stkobjects/PlanetGraphics3D>
     PlanetOrbitDisplayTime<stkobjects/PlanetOrbitDisplayTime>
     PlanetPositionCentralBody<stkobjects/PlanetPositionCentralBody>
     PlanetPositionFile<stkobjects/PlanetPositionFile>
     PlatformLaserEnvironment<stkobjects/PlatformLaserEnvironment>
     PointingStrategy<stkobjects/PointingStrategy>
     PointingStrategyFixed<stkobjects/PointingStrategyFixed>
     PointingStrategySpinning<stkobjects/PointingStrategySpinning>
     PointingStrategyTargeted<stkobjects/PointingStrategyTargeted>
     PointTargetGraphics3DModel<stkobjects/PointTargetGraphics3DModel>
     Polarization<stkobjects/Polarization>
     PolarizationElliptical<stkobjects/PolarizationElliptical>
     PolarizationHorizontal<stkobjects/PolarizationHorizontal>
     PolarizationLeftHandCircular<stkobjects/PolarizationLeftHandCircular>
     PolarizationLinear<stkobjects/PolarizationLinear>
     PolarizationRightHandCircular<stkobjects/PolarizationRightHandCircular>
     PolarizationVertical<stkobjects/PolarizationVertical>
     Preferences<stkobjects/Preferences>
     PreferencesConnect<stkobjects/PreferencesConnect>
     PreferencesPythonPlugins<stkobjects/PreferencesPythonPlugins>
     PreferencesVDF<stkobjects/PreferencesVDF>
     Priority<stkobjects/Priority>
     PriorityCollection<stkobjects/PriorityCollection>
     ProgressBarEventArguments<stkobjects/ProgressBarEventArguments>
     PropagationChannel<stkobjects/PropagationChannel>
     Propagator11Parameters<stkobjects/Propagator11Parameters>
     Propagator11ParametersDescriptor<stkobjects/Propagator11ParametersDescriptor>
     Propagator11ParametersDescriptorCollection<stkobjects/Propagator11ParametersDescriptorCollection>
     PropagatorAviator<stkobjects/PropagatorAviator>
     PropagatorBallistic<stkobjects/PropagatorBallistic>
     PropagatorDefinitionExportTool<stkobjects/PropagatorDefinitionExportTool>
     PropagatorGPS<stkobjects/PropagatorGPS>
     PropagatorGreatArc<stkobjects/PropagatorGreatArc>
     PropagatorHPOP<stkobjects/PropagatorHPOP>
     PropagatorHPOPStaticForceModelSettings<stkobjects/PropagatorHPOPStaticForceModelSettings>
     PropagatorHPOPThirdBodyGravityCollection<stkobjects/PropagatorHPOPThirdBodyGravityCollection>
     PropagatorHPOPThirdBodyGravityElement<stkobjects/PropagatorHPOPThirdBodyGravityElement>
     PropagatorJ2Perturbation<stkobjects/PropagatorJ2Perturbation>
     PropagatorJ4Perturbation<stkobjects/PropagatorJ4Perturbation>
     PropagatorLOP<stkobjects/PropagatorLOP>
     PropagatorLOPThirdBodyGravity<stkobjects/PropagatorLOPThirdBodyGravity>
     PropagatorRealtime<stkobjects/PropagatorRealtime>
     PropagatorRealtimeCartesianPoints<stkobjects/PropagatorRealtimeCartesianPoints>
     PropagatorRealtimeDeticPoints<stkobjects/PropagatorRealtimeDeticPoints>
     PropagatorRealtimeHeadingPitch<stkobjects/PropagatorRealtimeHeadingPitch>
     PropagatorRealtimePointBuilder<stkobjects/PropagatorRealtimePointBuilder>
     PropagatorRealtimeUTMPoints<stkobjects/PropagatorRealtimeUTMPoints>
     PropagatorSGP4<stkobjects/PropagatorSGP4>
     PropagatorSGP4AutoUpdate<stkobjects/PropagatorSGP4AutoUpdate>
     PropagatorSGP4AutoUpdateFileSource<stkobjects/PropagatorSGP4AutoUpdateFileSource>
     PropagatorSGP4AutoUpdateOnlineSource<stkobjects/PropagatorSGP4AutoUpdateOnlineSource>
     PropagatorSGP4AutoUpdateProperties<stkobjects/PropagatorSGP4AutoUpdateProperties>
     PropagatorSGP4CommonTasks<stkobjects/PropagatorSGP4CommonTasks>
     PropagatorSGP4LoadFile<stkobjects/PropagatorSGP4LoadFile>
     PropagatorSGP4OnlineAutoLoad<stkobjects/PropagatorSGP4OnlineAutoLoad>
     PropagatorSGP4OnlineLoad<stkobjects/PropagatorSGP4OnlineLoad>
     PropagatorSGP4PropagatorSettings<stkobjects/PropagatorSGP4PropagatorSettings>
     PropagatorSGP4Segment<stkobjects/PropagatorSGP4Segment>
     PropagatorSGP4SegmentCollection<stkobjects/PropagatorSGP4SegmentCollection>
     PropagatorSimpleAscent<stkobjects/PropagatorSimpleAscent>
     PropagatorSP3<stkobjects/PropagatorSP3>
     PropagatorSP3File<stkobjects/PropagatorSP3File>
     PropagatorSP3FileCollection<stkobjects/PropagatorSP3FileCollection>
     PropagatorSPICE<stkobjects/PropagatorSPICE>
     PropagatorSPICESegment<stkobjects/PropagatorSPICESegment>
     PropagatorSPICESegmentsCollection<stkobjects/PropagatorSPICESegmentsCollection>
     PropagatorSTKExternal<stkobjects/PropagatorSTKExternal>
     PropagatorTwoBody<stkobjects/PropagatorTwoBody>
     PropagatorUserExternal<stkobjects/PropagatorUserExternal>
     Radar<stkobjects/Radar>
     RadarAccessGraphics<stkobjects/RadarAccessGraphics>
     RadarActivity<stkobjects/RadarActivity>
     RadarActivityAlwaysActive<stkobjects/RadarActivityAlwaysActive>
     RadarActivityAlwaysInactive<stkobjects/RadarActivityAlwaysInactive>
     RadarActivityTimeComponentList<stkobjects/RadarActivityTimeComponentList>
     RadarActivityTimeComponentListCollection<stkobjects/RadarActivityTimeComponentListCollection>
     RadarActivityTimeComponentListElement<stkobjects/RadarActivityTimeComponentListElement>
     RadarActivityTimeIntervalList<stkobjects/RadarActivityTimeIntervalList>
     RadarActivityTimeIntervalListCollection<stkobjects/RadarActivityTimeIntervalListCollection>
     RadarActivityTimeIntervalListElement<stkobjects/RadarActivityTimeIntervalListElement>
     RadarAntennaBeam<stkobjects/RadarAntennaBeam>
     RadarAntennaBeamCollection<stkobjects/RadarAntennaBeamCollection>
     RadarClutter<stkobjects/RadarClutter>
     RadarClutterGeometry<stkobjects/RadarClutterGeometry>
     RadarContinuousWaveAnalysisModeFixedTime<stkobjects/RadarContinuousWaveAnalysisModeFixedTime>
     RadarContinuousWaveAnalysisModeGoalSNR<stkobjects/RadarContinuousWaveAnalysisModeGoalSNR>
     RadarCrossSection<stkobjects/RadarCrossSection>
     RadarCrossSectionComputeStrategy<stkobjects/RadarCrossSectionComputeStrategy>
     RadarCrossSectionComputeStrategyAnsysCSVFile<stkobjects/RadarCrossSectionComputeStrategyAnsysCSVFile>
     RadarCrossSectionComputeStrategyConstantValue<stkobjects/RadarCrossSectionComputeStrategyConstantValue>
     RadarCrossSectionComputeStrategyExternalFile<stkobjects/RadarCrossSectionComputeStrategyExternalFile>
     RadarCrossSectionComputeStrategyPlugin<stkobjects/RadarCrossSectionComputeStrategyPlugin>
     RadarCrossSectionComputeStrategyScriptPlugin<stkobjects/RadarCrossSectionComputeStrategyScriptPlugin>
     RadarCrossSectionContourLevel<stkobjects/RadarCrossSectionContourLevel>
     RadarCrossSectionContourLevelCollection<stkobjects/RadarCrossSectionContourLevelCollection>
     RadarCrossSectionFrequencyBand<stkobjects/RadarCrossSectionFrequencyBand>
     RadarCrossSectionFrequencyBandCollection<stkobjects/RadarCrossSectionFrequencyBandCollection>
     RadarCrossSectionGraphics<stkobjects/RadarCrossSectionGraphics>
     RadarCrossSectionGraphics3D<stkobjects/RadarCrossSectionGraphics3D>
     RadarCrossSectionInheritable<stkobjects/RadarCrossSectionInheritable>
     RadarCrossSectionModel<stkobjects/RadarCrossSectionModel>
     RadarCrossSectionVolumeGraphics<stkobjects/RadarCrossSectionVolumeGraphics>
     RadarCrossSectionVolumeLevel<stkobjects/RadarCrossSectionVolumeLevel>
     RadarCrossSectionVolumeLevelCollection<stkobjects/RadarCrossSectionVolumeLevelCollection>
     RadarDopplerClutterFilters<stkobjects/RadarDopplerClutterFilters>
     RadarGraphics<stkobjects/RadarGraphics>
     RadarGraphics3D<stkobjects/RadarGraphics3D>
     RadarJamming<stkobjects/RadarJamming>
     RadarModeBistaticReceiver<stkobjects/RadarModeBistaticReceiver>
     RadarModeBistaticReceiverSAR<stkobjects/RadarModeBistaticReceiverSAR>
     RadarModeBistaticReceiverSearchTrack<stkobjects/RadarModeBistaticReceiverSearchTrack>
     RadarModeBistaticTransmitter<stkobjects/RadarModeBistaticTransmitter>
     RadarModeBistaticTransmitterSAR<stkobjects/RadarModeBistaticTransmitterSAR>
     RadarModeBistaticTransmitterSearchTrack<stkobjects/RadarModeBistaticTransmitterSearchTrack>
     RadarModel<stkobjects/RadarModel>
     RadarModelBistaticReceiver<stkobjects/RadarModelBistaticReceiver>
     RadarModelBistaticTransmitter<stkobjects/RadarModelBistaticTransmitter>
     RadarModelMonostatic<stkobjects/RadarModelMonostatic>
     RadarModelMultifunction<stkobjects/RadarModelMultifunction>
     RadarModeMonostatic<stkobjects/RadarModeMonostatic>
     RadarModeMonostaticSAR<stkobjects/RadarModeMonostaticSAR>
     RadarModeMonostaticSearchTrack<stkobjects/RadarModeMonostaticSearchTrack>
     RadarModulator<stkobjects/RadarModulator>
     RadarMultifunctionDetectionProcessing<stkobjects/RadarMultifunctionDetectionProcessing>
     RadarMultifunctionWaveformStrategySettings<stkobjects/RadarMultifunctionWaveformStrategySettings>
     RadarMultipathGraphics<stkobjects/RadarMultipathGraphics>
     RadarProbabilityOfDetection<stkobjects/RadarProbabilityOfDetection>
     RadarProbabilityOfDetectionCFAR<stkobjects/RadarProbabilityOfDetectionCFAR>
     RadarProbabilityOfDetectionCFARCellAveraging<stkobjects/RadarProbabilityOfDetectionCFARCellAveraging>
     RadarProbabilityOfDetectionCFAROrderedStatistics<stkobjects/RadarProbabilityOfDetectionCFAROrderedStatistics>
     RadarProbabilityOfDetectionNonCFAR<stkobjects/RadarProbabilityOfDetectionNonCFAR>
     RadarProbabilityOfDetectionPlugin<stkobjects/RadarProbabilityOfDetectionPlugin>
     RadarPulseIntegrationFixedNumberOfPulses<stkobjects/RadarPulseIntegrationFixedNumberOfPulses>
     RadarPulseIntegrationGoalSNR<stkobjects/RadarPulseIntegrationGoalSNR>
     RadarReceiver<stkobjects/RadarReceiver>
     RadarSTCAttenuation<stkobjects/RadarSTCAttenuation>
     RadarSTCAttenuationDecayFactor<stkobjects/RadarSTCAttenuationDecayFactor>
     RadarSTCAttenuationDecaySlope<stkobjects/RadarSTCAttenuationDecaySlope>
     RadarSTCAttenuationMapAzimuthRange<stkobjects/RadarSTCAttenuationMapAzimuthRange>
     RadarSTCAttenuationMapElevationRange<stkobjects/RadarSTCAttenuationMapElevationRange>
     RadarSTCAttenuationMapRange<stkobjects/RadarSTCAttenuationMapRange>
     RadarSTCAttenuationPlugin<stkobjects/RadarSTCAttenuationPlugin>
     RadarTransmitter<stkobjects/RadarTransmitter>
     RadarTransmitterMultifunction<stkobjects/RadarTransmitterMultifunction>
     RadarWaveformBistaticReceiverSearchTrackContinuous<stkobjects/RadarWaveformBistaticReceiverSearchTrackContinuous>
     RadarWaveformBistaticReceiverSearchTrackFixedPRF<stkobjects/RadarWaveformBistaticReceiverSearchTrackFixedPRF>
     RadarWaveformBistaticTransmitterSearchTrackContinuous<stkobjects/RadarWaveformBistaticTransmitterSearchTrackContinuous>
     RadarWaveformBistaticTransmitterSearchTrackFixedPRF<stkobjects/RadarWaveformBistaticTransmitterSearchTrackFixedPRF>
     RadarWaveformMonostaticSearchTrackContinuous<stkobjects/RadarWaveformMonostaticSearchTrackContinuous>
     RadarWaveformMonostaticSearchTrackFixedPRF<stkobjects/RadarWaveformMonostaticSearchTrackFixedPRF>
     RadarWaveformSarPulseDefinition<stkobjects/RadarWaveformSarPulseDefinition>
     RadarWaveformSarPulseIntegration<stkobjects/RadarWaveformSarPulseIntegration>
     RadarWaveformSearchTrackPulseDefinition<stkobjects/RadarWaveformSearchTrackPulseDefinition>
     RadiationPressure<stkobjects/RadiationPressure>
     RainLossModel<stkobjects/RainLossModel>
     RainLossModelCCIR1983<stkobjects/RainLossModelCCIR1983>
     RainLossModelCrane1982<stkobjects/RainLossModelCrane1982>
     RainLossModelCrane1985<stkobjects/RainLossModelCrane1985>
     RainLossModelITURP618Version10<stkobjects/RainLossModelITURP618Version10>
     RainLossModelITURP618Version12<stkobjects/RainLossModelITURP618Version12>
     RainLossModelITURP618Version13<stkobjects/RainLossModelITURP618Version13>
     RainLossModelScriptPlugin<stkobjects/RainLossModelScriptPlugin>
     ReceivePolarizationElliptical<stkobjects/ReceivePolarizationElliptical>
     ReceivePolarizationHorizontal<stkobjects/ReceivePolarizationHorizontal>
     ReceivePolarizationLeftHandCircular<stkobjects/ReceivePolarizationLeftHandCircular>
     ReceivePolarizationLinear<stkobjects/ReceivePolarizationLinear>
     ReceivePolarizationRightHandCircular<stkobjects/ReceivePolarizationRightHandCircular>
     ReceivePolarizationVertical<stkobjects/ReceivePolarizationVertical>
     Receiver<stkobjects/Receiver>
     ReceiverGraphics<stkobjects/ReceiverGraphics>
     ReceiverGraphics3D<stkobjects/ReceiverGraphics3D>
     ReceiverModel<stkobjects/ReceiverModel>
     ReceiverModelCable<stkobjects/ReceiverModelCable>
     ReceiverModelComplex<stkobjects/ReceiverModelComplex>
     ReceiverModelLaser<stkobjects/ReceiverModelLaser>
     ReceiverModelMedium<stkobjects/ReceiverModelMedium>
     ReceiverModelMultibeam<stkobjects/ReceiverModelMultibeam>
     ReceiverModelScriptPluginLaser<stkobjects/ReceiverModelScriptPluginLaser>
     ReceiverModelScriptPluginRF<stkobjects/ReceiverModelScriptPluginRF>
     ReceiverModelSimple<stkobjects/ReceiverModelSimple>
     RefractionCoefficients<stkobjects/RefractionCoefficients>
     RefractionModelEffectiveRadiusMethod<stkobjects/RefractionModelEffectiveRadiusMethod>
     RefractionModelITURP8344<stkobjects/RefractionModelITURP8344>
     RefractionModelSCFMethod<stkobjects/RefractionModelSCFMethod>
     RepeatGroundTrackNumbering<stkobjects/RepeatGroundTrackNumbering>
     ReTransmitterModelComplex<stkobjects/ReTransmitterModelComplex>
     ReTransmitterModelMedium<stkobjects/ReTransmitterModelMedium>
     ReTransmitterModelSimple<stkobjects/ReTransmitterModelSimple>
     RFEnvironment<stkobjects/RFEnvironment>
     RFFilterModel<stkobjects/RFFilterModel>
     RFFilterModelBessel<stkobjects/RFFilterModelBessel>
     RFFilterModelButterworth<stkobjects/RFFilterModelButterworth>
     RFFilterModelChebyshev<stkobjects/RFFilterModelChebyshev>
     RFFilterModelCosineWindow<stkobjects/RFFilterModelCosineWindow>
     RFFilterModelElliptic<stkobjects/RFFilterModelElliptic>
     RFFilterModelExternal<stkobjects/RFFilterModelExternal>
     RFFilterModelFIR<stkobjects/RFFilterModelFIR>
     RFFilterModelFIRBoxCar<stkobjects/RFFilterModelFIRBoxCar>
     RFFilterModelGaussianWindow<stkobjects/RFFilterModelGaussianWindow>
     RFFilterModelHammingWindow<stkobjects/RFFilterModelHammingWindow>
     RFFilterModelIIR<stkobjects/RFFilterModelIIR>
     RFFilterModelRaisedCosine<stkobjects/RFFilterModelRaisedCosine>
     RFFilterModelRCLowPass<stkobjects/RFFilterModelRCLowPass>
     RFFilterModelRectangular<stkobjects/RFFilterModelRectangular>
     RFFilterModelRootRaisedCosine<stkobjects/RFFilterModelRootRaisedCosine>
     RFFilterModelScriptPlugin<stkobjects/RFFilterModelScriptPlugin>
     RFFilterModelSinc<stkobjects/RFFilterModelSinc>
     RFFilterModelSincEnvelopeSinc<stkobjects/RFFilterModelSincEnvelopeSinc>
     RFInterference<stkobjects/RFInterference>
     RotationRateAndOffset<stkobjects/RotationRateAndOffset>
     SamplingMethodAdaptive<stkobjects/SamplingMethodAdaptive>
     SamplingMethodFixedStep<stkobjects/SamplingMethodFixedStep>
     Satellite<stkobjects/Satellite>
     SatelliteCollection<stkobjects/SatelliteCollection>
     SatelliteExportTools<stkobjects/SatelliteExportTools>
     SatelliteGraphics<stkobjects/SatelliteGraphics>
     SatelliteGraphics3D<stkobjects/SatelliteGraphics3D>
     SatelliteGraphics3DModel<stkobjects/SatelliteGraphics3DModel>
     ScatteringPointCollection<stkobjects/ScatteringPointCollection>
     ScatteringPointCollectionElement<stkobjects/ScatteringPointCollectionElement>
     ScatteringPointModel<stkobjects/ScatteringPointModel>
     ScatteringPointModelConstantCoefficient<stkobjects/ScatteringPointModelConstantCoefficient>
     ScatteringPointModelPlugin<stkobjects/ScatteringPointModelPlugin>
     ScatteringPointModelWindTurbine<stkobjects/ScatteringPointModelWindTurbine>
     ScatteringPointProvider<stkobjects/ScatteringPointProvider>
     ScatteringPointProviderCollection<stkobjects/ScatteringPointProviderCollection>
     ScatteringPointProviderCollectionElement<stkobjects/ScatteringPointProviderCollectionElement>
     ScatteringPointProviderList<stkobjects/ScatteringPointProviderList>
     ScatteringPointProviderPlugin<stkobjects/ScatteringPointProviderPlugin>
     ScatteringPointProviderPointsFile<stkobjects/ScatteringPointProviderPointsFile>
     ScatteringPointProviderRangeOverCFARCells<stkobjects/ScatteringPointProviderRangeOverCFARCells>
     ScatteringPointProviderSinglePoint<stkobjects/ScatteringPointProviderSinglePoint>
     ScatteringPointProviderSmoothOblateEarth<stkobjects/ScatteringPointProviderSmoothOblateEarth>
     Scenario<stkobjects/Scenario>
     Scenario3dFont<stkobjects/Scenario3dFont>
     ScenarioAnimation<stkobjects/ScenarioAnimation>
     ScenarioAnimationTimePeriod<stkobjects/ScenarioAnimationTimePeriod>
     ScenarioBeforeSaveEventArguments<stkobjects/ScenarioBeforeSaveEventArguments>
     ScenarioDatabase<stkobjects/ScenarioDatabase>
     ScenarioDatabaseCollection<stkobjects/ScenarioDatabaseCollection>
     ScenarioEarthData<stkobjects/ScenarioEarthData>
     ScenarioGraphics<stkobjects/ScenarioGraphics>
     ScenarioGraphics3D<stkobjects/ScenarioGraphics3D>
     ScenarioSpaceEnvironment<stkobjects/ScenarioSpaceEnvironment>
     ScheduleTime<stkobjects/ScheduleTime>
     ScheduleTimeCollection<stkobjects/ScheduleTimeCollection>
     Sensor<stkobjects/Sensor>
     SensorAccessAdvancedSettings<stkobjects/SensorAccessAdvancedSettings>
     SensorAzElMaskFile<stkobjects/SensorAzElMaskFile>
     SensorCommonTasks<stkobjects/SensorCommonTasks>
     SensorComplexConicPattern<stkobjects/SensorComplexConicPattern>
     SensorCustomPattern<stkobjects/SensorCustomPattern>
     SensorEOIRBand<stkobjects/SensorEOIRBand>
     SensorEOIRBandCollection<stkobjects/SensorEOIRBandCollection>
     SensorEOIRPattern<stkobjects/SensorEOIRPattern>
     SensorEOIRRadiometricPair<stkobjects/SensorEOIRRadiometricPair>
     SensorEOIRSaturationCollection<stkobjects/SensorEOIRSaturationCollection>
     SensorEOIRSensitivityCollection<stkobjects/SensorEOIRSensitivityCollection>
     SensorGraphics<stkobjects/SensorGraphics>
     SensorGraphics3D<stkobjects/SensorGraphics3D>
     SensorGraphics3DOffset<stkobjects/SensorGraphics3DOffset>
     SensorGraphics3DProjectionElement<stkobjects/SensorGraphics3DProjectionElement>
     SensorGraphics3DPulse<stkobjects/SensorGraphics3DPulse>
     SensorGraphics3DSpaceProjectionCollection<stkobjects/SensorGraphics3DSpaceProjectionCollection>
     SensorGraphics3DTargetProjectionCollection<stkobjects/SensorGraphics3DTargetProjectionCollection>
     SensorHalfPowerPattern<stkobjects/SensorHalfPowerPattern>
     SensorPointing3DModel<stkobjects/SensorPointing3DModel>
     SensorPointingAlongVector<stkobjects/SensorPointingAlongVector>
     SensorPointingExternal<stkobjects/SensorPointingExternal>
     SensorPointingFixed<stkobjects/SensorPointingFixed>
     SensorPointingFixedInAxes<stkobjects/SensorPointingFixedInAxes>
     SensorPointingGrazingAltitude<stkobjects/SensorPointingGrazingAltitude>
     SensorPointingSchedule<stkobjects/SensorPointingSchedule>
     SensorPointingSpinning<stkobjects/SensorPointingSpinning>
     SensorPointingTargeted<stkobjects/SensorPointingTargeted>
     SensorPointingTargetedBoresightFixed<stkobjects/SensorPointingTargetedBoresightFixed>
     SensorPointingTargetedBoresightTrack<stkobjects/SensorPointingTargetedBoresightTrack>
     SensorProjection<stkobjects/SensorProjection>
     SensorProjectionConstantAltitude<stkobjects/SensorProjectionConstantAltitude>
     SensorProjectionDisplayDistance<stkobjects/SensorProjectionDisplayDistance>
     SensorProjectionObjectAltitude<stkobjects/SensorProjectionObjectAltitude>
     SensorRectangularPattern<stkobjects/SensorRectangularPattern>
     SensorSARPattern<stkobjects/SensorSARPattern>
     SensorSimpleConicPattern<stkobjects/SensorSimpleConicPattern>
     SensorTarget<stkobjects/SensorTarget>
     SensorTargetCollection<stkobjects/SensorTargetCollection>
     SensorUnknownPattern<stkobjects/SensorUnknownPattern>
     Ship<stkobjects/Ship>
     ShipExportTools<stkobjects/ShipExportTools>
     ShipGraphics<stkobjects/ShipGraphics>
     ShipGraphics3D<stkobjects/ShipGraphics3D>
     SolarActivityConfiguration<stkobjects/SolarActivityConfiguration>
     SolarActivityConfigurationSolarFlux<stkobjects/SolarActivityConfigurationSolarFlux>
     SolarActivityConfigurationSunspotNumber<stkobjects/SolarActivityConfigurationSunspotNumber>
     SolarFluxGeoMagneticFileSettings<stkobjects/SolarFluxGeoMagneticFileSettings>
     SolarFluxGeoMagneticValueSettings<stkobjects/SolarFluxGeoMagneticValueSettings>
     SolarRadiationPressureModelGPS<stkobjects/SolarRadiationPressureModelGPS>
     SolarRadiationPressureModelPlugin<stkobjects/SolarRadiationPressureModelPlugin>
     SolarRadiationPressureModelPluginSettings<stkobjects/SolarRadiationPressureModelPluginSettings>
     SolarRadiationPressureModelSpherical<stkobjects/SolarRadiationPressureModelSpherical>
     SolidTides<stkobjects/SolidTides>
     SpaceEnvironment<stkobjects/SpaceEnvironment>
     SpaceEnvironmentGraphics<stkobjects/SpaceEnvironmentGraphics>
     SpaceEnvironmentMagneticField<stkobjects/SpaceEnvironmentMagneticField>
     SpaceEnvironmentMagnitudeFieldGraphics2D<stkobjects/SpaceEnvironmentMagnitudeFieldGraphics2D>
     SpaceEnvironmentMagnitudeFieldLine<stkobjects/SpaceEnvironmentMagnitudeFieldLine>
     SpaceEnvironmentParticleFlux<stkobjects/SpaceEnvironmentParticleFlux>
     SpaceEnvironmentRadiation<stkobjects/SpaceEnvironmentRadiation>
     SpaceEnvironmentRadiationDoseRateCollection<stkobjects/SpaceEnvironmentRadiationDoseRateCollection>
     SpaceEnvironmentRadiationDoseRateElement<stkobjects/SpaceEnvironmentRadiationDoseRateElement>
     SpaceEnvironmentRadiationEnergyMethodEnergies<stkobjects/SpaceEnvironmentRadiationEnergyMethodEnergies>
     SpaceEnvironmentRadiationEnergyValues<stkobjects/SpaceEnvironmentRadiationEnergyValues>
     SpaceEnvironmentRadiationEnvironment<stkobjects/SpaceEnvironmentRadiationEnvironment>
     SpaceEnvironmentSAAContour<stkobjects/SpaceEnvironmentSAAContour>
     SpaceEnvironmentScenarioGraphics3D<stkobjects/SpaceEnvironmentScenarioGraphics3D>
     SpaceEnvironmentVehicleTemperature<stkobjects/SpaceEnvironmentVehicleTemperature>
     SpatialState<stkobjects/SpatialState>
     SphericalFlightPathAngleHorizontal<stkobjects/SphericalFlightPathAngleHorizontal>
     SphericalFlightPathAngleVertical<stkobjects/SphericalFlightPathAngleVertical>
     Star<stkobjects/Star>
     StarCollection<stkobjects/StarCollection>
     StarGraphics<stkobjects/StarGraphics>
     StarGraphics3D<stkobjects/StarGraphics3D>
     StarInformation<stkobjects/StarInformation>
     STKObject<stkobjects/STKObject>
     STKObjectChangedEventArguments<stkobjects/STKObjectChangedEventArguments>
     STKObjectCutCopyPasteEventArguments<stkobjects/STKObjectCutCopyPasteEventArguments>
     STKObjectModelContext<stkobjects/STKObjectModelContext>
     STKObjectPreDeleteEventArguments<stkobjects/STKObjectPreDeleteEventArguments>
     STKObjectRoot<stkobjects/STKObjectRoot>
     Subset<stkobjects/Subset>
     Swath<stkobjects/Swath>
     SystemNoiseTemperature<stkobjects/SystemNoiseTemperature>
     Target<stkobjects/Target>
     TargetGraphics<stkobjects/TargetGraphics>
     TargetGraphics3D<stkobjects/TargetGraphics3D>
     TargetSelectionMethod<stkobjects/TargetSelectionMethod>
     TargetSelectionMethodClosingVelocity<stkobjects/TargetSelectionMethodClosingVelocity>
     TargetSelectionMethodPriority<stkobjects/TargetSelectionMethodPriority>
     TargetSelectionMethodRange<stkobjects/TargetSelectionMethodRange>
     Terrain<stkobjects/Terrain>
     TerrainCollection<stkobjects/TerrainCollection>
     TerrainNormalSlopeAzimuth<stkobjects/TerrainNormalSlopeAzimuth>
     Tileset3D<stkobjects/Tileset3D>
     Tileset3DCollection<stkobjects/Tileset3DCollection>
     TimeIntervalCollection<stkobjects/TimeIntervalCollection>
     TimeIntervalCollectionReadOnly<stkobjects/TimeIntervalCollectionReadOnly>
     TimePeriod<stkobjects/TimePeriod>
     TimePeriodValue<stkobjects/TimePeriodValue>
     TransferFunctionInputBackOffOutputBackOffTable<stkobjects/TransferFunctionInputBackOffOutputBackOffTable>
     TransferFunctionInputBackOffOutputBackOffTableRow<stkobjects/TransferFunctionInputBackOffOutputBackOffTableRow>
     TransferFunctionInputBackOffVsCOverImTable<stkobjects/TransferFunctionInputBackOffVsCOverImTable>
     TransferFunctionInputBackOffVsCOverImTableRow<stkobjects/TransferFunctionInputBackOffVsCOverImTableRow>
     TransferFunctionPolynomialCollection<stkobjects/TransferFunctionPolynomialCollection>
     Transmitter<stkobjects/Transmitter>
     TransmitterGraphics<stkobjects/TransmitterGraphics>
     TransmitterGraphics3D<stkobjects/TransmitterGraphics3D>
     TransmitterModel<stkobjects/TransmitterModel>
     TransmitterModelCable<stkobjects/TransmitterModelCable>
     TransmitterModelComplex<stkobjects/TransmitterModelComplex>
     TransmitterModelLaser<stkobjects/TransmitterModelLaser>
     TransmitterModelMedium<stkobjects/TransmitterModelMedium>
     TransmitterModelMultibeam<stkobjects/TransmitterModelMultibeam>
     TransmitterModelScriptPluginLaser<stkobjects/TransmitterModelScriptPluginLaser>
     TransmitterModelScriptPluginRF<stkobjects/TransmitterModelScriptPluginRF>
     TransmitterModelSimple<stkobjects/TransmitterModelSimple>
     TroposphericScintillationFadingLossModel<stkobjects/TroposphericScintillationFadingLossModel>
     TroposphericScintillationFadingLossModelP618Version12<stkobjects/TroposphericScintillationFadingLossModelP618Version12>
     TroposphericScintillationFadingLossModelP618Version8<stkobjects/TroposphericScintillationFadingLossModelP618Version8>
     UrbanTerrestrialLossModel<stkobjects/UrbanTerrestrialLossModel>
     UrbanTerrestrialLossModelTwoRay<stkobjects/UrbanTerrestrialLossModelTwoRay>
     UrbanTerrestrialLossModelWirelessInSite64<stkobjects/UrbanTerrestrialLossModelWirelessInSite64>
     VehicleAccessAdvancedSettings<stkobjects/VehicleAccessAdvancedSettings>
     VehicleAttitudeExportTool<stkobjects/VehicleAttitudeExportTool>
     VehicleAttitudeExternal<stkobjects/VehicleAttitudeExternal>
     VehicleAttitudeMaximumSlewAcceleration<stkobjects/VehicleAttitudeMaximumSlewAcceleration>
     VehicleAttitudeMaximumSlewRate<stkobjects/VehicleAttitudeMaximumSlewRate>
     VehicleAttitudePointing<stkobjects/VehicleAttitudePointing>
     VehicleAttitudeRealTime<stkobjects/VehicleAttitudeRealTime>
     VehicleAttitudeRealTimeDataReference<stkobjects/VehicleAttitudeRealTimeDataReference>
     VehicleAttitudeSlewConstrained<stkobjects/VehicleAttitudeSlewConstrained>
     VehicleAttitudeSlewFixedRate<stkobjects/VehicleAttitudeSlewFixedRate>
     VehicleAttitudeSlewFixedTime<stkobjects/VehicleAttitudeSlewFixedTime>
     VehicleAttitudeTargetSlew<stkobjects/VehicleAttitudeTargetSlew>
     VehicleAttitudeTrendingControlAviator<stkobjects/VehicleAttitudeTrendingControlAviator>
     VehicleBreakAngleBreakByLatitude<stkobjects/VehicleBreakAngleBreakByLatitude>
     VehicleBreakAngleBreakByLongitude<stkobjects/VehicleBreakAngleBreakByLongitude>
     VehicleCentralBodies<stkobjects/VehicleCentralBodies>
     VehicleConsiderAnalysisCollection<stkobjects/VehicleConsiderAnalysisCollection>
     VehicleConsiderAnalysisCollectionElement<stkobjects/VehicleConsiderAnalysisCollectionElement>
     VehicleCoordinateAxesCustom<stkobjects/VehicleCoordinateAxesCustom>
     VehicleCorrelationListCollection<stkobjects/VehicleCorrelationListCollection>
     VehicleCorrelationListElement<stkobjects/VehicleCorrelationListElement>
     VehicleCovariance<stkobjects/VehicleCovariance>
     VehicleDefinition<stkobjects/VehicleDefinition>
     VehicleDuration<stkobjects/VehicleDuration>
     VehicleEclipseBodies<stkobjects/VehicleEclipseBodies>
     VehicleEclipsingBodies<stkobjects/VehicleEclipsingBodies>
     VehicleEllipseDataCollection<stkobjects/VehicleEllipseDataCollection>
     VehicleEllipseDataElement<stkobjects/VehicleEllipseDataElement>
     VehicleEOIR<stkobjects/VehicleEOIR>
     VehicleEphemerisBinaryExportTool<stkobjects/VehicleEphemerisBinaryExportTool>
     VehicleEphemerisCCSDSExportTool<stkobjects/VehicleEphemerisCCSDSExportTool>
     VehicleEphemerisCCSDSv2ExportTool<stkobjects/VehicleEphemerisCCSDSv2ExportTool>
     VehicleEphemerisCode500ExportTool<stkobjects/VehicleEphemerisCode500ExportTool>
     VehicleEphemerisExportTool<stkobjects/VehicleEphemerisExportTool>
     VehicleEphemerisSPICEExportTool<stkobjects/VehicleEphemerisSPICEExportTool>
     VehicleExponentialDensityModelParameters<stkobjects/VehicleExponentialDensityModelParameters>
     VehicleGPSAlmanacProperties<stkobjects/VehicleGPSAlmanacProperties>
     VehicleGPSAlmanacPropertiesSEM<stkobjects/VehicleGPSAlmanacPropertiesSEM>
     VehicleGPSAlmanacPropertiesSP3<stkobjects/VehicleGPSAlmanacPropertiesSP3>
     VehicleGPSAlmanacPropertiesYUMA<stkobjects/VehicleGPSAlmanacPropertiesYUMA>
     VehicleGPSAutoUpdate<stkobjects/VehicleGPSAutoUpdate>
     VehicleGPSAutoUpdateFileSource<stkobjects/VehicleGPSAutoUpdateFileSource>
     VehicleGPSAutoUpdateOnlineSource<stkobjects/VehicleGPSAutoUpdateOnlineSource>
     VehicleGPSAutoUpdateProperties<stkobjects/VehicleGPSAutoUpdateProperties>
     VehicleGPSElement<stkobjects/VehicleGPSElement>
     VehicleGPSElementCollection<stkobjects/VehicleGPSElementCollection>
     VehicleGPSSpecifyAlmanac<stkobjects/VehicleGPSSpecifyAlmanac>
     VehicleGraphics2DAttributesAccess<stkobjects/VehicleGraphics2DAttributesAccess>
     VehicleGraphics2DAttributesCustom<stkobjects/VehicleGraphics2DAttributesCustom>
     VehicleGraphics2DAttributesOrbit<stkobjects/VehicleGraphics2DAttributesOrbit>
     VehicleGraphics2DAttributesRealtime<stkobjects/VehicleGraphics2DAttributesRealtime>
     VehicleGraphics2DAttributesRoute<stkobjects/VehicleGraphics2DAttributesRoute>
     VehicleGraphics2DAttributesTimeComponents<stkobjects/VehicleGraphics2DAttributesTimeComponents>
     VehicleGraphics2DAttributesTrajectory<stkobjects/VehicleGraphics2DAttributesTrajectory>
     VehicleGraphics2DElevationContours<stkobjects/VehicleGraphics2DElevationContours>
     VehicleGraphics2DElevationGroundElevation<stkobjects/VehicleGraphics2DElevationGroundElevation>
     VehicleGraphics2DElevationsCollection<stkobjects/VehicleGraphics2DElevationsCollection>
     VehicleGraphics2DElevationsElement<stkobjects/VehicleGraphics2DElevationsElement>
     VehicleGraphics2DElevationSwathHalfWidth<stkobjects/VehicleGraphics2DElevationSwathHalfWidth>
     VehicleGraphics2DElevationVehicleHalfAngle<stkobjects/VehicleGraphics2DElevationVehicleHalfAngle>
     VehicleGraphics2DGroundEllipsesCollection<stkobjects/VehicleGraphics2DGroundEllipsesCollection>
     VehicleGraphics2DGroundEllipsesElement<stkobjects/VehicleGraphics2DGroundEllipsesElement>
     VehicleGraphics2DInterval<stkobjects/VehicleGraphics2DInterval>
     VehicleGraphics2DIntervalsCollection<stkobjects/VehicleGraphics2DIntervalsCollection>
     VehicleGraphics2DLeadDataFraction<stkobjects/VehicleGraphics2DLeadDataFraction>
     VehicleGraphics2DLeadDataTime<stkobjects/VehicleGraphics2DLeadDataTime>
     VehicleGraphics2DLeadTrailData<stkobjects/VehicleGraphics2DLeadTrailData>
     VehicleGraphics2DLighting<stkobjects/VehicleGraphics2DLighting>
     VehicleGraphics2DLightingElement<stkobjects/VehicleGraphics2DLightingElement>
     VehicleGraphics2DLine<stkobjects/VehicleGraphics2DLine>
     VehicleGraphics2DOrbitPassData<stkobjects/VehicleGraphics2DOrbitPassData>
     VehicleGraphics2DPasses<stkobjects/VehicleGraphics2DPasses>
     VehicleGraphics2DPassResolution<stkobjects/VehicleGraphics2DPassResolution>
     VehicleGraphics2DPassShowPasses<stkobjects/VehicleGraphics2DPassShowPasses>
     VehicleGraphics2DRoutePassData<stkobjects/VehicleGraphics2DRoutePassData>
     VehicleGraphics2DRouteResolution<stkobjects/VehicleGraphics2DRouteResolution>
     VehicleGraphics2DSAA<stkobjects/VehicleGraphics2DSAA>
     VehicleGraphics2DSwath<stkobjects/VehicleGraphics2DSwath>
     VehicleGraphics2DTimeComponentsCollection<stkobjects/VehicleGraphics2DTimeComponentsCollection>
     VehicleGraphics2DTimeComponentsEventCollectionElement<stkobjects/VehicleGraphics2DTimeComponentsEventCollectionElement>
     VehicleGraphics2DTimeComponentsEventElement<stkobjects/VehicleGraphics2DTimeComponentsEventElement>
     VehicleGraphics2DTimeEventsCollection<stkobjects/VehicleGraphics2DTimeEventsCollection>
     VehicleGraphics2DTimeEventsElement<stkobjects/VehicleGraphics2DTimeEventsElement>
     VehicleGraphics2DTimeEventTypeLine<stkobjects/VehicleGraphics2DTimeEventTypeLine>
     VehicleGraphics2DTimeEventTypeMarker<stkobjects/VehicleGraphics2DTimeEventTypeMarker>
     VehicleGraphics2DTimeEventTypeText<stkobjects/VehicleGraphics2DTimeEventTypeText>
     VehicleGraphics2DTrailDataFraction<stkobjects/VehicleGraphics2DTrailDataFraction>
     VehicleGraphics2DTrailDataTime<stkobjects/VehicleGraphics2DTrailDataTime>
     VehicleGraphics2DTrajectoryPassData<stkobjects/VehicleGraphics2DTrajectoryPassData>
     VehicleGraphics2DTrajectoryResolution<stkobjects/VehicleGraphics2DTrajectoryResolution>
     VehicleGraphics2DWaypointMarker<stkobjects/VehicleGraphics2DWaypointMarker>
     VehicleGraphics2DWaypointMarkersCollection<stkobjects/VehicleGraphics2DWaypointMarkersCollection>
     VehicleGraphics2DWaypointMarkersElement<stkobjects/VehicleGraphics2DWaypointMarkersElement>
     VehicleGraphics3DAttributesBasic<stkobjects/VehicleGraphics3DAttributesBasic>
     VehicleGraphics3DAttributesIntervals<stkobjects/VehicleGraphics3DAttributesIntervals>
     VehicleGraphics3DBearingBox<stkobjects/VehicleGraphics3DBearingBox>
     VehicleGraphics3DBearingEllipse<stkobjects/VehicleGraphics3DBearingEllipse>
     VehicleGraphics3DBPlaneEvent<stkobjects/VehicleGraphics3DBPlaneEvent>
     VehicleGraphics3DBPlaneInstance<stkobjects/VehicleGraphics3DBPlaneInstance>
     VehicleGraphics3DBPlaneInstancesCollection<stkobjects/VehicleGraphics3DBPlaneInstancesCollection>
     VehicleGraphics3DBPlanePoint<stkobjects/VehicleGraphics3DBPlanePoint>
     VehicleGraphics3DBPlanePointCollection<stkobjects/VehicleGraphics3DBPlanePointCollection>
     VehicleGraphics3DBPlanes<stkobjects/VehicleGraphics3DBPlanes>
     VehicleGraphics3DBPlaneTargetPoint<stkobjects/VehicleGraphics3DBPlaneTargetPoint>
     VehicleGraphics3DBPlaneTargetPointPositionCartesian<stkobjects/VehicleGraphics3DBPlaneTargetPointPositionCartesian>
     VehicleGraphics3DBPlaneTargetPointPositionPolar<stkobjects/VehicleGraphics3DBPlaneTargetPointPositionPolar>
     VehicleGraphics3DBPlaneTemplate<stkobjects/VehicleGraphics3DBPlaneTemplate>
     VehicleGraphics3DBPlaneTemplateDisplayCollection<stkobjects/VehicleGraphics3DBPlaneTemplateDisplayCollection>
     VehicleGraphics3DBPlaneTemplateDisplayElement<stkobjects/VehicleGraphics3DBPlaneTemplateDisplayElement>
     VehicleGraphics3DBPlaneTemplatesCollection<stkobjects/VehicleGraphics3DBPlaneTemplatesCollection>
     VehicleGraphics3DControlBox<stkobjects/VehicleGraphics3DControlBox>
     VehicleGraphics3DCovariance<stkobjects/VehicleGraphics3DCovariance>
     VehicleGraphics3DCovariancePointingContour<stkobjects/VehicleGraphics3DCovariancePointingContour>
     VehicleGraphics3DDataFraction<stkobjects/VehicleGraphics3DDataFraction>
     VehicleGraphics3DDataTime<stkobjects/VehicleGraphics3DDataTime>
     VehicleGraphics3DDefaultAttributes<stkobjects/VehicleGraphics3DDefaultAttributes>
     VehicleGraphics3DDropLinePathItem<stkobjects/VehicleGraphics3DDropLinePathItem>
     VehicleGraphics3DDropLinePathItemCollection<stkobjects/VehicleGraphics3DDropLinePathItemCollection>
     VehicleGraphics3DDropLinePositionItem<stkobjects/VehicleGraphics3DDropLinePositionItem>
     VehicleGraphics3DDropLinePositionItemCollection<stkobjects/VehicleGraphics3DDropLinePositionItemCollection>
     VehicleGraphics3DElevationContours<stkobjects/VehicleGraphics3DElevationContours>
     VehicleGraphics3DEllipsoid<stkobjects/VehicleGraphics3DEllipsoid>
     VehicleGraphics3DGeoBox<stkobjects/VehicleGraphics3DGeoBox>
     VehicleGraphics3DIntervalsCollection<stkobjects/VehicleGraphics3DIntervalsCollection>
     VehicleGraphics3DIntervalsElement<stkobjects/VehicleGraphics3DIntervalsElement>
     VehicleGraphics3DLeadTrailData<stkobjects/VehicleGraphics3DLeadTrailData>
     VehicleGraphics3DLineOfBearing<stkobjects/VehicleGraphics3DLineOfBearing>
     VehicleGraphics3DModelRoute<stkobjects/VehicleGraphics3DModelRoute>
     VehicleGraphics3DModelTrajectory<stkobjects/VehicleGraphics3DModelTrajectory>
     VehicleGraphics3DOrbitDropLines<stkobjects/VehicleGraphics3DOrbitDropLines>
     VehicleGraphics3DOrbitPassData<stkobjects/VehicleGraphics3DOrbitPassData>
     VehicleGraphics3DOrbitProximity<stkobjects/VehicleGraphics3DOrbitProximity>
     VehicleGraphics3DOrbitTickMarks<stkobjects/VehicleGraphics3DOrbitTickMarks>
     VehicleGraphics3DOrbitTrackData<stkobjects/VehicleGraphics3DOrbitTrackData>
     VehicleGraphics3DPass<stkobjects/VehicleGraphics3DPass>
     VehicleGraphics3DPathTickMarks<stkobjects/VehicleGraphics3DPathTickMarks>
     VehicleGraphics3DRoute<stkobjects/VehicleGraphics3DRoute>
     VehicleGraphics3DRouteDropLines<stkobjects/VehicleGraphics3DRouteDropLines>
     VehicleGraphics3DRouteProximity<stkobjects/VehicleGraphics3DRouteProximity>
     VehicleGraphics3DSAA<stkobjects/VehicleGraphics3DSAA>
     VehicleGraphics3DSigmaScaleProbability<stkobjects/VehicleGraphics3DSigmaScaleProbability>
     VehicleGraphics3DSigmaScaleScale<stkobjects/VehicleGraphics3DSigmaScaleScale>
     VehicleGraphics3DSize<stkobjects/VehicleGraphics3DSize>
     VehicleGraphics3DSystemsCollection<stkobjects/VehicleGraphics3DSystemsCollection>
     VehicleGraphics3DSystemsElement<stkobjects/VehicleGraphics3DSystemsElement>
     VehicleGraphics3DSystemsSpecialElement<stkobjects/VehicleGraphics3DSystemsSpecialElement>
     VehicleGraphics3DTickDataLine<stkobjects/VehicleGraphics3DTickDataLine>
     VehicleGraphics3DTickDataPoint<stkobjects/VehicleGraphics3DTickDataPoint>
     VehicleGraphics3DTrajectory<stkobjects/VehicleGraphics3DTrajectory>
     VehicleGraphics3DTrajectoryDropLines<stkobjects/VehicleGraphics3DTrajectoryDropLines>
     VehicleGraphics3DTrajectoryPassData<stkobjects/VehicleGraphics3DTrajectoryPassData>
     VehicleGraphics3DTrajectoryProximity<stkobjects/VehicleGraphics3DTrajectoryProximity>
     VehicleGraphics3DTrajectoryTickMarks<stkobjects/VehicleGraphics3DTrajectoryTickMarks>
     VehicleGraphics3DTrajectoryTrackData<stkobjects/VehicleGraphics3DTrajectoryTrackData>
     VehicleGraphics3DVelocityCovariance<stkobjects/VehicleGraphics3DVelocityCovariance>
     VehicleGraphics3DWaypointMarkersCollection<stkobjects/VehicleGraphics3DWaypointMarkersCollection>
     VehicleGraphics3DWaypointMarkersElement<stkobjects/VehicleGraphics3DWaypointMarkersElement>
     VehicleGravity<stkobjects/VehicleGravity>
     VehicleGroundEllipseElement<stkobjects/VehicleGroundEllipseElement>
     VehicleGroundEllipsesCollection<stkobjects/VehicleGroundEllipsesCollection>
     VehicleHPOPCentralBodyGravity<stkobjects/VehicleHPOPCentralBodyGravity>
     VehicleHPOPDragModel<stkobjects/VehicleHPOPDragModel>
     VehicleHPOPDragModelPlugin<stkobjects/VehicleHPOPDragModelPlugin>
     VehicleHPOPDragModelPluginSettings<stkobjects/VehicleHPOPDragModelPluginSettings>
     VehicleHPOPDragModelSpherical<stkobjects/VehicleHPOPDragModelSpherical>
     VehicleHPOPForceModel<stkobjects/VehicleHPOPForceModel>
     VehicleHPOPForceModelDrag<stkobjects/VehicleHPOPForceModelDrag>
     VehicleHPOPForceModelDragOptions<stkobjects/VehicleHPOPForceModelDragOptions>
     VehicleHPOPForceModelMoreOptions<stkobjects/VehicleHPOPForceModelMoreOptions>
     VehicleHPOPSolarRadiationPressure<stkobjects/VehicleHPOPSolarRadiationPressure>
     VehicleHPOPSolarRadiationPressureModel<stkobjects/VehicleHPOPSolarRadiationPressureModel>
     VehicleHPOPSolarRadiationPressureOptions<stkobjects/VehicleHPOPSolarRadiationPressureOptions>
     VehicleImpactLocationCentric<stkobjects/VehicleImpactLocationCentric>
     VehicleImpactLocationDetic<stkobjects/VehicleImpactLocationDetic>
     VehicleImpactLocationLaunchAzEl<stkobjects/VehicleImpactLocationLaunchAzEl>
     VehicleImpactLocationPoint<stkobjects/VehicleImpactLocationPoint>
     VehicleInertia<stkobjects/VehicleInertia>
     VehicleInitialState<stkobjects/VehicleInitialState>
     VehicleIntegratedAttitude<stkobjects/VehicleIntegratedAttitude>
     VehicleIntegrator<stkobjects/VehicleIntegrator>
     VehicleInterpolation<stkobjects/VehicleInterpolation>
     VehicleLOPCentralBodyGravity<stkobjects/VehicleLOPCentralBodyGravity>
     VehicleLOPDragSettings<stkobjects/VehicleLOPDragSettings>
     VehicleLOPForceModel<stkobjects/VehicleLOPForceModel>
     VehicleLOPForceModelDrag<stkobjects/VehicleLOPForceModelDrag>
     VehicleLOPSolarRadiationPressure<stkobjects/VehicleLOPSolarRadiationPressure>
     VehicleMassProperties<stkobjects/VehicleMassProperties>
     VehiclePhysicalData<stkobjects/VehiclePhysicalData>
     VehiclePluginPropagator<stkobjects/VehiclePluginPropagator>
     VehiclePluginSettings<stkobjects/VehiclePluginSettings>
     VehiclePositionVelocityCollection<stkobjects/VehiclePositionVelocityCollection>
     VehiclePositionVelocityElement<stkobjects/VehiclePositionVelocityElement>
     VehicleSpatialInformation<stkobjects/VehicleSpatialInformation>
     VehicleTargetPointingCollection<stkobjects/VehicleTargetPointingCollection>
     VehicleTargetPointingElement<stkobjects/VehicleTargetPointingElement>
     VehicleTargetPointingIntervalCollection<stkobjects/VehicleTargetPointingIntervalCollection>
     VehicleTargetTimes<stkobjects/VehicleTargetTimes>
     VehicleVector<stkobjects/VehicleVector>
     VehicleWaypointAltitudeReference<stkobjects/VehicleWaypointAltitudeReference>
     VehicleWaypointAltitudeReferenceTerrain<stkobjects/VehicleWaypointAltitudeReferenceTerrain>
     VehicleWaypointsCollection<stkobjects/VehicleWaypointsCollection>
     VehicleWaypointsElement<stkobjects/VehicleWaypointsElement>
     VehicleZonalPropagatorInitialState<stkobjects/VehicleZonalPropagatorInitialState>
     Volumetric<stkobjects/Volumetric>
     VolumetricAdvancedSettings<stkobjects/VolumetricAdvancedSettings>
     VolumetricAnalysisInterval<stkobjects/VolumetricAnalysisInterval>
     VolumetricExportTool<stkobjects/VolumetricExportTool>
     VolumetricExternalFile<stkobjects/VolumetricExternalFile>
     VolumetricGraphics3D<stkobjects/VolumetricGraphics3D>
     VolumetricGraphics3DActiveGridPoints<stkobjects/VolumetricGraphics3DActiveGridPoints>
     VolumetricGraphics3DCrossSection<stkobjects/VolumetricGraphics3DCrossSection>
     VolumetricGraphics3DCrossSectionPlane<stkobjects/VolumetricGraphics3DCrossSectionPlane>
     VolumetricGraphics3DCrossSectionPlaneCollection<stkobjects/VolumetricGraphics3DCrossSectionPlaneCollection>
     VolumetricGraphics3DGrid<stkobjects/VolumetricGraphics3DGrid>
     VolumetricGraphics3DLegend<stkobjects/VolumetricGraphics3DLegend>
     VolumetricGraphics3DSpatialCalculationLevel<stkobjects/VolumetricGraphics3DSpatialCalculationLevel>
     VolumetricGraphics3DSpatialCalculationLevelCollection<stkobjects/VolumetricGraphics3DSpatialCalculationLevelCollection>
     VolumetricGraphics3DSpatialCalculationLevels<stkobjects/VolumetricGraphics3DSpatialCalculationLevels>
     VolumetricGraphics3DVolume<stkobjects/VolumetricGraphics3DVolume>
     VolumetricGridSpatialCalculation<stkobjects/VolumetricGridSpatialCalculation>
     Waveform<stkobjects/Waveform>
     WaveformPulseDefinition<stkobjects/WaveformPulseDefinition>
     WaveformRectangular<stkobjects/WaveformRectangular>
     WaveformSelectionStrategy<stkobjects/WaveformSelectionStrategy>
     WaveformSelectionStrategyFixed<stkobjects/WaveformSelectionStrategyFixed>
     WaveformSelectionStrategyRangeLimits<stkobjects/WaveformSelectionStrategyRangeLimits>
     WirelessInSite64GeometryData<stkobjects/WirelessInSite64GeometryData>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AberrationType<stkobjects/AberrationType>
    ≔ AccessConstraintType<stkobjects/AccessConstraintType>
    ≔ AccessTimeType<stkobjects/AccessTimeType>
    ≔ ActionType<stkobjects/ActionType>
    ≔ AdvCATConjunctionType<stkobjects/AdvCATConjunctionType>
    ≔ AdvCATEllipsoidClassType<stkobjects/AdvCATEllipsoidClassType>
    ≔ AdvCATSecondaryEllipsoidsVisibilityType<stkobjects/AdvCATSecondaryEllipsoidsVisibilityType>
    ≔ AircraftWGS84WarningType<stkobjects/AircraftWGS84WarningType>
    ≔ AltitudeReferenceType<stkobjects/AltitudeReferenceType>
    ≔ AnalysisWorkbenchAccessConstraintType<stkobjects/AnalysisWorkbenchAccessConstraintType>
    ≔ AnimationActionType<stkobjects/AnimationActionType>
    ≔ AnimationDirectionType<stkobjects/AnimationDirectionType>
    ≔ AnimationEndTimeMode<stkobjects/AnimationEndTimeMode>
    ≔ AnimationOptionType<stkobjects/AnimationOptionType>
    ≔ AntennaContourType<stkobjects/AntennaContourType>
    ≔ AntennaControlReferenceType<stkobjects/AntennaControlReferenceType>
    ≔ AntennaGraphicsCoordinateSystem<stkobjects/AntennaGraphicsCoordinateSystem>
    ≔ AntennaModelCosecantSquaredSidelobeType<stkobjects/AntennaModelCosecantSquaredSidelobeType>
    ≔ AntennaModelInputType<stkobjects/AntennaModelInputType>
    ≔ AntennaModelType<stkobjects/AntennaModelType>
    ≔ AreaType<stkobjects/AreaType>
    ≔ AtmosphericAbsorptionModelType<stkobjects/AtmosphericAbsorptionModelType>
    ≔ AtmosphericDensityModel<stkobjects/AtmosphericDensityModel>
    ≔ AtmosphericTurbulenceModelType<stkobjects/AtmosphericTurbulenceModelType>
    ≔ AttitudeCoordinateAxes<stkobjects/AttitudeCoordinateAxes>
    ≔ AttitudeInclude<stkobjects/AttitudeInclude>
    ≔ AttitudeProfile<stkobjects/AttitudeProfile>
    ≔ AttitudeStandardType<stkobjects/AttitudeStandardType>
    ≔ AxisOffset<stkobjects/AxisOffset>
    ≔ AzElMaskType<stkobjects/AzElMaskType>
    ≔ BeamformerType<stkobjects/BeamformerType>
    ≔ BeamSelectionStrategyType<stkobjects/BeamSelectionStrategyType>
    ≔ BorderWallUpperLowerEdgeAltitudeReference<stkobjects/BorderWallUpperLowerEdgeAltitudeReference>
    ≔ BoresightType<stkobjects/BoresightType>
    ≔ BuildHeightReferenceMethod<stkobjects/BuildHeightReferenceMethod>
    ≔ BuildingHeightUnit<stkobjects/BuildingHeightUnit>
    ≔ CCSDSDateFormat<stkobjects/CCSDSDateFormat>
    ≔ CCSDSEphemerisFormatType<stkobjects/CCSDSEphemerisFormatType>
    ≔ CCSDSReferenceFrame<stkobjects/CCSDSReferenceFrame>
    ≔ CCSDSTimeSystem<stkobjects/CCSDSTimeSystem>
    ≔ ChainConstellationConstraintsMode<stkobjects/ChainConstellationConstraintsMode>
    ≔ ChainCoverageAssetMode<stkobjects/ChainCoverageAssetMode>
    ≔ ChainOptimalStrandCalculationScalarMetricType<stkobjects/ChainOptimalStrandCalculationScalarMetricType>
    ≔ ChainOptimalStrandCompareStrandsType<stkobjects/ChainOptimalStrandCompareStrandsType>
    ≔ ChainOptimalStrandLinkCompareType<stkobjects/ChainOptimalStrandLinkCompareType>
    ≔ ChainOptimalStrandMetricType<stkobjects/ChainOptimalStrandMetricType>
    ≔ ChainParentPlatformRestriction<stkobjects/ChainParentPlatformRestriction>
    ≔ ChainTimePeriodType<stkobjects/ChainTimePeriodType>
    ≔ CircularApertureInputType<stkobjects/CircularApertureInputType>
    ≔ ClassicalLocation<stkobjects/ClassicalLocation>
    ≔ ClassicalSizeShape<stkobjects/ClassicalSizeShape>
    ≔ CloudsAndFogFadingLossModelType<stkobjects/CloudsAndFogFadingLossModelType>
    ≔ CloudsAndFogLiquidWaterChoiceType<stkobjects/CloudsAndFogLiquidWaterChoiceType>
    ≔ CommSystemAccessEventDetectionType<stkobjects/CommSystemAccessEventDetectionType>
    ≔ CommSystemAccessSamplingMethodType<stkobjects/CommSystemAccessSamplingMethodType>
    ≔ CommSystemConstrainingRole<stkobjects/CommSystemConstrainingRole>
    ≔ CommSystemLinkSelectionCriteriaType<stkobjects/CommSystemLinkSelectionCriteriaType>
    ≔ CommSystemReferenceBandwidth<stkobjects/CommSystemReferenceBandwidth>
    ≔ CommSystemSaveMode<stkobjects/CommSystemSaveMode>
    ≔ Component<stkobjects/Component>
    ≔ ComponentLinkEmbedControlReferenceType<stkobjects/ComponentLinkEmbedControlReferenceType>
    ≔ Constants<stkobjects/Constants>
    ≔ ConstellationConstraintRestrictionType<stkobjects/ConstellationConstraintRestrictionType>
    ≔ ConstellationFromToParentConstraint<stkobjects/ConstellationFromToParentConstraint>
    ≔ ConstraintBackground<stkobjects/ConstraintBackground>
    ≔ ConstraintGroundTrack<stkobjects/ConstraintGroundTrack>
    ≔ ConstraintLighting<stkobjects/ConstraintLighting>
    ≔ Coverage3dDrawAtAltitudeMode<stkobjects/Coverage3dDrawAtAltitudeMode>
    ≔ CoverageAltitudeMethod<stkobjects/CoverageAltitudeMethod>
    ≔ CoverageAssetGrouping<stkobjects/CoverageAssetGrouping>
    ≔ CoverageAssetStatus<stkobjects/CoverageAssetStatus>
    ≔ CoverageBounds<stkobjects/CoverageBounds>
    ≔ CoverageCustomRegionAlgorithm<stkobjects/CoverageCustomRegionAlgorithm>
    ≔ CoverageDataRetention<stkobjects/CoverageDataRetention>
    ≔ CoverageGridClass<stkobjects/CoverageGridClass>
    ≔ CoverageGroundAltitudeMethod<stkobjects/CoverageGroundAltitudeMethod>
    ≔ CoveragePointAltitudeMethod<stkobjects/CoveragePointAltitudeMethod>
    ≔ CoveragePointLocationMethod<stkobjects/CoveragePointLocationMethod>
    ≔ CoverageRegionAccessAccelerationType<stkobjects/CoverageRegionAccessAccelerationType>
    ≔ CoverageResolution<stkobjects/CoverageResolution>
    ≔ CoverageSatisfactionType<stkobjects/CoverageSatisfactionType>
    ≔ DataProviderElementType<stkobjects/DataProviderElementType>
    ≔ DataProviderResultCategory<stkobjects/DataProviderResultCategory>
    ≔ DataProviderType<stkobjects/DataProviderType>
    ≔ DataSaveMode<stkobjects/DataSaveMode>
    ≔ DelaunayGType<stkobjects/DelaunayGType>
    ≔ DelaunayHType<stkobjects/DelaunayHType>
    ≔ DelaunayLType<stkobjects/DelaunayLType>
    ≔ DemodulatorModelType<stkobjects/DemodulatorModelType>
    ≔ DeticPositionType<stkobjects/DeticPositionType>
    ≔ DirectionProviderType<stkobjects/DirectionProviderType>
    ≔ DisplayTimesType<stkobjects/DisplayTimesType>
    ≔ DistanceOnSphere<stkobjects/DistanceOnSphere>
    ≔ DragModel<stkobjects/DragModel>
    ≔ ElementConfigurationType<stkobjects/ElementConfigurationType>
    ≔ EOIRFlightType<stkobjects/EOIRFlightType>
    ≔ EOIRShapeMaterialSpecificationType<stkobjects/EOIRShapeMaterialSpecificationType>
    ≔ EOIRShapeType<stkobjects/EOIRShapeType>
    ≔ EOIRThermalModelType<stkobjects/EOIRThermalModelType>
    ≔ EphemerisCoordinateSystemType<stkobjects/EphemerisCoordinateSystemType>
    ≔ EphemerisCovarianceType<stkobjects/EphemerisCovarianceType>
    ≔ EphemExportToolFileFormat<stkobjects/EphemExportToolFileFormat>
    ≔ EphemSourceType<stkobjects/EphemSourceType>
    ≔ EquinoctialFormulation<stkobjects/EquinoctialFormulation>
    ≔ EquinoctialSizeShape<stkobjects/EquinoctialSizeShape>
    ≔ ErrorCode<stkobjects/ErrorCode>
    ≔ EventDetection<stkobjects/EventDetection>
    ≔ ExportToolStepSizeType<stkobjects/ExportToolStepSizeType>
    ≔ ExportToolTimePeriodType<stkobjects/ExportToolTimePeriodType>
    ≔ ExportToolVersionFormat<stkobjects/ExportToolVersionFormat>
    ≔ ExternalEphemerisFormatType<stkobjects/ExternalEphemerisFormatType>
    ≔ ExternalFileMessageLevelType<stkobjects/ExternalFileMessageLevelType>
    ≔ FigureOfMeritAcrossAssets<stkobjects/FigureOfMeritAcrossAssets>
    ≔ FigureOfMeritCompute<stkobjects/FigureOfMeritCompute>
    ≔ FigureOfMeritConstraintName<stkobjects/FigureOfMeritConstraintName>
    ≔ FigureOfMeritDefinitionType<stkobjects/FigureOfMeritDefinitionType>
    ≔ FigureOfMeritEndGapOption<stkobjects/FigureOfMeritEndGapOption>
    ≔ FigureOfMeritGraphics2DAccumulation<stkobjects/FigureOfMeritGraphics2DAccumulation>
    ≔ FigureOfMeritGraphics2DColorMethod<stkobjects/FigureOfMeritGraphics2DColorMethod>
    ≔ FigureOfMeritGraphics2DContourType<stkobjects/FigureOfMeritGraphics2DContourType>
    ≔ FigureOfMeritGraphics2DDirection<stkobjects/FigureOfMeritGraphics2DDirection>
    ≔ FigureOfMeritGraphics2DFloatingPointFormat<stkobjects/FigureOfMeritGraphics2DFloatingPointFormat>
    ≔ FigureOfMeritInvalidValueActionType<stkobjects/FigureOfMeritInvalidValueActionType>
    ≔ FigureOfMeritMethod<stkobjects/FigureOfMeritMethod>
    ≔ FigureOfMeritNavigationAccuracyMethod<stkobjects/FigureOfMeritNavigationAccuracyMethod>
    ≔ FigureOfMeritNavigationComputeType<stkobjects/FigureOfMeritNavigationComputeType>
    ≔ FigureOfMeritSatisfactionType<stkobjects/FigureOfMeritSatisfactionType>
    ≔ FrequencySpecificationType<stkobjects/FrequencySpecificationType>
    ≔ GeodeticSize<stkobjects/GeodeticSize>
    ≔ GeometricElementType<stkobjects/GeometricElementType>
    ≔ GPSAttitudeModelType<stkobjects/GPSAttitudeModelType>
    ≔ GPSReferenceWeek<stkobjects/GPSReferenceWeek>
    ≔ Graphics3DACAPCoefficientDataType<stkobjects/Graphics3DACAPCoefficientDataType>
    ≔ Graphics3DACAPSolarActivityConfigurationType<stkobjects/Graphics3DACAPSolarActivityConfigurationType>
    ≔ Graphics3DFontSize<stkobjects/Graphics3DFontSize>
    ≔ Graphics3DFormat<stkobjects/Graphics3DFormat>
    ≔ Graphics3DLabelSwapDistanceType<stkobjects/Graphics3DLabelSwapDistanceType>
    ≔ Graphics3DLocation<stkobjects/Graphics3DLocation>
    ≔ Graphics3DMarkerOrientation<stkobjects/Graphics3DMarkerOrientation>
    ≔ Graphics3DMarkerOriginType<stkobjects/Graphics3DMarkerOriginType>
    ≔ Graphics3DXOrigin<stkobjects/Graphics3DXOrigin>
    ≔ Graphics3DYOrigin<stkobjects/Graphics3DYOrigin>
    ≔ HelpContextIdentifierType<stkobjects/HelpContextIdentifierType>
    ≔ HFSSFarFieldDataGainType<stkobjects/HFSSFarFieldDataGainType>
    ≔ IntersectionType<stkobjects/IntersectionType>
    ≔ IonosphericFadingLossModelType<stkobjects/IonosphericFadingLossModelType>
    ≔ IvClockHost<stkobjects/IvClockHost>
    ≔ IvTimeSense<stkobjects/IvTimeSense>
    ≔ LaserPropagationLossModelType<stkobjects/LaserPropagationLossModelType>
    ≔ LaserTroposphericScintillationLossModelType<stkobjects/LaserTroposphericScintillationLossModelType>
    ≔ LatticeType<stkobjects/LatticeType>
    ≔ LeadTrailData<stkobjects/LeadTrailData>
    ≔ LightingObstructionModelType<stkobjects/LightingObstructionModelType>
    ≔ LimitsExceededBehaviorType<stkobjects/LimitsExceededBehaviorType>
    ≔ LineWidth<stkobjects/LineWidth>
    ≔ LinkMarginType<stkobjects/LinkMarginType>
    ≔ LoadMethod<stkobjects/LoadMethod>
    ≔ LookAheadPropagator<stkobjects/LookAheadPropagator>
    ≔ LOPAtmosphericDensityModel<stkobjects/LOPAtmosphericDensityModel>
    ≔ LowAltitudeAtmosphericDensityModel<stkobjects/LowAltitudeAtmosphericDensityModel>
    ≔ MarkerShape3d<stkobjects/MarkerShape3d>
    ≔ MarkerType<stkobjects/MarkerType>
    ≔ MethodToComputeSunPosition<stkobjects/MethodToComputeSunPosition>
    ≔ MixedSphericalFlightPathAngleType<stkobjects/MixedSphericalFlightPathAngleType>
    ≔ ModelGltfReflectionMapType<stkobjects/ModelGltfReflectionMapType>
    ≔ ModelType<stkobjects/ModelType>
    ≔ ModtranAerosolModelType<stkobjects/ModtranAerosolModelType>
    ≔ ModtranCloudModelType<stkobjects/ModtranCloudModelType>
    ≔ ModulatorModelType<stkobjects/ModulatorModelType>
    ≔ MTOEntirety<stkobjects/MTOEntirety>
    ≔ MTOInputDataType<stkobjects/MTOInputDataType>
    ≔ MTOObjectInterval<stkobjects/MTOObjectInterval>
    ≔ MTORangeMode<stkobjects/MTORangeMode>
    ≔ MTOTrackEvaluationType<stkobjects/MTOTrackEvaluationType>
    ≔ MTOVisibilityMode<stkobjects/MTOVisibilityMode>
    ≔ NoiseTemperatureComputeType<stkobjects/NoiseTemperatureComputeType>
    ≔ NoteShowType<stkobjects/NoteShowType>
    ≔ NotificationFilterMask<stkobjects/NotificationFilterMask>
    ≔ OffsetFrameType<stkobjects/OffsetFrameType>
    ≔ OnePointAccessStatus<stkobjects/OnePointAccessStatus>
    ≔ OnePointAccessSummary<stkobjects/OnePointAccessSummary>
    ≔ OrientationAscNode<stkobjects/OrientationAscNode>
    ≔ PlanetOrbitDisplayType<stkobjects/PlanetOrbitDisplayType>
    ≔ PlanetPositionSourceType<stkobjects/PlanetPositionSourceType>
    ≔ PointingStrategyType<stkobjects/PointingStrategyType>
    ≔ PolarizationReferenceAxis<stkobjects/PolarizationReferenceAxis>
    ≔ PolarizationType<stkobjects/PolarizationType>
    ≔ PRFMode<stkobjects/PRFMode>
    ≔ ProjectionHorizontalDatumType<stkobjects/ProjectionHorizontalDatumType>
    ≔ PropagatorDisplayCoordinateType<stkobjects/PropagatorDisplayCoordinateType>
    ≔ PropagatorSGP4SwitchMethod<stkobjects/PropagatorSGP4SwitchMethod>
    ≔ PropagatorType<stkobjects/PropagatorType>
    ≔ PulseWidthMode<stkobjects/PulseWidthMode>
    ≔ RadarActivityType<stkobjects/RadarActivityType>
    ≔ RadarClutterGeometryModelType<stkobjects/RadarClutterGeometryModelType>
    ≔ RadarClutterMapModelType<stkobjects/RadarClutterMapModelType>
    ≔ RadarContinuousWaveAnalysisMode<stkobjects/RadarContinuousWaveAnalysisMode>
    ≔ RadarCrossSectionContourGraphicsPolarization<stkobjects/RadarCrossSectionContourGraphicsPolarization>
    ≔ RadarFrequencySpecificationType<stkobjects/RadarFrequencySpecificationType>
    ≔ RadarMode<stkobjects/RadarMode>
    ≔ RadarModelType<stkobjects/RadarModelType>
    ≔ RadarProbabilityOfDetectionType<stkobjects/RadarProbabilityOfDetectionType>
    ≔ RadarPulseIntegrationType<stkobjects/RadarPulseIntegrationType>
    ≔ RadarPulseIntegratorType<stkobjects/RadarPulseIntegratorType>
    ≔ RadarSarPcrMode<stkobjects/RadarSarPcrMode>
    ≔ RadarSarPRFMode<stkobjects/RadarSarPRFMode>
    ≔ RadarSARPulseIntegrationAnalysisMode<stkobjects/RadarSARPulseIntegrationAnalysisMode>
    ≔ RadarSarRangeResolutionMode<stkobjects/RadarSarRangeResolutionMode>
    ≔ RadarSearchTrackPRFMode<stkobjects/RadarSearchTrackPRFMode>
    ≔ RadarSearchTrackPulseWidthMode<stkobjects/RadarSearchTrackPulseWidthMode>
    ≔ RadarSNRContourType<stkobjects/RadarSNRContourType>
    ≔ RadarSTCAttenuationType<stkobjects/RadarSTCAttenuationType>
    ≔ RadarSwerlingCase<stkobjects/RadarSwerlingCase>
    ≔ RadarWaveformSearchTrackType<stkobjects/RadarWaveformSearchTrackType>
    ≔ RainLossModelType<stkobjects/RainLossModelType>
    ≔ RCSComputeStrategy<stkobjects/RCSComputeStrategy>
    ≔ ReceiverModelType<stkobjects/ReceiverModelType>
    ≔ RectangularApertureInputType<stkobjects/RectangularApertureInputType>
    ≔ ReTransmitterOpMode<stkobjects/ReTransmitterOpMode>
    ≔ RFFilterModelType<stkobjects/RFFilterModelType>
    ≔ RouteGraphics3DMarkerType<stkobjects/RouteGraphics3DMarkerType>
    ≔ SamplingMethod<stkobjects/SamplingMethod>
    ≔ ScatteringPointModelType<stkobjects/ScatteringPointModelType>
    ≔ ScatteringPointProviderListType<stkobjects/ScatteringPointProviderListType>
    ≔ ScatteringPointProviderType<stkobjects/ScatteringPointProviderType>
    ≔ Scenario3dPointSize<stkobjects/Scenario3dPointSize>
    ≔ ScenarioEndLoopType<stkobjects/ScenarioEndLoopType>
    ≔ ScenarioRefreshDeltaType<stkobjects/ScenarioRefreshDeltaType>
    ≔ ScenarioTimeStepType<stkobjects/ScenarioTimeStepType>
    ≔ SensorAltitudeCrossingDirection<stkobjects/SensorAltitudeCrossingDirection>
    ≔ SensorAltitudeCrossingSideType<stkobjects/SensorAltitudeCrossingSideType>
    ≔ SensorAzElBoresightAxisType<stkobjects/SensorAzElBoresightAxisType>
    ≔ SensorEOIRBandImageQuality<stkobjects/SensorEOIRBandImageQuality>
    ≔ SensorEOIRBandOpticalInputMode<stkobjects/SensorEOIRBandOpticalInputMode>
    ≔ SensorEOIRBandOpticalTransmissionMode<stkobjects/SensorEOIRBandOpticalTransmissionMode>
    ≔ SensorEOIRBandQuantizationMode<stkobjects/SensorEOIRBandQuantizationMode>
    ≔ SensorEOIRBandQuantumEfficiencyMode<stkobjects/SensorEOIRBandQuantumEfficiencyMode>
    ≔ SensorEOIRBandRadiometricParameterLevelType<stkobjects/SensorEOIRBandRadiometricParameterLevelType>
    ≔ SensorEOIRBandSaturationMode<stkobjects/SensorEOIRBandSaturationMode>
    ≔ SensorEOIRBandSpatialInputMode<stkobjects/SensorEOIRBandSpatialInputMode>
    ≔ SensorEOIRBandSpectralRelativeSystemResponseUnitsType<stkobjects/SensorEOIRBandSpectralRelativeSystemResponseUnitsType>
    ≔ SensorEOIRBandSpectralShape<stkobjects/SensorEOIRBandSpectralShape>
    ≔ SensorEOIRBandWavelengthType<stkobjects/SensorEOIRBandWavelengthType>
    ≔ SensorEOIRJitterType<stkobjects/SensorEOIRJitterType>
    ≔ SensorEOIRProcessingLevelType<stkobjects/SensorEOIRProcessingLevelType>
    ≔ SensorEOIRScanMode<stkobjects/SensorEOIRScanMode>
    ≔ SensorGraphics3DInheritFrom2D<stkobjects/SensorGraphics3DInheritFrom2D>
    ≔ SensorGraphics3DProjectionTimeDependencyType<stkobjects/SensorGraphics3DProjectionTimeDependencyType>
    ≔ SensorGraphics3DProjectionType<stkobjects/SensorGraphics3DProjectionType>
    ≔ SensorGraphics3DPulseFrequencyPreset<stkobjects/SensorGraphics3DPulseFrequencyPreset>
    ≔ SensorGraphics3DPulseStyle<stkobjects/SensorGraphics3DPulseStyle>
    ≔ SensorGraphics3DVisualAppearance<stkobjects/SensorGraphics3DVisualAppearance>
    ≔ SensorLocation<stkobjects/SensorLocation>
    ≔ SensorPattern<stkobjects/SensorPattern>
    ≔ SensorPointing<stkobjects/SensorPointing>
    ≔ SensorPointingTargetedBoresightType<stkobjects/SensorPointingTargetedBoresightType>
    ≔ SensorProjectionDistanceType<stkobjects/SensorProjectionDistanceType>
    ≔ SensorRefractionType<stkobjects/SensorRefractionType>
    ≔ SensorScanMode<stkobjects/SensorScanMode>
    ≔ SolarRadiationPressureModelType<stkobjects/SolarRadiationPressureModelType>
    ≔ SolarRadiationPressureShadowModelType<stkobjects/SolarRadiationPressureShadowModelType>
    ≔ SolidTide<stkobjects/SolidTide>
    ≔ SpaceEnvironmentCrresProtonActivity<stkobjects/SpaceEnvironmentCrresProtonActivity>
    ≔ SpaceEnvironmentCrresRadiationActivity<stkobjects/SpaceEnvironmentCrresRadiationActivity>
    ≔ SpaceEnvironmentMagneticExternalField<stkobjects/SpaceEnvironmentMagneticExternalField>
    ≔ SpaceEnvironmentMagneticFieldColorMode<stkobjects/SpaceEnvironmentMagneticFieldColorMode>
    ≔ SpaceEnvironmentMagneticFieldColorScaleType<stkobjects/SpaceEnvironmentMagneticFieldColorScaleType>
    ≔ SpaceEnvironmentMagneticMainField<stkobjects/SpaceEnvironmentMagneticMainField>
    ≔ SpaceEnvironmentNasaModelsActivity<stkobjects/SpaceEnvironmentNasaModelsActivity>
    ≔ SpaceEnvironmentSAAChannel<stkobjects/SpaceEnvironmentSAAChannel>
    ≔ SpaceEnvironmentSAAFluxLevel<stkobjects/SpaceEnvironmentSAAFluxLevel>
    ≔ SpacingUnit<stkobjects/SpacingUnit>
    ≔ SphericalFlightPathAzimuthType<stkobjects/SphericalFlightPathAzimuthType>
    ≔ SpiceInterpolation<stkobjects/SpiceInterpolation>
    ≔ StarReferenceFrame<stkobjects/StarReferenceFrame>
    ≔ StatisticType<stkobjects/StatisticType>
    ≔ STKObjectType<stkobjects/STKObjectType>
    ≔ SurfaceReference<stkobjects/SurfaceReference>
    ≔ SwathComputationalMethod<stkobjects/SwathComputationalMethod>
    ≔ TargetSelectionMethod<stkobjects/TargetSelectionMethod>
    ≔ TerrainFileType<stkobjects/TerrainFileType>
    ≔ TerrainNormalType<stkobjects/TerrainNormalType>
    ≔ TextOutlineStyle<stkobjects/TextOutlineStyle>
    ≔ ThirdBodyGravitySourceType<stkobjects/ThirdBodyGravitySourceType>
    ≔ TickData<stkobjects/TickData>
    ≔ Tileset3DSourceType<stkobjects/Tileset3DSourceType>
    ≔ TimePeriodValueType<stkobjects/TimePeriodValueType>
    ≔ TimeVaryingExtremum<stkobjects/TimeVaryingExtremum>
    ≔ TIREMPolarizationType<stkobjects/TIREMPolarizationType>
    ≔ TrackMode<stkobjects/TrackMode>
    ≔ TrajectoryType<stkobjects/TrajectoryType>
    ≔ TransferFunctionType<stkobjects/TransferFunctionType>
    ≔ TransmitterModelType<stkobjects/TransmitterModelType>
    ≔ TroposphericScintillationAverageTimeChoiceType<stkobjects/TroposphericScintillationAverageTimeChoiceType>
    ≔ TroposphericScintillationFadingLossModelType<stkobjects/TroposphericScintillationFadingLossModelType>
    ≔ UrbanTerrestrialLossModelType<stkobjects/UrbanTerrestrialLossModelType>
    ≔ VectorAxesConnectType<stkobjects/VectorAxesConnectType>
    ≔ VehicleAltitudeReference<stkobjects/VehicleAltitudeReference>
    ≔ VehicleAttitude<stkobjects/VehicleAttitude>
    ≔ VehicleBreakAngleType<stkobjects/VehicleBreakAngleType>
    ≔ VehicleConsiderAnalysisType<stkobjects/VehicleConsiderAnalysisType>
    ≔ VehicleCoordinateSystem<stkobjects/VehicleCoordinateSystem>
    ≔ VehicleCorrelationListType<stkobjects/VehicleCorrelationListType>
    ≔ VehicleDirection<stkobjects/VehicleDirection>
    ≔ VehicleEllipseOptionType<stkobjects/VehicleEllipseOptionType>
    ≔ VehicleFrame<stkobjects/VehicleFrame>
    ≔ VehicleGeomagneticFluxSourceType<stkobjects/VehicleGeomagneticFluxSourceType>
    ≔ VehicleGeomagneticFluxUpdateRateType<stkobjects/VehicleGeomagneticFluxUpdateRateType>
    ≔ VehicleGPSAlmanacType<stkobjects/VehicleGPSAlmanacType>
    ≔ VehicleGPSAutomaticUpdateSourceType<stkobjects/VehicleGPSAutomaticUpdateSourceType>
    ≔ VehicleGPSElementSelectionType<stkobjects/VehicleGPSElementSelectionType>
    ≔ VehicleGPSSwitchMethod<stkobjects/VehicleGPSSwitchMethod>
    ≔ VehicleGraphics2DAttributeType<stkobjects/VehicleGraphics2DAttributeType>
    ≔ VehicleGraphics2DElevation<stkobjects/VehicleGraphics2DElevation>
    ≔ VehicleGraphics2DOffset<stkobjects/VehicleGraphics2DOffset>
    ≔ VehicleGraphics2DOptionType<stkobjects/VehicleGraphics2DOptionType>
    ≔ VehicleGraphics2DPass<stkobjects/VehicleGraphics2DPass>
    ≔ VehicleGraphics2DTimeEventType<stkobjects/VehicleGraphics2DTimeEventType>
    ≔ VehicleGraphics2DVisibleSideType<stkobjects/VehicleGraphics2DVisibleSideType>
    ≔ VehicleGraphics3DAttributeType<stkobjects/VehicleGraphics3DAttributeType>
    ≔ VehicleGraphics3DBPlaneTargetPointPosition<stkobjects/VehicleGraphics3DBPlaneTargetPointPosition>
    ≔ VehicleGraphics3DDropLineType<stkobjects/VehicleGraphics3DDropLineType>
    ≔ VehicleGraphics3DSigmaScale<stkobjects/VehicleGraphics3DSigmaScale>
    ≔ VehicleImpact<stkobjects/VehicleImpact>
    ≔ VehicleImpactLocation<stkobjects/VehicleImpactLocation>
    ≔ VehicleIntegrationModel<stkobjects/VehicleIntegrationModel>
    ≔ VehicleInterpolationMethod<stkobjects/VehicleInterpolationMethod>
    ≔ VehicleLaunch<stkobjects/VehicleLaunch>
    ≔ VehicleLaunchControl<stkobjects/VehicleLaunchControl>
    ≔ VehicleLookAheadMethod<stkobjects/VehicleLookAheadMethod>
    ≔ VehicleMethod<stkobjects/VehicleMethod>
    ≔ VehiclePartialPassMeasurement<stkobjects/VehiclePartialPassMeasurement>
    ≔ VehiclePassNumbering<stkobjects/VehiclePassNumbering>
    ≔ VehiclePredictorCorrectorScheme<stkobjects/VehiclePredictorCorrectorScheme>
    ≔ VehiclePropagationFrame<stkobjects/VehiclePropagationFrame>
    ≔ VehicleSGP4AutomaticUpdateSourceType<stkobjects/VehicleSGP4AutomaticUpdateSourceType>
    ≔ VehicleSGP4TLESelectionType<stkobjects/VehicleSGP4TLESelectionType>
    ≔ VehicleSlewMode<stkobjects/VehicleSlewMode>
    ≔ VehicleSlewTimingBetweenTargetType<stkobjects/VehicleSlewTimingBetweenTargetType>
    ≔ VehicleSolarFluxGeomagneticType<stkobjects/VehicleSolarFluxGeomagneticType>
    ≔ VehicleSpaceEnvironmentApSource<stkobjects/VehicleSpaceEnvironmentApSource>
    ≔ VehicleSpaceEnvironmentComputationMode<stkobjects/VehicleSpaceEnvironmentComputationMode>
    ≔ VehicleSpaceEnvironmentDetectorGeometry<stkobjects/VehicleSpaceEnvironmentDetectorGeometry>
    ≔ VehicleSpaceEnvironmentDetectorType<stkobjects/VehicleSpaceEnvironmentDetectorType>
    ≔ VehicleSpaceEnvironmentDoseChannel<stkobjects/VehicleSpaceEnvironmentDoseChannel>
    ≔ VehicleSpaceEnvironmentF10P7SourceType<stkobjects/VehicleSpaceEnvironmentF10P7SourceType>
    ≔ VehicleSpaceEnvironmentMaterial<stkobjects/VehicleSpaceEnvironmentMaterial>
    ≔ VehicleSpaceEnvironmentShapeModel<stkobjects/VehicleSpaceEnvironmentShapeModel>
    ≔ VehicleWaypointComputationMethod<stkobjects/VehicleWaypointComputationMethod>
    ≔ VehicleWaypointInterpolationMethod<stkobjects/VehicleWaypointInterpolationMethod>
    ≔ VolumetricDataExportFormatType<stkobjects/VolumetricDataExportFormatType>
    ≔ VolumetricDefinitionType<stkobjects/VolumetricDefinitionType>
    ≔ VolumetricDisplayQualityType<stkobjects/VolumetricDisplayQualityType>
    ≔ VolumetricDisplayVolumeType<stkobjects/VolumetricDisplayVolumeType>
    ≔ VolumetricLegendNumericNotationType<stkobjects/VolumetricLegendNumericNotationType>
    ≔ VolumetricLevelOrder<stkobjects/VolumetricLevelOrder>
    ≔ VolumetricSaveComputedDataType<stkobjects/VolumetricSaveComputedDataType>
    ≔ VolumetricSpatialCalculationEvaluationType<stkobjects/VolumetricSpatialCalculationEvaluationType>
    ≔ VolumetricVolumeGridExportType<stkobjects/VolumetricVolumeGridExportType>
    ≔ WaveformSelectionStrategyType<stkobjects/WaveformSelectionStrategyType>
    ≔ WaveformType<stkobjects/WaveformType>

