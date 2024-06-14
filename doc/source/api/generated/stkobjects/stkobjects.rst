
The ``STKObjects`` module
=========================


.. py::module:: ansys.stk.core.stkobjects


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~IDataProviderResult`
              - Provide methods to access the results returned by the data provider.

            * - :pyclass:`~IDataProviderTimeVarying`
              - Represents the Time-dependent Data Provider (for instance satellite position).

            * - :pyclass:`~IDataProviderInterval`
              - Represents the Interval Data Provider (for instance facility lighting times).

            * - :pyclass:`~IDataProviderFixed`
              - Represents the Fixed Data Provider (i.e. non time dependent like facility position).

            * - :pyclass:`~IDataProviderResultStatistics`
              - Compute statistics and time varying extremums on a data set when available.

            * - :pyclass:`~IDataProviderInfo`
              - Provide methods for retrieving the information about data providers.

            * - :pyclass:`~IDataProviderCollection`
              - Represents a collection of data providers.

            * - :pyclass:`~IDataProviderResultDataSet`
              - Represents a dataset element.

            * - :pyclass:`~IDataProviderResultDataSetCollection`
              - Represents a collection of dataset elements.

            * - :pyclass:`~IDataProviderResultInterval`
              - Represents a data interval element.

            * - :pyclass:`~IDataProviderResultIntervalCollection`
              - Represents a collection of intervals.

            * - :pyclass:`~IDataProviderResultSubSection`
              - Represents a sub-section data element.

            * - :pyclass:`~IDataProviderResultSubSectionCollection`
              - Represents a collection of sub-section data elements.

            * - :pyclass:`~IDataProviderResultTextMessage`
              - Represents notification/failure message returned by the data provider.

            * - :pyclass:`~IDataProviderElement`
              - Provide methods to access the information about the element (for instance ``x``).

            * - :pyclass:`~IDataProviderElements`
              - Represents a collection of elements in the data provider (for instance ``x``, ``y``, ``z``).

            * - :pyclass:`~IDataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :pyclass:`~IDataProvider`
              - Represents the Sub Data Provider (i.e. ``Fixed`` in ``Cartesian Position`` group on satellites, or ``Cartesian Position`` on facilities).

            * - :pyclass:`~IDataProviders`
              - Represents a collection of data providers.

            * - :pyclass:`~IDataProviderGroup`
              - Represents a group of data providers (for instance ``Cartesian Position`` on satellite).

            * - :pyclass:`~IDataProviderResultStatisticResult`
              - Represents the results of computing a data set statistics using IAgDrStatistics.ComputeStatistic method.

            * - :pyclass:`~IDataProviderResultTimeVaryingExtremumResult`
              - Represents the results of computing a data set time varying extremum using IAgDrStatistics.ComputeTimeVarExtremum method.

            * - :pyclass:`~IGraphics3DDataDisplayCollection`
              - Data Display Text.

            * - :pyclass:`~IIntervalCollection`
              - AgIntervalCollection used to access the Intervals Collection interface.

            * - :pyclass:`~ITimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :pyclass:`~IStkObject`
              - Represents the instance of STK object.

            * - :pyclass:`~IAccessInterval`
              - Base interface for IAgTimePeriod and IAgIntervalCollection.

            * - :pyclass:`~IAccessTimeEventIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :pyclass:`~IAccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :pyclass:`~IStkAccessGraphics`
              - Provide access to the Graphics for Access Computations.

            * - :pyclass:`~IStkAccessAdvanced`
              - Provide access to the Advanced properties for Access Computations.

            * - :pyclass:`~IStkAccess`
              - Provide access to the Data Providers and access computations.

            * - :pyclass:`~IAccessConstraintCollection`
              - AgAccessConstraintCollection used to access the list of constraints.

            * - :pyclass:`~IImmutableIntervalCollection`
              - IAgImmutableIntervalCollection represents a immutable (read-only) collection of intervals.

            * - :pyclass:`~IFigureOfMeritDefinition`
              - Figure of Merit definition.

            * - :pyclass:`~IFigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :pyclass:`~IFigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :pyclass:`~IFigureOfMeritGraphics`
              - 2D graphics for a Figure of Merit.

            * - :pyclass:`~ICoverageAssetListCollection`
              - Asset List.

            * - :pyclass:`~IAvailableFeatures`
              - Define methods to inquiry available and supported features, object types, etc.

            * - :pyclass:`~IStkCentralBodyCollection`
              - A collection of available central bodies.

            * - :pyclass:`~IStkPreferences`
              - Configures STK preferences.

            * - :pyclass:`~IOnePointAccessConstraint`
              - One Point Access Result.

            * - :pyclass:`~IOnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :pyclass:`~IOnePointAccessResult`
              - One Point Access Result.

            * - :pyclass:`~IOnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :pyclass:`~IOnePointAccess`
              - One Point Access.

            * - :pyclass:`~IKeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :pyclass:`~IStkObjectElementCollection`
              - Represents a collection of STK objects.

            * - :pyclass:`~IStkObjectCollection`
              - Represents a collection of STK objects.

            * - :pyclass:`~IObjectCoverageFigureOfMerit`
              - Provide access to the Figure of Merit on the Object Coverage tool.

            * - :pyclass:`~IStkObjectCoverage`
              - Provide access to the Data Providers on an ObjectCoverage Object.

            * - :pyclass:`~IStdMilitary2525bSymbols`
              - Represents the automation interface to generate 2525b symbology markers (military standard).

            * - :pyclass:`~IStkObjectRoot`
              - Represents the automation interface supported by the root object of the Automation Object Model.

            * - :pyclass:`~IObjectLink`
              - IAgObjectLink provides methods and properties of elements stored in IAgObjectLinkCollection collection.

            * - :pyclass:`~ILinkToObject`
              - IAgLinkToObject represents a link to STK object.

            * - :pyclass:`~IObjectLinkCollection`
              - IAgObjectLinkCollection represents a collection of names of STK objects that are available in the current scenario.

            * - :pyclass:`~IAnimation`
              - Provide methods to control scenario animation.

            * - :pyclass:`~IStkObjectModelContext`
              - Represents a factory class to create instances of the AgStkObjectRoot class.

            * - :pyclass:`~IComponentInfo`
              - Interface for a component.

            * - :pyclass:`~IComponentInfoCollection`
              - The collection of components and component folders.

            * - :pyclass:`~IComponentDirectory`
              - Manages all components.

            * - :pyclass:`~ICloneable`
              - Interface for a component.

            * - :pyclass:`~IComponentLinkEmbedControl`
              - Interface for a control which manages the linking or embedding of a component from the component browser.

            * - :pyclass:`~ISwath`
              - Provide access to the Swath properties.

            * - :pyclass:`~IDisplayTimesData`
              - Base Interface IAgDisplayTimesData. IAgIntervalCollection, IAgDuringAccess and IAgDisplayTimesTimeComponent derive from this.

            * - :pyclass:`~IDisplayTime`
              - The display time interface.

            * - :pyclass:`~IBasicAzElMask`
              - AgAzElMask Azimuth-elevation access points.

            * - :pyclass:`~ILabelNote`
              - AgLabelNote used to access the label note.

            * - :pyclass:`~ILabelNoteCollection`
              - AgLabelNoteCollection used to access the list of label notes.

            * - :pyclass:`~IDuringAccess`
              - AgDuringAccess used to access the display intervals and Access objects.

            * - :pyclass:`~IDisplayTimesTimeComponent`
              - Interface provides methods to configure the display times using Timeline API components.

            * - :pyclass:`~ITerrainNormSlopeAzimuth`
              - AgTerrainNormSlopeAzimuth used to access the Slope/Azimuth data for the TerrainNormal.

            * - :pyclass:`~IAccessTime`
              - IAgAccessTime Interface, part of the target times scheme for specifying when a satellite or sensor can access a given object.

            * - :pyclass:`~IAccessTimeCollection`
              - IAgAccessTimeCollection Interface.

            * - :pyclass:`~ITerrainNormData`
              - Base Interface IAgTerrainNormData. IAgTerrainNormSlopeAzimuth derives from this interface.

            * - :pyclass:`~ILifetimeInformation`
              - Provide the information about the lifetime of the object.

            * - :pyclass:`~IVehicleLeadTrailData`
              - Base interface IAgVeLeadTrailData.

            * - :pyclass:`~IVehicleLeadTrailDataFraction`
              - The percentage of the leading or trailing portion of a vehicle's path that will display in the 2D or 3D window.

            * - :pyclass:`~IVehicleLeadTrailDataTime`
              - Configure the amount of time to display the vehicle's path in 2D or 3D window.

            * - :pyclass:`~IStkCentralBodyEllipsoid`
              - Provide information about the central body's equatorial and polar radii.

            * - :pyclass:`~IStkCentralBody`
              - A central body interface.

            * - :pyclass:`~IAccessConstraint`
              - AgAccessConstraint used to access the AccessConstraint attributes.

            * - :pyclass:`~IAccessConstraintTimeSlipRange`
              - IAgAccessCnstrTimeSlipRange used to access the Time Slip Range.

            * - :pyclass:`~IAccessConstraintZone`
              - IAgAccessCnstrZone used to access the Zone access constraints.

            * - :pyclass:`~IAccessConstraintExclZonesCollection`
              - AgAccessCnstrExclZonesCollection used to access the Exclusion Zones List interface.

            * - :pyclass:`~IAccessConstraintThirdBody`
              - Do not use this interface, as it is deprecated. Use IAgAccessCnstrCbObstruction instead. Access Constraint Used for Third Body Obstructions.

            * - :pyclass:`~IAccessConstraintIntervals`
              - Access Constraint used for time intervals.

            * - :pyclass:`~IAccessConstraintObjExAngle`
              - Access Constraint used for Object Exclusion Angles.

            * - :pyclass:`~IAccessConstraintCondition`
              - Access Constraint used for lighting conditions.

            * - :pyclass:`~IAccessConstraintCentralBodyObstruction`
              - Access Constraint used for Central Body Obstruction.

            * - :pyclass:`~IAccessConstraintAngle`
              - Access Constraint used for angle constraints.

            * - :pyclass:`~IAccessConstraintMinMax`
              - Access Constraint used for min/max constraints.

            * - :pyclass:`~IAccessConstraintPluginMinMax`
              - Access Constraint used for min/max plugin constraints.

            * - :pyclass:`~IAccessConstraintCrdnConstellation`
              - Access Constraint used for Vector Constraints.

            * - :pyclass:`~IAccessConstraintBackground`
              - Access Constraint used for Background Constraints.

            * - :pyclass:`~IAccessConstraintGroundTrack`
              - Access Constraint used for GroundTrack Constraints.

            * - :pyclass:`~IAccessConstraintAnalysisWorkbench`
              - Access Constraint used for Analysis Workbench Constraints.

            * - :pyclass:`~IAccessConstraintAnalysisWorkbenchCollection`
              - IAgAccessCnstrAWBCollection used to access angle, vector and condition constraint List interface.

            * - :pyclass:`~IAccessConstraintGrazingAltitude`
              - Access Constraint used for Grazing Altitude Constraint.

            * - :pyclass:`~ILevelAttribute`
              - AgLevelAttribute used to access individual contour level attributes.

            * - :pyclass:`~ILevelAttributeCollection`
              - AgLevelAttributeCollection used to access level attributes.

            * - :pyclass:`~IGraphics2DRangeContours`
              - AgGfxRangeContours used to access contours of 2-d object.

            * - :pyclass:`~IGraphics3DModelFile`
              - IAgVOModelFile Interface. Used to specify the model's file.

            * - :pyclass:`~IGraphics3DArticulationFile`
              - Interface for VO model articulations.

            * - :pyclass:`~IGraphics3DModelGltfImageBased`
              - glTF Reflection Settings Interface.

            * - :pyclass:`~IVehicleEllipseDataElement`
              - Ground ellipse data.

            * - :pyclass:`~IVehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :pyclass:`~IVehicleGroundEllipseElement`
              - Ground ellipse.

            * - :pyclass:`~IVehicleGroundEllipsesCollection`
              - Ground Ellipses.

            * - :pyclass:`~IGraphics3DDataDisplayElement`
              - Interface for 3D Graphics window data display element.

            * - :pyclass:`~IGraphics3DPointableElementsElement`
              - Pointable elements interface for 3D model pointing.

            * - :pyclass:`~IGraphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :pyclass:`~IGraphics3DModelPointing`
              - List of pointable model elements.

            * - :pyclass:`~IGraphics3DLabelSwapDistance`
              - Interface to control the level of detail in labels and other screen objects at specified distances.

            * - :pyclass:`~IGraphics3DAzElMask`
              - Use to display labels and adjust the translucency of the azimuth-elevation mask for a facility, place or target.

            * - :pyclass:`~IGraphics3DBorderWall`
              - Border Wall Properties.

            * - :pyclass:`~IGraphics3DRangeContours`
              - AgVORangeContour used to access the 3D RangeContour attributes.

            * - :pyclass:`~IGraphics3DOffsetLabel`
              - AgVOOffsetLabel used to access the 3D Label attributes.

            * - :pyclass:`~IGraphics3DOffsetRotate`
              - AgVOOffsetRotate used to access the 3D Rotational attributes.

            * - :pyclass:`~IGraphics3DOffsetTransformation`
              - AgVOOffsetTrans used to access the 3D Translational attributes.

            * - :pyclass:`~IGraphics3DOffsetAttach`
              - Interface for specifying attach points for the attachment of lines to objects.

            * - :pyclass:`~IGraphics3DOffset`
              - AgVOOffset used to access the 3D offset attributes.

            * - :pyclass:`~IGraphics3DMarkerData`
              - Base Interface IAgVOMarkerData.

            * - :pyclass:`~IGraphics3DMarkerShape`
              - AgVOMarkerShape used to access the 3D markerShape attributes.

            * - :pyclass:`~IGraphics3DMarkerFile`
              - AgVOMarkerFile used to access the 3D MarkerFile attributes.

            * - :pyclass:`~IGraphics3DMarker`
              - AgVOMarker used to access the Marker values.

            * - :pyclass:`~IGraphics3DModelTransformation`
              - IAgVOModelTrans Interface. Used to modify the transformation value.

            * - :pyclass:`~IGraphics3DModelTransformationCollection`
              - IAgVOModelTransCollection Interface. A collection of available transformations in the model.

            * - :pyclass:`~IGraphics3DModelArtic`
              - ModelArticulation Interface.

            * - :pyclass:`~IGraphics3DDetailThreshold`
              - AgVODetailThreshold used to access the 3D DetailThreshold values.

            * - :pyclass:`~IGraphics3DModelItem`
              - AgVOModelItem used to access the Model Item in the ModelCollection.

            * - :pyclass:`~IGraphics3DModelCollection`
              - IAgVOModelCollection used to access the 3D Model List.

            * - :pyclass:`~IGraphics3DModelData`
              - IAgVOModelData base interface. IAgVOModelFile and IAgVOModelCollection derive from this.

            * - :pyclass:`~IGraphics3DModel`
              - AgVOModel used to access the 3D model attributes.

            * - :pyclass:`~IPointTargetGraphics3DModel`
              - AgPtTargetVOModel used to access the 3D model attributes.

            * - :pyclass:`~IGraphics3DReferenceAnalysisWorkbenchComponent`
              - IAgVORefCrdn used to access the shared properties of all 3D RefCrdn.

            * - :pyclass:`~IGraphics3DReferenceVectorGeometryToolVector`
              - Configure the visual representation of a Vector Geometry vector component in 3D.

            * - :pyclass:`~IGraphics3DReferenceVectorGeometryToolAxes`
              - Configure the visual representation of a Vector Geometry axes component in 3D.

            * - :pyclass:`~IGraphics3DReferenceVectorGeometryToolAngle`
              - Configure the visual representation of a Vector Geometry angle component in 3D.

            * - :pyclass:`~IGraphics3DReferenceVectorGeometryToolPoint`
              - Configure the visual representation of a Vector Geometry point component in 3D.

            * - :pyclass:`~IGraphics3DReferenceVectorGeometryToolPlane`
              - Configure the visual representation of a Vector Geometry plane component in 3D.

            * - :pyclass:`~IGraphics3DReferenceAnalysisWorkbenchCollection`
              - Manages the collection of elements that are used to visualize the Vector Geometry Tool components in 3D.

            * - :pyclass:`~IGraphics3DVector`
              - Configures the Vector Geometry Tool 3D visualization.

            * - :pyclass:`~IGraphics3DVaporTrail`
              - Configure the vapor trail 3D attributes.

            * - :pyclass:`~ILLAPosition`
              - Interface to set and retrieve the LLA position type.

            * - :pyclass:`~ILLAGeocentric`
              - Geocentric LLA position interface:.

            * - :pyclass:`~ILLAGeodetic`
              - Geodetic LLA position interface.

            * - :pyclass:`~IOrbitStateCoordinateSystem`
              - Interface for selecting coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :pyclass:`~IOrbitStateCartesian`
              - Cartesian coordinate type.

            * - :pyclass:`~IClassicalSizeShape`
              - Base Interface for SizeShape property. IAgClassicalSizeShapeAltitude, IAgClassicalSizeShapeMeanMotion, IAgClassicalSizeShapePeriod, IAgClassicalSizeShapeRadius and IAgClassicalSizeShapeSemimajorAxis derive from this.

            * - :pyclass:`~IClassicalSizeShapeAltitude`
              - Interface for specifying orbit size and shape using altitude.

            * - :pyclass:`~IClassicalSizeShapeMeanMotion`
              - Interface for specifying orbit size and shape using Mean Motion and Eccentricity.

            * - :pyclass:`~IClassicalSizeShapePeriod`
              - Interface for specifying orbit size and shape using Period and Eccentricity.

            * - :pyclass:`~IClassicalSizeShapeRadius`
              - Interface for specifying orbit size and shape using Radius.

            * - :pyclass:`~IClassicalSizeShapeSemimajorAxis`
              - Interface for specifying orbit size and shape using Semimajor Axis and Eccentricity.

            * - :pyclass:`~IOrientationAscNode`
              - Base Interface to IAgOrientationAscNodeLAN and IAgOrientationAscNodeRAAN.

            * - :pyclass:`~IOrientationAscNodeLAN`
              - Longitude of Ascending Node: the Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :pyclass:`~IOrientationAscNodeRAAN`
              - Right Ascension of Ascending Node: the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :pyclass:`~IClassicalOrientation`
              - Interface for specifying orbit orientation in the Classical (Keplerian) system.

            * - :pyclass:`~IClassicalLocation`
              - Base Interface of all IAgClassicalLocation* interfaces.

            * - :pyclass:`~IClassicalLocationArgumentOfLatitude`
              - Interface for Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~IClassicalLocationEccentricAnomaly`
              - Interface for Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~IClassicalLocationMeanAnomaly`
              - Interface for Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~IClassicalLocationTimePastAN`
              - Interface for Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~IClassicalLocationTimePastPerigee`
              - Interface for Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~IClassicalLocationTrueAnomaly`
              - Interface for True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~IOrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :pyclass:`~IGeodeticSize`
              - Base Interface IAgGeodeticSize. IAgGeodeticSizeAltitude and IAgGeodeticSizeRadius derive from this.

            * - :pyclass:`~IGeodeticSizeAltitude`
              - Interface for Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :pyclass:`~IGeodeticSizeRadius`
              - Interface for Radius and Radius Rate (for Geodetic coordinate type).

            * - :pyclass:`~IOrbitStateGeodetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :pyclass:`~IDelaunayActionVariable`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :pyclass:`~IDelaunayL`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :pyclass:`~IDelaunayLOverSQRTmu`
              - Interface for Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :pyclass:`~IDelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :pyclass:`~IDelaunayHOverSQRTmu`
              - Interface for Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :pyclass:`~IDelaunayG`
              - Interface for Delaunay Variagle G, the magnitude of the orbital angular momentum.

            * - :pyclass:`~IDelaunayGOverSQRTmu`
              - Interface for Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :pyclass:`~IOrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :pyclass:`~IEquinoctialSizeShapeMeanMotion`
              - Interface for Mean Motion, an element of the Equinoctial coordinate type.

            * - :pyclass:`~IEquinoctialSizeShapeSemimajorAxis`
              - Interface for Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :pyclass:`~IOrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :pyclass:`~IFlightPathAngle`
              - Base Interface IAgFlightPathAngle. IAgMixedSphericalFPAHorizontal, IAgMixedSphericalFPAVertical, IAgSphericalFPAHorizontal and IAgSphericalFPAVertical derive from this.

            * - :pyclass:`~IMixedSphericalFPAHorizontal`
              - Interface for Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :pyclass:`~IMixedSphericalFPAVertical`
              - Interface for Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :pyclass:`~IOrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :pyclass:`~ISphericalFPAHorizontal`
              - Interface for Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :pyclass:`~ISphericalFPAVertical`
              - Interface for Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :pyclass:`~IOrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :pyclass:`~ISpatialState`
              - Represents a position and an attitude of an object.

            * - :pyclass:`~IVehicleSpatialInfo`
              - Represents a spatial information of the vehicle.

            * - :pyclass:`~IProvideSpatialInfo`
              - Provide methods for accessing spatial information for an object.

            * - :pyclass:`~IScenSpaceEnvironment`
              - no helpstring provided.

            * - :pyclass:`~IRadarClutterMap`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar clutter map.

            * - :pyclass:`~IRadarCrossSection`
              - Provide access to the properties and methods defining radar cross section.

            * - :pyclass:`~IRFEnvironment`
              - Provide access to the properties and methods defining the RF environment.

            * - :pyclass:`~ILaserEnvironment`
              - Provide access to the properties and methods defining the laser environment.

            * - :pyclass:`~IScenarioGraphics`
              - IAgScGraphics Interface for Scenario-level 2D Graphics attributes.

            * - :pyclass:`~IScenarioEarthData`
              - IAgScEarthData Interface for Earth Orientation Parameters.

            * - :pyclass:`~IScenarioAnimationTimePeriod`
              - IAgScAnimationTimePeriod defines methods and properties to configure the scenario's animation time.

            * - :pyclass:`~IScenarioAnimation`
              - IAgScAnimation Interface for Scenario-level properties that control the animation cycle, animation step definition and the intervals between refresh updates in the 2D and 3D windows.

            * - :pyclass:`~ITerrain`
              - IAgTerrain Interface.

            * - :pyclass:`~ITerrainCollection`
              - IAgTerrainCollection lists all the terrain data files available in this scenario for visualization and analysis.

            * - :pyclass:`~ICentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :pyclass:`~ICentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :pyclass:`~ITileset3D`
              - IAg3DTileset Interface.

            * - :pyclass:`~ITilesetCollection3D`
              - IAg3DTilesetCollection lists all the terrain data files available in this scenario for visualization and analysis.

            * - :pyclass:`~IScenarioGenDatabase`
              - Represents a scenario database.

            * - :pyclass:`~IScenarioGenDatabaseCollection`
              - Represents a collection of the scenario's databases.

            * - :pyclass:`~IScenario3dFont`
              - IAgSc3dFont Interface.

            * - :pyclass:`~IScenarioGraphics3D`
              - Scenario 3D Graphics Attributes.

            * - :pyclass:`~ITimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :pyclass:`~IScenario`
              - IAgScenario Interface for Scenario-level properties.

            * - :pyclass:`~ICelestialBodyInfo`
              - The interface represents information associated with a celestial body.

            * - :pyclass:`~ICelestialBodyCollection`
              - Represents a collection of celestial bodies.

            * - :pyclass:`~IAccessAdvanced`
              - Interface for configuring advanced targeting access computation properties.

            * - :pyclass:`~ISensorAccessAdvanced`
              - Interface for configuring sensor's advanced targeting access computation properties.

            * - :pyclass:`~IRefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :pyclass:`~IRefractionModelBase`
              - A base interface for the Refraction Models.

            * - :pyclass:`~IRefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :pyclass:`~IRefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :pyclass:`~IRefractionModelSCFMethod`
              - SCF Method.

            * - :pyclass:`~IScheduleTime`
              - IAgScheduleTime Interface, part of the target times scheme for specifying when a satellite or sensor can access a given object.

            * - :pyclass:`~IScheduleTimeCollection`
              - You can modify the scheduled times by disabling Use Access Times.

            * - :pyclass:`~IDisplayDistance`
              - Base interface IAgDisplayDistance. IAgSnProjDisplayDistance, IAgSnProjConstantAlt and IAgSnProjObjectAlt derive from this.

            * - :pyclass:`~ISensorProjectionDisplayDistance`
              - IAgSnProjDisplayDistance Interface for setting projection altitude options for a sensor.

            * - :pyclass:`~ISensorProjection`
              - IAgSnProjection Interface for setting and retrieving 2D Graphics Projection properties for a sensor.

            * - :pyclass:`~ISensorGraphics`
              - IAgSnGraphics Interface for a sensor's 2D Graphics properties.

            * - :pyclass:`~ISensorGraphics3DPulse`
              - IAgSnVOPulse Interface, for setting and retrieving 3D Graphics Pulse properties of a sensor.

            * - :pyclass:`~ISensorGraphics3DOffset`
              - IAgSnVOOffset Interface for setting and retrieving 3D Graphics Vertex Offset properties of a sensor.

            * - :pyclass:`~ISensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :pyclass:`~ISensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :pyclass:`~ISensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :pyclass:`~ISensorGraphics3D`
              - IAgSnVO Interface for a sensor's 3D Graphics properties.

            * - :pyclass:`~ISensorPattern`
              - Base interface IAgSnPattern. IAgSnComplexConicPattern, IAgSnCustomPattern, IAgSnHalfPowerPattern, IAgSnRectangularPattern, IAgSnSARPattern, IAgSnEOIRPattern and IAgSnSimpleConicPattern implement this interface.

            * - :pyclass:`~ISensorSimpleConicPattern`
              - IAgSnSimpleConicPattern Interface for a sensor pattern defined by a simple cone angle.

            * - :pyclass:`~ISensorSARPattern`
              - IAgSnSARPattern Interface for the Synthetic Aperture Radar (SAR) sensor type, designed to model the field of regard of a SAR sensor with respect to the surface of the Earth.

            * - :pyclass:`~ISensorRectangularPattern`
              - IAgSnRectangularPattern Interface for rectangular sensor types typically used with satellites or aircraft for modeling the field of view of instruments such as push broom sensors and star trackers.

            * - :pyclass:`~ISensorHalfPowerPattern`
              - IAgSnHalfPowerPattern Interface for half power sensors designed to model parabolic antennas.

            * - :pyclass:`~ISensorCustomPattern`
              - IAgSnCustomPattern Interface for custom sensor patterns.

            * - :pyclass:`~ISensorComplexConicPattern`
              - IAgSnComplexConicPattern Interface for defining sensor patterns by the inner and outer half angles and minimum and maximum clock angles of the sensor's cone.

            * - :pyclass:`~ISensorEOIRRadiometricPair`
              - IAgSnEOIRRadiometricPair Interface for defining the individual band properties.

            * - :pyclass:`~ISensorEOIRSensitivityCollection`
              - IAgSnEOIRFCollection Interface. A collection of Radiometric pairs defining the Sensitivities.

            * - :pyclass:`~ISensorEOIRSaturationCollection`
              - IAgSnEOIRSaturationCollection Interface. A collection of Radiometric pairs defining the saturations.

            * - :pyclass:`~ISensorEOIRBand`
              - IAgSnEOIRBand Interface for defining the individual band properties.

            * - :pyclass:`~ISensorEOIRBandCollection`
              - IAgSnEOIRBandCollection Interface. A collection of EOIR bands.

            * - :pyclass:`~ISensorEOIRPattern`
              - IAgSnEOIRPattern Interface for a sensor pattern.

            * - :pyclass:`~ISensorPointingTargetedBoresight`
              - Base interface IAgSnPtTrgtBsight. IAgSnPtTrgtBsightFixed and IAgSnPtTrgtBsightTrack derive from this.

            * - :pyclass:`~ISensorPointingTargetedBoresightTrack`
              - IAgSnPtTrgtBsightTrack Interface for targeted sensor with fixed boresight.

            * - :pyclass:`~ISensorPointingTargetedBoresightFixed`
              - IAgSnPtTrgtBsightFixed Interface for targeted sensors with fixed boresight.

            * - :pyclass:`~ISensorTarget`
              - IAgSnTarget Interface.

            * - :pyclass:`~ISensorTargetCollection`
              - IAgSnTargetCollection Interface. A collection of targets.

            * - :pyclass:`~ISensorPointing`
              - Base interface IAgSnPointing. IAgSnPt3DModel, IAgSnPtExternal, IAgSnPtFixed, IAgSnPtFixedAxes, IAgSnPtGrazingAlt, IAgSnPtTargeted, IAgSnPtAlongVector and IAgSnPtSchedule implement this interface.

            * - :pyclass:`~ISensorPointingTargeted`
              - IAgSnPtTargeted Interface for targeted sensors.

            * - :pyclass:`~ISensorPointingSpinning`
              - IAgSnPtSpinning Interface for defining the pointing properties of a spinning sensor.

            * - :pyclass:`~ISensorPointingGrazingAltitude`
              - IAgSnPtGrazingAlt Interface for a sensor pointed in such a way that the boresight vector will graze the central body at a specified altitude.

            * - :pyclass:`~ISensorPointingFixedAxes`
              - IAgSnPtFixedAxes Interface for sensors pointed with reference to a set of reference axes.

            * - :pyclass:`~ISensorPointingFixed`
              - IAgSnPtFixed Interface for sensors that are fixed in the parent object's body coordinate frame, so that they always point in the same direction relative to the parent.

            * - :pyclass:`~ISensorPointingExternal`
              - IAgSnPtExternal Interface for antennas oriented with a custom pointing file.

            * - :pyclass:`~ISensorPointing3DModel`
              - IAgSnPt3DModel Interface for a sensor with pointing along one of the available elements of a 3D model.

            * - :pyclass:`~ISensorPointingAlongVector`
              - IAgSnPtAlongVector Interface for a sensor whose alignment is controlled by a pair of vectors defined using the Vector Geometry tool.

            * - :pyclass:`~ISensorPointingSchedule`
              - IAgSnPtSchedule is a placeholder interface to handle Sensor Schedule pointing type. Use Point path/to/sensor Schedule connect command to control scheduled sensor pointing.

            * - :pyclass:`~IAzElMaskData`
              - Base interface IAgAzElMaskData. IAgSnAzElMaskFile implements this interface.

            * - :pyclass:`~ISensorAzElMaskFile`
              - IAgSnAzElMaskFile Interface.

            * - :pyclass:`~ISensorCommonTasks`
              - The common tasks available for the sensor object.

            * - :pyclass:`~ILocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :pyclass:`~ISensor`
              - Provide access to the properties and methods used in defining a sensor object.

            * - :pyclass:`~ISensorProjectionConstantAltitude`
              - IAgSnProjConstantAlt Interface for setting projection altitude options for constant altitude for a sensor.

            * - :pyclass:`~ISensorProjectionObjectAltitude`
              - IAgSnProjObjectAlt Interface for setting projection altitude options for object altitude for a sensor.

            * - :pyclass:`~IAtmosphere`
              - Provide access to the properties and methods defining the local atmosphere.

            * - :pyclass:`~IRadarClutterMapInheritable`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar inheritable clutter map.

            * - :pyclass:`~IRadarCrossSectionInheritable`
              - Provide access to the properties and methods defining a inheritable radar cross section.

            * - :pyclass:`~IPlatformLaserEnvironment`
              - Provide access to the properties and methods defining the laser environment for a platform.

            * - :pyclass:`~IPlatformRFEnvironment`
              - Provide access to the properties and methods defining the platform RF environment.

            * - :pyclass:`~IRadarCrossSectionGraphics3D`
              - IAgRadarCrossSectionVO Interface for radar cross section 3D properties.

            * - :pyclass:`~IRadarCrossSectionGraphics`
              - IAgRadarCrossSectionGraphics Interface for radar cross section graphics properties.

            * - :pyclass:`~ITargetGraphics`
              - IAgTargetGraphics used to access the 2-d graphics properties for a Target object.

            * - :pyclass:`~ITargetGraphics3D`
              - IAgTargetVO Interface. For 3D properties of a Target object.

            * - :pyclass:`~ITarget`
              - Provide access to the properties and methods used in defining a target object.

            * - :pyclass:`~IAreaTypeEllipse`
              - AgAreaTypeEllipse used to access the MajorAxis MinorAxis and Bearing of the AreaTarget AreaType.

            * - :pyclass:`~IAreaTypePatternCollection`
              - AgAreaTypePatternCollection used to access the List of coords of the AreaTarget AreaType.

            * - :pyclass:`~IAreaTargetCommonTasks`
              - AreaTarget common tasks.

            * - :pyclass:`~IAreaTypeData`
              - Base interface IAgAreaTypeData. IAgAreaTypePatternCollection and IAgAreaTypeEllipse derive from it.

            * - :pyclass:`~IAreaTargetGraphics`
              - AgATGraphics used to access the 2D Graphics attributes of an AreaTarget interface.

            * - :pyclass:`~IAreaTargetGraphics3D`
              - AgATVO used to access the 3D attributes of an AreaTarget interface.

            * - :pyclass:`~IAreaTarget`
              - Provide access to the properties and methods defining an AreaTarget object.

            * - :pyclass:`~IAreaTypePattern`
              - AgAreaTypePattern used to access the List of coordinates of the AreaTarget AreaType interface.

            * - :pyclass:`~IPlanetPositionFile`
              - IAgPlPosFile Interface.

            * - :pyclass:`~IPlanetPositionCentralBody`
              - IAgPlPosCentralBody Interface.

            * - :pyclass:`~IPlanetCommonTasks`
              - IAgPlCommonTasks.

            * - :pyclass:`~IPositionSourceData`
              - Base interface to IAgPlPosCentralBody and IAgPlPosFile.

            * - :pyclass:`~IOrbitDisplayData`
              - IAgOrbitDisplayData Interface. IAgPlOrbitDisplayTime derives from this.

            * - :pyclass:`~IPlanetOrbitDisplayTime`
              - IAgPlOrbitDisplayTime Interface.

            * - :pyclass:`~IPlanetGraphics`
              - AgPlGraphics used to access the 2D graphics of the planet.

            * - :pyclass:`~IPlanetGraphics3D`
              - AgPlVO interface. Used to access the 3D graphics of the planet.

            * - :pyclass:`~IPlanet`
              - Provide access to the properties and methods used in defining a planet object.

            * - :pyclass:`~IStarGraphics`
              - AgStGraphics used to access the Star's 2D graphics.

            * - :pyclass:`~IStarGraphics3D`
              - AgStVO used to access the Star's 3D graphics.

            * - :pyclass:`~IStar`
              - Provide access to the properties and methods used in defining a star object.

            * - :pyclass:`~IFacilityGraphics`
              - AgFaGraphics used to access the 2D graphics for a Facility object interface.

            * - :pyclass:`~IFacilityGraphics3D`
              - AgFaVO Interface. For 3D properties of a Facility object interface.

            * - :pyclass:`~IFacility`
              - Provide access to the properties and methods used in defining a facility object.

            * - :pyclass:`~IPlaceGraphics`
              - IAgPlaceGraphics used to access the 2-d graphics properties for a Place object.

            * - :pyclass:`~IPlaceGraphics3D`
              - IAgPlaceVO Interface. For 3D properties of a Place object.

            * - :pyclass:`~IPlace`
              - Provide access to the properties and methods used in defining a place object.

            * - :pyclass:`~IAntennaNoiseTemperature`
              - Provide access to the antenna noise temperature parameters.

            * - :pyclass:`~ISystemNoiseTemperature`
              - Provide access to the system noise temperature parameters.

            * - :pyclass:`~IPolarization`
              - Provide the base interface for the a polarization object.

            * - :pyclass:`~IPolarizationElliptical`
              - Provide the interface for elliptical polarization.

            * - :pyclass:`~IPolarizationCrossPolLeakage`
              - Provide the interface for polarization cross pol leakage.

            * - :pyclass:`~IPolarizationLinear`
              - Provide the interface for linear polarization.

            * - :pyclass:`~IPolarizationHorizontal`
              - Provide the interface for linear polarization.

            * - :pyclass:`~IPolarizationVertical`
              - Provide the interface for linear polarization.

            * - :pyclass:`~IAdditionalGainLoss`
              - Provide access to an additional gain/loss.

            * - :pyclass:`~IAdditionalGainLossCollection`
              - Represents a collection of gains and losses.

            * - :pyclass:`~ICRPluginConfiguration`
              - Provide access to plugin properties.

            * - :pyclass:`~ICRComplex`
              - Provide access to the real and imaginary parts of a complex number.

            * - :pyclass:`~ICRComplexCollection`
              - Represents a collection of complex numbers.

            * - :pyclass:`~ICRLocation`
              - Provide the interface for a location.

            * - :pyclass:`~IPointingStrategy`
              - Provide the base interface for a pointing strategy.

            * - :pyclass:`~IPointingStrategyFixed`
              - Provide the interface for a fixed pointing strategy.

            * - :pyclass:`~IPointingStrategySpinning`
              - Provide the interface for a spinning pointing strategy.

            * - :pyclass:`~IPointingStrategyTargeted`
              - Provide the interface for a targeted pointing strategy.

            * - :pyclass:`~IWaveformPulseDefinition`
              - Provide access to the properties and methods defining the pulse definition for a rectangular pulsed waveform.

            * - :pyclass:`~IWaveform`
              - Provide access to the properties and methods defining an antenna model.

            * - :pyclass:`~IWaveformRectangular`
              - Provide access to a rectangular waveform.

            * - :pyclass:`~IWaveformSelectionStrategy`
              - Provide the base interface for a waveform selection strategy.

            * - :pyclass:`~IWaveformSelectionStrategyFixed`
              - Provide the base interface for a waveform selection strategy which produces a Fixed waveform.

            * - :pyclass:`~IWaveformSelectionStrategyRangeLimits`
              - Provide the base interface for a waveform selection strategy which produces a waveform based on target range.

            * - :pyclass:`~IRFInterference`
              - Provide access to the properties and methods defining a radio frequency interference.

            * - :pyclass:`~IScatteringPointProvider`
              - Provide access to the properties and methods defining a scattering point provider.

            * - :pyclass:`~IScatteringPointProviderSinglePoint`
              - Provide access to the properties and methods defining a single point scattering point provider.

            * - :pyclass:`~IScatteringPointCollectionElement`
              - Provide access to the properties and methods defining a scattering point collection element.

            * - :pyclass:`~IScatteringPointCollection`
              - Represents a collection of scattering points.

            * - :pyclass:`~IScatteringPointProviderPointsFile`
              - Provide access to the properties and methods defining a scattering point provider where the scattering points are defined in a ascii text file.

            * - :pyclass:`~IScatteringPointProviderRangeOverCFARCells`
              - Provide access to the properties and methods defining a range over CFAR cells scattering point provider.

            * - :pyclass:`~IScatteringPointProviderSmoothOblateEarth`
              - Provide access to the properties and methods defining a smooth oblate earth scattering point provider.

            * - :pyclass:`~IScatteringPointProviderPlugin`
              - Provide access to the properties and methods defining a plugin scattering point provider.

            * - :pyclass:`~IScatteringPointModel`
              - Provide access to the properties and methods defining a scattering point model model.

            * - :pyclass:`~IScatteringPointModelConstantCoefficient`
              - Provide access to the properties and methods defining a constant coefficient scattering point model.

            * - :pyclass:`~IScatteringPointModelWindTurbine`
              - Provide access to the properties and methods defining a wind turbine scattering point model.

            * - :pyclass:`~IScatteringPointModelPlugin`
              - Provide access to the properties and methods defining a plugin scattering point model.

            * - :pyclass:`~IScatteringPointProviderCollectionElement`
              - Provide access to the properties and methods defining an entry in the scattering point provider collection.

            * - :pyclass:`~IScatteringPointProviderCollection`
              - Represents a collection of scattering point provider elements.

            * - :pyclass:`~IScatteringPointProviderList`
              - Provide access to the properties and methods defining a scattering point provider list.

            * - :pyclass:`~IObjectRFEnvironment`
              - Provide access to the properties and methods defining the RF environment for an object.

            * - :pyclass:`~IObjectLaserEnvironment`
              - Provide access to the properties and methods defining the laser environment for an object.

            * - :pyclass:`~IAntennaModel`
              - Provide access to the properties and methods defining an antenna model.

            * - :pyclass:`~IAntennaModelGaussian`
              - Provide access to the properties and methods defining a gaussian antenna model.

            * - :pyclass:`~IAntennaModelParabolic`
              - Provide access to the properties and methods defining a parabolic antenna model.

            * - :pyclass:`~IAntennaModelSquareHorn`
              - Provide access to the properties and methods defining a square horn antenna model.

            * - :pyclass:`~IAntennaModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin antenna model.

            * - :pyclass:`~IAntennaModelExternal`
              - Provide access to the properties and methods defining a external antenna model.

            * - :pyclass:`~IAntennaModelGimroc`
              - Provide access to the properties and methods defining a GIMROC antenna model.

            * - :pyclass:`~IAntennaModelRemcomUanFormat`
              - Provide access to the properties and methods defining an antnna pattern Remcom uan format model.

            * - :pyclass:`~IAntennaModelANSYSffdFormat`
              - Provide access to the properties and methods defining an antnna pattern ANSYS ffd format model.

            * - :pyclass:`~IAntennaModelTicraGRASPFormat`
              - Provide access to the properties and methods defining an antnna pattern Ticra GRASP format model.

            * - :pyclass:`~IAntennaModelElevationAzimuthCuts`
              - Provide access to the properties and methods defining a pattern elevation/azimuth cuts antenna model.

            * - :pyclass:`~IAntennaModelIeee1979`
              - Provide access to the properties and methods defining a IEEE 1979 antenna model.

            * - :pyclass:`~IAntennaModelDipole`
              - Provide access to the properties and methods defining a dipole antenna model.

            * - :pyclass:`~IAntennaModelHelix`
              - Provide access to the properties and methods defining a helix antenna model.

            * - :pyclass:`~IAntennaModelCosecantSquared`
              - Provide access to the properties and methods defining a cosecant squared antenna model.

            * - :pyclass:`~IAntennaModelHemispherical`
              - Provide access to the properties and methods defining a hemispherical antenna model.

            * - :pyclass:`~IAntennaModelPencilBeam`
              - Provide access to the properties and methods defining a pencil beam antenna model.

            * - :pyclass:`~IElementConfiguration`
              - Provide access to the properties and methods defining an element configuration.

            * - :pyclass:`~IElementConfigurationCircular`
              - Provide access to the properties and methods defining a circular element configuration.

            * - :pyclass:`~IElementConfigurationLinear`
              - Provide access to the properties and methods defining a linear element configuration.

            * - :pyclass:`~IElementConfigurationAsciiFile`
              - Provide access to the properties and methods defining a ascii file element configuration.

            * - :pyclass:`~IElementConfigurationHfssEepFile`
              - Provide access to the properties and methods defining an HFSS EEP file element configuration.

            * - :pyclass:`~IElementConfigurationPolygon`
              - Provide access to the properties and methods defining a polygon element configuration.

            * - :pyclass:`~IBeamformer`
              - Provide access to the properties and methods defining a beamformer.

            * - :pyclass:`~IBeamformerMvdr`
              - Provide access to the properties and methods defining an MVDR beamformer.

            * - :pyclass:`~IBeamformerUniform`
              - Provide access to the properties and methods defining a uniform tapered beamformer.

            * - :pyclass:`~IBeamformerAsciiFile`
              - Provide access to the properties and methods defining an ascii file beamformer.

            * - :pyclass:`~IBeamformerScript`
              - Provide access to the properties and methods defining an script plugin beamformer.

            * - :pyclass:`~IBeamformerBlackmanHarris`
              - Provide access to the properties and methods defining a Blackman-Harris tapered beamformer.

            * - :pyclass:`~IBeamformerCosine`
              - Provide access to the properties and methods defining a cosine tapered beamformer.

            * - :pyclass:`~IBeamformerCosineX`
              - Provide access to the properties and methods defining an cosine^X tapered beamformer.

            * - :pyclass:`~IBeamformerCustomTaperFile`
              - Provide access to the properties and methods defining a custom taper file beamformer.

            * - :pyclass:`~IBeamformerDolphChebyshev`
              - Provide access to the properties and methods defining a Dolph-Chebyshev tapered beamformer.

            * - :pyclass:`~IBeamformerHamming`
              - Provide access to the properties and methods defining a Hamming tapered beamformer.

            * - :pyclass:`~IBeamformerHann`
              - Provide access to the properties and methods defining a Hann tapered beamformer.

            * - :pyclass:`~IBeamformerRaisedCosine`
              - Provide access to the properties and methods defining a raised cosine tapered beamformer.

            * - :pyclass:`~IBeamformerRaisedCosineSquared`
              - Provide access to the properties and methods defining a raised cosine-squared tapered beamformer.

            * - :pyclass:`~IDirectionProvider`
              - Provide access to the properties and methods defining an direction provider.

            * - :pyclass:`~IDirectionProviderAsciiFile`
              - Provide access to the properties and methods defining an ascii file direction provider.

            * - :pyclass:`~IDirectionProviderObject`
              - Provide access to the properties and methods defining an object direction provider.

            * - :pyclass:`~IDirectionProviderLink`
              - Provide access to the properties and methods defining an link direction provider.

            * - :pyclass:`~IDirectionProviderScript`
              - Provide access to the properties and methods defining an script plugin direction provider.

            * - :pyclass:`~IElement`
              - Provide access to the properties and methods defining a phased array element.

            * - :pyclass:`~IElementCollection`
              - Represents a collection of phased array elements.

            * - :pyclass:`~IAntennaModelPhasedArray`
              - Provide access to the properties and methods defining a phased array antenna model.

            * - :pyclass:`~IAntennaModelHfssEepArray`
              - Provide access to the properties and methods defining an HFSS EEP array antenna model.

            * - :pyclass:`~IAntennaModelIsotropic`
              - Provide access to the properties and methods defining an isotropic antenna model.

            * - :pyclass:`~IAntennaModelIntelSat`
              - Provide access to the properties and methods defining an IntelSat antenna model.

            * - :pyclass:`~IAntennaModelOpticalSimple`
              - Provide access to the properties and methods defining a simple optical antenna model.

            * - :pyclass:`~IAntennaModelRectangularPattern`
              - Provide access to the properties and methods defining a rectangular pattern antenna model.

            * - :pyclass:`~IAntennaModelGpsGlobal`
              - Provide access to the properties and methods defining a GPS global antenna model.

            * - :pyclass:`~IAntennaModelGpsFrpa`
              - Provide access to the properties and methods defining a GPS FRPA antenna model.

            * - :pyclass:`~IAntennaModelItuBO1213CoPolar`
              - Provide access to the properties and methods defining an ITU-R BO1213 co-polar antenna model.

            * - :pyclass:`~IAntennaModelItuBO1213CrossPolar`
              - Provide access to the properties and methods defining an ITU-R BO1213 cross-polar antenna model.

            * - :pyclass:`~IAntennaModelItuF1245`
              - Provide access to the properties and methods defining an ITU-R F1245-3 antenna model.

            * - :pyclass:`~IAntennaModelItuS580`
              - Provide access to the properties and methods defining an ITU-R S580-6 antenna model.

            * - :pyclass:`~IAntennaModelItuS465`
              - Provide access to the properties and methods defining an ITU-R S465-6 antenna model.

            * - :pyclass:`~IAntennaModelItuS731`
              - Provide access to the properties and methods defining an ITU-R S731 antenna model.

            * - :pyclass:`~IAntennaModelItuS1528R12Circular`
              - Provide access to the properties and methods defining an ITU-R S1528 1.2 circular antenna model.

            * - :pyclass:`~IAntennaModelItuS1528R13`
              - Provide access to the properties and methods defining an ITU-R S1528 1.3 antenna model.

            * - :pyclass:`~IAntennaModelItuS672Circular`
              - Provide access to the properties and methods defining an ITU-R S672-4 circular antenna model.

            * - :pyclass:`~IAntennaModelItuS1528R12Rectangular`
              - Provide access to the properties and methods defining an ITU-R S1528 1.2 rectangular antenna model.

            * - :pyclass:`~IAntennaModelItuS672Rectangular`
              - Provide access to the properties and methods defining an ITU-R S672-4 1.2 rectangular antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularCosine`
              - Provide access to the properties and methods defining a circular cosine aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularUniform`
              - Provide access to the properties and methods defining a circular uniform aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularCosineSquared`
              - Provide access to the properties and methods defining a circular cosine squared aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularBessel`
              - Provide access to the properties and methods defining a circular bessel aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularBesselEnvelope`
              - Provide access to the properties and methods defining a circular bessel envelope aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularCosinePedestal`
              - Provide access to the properties and methods defining a circular cosine pedestal aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularCosineSquaredPedestal`
              - Provide access to the properties and methods defining a circular cosine squared pedestal aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularSincIntPower`
              - Provide access to the properties and methods defining a circular sinc integer power aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureCircularSincRealPower`
              - Provide access to the properties and methods defining a circular sinc real power aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularUniform`
              - Provide access to the properties and methods defining a rectangular uniform aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularCosineSquared`
              - Provide access to the properties and methods defining a rectangular cosine squared aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularCosine`
              - Provide access to the properties and methods defining a rectangular cosine aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularCosinePedestal`
              - Provide access to the properties and methods defining a rectangular cosine pedestal aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularCosineSquaredPedestal`
              - Provide access to the properties and methods defining a rectangular cosine squared pedestal aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularSincIntPower`
              - Provide access to the properties and methods defining a rectangular sinc integer power aperture antenna model.

            * - :pyclass:`~IAntennaModelApertureRectangularSincRealPower`
              - Provide access to the properties and methods defining a rectangular sinc real power aperture antenna model.

            * - :pyclass:`~IAntennaVolumeLevel`
              - IAgRadarCrossSectionVolumeLevel Interface for an radar cross section volume level.

            * - :pyclass:`~IAntennaVolumeLevelCollection`
              - Represents a collection of antenna volume levels.

            * - :pyclass:`~IAntennaVolumeGraphics`
              - IAgAntennaVolumeGraphics Interface for a antenna's 3D volume properties.

            * - :pyclass:`~IAntennaGraphics3D`
              - IAgAntennaVO Interface for a antenna's 3D Graphics properties.

            * - :pyclass:`~IAntennaContourLevel`
              - IAgAntennaContourLevel Interface for an antenna contour level.

            * - :pyclass:`~IAntennaContourLevelCollection`
              - Represents a collection of antenna contour levels.

            * - :pyclass:`~IAntennaContour`
              - IAgAntennaContour Interface for a antenna's contour properties.

            * - :pyclass:`~IAntennaContourGain`
              - IAgAntennaContourGain Interface for a antenna's gain contour properties.

            * - :pyclass:`~IAntennaContourEirp`
              - IAgAntennaContourEirp Interface for a antenna's eirp contour properties.

            * - :pyclass:`~IAntennaContourRip`
              - IAgAntennaContourRip Interface for a antenna's rip contour properties.

            * - :pyclass:`~IAntennaContourFluxDensity`
              - IAgAntennaContourFluxDensity Interface for a antenna's flux density contour properties.

            * - :pyclass:`~IAntennaContourSpectralFluxDensity`
              - IAgAntennaContourSpectralFluxDensity Interface for a antenna's spectral flux density contour properties.

            * - :pyclass:`~IAntennaContourGraphics`
              - IAgAntennaContourGraphics Interface for a antenna's contour properties.

            * - :pyclass:`~IAntennaGraphics`
              - IAgAntennaGraphics Interface for a antenna's 2D Graphics properties.

            * - :pyclass:`~IAntenna`
              - Provide access to the properties and methods defining an Antenna object.

            * - :pyclass:`~IAntennaControl`
              - Provide access to the properties and methods of the antenna control.

            * - :pyclass:`~IAntennaBeamSelectionStrategy`
              - Provide access to a beam selection strategy.

            * - :pyclass:`~IAntennaBeamSelectionStrategyScriptPlugin`
              - Provide access to a script plugin beam selection strategy.

            * - :pyclass:`~IAntennaBeam`
              - Provide access to an antenna beam.

            * - :pyclass:`~IAntennaBeamTransmit`
              - Provide access to an transmit antenna beam.

            * - :pyclass:`~IAntennaBeamCollection`
              - Represents a collection of antenna beams.

            * - :pyclass:`~IAntennaSystem`
              - Provide access to the properties for a antenna system.

            * - :pyclass:`~IRFFilterModel`
              - Provide access to the properties and methods defining an RF filter model.

            * - :pyclass:`~IModulatorModel`
              - Provide access to the properties and methods defining a modulator model.

            * - :pyclass:`~ITransmitterModel`
              - Provide access to the properties and methods defining a transmitter model.

            * - :pyclass:`~ITransmitterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin transmitter model.

            * - :pyclass:`~ITransmitterModelCable`
              - Provide access to the properties and methods defining a cable transmitter model.

            * - :pyclass:`~ITransmitterModelSimple`
              - Provide access to the properties and methods defining a simple transmitter model.

            * - :pyclass:`~ITransmitterModelMedium`
              - Provide access to the properties and methods defining a medium transmitter model.

            * - :pyclass:`~ITransmitterModelComplex`
              - Provide access to the properties and methods defining a complex transmitter model.

            * - :pyclass:`~ITransmitterModelMultibeam`
              - Provide access to the properties and methods defining a multibeam transmitter model.

            * - :pyclass:`~ITransmitterModelLaser`
              - Provide access to the properties and methods defining a laser transmitter model.

            * - :pyclass:`~ITransferFunctionInputBackOffCOverImTableRow`
              - Provide access to the row of an input back off vs C/Im table.

            * - :pyclass:`~ITransferFunctionInputBackOffCOverImTable`
              - Represents a collection of input back off vs C/Im values.

            * - :pyclass:`~ITransferFunctionInputBackOffOutputBackOffTableRow`
              - Provide access to the row of an input back off vs output back off table.

            * - :pyclass:`~ITransferFunctionInputBackOffOutputBackOffTable`
              - Represents a collection of input back off vs output back off values.

            * - :pyclass:`~ITransferFunctionPolynomialCollection`
              - Represents a transfer function polynomial collection.

            * - :pyclass:`~IReTransmitterModel`
              - Provide access to the properties and methods defining a re-transmitter model.

            * - :pyclass:`~IReTransmitterModelSimple`
              - Provide access to the properties and methods defining a simple re-transmitter model.

            * - :pyclass:`~IReTransmitterModelMedium`
              - Provide access to the properties and methods defining a medium re-transmitter model.

            * - :pyclass:`~IReTransmitterModelComplex`
              - Provide access to the properties and methods defining a complex re-transmitter model.

            * - :pyclass:`~ITransmitterGraphics3D`
              - IAgTransmitterVO Interface for a transmitter's 3D Graphics properties.

            * - :pyclass:`~ITransmitterGraphics`
              - IAgTransmitterGraphics Interface for a transmitter's 2D Graphics properties.

            * - :pyclass:`~ITransmitter`
              - Provide access to the properties and methods defining an Transmitter object.

            * - :pyclass:`~IDemodulatorModel`
              - Provide access to the properties and methods defining a demodulator model.

            * - :pyclass:`~ILaserPropagationLossModels`
              - Provide access to laser propagation loss models.

            * - :pyclass:`~ILinkMargin`
              - Provide access to the properties for configuring the link margin computation.

            * - :pyclass:`~IReceiverModel`
              - Provide access to the properties and methods defining a receiver model.

            * - :pyclass:`~IReceiverModelSimple`
              - Provide access to the properties and methods defining a simple receiver model.

            * - :pyclass:`~IReceiverModelMedium`
              - Provide access to the properties and methods defining a medium receiver model.

            * - :pyclass:`~IReceiverModelComplex`
              - Provide access to the properties and methods defining a complex receiver model.

            * - :pyclass:`~IReceiverModelMultibeam`
              - Provide access to the properties and methods defining a multibeam receiver model.

            * - :pyclass:`~IReceiverModelLaser`
              - Provide access to the properties and methods defining a laser receiver model.

            * - :pyclass:`~IReceiverModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin receiver model.

            * - :pyclass:`~IReceiverModelScriptPluginRF`
              - Provide access to the properties and methods defining a radio frequency script plugin receiver model.

            * - :pyclass:`~IReceiverModelCable`
              - Provide access to the properties and methods defining a cable receiver model.

            * - :pyclass:`~IReceiverGraphics3D`
              - IAgReceiverVO Interface for a receiver's 3D Graphics properties.

            * - :pyclass:`~IReceiverGraphics`
              - IAgReceiverGraphics Interface for a receiver's 2D Graphics properties.

            * - :pyclass:`~IReceiver`
              - Provide access to the properties and methods defining an Receiver object.

            * - :pyclass:`~IRadarActivity`
              - Provide access to the properties and methods defining radar activity.

            * - :pyclass:`~IRadarActivityTimeComponentListElement`
              - Provide access to the properties and methods defining an entry in the time components activity list.

            * - :pyclass:`~IRadarActivityTimeComponentListCollection`
              - Represents a collection of time component activity elements.

            * - :pyclass:`~IRadarActivityTimeComponentList`
              - Provide access to the properties and methods defining radar time components list activity.

            * - :pyclass:`~IRadarActivityTimeIntervalListElement`
              - Provide access to the properties and methods defining an entry in the time interval activity list.

            * - :pyclass:`~IRadarActivityTimeIntervalListCollection`
              - Represents a collection of time interval activity elements.

            * - :pyclass:`~IRadarActivityTimeIntervalList`
              - Provide access to the properties and methods defining radar time interval list activity.

            * - :pyclass:`~IRadarStcAttenuation`
              - Provide access to the properties and methods defining a radar STC attenuation.

            * - :pyclass:`~IRadarStcAttenuationDecayFactor`
              - Provide access to the properties and methods defining a radar decay factor STC attenuation.

            * - :pyclass:`~IRadarStcAttenuationDecaySlope`
              - Provide access to the properties and methods defining a radar decay slope STC attenuation.

            * - :pyclass:`~IRadarStcAttenuationMap`
              - Provide access to the properties and methods defining a radar STC attenuation map.

            * - :pyclass:`~IRadarJamming`
              - Provide access to the properties and methods defining a radar jamming.

            * - :pyclass:`~IRadarClutterGeometryModel`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointProvider interface instead. Provides access to the properties and methods defining a radar clutter geometry model.

            * - :pyclass:`~IRadarClutterGeometryModelPlugin`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointProviderPlugin interface instead. Provides access to the properties and methods defining a radar clutter geometry plugin model.

            * - :pyclass:`~IRadarClutter`
              - Interface which defines a radar's clutter.

            * - :pyclass:`~IRadarClutterGeometry`
              - Do not use this interface, as it is deprecated. Use IAgRadarClutter interface instead. Interface which defines a radar's clutter geometry.

            * - :pyclass:`~IRadarTransmitter`
              - Interface which defines a radar transmitter.

            * - :pyclass:`~IRadarTransmitterMultifunction`
              - Interface which defines a multifunction radar transmitter.

            * - :pyclass:`~IRadarReceiver`
              - Interface which defines a radar receiver.

            * - :pyclass:`~IRadarContinuousWaveAnalysisMode`
              - Interface which defines an continuous wave analysis.

            * - :pyclass:`~IRadarContinuousWaveAnalysisModeGoalSNR`
              - Interface which defines an continuous wave goal SNR analysis.

            * - :pyclass:`~IRadarContinuousWaveAnalysisModeFixedTime`
              - Interface which defines an continuous wave fixed time analysis.

            * - :pyclass:`~IRadarPulseIntegration`
              - Interface which defines an integration method.

            * - :pyclass:`~IRadarPulseIntegrationGoalSNR`
              - Interface which defines a goal SNR integration method.

            * - :pyclass:`~IRadarPulseIntegrationFixedNumberOfPulses`
              - Interface which defines a fixed number of pulses integration method.

            * - :pyclass:`~IRadarWaveformSearchTrack`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarWaveformSearchTrackPulseDefinition`
              - Provide access to the properties and methods defining the pulse definition for a search track waveform.

            * - :pyclass:`~IRadarWaveformSarPulseDefinition`
              - Provide access to the properties and methods defining the pulse definition for a Sar waveform.

            * - :pyclass:`~IRadarWaveformSarPulseIntegration`
              - Provide access to the properties and methods defining the pulse integration for a SAR waveform.

            * - :pyclass:`~IRadarModulator`
              - Provide access to the properties and methods defining the radar modulator.

            * - :pyclass:`~IRadarProbabilityOfDetection`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :pyclass:`~IRadarProbabilityOfDetectionPlugin`
              - Provide access to the properties and methods defining a radar clutter geometry plugin model.

            * - :pyclass:`~IRadarProbabilityOfDetectionNonCFAR`
              - Provide access to the properties and methods for configuring non CFAR probability of detection parameters.

            * - :pyclass:`~IRadarProbabilityOfDetectionCFAR`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :pyclass:`~IRadarWaveformMonostaticSearchTrackContinuous`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarMultifunctionDetectionProcessing`
              - Interface which represents multifunction radar detection processing.

            * - :pyclass:`~IRadarWaveformMonostaticSearchTrackFixedPRF`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarWaveformBistaticReceiverSearchTrackContinuous`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Interface which is implemented by a search/track waveform.

            * - :pyclass:`~IRadarDopplerClutterFilters`
              - Provide access to the properties and methods defining a radar doppler clutter filter.

            * - :pyclass:`~IRadarModel`
              - Provide access to the properties and methods defining a radar model.

            * - :pyclass:`~IRadarModeMonostatic`
              - Provide access to the properties and methods defining a monostatic mode.

            * - :pyclass:`~IRadarModeMonostaticSearchTrack`
              - Provide access to the properties and methods defining a monostatic search/track mode.

            * - :pyclass:`~IRadarModeMonostaticSar`
              - Provide access to the properties and methods defining a monostatic sar mode.

            * - :pyclass:`~IRadarModelMonostatic`
              - Provide access to the properties and methods defining a monostatic radar model.

            * - :pyclass:`~IRadarAntennaBeam`
              - Provide access to a radar antenna beam.

            * - :pyclass:`~IRadarAntennaBeamCollection`
              - Represents a collection of antenna beams.

            * - :pyclass:`~IRadarMultifunctionWaveformStrategySettings`
              - Interface which defines a multifunction radar waveform strategy settings.

            * - :pyclass:`~IRadarModelMultifunction`
              - Provide access to the properties and methods defining a multifunction radar model.

            * - :pyclass:`~IRadarModeBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter mode.

            * - :pyclass:`~IRadarModeBistaticTransmitterSearchTrack`
              - Provide access to the properties and methods defining a bistatic transmitter search/track mode.

            * - :pyclass:`~IRadarModeBistaticTransmitterSar`
              - Provide access to the properties and methods defining a bistatic transmitter sar mode.

            * - :pyclass:`~IRadarModelBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter radar model.

            * - :pyclass:`~IRadarModeBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver mode.

            * - :pyclass:`~IRadarModeBistaticReceiverSearchTrack`
              - Provide access to the properties and methods defining a bistatic receiver search/track mode.

            * - :pyclass:`~IRadarModeBistaticReceiverSar`
              - Provide access to the properties and methods defining a bistatic receiver sar mode.

            * - :pyclass:`~IRadarModelBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver radar model.

            * - :pyclass:`~IRadarGraphics3D`
              - IAgRadarVO Interface for a radar's 3D Graphics properties.

            * - :pyclass:`~IRadarMultipathGraphics`
              - IAgRadarMultipathGraphics Interface for a radar's multipath graphics properties.

            * - :pyclass:`~IRadarAccessGraphics`
              - IAgRadarAccessGraphics Interface for a radar's access graphics properties.

            * - :pyclass:`~IRadarGraphics`
              - IAgRadarGraphics Interface for a radar's 2D Graphics properties.

            * - :pyclass:`~IRadar`
              - Provide access to the properties and methods defining an Radar object.

            * - :pyclass:`~IRadarClutterMapModel`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModel interface instead. Provides access to the properties and methods defining a radar clutter map model.

            * - :pyclass:`~IRadarClutterMapModelPlugin`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModelPlugin interface instead. Provides access to the properties and methods defining a radar clutter map plugin model.

            * - :pyclass:`~IRadarClutterMapModelConstantCoefficient`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModelConstantCoefficient interface instead. Provides access to the properties and methods defining a radar clutter map constant coefficient model.

            * - :pyclass:`~IRadarCrossSectionComputeStrategy`
              - Provide access to the properties and methods defining a radar cross section compute Strategy.

            * - :pyclass:`~IRadarCrossSectionComputeStrategyConstantValue`
              - Provide access to the properties and methods defining a radar cross section constant value compute Strategy.

            * - :pyclass:`~IRadarCrossSectionComputeStrategyScriptPlugin`
              - Provide access to the properties and methods defining a radar cross section script plugin compute Strategy.

            * - :pyclass:`~IRadarCrossSectionComputeStrategyExternalFile`
              - Provide access to the properties and methods defining a radar cross section external file compute Strategy.

            * - :pyclass:`~IRadarCrossSectionComputeStrategyAnsysCsvFile`
              - Provide access to the properties and methods defining a radar cross section Ansys Csv file compute Strategy.

            * - :pyclass:`~IRadarCrossSectionComputeStrategyPlugin`
              - Provide access to the properties and methods defining a radar cross section plugin compute Strategy.

            * - :pyclass:`~IRadarCrossSectionFrequencyBand`
              - Provide access to the properties and methods defining radar cross section frequency band.

            * - :pyclass:`~IRadarCrossSectionFrequencyBandCollection`
              - Represents a collection of radar cross section frequency bands.

            * - :pyclass:`~IRadarCrossSectionModel`
              - Provide access to the properties and methods defining a radar cross section model.

            * - :pyclass:`~IRadarStcAttenuationPlugin`
              - Provide access to the properties and methods defining a radar STC plugin model.

            * - :pyclass:`~IRadarCrossSectionVolumeLevel`
              - IAgRadarCrossSectionVolumeLevel Interface for an radar cross section volume level.

            * - :pyclass:`~IRadarCrossSectionVolumeLevelCollection`
              - Represents a collection of radar cross section volume levels.

            * - :pyclass:`~IRadarCrossSectionVolumeGraphics`
              - IAgRadarCrossSectionVolumeGraphics Interface for radar cross section 3D volume properties.

            * - :pyclass:`~IRadarCrossSectionContourLevel`
              - IAgRadarCrossSectionContourLevel Interface for an radar cross section contour level.

            * - :pyclass:`~IRadarCrossSectionContourLevelCollection`
              - Represents a collection of radar cross section contour levels.

            * - :pyclass:`~IRFFilterModelBessel`
              - Provide access to the properties and methods defining an bessel RF filter model.

            * - :pyclass:`~IRFFilterModelButterworth`
              - Provide access to the properties and methods defining an butterworth RF filter model.

            * - :pyclass:`~IRFFilterModelSincEnvSinc`
              - Provide access to the properties and methods defining a sinc envelope sinc analog RF filter model.

            * - :pyclass:`~IRFFilterModelElliptic`
              - Provide access to the properties and methods defining an elliptic analog RF filter model.

            * - :pyclass:`~IRFFilterModelChebyshev`
              - Provide access to the properties and methods defining an Chebyshev analog RF filter model.

            * - :pyclass:`~IRFFilterModelCosineWindow`
              - Provide access to the properties and methods defining a cosine window RF filter model.

            * - :pyclass:`~IRFFilterModelGaussianWindow`
              - Provide access to the properties and methods defining a gaussian window RF filter model.

            * - :pyclass:`~IRFFilterModelHammingWindow`
              - Provide access to the properties and methods defining a Hamming window RF filter model.

            * - :pyclass:`~IRFFilterModelExternal`
              - Provide access to the properties and methods defining a external RF filter model.

            * - :pyclass:`~IRFFilterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin RF filter model.

            * - :pyclass:`~IRFFilterModelSinc`
              - Provide access to the properties and methods defining a sinc RF filter model.

            * - :pyclass:`~IRFFilterModelRaisedCosine`
              - Provide access to the properties and methods defining a raised cosine RF filter model.

            * - :pyclass:`~IRFFilterModelRootRaisedCosine`
              - Provide access to the properties and methods defining a root raised cosine RF filter model.

            * - :pyclass:`~IRFFilterModelRcLowPass`
              - Provide access to the properties and methods defining a rc low pass RF filter model.

            * - :pyclass:`~IRFFilterModelFirBoxCar`
              - Provide access to the properties and methods defining a FIR box car RF filter model.

            * - :pyclass:`~IRFFilterModelFir`
              - Provide access to the properties and methods defining a FIR RF filter model.

            * - :pyclass:`~IRFFilterModelIir`
              - Provide access to the properties and methods defining a IIR RF filter model.

            * - :pyclass:`~IModulatorModelExternal`
              - Provide access to the properties and methods defining an external file modulator model.

            * - :pyclass:`~IModulatorModelBoc`
              - Provide access to the properties and methods defining a BOC modulator model.

            * - :pyclass:`~IModulatorModelPulsedSignal`
              - Provide access to the properties and methods defining a pulsed signal modulator model.

            * - :pyclass:`~IModulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin modulator model.

            * - :pyclass:`~IDemodulatorModelExternal`
              - Provide access to the properties and methods defining an external file demodulator model.

            * - :pyclass:`~IDemodulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin demodulator model.

            * - :pyclass:`~IRainLossModelScriptPlugin`
              - Provide access to the properties and methods of a script plugin rain loss model.

            * - :pyclass:`~IRainLossModel`
              - Provide access to the properties and methods a rain loss model.

            * - :pyclass:`~IRainLossModelCrane1985`
              - Provide access to the properties and methods for a Crane 1985 rain loss model.

            * - :pyclass:`~IRainLossModelCrane1982`
              - Provide access to the properties and methods for a Crane 1982 rain loss model.

            * - :pyclass:`~IRainLossModelCCIR1983`
              - Provide access to the properties and methods for a CCIR 1983 rain loss model.

            * - :pyclass:`~IRainLossModelITURP618_10`
              - Provide access to the properties and methods for a ITU-R P618-10 rain loss model.

            * - :pyclass:`~IRainLossModelITURP618_12`
              - Provide access to the properties and methods for a ITU-R P618-12 rain loss model.

            * - :pyclass:`~IRainLossModelITURP618_13`
              - Provide access to the properties and methods for a ITU-R P618-13 rain loss model.

            * - :pyclass:`~IUrbanTerrestrialLossModel`
              - Provide access to the properties and methods for an urban/terrestrial loss model.

            * - :pyclass:`~IUrbanTerrestrialLossModelTwoRay`
              - Provide access to the properties and methods for an urban/terrestrial loss two ray model.

            * - :pyclass:`~IWirelessInSite64GeometryData`
              - Provide access to the properties and methods for geometry data for the Wireless InSite RT model.

            * - :pyclass:`~IUrbanTerrestrialLossModelWirelessInSite64`
              - Provide access to the properties and methods for an urban/terrestrial loss Wireless InSite 64 model.

            * - :pyclass:`~ITroposphericScintillationFadingLossModel`
              - Provide access to the properties and methods for a TropoSpheric Scintillation Fading loss model.

            * - :pyclass:`~ITroposphericScintillationFadingLossModelP618_8`
              - Provide access to the properties and methods a Tropospheric Scintillation loss model ITU-R P.618_8.

            * - :pyclass:`~ITroposphericScintillationFadingLossModelP618_12`
              - Provide access to the properties and methods of a Tropospheric Scintillation loss model ITU-R P.618_12.

            * - :pyclass:`~IIonosphericFadingLossModel`
              - Provide access to the properties and methods for an Ionospheric Fading loss model.

            * - :pyclass:`~IIonosphericFadingLossModelP531_13`
              - Provide access to the properties and methods for the Ionospheric Fading loss model ITU-R P.531_13.

            * - :pyclass:`~ICloudsAndFogFadingLossModel`
              - Provide access to the properties and methods for Clouds and Fog loss models.

            * - :pyclass:`~ICloudsAndFogFadingLossModelP840_6`
              - Provide access to the properties and methods for clouds and fog loss model ITU-R P.840-6.

            * - :pyclass:`~ICloudsAndFogFadingLossModelP840_7`
              - Provide access to the properties and methods for clouds and fog loss model ITU-R P.840-7.

            * - :pyclass:`~IAtmosphericAbsorptionModel`
              - Provide access to the properties and methods an atmospheric absorption model.

            * - :pyclass:`~IAtmosphericAbsorptionModelITURP676`
              - Provide access to the properties and methods of the ITU-R P676 atmospheric absorption model.

            * - :pyclass:`~IAtmosphericAbsorptionModelTirem`
              - Provide access to the properties and methods of the TIREM atmospheric absorption model.

            * - :pyclass:`~ISolarActivityConfiguration`
              - Provide access to the properties and methods defining the solar activity configuration.

            * - :pyclass:`~ISolarActivityConfigurationSunspotNumber`
              - Provide access to the properties and methods defining the sunspot number.

            * - :pyclass:`~ISolarActivityConfigurationSolarFlux`
              - Provide access to the properties and methods defining the solar flux.

            * - :pyclass:`~IAtmosphericAbsorptionModelVoacap`
              - Provide access to the properties and methods of the VOACAP atmospheric absorption model.

            * - :pyclass:`~IAtmosphericAbsorptionModelSimpleSatcom`
              - Provide access to the properties and methods of the Simple Satcom atmospheric absorption model.

            * - :pyclass:`~IAtmosphericAbsorptionModelScriptPlugin`
              - Provide access to the properties and methods of the script plugin atmospheric absorption model.

            * - :pyclass:`~IAtmosphericAbsorptionModelCOMPlugin`
              - Provide access to the properties and methods of the COM plugin atmospheric absorption model.

            * - :pyclass:`~ICustomPropagationModel`
              - Provide access to the properties and methods for a custom propagation model.

            * - :pyclass:`~IPropagationChannel`
              - Provide access to the properties and methods defining a propagation channel.

            * - :pyclass:`~IBeerBouguerLambertLawLayer`
              - Provide access to a atmosphere layer used in the Beer-Bouguer-Lambert law propagation loss model.

            * - :pyclass:`~IBeerBouguerLambertLawLayerCollection`
              - Represents a collection of complex numbers.

            * - :pyclass:`~ILaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Provide access to the properties and methods a Beer-Bouguer-Lambert law laser propagation loss model.

            * - :pyclass:`~IModtranLookupTablePropagationModel`
              - Provide access to the properties and methods of the MODTRAN lookup table model.

            * - :pyclass:`~IModtranPropagationModel`
              - Provide access to the properties and methods of the MODTRAN propagation model.

            * - :pyclass:`~ILaserAtmosphericLossModel`
              - Provide access to the properties and methods for a laser atmospheric absorption loss model.

            * - :pyclass:`~ILaserTroposphericScintillationLossModel`
              - Provide access to the properties and methods for a laser tropospheric scintillation loss model.

            * - :pyclass:`~IAtmosphericTurbulenceModel`
              - Provide access to a refractive index structure parameter model.

            * - :pyclass:`~IAtmosphericTurbulenceModelConstant`
              - Provide access to a constant atmospheric turbulence model.

            * - :pyclass:`~IAtmosphericTurbulenceModelHufnagelValley`
              - Provide access to a Hufnagel Valley atmospheric turbulence model.

            * - :pyclass:`~ILaserTroposphericScintillationLossModelITURP1814`
              - Provide access to the properties and methods an ITU-R P.1814 laser tropospheric scintillation propagation loss model.

            * - :pyclass:`~ILaserPropagationChannel`
              - Provide access to laser propagation loss models.

            * - :pyclass:`~ICommSystemLinkSelectionCriteria`
              - Provide access to a link selection criteria.

            * - :pyclass:`~ICommSystemLinkSelectionCriteriaScriptPlugin`
              - Provide access to a script plugin link selection criteria.

            * - :pyclass:`~ICommSystemAccessEventDetection`
              - Provide access to the properties an access event detection algorithm.

            * - :pyclass:`~ICommSystemAccessEventDetectionSubsample`
              - Provide access to the properties an access sub-sample event detection algorithm.

            * - :pyclass:`~ICommSystemAccessSamplingMethod`
              - Provide access to the properties for the sampling method.

            * - :pyclass:`~ICommSystemAccessSamplingMethodFixed`
              - Provide access to the properties for a fixed sampling method.

            * - :pyclass:`~ICommSystemAccessSamplingMethodAdaptive`
              - Provide access to the properties for a adaptive sampling method.

            * - :pyclass:`~ICommSystemAccessOptions`
              - Provide access to the CommSystem object access options.

            * - :pyclass:`~ICommSystemGraphics`
              - IAgCommSystemGraphics Interface for a CommSystem's 2D Graphics properties.

            * - :pyclass:`~ICommSystemGraphics3D`
              - IAgCommSystemVO Interface for a CommSystem's 3D Graphics properties.

            * - :pyclass:`~ICommSystem`
              - Provide access to the properties and methods defining an CommSystem object.

            * - :pyclass:`~ISRPModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :pyclass:`~ISRPModelBase`
              - A base interface for solar radiation pressure models.

            * - :pyclass:`~ISRPModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :pyclass:`~ISRPModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :pyclass:`~ISRPModelPlugin`
              - Plugin Light Reflection Model.

            * - :pyclass:`~IVehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :pyclass:`~IVehicleHPOPDragModel`
              - A base interface for drag models.

            * - :pyclass:`~IVehicleHPOPDragModelSpherical`
              - Spherical Drag Model.

            * - :pyclass:`~IVehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :pyclass:`~IVehicleDuration`
              - Look ahead and look behind duration options.

            * - :pyclass:`~IVehicleRealtimeCartesianPoints`
              - Add one ephemeris point using cartesian coordinates.

            * - :pyclass:`~IVehicleRealtimeLLAHPSPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :pyclass:`~IVehicleRealtimeLLAPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :pyclass:`~IVehicleRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :pyclass:`~IVehicleGPSElement`
              - An element of the GPS element collection.

            * - :pyclass:`~IVehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :pyclass:`~IVehicleHPOPSRPModel`
              - HPOP Solar Radiation Pressure Model.

            * - :pyclass:`~IVehicleThirdBodyGravityElement`
              - Third-body gravity interface.

            * - :pyclass:`~IVehicleThirdBodyGravityCollection`
              - Third Body Gravity Collection.

            * - :pyclass:`~IVehicleSGP4LoadData`
              - Load Method Data interface.

            * - :pyclass:`~IVehicleSGP4OnlineLoad`
              - Interface for SGP4 propagator. Loads segments from online.

            * - :pyclass:`~IVehicleSGP4OnlineAutoLoad`
              - Do not use this interface, as it is deprecated. Use IAgVeSGP4OnlineLoad instead. Interface for SGP4 propagator. Loads the most current segment from online.

            * - :pyclass:`~IVehicleSGP4LoadFile`
              - Interface for SGP4 propagator.

            * - :pyclass:`~IVehicleSGP4Segment`
              - Interface for SGP4 propagator.

            * - :pyclass:`~IVehiclePropagatorSGP4CommonTasks`
              - Interface provides methods encapsulating most commonly used functionality when working with SGP4 propagator.

            * - :pyclass:`~IVehicleSGP4AutoUpdateProperties`
              - SGP4 Element AutoUpdate properties.

            * - :pyclass:`~IVehicleSGP4AutoUpdateFileSource`
              - Interface to configure the SGP4 automatic updates using file(s).

            * - :pyclass:`~IVehicleSGP4AutoUpdateOnlineSource`
              - Interface to configure the SGP4 automatic updates using online source (AGI server).

            * - :pyclass:`~IVehicleSGP4AutoUpdate`
              - SGP4 Automatic Update properties.

            * - :pyclass:`~IVehicleSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :pyclass:`~IVehicleSGP4SegmentCollection`
              - Set of Trajectories.

            * - :pyclass:`~IVehicleInitialState`
              - Propagator Initial State.

            * - :pyclass:`~IVehicleHPOPCentralBodyGravity`
              - Central Body Gravity interface.

            * - :pyclass:`~IVehicleRadiationPressure`
              - Interface for additional radiation pressure options.

            * - :pyclass:`~IVehicleHPOPSolarRadiationPressure`
              - Solar Radiation Pressure (SRP) interface.

            * - :pyclass:`~IVehicleSolarFluxGeoMagnitudeEnterManually`
              - Interface for specifying solar and geomagnetic flux directly.

            * - :pyclass:`~IVehicleSolarFluxGeoMagnitudeUseFile`
              - Interface for specifying solar and geomagnetic flux via a file.

            * - :pyclass:`~IVehicleSolarFluxGeoMagnitude`
              - Base Interface IAgVeSolarFluxGeoMag. IAgVeSolarFluxGeoMagEnterManually and IAgVeSolarFluxGeoMagUseFile derive from this interface.

            * - :pyclass:`~IVehicleHPOPForceModelDrag`
              - Atmospheric Drag interface.

            * - :pyclass:`~IVehicleHPOPForceModelDragOptions`
              - Interface for additional options for atmospheric drag.

            * - :pyclass:`~IVehicleHPOPSolarRadiationPressureOptions`
              - Interface for additional solar radiation pressure options.

            * - :pyclass:`~IVehicleStatic`
              - Interface for additional static force model options.

            * - :pyclass:`~IVehicleSolidTides`
              - Interface for additional force model options related to solid tides.

            * - :pyclass:`~IVehicleOceanTides`
              - Interface for additional force model options related to ocean tides.

            * - :pyclass:`~IVehiclePluginSettings`
              - Interface for HPOP plugin settings.

            * - :pyclass:`~IVehiclePluginPropagator`
              - Interface for propagator plugin.

            * - :pyclass:`~IVehicleHPOPForceModelMoreOptions`
              - Interface for additional force model options.

            * - :pyclass:`~IVehicleEclipsingBodies`
              - Interface for eclipsing bodies.

            * - :pyclass:`~IVehicleHPOPForceModel`
              - Interface for HPOP force models.

            * - :pyclass:`~IVehicleStepSizeControl`
              - Interface for step size control.

            * - :pyclass:`~IVehicleTimeRegularization`
              - Interface for time regularization.

            * - :pyclass:`~IVehicleInterpolation`
              - Interpolation interface.

            * - :pyclass:`~IVehicleIntegrator`
              - Interface for HPOP integrator.

            * - :pyclass:`~IVehicleGravity`
              - Gravity options for covariance matrix.

            * - :pyclass:`~IVehiclePositionVelocityElement`
              - Covariance matrix interface.

            * - :pyclass:`~IVehiclePositionVelocityCollection`
              - An initial state error covariance matrix used to represent the uncertainty in the vehicle's position and velocity. Because the matrix is symmetric, you only need to enter the lower triangle of the 6x6 matrix.

            * - :pyclass:`~IVehicleCorrelationListElement`
              - Item in Consider Cross Correlation list.

            * - :pyclass:`~IVehicleCorrelationListCollection`
              - Consider Analysis list for HPOP covariance.

            * - :pyclass:`~IVehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :pyclass:`~IVehicleConsiderAnalysisCollection`
              - AgVeConsiderAnalysisCollection.

            * - :pyclass:`~IVehicleCovariance`
              - HPOP covariance interface.

            * - :pyclass:`~IVehicleJxInitialState`
              - Initial state interface for J2/J4 perturbation propagators.

            * - :pyclass:`~IVehicleLOPCentralBodyGravity`
              - Central body gravity interface for Long-range Orbit Predictor (LOP) propagator.

            * - :pyclass:`~IVehicleThirdBodyGravity`
              - Third body gravity interface options for Long-range Orbit Predictor (LOP) propagator.

            * - :pyclass:`~IVehicleExpDensModelParams`
              - Interface for exponential density model (for LOP propagator).

            * - :pyclass:`~IVehicleAdvanced`
              - Interface for advanced drag options for LOP propagator.

            * - :pyclass:`~IVehicleLOPForceModelDrag`
              - Interface for atmospheric drag for LOP propagator.

            * - :pyclass:`~IVehicleLOPSolarRadiationPressure`
              - Solar radiation pressure interface for LOP propagator.

            * - :pyclass:`~IVehiclePhysicalData`
              - Physical data interface for LOP propagator.

            * - :pyclass:`~IVehicleLOPForceModel`
              - Force model interface for LOP propagator.

            * - :pyclass:`~IVehicleSPICESegment`
              - Interface for SPICE propagator segment.

            * - :pyclass:`~IVehicleSegmentsCollection`
              - Set of segments.

            * - :pyclass:`~IVehiclePropagator`
              - Base vehicle propagator interface.

            * - :pyclass:`~IVehiclePropagatorHPOP`
              - HPOP propagator interface.

            * - :pyclass:`~IVehiclePropagatorJ2Perturbation`
              - J2 Perturbation propagator interface.

            * - :pyclass:`~IVehiclePropagatorJ4Perturbation`
              - J4 Perturbation propagator interface.

            * - :pyclass:`~IVehiclePropagatorLOP`
              - LOP (Long-Range Orbit Predictor) propagator interface.

            * - :pyclass:`~IVehiclePropagatorSGP4`
              - SGP4 propagator interface.

            * - :pyclass:`~IVehiclePropagatorSPICE`
              - SPICE propagator interface.

            * - :pyclass:`~IVehiclePropagatorStkExternal`
              - StkExternal propagator interface.

            * - :pyclass:`~IVehiclePropagatorTwoBody`
              - Two-body propagator interface.

            * - :pyclass:`~IVehiclePropagatorUserExternal`
              - User-external propagator interface.

            * - :pyclass:`~IVehicleLaunchVehicleInitialState`
              - Simple Ascent propagator initial state interface.

            * - :pyclass:`~IVehiclePropagatorSimpleAscent`
              - SimpleAscent Propagator.

            * - :pyclass:`~IVehicleWaypointAltitudeReference`
              - Base interface for the altitude references.

            * - :pyclass:`~IVehicleWaypointAltitudeReferenceTerrain`
              - Interface for terrain altitude reference.

            * - :pyclass:`~IVehicleWaypointsElement`
              - Interface for representing a waypoint in a collection of waypoints.

            * - :pyclass:`~IVehicleWaypointsCollection`
              - Represents a collection of waypoints used with GreatArc vehicles.

            * - :pyclass:`~IVehiclePropagatorGreatArc`
              - Great arc propagator interface.

            * - :pyclass:`~IVehiclePropagatorAviator`
              - Aviator propagator interface.

            * - :pyclass:`~IVehicleLaunchLLA`
              - Interface for geodetic LLA position.

            * - :pyclass:`~IVehicleLaunchLLR`
              - Interface for geocentric LLR position.

            * - :pyclass:`~IVehicleImpactLLA`
              - Interface for LLA (geodetic) coordinates for a missile's impact location.

            * - :pyclass:`~IVehicleImpactLLR`
              - Interface for LLR (geocentric) coordinates for a missile's impact location.

            * - :pyclass:`~IVehicleLaunchControlFixedApogeeAltitude`
              - Fixed apogee altitude interface for missile flight parameters.

            * - :pyclass:`~IVehicleLaunchControlFixedDeltaV`
              - Fixed Delta V interface for missile flight parameters.

            * - :pyclass:`~IVehicleLaunchControlFixedDeltaVMinEccentricity`
              - Fixed Delta V minimum eccentricity interface for missile flight parameters.

            * - :pyclass:`~IVehicleLaunchControlFixedTimeOfFlight`
              - Fixed time of flight interface for missile flight parameters.

            * - :pyclass:`~IVehicleImpactLocationLaunchAzEl`
              - Launch AzEl interface for missile impact location. All properties on this interface should be set explicitly.

            * - :pyclass:`~IVehicleImpact`
              - Base Interface IAgVeImpact. IAgVeImpactLLA and IAgVeImpactLLR derive from this.

            * - :pyclass:`~IVehicleLaunchControl`
              - Base Interface IAgVeLaunchControl. IAgVeLaunchControlFixedApogeeAlt, IAgVeLaunchControlFixedDeltaV, IAgVeLaunchControlDixedDeltaVMinEcc and IAgVeLaunchControlTimeOfFlight derive from this.

            * - :pyclass:`~IVehicleImpactLocationPoint`
              - Missile impact point interface.

            * - :pyclass:`~IVehicleLaunch`
              - Base interface IAgVeLaunch. IAgVeLaunchLLA and IAgVeLaunchLLR derive from this.

            * - :pyclass:`~IVehicleImpactLocation`
              - Base interface IAgVeImpactLocation. IAgVeImpactLocationLaunchAzEl and IAgVeImpactLocationPoint derive from this.

            * - :pyclass:`~IVehiclePropagatorBallistic`
              - Ballistic propagator interface.

            * - :pyclass:`~IVehicleRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :pyclass:`~IVehiclePropagatorRealtime`
              - Realtime propagator interface.

            * - :pyclass:`~IVehicleGPSAlmanacProperties`
              - A common base interface for GPS almanac properties.

            * - :pyclass:`~IVehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :pyclass:`~IVehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :pyclass:`~IVehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :pyclass:`~IVehicleGPSSpecifyAlmanac`
              - Interface to specify a GPS almanac.

            * - :pyclass:`~IVehicleGPSAutoUpdateProperties`
              - Interface for GPS AutoUpdate properties.

            * - :pyclass:`~IVehicleGPSAutoUpdateFileSource`
              - Interface to configure the GPS automatic updates using almanac file(s).

            * - :pyclass:`~IVehicleGPSAutoUpdateOnlineSource`
              - Interface to configure the GPS automatic updates using online source (AGI server).

            * - :pyclass:`~IVehicleGPSAutoUpdate`
              - Interface for GPS AutoUpdate.

            * - :pyclass:`~IVehiclePropagatorGPS`
              - Allow the user to configure and propagate a vehicle using the GPS propagator.

            * - :pyclass:`~IVehiclePropagator11ParamDescriptor`
              - 11-Param file definition.

            * - :pyclass:`~IVehiclePropagator11ParamDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :pyclass:`~IVehiclePropagator11Param`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :pyclass:`~IVehiclePropagatorSP3File`
              - SP3 file data.

            * - :pyclass:`~IVehiclePropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :pyclass:`~IVehiclePropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :pyclass:`~IVehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :pyclass:`~IVehicleAccessAdvanced`
              - Interface for configuring a vehicle's advanced targeting access computation properties.

            * - :pyclass:`~IVehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :pyclass:`~IVehicleTorque`
              - Torque file to use in defining integrated attitude.

            * - :pyclass:`~IVehicleIntegratedAttitude`
              - Integrated Attitude interface generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :pyclass:`~IVehicleVector`
              - Aligned and Constrained attitude profile.

            * - :pyclass:`~IVehicleRateOffset`
              - Rate and offset interface for precession and spin.

            * - :pyclass:`~IVehicleAttitudeProfile`
              - The base interface that all vehicle attitude profiles are derived from.

            * - :pyclass:`~IVehicleProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :pyclass:`~IVehicleProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :pyclass:`~IVehicleProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :pyclass:`~IVehicleProfileConstraintOffset`
              - Interface for constraint offset for various attitude profiles.

            * - :pyclass:`~IVehicleProfileAlignmentOffset`
              - Interface for alignment offset for various attitude profiles.

            * - :pyclass:`~IVehicleProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :pyclass:`~IVehicleProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :pyclass:`~IVehicleProfileSpinAboutXXX`
              - Shared interface for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :pyclass:`~IVehicleProfileSpinning`
              - Spinning attitude profile.

            * - :pyclass:`~IVehicleProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :pyclass:`~IVehicleScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :pyclass:`~IVehicleScheduleTimesCollection`
              - List of scheduled accesses.

            * - :pyclass:`~IVehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :pyclass:`~IVehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :pyclass:`~IVehicleTargetPointingCollection`
              - Attitude Targets.

            * - :pyclass:`~IVehiclePointing`
              - Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

            * - :pyclass:`~IVehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :pyclass:`~IVehicleStandardBasic`
              - Basic attitude profile.

            * - :pyclass:`~IVehicleAttitudeExternal`
              - Interface for using an external attitude (.a) file.

            * - :pyclass:`~IVehicleAttitude`
              - Base interface for vehicle attitude options.

            * - :pyclass:`~IVehicleAttitudeRealTimeDataReference`
              - Real time attitude data reference.

            * - :pyclass:`~IVehicleAttitudeRealTime`
              - Real time attitude interface.

            * - :pyclass:`~IVehicleAttitudeStandard`
              - Standard attitude profile.

            * - :pyclass:`~IVehicleTrajectoryAttitudeStandard`
              - Standard attitude profile for launch vehicle or missile.

            * - :pyclass:`~IVehicleOrbitAttitudeStandard`
              - Standard attitude profile for satellite.

            * - :pyclass:`~IVehicleRouteAttitudeStandard`
              - Standard attitude profile for aircraft.

            * - :pyclass:`~IVehicleProfileGPS`
              - GPS Attitude profile.

            * - :pyclass:`~IVehicleAttitudeTrendControlAviator`
              - Trending controls for Aviator attitude.

            * - :pyclass:`~IVehicleProfileAviator`
              - The profile used for Aviator aircraft.

            * - :pyclass:`~IVehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :pyclass:`~IVehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :pyclass:`~IVehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :pyclass:`~IVehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :pyclass:`~IVehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :pyclass:`~IVehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :pyclass:`~IVehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :pyclass:`~IVehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :pyclass:`~IVehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :pyclass:`~IVehicleGraphics2DElevContours`
              - General settings regarding display of elevation contours.

            * - :pyclass:`~IVehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :pyclass:`~IVehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :pyclass:`~IVehicleGraphics2DPass`
              - interface IAgVeGfxPass. IAgVeGfxPassShowPasses and IAgVeGfxPassResolution derive from this.

            * - :pyclass:`~IVehicleGraphics2DPasses`
              - Interface for setting satellite pass display graphics.

            * - :pyclass:`~IVehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :pyclass:`~IVehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :pyclass:`~IVehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :pyclass:`~IVehicleGraphics2DTimeEventType`
              - Base Interface IAgVeGfxTimeEventType. IAgVeGfxTimeEventTypeLine, IAgVeGfxTimeEventTypeMarker and IAgVeGfxTimeEventTypeText derive from this.

            * - :pyclass:`~IVehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :pyclass:`~IVehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :pyclass:`~IVehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :pyclass:`~IVehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :pyclass:`~IVehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :pyclass:`~IVehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :pyclass:`~IVehicleGraphics2DOrbitPassData`
              - 2D Graphics ground track and orbit pass properties.

            * - :pyclass:`~IVehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :pyclass:`~IVehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :pyclass:`~IVehicleGraphics2DLighting`
              - Lighting.

            * - :pyclass:`~IVehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :pyclass:`~IVehicleGraphics2DAttributes`
              - Base Interface for Vehicle 2D Graphics Attributes.

            * - :pyclass:`~IVehicleGraphics2DAttributesBasic`
              - Basic 2D Graphics Attributes for a vehicle.

            * - :pyclass:`~IVehicleGraphics2DAttributesDisplayState`
              - Provide access to non-trivial properties of 2D vehicle attributes.

            * - :pyclass:`~IVehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :pyclass:`~IVehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :pyclass:`~IVehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :pyclass:`~IVehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :pyclass:`~IVehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :pyclass:`~IVehicleGraphics2DElevationGroundElevation`
              - Ground elevation interface for vehicle swath.

            * - :pyclass:`~IVehicleGraphics2DElevationSwathHalfWidth`
              - Half width interface for vehicle swath.

            * - :pyclass:`~IVehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle interface for vehicle swath.

            * - :pyclass:`~IVehicleGraphics2DElevation`
              - Base Interface IAgVeGfxElevation. IAgVeGfxElevationGroundElevation, IAgVeGfxElevationsSwathHalfWidth and IAgVeGfxElevationsSwathHalfAngle derive from this.

            * - :pyclass:`~IVehicleGraphics2DSwath`
              - Vehicle swath interface.

            * - :pyclass:`~IVehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :pyclass:`~IVehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :pyclass:`~IVehicleGraphics2DTimeComponentsElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views.

            * - :pyclass:`~IVehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :pyclass:`~IVehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :pyclass:`~IVehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :pyclass:`~IVehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :pyclass:`~IVehicleTrajectoryGraphics3DModel`
              - Marker interface for launch vehicle or missile.

            * - :pyclass:`~IVehicleRouteGraphics3DModel`
              - 3D marker interface for great arc vehicles.

            * - :pyclass:`~IVehicleGraphics3DLeadTrailData`
              - Interface for vehicle's lead/trail data.

            * - :pyclass:`~IVehicleGraphics3DSystemsElementBase`
              - Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

            * - :pyclass:`~IVehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :pyclass:`~IVehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :pyclass:`~IVehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :pyclass:`~IVehicleGraphics3DDropLinePositionItem`
              - Interface for drop lines from the vehicle's current position.

            * - :pyclass:`~IVehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :pyclass:`~IVehicleGraphics3DDropLinePathItem`
              - Interface for drop lines at intervals along the vehicle's path.

            * - :pyclass:`~IVehicleGraphics3DDropLinePathItemCollection`
              - Interface for drop lines from the vehicle's orbit or trajectory.

            * - :pyclass:`~IVehicleGraphics3DOrbitDropLines`
              - Interface for droplines collections.

            * - :pyclass:`~IVehicleGraphics3DRouteDropLines`
              - Interface for droplines for great arc vehicles.

            * - :pyclass:`~IVehicleGraphics3DTrajectoryDropLines`
              - Interface for droplines for launch vehicles and missiles.

            * - :pyclass:`~IVehicleGraphics3DProximityAreaObject`
              - A base class that defines methods and properties common to all proximity area objects.

            * - :pyclass:`~IVehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :pyclass:`~IVehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :pyclass:`~IVehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :pyclass:`~IVehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :pyclass:`~IVehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :pyclass:`~IVehicleGraphics3DGeoBox`
              - Interface for geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :pyclass:`~IVehicleGraphics3DProximity`
              - Base Proximity graphics interface.

            * - :pyclass:`~IVehicleGraphics3DRouteProximity`
              - Proximity graphics interface for GreatArc Vehicles.

            * - :pyclass:`~IVehicleGraphics3DOrbitProximity`
              - Proximity graphics interface.

            * - :pyclass:`~IVehicleGraphics3DTrajectoryProximity`
              - Proximity graphics for a launch vehicle or missile.

            * - :pyclass:`~IVehicleGraphics3DElevContours`
              - Interface for 3D elevation angle contours.

            * - :pyclass:`~IVehicleGraphics3DSAA`
              - Interface for 3D South Atlantic Anomaly contours.

            * - :pyclass:`~IVehicleGraphics3DSigmaScaleProbability`
              - Interface for sigma probability for indirect sizing of covariance pointing contours.

            * - :pyclass:`~IVehicleGraphics3DSigmaScaleScale`
              - Interface for sigma scale for direct sizing of covariance pointing contours.

            * - :pyclass:`~IVehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :pyclass:`~IVehicleGraphics3DIntervalsElement`
              - Intervals graphics interface for covariance pointing contour.

            * - :pyclass:`~IVehicleGraphics3DIntervalsCollection`
              - Intervals.

            * - :pyclass:`~IVehicleGraphics3DAttributesBasic`
              - Interface for basic 3D graphics for covariance pointing contours.

            * - :pyclass:`~IVehicleGraphics3DAttributesIntervals`
              - Interface for 3D graphics based on intervals for covariance pointing contours.

            * - :pyclass:`~IVehicleGraphics3DSize`
              - 3D graphics vector size interface.

            * - :pyclass:`~IVehicleGraphics3DSigmaScale`
              - Base Interface IAgVeVOSigmaScale. IAgVeVOSigmaScaleScale and IAgVeVOSigmaScaleProbability derive from this.

            * - :pyclass:`~IVehicleGraphics3DAttributes`
              - Base Interface IAgVeVOAttributes. IAgVeVOAttributesBasic and IAgVeVOAttributesIntervals derive from this.

            * - :pyclass:`~IVehicleGraphics3DCovariancePointingContour`
              - Interface for covariance pointing contours.

            * - :pyclass:`~IVehicleGraphics3DOrbitPassData`
              - Interface for satellite 3D ground and orbit track data.

            * - :pyclass:`~IVehicleGraphics3DTrajectoryPassData`
              - Interface for 3D ground track and trajectory data for a launch vehicle or missile.

            * - :pyclass:`~IVehicleGraphics3DOrbitTrackData`
              - Interface for 3D leading/trailing track data for satellites.

            * - :pyclass:`~IVehicleGraphics3DTrajectoryTrackData`
              - Interface for 3D leading/trailing track data for launch vehicles and missiles.

            * - :pyclass:`~IVehicleGraphics3DTickData`
              - Base interface IAgVeVOTickData. IAgVeVOTickDataLine and IAgVeVOTickDataPoint derive from this.

            * - :pyclass:`~IVehicleGraphics3DPathTickMarks`
              - Interface for tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :pyclass:`~IVehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data interface for launch vehicles and missiles.

            * - :pyclass:`~IVehicleGraphics3DTrajectory`
              - 3D pass interface for launch vehicles and missiles.

            * - :pyclass:`~IVehicleGraphics3DTickDataLine`
              - Interface for line type tick marks.

            * - :pyclass:`~IVehicleGraphics3DTickDataPoint`
              - Interface for point type tick mark.

            * - :pyclass:`~IVehicleGraphics3DOrbitTickMarks`
              - Tick mark interface for satellites.

            * - :pyclass:`~IVehicleGraphics3DPass`
              - 3D pass interface for satellites.

            * - :pyclass:`~IVehicleGraphics3DCovariance`
              - Interface for 3D covariance ellipsoids.

            * - :pyclass:`~IVehicleGraphics3DVelCovariance`
              - Interface for 3D velocity covariance ellipsoids.

            * - :pyclass:`~IVehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint interface.

            * - :pyclass:`~IVehicleGraphics3DWaypointMarkersCollection`
              - Waypoint markers collection interface.

            * - :pyclass:`~IVehicleGraphics3DRoute`
              - 3D route graphics interface for great arc vehicles.

            * - :pyclass:`~IVehicleEclipseBodies`
              - Satellite Eclipse Bodies interface, for defining the eclipse central body list used for lighting computations.

            * - :pyclass:`~IGreatArcGraphics`
              - 2D Graphics common for all Great Arc Vehicles.

            * - :pyclass:`~IGreatArcGraphics3D`
              - 3D Graphics common for all Great Arc Vehicles.

            * - :pyclass:`~IGreatArcVehicle`
              - A base interface for all Great Arc Vehicles.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of IAgVeVOBPlaneTemplateDisplayCollection.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTemplate`
              - An element of IAgVeVOBPlaneTemplatesCollection.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :pyclass:`~IVehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :pyclass:`~IVehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTargetPointPosition`
              - A base class for BPlane target point position interfaces.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :pyclass:`~IVehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :pyclass:`~IVehicleGraphics3DBPlanePointCollection`
              - A list of available additional points.

            * - :pyclass:`~IVehicleGraphics3DBPlaneInstance`
              - Properties of an instance of a B-Plane template.

            * - :pyclass:`~IVehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :pyclass:`~IVehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :pyclass:`~IVehicleSpaceEnvironment`
              - no helpstring provided.

            * - :pyclass:`~IEOIR`
              - Property used to access IAgEOIR interface.

            * - :pyclass:`~ISatelliteGraphics3DModel`
              - Interface IAgSaVOModel exposes all Satellite's VO Model properties.

            * - :pyclass:`~ISatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :pyclass:`~IVehicleCentralBodies`
              - Satellite Central Bodies interface.

            * - :pyclass:`~ISatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :pyclass:`~IVehicleRepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :pyclass:`~IVehicleBreakAngle`
              - Base Interface IAgVeBreakAngle. IAgVeBreakAngleBreakByLatitude and IAgVeBreakAngleBreakByLongitude derive from this.

            * - :pyclass:`~IVehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :pyclass:`~IVehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :pyclass:`~IVehicleDefinition`
              - Pass break definition properties.

            * - :pyclass:`~IVehiclePassNumbering`
              - Base Interaface IAgVePassNumbering. IAgVePassNumberingDateOfFirstPass and IAgVePassNumberingFirstPassNum derive from this.

            * - :pyclass:`~IVehiclePassNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :pyclass:`~IVehiclePassNumberingFirstPassNum`
              - First pass number.

            * - :pyclass:`~IVehiclePassBreak`
              - Satellite Pass Break properties.

            * - :pyclass:`~IVehicleInertia`
              - Satellite inertia matrix parameters.

            * - :pyclass:`~IVehicleMassProperties`
              - Satellite Mass properties.

            * - :pyclass:`~IExportToolTimePeriod`
              - Specify Time Period.

            * - :pyclass:`~IExportToolStepSize`
              - The step size.

            * - :pyclass:`~IVehicleEphemerisCode500ExportTool`
              - The Code 500 Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :pyclass:`~IVehicleEphemerisCCSDSExportTool`
              - The CCSDS Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :pyclass:`~IVehicleEphemerisStkExportTool`
              - The STK Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :pyclass:`~IVehicleCoordinateAxes`
              - IAgVeCoordinateAxes.

            * - :pyclass:`~IVehicleCoordinateAxesCustom`
              - Custom.

            * - :pyclass:`~IVehicleAttitudeExportTool`
              - Attitude file for the Export Ephemeris/Attitude File Tool.

            * - :pyclass:`~IVehicleEphemerisSpiceExportTool`
              - The SPICE Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :pyclass:`~IVehiclePropDefinitionExportTool`
              - Interface used to define the export to data file options.

            * - :pyclass:`~IVehicleEphemerisStkBinaryExportTool`
              - The STK Binary Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :pyclass:`~IVehicleEphemerisCCSDSv2ExportTool`
              - The CCSDSv2 Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :pyclass:`~ISatelliteExportTools`
              - Interface used to define the export to data file options.

            * - :pyclass:`~ISatellite`
              - Satellite properties.

            * - :pyclass:`~ILaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :pyclass:`~ILaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :pyclass:`~ILaunchVehicleExportTools`
              - Interface for a launch vehicle object.

            * - :pyclass:`~ILaunchVehicle`
              - Interface for a launch vehicle object.

            * - :pyclass:`~IGroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :pyclass:`~IGroundVehicleGraphics3D`
              - 3D Graphics properties for ground vehicles.

            * - :pyclass:`~IGroundVehicleExportTools`
              - Interface used to define the export to data file options.

            * - :pyclass:`~IGroundVehicle`
              - Interface for a ground vehicle object.

            * - :pyclass:`~IMissileGraphics`
              - 2D Graphics for missiles.

            * - :pyclass:`~IMissileGraphics3D`
              - 3D Graphics for missiles.

            * - :pyclass:`~IMissileExportTools`
              - Interface used to define the export to data file options.

            * - :pyclass:`~IMissile`
              - Interface for a missile object.

            * - :pyclass:`~IAircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :pyclass:`~IAircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :pyclass:`~IAircraftExportTools`
              - Interface used to define the export to data file options.

            * - :pyclass:`~IAircraft`
              - Interface for aircraft object.

            * - :pyclass:`~IShipGraphics`
              - 2D Graphics options for a ship.

            * - :pyclass:`~IShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :pyclass:`~IShipExportTools`
              - Interface used to define the export to data file options.

            * - :pyclass:`~IShip`
              - Interface for a ship object.

            * - :pyclass:`~IMtoGraphics2DMarker`
              - Interface to define the 2D graphics attributes of the selected MTO track or tracks.

            * - :pyclass:`~IMtoGraphics2DLine`
              - MTO track line display options.

            * - :pyclass:`~IMtoGraphics2DFadeTimes`
              - MTO track fade times interface.

            * - :pyclass:`~IMtoGraphics2DLeadTrailTimes`
              - MTO track lead/trail times interface.

            * - :pyclass:`~IMtoGraphics2DTrack`
              - Interface to set 2D graphics attributes for each track in the MTO.

            * - :pyclass:`~IMtoGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :pyclass:`~IMtoDefaultGraphics2DTrack`
              - Interface to set 2D graphics attributes for default MTO tracks.

            * - :pyclass:`~IMtoGraphics2DGlobalTrackOptions`
              - Interface for global 2D graphics options for an MTO.

            * - :pyclass:`~IMtoGraphics`
              - MTO 2D Graphics interface.

            * - :pyclass:`~IMtoGraphics3DModelArtic`
              - MTO ModelArticulation Interface.

            * - :pyclass:`~IMtoGraphics3DMarker`
              - Interface for MTO 3D graphics marker options.

            * - :pyclass:`~IMtoGraphics3DPoint`
              - MTO track 3D marker point options interface.

            * - :pyclass:`~IMtoGraphics3DModel`
              - Interface for MTO track model options.

            * - :pyclass:`~IMtoGraphics3DSwapDistances`
              - Interface for MTO track 3D swap distances.

            * - :pyclass:`~IMtoGraphics3DDropLines`
              - Interface for MTO droplines.

            * - :pyclass:`~IMtoGraphics3DTrack`
              - Interface for setting 3D graphics properties for MTO tracks.

            * - :pyclass:`~IMtoGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :pyclass:`~IMtoDefaultGraphics3DTrack`
              - Interface for setting 3D graphics properties for default MTO tracks.

            * - :pyclass:`~IMtoGraphics3DGlobalTrackOptions`
              - Interface for global 3D graphics MTO track options.

            * - :pyclass:`~IMtoGraphics3D`
              - Interface for MTO 3D graphics properties.

            * - :pyclass:`~IMtoTrackPoint`
              - The points defined for the selected track.

            * - :pyclass:`~IMtoTrackPointCollection`
              - MTO track point list.

            * - :pyclass:`~IMtoTrack`
              - List of MTO tracks with basic information about each.

            * - :pyclass:`~IMtoTrackCollection`
              - MTO Track List.

            * - :pyclass:`~IMtoDefaultTrack`
              - Default MTO track.

            * - :pyclass:`~IMtoGlobalTrackOptions`
              - Global MTO track options.

            * - :pyclass:`~IMtoAnalysisPosition`
              - MTO position.

            * - :pyclass:`~IMtoAnalysisVisibility`
              - MTO Visibility computation.

            * - :pyclass:`~IMtoAnalysisFieldOfView`
              - MTO Field Of View computation.

            * - :pyclass:`~IMtoAnalysisRange`
              - MTO range computation.

            * - :pyclass:`~IMtoAnalysis`
              - MTO spatial state info.

            * - :pyclass:`~IMto`
              - Multi-Track Object (MTO) interface.

            * - :pyclass:`~ILineTargetGraphics`
              - Line Target 2D graphics.

            * - :pyclass:`~ILineTargetGraphics3D`
              - Line Target 3D Graphics properties.

            * - :pyclass:`~ILineTargetPoint`
              - Line Target Point interface.

            * - :pyclass:`~ILineTargetPointCollection`
              - The collection of points for the line target.

            * - :pyclass:`~ILineTarget`
              - Line Target Path properties.

            * - :pyclass:`~IChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :pyclass:`~IChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :pyclass:`~IChainGraphics`
              - 2D graphics properties of a chain.

            * - :pyclass:`~IChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :pyclass:`~IAccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :pyclass:`~IAccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :pyclass:`~IChainConnectionCollection`
              - Represents a collection of connections.

            * - :pyclass:`~IChainTimePeriodBase`
              - Chain time period options.

            * - :pyclass:`~IChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :pyclass:`~IChainConstraints`
              - Chain constraints.

            * - :pyclass:`~IChainConnection`
              - Provide access to a Chain connection.

            * - :pyclass:`~IChainOptimalStrandOpts`
              - Chain optimal strand options.

            * - :pyclass:`~IChain`
              - Configuration options for chains.

            * - :pyclass:`~ICoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :pyclass:`~ICoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :pyclass:`~ICoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :pyclass:`~ICoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :pyclass:`~ICoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :pyclass:`~ICoverageGraphics3D`
              - 3D graphics options for the coverage grid.

            * - :pyclass:`~ICoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :pyclass:`~ICoverageGridPointSelection`
              - Represents a set of coverage grid points.

            * - :pyclass:`~ICoverageGridInspector`
              - Provide access to the Coverage Definition grid inspector properties.

            * - :pyclass:`~ICoverageRegionFilesCollection`
              - Region Files.

            * - :pyclass:`~ICoverageAreaTargetsCollection`
              - Area Targets.

            * - :pyclass:`~ICoveragePointFileListCollection`
              - Point file list collection.

            * - :pyclass:`~ICoverageBounds`
              - Base interface for IAgCvBoundsCustom, IAgCvBoundsGlobal, IAgCvBoundsLat, IAgCvBoundsLatLines, IAgCvBoundsLonLines, IAgCvBoundsCustomBoundary.

            * - :pyclass:`~ICoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :pyclass:`~ICoverageBoundsCustomRegions`
              - Custom Regions.

            * - :pyclass:`~ICoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :pyclass:`~ICoverageBoundsLat`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :pyclass:`~ICoverageBoundsLatLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :pyclass:`~ICoverageBoundsLonLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :pyclass:`~ICoverageBoundsLatLonRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :pyclass:`~ICoverageResolution`
              - Base interface for IAgCvResolutionArea, IAgCvResolutionDistance and IAgCvResolutionLatLon, used to define coverage resolution (spacing between grid points).

            * - :pyclass:`~ICoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :pyclass:`~ICoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :pyclass:`~ICoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :pyclass:`~ICoverageGrid`
              - Grid Definition and resolution.

            * - :pyclass:`~ICoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :pyclass:`~ICoverageAssetListElement`
              - Coverage asset.

            * - :pyclass:`~ICoverageAdvanced`
              - Advanced Properties.

            * - :pyclass:`~ICoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :pyclass:`~ICoverageDefinition`
              - Coverage definition properties.

            * - :pyclass:`~IFigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :pyclass:`~IFigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :pyclass:`~IFigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :pyclass:`~IFigureOfMeritGraphics2DLevelAttributesCollection`
              - Level Attributes.

            * - :pyclass:`~IFigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :pyclass:`~IFigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :pyclass:`~IFigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :pyclass:`~IFigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :pyclass:`~IFigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :pyclass:`~IFigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :pyclass:`~IFigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :pyclass:`~IFigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :pyclass:`~IFigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :pyclass:`~IFigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :pyclass:`~IFigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :pyclass:`~IFigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :pyclass:`~IFigureOfMeritDefinitionScalarCalculation`
              - Figure of Merit using an Analysis Workbench scalar calculation component as the metric.

            * - :pyclass:`~IFigureOfMeritGridInspector`
              - Provide access to the FOM grid inspector properties.

            * - :pyclass:`~IFigureOfMeritNavigationAccuracyMethod`
              - Navigation Accuracy Figure of Merit type.

            * - :pyclass:`~IFigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :pyclass:`~IFigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :pyclass:`~IFigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :pyclass:`~IFigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :pyclass:`~IFigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :pyclass:`~IFigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionData`
              - IAgFmDefinitionData.

            * - :pyclass:`~IFigureOfMeritDefinitionDataMinMax`
              - IAgFmDefDataMinMax.

            * - :pyclass:`~IFigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :pyclass:`~IFigureOfMeritDefinitionDataMinAssets`
              - Minimum number of assets.

            * - :pyclass:`~IFigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :pyclass:`~IFigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best four satellites.

            * - :pyclass:`~IFigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :pyclass:`~IFigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :pyclass:`~IFigureOfMerit`
              - Figure of Merit properties.

            * - :pyclass:`~IFigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :pyclass:`~IFigureOfMeritDefinitionSystemAgeOfData`
              - System Age of Data Figure of Merit.

            * - :pyclass:`~IConstellationConstraintRestriction`
              - A base interface for all interfaces returned by the Restriction property of the IAgCnConstraints interface. It can be cast to IAgCnCnstrObjectRestriction.

            * - :pyclass:`~IConstellationConstraintObjectRestriction`
              - A restriction interface that is satisfied only when specified number of objects meets the conditions for the chain access.

            * - :pyclass:`~IConstellationConstraints`
              - Constellation Constraints.

            * - :pyclass:`~IConstellationGraphics`
              - Graphics options for constellation.

            * - :pyclass:`~IConstellationRouting`
              - Routing options for constellation.

            * - :pyclass:`~IConstellation`
              - Configuration options for constellations.

            * - :pyclass:`~IEventDetectionStrategy`
              - Define a base interface for the event detection strategies.

            * - :pyclass:`~IEventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :pyclass:`~IEventDetectionSubSampling`
              - Interface for event detection strategy involving subsampling.

            * - :pyclass:`~ISamplingMethodStrategy`
              - Define a base interface for the sampling method strategies.

            * - :pyclass:`~ISamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :pyclass:`~ISamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :pyclass:`~ISpaceEnvironmentRadEnergyMethodSpecify`
              - Customized energy lists for protons and electrons.

            * - :pyclass:`~ISpaceEnvironmentRadEnergyValues`
              - Energy values for computing electron and proton flux.

            * - :pyclass:`~ISpaceEnvironmentRadiationEnvironment`
              - Radiation environment settings.

            * - :pyclass:`~ISpaceEnvironmentMagnitudeFieldGraphics2D`
              - Graphics settings for showing magnetic field.

            * - :pyclass:`~ISpaceEnvironmentScenarioExtGraphics3D`
              - Graphics settings for space environment.

            * - :pyclass:`~ISpaceEnvironmentSAAContour`
              - SAA Contour settings.

            * - :pyclass:`~IVehicleSpaceEnvironmentMagneticField`
              - Magnetic field model.

            * - :pyclass:`~IVehicleSpaceEnvironmentVehTemperature`
              - Vehicle temperature model.

            * - :pyclass:`~IVehicleSpaceEnvironmentParticleFlux`
              - Particle Flux model.

            * - :pyclass:`~IVehicleSpaceEnvironmentRadDoseRateElement`
              - Dose rate interface.

            * - :pyclass:`~IVehicleSpaceEnvironmentRadDoseRateCollection`
              - The collection holds dose rate elements computed for each shielding thickness.

            * - :pyclass:`~IVehicleSpaceEnvironmentRadiation`
              - Radiation model.

            * - :pyclass:`~IVehicleSpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for showing magnetic field line.

            * - :pyclass:`~IVehicleSpaceEnvironmentGraphics`
              - Graphics settings for space environment.

            * - :pyclass:`~IStkPreferencesVDF`
              - VDF Load/Save settings.

            * - :pyclass:`~IStkPreferencesConnect`
              - Connect settings.

            * - :pyclass:`~IStkPreferencesPythonPlugins`
              - Python plugin settings.

            * - :pyclass:`~IPathCollection`
              - Collection to add and remove paths.

            * - :pyclass:`~IVehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :pyclass:`~IVehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :pyclass:`~IVehicleAttitudeSlewBase`
              - Represents an attitude slew base type.

            * - :pyclass:`~IVehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :pyclass:`~IVehicleAttitudeSlewFixedRate`
              - Fixed Rate slew.

            * - :pyclass:`~IVehicleAttitudeSlewFixedTime`
              - Fixed Time slew.

            * - :pyclass:`~IVmGridDefinition`
              - Base interface IAgVmGridDefinition. IAgVmGridSpatialCalculation and IAgVmExternalFile implement this interface.

            * - :pyclass:`~IVmAnalysisInterval`
              - IAgVmAnalysisInterval Interface for volume analysis interval.

            * - :pyclass:`~IVmAdvanced`
              - IAgVmAdvanced Interface for advanced volumetric options.

            * - :pyclass:`~IVmGraphics3D`
              - IAgVmVO Interface for a volumetric object's 3D Graphics properties.

            * - :pyclass:`~IVmGraphics3DGrid`
              - IAgVmVO Interface for a volumetric object's 3D Graphics properties.

            * - :pyclass:`~IVmGraphics3DCrossSection`
              - IAgVmVOCrossSection Interface for defining planar cross-sections through the volumetric grid.

            * - :pyclass:`~IVmGraphics3DCrossSectionPlaneCollection`
              - IAgVmVOCrossSectionPlaneCollection Interface for defining collections of planar cross-sections for the volumetric grid.

            * - :pyclass:`~IVmGraphics3DVolume`
              - IAgVmVOVolume Interface for defining volume for volumetric object.

            * - :pyclass:`~IVmGraphics3DActiveGridPoints`
              - IAgVmVOActiveGridPoints Interface for defining Active Grid Points for Volumetric Object.

            * - :pyclass:`~IVmGraphics3DSpatialCalculationLevels`
              - IAgVmVOSpatialCalculationLevels Interface for defining Spatial Calculation Levels for Volumetric Object.

            * - :pyclass:`~IVmGraphics3DSpatialCalculationLevelCollection`
              - IAgVmVOSpatialCalculationLevelCollection Interface for defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :pyclass:`~IVmGraphics3DLegend`
              - IAgVmVOLegend Interface for defining boundary/fill legend for volumetric object.

            * - :pyclass:`~IVmExportTool`
              - The Volumetric Export Tool.

            * - :pyclass:`~IVolumetric`
              - Volumetric properties.

            * - :pyclass:`~IVmGridSpatialCalculation`
              - IAgVmGridSpatialCalculation Interface volume grid spatial calculation.

            * - :pyclass:`~IVmExternalFile`
              - IAgVmExternalFile Interface for volume external file.

            * - :pyclass:`~IVmGraphics3DCrossSectionPlane`
              - IAgVmVOCrossSectionPlane Interface for defining planar cross-sections through the volumetric grid.

            * - :pyclass:`~IVmGraphics3DSpatialCalculationLevel`
              - IAgVmVOSpatialCalculationLevel Interface for defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :pyclass:`~ISatelliteCollection`
              - SatelliteCollection properties.

            * - :pyclass:`~ISubset`
              - Subset properties.

            * - :pyclass:`~IAdvCATAvailableObjectCollection`
              - IAgAdvCATAvailableObjectCollection represents available objects.

            * - :pyclass:`~IAdvCATChosenObjectCollection`
              - Chosen object collection.

            * - :pyclass:`~IAdvCATPreFilters`
              - Pre-Filters.

            * - :pyclass:`~IAdvCATAdvancedEllipsoid`
              - Advanced ellipsoid properties.

            * - :pyclass:`~IAdvCATAdvanced`
              - AdvCAT Advanced properties.

            * - :pyclass:`~IAdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :pyclass:`~IAdvCAT`
              - AgAdvCAT properties.

            * - :pyclass:`~IAdvCATChosenObject`
              - Chosen object.

            * - :pyclass:`~IEOIRShapeObject`
              - A shape object interface.

            * - :pyclass:`~IEOIRShapeBox`
              - A box shape interface.

            * - :pyclass:`~IEOIRShapeCone`
              - A cone shape interface.

            * - :pyclass:`~IEOIRShapePlate`
              - A plate shape interface.

            * - :pyclass:`~IEOIRShapeSphere`
              - A sphere shape interface.

            * - :pyclass:`~IEOIRShapeCoupler`
              - A coupler shape interface.

            * - :pyclass:`~IEOIRShapeNone`
              - A none shape interface.

            * - :pyclass:`~IEOIRShapeGEOComm`
              - A GEOComm shape interface.

            * - :pyclass:`~IEOIRShapeLEOComm`
              - A LEOComm shape interface.

            * - :pyclass:`~IEOIRShapeLEOImaging`
              - A LEOImaging shape interface.

            * - :pyclass:`~IEOIRShapeCustomMesh`
              - A custom mesh shape interface.

            * - :pyclass:`~IEOIRShapeTargetSignature`
              - A target signature shape interface.

            * - :pyclass:`~IEOIRStagePlume`
              - A stage interface.

            * - :pyclass:`~IEOIRShape`
              - A shape interface.

            * - :pyclass:`~IEOIRStage`
              - A stage interface.

            * - :pyclass:`~IEOIRShapeCollection`
              - IAgEOIRShapeCollection Interface.

            * - :pyclass:`~IEOIRMaterialElement`
              - A material element interface.

            * - :pyclass:`~IEOIRMaterialElementCollection`
              - IAgEOIRMaterialElementCollection Interface.

            * - :pyclass:`~IMissileEOIR`
              - EOIR interface.

            * - :pyclass:`~IVehicleEOIR`
              - Property used to access the IAgEOIR interface.

            * - :pyclass:`~IEOIRShapeCylinder`
              - A cylinder shape interface.

            * - :pyclass:`~IStkObjectChangedEventArgs`
              - Contains information about the changes in the object's state.

            * - :pyclass:`~IScenarioBeforeSaveEventArgs`
              - Contains information about the changes in the object's state.

            * - :pyclass:`~IPctCmpltEventArgs`
              - Represents a structure used by the Percent Complete events.

            * - :pyclass:`~IStkObjectPreDeleteEventArgs`
              - Arguments for the OnStkObjectPreDelete event.

            * - :pyclass:`~IStkObjectCutCopyPasteEventArgs`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~StkObject`
              - Represents a generic STK object.

            * - :pyclass:`~StkObjectRoot`
              - Top-level object in the Object Model Hierarchy.

            * - :pyclass:`~LevelAttribute`
              - Properties defining display of contour levels.

            * - :pyclass:`~LevelAttributeCollection`
              - Collection of properties defining display of contour levels.

            * - :pyclass:`~BasicAzElMask`
              - The Azimuth-Elevation Mask class.

            * - :pyclass:`~FacilityGraphics`
              - 2D Graphics properties of a Facility.

            * - :pyclass:`~PlaceGraphics`
              - 2D Graphics properties of a Place.

            * - :pyclass:`~Graphics2DRangeContours`
              - Class defining 2D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :pyclass:`~AccessConstraint`
              - Class defining access constraints.

            * - :pyclass:`~AccessConstraintCollection`
              - Collection of access constraints.

            * - :pyclass:`~Graphics3DRangeContours`
              - Class defining 3D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :pyclass:`~Graphics3DOffsetRotate`
              - Class defining rotation in the object body frame's X, Y and Z directions.

            * - :pyclass:`~Graphics3DOffsetTransformation`
              - Class defining model translation in the object body frame's X, Y and Z directions.

            * - :pyclass:`~Graphics3DOffsetAttach`
              - Class defining attach points for the attachment of lines to objects.

            * - :pyclass:`~Graphics3DOffsetLabel`
              - Class defining the offset of the position of an object label in the 3D Graphics window.

            * - :pyclass:`~Graphics3DOffset`
              - Class defining 3D offset attributes.

            * - :pyclass:`~Graphics3DMarkerShape`
              - Class defining the marker type that represents the object in the 3D Graphics window.

            * - :pyclass:`~Graphics3DMarkerFile`
              - Class defining 3D marker file attributes.

            * - :pyclass:`~Graphics3DMarker`
              - Class defining the 3D marker to represent an object at a specified threshold.

            * - :pyclass:`~Graphics3DDetailThreshold`
              - Class defining detail thresholds as an aid for improving performance when viewing in 3D.

            * - :pyclass:`~Graphics3DModelItem`
              - Class defining selection and display of 3D models.

            * - :pyclass:`~Graphics3DModelCollection`
              - Collection representing 3D model list.

            * - :pyclass:`~LabelNote`
              - Class defining label notes.

            * - :pyclass:`~LabelNoteCollection`
              - Collection representing label notes list.

            * - :pyclass:`~Graphics3DVector`
              - Class defining 3D vectors.

            * - :pyclass:`~FacilityGraphics3D`
              - 3D Graphics properties of a Facility.

            * - :pyclass:`~PlaceGraphics3D`
              - 3D Graphics properties of a Place.

            * - :pyclass:`~TerrainNormSlopeAzimuth`
              - Class defining Slope/Azimuth data for the TerrainNormal.

            * - :pyclass:`~IntervalCollection`
              - Class defining display intervals.

            * - :pyclass:`~ImmutableIntervalCollection`
              - Read-only collection of intervals.

            * - :pyclass:`~DuringAccess`
              - Class defining display intervals in terms of access to objects.

            * - :pyclass:`~DisplayTimesTimeComponent`
              - Provide methods to configure the display times using Timeline API components.

            * - :pyclass:`~StarGraphics3D`
              - Class defining 3D Graphics properties of a Star.

            * - :pyclass:`~StarGraphics`
              - Class defining 2D Graphics properties of a Star.

            * - :pyclass:`~PlanetGraphics3D`
              - Class defining 3D Graphics properties of a Planet.

            * - :pyclass:`~PlanetGraphics`
              - Class defining 2D Graphics properties of a Planet.

            * - :pyclass:`~AreaTypePattern`
              - Class defining coordinates of the AreaTarget AreaType.

            * - :pyclass:`~AreaTypePatternCollection`
              - Class defining the list of coordinates of the AreaTarget AreaType.

            * - :pyclass:`~AreaTypeEllipse`
              - Class defining the AreaTarget AreaType in terms of MajorAxis, MinorAxis and Bearing.

            * - :pyclass:`~AreaTargetGraphics3D`
              - Class to define the 3D attributes of an AreaTarget.

            * - :pyclass:`~AreaTargetGraphics`
              - Class to define the 2D attributes of an AreaTarget.

            * - :pyclass:`~Graphics3DAzElMask`
              - Class to define display labels and adjust the translucency of the 3D azimuth-elevation mask for a facility, place or target.

            * - :pyclass:`~Graphics3DModelArtic`
              - Class defining 3D model articulations.

            * - :pyclass:`~Graphics3DModelTransformationCollection`
              - Collection of available transformations in a model.

            * - :pyclass:`~Graphics3DModelTransformation`
              - Class to modify transformation values.

            * - :pyclass:`~Graphics3DModelFile`
              - Class defining 3D model file.

            * - :pyclass:`~PlanetPositionFile`
              - Class defining the planetary ephemeris file.

            * - :pyclass:`~PlanetPositionCentralBody`
              - Class defining central body used to define Planet object.

            * - :pyclass:`~PlanetOrbitDisplayTime`
              - Class defining display time of a planet's orbit.

            * - :pyclass:`~Scenario`
              - Class defining the Scenario object.

            * - :pyclass:`~ScenarioAnimation`
              - Class defining the animation properties of a Scenario.

            * - :pyclass:`~ScenarioEarthData`
              - Class defining the Earth Orientation Parameters of a Scenario.

            * - :pyclass:`~ScenarioGraphics`
              - Class defining the 2D Graphics properties of a Scenario.

            * - :pyclass:`~TerrainCollection`
              - Collection of terrain data files available in the Scenario for visualization and analysis.

            * - :pyclass:`~Terrain`
              - Class defining terrain data for a Scenario.

            * - :pyclass:`~TilesetCollection3D`
              - Collection of 3DTilesets available in the Scenario for analysis.

            * - :pyclass:`~Tileset3D`
              - Class defining Analytical 3DTileset for a Scenario.

            * - :pyclass:`~ScenarioGenDatabaseCollection`
              - Collection of Scenario database settings.

            * - :pyclass:`~ScenarioGenDatabase`
              - Class defining database settings of the Scenario.

            * - :pyclass:`~ScenarioGraphics3D`
              - Class defining 3D Graphics properties of the Scenario.

            * - :pyclass:`~SensorComplexConicPattern`
              - Class defining the complex conic pattern for a Sensor.

            * - :pyclass:`~SensorEOIRPattern`
              - Class defining the EOIR pattern for a Sensor.

            * - :pyclass:`~SensorUnknownPattern`
              - Unsupported/unknown sensor pattern.

            * - :pyclass:`~SensorEOIRBandCollection`
              - Class defining the band collection for an EOIR Sensor.

            * - :pyclass:`~SensorEOIRBand`
              - Class defining an EOIR band.

            * - :pyclass:`~SensorEOIRRadiometricPair`
              - Class defining an Sensitivities item.

            * - :pyclass:`~SensorEOIRSensitivityCollection`
              - Class defining the Sensitivities collection for an EOIR Sensor.

            * - :pyclass:`~SensorEOIRSaturationCollection`
              - Class defining the Saturations collection for an EOIR Sensor.

            * - :pyclass:`~SensorCustomPattern`
              - Class defining the custom pattern for a Sensor.

            * - :pyclass:`~SensorHalfPowerPattern`
              - Class defining the half-power pattern for a Sensor.

            * - :pyclass:`~SensorRectangularPattern`
              - Class defining the rectangular pattern for a Sensor.

            * - :pyclass:`~SensorSARPattern`
              - Class defining the Synthetic Aperture Radar (SAR) pattern for a Sensor.

            * - :pyclass:`~SensorSimpleConicPattern`
              - Class defining the simple conic pattern for a Sensor.

            * - :pyclass:`~SensorPointingFixed`
              - Class defining the fixed pointing type for a Sensor.

            * - :pyclass:`~SensorPointingFixedAxes`
              - Class defining the fixed in axes pointing type for a Sensor.

            * - :pyclass:`~SensorPointing3DModel`
              - Class defining the 3D model pointing type for a Sensor.

            * - :pyclass:`~SensorPointingSpinning`
              - Class defining the spinning pointing type for a Sensor.

            * - :pyclass:`~SensorPointingTargeted`
              - Class defining the targeted pointing type for a Sensor.

            * - :pyclass:`~SensorPointingExternal`
              - Class defining the external file-defined pointing type for a Sensor.

            * - :pyclass:`~SensorPointingTargetedBoresightTrack`
              - Class defining a targeted sensor with tracking boresight.

            * - :pyclass:`~SensorPointingTargetedBoresightFixed`
              - Class defining a targeted Sensor with fixed boresight.

            * - :pyclass:`~SensorTargetCollection`
              - Class defining the target collection for a target-pointing Sensor.

            * - :pyclass:`~SensorTarget`
              - Class defining a Sensor target.

            * - :pyclass:`~AccessTime`
              - Class for defining Sensor target times in terms of access.

            * - :pyclass:`~ScheduleTime`
              - Class for defining Sensor target times in terms of a specified schedule.

            * - :pyclass:`~SensorAzElMaskFile`
              - Class to define a Sensor's Azimuth-Elevation mask.

            * - :pyclass:`~SensorGraphics`
              - Class defining the 2D Graphics properties of a Sensor.

            * - :pyclass:`~SensorProjection`
              - Class defining the projection properties of a Sensor.

            * - :pyclass:`~SensorProjectionDisplayDistance`
              - Class defining projection altitude options for a sensor.

            * - :pyclass:`~SensorGraphics3D`
              - Class defining 3D Graphics properties of a Sensor.

            * - :pyclass:`~SensorGraphics3DPulse`
              - Class defining 3D pulse properties of a Sensor.

            * - :pyclass:`~SensorGraphics3DOffset`
              - Class defining 3D Graphics vertex offset properties of a Sensor.

            * - :pyclass:`~AccessConstraintTimeSlipRange`
              - Class for controlling the use the Time Slip constraint for a missile or launch vehicle, used with the Close Approach Tool.

            * - :pyclass:`~AccessConstraintBackground`
              - Class related to the Background constraint, which constrains access periods based on whether the Earth is or is not in the background.

            * - :pyclass:`~AccessConstraintGroundTrack`
              - Class related to the Ground Track constraint, which constrains access to the Ascending or Descending side of the Satellite's ground track.

            * - :pyclass:`~AccessConstraintMinMax`
              - Class related to defining constraints in terms of minimum and/or maximum values.

            * - :pyclass:`~AccessConstraintCrdnConstellation`
              - Class related to Vector constraints.

            * - :pyclass:`~AccessConstraintCentralBodyObstruction`
              - Class defining constraints in terms of obstruction by a specified central body.

            * - :pyclass:`~AccessConstraintAngle`
              - Class defining Angle constraints, limiting access to intervals during which the selected angle is within the specified minimum and maximum limits.

            * - :pyclass:`~AccessConstraintCondition`
              - Class defining access constraints in terms of lighting conditions.

            * - :pyclass:`~AccessTimeCollection`
              - Collection of access times.

            * - :pyclass:`~ScheduleTimeCollection`
              - Collection of user-scheduled access times.

            * - :pyclass:`~AccessConstraintIntervals`
              - Class defining the Intervals constraint.

            * - :pyclass:`~AccessConstraintObjExAngle`
              - Class defining the Object Exclusion Angle constraint.

            * - :pyclass:`~AccessConstraintZone`
              - Class defining the Exclusion Zone constraint.

            * - :pyclass:`~AccessConstraintThirdBody`
              - Do not use this class, as it is deprecated. Use AgAccessCnstrCbObstruction instead. Class defining Central Body Obstruction constraints.

            * - :pyclass:`~AccessConstraintExclZonesCollection`
              - Collection of Exclusion Zones used in Exclusion Zone constraint.

            * - :pyclass:`~AccessConstraintGrazingAltitude`
              - Class defining the Grazing Altidude constraint.

            * - :pyclass:`~SensorPointingGrazingAltitude`
              - Class defining Grazing Altitude pointing type for a Sensor.

            * - :pyclass:`~AreaTarget`
              - Class defining the AreaTarget object.

            * - :pyclass:`~Facility`
              - Class defining the Facility object.

            * - :pyclass:`~Target`
              - Class defining the Target object.

            * - :pyclass:`~Place`
              - Class defining the Place object.

            * - :pyclass:`~Planet`
              - Class defining the Planet object.

            * - :pyclass:`~Sensor`
              - Class defining the Sensor class.

            * - :pyclass:`~SensorCommonTasks`
              - Class defining the Sensor Common class.

            * - :pyclass:`~AreaTargetCommonTasks`
              - Class defining the Area Target Common class.

            * - :pyclass:`~PlanetCommonTasks`
              - Class defining the Planet Common class.

            * - :pyclass:`~Swath`
              - Class defining Swath properties.

            * - :pyclass:`~Star`
              - Class defining the Star object.

            * - :pyclass:`~DataProviderCollection`
              - Collection of data providers attached to the current STK object.

            * - :pyclass:`~DataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :pyclass:`~DataProviderResult`
              - Results returned by the data provider.

            * - :pyclass:`~DataProviderResultSubSectionCollection`
              - Represents a collection of subsections returned by the data providers.

            * - :pyclass:`~DataProviderResultSubSection`
              - Represents a subsection in the data returned by the data providers.

            * - :pyclass:`~DataProviderResultIntervalCollection`
              - Represents a collection of intervals returned by the data providers.

            * - :pyclass:`~DataProviderResultInterval`
              - Represents a interval in the collection of intervals returned by the data providers.

            * - :pyclass:`~DataProviderResultDataSetCollection`
              - Represents a collection of datasets in the interval returned by the data providers.

            * - :pyclass:`~DataProviderResultDataSet`
              - Represents a dataset in the collection of datasets returned by the data providers.

            * - :pyclass:`~DataProviderFixed`
              - Support for fixed data providers (i.e. non time-dependent like Facility position).

            * - :pyclass:`~DataProviderTimeVarying`
              - Support for time-dependent data providers (e.g. Satellite position).

            * - :pyclass:`~DataProviderInterval`
              - Support for interval data providers (e.g. Facility lighting times).

            * - :pyclass:`~DataProviderResultTextMessage`
              - Notification or failure messages returned by the data provider.

            * - :pyclass:`~DataProviderGroup`
              - Group of sub data providers (e.g. ``Cartesian Position`` on Satellites).

            * - :pyclass:`~DataProviderElements`
              - Elements returned by the data provider (e.g. ``x``, ``y``, ``z``).

            * - :pyclass:`~DataProviderElement`
              - Class defining a data provider element.

            * - :pyclass:`~DataProviders`
              - Class defining data providers.

            * - :pyclass:`~StkAccess`
              - Class defining Access.

            * - :pyclass:`~StkAccessGraphics`
              - Class defining 2D Graphics for Access.

            * - :pyclass:`~StkAccessAdvanced`
              - Class defining advanced Access settings.

            * - :pyclass:`~AccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :pyclass:`~AccessTimeEventIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :pyclass:`~StkObjectCoverage`
              - Class defining object coverage.

            * - :pyclass:`~ObjectCoverageFigureOfMerit`
              - Class defining the fom on the coverage object tool.

            * - :pyclass:`~Scenario3dFont`
              - Font properties for Scenario 3D Graphics.

            * - :pyclass:`~Graphics3DBorderWall`
              - Class defining 3D Graphics border wall properties.

            * - :pyclass:`~Graphics3DReferenceAnalysisWorkbenchCollection`
              - Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

            * - :pyclass:`~Graphics3DReferenceVectorGeometryToolVector`
              - Class defining a reference vector (3D Graphics, Vector Geometry Tool).

            * - :pyclass:`~Graphics3DReferenceVectorGeometryToolAxes`
              - Class defining a set of reference axes (3D Graphics, Vector Geometry Tool).

            * - :pyclass:`~Graphics3DReferenceVectorGeometryToolAngle`
              - Class defining a reference angle (3D Graphics, Vector Geometry Tool).

            * - :pyclass:`~Graphics3DReferenceVectorGeometryToolPlane`
              - Class defining a reference plane (3D Graphics, Vector Geometry Tool).

            * - :pyclass:`~Graphics3DReferenceVectorGeometryToolPoint`
              - Class defining a reference point (3D Graphics, Vector Geometry Tool).

            * - :pyclass:`~TargetGraphics`
              - Class defining 2D Graphics for a Target object.

            * - :pyclass:`~TargetGraphics3D`
              - Class defining 3D Graphics for a Target object.

            * - :pyclass:`~PointTargetGraphics3DModel`
              - Point properties for a 3D model.

            * - :pyclass:`~ObjectLinkCollection`
              - Collection of names of STK objects that are available in the current Scenario.

            * - :pyclass:`~ObjectLink`
              - Class defining name of an STK object.

            * - :pyclass:`~LinkToObject`
              - Class defining a link to an STK object.

            * - :pyclass:`~LLAPosition`
              - Class defining position defined in terms of latitude, longitude and altitude (LLA).

            * - :pyclass:`~Graphics3DDataDisplayElement`
              - Class defining 3D Graphics data display element.

            * - :pyclass:`~Graphics3DDataDisplayCollection`
              - Collection of 3D Graphics data display text.

            * - :pyclass:`~VehicleInitialState`
              - Class defining the initial state of the vehicle.

            * - :pyclass:`~VehicleHPOPCentralBodyGravity`
              - Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

            * - :pyclass:`~VehicleRadiationPressure`
              - Class defining solar radiation pressure on a vehicle.

            * - :pyclass:`~VehicleHPOPSolarRadiationPressure`
              - Class defining HPOP solar radiation pressure properties.

            * - :pyclass:`~VehicleSolarFluxGeoMagnitudeEnterManually`
              - Class defining the option to enter a vehicle's solar flux and/or GeoMag properties manually, depending on the selected atmospheric density model.

            * - :pyclass:`~VehicleSolarFluxGeoMagnitudeUseFile`
              - Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

            * - :pyclass:`~VehicleHPOPForceModelDrag`
              - Class defining the HPOP atmospheric drag model.

            * - :pyclass:`~VehicleHPOPForceModelDragOptions`
              - Class defining HPOP atmospheric drag options.

            * - :pyclass:`~VehicleHPOPSolarRadiationPressureOptions`
              - Class defining HPOP solar radiation pressure options.

            * - :pyclass:`~VehicleStatic`
              - Class defining static force model options for the HPOP propagator.

            * - :pyclass:`~VehicleSolidTides`
              - Class defining the contribution of solid tides.

            * - :pyclass:`~VehicleOceanTides`
              - Class defining the contribution of ocean tides.

            * - :pyclass:`~VehiclePluginSettings`
              - Class defining force model plugin settings for HPOP.

            * - :pyclass:`~VehiclePluginPropagator`
              - Class defining a propagator plugin for HPOP for customization of the accelerations used in the propagation of the satellite trajectory.

            * - :pyclass:`~VehicleHPOPForceModelMoreOptions`
              - Class defining additional force model options for HPOP.

            * - :pyclass:`~VehicleHPOPForceModel`
              - Class defining HPOP force models.

            * - :pyclass:`~VehicleStepSizeControl`
              - Class defining step size control for the HPOP integrator.

            * - :pyclass:`~VehicleTimeRegularization`
              - Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

            * - :pyclass:`~VehicleInterpolation`
              - Class defining interpolation for the HPOP integrator.

            * - :pyclass:`~VehicleIntegrator`
              - Class defining the HPOP integrator.

            * - :pyclass:`~VehicleGravity`
              - Class defining gravity modeling options for a vehicle.

            * - :pyclass:`~VehiclePositionVelocityElement`
              - Class defining position and velocity elements for HPOP covariance.

            * - :pyclass:`~VehiclePositionVelocityCollection`
              - Collection of position and velocity elements for HPOP covariance.

            * - :pyclass:`~VehicleCorrelationListCollection`
              - Collection representing HPOP covariance matrix.

            * - :pyclass:`~VehicleCorrelationListElement`
              - Class representing an element of an HPOP covariance matrix.

            * - :pyclass:`~VehicleCovariance`
              - Class defining HPOP covariance.

            * - :pyclass:`~VehicleJxInitialState`
              - Class defining initial state for the J2/4 propagators.

            * - :pyclass:`~VehicleLOPCentralBodyGravity`
              - Class defining gravity options for the LOP propagator.

            * - :pyclass:`~VehicleThirdBodyGravityElement`
              - Class defining third-body gravity options for the LOP propagator.

            * - :pyclass:`~VehicleThirdBodyGravityCollection`
              - Collection of third-body gravity options for the LOP propagator.

            * - :pyclass:`~VehicleExpDensModelParams`
              - Class defining the Exponential atmospheric density model for the LOP propagator.

            * - :pyclass:`~VehicleAdvanced`
              - Class defining advanced atmospheric density options for the LOP propagator.

            * - :pyclass:`~VehicleLOPForceModelDrag`
              - Class defining the atmospheric drag model for the LOP propagator.

            * - :pyclass:`~VehicleLOPSolarRadiationPressure`
              - Class defining the solar radiation pressure model for the LOP propagator.

            * - :pyclass:`~VehiclePhysicalData`
              - Class defining physical data for the LOP force model.

            * - :pyclass:`~VehicleLOPForceModel`
              - Class defining the force model for the LOP propagator.

            * - :pyclass:`~VehicleSegmentsCollection`
              - Collection of segments for a vehicle.

            * - :pyclass:`~VehiclePropagatorHPOP`
              - Class defining the High Precision Orbit Propagator (HPOP).

            * - :pyclass:`~VehiclePropagatorJ2Perturbation`
              - Class defining the J2 perturbation propagator.

            * - :pyclass:`~VehiclePropagatorJ4Perturbation`
              - Class defining the J4 perturbation propagator.

            * - :pyclass:`~VehiclePropagatorLOP`
              - Class defining the Long-term Orbit Predictor (LOP).

            * - :pyclass:`~VehiclePropagatorSGP4`
              - Class defining the SGP4 propagator.

            * - :pyclass:`~VehiclePropagatorSPICE`
              - Class defining the SPICE propagator.

            * - :pyclass:`~VehiclePropagatorStkExternal`
              - Class defining the STK External propagator.

            * - :pyclass:`~VehiclePropagatorTwoBody`
              - Class defining the two body propagator.

            * - :pyclass:`~VehiclePropagatorUserExternal`
              - Class defining the user-external propagator.

            * - :pyclass:`~VehicleLaunchVehicleInitialState`
              - Class defining launch vehicle initial state.

            * - :pyclass:`~VehiclePropagatorSimpleAscent`
              - Class defining the simple ascent propagator for a launch vehicle.

            * - :pyclass:`~VehicleWaypointsElement`
              - Class defining a waypoint for a Great Arc vehicle.

            * - :pyclass:`~VehicleWaypointsCollection`
              - Collection of waypoints for a Great Arc vehicle.

            * - :pyclass:`~VehicleLaunchLLA`
              - Class defining geodetic launch latitude, longitude and altitude for a Missile or LaunchVehicle.

            * - :pyclass:`~VehicleLaunchLLR`
              - Class defining geocentric launch latitude, longitude and radius for a Missile or LaunchVehicle.

            * - :pyclass:`~VehicleImpactLLA`
              - Class defining geodetic impact latitude, longitude and altitude for a Missile.

            * - :pyclass:`~VehicleImpactLLR`
              - Class defining geocentric impact latitude, longitude and radius for a Missile.

            * - :pyclass:`~VehicleLaunchControlFixedApogeeAltitude`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed apogee altitude.

            * - :pyclass:`~VehicleLaunchControlFixedDeltaV`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V.

            * - :pyclass:`~VehicleLaunchControlFixedDeltaVMinEccentricity`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V with minimum eccentricity.

            * - :pyclass:`~VehicleLaunchControlFixedTimeOfFlight`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed time of flight.

            * - :pyclass:`~VehicleImpactLocationLaunchAzEl`
              - Class defining the option to use azimuth and elevation to specify the Missile's impact location.

            * - :pyclass:`~VehicleImpactLocationPoint`
              - Class defining a Missile's impact location.

            * - :pyclass:`~VehiclePropagatorBallistic`
              - Class defining the ballistic propagator for a Missile.

            * - :pyclass:`~VehiclePropagatorGreatArc`
              - Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

            * - :pyclass:`~VehicleSGP4SegmentCollection`
              - Set of Trajectories.

            * - :pyclass:`~VehicleSGP4Segment`
              - SGP4 propagator segment.

            * - :pyclass:`~VehicleThirdBodyGravity`
              - Third body gravity options for Long-range Orbit Predictor (LOP) propagator.

            * - :pyclass:`~VehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :pyclass:`~VehicleConsiderAnalysisCollection`
              - The Consider Analysis list for HPOP covariance.

            * - :pyclass:`~VehicleSPICESegment`
              - SPICE propagator segment.

            * - :pyclass:`~VehicleWaypointAltitudeReferenceTerrain`
              - Terrain altitude reference.

            * - :pyclass:`~VehicleWaypointAltitudeReference`
              - Altitude references.

            * - :pyclass:`~VehicleSGP4LoadFile`
              - SGP4 propagator. Allows the user to load segments from file.

            * - :pyclass:`~VehicleSGP4OnlineLoad`
              - SGP4 propagator. Allows the user to load segments from online.

            * - :pyclass:`~VehicleSGP4OnlineAutoLoad`
              - Do not use this class, as it is deprecated. Use AgVeSGP4OnlineLoad instead. SGP4 propagator. Allows the user to load the most current segment from online.

            * - :pyclass:`~VehicleGroundEllipsesCollection`
              - List of Ground Ellipses.

            * - :pyclass:`~Satellite`
              - Satellite properties.

            * - :pyclass:`~VehicleInertia`
              - Satellite inertia matrix parameters.

            * - :pyclass:`~VehicleMassProperties`
              - Satellite Mass properties.

            * - :pyclass:`~VehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :pyclass:`~VehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :pyclass:`~VehicleDefinition`
              - Pass break definition properties.

            * - :pyclass:`~VehicleRepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :pyclass:`~VehiclePassNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :pyclass:`~VehiclePassNumberingFirstPassNum`
              - First pass number.

            * - :pyclass:`~VehiclePassBreak`
              - Satellite Pass Break properties.

            * - :pyclass:`~VehicleCentralBodies`
              - Satellite Central Bodies.

            * - :pyclass:`~SatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :pyclass:`~SatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :pyclass:`~VehicleEllipseDataElement`
              - Ground ellipse data.

            * - :pyclass:`~VehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :pyclass:`~VehicleGroundEllipseElement`
              - Ground ellipse.

            * - :pyclass:`~SatelliteGraphics3DModel`
              - All Satellite's VO Model properties.

            * - :pyclass:`~VehicleEclipseBodies`
              - Satellite Eclipse Bodies, for defining the eclipse central body list used for lighting computations.

            * - :pyclass:`~VehicleVector`
              - Aligned and Constrained attitude profile.

            * - :pyclass:`~VehicleRateOffset`
              - AgVeSpin Class.

            * - :pyclass:`~VehicleProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :pyclass:`~VehicleProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :pyclass:`~VehicleProfileConstraintOffset`
              - Constraint offset for various attitude profiles.

            * - :pyclass:`~VehicleProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :pyclass:`~VehicleProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :pyclass:`~VehicleProfileSpinAboutXXX`
              - Shared for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :pyclass:`~VehicleProfileSpinning`
              - Spinning attitude profile.

            * - :pyclass:`~VehicleProfileAlignmentOffset`
              - Alignment offset for various attitude profiles.

            * - :pyclass:`~VehicleScheduleTimesCollection`
              - List of scheduled accesses.

            * - :pyclass:`~VehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :pyclass:`~VehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :pyclass:`~VehicleDuration`
              - Look ahead and look behind duration options.

            * - :pyclass:`~VehicleStandardBasic`
              - Basic attitude profile.

            * - :pyclass:`~VehicleAttitudeExternal`
              - External attitude (.a) file.

            * - :pyclass:`~VehicleAttitudeRealTime`
              - Real time attitude.

            * - :pyclass:`~VehicleProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :pyclass:`~VehicleProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :pyclass:`~VehicleAttitudeTrendControlAviator`
              - Trending controls for Aviator attitude.

            * - :pyclass:`~VehicleProfileAviator`
              - The profile used for Aviator aircraft.

            * - :pyclass:`~VehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :pyclass:`~VehicleTargetPointingCollection`
              - List of Attitude Targets.

            * - :pyclass:`~VehicleTorque`
              - Torque file to use in defining integrated attitude.

            * - :pyclass:`~VehicleIntegratedAttitude`
              - Integrated Attitude generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :pyclass:`~VehicleScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :pyclass:`~VehicleTrajectoryAttitudeStandard`
              - Standard attitude profile for launch vehicle or missile.

            * - :pyclass:`~VehicleOrbitAttitudeStandard`
              - Standard attitude profile for satellite.

            * - :pyclass:`~VehicleRouteAttitudeStandard`
              - Standard attitude profile for aircraft.

            * - :pyclass:`~VehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :pyclass:`~VehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :pyclass:`~VehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :pyclass:`~VehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :pyclass:`~VehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :pyclass:`~VehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :pyclass:`~VehicleGraphics2DLighting`
              - Lighting.

            * - :pyclass:`~VehicleGraphics2DElevationGroundElevation`
              - Ground elevation for vehicle swath.

            * - :pyclass:`~VehicleGraphics2DElevationSwathHalfWidth`
              - Half width for vehicle swath.

            * - :pyclass:`~VehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle for vehicle swath.

            * - :pyclass:`~VehicleGraphics2DSwath`
              - Vehicle swath.

            * - :pyclass:`~VehicleGraphics2DLeadDataFraction`
              - 2D Graphics pass: fraction of leading portion of vehicle track to display.

            * - :pyclass:`~VehicleGraphics2DLeadDataTime`
              - 2D Graphics pass: time-defined segment of leading portion of vehicle track to display.

            * - :pyclass:`~VehicleGraphics2DTrailDataFraction`
              - 2D Graphics pass: fraction of trailing portion of vehicle track to display.

            * - :pyclass:`~VehicleGraphics2DTrailDataTime`
              - 2D Graphics pass: time-defined segment of trailing portion of vehicle track to display.

            * - :pyclass:`~VehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :pyclass:`~VehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :pyclass:`~VehicleGraphics2DOrbitPassData`
              - AgVeGfxPassData Class.

            * - :pyclass:`~VehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :pyclass:`~VehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :pyclass:`~VehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :pyclass:`~VehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :pyclass:`~VehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :pyclass:`~VehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :pyclass:`~VehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :pyclass:`~VehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :pyclass:`~VehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :pyclass:`~VehicleGraphics2DPasses`
              - Settings for satellite pass display graphics.

            * - :pyclass:`~VehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :pyclass:`~VehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :pyclass:`~VehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :pyclass:`~VehicleGraphics2DElevContours`
              - General settings regarding display of elevation contours.

            * - :pyclass:`~VehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :pyclass:`~VehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :pyclass:`~VehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :pyclass:`~VehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :pyclass:`~VehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :pyclass:`~VehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :pyclass:`~VehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :pyclass:`~VehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :pyclass:`~VehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :pyclass:`~VehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :pyclass:`~Graphics3DPointableElementsElement`
              - Pointable elements for 3D model pointing.

            * - :pyclass:`~Graphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :pyclass:`~VehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :pyclass:`~VehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :pyclass:`~VehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :pyclass:`~VehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :pyclass:`~VehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :pyclass:`~VehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :pyclass:`~VehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :pyclass:`~VehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :pyclass:`~VehicleGraphics3DGeoBox`
              - Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :pyclass:`~VehicleGraphics3DRouteProximity`
              - Proximity graphics for GreatArc Vehicles.

            * - :pyclass:`~VehicleGraphics3DOrbitProximity`
              - Proximity graphics.

            * - :pyclass:`~VehicleGraphics3DElevContours`
              - 3D elevation angle contours.

            * - :pyclass:`~VehicleGraphics3DSAA`
              - 3D South Atlantic Anomaly contours.

            * - :pyclass:`~VehicleGraphics3DSigmaScaleProbability`
              - Sigma probability for indirect sizing of covariance pointing contours.

            * - :pyclass:`~VehicleGraphics3DSigmaScaleScale`
              - Sigma scale for direct sizing of covariance pointing contours.

            * - :pyclass:`~VehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :pyclass:`~VehicleGraphics3DIntervalsElement`
              - Intervals graphics for covariance pointing contour.

            * - :pyclass:`~VehicleGraphics3DIntervalsCollection`
              - List of Intervals.

            * - :pyclass:`~VehicleGraphics3DAttributesBasic`
              - Basic 3D graphics for covariance pointing contours.

            * - :pyclass:`~VehicleGraphics3DAttributesIntervals`
              - 3D graphics based on intervals for covariance pointing contours.

            * - :pyclass:`~VehicleGraphics3DSize`
              - 3D graphics vector size.

            * - :pyclass:`~VehicleGraphics3DCovariancePointingContour`
              - Covariance pointing contours.

            * - :pyclass:`~VehicleGraphics3DDataFraction`
              - Fraction for 3D track display.

            * - :pyclass:`~VehicleGraphics3DDataTime`
              - Time.

            * - :pyclass:`~VehicleGraphics3DOrbitPassData`
              - Satellite 3D ground and orbit track data.

            * - :pyclass:`~VehicleGraphics3DOrbitTrackData`
              - 3D leading/trailing track data for satellites.

            * - :pyclass:`~VehicleGraphics3DTickDataLine`
              - Line type tick marks.

            * - :pyclass:`~VehicleGraphics3DTickDataPoint`
              - Point type tick mark.

            * - :pyclass:`~VehicleGraphics3DOrbitTickMarks`
              - Tick mark for satellites.

            * - :pyclass:`~VehicleGraphics3DPass`
              - 3D pass for satellites.

            * - :pyclass:`~VehicleGraphics3DCovariance`
              - 3D position covariance ellipsoids.

            * - :pyclass:`~VehicleGraphics3DVelCovariance`
              - 3D velocity covariance ellipsoids.

            * - :pyclass:`~VehicleGraphics3DTrajectoryProximity`
              - AgVeTrajectoryProximity Class.

            * - :pyclass:`~VehicleGraphics3DTrajectory`
              - AgLvVOTrajectory Class.

            * - :pyclass:`~VehicleGraphics3DTrajectoryTrackData`
              - 3D leading/trailing track data for launch vehicles and missiles.

            * - :pyclass:`~VehicleGraphics3DTrajectoryPassData`
              - 3D ground track and trajectory data for a launch vehicle or missile.

            * - :pyclass:`~VehicleGraphics3DLeadTrailData`
              - AgLvVOTrajectory2 Class.

            * - :pyclass:`~VehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data for launch vehicles and missiles.

            * - :pyclass:`~VehicleGraphics3DPathTickMarks`
              - Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :pyclass:`~VehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint.

            * - :pyclass:`~VehicleGraphics3DWaypointMarkersCollection`
              - Collection of Waypoint Markers .

            * - :pyclass:`~VehicleGraphics3DRoute`
              - AgVeVORoute2 Class.

            * - :pyclass:`~Graphics3DModelPointing`
              - List of pointable model elements.

            * - :pyclass:`~Graphics3DLabelSwapDistance`
              - Control the level of detail in labels and other screen objects at specified distances.

            * - :pyclass:`~VehicleGraphics3DDropLinePositionItem`
              - Drop lines from the vehicle's current position.

            * - :pyclass:`~VehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :pyclass:`~VehicleGraphics3DDropLinePathItem`
              - Drop lines at intervals along the vehicle's path.

            * - :pyclass:`~VehicleGraphics3DDropLinePathItemCollection`
              - Collection of drop lines from the vehicle's orbit or trajectory.

            * - :pyclass:`~VehicleGraphics3DOrbitDropLines`
              - Droplines collections.

            * - :pyclass:`~VehicleGraphics3DRouteDropLines`
              - Droplines for great arc vehicles.

            * - :pyclass:`~VehicleGraphics3DTrajectoryDropLines`
              - Droplines for launch vehicles and missiles.

            * - :pyclass:`~VehicleTrajectoryGraphics3DModel`
              - Marker for launch vehicle or missile.

            * - :pyclass:`~VehicleRouteGraphics3DModel`
              - 3D marker for great arc vehicles.

            * - :pyclass:`~VehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of IAgVeVOBPlaneTemplateDisplayCollection.

            * - :pyclass:`~VehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :pyclass:`~VehicleGraphics3DBPlaneTemplate`
              - An element of IAgVeVOBPlaneTemplatesCollection.

            * - :pyclass:`~VehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :pyclass:`~VehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :pyclass:`~VehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :pyclass:`~VehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :pyclass:`~VehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :pyclass:`~VehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :pyclass:`~VehicleGraphics3DBPlaneInstance`
              - An element in the IAgVeVOBPlanePointCollection.

            * - :pyclass:`~VehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :pyclass:`~VehicleGraphics3DBPlanePointCollection`
              - AgVeVOBPlaneCollection Class.

            * - :pyclass:`~VehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :pyclass:`~LaunchVehicle`
              - Launch vehicle object.

            * - :pyclass:`~LaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :pyclass:`~LaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :pyclass:`~GroundVehicle`
              - Ground vehicle object.

            * - :pyclass:`~GroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :pyclass:`~GroundVehicleGraphics3D`
              - AgGvVOVO Class.

            * - :pyclass:`~Missile`
              - Missile object.

            * - :pyclass:`~MissileGraphics`
              - 2D Graphics for missiles.

            * - :pyclass:`~MissileGraphics3D`
              - 3D Graphics for missiles.

            * - :pyclass:`~Aircraft`
              - Aircraft object.

            * - :pyclass:`~AircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :pyclass:`~AircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :pyclass:`~Ship`
              - Ship object.

            * - :pyclass:`~ShipGraphics`
              - 2D Graphics options for a ship.

            * - :pyclass:`~ShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :pyclass:`~MtoTrackPoint`
              - The points defined for the selected track.

            * - :pyclass:`~MtoTrackPointCollection`
              - MTO track point list.

            * - :pyclass:`~MtoTrack`
              - List of MTO tracks with basic information about each.

            * - :pyclass:`~MtoTrackCollection`
              - MTO Track List.

            * - :pyclass:`~MtoDefaultTrack`
              - Default MTO track.

            * - :pyclass:`~MtoGlobalTrackOptions`
              - Global MTO track options.

            * - :pyclass:`~Mto`
              - Multi-Track Object (MTO).

            * - :pyclass:`~MtoGraphics2DMarker`
              - Define the 2D graphics attributes of the selected MTO track or tracks.

            * - :pyclass:`~MtoGraphics2DLine`
              - MTO track line display options.

            * - :pyclass:`~MtoGraphics2DFadeTimes`
              - MTO track fade times.

            * - :pyclass:`~MtoGraphics2DLeadTrailTimes`
              - MTO track lead/trail times.

            * - :pyclass:`~MtoGraphics2DTrack`
              - 2D graphics attributes for each track in the MTO.

            * - :pyclass:`~MtoGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :pyclass:`~MtoDefaultGraphics2DTrack`
              - 2D graphics attributes for default MTO tracks.

            * - :pyclass:`~MtoGraphics2DGlobalTrackOptions`
              - Global 2D graphics options for an MTO.

            * - :pyclass:`~MtoGraphics`
              - MTO 2D Graphics.

            * - :pyclass:`~MtoGraphics3DMarker`
              - MTO 3D graphics marker options.

            * - :pyclass:`~MtoGraphics3DPoint`
              - MTO track 3D marker point options.

            * - :pyclass:`~MtoGraphics3DModel`
              - MTO track model options.

            * - :pyclass:`~MtoGraphics3DSwapDistances`
              - MTO track 3D swap distances.

            * - :pyclass:`~MtoGraphics3DDropLines`
              - MTO droplines.

            * - :pyclass:`~MtoGraphics3DTrack`
              - 3D graphics properties for MTO tracks.

            * - :pyclass:`~MtoGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :pyclass:`~MtoDefaultGraphics3DTrack`
              - 3D graphics properties for default MTO tracks.

            * - :pyclass:`~MtoGraphics3DGlobalTrackOptions`
              - Global 3D graphics MTO track options.

            * - :pyclass:`~MtoGraphics3D`
              - MTO 3D graphics properties.

            * - :pyclass:`~LLAGeocentric`
              - Geocentric LLA position.

            * - :pyclass:`~LLAGeodetic`
              - Geodetic LLA position.

            * - :pyclass:`~LineTargetPoint`
              - Line Target Point.

            * - :pyclass:`~LineTargetPointCollection`
              - The collection of points for the line target.

            * - :pyclass:`~LineTarget`
              - Line Target Path properties.

            * - :pyclass:`~LineTargetGraphics`
              - The AgLtGraphics class.

            * - :pyclass:`~LineTargetGraphics3D`
              - The AgLtVO class.

            * - :pyclass:`~CoverageDefinition`
              - The AgCoverageDefinition class.

            * - :pyclass:`~CoverageBoundsCustomRegions`
              - Custom Regions.

            * - :pyclass:`~CoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :pyclass:`~CoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :pyclass:`~CoverageBoundsLat`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :pyclass:`~CoverageBoundsLatLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :pyclass:`~CoverageBoundsLonLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :pyclass:`~CoverageBoundsLatLonRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :pyclass:`~CoverageGrid`
              - Grid Definition and resolution.

            * - :pyclass:`~CoverageAssetListElement`
              - Coverage asset.

            * - :pyclass:`~CoverageAssetListCollection`
              - Asset List.

            * - :pyclass:`~CoverageRegionFilesCollection`
              - Collection of Region Files.

            * - :pyclass:`~CoverageAreaTargetsCollection`
              - Collection of Area Targets.

            * - :pyclass:`~CoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :pyclass:`~CoveragePointFileListCollection`
              - Point file list collection.

            * - :pyclass:`~CoverageAdvanced`
              - Advanced Properties.

            * - :pyclass:`~CoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :pyclass:`~CoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :pyclass:`~CoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :pyclass:`~CoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :pyclass:`~CoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :pyclass:`~CoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :pyclass:`~CoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :pyclass:`~CoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :pyclass:`~CoverageGraphics3D`
              - AgCvVOStatic Class.

            * - :pyclass:`~CoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :pyclass:`~ChainTimePeriodBase`
              - Chain time period options.

            * - :pyclass:`~ChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :pyclass:`~ChainConstraints`
              - Chain constraints.

            * - :pyclass:`~Chain`
              - AgChain Class is used to access the methods and properties of the STK Chain Object.

            * - :pyclass:`~ChainConnection`
              - Class defining Chain connections.

            * - :pyclass:`~ChainConnectionCollection`
              - Class defining a collection of Chain connections.

            * - :pyclass:`~ChainOptimalStrandOpts`
              - Class defining Chain optimal strand options.

            * - :pyclass:`~ChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :pyclass:`~ChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :pyclass:`~ChainGraphics`
              - 2D graphics properties of a chain.

            * - :pyclass:`~ChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :pyclass:`~RefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :pyclass:`~RefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :pyclass:`~RefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :pyclass:`~RefractionModelSCFMethod`
              - SCF Method.

            * - :pyclass:`~FigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :pyclass:`~FigureOfMeritDefinitionDataMinMax`
              - Minimum and maximum data values for navigation accuracy.

            * - :pyclass:`~FigureOfMeritDefinitionDataMinAssets`
              - Minimum number of assets.

            * - :pyclass:`~FigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :pyclass:`~FigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :pyclass:`~FigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best 4 satellites.

            * - :pyclass:`~FigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :pyclass:`~FigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :pyclass:`~FigureOfMerit`
              - Figure of Merit properties.

            * - :pyclass:`~FigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :pyclass:`~FigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :pyclass:`~FigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :pyclass:`~FigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :pyclass:`~FigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionSystemAgeOfData`
              - System Age Of Data Figure of Merit.

            * - :pyclass:`~FigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :pyclass:`~FigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :pyclass:`~FigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :pyclass:`~FigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :pyclass:`~FigureOfMeritGraphics`
              - AgFmGfxGraphics Class.

            * - :pyclass:`~FigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :pyclass:`~FigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :pyclass:`~FigureOfMeritGraphics2DLevelAttributesCollection`
              - Collection of Level Attributes.

            * - :pyclass:`~FigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :pyclass:`~FigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :pyclass:`~FigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :pyclass:`~FigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :pyclass:`~FigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :pyclass:`~FigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :pyclass:`~FigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :pyclass:`~FigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :pyclass:`~FigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :pyclass:`~FigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :pyclass:`~FigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :pyclass:`~VehicleProfileGPS`
              - GPS Attitude profile.

            * - :pyclass:`~StkObjectModelContext`
              - AgStkObjectModelContext class provides methods to create instance of AgStkObjectRoot class.

            * - :pyclass:`~StdMilitary2525bSymbols`
              - AgStdMil2525bSymbols class provides methods to create 2525b symbols.

            * - :pyclass:`~CoverageGridInspector`
              - AgCvGridInspector class provides methods to use the grid inspector tool for coverage definition.

            * - :pyclass:`~FigureOfMeritGridInspector`
              - AgFmGridInspector class provides methods to use the grid inspector tool for FOM.

            * - :pyclass:`~Graphics3DVaporTrail`
              - Vapor trail attributes.

            * - :pyclass:`~VehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :pyclass:`~AccessConstraintPluginMinMax`
              - Class related to defining access plugin constraints in terms of minimum and/or maximum values.

            * - :pyclass:`~ConstellationConstraints`
              - Class related to the constellation constraints.

            * - :pyclass:`~ConstellationConstraintObjectRestriction`
              - Class related to the constellation constraint restrictions.

            * - :pyclass:`~ConstellationConstraintRestriction`
              - Class related to the constellation constraint restrictions.

            * - :pyclass:`~Constellation`
              - Class represents the STK Constellation.

            * - :pyclass:`~ConstellationGraphics`
              - 2D Graphics properties of the STK Constellation.

            * - :pyclass:`~ConstellationRouting`
              - Routing properties of the STK Constellation.

            * - :pyclass:`~EventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :pyclass:`~EventDetectionSubSampling`
              - Event detection strategy involving subsampling.

            * - :pyclass:`~SamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :pyclass:`~SamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :pyclass:`~SensorAccessAdvanced`
              - Sensor's advanced targeting access computation properties.

            * - :pyclass:`~VehicleAccessAdvanced`
              - Vehicle advanced targeting access computation properties.

            * - :pyclass:`~AccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :pyclass:`~AccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :pyclass:`~SensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :pyclass:`~SensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :pyclass:`~SensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :pyclass:`~CentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :pyclass:`~CentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :pyclass:`~SatelliteExportTools`
              - The Satellite Export Tools.

            * - :pyclass:`~LaunchVehicleExportTools`
              - The LaunchVehicle Export Tools.

            * - :pyclass:`~GroundVehicleExportTools`
              - The GroundVehicle Export Tools.

            * - :pyclass:`~MissileExportTools`
              - The Missile Export Tools.

            * - :pyclass:`~AircraftExportTools`
              - The Aircraft Export Tools.

            * - :pyclass:`~ShipExportTools`
              - The Ship Export Tools.

            * - :pyclass:`~VehicleEphemerisCode500ExportTool`
              - AgVeEphemerisTypeCode500 Class.

            * - :pyclass:`~VehicleEphemerisCCSDSExportTool`
              - AgVeEphemerisTypeCCSDS Class.

            * - :pyclass:`~VehicleEphemerisStkExportTool`
              - AgVeEphemerisTypeSTK Class.

            * - :pyclass:`~VehicleEphemerisSpiceExportTool`
              - AgVeEphemerisTypeSpice Class.

            * - :pyclass:`~ExportToolTimePeriod`
              - Specify Time Period.

            * - :pyclass:`~VehicleAttitudeExportTool`
              - AgVeExternalFileAttitude Class.

            * - :pyclass:`~VehiclePropDefinitionExportTool`
              - AgVeExternalFileAttitude Class.

            * - :pyclass:`~VehicleCoordinateAxesCustom`
              - Custom.

            * - :pyclass:`~ExportToolStepSize`
              - AgStepSize Class.

            * - :pyclass:`~PctCmpltEventArgs`
              - Represents a structure used by the Percent Complete events.

            * - :pyclass:`~StkObjectChangedEventArgs`
              - Contains information about the changes in the object's state.

            * - :pyclass:`~VehicleEclipsingBodies`
              - Eclipsing bodies.

            * - :pyclass:`~LocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :pyclass:`~TimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :pyclass:`~TimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :pyclass:`~SpatialState`
              - Represents a position and an attitude of an object.

            * - :pyclass:`~VehicleSpatialInfo`
              - Represents a spatial information of the vehicle.

            * - :pyclass:`~OnePointAccess`
              - One Point Access.

            * - :pyclass:`~OnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :pyclass:`~OnePointAccessResult`
              - One Point Access Result.

            * - :pyclass:`~OnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :pyclass:`~OnePointAccessConstraint`
              - One Point Access Result.

            * - :pyclass:`~VehiclePropagatorRealtime`
              - Realtime propagator.

            * - :pyclass:`~VehicleRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :pyclass:`~VehicleRealtimeCartesianPoints`
              - AgVeRealtimeCartesianPoint Class.

            * - :pyclass:`~VehicleRealtimeLLAHPSPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :pyclass:`~VehicleRealtimeLLAPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :pyclass:`~VehicleRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :pyclass:`~SRPModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :pyclass:`~SRPModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :pyclass:`~SRPModelPlugin`
              - Plugin Light Reflection Model.

            * - :pyclass:`~SRPModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :pyclass:`~VehicleHPOPSRPModel`
              - SRP Model Base CoClass.

            * - :pyclass:`~VehicleHPOPDragModelSpherical`
              - Spherical Drag Pressure Model.

            * - :pyclass:`~VehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :pyclass:`~VehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :pyclass:`~VehicleHPOPDragModel`
              - HPOP Drag Model Base CoClass.

            * - :pyclass:`~ScenarioAnimationTimePeriod`
              - Configure the scenario's animation time.

            * - :pyclass:`~SensorProjectionConstantAltitude`
              - Class defining projection altitude options for constant altitude for a sensor.

            * - :pyclass:`~SensorProjectionObjectAltitude`
              - Class defining projection altitude options for object altitude for a sensor.

            * - :pyclass:`~VehicleAttitudeRealTimeDataReference`
              - Reference attitude profile for the incoming attitude data.

            * - :pyclass:`~MtoAnalysis`
              - MTO Spatial State Info.

            * - :pyclass:`~MtoAnalysisPosition`
              - MTO Position Computation.

            * - :pyclass:`~MtoAnalysisRange`
              - MTO Range Computation.

            * - :pyclass:`~MtoAnalysisFieldOfView`
              - MTO Field Of View Computation.

            * - :pyclass:`~MtoAnalysisVisibility`
              - MTO Visibility Computation.

            * - :pyclass:`~VehiclePropagatorGPS`
              - GPS propagator.

            * - :pyclass:`~AvailableFeatures`
              - Class is used to check the availability of the features such as Astrogator, etc.

            * - :pyclass:`~ScenarioBeforeSaveEventArgs`
              - Contains information about the changes in the object's state.

            * - :pyclass:`~StkObjectPreDeleteEventArgs`
              - Arguments for the OnStkObjectPreDelete event.

            * - :pyclass:`~VehiclePropagatorSGP4CommonTasks`
              - Most commonly used functionality when working with SGP4 propagator.

            * - :pyclass:`~VehicleSGP4AutoUpdateProperties`
              - SGP4 AutoUpdate properties.

            * - :pyclass:`~VehicleSGP4AutoUpdateFileSource`
              - Configure the SGP4 automatic updates using file(s).

            * - :pyclass:`~VehicleSGP4AutoUpdateOnlineSource`
              - Configure the SGP4 automatic updates using online source (AGI server).

            * - :pyclass:`~VehicleSGP4AutoUpdate`
              - SGP4 AutoUpdate.

            * - :pyclass:`~VehicleSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :pyclass:`~VehicleGPSAutoUpdateProperties`
              - GPS AutoUpdate properties.

            * - :pyclass:`~VehicleGPSAutoUpdateFileSource`
              - GPS automatic updates using almanac file(s).

            * - :pyclass:`~VehicleGPSAutoUpdateOnlineSource`
              - GPS automatic updates using online source (AGI server).

            * - :pyclass:`~VehicleGPSAutoUpdate`
              - GPS AutoUpdate.

            * - :pyclass:`~VehicleGPSSpecifyAlmanac`
              - Specify a GPS almanac.

            * - :pyclass:`~VehicleGPSAlmanacProperties`
              - A common base for GPS almanac properties.

            * - :pyclass:`~VehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :pyclass:`~VehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :pyclass:`~VehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :pyclass:`~VehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :pyclass:`~VehicleGPSElement`
              - An element of the GPS element collection.

            * - :pyclass:`~SpaceEnvironmentRadEnergyMethodSpecify`
              - Set the electron and proton energies to consider.

            * - :pyclass:`~SpaceEnvironmentRadEnergyValues`
              - Energy values used by the Radiation Environment model.

            * - :pyclass:`~SpaceEnvironmentRadiationEnvironment`
              - Radiation Environment model settings.

            * - :pyclass:`~SpaceEnvironmentMagnitudeFieldGraphics2D`
              - Geomagnetic field graphics settings.

            * - :pyclass:`~SpaceEnvironmentScenarioExtGraphics3D`
              - 3D Graphics settings.

            * - :pyclass:`~ScenSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :pyclass:`~VehicleSpaceEnvironmentRadDoseRateElement`
              - Class defining dose rate information computed for a shielding thickness.

            * - :pyclass:`~VehicleSpaceEnvironmentRadDoseRateCollection`
              - Collection of dose rate elements computed for a shielding thickness.

            * - :pyclass:`~SpaceEnvironmentSAAContour`
              - SAA settings.

            * - :pyclass:`~VehicleSpaceEnvironmentVehTemperature`
              - Vehicle Temperature settings.

            * - :pyclass:`~VehicleSpaceEnvironmentParticleFlux`
              - Particle Flux settings.

            * - :pyclass:`~VehicleSpaceEnvironmentMagneticField`
              - Magnetic field settings.

            * - :pyclass:`~VehicleSpaceEnvironmentRadiation`
              - Radiation model settings.

            * - :pyclass:`~VehicleSpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for displaying magnetic field lines.

            * - :pyclass:`~VehicleSpaceEnvironmentGraphics`
              - Graphics settings.

            * - :pyclass:`~VehicleSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :pyclass:`~CoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :pyclass:`~CoverageGridPointSelection`
              - Represents a set of points selected with the grid inspector.

            * - :pyclass:`~CelestialBodyCollection`
              - Represents a collection of stars.

            * - :pyclass:`~CelestialBodyInfo`
              - Represents a celestial body information.

            * - :pyclass:`~StkCentralBodyEllipsoid`
              - Central body's ellipsoid information.

            * - :pyclass:`~StkCentralBody`
              - A central body coclass.

            * - :pyclass:`~StkCentralBodyCollection`
              - Central body collection coclass.

            * - :pyclass:`~FigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :pyclass:`~FigureOfMeritDefinitionScalarCalculation`
              - Scalar Calculation Figure of Merit.

            * - :pyclass:`~VehiclePropagator11ParamDescriptor`
              - 11-Param file definition.

            * - :pyclass:`~VehiclePropagator11ParamDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :pyclass:`~VehiclePropagator11Param`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :pyclass:`~VehiclePropagatorSP3File`
              - SP3 file data.

            * - :pyclass:`~VehiclePropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :pyclass:`~VehiclePropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :pyclass:`~VehicleEphemerisStkBinaryExportTool`
              - AgVeEphemerisTypeSTKBinary Class.

            * - :pyclass:`~OrbitState`
              - Class defining orbit state.

            * - :pyclass:`~OrbitStateCoordinateSystem`
              - Selection of coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :pyclass:`~OrbitStateCartesian`
              - Cartesian coordinate type.

            * - :pyclass:`~ClassicalSizeShapeAltitude`
              - Orbit size and shape using altitude.

            * - :pyclass:`~ClassicalSizeShapeMeanMotion`
              - Orbit size and shape using Mean Motion and Eccentricity.

            * - :pyclass:`~ClassicalSizeShapePeriod`
              - Orbit size and shape using Period and Eccentricity.

            * - :pyclass:`~ClassicalSizeShapeRadius`
              - Orbit size and shape using Radius.

            * - :pyclass:`~ClassicalSizeShapeSemimajorAxis`
              - Orbit size and shape using Semimajor Axis and Eccentricity.

            * - :pyclass:`~OrientationAscNodeLAN`
              - Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :pyclass:`~OrientationAscNodeRAAN`
              - Angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :pyclass:`~ClassicalOrientation`
              - Orbit orientation in the Classical (Keplerian) system.

            * - :pyclass:`~ClassicalLocationArgumentOfLatitude`
              - Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~ClassicalLocationEccentricAnomaly`
              - Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~ClassicalLocationMeanAnomaly`
              - Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~ClassicalLocationTimePastAN`
              - Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~ClassicalLocationTimePastPerigee`
              - Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~ClassicalLocationTrueAnomaly`
              - True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~OrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :pyclass:`~GeodeticSizeAltitude`
              - Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :pyclass:`~GeodeticSizeRadius`
              - Radius and Radius Rate (for Geodetic coordinate type).

            * - :pyclass:`~OrbitStateGeodetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :pyclass:`~DelaunayL`
              - Delaunay Variable L, which is related to the two-body orbital energy.

            * - :pyclass:`~DelaunayLOverSQRTmu`
              - Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :pyclass:`~DelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :pyclass:`~DelaunayHOverSQRTmu`
              - Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :pyclass:`~DelaunayG`
              - Delaunay Variable G, the magnitude of the orbital angular momentum.

            * - :pyclass:`~DelaunayGOverSQRTmu`
              - Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :pyclass:`~OrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :pyclass:`~EquinoctialSizeShapeMeanMotion`
              - Mean Motion, an element of the Equinoctial coordinate type.

            * - :pyclass:`~EquinoctialSizeShapeSemimajorAxis`
              - Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :pyclass:`~OrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :pyclass:`~MixedSphericalFPAHorizontal`
              - Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :pyclass:`~MixedSphericalFPAVertical`
              - Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :pyclass:`~OrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :pyclass:`~SphericalFPAHorizontal`
              - Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :pyclass:`~SphericalFPAVertical`
              - Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :pyclass:`~OrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :pyclass:`~VehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :pyclass:`~VehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :pyclass:`~VehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :pyclass:`~VehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :pyclass:`~StkPreferences`
              - Allow configuring STK preferences.

            * - :pyclass:`~StkPreferencesVDF`
              - Allow configuring VDF preferences.

            * - :pyclass:`~VehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :pyclass:`~VehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :pyclass:`~VehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :pyclass:`~VehicleAttitudeSlewFixedRate`
              - Fixed rate slew.

            * - :pyclass:`~VehicleAttitudeSlewFixedTime`
              - Fixed time slew.

            * - :pyclass:`~VehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :pyclass:`~MtoGraphics3DModelArtic`
              - Class defining MTO model articulations.

            * - :pyclass:`~VehiclePropagatorAviator`
              - Class defining the Mission Modler propagator for an Aircraft.

            * - :pyclass:`~VehicleEphemerisCCSDSv2ExportTool`
              - The Ephemeris/Attitude Export Tool for CCSDSv2 Ephemeris type.

            * - :pyclass:`~StkPreferencesConnect`
              - Allow configuring connect preferences.

            * - :pyclass:`~Antenna`
              - Class defining the antenna object.

            * - :pyclass:`~AntennaModel`
              - Class defining a generic antenna model.

            * - :pyclass:`~AntennaModelOpticalSimple`
              - Class defining a simple optical antenna model.

            * - :pyclass:`~AntennaModelOpticalGaussian`
              - Class defining a gaussian optical antenna model.

            * - :pyclass:`~AntennaModelGaussian`
              - Class defining a gaussian antenna model.

            * - :pyclass:`~AntennaModelParabolic`
              - Class defining a parabolic antenna model.

            * - :pyclass:`~AntennaModelSquareHorn`
              - Class defining a square horn antenna model.

            * - :pyclass:`~AntennaModelScriptPlugin`
              - Class defining a script plguin antenna model.

            * - :pyclass:`~AntennaModelExternal`
              - Class defining a external antenna model.

            * - :pyclass:`~AntennaModelGimroc`
              - Class defining a GIMROC antenna model.

            * - :pyclass:`~AntennaModelRemcomUanFormat`
              - Class defining an antenna pattern Remcom uan model.

            * - :pyclass:`~AntennaModelANSYSffdFormat`
              - Class defining an antenna pattern ANSYS ffd model.

            * - :pyclass:`~AntennaModelTicraGRASPFormat`
              - Class defining an antenna pattern Ticra GRASP model.

            * - :pyclass:`~AntennaModelElevationAzimuthCuts`
              - Class defining a pattern elevation/azimuth cuts antenna model.

            * - :pyclass:`~AntennaModelIeee1979`
              - Class defining a IEEE 1979 antenna model.

            * - :pyclass:`~AntennaModelDipole`
              - Class defining a dipole antenna model.

            * - :pyclass:`~AntennaModelHelix`
              - Class defining a helix antenna model.

            * - :pyclass:`~AntennaModelCosecantSquared`
              - Class defining a cosecant squared antenna model.

            * - :pyclass:`~AntennaModelHemispherical`
              - Class defining a hemispherical antenna model.

            * - :pyclass:`~AntennaModelPencilBeam`
              - Class defining a pencil beam antenna model.

            * - :pyclass:`~AntennaModelPhasedArray`
              - Class defining a phased array antenna model.

            * - :pyclass:`~AntennaModelHfssEepArray`
              - Class defining an HFSS EEP array antenna model.

            * - :pyclass:`~AntennaModelIsotropic`
              - Class defining a isotropic antenna model.

            * - :pyclass:`~AntennaModelIntelSat`
              - Class defining a IntelSat antenna model.

            * - :pyclass:`~AntennaModelGpsGlobal`
              - Class defining a GPS global antenna model.

            * - :pyclass:`~AntennaModelGpsFrpa`
              - Class defining a GPS FRPA antenna model.

            * - :pyclass:`~AntennaModelItuBO1213CoPolar`
              - Class defining a ITU-R BO1213 co-polar antenna model.

            * - :pyclass:`~AntennaModelItuBO1213CrossPolar`
              - Class defining a ITU-R BO1213 cross-polar antenna model.

            * - :pyclass:`~AntennaModelItuF1245`
              - Class defining a ITU-R F1245-3 antenna model.

            * - :pyclass:`~AntennaModelItuS580`
              - Class defining a ITU-R S580-6 antenna model.

            * - :pyclass:`~AntennaModelItuS465`
              - Class defining a ITU-R S465-6 antenna model.

            * - :pyclass:`~AntennaModelItuS731`
              - Class defining a ITU-R S731 antenna model.

            * - :pyclass:`~AntennaModelItuS1528R12Circular`
              - Class defining a ITU-R S1528 1.2 circular antenna model.

            * - :pyclass:`~AntennaModelItuS1528R13`
              - Class defining a ITU-R S1528 1.3 antenna model.

            * - :pyclass:`~AntennaModelItuS672Circular`
              - Class defining a ITU-R S672 circular antenna model.

            * - :pyclass:`~AntennaModelItuS1528R12Rectangular`
              - Class defining a ITU-R S1528 1.2 rectangular antenna model.

            * - :pyclass:`~AntennaModelItuS672Rectangular`
              - Class defining a ITU-R S672-4 rectangular antenna model.

            * - :pyclass:`~AntennaModelApertureCircularCosine`
              - Class defining a circular cosine aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularUniform`
              - Class defining a circular uniform aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularCosineSquared`
              - Class defining a circular cosine squared aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularBessel`
              - Class defining a circular bessel aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularBesselEnvelope`
              - Class defining a circular bessel envelope aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularCosinePedestal`
              - Class defining a circular cosine pedestal aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularCosineSquaredPedestal`
              - Class defining a circular cosine squared pedestal aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularSincIntPower`
              - Class defining a circular sinc integer power aperture antenna model.

            * - :pyclass:`~AntennaModelApertureCircularSincRealPower`
              - Class defining a circular sinc real power aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularCosine`
              - Class defining a rectangular cosine aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularCosinePedestal`
              - Class defining a rectangular cosine pedestal aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularCosineSquaredPedestal`
              - Class defining a rectangular cosine squared pedestal aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularSincIntPower`
              - Class defining a rectangular sinc integer power aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularSincRealPower`
              - Class defining a rectangular sinc real power aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularCosineSquared`
              - Class defining a rectangular cosine squared aperture antenna model.

            * - :pyclass:`~AntennaModelApertureRectangularUniform`
              - Class defining a rectangular uniform aperture antenna model.

            * - :pyclass:`~AntennaModelRectangularPattern`
              - Class defining a rectangular pattern antenna model.

            * - :pyclass:`~AntennaControl`
              - Class defining the properties for a antenna control.

            * - :pyclass:`~AntennaGraphics3D`
              - Class defining 3D Graphics properties of a Antenna.

            * - :pyclass:`~RadarCrossSectionVolumeGraphics`
              - Class defining 3D Volume Graphics properties of radar cross section.

            * - :pyclass:`~RadarCrossSectionGraphics3D`
              - Class defining 3D Graphics properties of radar cross section.

            * - :pyclass:`~RadarCrossSectionGraphics`
              - Class defining graphics properties of radar cross section.

            * - :pyclass:`~AntennaVolumeGraphics`
              - Class defining 3D Volume Graphics properties of a Antenna.

            * - :pyclass:`~AntennaContourGraphics`
              - Class defining contour Graphics properties of a Antenna.

            * - :pyclass:`~AntennaGraphics`
              - Class defining 2D Graphics properties of a Antenna.

            * - :pyclass:`~RadarCrossSectionContourLevelCollection`
              - Class defining a collection of radar cross section contour levels.

            * - :pyclass:`~RadarCrossSectionContourLevel`
              - Class defining an radar cross section contour level.

            * - :pyclass:`~RadarCrossSectionVolumeLevelCollection`
              - Class defining a collection of radar cross section volume levels.

            * - :pyclass:`~RadarCrossSectionVolumeLevel`
              - Class defining an radar cross section volume level.

            * - :pyclass:`~AntennaVolumeLevelCollection`
              - Class defining a collection of antenna volume levels.

            * - :pyclass:`~AntennaVolumeLevel`
              - Class defining an antenna volume level.

            * - :pyclass:`~AntennaContourLevelCollection`
              - Class defining a collection of antenna contour levels.

            * - :pyclass:`~AntennaContourLevel`
              - Class defining an antenna contour level.

            * - :pyclass:`~AntennaContourGain`
              - Class defining an antenna gain contour properties.

            * - :pyclass:`~AntennaContourEirp`
              - Class defining an antenna eirp contour properties.

            * - :pyclass:`~AntennaContourRip`
              - Class defining an antenna rip contour properties.

            * - :pyclass:`~AntennaContourFluxDensity`
              - Class defining an antenna flux density contour properties.

            * - :pyclass:`~AntennaContourSpectralFluxDensity`
              - Class defining an antenna spectral flux density contour properties.

            * - :pyclass:`~Transmitter`
              - Class defining the transmitter object.

            * - :pyclass:`~TransmitterModel`
              - Class defining a generic transmitter model.

            * - :pyclass:`~TransmitterModelScriptPluginRF`
              - Class defining a RF script plugin transmitter model.

            * - :pyclass:`~TransmitterModelScriptPluginLaser`
              - Class defining a laser script plugin transmitter model.

            * - :pyclass:`~TransmitterModelCable`
              - Class defining a cable transmitter model.

            * - :pyclass:`~TransmitterModelSimple`
              - Class defining a simple transmitter model.

            * - :pyclass:`~TransmitterModelMedium`
              - Class defining a medium transmitter model.

            * - :pyclass:`~TransmitterModelComplex`
              - Class defining a complex transmitter model.

            * - :pyclass:`~TransmitterModelMultibeam`
              - Class defining a multibeam transmitter model.

            * - :pyclass:`~TransmitterModelLaser`
              - Class defining a laser transmitter model.

            * - :pyclass:`~ReTransmitterModelSimple`
              - Class defining a simple re-transmitter model.

            * - :pyclass:`~ReTransmitterModelMedium`
              - Class defining a medium re-transmitter model.

            * - :pyclass:`~ReTransmitterModelComplex`
              - Class defining a complex re-transmitter model.

            * - :pyclass:`~TransmitterGraphics3D`
              - Class defining 3D Graphics properties of a Transmitter.

            * - :pyclass:`~TransmitterGraphics`
              - Class defining 2D Graphics properties of a Transmitter.

            * - :pyclass:`~Receiver`
              - Class defining the receiver object.

            * - :pyclass:`~ReceiverModel`
              - Class defining a generic receiver model.

            * - :pyclass:`~ReceiverModelCable`
              - Class defining a cable receiver model.

            * - :pyclass:`~ReceiverModelSimple`
              - Class defining a simple receiver model.

            * - :pyclass:`~ReceiverModelMedium`
              - Class defining a medium receiver model.

            * - :pyclass:`~ReceiverModelComplex`
              - Class defining a complex receiver model.

            * - :pyclass:`~ReceiverModelMultibeam`
              - Class defining a mutibeam receiver model.

            * - :pyclass:`~ReceiverModelLaser`
              - Class defining a laser receiver model.

            * - :pyclass:`~ReceiverModelScriptPluginRF`
              - Class defining a RF script plugin receiver model.

            * - :pyclass:`~ReceiverModelScriptPluginLaser`
              - Class defining a laser script plugin receiver model.

            * - :pyclass:`~ReceiverGraphics3D`
              - Class defining 3D Graphics properties of a Receiver.

            * - :pyclass:`~ReceiverGraphics`
              - Class defining 2D Graphics properties of a Receiver.

            * - :pyclass:`~RadarDopplerClutterFilters`
              - Class defining the properties for doppler clutter filters.

            * - :pyclass:`~Waveform`
              - Class defining a waveform.

            * - :pyclass:`~WaveformRectangular`
              - Class defining a rectangular waveform.

            * - :pyclass:`~WaveformPulseDefinition`
              - Class defining the pulse definition for a rectangular waveform.

            * - :pyclass:`~RadarMultifunctionWaveformStrategySettings`
              - Class defining the waveform selection strategy settings.

            * - :pyclass:`~WaveformSelectionStrategy`
              - Class defining the waveform selection strategy.

            * - :pyclass:`~WaveformSelectionStrategyFixed`
              - Class defining the waveform selection strategy.

            * - :pyclass:`~WaveformSelectionStrategyRangeLimits`
              - Class defining the range limits waveform selection strategy.

            * - :pyclass:`~Radar`
              - Class defining the radar object.

            * - :pyclass:`~RadarModel`
              - Class defining a generic radar model.

            * - :pyclass:`~RadarModelMonostatic`
              - Class defining a monostatic radar model.

            * - :pyclass:`~RadarModelMultifunction`
              - Class defining a multifunction radar model.

            * - :pyclass:`~RadarModelBistaticTransmitter`
              - Class defining a bistatic transmitter radar model.

            * - :pyclass:`~RadarModelBistaticReceiver`
              - Class defining a bistatic receiver radar model.

            * - :pyclass:`~RadarGraphics3D`
              - Class defining 3D Graphics properties of a Radar.

            * - :pyclass:`~RadarGraphics`
              - Class defining 2D Graphics properties of a Radar.

            * - :pyclass:`~RadarAccessGraphics`
              - Class defining access graphics properties of a Radar.

            * - :pyclass:`~RadarMultipathGraphics`
              - Class defining multipath graphics properties of a Radar.

            * - :pyclass:`~RadarModeMonostatic`
              - Class defining a monostatic radar mode.

            * - :pyclass:`~RadarModeMonostaticSearchTrack`
              - Class defining a monostatic search/track radar mode.

            * - :pyclass:`~RadarModeMonostaticSar`
              - Class defining a monostatic sar radar mode.

            * - :pyclass:`~RadarModeBistaticTransmitter`
              - Class defining a bistatic transmitter radar mode.

            * - :pyclass:`~RadarModeBistaticTransmitterSearchTrack`
              - Class defining a bistatic transmitter search/track radar mode.

            * - :pyclass:`~RadarModeBistaticTransmitterSar`
              - Class defining a bistatic transmitter sar radar mode.

            * - :pyclass:`~RadarModeBistaticReceiver`
              - Class defining a bistatic receiver radar mode.

            * - :pyclass:`~RadarModeBistaticReceiverSearchTrack`
              - Class defining a bistatic receiver search/track radar mode.

            * - :pyclass:`~RadarModeBistaticReceiverSar`
              - Class defining a bistatic receiver sar radar mode.

            * - :pyclass:`~RadarWaveformMonostaticSearchTrackContinuous`
              - Class defining a monostatic continuous waveform.

            * - :pyclass:`~RadarWaveformMonostaticSearchTrackFixedPRF`
              - Class defining a monostatic fixed PRF waveform.

            * - :pyclass:`~RadarMultifunctionDetectionProcessing`
              - Class defining multifunction radar detection processing.

            * - :pyclass:`~RadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Class defining a bistatic transmitter continuous waveform.

            * - :pyclass:`~RadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Class defining a bistatic transmitter fixed PRF waveform.

            * - :pyclass:`~RadarWaveformBistaticReceiverSearchTrackContinuous`
              - Class defining a bistatic receiver continuous waveform.

            * - :pyclass:`~RadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Class defining a bistatic receiver fixed PRF waveform.

            * - :pyclass:`~RadarWaveformSearchTrackPulseDefinition`
              - Class defining the pulse definition for a search track waveform.

            * - :pyclass:`~RadarModulator`
              - Class defining a radar modulator.

            * - :pyclass:`~RadarProbabilityOfDetection`
              - Class defining the probability of detection.

            * - :pyclass:`~RadarProbabilityOfDetectionCFAR`
              - Class defining the probability of detection cfar.

            * - :pyclass:`~RadarProbabilityOfDetectionNonCFAR`
              - Class defining the non CFAR probability of detection cfar.

            * - :pyclass:`~RadarProbabilityOfDetectionPlugin`
              - Class defining the probability of detection plugin.

            * - :pyclass:`~RadarProbabilityOfDetectionCFARCellAveraging`
              - Class defining the probability of detection cell averaging cfar.

            * - :pyclass:`~RadarProbabilityOfDetectionCFAROrderedStatistics`
              - Class defining the probability of detection ordered statistics cfar.

            * - :pyclass:`~RadarPulseIntegrationGoalSNR`
              - Class defining the goal SNR integration method.

            * - :pyclass:`~RadarPulseIntegrationFixedNumberOfPulses`
              - Class defining the fixed number of pulses integration method.

            * - :pyclass:`~RadarContinuousWaveAnalysisModeGoalSNR`
              - Class defining the continuous wave goal SNR analysis mode.

            * - :pyclass:`~RadarContinuousWaveAnalysisModeFixedTime`
              - Class defining the continuous wave fixed time analysis mode.

            * - :pyclass:`~RadarWaveformSarPulseDefinition`
              - Class defining the pulse definition for a SAR waveform.

            * - :pyclass:`~RadarWaveformSarPulseIntegration`
              - Class defining the pulse integration for a SAR waveform.

            * - :pyclass:`~RadarTransmitter`
              - Class defining the radar transmitter.

            * - :pyclass:`~RadarTransmitterMultifunction`
              - Class defining the multifunction radar transmitter.

            * - :pyclass:`~RadarReceiver`
              - Class defining the radar transmitter.

            * - :pyclass:`~AdditionalGainLoss`
              - Class defining additional gains and losses.

            * - :pyclass:`~AdditionalGainLossCollection`
              - Class defining a collection of additional gains and losses.

            * - :pyclass:`~Polarization`
              - Class defining an polarization.

            * - :pyclass:`~PolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :pyclass:`~ReceivePolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :pyclass:`~PolarizationLHC`
              - Class defining a LHC polarization.

            * - :pyclass:`~PolarizationRHC`
              - Class defining a RHC polarization.

            * - :pyclass:`~ReceivePolarizationLHC`
              - Class defining a LHC polarization.

            * - :pyclass:`~ReceivePolarizationRHC`
              - Class defining a RHC polarization.

            * - :pyclass:`~PolarizationLinear`
              - Class defining a linear polarization.

            * - :pyclass:`~ReceivePolarizationLinear`
              - Class defining a linear polarization.

            * - :pyclass:`~PolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :pyclass:`~ReceivePolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :pyclass:`~PolarizationVertical`
              - Class defining a vertical polarization.

            * - :pyclass:`~ReceivePolarizationVertical`
              - Class defining a receive vertical polarization.

            * - :pyclass:`~RadarClutter`
              - Class defining a radar clutter.

            * - :pyclass:`~RadarClutterGeometry`
              - Class defining a radar clutter geometry.

            * - :pyclass:`~ScatteringPointProviderCollectionElement`
              - Class defining a scattering point provider collection element.

            * - :pyclass:`~ScatteringPointProviderCollection`
              - Class defining an scattering point provider collection.

            * - :pyclass:`~ScatteringPointProviderList`
              - Class defining a scattering point provider list.

            * - :pyclass:`~ScatteringPointProvider`
              - Class defining a scattering point provider.

            * - :pyclass:`~ScatteringPointProviderSinglePoint`
              - Class defining a single point scattring point provider.

            * - :pyclass:`~ScatteringPointCollectionElement`
              - Class defining a scattering point collection element.

            * - :pyclass:`~ScatteringPointCollection`
              - Class defining a collection of scattering points.

            * - :pyclass:`~ScatteringPointProviderPointsFile`
              - Class defining a scattring point provider where the points are defined in an ascii text file.

            * - :pyclass:`~ScatteringPointProviderRangeOverCFARCells`
              - Class defining a range over CFAR cells scattering point provider.

            * - :pyclass:`~ScatteringPointProviderSmoothOblateEarth`
              - Class defining a smooth oblate earth scattering point provider.

            * - :pyclass:`~ScatteringPointProviderPlugin`
              - Class defining a plugin scattering point provider.

            * - :pyclass:`~CRPluginConfiguration`
              - Class defining plugin configuration.

            * - :pyclass:`~RadarJamming`
              - Class defining radar jamming.

            * - :pyclass:`~RFInterference`
              - Class defining radar jamming.

            * - :pyclass:`~RFFilterModel`
              - Class defining a generic RF filter model.

            * - :pyclass:`~RFFilterModelBessel`
              - Class defining a bessel filter model.

            * - :pyclass:`~RFFilterModelSincEnvSinc`
              - Class defining a Sinc Envelope Sinc filter model.

            * - :pyclass:`~RFFilterModelElliptic`
              - Class defining a elliptic filter model.

            * - :pyclass:`~RFFilterModelChebyshev`
              - Class defining a Chebyshev filter model.

            * - :pyclass:`~RFFilterModelCosineWindow`
              - Class defining a cosine window filter model.

            * - :pyclass:`~RFFilterModelGaussianWindow`
              - Class defining a cosine window filter model.

            * - :pyclass:`~RFFilterModelHammingWindow`
              - Class defining a cosine window filter model.

            * - :pyclass:`~RFFilterModelButterworth`
              - Class defining a butterworth filter model.

            * - :pyclass:`~RFFilterModelExternal`
              - Class defining a external filter model.

            * - :pyclass:`~RFFilterModelScriptPlugin`
              - Class defining a script plugin filter model.

            * - :pyclass:`~RFFilterModelSinc`
              - Class defining a sinc filter model.

            * - :pyclass:`~RFFilterModelRaisedCosine`
              - Class defining a raised cosine filter model.

            * - :pyclass:`~RFFilterModelRootRaisedCosine`
              - Class defining a root raised cosine filter model.

            * - :pyclass:`~RFFilterModelRcLowPass`
              - Class defining a rc low pass filter model.

            * - :pyclass:`~RFFilterModelRectangular`
              - Class defining a rectangular filter model.

            * - :pyclass:`~RFFilterModelFirBoxCar`
              - Class defining a FIR box car filter model.

            * - :pyclass:`~RFFilterModelIir`
              - Class defining a IIR box car filter model.

            * - :pyclass:`~RFFilterModelFir`
              - Class defining a FIR filter model.

            * - :pyclass:`~SystemNoiseTemperature`
              - Class defining system noise temperature.

            * - :pyclass:`~AntennaNoiseTemperature`
              - Class defining antenna noise temperature.

            * - :pyclass:`~Atmosphere`
              - Class defining local atmosphere.

            * - :pyclass:`~LaserPropagationLossModels`
              - Class defining the properties for laser propagatoin models.

            * - :pyclass:`~LaserAtmosphericLossModel`
              - Class defining an laser propagation loss model.

            * - :pyclass:`~LaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Class defining an laser propagation loss model.

            * - :pyclass:`~ModtranLookupTablePropagationModel`
              - Class defining an MODTRAN-based lookup table propagation model.

            * - :pyclass:`~ModtranPropagationModel`
              - Class defining a MODTRAN propagation model.

            * - :pyclass:`~LaserTroposphericScintillationLossModel`
              - Class defining an laser tropospheric scintillation loss model.

            * - :pyclass:`~AtmosphericTurbulenceModel`
              - Class defining a atmospheric turbulence model.

            * - :pyclass:`~AtmosphericTurbulenceModelConstant`
              - Class defining a constant atmospheric turbulence model.

            * - :pyclass:`~AtmosphericTurbulenceModelHufnagelValley`
              - Class defining a Hufnagel Valley atmospheric turbulence model.

            * - :pyclass:`~LaserTroposphericScintillationLossModelITURP1814`
              - Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

            * - :pyclass:`~AtmosphericAbsorptionModel`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelITURP676_9`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelVoacap`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelTirem320`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelTirem331`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelTirem550`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelSimpleSatcom`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelScriptPlugin`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~AtmosphericAbsorptionModelCOMPlugin`
              - Class defining an atmospheric absorption model.

            * - :pyclass:`~ScatteringPointModel`
              - Class defining a scattering point model.

            * - :pyclass:`~ScatteringPointModelPlugin`
              - Class defining a plugin scattering point model.

            * - :pyclass:`~ScatteringPointModelConstantCoefficient`
              - Class defining a constant coefficient scattering point model.

            * - :pyclass:`~ScatteringPointModelWindTurbine`
              - Class defining a wind turbine scattering point model.

            * - :pyclass:`~RadarCrossSection`
              - Class defining a radar cross section.

            * - :pyclass:`~RadarCrossSectionModel`
              - Class defining a radar cross section model.

            * - :pyclass:`~RadarCrossSectionInheritable`
              - Class defining a inheritable radar cross section.

            * - :pyclass:`~RadarCrossSectionFrequencyBand`
              - Class defining a inheritable radar cross section frequency band.

            * - :pyclass:`~RadarCrossSectionFrequencyBandCollection`
              - Class defining a inheritable radar cross section frequency band collection.

            * - :pyclass:`~RadarCrossSectionComputeStrategy`
              - Class defining a inheritable radar cross section compute strategy.

            * - :pyclass:`~RadarCrossSectionComputeStrategyConstantValue`
              - Class defining a inheritable radar cross section compute strategy.

            * - :pyclass:`~RadarCrossSectionComputeStrategyScriptPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :pyclass:`~RadarCrossSectionComputeStrategyExternalFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :pyclass:`~RadarCrossSectionComputeStrategyAnsysCsvFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :pyclass:`~RadarCrossSectionComputeStrategyPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :pyclass:`~CustomPropagationModel`
              - Class defining a custom propatation model.

            * - :pyclass:`~PropagationChannel`
              - Class defining the propagation channel.

            * - :pyclass:`~RFEnvironment`
              - Class defining the RF environment.

            * - :pyclass:`~LaserEnvironment`
              - Class defining the laser environment for an object.

            * - :pyclass:`~ObjectRFEnvironment`
              - Class defining the RF environment for an object.

            * - :pyclass:`~ObjectLaserEnvironment`
              - Class defining the laser environment for an object.

            * - :pyclass:`~PlatformLaserEnvironment`
              - Class defining the laser environment for an platform.

            * - :pyclass:`~RainLossModel`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelITURP618_12`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelITURP618_13`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelITURP618_10`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelCrane1985`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelCrane1982`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelCCIR1983`
              - Class defining a rain loss model.

            * - :pyclass:`~RainLossModelScriptPlugin`
              - Class defining a rain loss model.

            * - :pyclass:`~CloudsAndFogFadingLossModel`
              - Class defining a clouds and fog fading loss model.

            * - :pyclass:`~CloudsAndFogFadingLossModelP840_6`
              - Class defining a clouds and fog Loss ITU-R P.840-6 model.

            * - :pyclass:`~CloudsAndFogFadingLossModelP840_7`
              - Class defining a clouds and fog Loss ITU-R P.840-7 model.

            * - :pyclass:`~TroposphericScintillationFadingLossModel`
              - Class defining a tropospheric scintillation fading loss model.

            * - :pyclass:`~TroposphericScintillationFadingLossModelP618_8`
              - Class defining a tropospheric scintillation fading loss P.618-8 model.

            * - :pyclass:`~TroposphericScintillationFadingLossModelP618_12`
              - Class defining a tropospheric scintillation fading loss P.618-12 model.

            * - :pyclass:`~IonosphericFadingLossModel`
              - Class defining a Ionospheric fading loss model.

            * - :pyclass:`~IonosphericFadingLossModelP531_13`
              - Class defining a Ionospheric fading loss P.531-13 model.

            * - :pyclass:`~UrbanTerrestrialLossModel`
              - Class defining an urban/terrestrial loss model.

            * - :pyclass:`~UrbanTerrestrialLossModelTwoRay`
              - Class defining an urban/terrestrial loss model.

            * - :pyclass:`~UrbanTerrestrialLossModelWirelessInSite64`
              - Class defining an urban/terrestrial loss model.

            * - :pyclass:`~WirelessInSite64GeometryData`
              - Class defining the REMCOM Wireless InSite 64 geometry data.

            * - :pyclass:`~PointingStrategy`
              - Class defining a pointing strategy.

            * - :pyclass:`~PointingStrategyFixed`
              - Class defining a fixed pointing strategy.

            * - :pyclass:`~PointingStrategySpinning`
              - Class defining a spinning pointing strategy.

            * - :pyclass:`~PointingStrategyTargeted`
              - Class defining a targeted pointing strategy.

            * - :pyclass:`~CRLocation`
              - Class defining a location.

            * - :pyclass:`~CRComplex`
              - Class defining a complex number.

            * - :pyclass:`~CRComplexCollection`
              - Class defining a collection of complex numbers.

            * - :pyclass:`~ModulatorModel`
              - Class defining a modulator model.

            * - :pyclass:`~ModulatorModelBpsk`
              - Class defining a BPSK modulator model.

            * - :pyclass:`~ModulatorModelQpsk`
              - Class defining a QPSK modulator model.

            * - :pyclass:`~ModulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :pyclass:`~ModulatorModelExternal`
              - Class defining a external modulator model.

            * - :pyclass:`~ModulatorModelQam16`
              - Class defining a QAM 16 modulator model.

            * - :pyclass:`~ModulatorModelQam32`
              - Class defining a QAM 32 modulator model.

            * - :pyclass:`~ModulatorModelQam64`
              - Class defining a QAM 64 modulator model.

            * - :pyclass:`~ModulatorModelQam128`
              - Class defining a QAM 128 modulator model.

            * - :pyclass:`~ModulatorModelQam256`
              - Class defining a QAM 256 modulator model.

            * - :pyclass:`~ModulatorModelQam1024`
              - Class defining a QAM 1024 modulator model.

            * - :pyclass:`~ModulatorModel8psk`
              - Class defining a 8PSK modulator model.

            * - :pyclass:`~ModulatorModel16psk`
              - Class defining a 16PSK modulator model.

            * - :pyclass:`~ModulatorModelMsk`
              - Class defining a MSK modulator model.

            * - :pyclass:`~ModulatorModelBoc`
              - Class defining a BOC modulator model.

            * - :pyclass:`~ModulatorModelDpsk`
              - Class defining a DPSK modulator model.

            * - :pyclass:`~ModulatorModelFsk`
              - Class defining a FSK modulator model.

            * - :pyclass:`~ModulatorModelNfsk`
              - Class defining a NFSK modulator model.

            * - :pyclass:`~ModulatorModelOqpsk`
              - Class defining a OQPSK modulator model.

            * - :pyclass:`~ModulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :pyclass:`~ModulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :pyclass:`~ModulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :pyclass:`~ModulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :pyclass:`~ModulatorModelScriptPluginCustomPsd`
              - Class defining a custom PSD script plugin modulator model.

            * - :pyclass:`~ModulatorModelScriptPluginIdealPsd`
              - Class defining a ideal PSD script plugin modulator model.

            * - :pyclass:`~LinkMargin`
              - Class defining a link margin computation object.

            * - :pyclass:`~DemodulatorModel`
              - Class defining a demodulator model.

            * - :pyclass:`~DemodulatorModelBpsk`
              - Class defining a BPSK modulator model.

            * - :pyclass:`~DemodulatorModelQpsk`
              - Class defining a QPSK modulator model.

            * - :pyclass:`~DemodulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :pyclass:`~DemodulatorModelExternal`
              - Class defining a external modulator model.

            * - :pyclass:`~DemodulatorModelQam16`
              - Class defining a QAM 16 modulator model.

            * - :pyclass:`~DemodulatorModelQam32`
              - Class defining a QAM 32 modulator model.

            * - :pyclass:`~DemodulatorModelQam64`
              - Class defining a QAM 64 modulator model.

            * - :pyclass:`~DemodulatorModelQam128`
              - Class defining a QAM 128 modulator model.

            * - :pyclass:`~DemodulatorModelQam256`
              - Class defining a QAM 256 modulator model.

            * - :pyclass:`~DemodulatorModelQam1024`
              - Class defining a QAM 1024 modulator model.

            * - :pyclass:`~DemodulatorModel8psk`
              - Class defining a 8PSK modulator model.

            * - :pyclass:`~DemodulatorModel16psk`
              - Class defining a 16PSK modulator model.

            * - :pyclass:`~DemodulatorModelMsk`
              - Class defining a MSK modulator model.

            * - :pyclass:`~DemodulatorModelBoc`
              - Class defining a BOC modulator model.

            * - :pyclass:`~DemodulatorModelDpsk`
              - Class defining a DPSK modulator model.

            * - :pyclass:`~DemodulatorModelFsk`
              - Class defining a FSK modulator model.

            * - :pyclass:`~DemodulatorModelNfsk`
              - Class defining a NFSK modulator model.

            * - :pyclass:`~DemodulatorModelOqpsk`
              - Class defining a OQPSK modulator model.

            * - :pyclass:`~DemodulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :pyclass:`~DemodulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :pyclass:`~DemodulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :pyclass:`~DemodulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :pyclass:`~DemodulatorModelScriptPlugin`
              - Class defining a script plugin modulator model.

            * - :pyclass:`~TransferFunctionPolynomialCollection`
              - Class defining a collection of polynomial coefficients.

            * - :pyclass:`~TransferFunctionInputBackOffCOverImTableRow`
              - Class defining a row of an input back off vs C/Im table.

            * - :pyclass:`~TransferFunctionInputBackOffCOverImTable`
              - Class defining an input back off vs C/Im table.

            * - :pyclass:`~TransferFunctionInputBackOffOutputBackOffTableRow`
              - Class defining a row of an input back off vs output back off table.

            * - :pyclass:`~TransferFunctionInputBackOffOutputBackOffTable`
              - Class defining an input back off vs output back off table.

            * - :pyclass:`~BeerBouguerLambertLawLayer`
              - Class defining a row of an input back off vs output back off table.

            * - :pyclass:`~BeerBouguerLambertLawLayerCollection`
              - Class defining collection of Beer-Bouguer-Lamber Law atmosphere layers.

            * - :pyclass:`~RadarActivity`
              - Class defining radar activity.

            * - :pyclass:`~RadarActivityAlwaysActive`
              - Class defining radar always active activity.

            * - :pyclass:`~RadarActivityAlwaysInactive`
              - Class defining radar always active inactivity.

            * - :pyclass:`~RadarActivityTimeComponentListElement`
              - Class defining an element of the time components activity list.

            * - :pyclass:`~RadarActivityTimeComponentListCollection`
              - Class defining an radar antenna beam collection.

            * - :pyclass:`~RadarActivityTimeComponentList`
              - Class defining a radar time component list activity.

            * - :pyclass:`~RadarActivityTimeIntervalListElement`
              - Class defining an element of the time components activity list.

            * - :pyclass:`~RadarActivityTimeIntervalListCollection`
              - Class defining an radar antenna beam collection.

            * - :pyclass:`~RadarActivityTimeIntervalList`
              - Class defining a radar time component list activity.

            * - :pyclass:`~RadarAntennaBeam`
              - Class defining a radar antenna beam.

            * - :pyclass:`~RadarAntennaBeamCollection`
              - Class defining an radar antenna beam collection.

            * - :pyclass:`~AntennaSystem`
              - Class defining an antenna system.

            * - :pyclass:`~AntennaBeam`
              - Class defining an antenna beam.

            * - :pyclass:`~AntennaBeamTransmit`
              - Class defining a transmit antenna beam.

            * - :pyclass:`~AntennaBeamCollection`
              - Class defining an antenna beam collection.

            * - :pyclass:`~AntennaBeamSelectionStrategy`
              - Class defining a beam selection strategy.

            * - :pyclass:`~AntennaBeamSelectionStrategyAggregate`
              - Class defining a aggregated beam selection strategy.

            * - :pyclass:`~AntennaBeamSelectionStrategyMaxGain`
              - Class defining a maximum gain beam selection strategy.

            * - :pyclass:`~AntennaBeamSelectionStrategyMinBoresightAngle`
              - Class defining a minimum boresight angle beam selection strategy.

            * - :pyclass:`~AntennaBeamSelectionStrategyScriptPlugin`
              - Class defining a script plugin beam selection strategy.

            * - :pyclass:`~CommSystem`
              - Class defining a CommSystem object.

            * - :pyclass:`~CommSystemGraphics`
              - Class defining 2D Graphics properties of a CommSystem.

            * - :pyclass:`~CommSystemGraphics3D`
              - Class defining 3D Graphics properties of a CommSystem.

            * - :pyclass:`~CommSystemAccessOptions`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemAccessEventDetection`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemAccessEventDetectionSubsample`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemAccessEventDetectionSamplesOnly`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemAccessSamplingMethod`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemAccessSamplingMethodFixed`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemAccessSamplingMethodAdaptive`
              - Class defining a CommSystem access options.

            * - :pyclass:`~CommSystemLinkSelectionCriteria`
              - Class defining a CommSystem link selection criteria.

            * - :pyclass:`~CommSystemLinkSelectionCriteriaMinimumRange`
              - Class defining a CommSystem link selection criteria.

            * - :pyclass:`~CommSystemLinkSelectionCriteriaMaximumElevation`
              - Class defining a CommSystem link selection criteria.

            * - :pyclass:`~CommSystemLinkSelectionCriteriaScriptPlugin`
              - Class defining a CommSystem link selection criteria.

            * - :pyclass:`~ComponentDirectory`
              - Manages all components.

            * - :pyclass:`~ComponentInfo`
              - Class defining a component.

            * - :pyclass:`~ComponentInfoCollection`
              - The collection of components and component folders.

            * - :pyclass:`~ComponentAttrLinkEmbedControl`
              - Attribute based component link/embed control.

            * - :pyclass:`~Volumetric`
              - The AgVolumetric class.

            * - :pyclass:`~VmGridSpatialCalculation`
              - Class defining the volume grid spatial calculation.

            * - :pyclass:`~VmExternalFile`
              - Class defining the volume external file.

            * - :pyclass:`~VmAnalysisInterval`
              - Class defining the volumetric analysis interval.

            * - :pyclass:`~VmAdvanced`
              - Class defining the volumetric Computed Data Save options.

            * - :pyclass:`~VmGraphics3D`
              - Class defining 3D graphics properties of volumetric object.

            * - :pyclass:`~VmGraphics3DGrid`
              - Class defining grid properties of 3D graphics for volumetric object.

            * - :pyclass:`~VmGraphics3DCrossSection`
              - Class defining planar cross-sections through the volumetric grid.

            * - :pyclass:`~VmGraphics3DCrossSectionPlane`
              - Class defining cross-section plane for volumetric grid.

            * - :pyclass:`~VmGraphics3DCrossSectionPlaneCollection`
              - Class defining collection of cross-section planes for volumetric grid.

            * - :pyclass:`~VmGraphics3DVolume`
              - Class defining planar cross-sections through the volumetric grid.

            * - :pyclass:`~VmGraphics3DActiveGridPoints`
              - Class defining Active Grid Points for Volumetric Object.

            * - :pyclass:`~VmGraphics3DSpatialCalculationLevels`
              - Class defining Spatial Calculation Levels for Volumetric Object.

            * - :pyclass:`~VmGraphics3DSpatialCalculationLevel`
              - Class defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :pyclass:`~VmGraphics3DSpatialCalculationLevelCollection`
              - Class defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :pyclass:`~VmGraphics3DLegend`
              - Class defining Boundary/Fill legend for volumetric object.

            * - :pyclass:`~VmExportTool`
              - The Volumetric Export Tool.

            * - :pyclass:`~SatelliteCollection`
              - The AgSatelliteCollection class.

            * - :pyclass:`~Subset`
              - The AgSubset class.

            * - :pyclass:`~ElementConfiguration`
              - Class defining an element configuration.

            * - :pyclass:`~ElementConfigurationCircular`
              - Class defining a circular element configuration.

            * - :pyclass:`~ElementConfigurationLinear`
              - Class defining a linear element configuration.

            * - :pyclass:`~ElementConfigurationAsciiFile`
              - Class defining a ascii file element configuration.

            * - :pyclass:`~ElementConfigurationHfssEepFile`
              - Class defining an HFSS EEP file element configuration.

            * - :pyclass:`~ElementConfigurationPolygon`
              - Class defining a polygon element configuration.

            * - :pyclass:`~ElementConfigurationHexagon`
              - Class defining a hexagon element configuration.

            * - :pyclass:`~SolarActivityConfiguration`
              - Class defining a solar activity configuration.

            * - :pyclass:`~SolarActivityConfigurationSunspotNumber`
              - Class defining sunspot number configuration.

            * - :pyclass:`~SolarActivityConfigurationSolarFlux`
              - Class defining the solar flux configuration.

            * - :pyclass:`~Beamformer`
              - Class defining a beamformer.

            * - :pyclass:`~BeamformerAsciiFile`
              - Class defining a beamformer ascii file.

            * - :pyclass:`~BeamformerMvdr`
              - Class defining a beamformer mvdr.

            * - :pyclass:`~BeamformerUniform`
              - Class defining a uniform tapered beamformer.

            * - :pyclass:`~BeamformerBlackmanHarris`
              - Class defining a Blackman-Harris tapered beamformer.

            * - :pyclass:`~BeamformerCosine`
              - Class defining a cosine tapered beamformer.

            * - :pyclass:`~BeamformerCosineX`
              - Class defining a cosine^X tapered beamformer.

            * - :pyclass:`~BeamformerCustomTaperFile`
              - Class defining a custom taper file beamformer.

            * - :pyclass:`~BeamformerDolphChebyshev`
              - Class defining a Dolph-Chebyshev tapered beamformer.

            * - :pyclass:`~BeamformerHamming`
              - Class defining a Hamming tapered beamformer.

            * - :pyclass:`~BeamformerHann`
              - Class defining a Hann tapered beamformer.

            * - :pyclass:`~BeamformerRaisedCosine`
              - Class defining a raised cosine tapered beamformer.

            * - :pyclass:`~BeamformerRaisedCosineSquared`
              - Class defining a raised cosine squared tapered beamformer.

            * - :pyclass:`~BeamformerScript`
              - Class defining a beamformer script plugin.

            * - :pyclass:`~DirectionProvider`
              - Class defining a direction provider.

            * - :pyclass:`~DirectionProviderAsciiFile`
              - Class defining an ascii file direction provider.

            * - :pyclass:`~DirectionProviderObject`
              - Class defining an object direction provider.

            * - :pyclass:`~DirectionProviderLink`
              - Class defining an link direction provider.

            * - :pyclass:`~DirectionProviderScript`
              - Class defining an script plugin direction provider.

            * - :pyclass:`~Element`
              - Class defining a phased array element.

            * - :pyclass:`~ElementCollection`
              - Class defining a phased array element collection.

            * - :pyclass:`~KeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :pyclass:`~RadarStcAttenuation`
              - Class defining an radar stc.

            * - :pyclass:`~RadarStcAttenuationDecayFactor`
              - Class defining an radar decay factor stc.

            * - :pyclass:`~RadarStcAttenuationDecaySlope`
              - Class defining an radar decay slope stc.

            * - :pyclass:`~RadarStcAttenuationMapRange`
              - Class defining an radar stc range map.

            * - :pyclass:`~RadarStcAttenuationMapAzimuthRange`
              - Class defining an radar stc azimuth-range map.

            * - :pyclass:`~RadarStcAttenuationMapElevationRange`
              - Class defining an radar stc elevation-range map.

            * - :pyclass:`~RadarStcAttenuationPlugin`
              - Class defining an radar stc Com Plugin.

            * - :pyclass:`~SensorPointingAlongVector`
              - Class defining the along vector pointing type for a Sensor.

            * - :pyclass:`~SensorPointingSchedule`
              - Allow to schedule a sensor to point at a specific location at a specific time.

            * - :pyclass:`~AccessConstraintAnalysisWorkbenchCollection`
              - Collection of Analysis Workbench constraints.

            * - :pyclass:`~AccessConstraintAnalysisWorkbench`
              - Class related to Analysis Workbench constraints.

            * - :pyclass:`~Graphics3DArticulationFile`
              - Class defining the vo articulation file.

            * - :pyclass:`~DataProviderResultStatisticResult`
              - Results returned by statistics computation.

            * - :pyclass:`~DataProviderResultTimeVaryingExtremumResult`
              - Results returned by time varying extremum computation.

            * - :pyclass:`~DataProviderResultStatistics`
              - Class used to compute statistics and time varying extremum on data provider result data sets.

            * - :pyclass:`~Graphics3DModelGltfImageBased`
              - Class defining glTF Reflection Settings.

            * - :pyclass:`~StkObjectCutCopyPasteEventArgs`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

            * - :pyclass:`~StkPreferencesPythonPlugins`
              - Allow configuring Python plugin preferences.

            * - :pyclass:`~PathCollection`
              - Allow adding and removing of paths.

            * - :pyclass:`~AdvCAT`
              - AdvCAT properties.

            * - :pyclass:`~AdvCATAvailableObjectCollection`
              - Read-only collection of available objects.

            * - :pyclass:`~AdvCATChosenObject`
              - A chosen object.

            * - :pyclass:`~AdvCATChosenObjectCollection`
              - The chosen object collection.

            * - :pyclass:`~AdvCATPreFilters`
              - AdvCAT pre-filters properties.

            * - :pyclass:`~AdvCATAdvancedEllipsoid`
              - AdvCAT advanced ellipsoid properties.

            * - :pyclass:`~AdvCATAdvanced`
              - AdvCAT advanced properties.

            * - :pyclass:`~AdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :pyclass:`~EOIRShapeObject`
              - Represents a generic shape object.

            * - :pyclass:`~EOIRShapeBox`
              - Box shape class.

            * - :pyclass:`~EOIRShapeCone`
              - Cone shape class.

            * - :pyclass:`~EOIRShapeCylinder`
              - Cylinder shape class.

            * - :pyclass:`~EOIRShapePlate`
              - Plate shape class.

            * - :pyclass:`~EOIRShapeSphere`
              - Sphere shape class.

            * - :pyclass:`~EOIRShapeCoupler`
              - Coupler shape class.

            * - :pyclass:`~EOIRShapeNone`
              - None shape class.

            * - :pyclass:`~EOIRShapeGEOComm`
              - GEOComm shape class.

            * - :pyclass:`~EOIRShapeLEOComm`
              - LEOComm shape class.

            * - :pyclass:`~EOIRShapeLEOImaging`
              - LEOImaging shape class.

            * - :pyclass:`~EOIRShapeCustomMesh`
              - CustomMesh shape class.

            * - :pyclass:`~EOIRShapeTargetSignature`
              - TargetSignature shape class.

            * - :pyclass:`~EOIRStagePlume`
              - Plume shape class.

            * - :pyclass:`~EOIRShape`
              - AgEOIRShape class.

            * - :pyclass:`~EOIRShapeCollection`
              - Collection of shapes.

            * - :pyclass:`~EOIRMaterialElement`
              - AgEOIRMaterialElement class.

            * - :pyclass:`~EOIRMaterialElementCollection`
              - Collection of material elements.

            * - :pyclass:`~EOIRStage`
              - Stage base class.

            * - :pyclass:`~EOIR`
              - AgEOIR interface class.

            * - :pyclass:`~MissileEOIR`
              - AgMsEOIR interface class.

            * - :pyclass:`~VehicleEOIR`
              - AgVeEOIR interface class.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~CONSTANTS`
              - AgEConstants contains base IDs for various structures.

            * - :pyclass:`~HELP_CONTEXT_IDS`
              - Help context IDs.

            * - :pyclass:`~ERROR_CODES`
              - Error codes.

            * - :pyclass:`~ABERRATION_TYPE`
              - The model of aberration to be used in access computations.

            * - :pyclass:`~ANIMATION_MODES`
              - Animation modes.

            * - :pyclass:`~ANIMATION_OPTIONS`
              - Animation Options.

            * - :pyclass:`~ANIMATION_ACTIONS`
              - Animation action options.

            * - :pyclass:`~ANIMATION_DIRECTIONS`
              - Animation direction options.

            * - :pyclass:`~AZ_EL_MASK_TYPE`
              - Obscura types of the facility, place or target for AzElMask definition.

            * - :pyclass:`~ACTION_TYPE`
              - Specify the action type for the Interval Access Constraint.

            * - :pyclass:`~AXIS_OFFSET`
              - Specify the axis offset for the sensor 3D Vertex Offset.

            * - :pyclass:`~DATA_PROVIDER_RESULT_CATEGORIES`
              - Specify the category of results returned by the data providers.

            * - :pyclass:`~DATA_PROVIDER_TYPE`
              - Specify the type of the result returned by data providers.

            * - :pyclass:`~DATA_PROVIDER_ELEMENT_TYPE`
              - Specify the type of data returned by data providers.

            * - :pyclass:`~ACCESS_TIME_TYPE`
              - The time period to use for the access computation.

            * - :pyclass:`~ALTITUDE_REFERENCE_TYPE`
              - Altitude reference options.

            * - :pyclass:`~TERRAIN_NORM_TYPE`
              - Methods of defining the slope of the local terrain for the facility, place or target.

            * - :pyclass:`~LIGHTING_OBSTRUCTION_MODEL_TYPE`
              - Obstruction model used in lighting computations.

            * - :pyclass:`~DISPLAY_TIMES_TYPE`
              - Display times options for the object.

            * - :pyclass:`~AREA_TYPE`
              - Methods of defining the area target's boundaries.

            * - :pyclass:`~TRAJECTORY_TYPE`
              - Trajectory type for a point.

            * - :pyclass:`~OFFSET_FRAME_TYPE`
              - Frame options for label offset.

            * - :pyclass:`~SCENARIO_3D_POINT_SIZE`
              - Font size in points.

            * - :pyclass:`~TERRAIN_FILE_TYPE`
              - Terrain file type options.

            * - :pyclass:`~TILESET_3D_SOURCE_TYPE`
              - 3DTileset source type options.

            * - :pyclass:`~MARKER_TYPE`
              - Marker style options for a waypoint.

            * - :pyclass:`~VECTOR_AXES_CONNECT_TYPE`
              - Methods for connecting geometric elements.

            * - :pyclass:`~GRAPHICS_3D_MARKER_ORIGIN_TYPE`
              - Options for the AgVOMarker X or Y Origin property.

            * - :pyclass:`~GRAPHICS_3D_LABEL_SWAP_DISTANCE`
              - Label swap distance options.

            * - :pyclass:`~PLANET_POSITION_SOURCE_TYPE`
              - Options for defining a planet.

            * - :pyclass:`~EPHEM_SOURCE_TYPE`
              - Central body ephemeris sources.

            * - :pyclass:`~PLANET_ORBIT_DISPLAY_TYPE`
              - Orbit display options for a planet.

            * - :pyclass:`~SCENARIO_END_LOOP_TYPE`
              - Scenario animation cycle options.

            * - :pyclass:`~SCENARIO_REFRESH_DELTA_TYPE`
              - Scenario animation refresh update options.

            * - :pyclass:`~SENSOR_PATTERN`
              - Sensor patterns.

            * - :pyclass:`~SENSOR_POINTING`
              - Sensor pointing options.

            * - :pyclass:`~SENSOR_POINTING_TARGETED_BORESIGHT_TYPE`
              - Boresight types for sensors of targeted pointing type.

            * - :pyclass:`~BORESIGHT_TYPE`
              - About boresight options for sensors of targeted pointing type.

            * - :pyclass:`~TRACK_MODE_TYPE`
              - Track mode options for tracking boresights.

            * - :pyclass:`~SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE`
              - Primary boresight axis for Sensor Az-El mask.

            * - :pyclass:`~SENSOR_REFRACTION_TYPE`
              - Sensor refraction models.

            * - :pyclass:`~SENSOR_PROJECTION_DISTANCE_TYPE`
              - Sensor 2D Graphics Projection 'Project To' options.

            * - :pyclass:`~SENSOR_LOCATION`
              - Sensor Location Type options.

            * - :pyclass:`~SCENARIO_TIME_STEP_TYPE`
              - Scenario animation time step options.

            * - :pyclass:`~NOTE_SHOW_TYPE`
              - Options for specifying when a label note displays.

            * - :pyclass:`~GEOMETRIC_ELEM_TYPE`
              - Options for the VORefCrdn Type.

            * - :pyclass:`~SENSOR_SCAN_MODE`
              - Options for the Sensor Spinning Scan Mode.

            * - :pyclass:`~CONSTRAINT_BACKGROUND`
              - Options for the Background constraint, and Advanced vehicle constraint.

            * - :pyclass:`~CONSTRAINT_GROUND_TRACK`
              - Options for the Ground Track constraint, an Advanced vehicle constraint.

            * - :pyclass:`~INTERSECTION_TYPE`
              - Intersection display options for sensor projection.

            * - :pyclass:`~CONSTRAINT_LIGHTING`
              - Options for the Lighting access constraint.

            * - :pyclass:`~SENSOR_GRAPHICS_3D_PROJECTION_TYPE`
              - Options for a sensor's 3D Graphics Projection Type.

            * - :pyclass:`~SENSOR_GRAPHICS_3D_PULSE_STYLE`
              - Options for a sensor's 3D Graphics Pulse Style.

            * - :pyclass:`~SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET`
              - Options for a sensor's 3D Graphics Pulse Frequency presets.

            * - :pyclass:`~LINE_WIDTH`
              - Line widths.

            * - :pyclass:`~STK_OBJECT_TYPE`
              - STK objects.

            * - :pyclass:`~ACCESS_CONSTRAINTS`
              - Available Access Constraint.

            * - :pyclass:`~BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE`
              - Border Wall upper and lower edge altitude references.

            * - :pyclass:`~SHADOW_MODEL`
              - Shadow model options for solar radiation pressure.

            * - :pyclass:`~METHOD_TO_COMPUTE_SUN_POSITION`
              - Methods to compute sun position.

            * - :pyclass:`~ATMOSPHERIC_DENSITY_MODEL`
              - Atmospheric density models.

            * - :pyclass:`~MARKER_SHAPE_3D`
              - 3D marker shapes.

            * - :pyclass:`~LEAD_TRAIL_DATA`
              - Lead and trail types for track display.

            * - :pyclass:`~TICK_DATA`
              - Tick mark options. Tick marks represent milestones at specified intervals along a vehicle's track in the 3D Graphics window.

            * - :pyclass:`~LOAD_METHOD_TYPE`
              - TLE load options.

            * - :pyclass:`~LLA_POSITION_TYPE`
              - LLA Position Types.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_PASS`
              - Pass display options.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_VISIBLE_SIDES`
              - Pass display direction options.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_OFFSET`
              - Options for offset direction for 2D time events graphics.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE`
              - 2D Graphics time event graphics options.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_ATTRIBUTES`
              - Criteria for displaying a vehicle's 2D Graphics attributes.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_ELEVATION`
              - Options for vehicle swath.

            * - :pyclass:`~VEHICLE_GRAPHICS_2D_OPTIONS`
              - Display options for vehicle swath.

            * - :pyclass:`~MODEL_TYPE`
              - Display options 3D model.

            * - :pyclass:`~VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE`
              - Options for where to end drop lines.

            * - :pyclass:`~VEHICLE_GRAPHICS_3D_SIGMA_SCALE`
              - Sigma scale options for sizing covariance pointing contours.

            * - :pyclass:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`
              - Options for 3D graphics for covariance pointing contours.

            * - :pyclass:`~ROUTE_GRAPHICS_3D_MARKER_TYPE`
              - Waypoint marker options.

            * - :pyclass:`~VEHICLE_ELLIPSE_OPTIONS`
              - Elliptical motion modeling options.

            * - :pyclass:`~VEHICLE_PROPAGATOR_TYPE`
              - Vehicle propagators (available for vehicle types listed in parentheses).

            * - :pyclass:`~VEHICLE_SGP4_SWITCH_METHOD`
              - TLE Switch method for the SGP4 propagator.

            * - :pyclass:`~VEHICLE_SGP4TLE_SELECTION`
              - TLE Selection method for the SGP4 propagator.

            * - :pyclass:`~VEHICLE_SGP4_AUTO_UPDATE_SOURCE`
              - The TLE sources where the SGP4 propagator retrieves TLEs from automatically upon propagation.

            * - :pyclass:`~THIRD_BODY_GRAV_SOURCE_TYPE`
              - Sources for 3rd body gravitation data.

            * - :pyclass:`~VEHICLE_GEOMAG_FLUX_SRC`
              - GeomagFluxSrc.

            * - :pyclass:`~VEHICLE_GEOMAG_FLUX_UPDATE_RATE`
              - Geomagnetic flux update rate options.

            * - :pyclass:`~VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE`
              - Options for specifying solar and geomagnetic flux.

            * - :pyclass:`~VEHICLE_INTEGRATION_MODEL`
              - Integration methods.

            * - :pyclass:`~VEHICLE_PREDICTOR_CORRECTOR_SCHEME`
              - Predictor Corrector schemes.

            * - :pyclass:`~VEHICLE_METHOD`
              - Step size control options.

            * - :pyclass:`~VEHICLE_INTERPOLATION_METHOD`
              - Interpolation methods.

            * - :pyclass:`~VEHICLE_FRAME`
              - Frame options for covariance matrix.

            * - :pyclass:`~VEHICLE_CORRELATION_LIST_TYPE`
              - Correlation List row and column values.

            * - :pyclass:`~VEHICLE_CONSIDER_ANALYSIS_TYPE`
              - Consider parameters for HPOP covariance.

            * - :pyclass:`~VEHICLE_WAYPOINT_COMP_METHOD`
              - Methods for computing waypoints.

            * - :pyclass:`~VEHICLE_ALTITUDE_REFERENCE`
              - Reference altitude options for waypoints.

            * - :pyclass:`~VEHICLE_WAYPOINT_INTERP_METHOD`
              - Interpolation methods.

            * - :pyclass:`~VEHICLE_LAUNCH`
              - Options for launch coordinates.

            * - :pyclass:`~VEHICLE_IMPACT`
              - Impact location options.

            * - :pyclass:`~VEHICLE_LAUNCH_CONTROL`
              - Flight parameters for a missile.

            * - :pyclass:`~VEHICLE_IMPACT_LOCATION`
              - Options for specifying missile impact point.

            * - :pyclass:`~VEHICLE_PASS_NUMBERING`
              - Pass numbering options.

            * - :pyclass:`~VEHICLE_PARTIAL_PASS_MEASUREMENT`
              - Partial Pass Measurement methods (typically used for reporting data).

            * - :pyclass:`~VEHICLE_COORDINATE_SYSTEM`
              - Coordinate system used for measurement of latitude and longitude.

            * - :pyclass:`~VEHICLE_BREAK_ANGLE_TYPE`
              - Definition options for setting pass breaks:.

            * - :pyclass:`~VEHICLE_DIRECTION`
              - Direction of latitude crossing at the beginning of a pass.

            * - :pyclass:`~GRAPHICS_3D_LOCATION`
              - Location options for the display of textual data in the 3D Graphics window.

            * - :pyclass:`~GRAPHICS_3D_X_ORIGIN`
              - X origin options for positioning data display.

            * - :pyclass:`~GRAPHICS_3D_Y_ORIGIN`
              - Y origin options for positioning data display.

            * - :pyclass:`~GRAPHICS_3D_FONT_SIZE`
              - Font size for data display.

            * - :pyclass:`~AIRCRAFT_WGS84_WARNING_TYPE`
              - Display mode options for aircraft mission modeler WGS84 warning.

            * - :pyclass:`~SURFACE_REFERENCE`
              - Options for surface reference of earth globes.

            * - :pyclass:`~GRAPHICS_3D_FORMAT`
              - Font format for data display.

            * - :pyclass:`~ATTITUDE_STANDARD_TYPE`
              - AgEAttitudeStandardType tells the user which interface to cast to. eRouteAttitudeStandard -> IAgVeRouteAttitudeStandard, eTrajectoryAttitudeStandard -> IAgVeTrajectoryAttitudeStandard, eOrbitAttitudeStanard -> IAgVeOrbitAttitudeStandard.

            * - :pyclass:`~VEHICLE_ATTITUDE`
              - Available attitude types.

            * - :pyclass:`~VEHICLE_PROFILE`
              - Predefined attitude profiles.

            * - :pyclass:`~VEHICLE_LOOK_AHEAD_METHOD`
              - Look ahead duration methods.

            * - :pyclass:`~VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION`
              - Values of the enumeration represent polymorphic object types.

            * - :pyclass:`~SENSOR_ALTITUDE_CROSSING_SIDES`
              - Options for specifying which crossings are computed and displayed in the 2D Graphics window.

            * - :pyclass:`~SENSOR_ALTITUDE_CROSSING_DIRECTION`
              - Options for specifying the direction in which the sensor's field of view crosses the specified altitude.

            * - :pyclass:`~SENSOR_GRAPHICS_3D_INHERIT_FROM_2D`
              - Options for how projection distances that are computed based on 2D Graphics projection settings are displayed in the 3D Graphics window.

            * - :pyclass:`~SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE`
              - Options optimizing the visual appearance of projections.

            * - :pyclass:`~CHAIN_TIME_PERIOD_TYPE`
              - Compute Time Period Type.

            * - :pyclass:`~CHAIN_CONST_CONSTRAINTS_MODE`
              - Constellation Constraints Mode.

            * - :pyclass:`~CHAIN_COV_ASSET_MODE`
              - Chain Cov Asset Mode.

            * - :pyclass:`~CHAIN_PARENT_PLATFORM_RESTRICTION`
              - Options for a chain's From and To Parent Platform Restriction.

            * - :pyclass:`~CHAIN_OPTIMAL_STRAND_METRIC_TYPE`
              - Chain optimal strand metric type.

            * - :pyclass:`~CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE`
              - Chain optimal strand calculation scalar type.

            * - :pyclass:`~CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE`
              - Chain optimal strand link comparison type.

            * - :pyclass:`~CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE`
              - Chain optimal strand link comparison type.

            * - :pyclass:`~DATA_SAVE_MODE`
              - Access Save Mode.

            * - :pyclass:`~COVERAGE_BOUNDS`
              - Coverage bounds options: values of the enumeration represent polymorphic object types.

            * - :pyclass:`~COVERAGE_POINT_LOC_METHOD`
              - Point location method.

            * - :pyclass:`~COVERAGE_POINT_ALTITUDE_METHOD`
              - Custom point altitude method.

            * - :pyclass:`~COVERAGE_GRID_CLASS`
              - Classes of objects that can be used as templates to associate access constraints, basic object properties and, in some cases, altitude with points in the grid.

            * - :pyclass:`~COVERAGE_ALTITUDE_METHOD`
              - Method for specifying the altitude of a grid point.

            * - :pyclass:`~COVERAGE_GROUND_ALTITUDE_METHOD`
              - Method for specifying the ground altitude of a grid point.

            * - :pyclass:`~COVERAGE_DATA_RETENTION`
              - Data retention options.

            * - :pyclass:`~COVERAGE_REGION_ACCESS_ACCEL`
              - Regional acceleration options.

            * - :pyclass:`~COVERAGE_RESOLUTION`
              - Coverage grid resolution options: values of the enumeration represent polymorphic object types.

            * - :pyclass:`~COVERAGE_ASSET_STATUS`
              - Coverage asset status.

            * - :pyclass:`~COVERAGE_ASSET_GROUPING`
              - Coverage asset grouping options.

            * - :pyclass:`~FIGURE_OF_MERIT_DEFINITION_TYPE`
              - Figure of Merit types: values of the enumeration represent polymorphic object types.

            * - :pyclass:`~FIGURE_OF_MERIT_SATISFACTION_TYPE`
              - Satisfaction options: determine whether satisfaction is achieved based on the value of the figure of merit.

            * - :pyclass:`~FIGURE_OF_MERIT_CONSTRAINT_NAME`
              - Available constraints to use for the Access Constraint Figure of Merit.

            * - :pyclass:`~FIGURE_OF_MERIT_COMPUTE`
              - Figure of Merit compute options.

            * - :pyclass:`~FIGURE_OF_MERIT_ACROSS_ASSETS`
              - Across Assets options: specify which value of the constraint is to be selected based on all currently available assets.

            * - :pyclass:`~FIGURE_OF_MERIT_COMPUTE_TYPE`
              - Allowed number of assets for the navigation solution.

            * - :pyclass:`~FIGURE_OF_MERIT_METHOD`
              - Dilution of Precision method.

            * - :pyclass:`~FIGURE_OF_MERIT_END_GAP_OPTION`
              - End gap options: control consideration of gaps at ends of analysis intervals.

            * - :pyclass:`~FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE`
              - Contour fill options.

            * - :pyclass:`~FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD`
              - Methods for assigning colors to contour levels.

            * - :pyclass:`~FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT`
              - Format options for floating point numbers.

            * - :pyclass:`~FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION`
              - Level order display options for the contour legend.

            * - :pyclass:`~FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION`
              - Accumulation options: control the sense and persistence of animation graphics for a Figure of Merit.

            * - :pyclass:`~FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE`
              - Options for uncertainty in one-way range measurements for the Navigation Accuracy Figure of Merit.

            * - :pyclass:`~IV_CLOCK_HOST`
              - Clock host options for access. Time values are reported with a clock colocated with the clock host object.

            * - :pyclass:`~IV_TIME_SENSE`
              - Mode of signal transmission of the designated clock host.

            * - :pyclass:`~GPS_ATTITUDE_MODEL_TYPE`
              - GPS attitude profile model types.

            * - :pyclass:`~CONSTELLATION_CONSTRAINT_RESTRICTION`
              - The values of the enumeration are used to define constellation constraints that allow you to specify the criteria to be used when constellations are combined with other objects in a chain.

            * - :pyclass:`~EVENT_DETECTION`
              - Available event detection strategies.

            * - :pyclass:`~SAMPLING_METHOD`
              - Available sampling methods.

            * - :pyclass:`~COVERAGE_SATISFACTION_TYPE`
              - The condition on the number of assets covering a grid point that must be satisfied for a valid access.

            * - :pyclass:`~CCSDS_REFERENCE_FRAME`
              - Reference Frame.

            * - :pyclass:`~CCSDS_DATE_FORMAT`
              - The date format of the file.

            * - :pyclass:`~CCSDS_EPHEM_FORMAT`
              - The ephemeris format of the file.

            * - :pyclass:`~CCSDS_TIME_SYSTEM`
              - Time System.

            * - :pyclass:`~STK_EPHEM_COORDINATE_SYSTEM`
              - The Coordinate System of the file.

            * - :pyclass:`~STK_EPHEM_COVARIANCE_TYPE`
              - The covariance data export type.

            * - :pyclass:`~EXPORT_TOOL_VERSION_FORMAT`
              - The version format of the file.

            * - :pyclass:`~EXPORT_TOOL_TIME_PERIOD`
              - Values of the enumeration represent polymorphic object types.

            * - :pyclass:`~SPICE_INTERPOLATION`
              - The SPICE interpolation type.

            * - :pyclass:`~ATTITUDE_COORDINATE_AXES`
              - Attitude export options.

            * - :pyclass:`~ATTITUDE_INCLUDE`
              - Details to include in an exported Attitude file.

            * - :pyclass:`~EXPORT_TOOL_STEP_SIZE`
              - The Step Size type for an attitude file.

            * - :pyclass:`~TEXT_OUTLINE_STYLE`
              - The text outline style for 2D graphics display.

            * - :pyclass:`~MTO_RANGE_MODE`
              - MTO Range Mode.

            * - :pyclass:`~MTO_TRACK_EVAL`
              - MTO Track Eval Mode.

            * - :pyclass:`~MTO_ENTIRETY`
              - MTO Entirety Mode.

            * - :pyclass:`~MTO_VISIBILITY_MODE`
              - MTO Visibility Mode.

            * - :pyclass:`~MTO_OBJECT_INTERVAL`
              - MTO object interval type.

            * - :pyclass:`~MTO_INPUT_DATA_TYPE`
              - MTO Input Data Type.

            * - :pyclass:`~SOLID_TIDE`
              - The Solid Tide Type for force modeling.

            * - :pyclass:`~TIME_PERIOD_VALUE_TYPE`
              - Time value types.

            * - :pyclass:`~ONE_POINT_ACCESS_STATUS`
              - One point access status.

            * - :pyclass:`~ONE_POINT_ACCESS_SUMMARY`
              - One point access summary type.

            * - :pyclass:`~LOOK_AHEAD_PROPAGATOR`
              - Propagators used for calculating ephemeris for look ahead purposes. The enumeration is used with realtime propagators.

            * - :pyclass:`~GRAPHICS_3D_MARKER_ORIENTATION`
              - 3D graphics marker orientations.

            * - :pyclass:`~SRP_MODEL`
              - Solar radiation pressure model types.

            * - :pyclass:`~DRAG_MODEL`
              - Drag model types.

            * - :pyclass:`~VEHICLE_PROPAGATION_FRAME`
              - Propagation frames used by J2/J4/TwoBody propagators.

            * - :pyclass:`~STAR_REFERENCE_FRAME`
              - Star reference frame types.

            * - :pyclass:`~GPS_REFERENCE_WEEK`
              - GPS almanac reference week.

            * - :pyclass:`~COVERAGE_CUSTOM_REGION_ALGORITHM`
              - The enumerations are used to enable/disable the special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).

            * - :pyclass:`~VEHICLE_GPS_SWITCH_METHOD`
              - GPS Switch method for the GPS propagator.

            * - :pyclass:`~VEHICLE_GPS_ELEM_SELECTION`
              - GPS Selection method for the GPS propagator.

            * - :pyclass:`~VEHICLE_GPS_AUTO_UPDATE_SOURCE`
              - The sources to retrieve GPS elements from upon propagation.

            * - :pyclass:`~VEHICLE_GPS_ALMANAC_TYPE`
              - GPS Almanac types.

            * - :pyclass:`~STK_EXTERNAL_EPHEMERIS_FORMAT`
              - Ephemeris file formats supported by the Stk external propagator.

            * - :pyclass:`~STK_EXTERNAL_FILE_MESSAGE_LEVEL`
              - Ephemeris file message level used by the Stk external propagator.

            * - :pyclass:`~COVERAGE_3D_DRAW_AT_ALTITUDE_MODE`
              - Coverage definition drawing modes for filled graphics when showing at altitude in 3D Graphics window.

            * - :pyclass:`~DISTANCE_ON_SPHERE`
              - Type of line which connects the two points.

            * - :pyclass:`~FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE`
              - Invalid Value Action: Controls consideration of time samples usage for computing navigation solution when insufficient number of assets are available at one or more of the time samples used.

            * - :pyclass:`~VEHICLE_SLEW_TIMING_BETWEEN_TARGETS`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

            * - :pyclass:`~VEHICLE_SLEW_MODE`
              - Target slew modes.

            * - :pyclass:`~COMPONENT`
              - The different types of components in the component browser.

            * - :pyclass:`~VM_DEFINITION_TYPE`
              - Volume grid definition types.

            * - :pyclass:`~VM_SPATIAL_CALC_EVAL_TYPE`
              - Evaluation of Spatial Calculation types.

            * - :pyclass:`~VM_SAVE_COMPUTED_DATA_TYPE`
              - Save Computed Data types.

            * - :pyclass:`~VM_DISPLAY_VOLUME_TYPE`
              - Graphics volume display type.

            * - :pyclass:`~VM_DISPLAY_QUALITY_TYPE`
              - Quality of the graphics display types.

            * - :pyclass:`~VM_LEGEND_NUMERIC_NOTATION`
              - Legend numeric notation types.

            * - :pyclass:`~VM_LEVEL_ORDER`
              - Legend level display order.

            * - :pyclass:`~SENSOR_EOIR_PROCESSING_LEVELS`
              - EOIR processing levels.

            * - :pyclass:`~SENSOR_EOIR_JITTER_TYPES`
              - EOIR jitter type.

            * - :pyclass:`~SENSOR_EOIR_SCAN_MODES`
              - EOIR sensor scan mode.

            * - :pyclass:`~SENSOR_EOIR_BAND_IMAGE_QUALITY`
              - EOIR band image quality levels.

            * - :pyclass:`~SENSOR_EOIR_BAND_SPECTRAL_SHAPE`
              - EOIR overall system spectral shape determination.

            * - :pyclass:`~SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE`
              - EOIR spatial input parameter specification.

            * - :pyclass:`~SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS`
              - EOIR spectral relative system response units specification.

            * - :pyclass:`~SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE`
              - EOIR optical input parameter specification.

            * - :pyclass:`~SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE`
              - EOIR optical transmission parameter specification mode.

            * - :pyclass:`~SENSOR_EOIR_BAND_RAD_PARAM_LEVEL`
              - EOIR radiometric detector parameter level of specification.

            * - :pyclass:`~SENSOR_EOIR_BAND_QE_MODE`
              - EOIR quantum efficiency specification mode.

            * - :pyclass:`~SENSOR_EOIR_BAND_QUANTIZATION_MODE`
              - EOIR mode of determining quantization step size.

            * - :pyclass:`~SENSOR_EOIR_BAND_WAVELENGTH_TYPE`
              - EOIR band diffraction wavelength reference type.

            * - :pyclass:`~SENSOR_EOIR_BAND_SATURATION_MODE`
              - EOIR band irradiance or radiance reference mode.

            * - :pyclass:`~VM_VOLUME_GRID_EXPORT_TYPE`
              - Volumetric data export types.

            * - :pyclass:`~VM_DATA_EXPORT_FORMAT_TYPE`
              - Volumetric data export format types.

            * - :pyclass:`~CONSTELLATION_FROM_TO_PARENT_CONSTRAINT`
              - Options for a chain's From and To Parent Constraints.

            * - :pyclass:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS`
              - Available Analysis Workbench Access Constraints.

            * - :pyclass:`~STATISTICS`
              - The different statistics that might be available for a data set.

            * - :pyclass:`~TIME_VARYING_EXTREMUM`
              - The different time varying extremum that might be available for a data set.

            * - :pyclass:`~MODEL_GLTF_REFLECTION_MAP_TYPE`
              - Settings for glTF Reflection.

            * - :pyclass:`~SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE`
              - The different ways to determine the sensor's space projection distance in the 3D window.

            * - :pyclass:`~LOP_ATMOSPHERIC_DENSITY_MODEL`
              - LOP Atmospheric density models.

            * - :pyclass:`~LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL`
              - Low Altitude Atmospheric density models.

            * - :pyclass:`~EPHEM_EXPORT_TOOL_FILE_FORMAT`
              - Ephemeris Export Tool file formats.

            * - :pyclass:`~ADV_CAT_ELLIPSOID_CLASS`
              - Method for determining Ellipsoid Sizing method (class).

            * - :pyclass:`~ADV_CAT_CONJUNCTION_TYPE`
              - Mode for computing events involving conjunction TCA.

            * - :pyclass:`~ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE`
              - Type of visible Secondary Ellipsoids.

            * - :pyclass:`~EOIR_SHAPE_TYPE`
              - The object geometry which will be rendered in the synthetic scene window.

            * - :pyclass:`~EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE`
              - Designation of how material properties are specified.

            * - :pyclass:`~EOIR_THERMAL_MODEL_TYPE`
              - EOIR thermal models.

            * - :pyclass:`~EOIR_FLIGHT_TYPE`
              - EOIR Flight Types.

            * - :pyclass:`~COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE`
              - Component link/embed control reference type.

            * - :pyclass:`~SWATH_COMPUTATIONAL_METHOD`
              - Computationals methods for generating swaths.

            * - :pyclass:`~CLASSICAL_LOCATION`
              - Classical (Keplerian) element used to specify the spacecraft's location within its orbit at epoch.

            * - :pyclass:`~ORIENTATION_ASC_NODE`
              - Ascending node-related options for use in specifying orbit orientation.

            * - :pyclass:`~GEODETIC_SIZE`
              - Size options for the Geodetic coordinate type.

            * - :pyclass:`~DELAUNAY_L_TYPE`
              - Select whether to use the default representation of Delaunay L or L/SQRT(mu).

            * - :pyclass:`~DELAUNAY_H_TYPE`
              - Select whether to use the default representation of Delaunay H or H/SQRT(mu).

            * - :pyclass:`~DELAUNAY_G_TYPE`
              - Select whether to use the default representation of Delaunay G or G/SQRT(mu).

            * - :pyclass:`~EQUINOCTIAL_SIZE_SHAPE`
              - Opt whether to use Mean Motion or Semimajor Axis to specify the orbit size (Equinoctial coordinate type).

            * - :pyclass:`~MIXED_SPHERICAL_FPA`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :pyclass:`~SPHERICAL_FPA`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :pyclass:`~CLASSICAL_SIZE_SHAPE`
              - Pairs of Classical (Keplerian) elements used to specify orbit size and shape.

            * - :pyclass:`~EQUINOCTIAL_FORMULATION`
              - Formulation: retrograde or posigrade.

            * - :pyclass:`~SCATTERING_POINT_PROVIDER_TYPE`
              - Scattering point provider type.

            * - :pyclass:`~SCATTERING_POINT_MODEL_TYPE`
              - Scattering point model type.

            * - :pyclass:`~SCATTERING_POINT_PROVIDER_LIST_TYPE`
              - Scattering Point Provider List Type.

            * - :pyclass:`~POLARIZATION_TYPE`
              - Polarization Type.

            * - :pyclass:`~POLARIZATION_REFERENCE_AXIS`
              - Polarization reference axis.

            * - :pyclass:`~NOISE_TEMP_COMPUTE_TYPE`
              - System noise temperature compute type.

            * - :pyclass:`~POINTING_STRATEGY_TYPE`
              - Pointing strategy type.

            * - :pyclass:`~WAVEFORM_TYPE`
              - Waveform types.

            * - :pyclass:`~FREQUENCY_SPEC`
              - Frequency Specification Type.

            * - :pyclass:`~PRF_MODE`
              - Radar search/track prf modes.

            * - :pyclass:`~PULSE_WIDTH_MODE`
              - Radar search/track pulse width modes.

            * - :pyclass:`~WAVEFORM_SELECTION_STRATEGY_TYPE`
              - Waveform selection strategy type.

            * - :pyclass:`~ANTENNA_CONTROL_REFERENCE_TYPE`
              - Antenna control reference type.

            * - :pyclass:`~ANTENNA_MODEL_TYPE`
              - Antenna model types.

            * - :pyclass:`~ANTENNA_CONTOUR_TYPE`
              - Antenna contour types.

            * - :pyclass:`~CIRCULAR_APERTURE_INPUT_TYPE`
              - Circular aperture antenna input type.

            * - :pyclass:`~RECTANGULAR_APERTURE_INPUT_TYPE`
              - Rectangular aperture antenna input type.

            * - :pyclass:`~DIRECTION_PROVIDER_TYPE`
              - Direction Provider types.

            * - :pyclass:`~BEAMFORMER_TYPE`
              - Beamformer types.

            * - :pyclass:`~ELEMENT_CONFIGURATION_TYPE`
              - Element configuration types.

            * - :pyclass:`~LATTICE_TYPE`
              - Lattice types.

            * - :pyclass:`~SPACING_UNIT`
              - Spacing Units.

            * - :pyclass:`~LIMITS_EXCEEDED_BEHAVIOR_TYPE`
              - Limits Exceeded Behavior types.

            * - :pyclass:`~ANTENNA_GRAPHICS_COORDINATE_SYSTEM`
              - Coordinate system for defining antenna graphics resolution.

            * - :pyclass:`~ANTENNA_MODEL_INPUT_TYPE`
              - Diameter computation input type.

            * - :pyclass:`~HFSS_FFD_GAIN_TYPE`
              - Gain type.

            * - :pyclass:`~ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE`
              - Cosecant Squared antenna sidelobe selection types.

            * - :pyclass:`~BEAM_SELECTION_STRATEGY_TYPE`
              - Beam selection strategy types.

            * - :pyclass:`~TRANSMITTER_MODEL_TYPE`
              - Transmitter model types.

            * - :pyclass:`~TRANSFER_FUNCTION_TYPE`
              - Transmitter model types.

            * - :pyclass:`~RE_TRANSMITTER_OP_MODE`
              - Re-Transmitter operational mode.

            * - :pyclass:`~RECEIVER_MODEL_TYPE`
              - Receiver model types.

            * - :pyclass:`~LINK_MARGIN_TYPE`
              - Link margin types.

            * - :pyclass:`~RADAR_STC_ATTENUATION_TYPE`
              - Stc Attenuation Type.

            * - :pyclass:`~RADAR_FREQUENCY_SPEC`
              - SNR Contour Type.

            * - :pyclass:`~RADAR_SNR_CONTOUR_TYPE`
              - SNR Contour Type.

            * - :pyclass:`~RADAR_MODEL_TYPE`
              - Radar system types.

            * - :pyclass:`~RADAR_MODE_TYPE`
              - Radar mode types.

            * - :pyclass:`~RADAR_WAVEFORM_SEARCH_TRACK_TYPE`
              - Radar search/track waveform types.

            * - :pyclass:`~RADAR_SEARCH_TRACK_PRF_MODE`
              - Radar search/track prf modes.

            * - :pyclass:`~RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE`
              - Radar search/track pulse width modes.

            * - :pyclass:`~RADAR_SAR_PRF_MODE`
              - Radar SAR prf modes.

            * - :pyclass:`~RADAR_SAR_RANGE_RESOLUTION_MODE`
              - Radar SAR range resolution modes.

            * - :pyclass:`~RADAR_SAR_PCR_MODE`
              - Radar SAR pulse compression ratio modes.

            * - :pyclass:`~RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE`
              - Radar sar pulse integration mode.

            * - :pyclass:`~RADAR_P_DET_TYPE`
              - Radar probability of detection type.

            * - :pyclass:`~RADAR_PULSE_INTEGRATION_TYPE`
              - Radar pulse integration type.

            * - :pyclass:`~RADAR_PULSE_INTEGRATOR_TYPE`
              - Radar pulse integrator type.

            * - :pyclass:`~RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE`
              - Radar continuous wave analysis mode.

            * - :pyclass:`~RADAR_CLUTTER_GEOMETRY_MODEL_TYPE`
              - Radar clutter geometry model type.

            * - :pyclass:`~RADAR_CLUTTER_MAP_MODEL_TYPE`
              - Radar clutter map model type.

            * - :pyclass:`~RADAR_SWERLING_CASE`
              - Radar swerling case.

            * - :pyclass:`~RCS_COMPUTE_STRATEGY`
              - Radar cross section compute strategy.

            * - :pyclass:`~RADAR_ACTIVITY_TYPE`
              - Radar activity times strategy.

            * - :pyclass:`~RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION`
              - Radar cross section contour graphics polarization.

            * - :pyclass:`~RF_FILTER_MODEL_TYPE`
              - RF filter model types.

            * - :pyclass:`~MODULATOR_MODEL_TYPE`
              - Modulator model types.

            * - :pyclass:`~DEMODULATOR_MODEL_TYPE`
              - Demodulator model types.

            * - :pyclass:`~RAIN_LOSS_MODEL_TYPE`
              - Rain loss model types.

            * - :pyclass:`~ATMOSPHERIC_ABSORPTION_MODEL_TYPE`
              - Atmospheric absorption model types.

            * - :pyclass:`~URBAN_TERRESTRIAL_LOSS_MODEL_TYPE`
              - urban/terrestrial loss model types.

            * - :pyclass:`~CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE`
              - Clouds and Fog loss model types.

            * - :pyclass:`~CLOUDS_AND_FOG_LIQUID_WATER_CHOICES`
              - Clouds and Fog loss model liquid water content choices.

            * - :pyclass:`~IONOSPHERIC_FADING_LOSS_MODEL_TYPE`
              - Ionospheric loss model types.

            * - :pyclass:`~TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE`
              - TropoScintillation loss model types.

            * - :pyclass:`~TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES`
              - TroposphericScintillation loss model average time choices.

            * - :pyclass:`~PROJECTION_HORIZONTAL_DATUM_TYPE`
              - REMCOM Wireless InSite RT project/horizontal datum type.

            * - :pyclass:`~BUILD_HEIGHT_REFERENCE_METHOD`
              - REMCOM Wireless InSite RT building height reference method.

            * - :pyclass:`~BUILD_HEIGHT_UNIT`
              - REMCOM Wireless InSite RT building height unit.

            * - :pyclass:`~TIREM_POLARIZATION_TYPE`
              - TIREM polarization type.

            * - :pyclass:`~VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE`
              - VOACAP solar activity configuration type.

            * - :pyclass:`~VOACAP_COEFFICIENT_DATA_TYPE`
              - VOACAP coefficient data type.

            * - :pyclass:`~LASER_PROPAGATION_LOSS_MODEL_TYPE`
              - Laser propagation loss model types.

            * - :pyclass:`~LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE`
              - Laser tropospheric scintillation loss model types.

            * - :pyclass:`~ATMOSPHERIC_TURBULENCE_MODEL_TYPE`
              - Refractive index structure parameter model types.

            * - :pyclass:`~MODTRAN_AEROSOL_MODEL_TYPE`
              - MODTRAN-derived lookup table aerosol model extinction types.

            * - :pyclass:`~MODTRAN_CLOUD_MODEL_TYPE`
              - MODTRAN Cloud model types.

            * - :pyclass:`~COMM_SYSTEM_REFERENCE_BANDWIDTH`
              - CommSystem reference bandwidth.

            * - :pyclass:`~COMM_SYSTEM_CONSTRAINING_ROLE`
              - CommSystem constraining role.

            * - :pyclass:`~COMM_SYSTEM_SAVE_MODE`
              - CommSystem save mode.

            * - :pyclass:`~COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE`
              - CommSystem access options event detection type.

            * - :pyclass:`~COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE`
              - CommSystem access options sampling method type.

            * - :pyclass:`~COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE`
              - Link selection strategy types.

            * - :pyclass:`~SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY`
              - Activity level for the NASA models NASAELE and NASAPRO.

            * - :pyclass:`~SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY`
              - Activity level for CRRESPRO model.

            * - :pyclass:`~SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY`
              - Activity level for CRRESRAD model.

            * - :pyclass:`~SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE`
              - Mode by which color is assigned.

            * - :pyclass:`~SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE`
              - Scaling of magnetic field to use when assigning color/translucency.

            * - :pyclass:`~SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD`
              - Main magnetic field.

            * - :pyclass:`~SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD`
              - External magnetic field.

            * - :pyclass:`~SPACE_ENVIRONMENT_SAA_CHANNEL`
              - Energy level for SAA protons.

            * - :pyclass:`~SPACE_ENVIRONMENT_SAA_FLUX_LEVEL`
              - Flux level for SAA contour.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL`
              - Thermal shape model.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE`
              - Mode for computing 13-month average F10.7.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_MATERIAL`
              - Material.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE`
              - Models that are to be included when modeling radiation.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL`
              - Dose channel.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY`
              - Detector geometry.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE`
              - Detector material.

            * - :pyclass:`~VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE`
              - Mode for computing 15 day average Ap.

            * - :pyclass:`~NOTIFICATION_FILTER_MASK`
              - The notification flags are used to enable/disable STK Object Model event notifications.



Description
-----------

The following is an overview of the classes, interfaces and enumerations of the STK Object Model.

Detail
------

.. py:currentmodule:: ansys.stk.core.stkobjects


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🖿 aviator<aviator>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    🗎 astrogator<astrogator>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> IDataProviderResult<IDataProviderResult>
    --> IDataProviderTimeVarying<IDataProviderTimeVarying>
    --> IDataProviderInterval<IDataProviderInterval>
    --> IDataProviderFixed<IDataProviderFixed>
    --> IDataProviderResultStatistics<IDataProviderResultStatistics>
    --> IDataProviderInfo<IDataProviderInfo>
    --> IDataProviderCollection<IDataProviderCollection>
    --> IDataProviderResultDataSet<IDataProviderResultDataSet>
    --> IDataProviderResultDataSetCollection<IDataProviderResultDataSetCollection>
    --> IDataProviderResultInterval<IDataProviderResultInterval>
    --> IDataProviderResultIntervalCollection<IDataProviderResultIntervalCollection>
    --> IDataProviderResultSubSection<IDataProviderResultSubSection>
    --> IDataProviderResultSubSectionCollection<IDataProviderResultSubSectionCollection>
    --> IDataProviderResultTextMessage<IDataProviderResultTextMessage>
    --> IDataProviderElement<IDataProviderElement>
    --> IDataProviderElements<IDataProviderElements>
    --> IDataProviderResultTimeArrayElements<IDataProviderResultTimeArrayElements>
    --> IDataProvider<IDataProvider>
    --> IDataProviders<IDataProviders>
    --> IDataProviderGroup<IDataProviderGroup>
    --> IDataProviderResultStatisticResult<IDataProviderResultStatisticResult>
    --> IDataProviderResultTimeVaryingExtremumResult<IDataProviderResultTimeVaryingExtremumResult>
    --> IGraphics3DDataDisplayCollection<IGraphics3DDataDisplayCollection>
    --> IIntervalCollection<IIntervalCollection>
    --> ITimePeriodValue<ITimePeriodValue>
    --> IStkObject<IStkObject>
    --> IAccessInterval<IAccessInterval>
    --> IAccessTimeEventIntervals<IAccessTimeEventIntervals>
    --> IAccessTimePeriod<IAccessTimePeriod>
    --> IStkAccessGraphics<IStkAccessGraphics>
    --> IStkAccessAdvanced<IStkAccessAdvanced>
    --> IStkAccess<IStkAccess>
    --> IAccessConstraintCollection<IAccessConstraintCollection>
    --> IImmutableIntervalCollection<IImmutableIntervalCollection>
    --> IFigureOfMeritDefinition<IFigureOfMeritDefinition>
    --> IFigureOfMeritDefinitionCompute<IFigureOfMeritDefinitionCompute>
    --> IFigureOfMeritDefinitionAccessConstraint<IFigureOfMeritDefinitionAccessConstraint>
    --> IFigureOfMeritGraphics<IFigureOfMeritGraphics>
    --> ICoverageAssetListCollection<ICoverageAssetListCollection>
    --> IAvailableFeatures<IAvailableFeatures>
    --> IStkCentralBodyCollection<IStkCentralBodyCollection>
    --> IStkPreferences<IStkPreferences>
    --> IOnePointAccessConstraint<IOnePointAccessConstraint>
    --> IOnePointAccessConstraintCollection<IOnePointAccessConstraintCollection>
    --> IOnePointAccessResult<IOnePointAccessResult>
    --> IOnePointAccessResultCollection<IOnePointAccessResultCollection>
    --> IOnePointAccess<IOnePointAccess>
    --> IKeyValueCollection<IKeyValueCollection>
    --> IStkObjectElementCollection<IStkObjectElementCollection>
    --> IStkObjectCollection<IStkObjectCollection>
    --> IObjectCoverageFigureOfMerit<IObjectCoverageFigureOfMerit>
    --> IStkObjectCoverage<IStkObjectCoverage>
    --> IStdMilitary2525bSymbols<IStdMilitary2525bSymbols>
    --> IStkObjectRoot<IStkObjectRoot>
    --> IObjectLink<IObjectLink>
    --> ILinkToObject<ILinkToObject>
    --> IObjectLinkCollection<IObjectLinkCollection>
    --> IAnimation<IAnimation>
    --> IStkObjectModelContext<IStkObjectModelContext>
    --> IComponentInfo<IComponentInfo>
    --> IComponentInfoCollection<IComponentInfoCollection>
    --> IComponentDirectory<IComponentDirectory>
    --> ICloneable<ICloneable>
    --> IComponentLinkEmbedControl<IComponentLinkEmbedControl>
    --> ISwath<ISwath>
    --> IDisplayTimesData<IDisplayTimesData>
    --> IDisplayTime<IDisplayTime>
    --> IBasicAzElMask<IBasicAzElMask>
    --> ILabelNote<ILabelNote>
    --> ILabelNoteCollection<ILabelNoteCollection>
    --> IDuringAccess<IDuringAccess>
    --> IDisplayTimesTimeComponent<IDisplayTimesTimeComponent>
    --> ITerrainNormSlopeAzimuth<ITerrainNormSlopeAzimuth>
    --> IAccessTime<IAccessTime>
    --> IAccessTimeCollection<IAccessTimeCollection>
    --> ITerrainNormData<ITerrainNormData>
    --> ILifetimeInformation<ILifetimeInformation>
    --> IVehicleLeadTrailData<IVehicleLeadTrailData>
    --> IVehicleLeadTrailDataFraction<IVehicleLeadTrailDataFraction>
    --> IVehicleLeadTrailDataTime<IVehicleLeadTrailDataTime>
    --> IStkCentralBodyEllipsoid<IStkCentralBodyEllipsoid>
    --> IStkCentralBody<IStkCentralBody>
    --> IAccessConstraint<IAccessConstraint>
    --> IAccessConstraintTimeSlipRange<IAccessConstraintTimeSlipRange>
    --> IAccessConstraintZone<IAccessConstraintZone>
    --> IAccessConstraintExclZonesCollection<IAccessConstraintExclZonesCollection>
    --> IAccessConstraintThirdBody<IAccessConstraintThirdBody>
    --> IAccessConstraintIntervals<IAccessConstraintIntervals>
    --> IAccessConstraintObjExAngle<IAccessConstraintObjExAngle>
    --> IAccessConstraintCondition<IAccessConstraintCondition>
    --> IAccessConstraintCentralBodyObstruction<IAccessConstraintCentralBodyObstruction>
    --> IAccessConstraintAngle<IAccessConstraintAngle>
    --> IAccessConstraintMinMax<IAccessConstraintMinMax>
    --> IAccessConstraintPluginMinMax<IAccessConstraintPluginMinMax>
    --> IAccessConstraintCrdnConstellation<IAccessConstraintCrdnConstellation>
    --> IAccessConstraintBackground<IAccessConstraintBackground>
    --> IAccessConstraintGroundTrack<IAccessConstraintGroundTrack>
    --> IAccessConstraintAnalysisWorkbench<IAccessConstraintAnalysisWorkbench>
    --> IAccessConstraintAnalysisWorkbenchCollection<IAccessConstraintAnalysisWorkbenchCollection>
    --> IAccessConstraintGrazingAltitude<IAccessConstraintGrazingAltitude>
    --> ILevelAttribute<ILevelAttribute>
    --> ILevelAttributeCollection<ILevelAttributeCollection>
    --> IGraphics2DRangeContours<IGraphics2DRangeContours>
    --> IGraphics3DModelFile<IGraphics3DModelFile>
    --> IGraphics3DArticulationFile<IGraphics3DArticulationFile>
    --> IGraphics3DModelGltfImageBased<IGraphics3DModelGltfImageBased>
    --> IVehicleEllipseDataElement<IVehicleEllipseDataElement>
    --> IVehicleEllipseDataCollection<IVehicleEllipseDataCollection>
    --> IVehicleGroundEllipseElement<IVehicleGroundEllipseElement>
    --> IVehicleGroundEllipsesCollection<IVehicleGroundEllipsesCollection>
    --> IGraphics3DDataDisplayElement<IGraphics3DDataDisplayElement>
    --> IGraphics3DPointableElementsElement<IGraphics3DPointableElementsElement>
    --> IGraphics3DPointableElementsCollection<IGraphics3DPointableElementsCollection>
    --> IGraphics3DModelPointing<IGraphics3DModelPointing>
    --> IGraphics3DLabelSwapDistance<IGraphics3DLabelSwapDistance>
    --> IGraphics3DAzElMask<IGraphics3DAzElMask>
    --> IGraphics3DBorderWall<IGraphics3DBorderWall>
    --> IGraphics3DRangeContours<IGraphics3DRangeContours>
    --> IGraphics3DOffsetLabel<IGraphics3DOffsetLabel>
    --> IGraphics3DOffsetRotate<IGraphics3DOffsetRotate>
    --> IGraphics3DOffsetTransformation<IGraphics3DOffsetTransformation>
    --> IGraphics3DOffsetAttach<IGraphics3DOffsetAttach>
    --> IGraphics3DOffset<IGraphics3DOffset>
    --> IGraphics3DMarkerData<IGraphics3DMarkerData>
    --> IGraphics3DMarkerShape<IGraphics3DMarkerShape>
    --> IGraphics3DMarkerFile<IGraphics3DMarkerFile>
    --> IGraphics3DMarker<IGraphics3DMarker>
    --> IGraphics3DModelTransformation<IGraphics3DModelTransformation>
    --> IGraphics3DModelTransformationCollection<IGraphics3DModelTransformationCollection>
    --> IGraphics3DModelArtic<IGraphics3DModelArtic>
    --> IGraphics3DDetailThreshold<IGraphics3DDetailThreshold>
    --> IGraphics3DModelItem<IGraphics3DModelItem>
    --> IGraphics3DModelCollection<IGraphics3DModelCollection>
    --> IGraphics3DModelData<IGraphics3DModelData>
    --> IGraphics3DModel<IGraphics3DModel>
    --> IPointTargetGraphics3DModel<IPointTargetGraphics3DModel>
    --> IGraphics3DReferenceAnalysisWorkbenchComponent<IGraphics3DReferenceAnalysisWorkbenchComponent>
    --> IGraphics3DReferenceVectorGeometryToolVector<IGraphics3DReferenceVectorGeometryToolVector>
    --> IGraphics3DReferenceVectorGeometryToolAxes<IGraphics3DReferenceVectorGeometryToolAxes>
    --> IGraphics3DReferenceVectorGeometryToolAngle<IGraphics3DReferenceVectorGeometryToolAngle>
    --> IGraphics3DReferenceVectorGeometryToolPoint<IGraphics3DReferenceVectorGeometryToolPoint>
    --> IGraphics3DReferenceVectorGeometryToolPlane<IGraphics3DReferenceVectorGeometryToolPlane>
    --> IGraphics3DReferenceAnalysisWorkbenchCollection<IGraphics3DReferenceAnalysisWorkbenchCollection>
    --> IGraphics3DVector<IGraphics3DVector>
    --> IGraphics3DVaporTrail<IGraphics3DVaporTrail>
    --> ILLAPosition<ILLAPosition>
    --> ILLAGeocentric<ILLAGeocentric>
    --> ILLAGeodetic<ILLAGeodetic>
    --> IOrbitStateCoordinateSystem<IOrbitStateCoordinateSystem>
    --> IOrbitStateCartesian<IOrbitStateCartesian>
    --> IClassicalSizeShape<IClassicalSizeShape>
    --> IClassicalSizeShapeAltitude<IClassicalSizeShapeAltitude>
    --> IClassicalSizeShapeMeanMotion<IClassicalSizeShapeMeanMotion>
    --> IClassicalSizeShapePeriod<IClassicalSizeShapePeriod>
    --> IClassicalSizeShapeRadius<IClassicalSizeShapeRadius>
    --> IClassicalSizeShapeSemimajorAxis<IClassicalSizeShapeSemimajorAxis>
    --> IOrientationAscNode<IOrientationAscNode>
    --> IOrientationAscNodeLAN<IOrientationAscNodeLAN>
    --> IOrientationAscNodeRAAN<IOrientationAscNodeRAAN>
    --> IClassicalOrientation<IClassicalOrientation>
    --> IClassicalLocation<IClassicalLocation>
    --> IClassicalLocationArgumentOfLatitude<IClassicalLocationArgumentOfLatitude>
    --> IClassicalLocationEccentricAnomaly<IClassicalLocationEccentricAnomaly>
    --> IClassicalLocationMeanAnomaly<IClassicalLocationMeanAnomaly>
    --> IClassicalLocationTimePastAN<IClassicalLocationTimePastAN>
    --> IClassicalLocationTimePastPerigee<IClassicalLocationTimePastPerigee>
    --> IClassicalLocationTrueAnomaly<IClassicalLocationTrueAnomaly>
    --> IOrbitStateClassical<IOrbitStateClassical>
    --> IGeodeticSize<IGeodeticSize>
    --> IGeodeticSizeAltitude<IGeodeticSizeAltitude>
    --> IGeodeticSizeRadius<IGeodeticSizeRadius>
    --> IOrbitStateGeodetic<IOrbitStateGeodetic>
    --> IDelaunayActionVariable<IDelaunayActionVariable>
    --> IDelaunayL<IDelaunayL>
    --> IDelaunayLOverSQRTmu<IDelaunayLOverSQRTmu>
    --> IDelaunayH<IDelaunayH>
    --> IDelaunayHOverSQRTmu<IDelaunayHOverSQRTmu>
    --> IDelaunayG<IDelaunayG>
    --> IDelaunayGOverSQRTmu<IDelaunayGOverSQRTmu>
    --> IOrbitStateDelaunay<IOrbitStateDelaunay>
    --> IEquinoctialSizeShapeMeanMotion<IEquinoctialSizeShapeMeanMotion>
    --> IEquinoctialSizeShapeSemimajorAxis<IEquinoctialSizeShapeSemimajorAxis>
    --> IOrbitStateEquinoctial<IOrbitStateEquinoctial>
    --> IFlightPathAngle<IFlightPathAngle>
    --> IMixedSphericalFPAHorizontal<IMixedSphericalFPAHorizontal>
    --> IMixedSphericalFPAVertical<IMixedSphericalFPAVertical>
    --> IOrbitStateMixedSpherical<IOrbitStateMixedSpherical>
    --> ISphericalFPAHorizontal<ISphericalFPAHorizontal>
    --> ISphericalFPAVertical<ISphericalFPAVertical>
    --> IOrbitStateSpherical<IOrbitStateSpherical>
    --> ISpatialState<ISpatialState>
    --> IVehicleSpatialInfo<IVehicleSpatialInfo>
    --> IProvideSpatialInfo<IProvideSpatialInfo>
    --> IScenSpaceEnvironment<IScenSpaceEnvironment>
    --> IRadarClutterMap<IRadarClutterMap>
    --> IRadarCrossSection<IRadarCrossSection>
    --> IRFEnvironment<IRFEnvironment>
    --> ILaserEnvironment<ILaserEnvironment>
    --> IScenarioGraphics<IScenarioGraphics>
    --> IScenarioEarthData<IScenarioEarthData>
    --> IScenarioAnimationTimePeriod<IScenarioAnimationTimePeriod>
    --> IScenarioAnimation<IScenarioAnimation>
    --> ITerrain<ITerrain>
    --> ITerrainCollection<ITerrainCollection>
    --> ICentralBodyTerrainCollectionElement<ICentralBodyTerrainCollectionElement>
    --> ICentralBodyTerrainCollection<ICentralBodyTerrainCollection>
    --> ITileset3D<ITileset3D>
    --> ITilesetCollection3D<ITilesetCollection3D>
    --> IScenarioGenDatabase<IScenarioGenDatabase>
    --> IScenarioGenDatabaseCollection<IScenarioGenDatabaseCollection>
    --> IScenario3dFont<IScenario3dFont>
    --> IScenarioGraphics3D<IScenarioGraphics3D>
    --> ITimePeriod<ITimePeriod>
    --> IScenario<IScenario>
    --> ICelestialBodyInfo<ICelestialBodyInfo>
    --> ICelestialBodyCollection<ICelestialBodyCollection>
    --> IAccessAdvanced<IAccessAdvanced>
    --> ISensorAccessAdvanced<ISensorAccessAdvanced>
    --> IRefractionCoefficients<IRefractionCoefficients>
    --> IRefractionModelBase<IRefractionModelBase>
    --> IRefractionModelEffectiveRadiusMethod<IRefractionModelEffectiveRadiusMethod>
    --> IRefractionModelITURP8344<IRefractionModelITURP8344>
    --> IRefractionModelSCFMethod<IRefractionModelSCFMethod>
    --> IScheduleTime<IScheduleTime>
    --> IScheduleTimeCollection<IScheduleTimeCollection>
    --> IDisplayDistance<IDisplayDistance>
    --> ISensorProjectionDisplayDistance<ISensorProjectionDisplayDistance>
    --> ISensorProjection<ISensorProjection>
    --> ISensorGraphics<ISensorGraphics>
    --> ISensorGraphics3DPulse<ISensorGraphics3DPulse>
    --> ISensorGraphics3DOffset<ISensorGraphics3DOffset>
    --> ISensorGraphics3DProjectionElement<ISensorGraphics3DProjectionElement>
    --> ISensorGraphics3DSpaceProjectionCollection<ISensorGraphics3DSpaceProjectionCollection>
    --> ISensorGraphics3DTargetProjectionCollection<ISensorGraphics3DTargetProjectionCollection>
    --> ISensorGraphics3D<ISensorGraphics3D>
    --> ISensorPattern<ISensorPattern>
    --> ISensorSimpleConicPattern<ISensorSimpleConicPattern>
    --> ISensorSARPattern<ISensorSARPattern>
    --> ISensorRectangularPattern<ISensorRectangularPattern>
    --> ISensorHalfPowerPattern<ISensorHalfPowerPattern>
    --> ISensorCustomPattern<ISensorCustomPattern>
    --> ISensorComplexConicPattern<ISensorComplexConicPattern>
    --> ISensorEOIRRadiometricPair<ISensorEOIRRadiometricPair>
    --> ISensorEOIRSensitivityCollection<ISensorEOIRSensitivityCollection>
    --> ISensorEOIRSaturationCollection<ISensorEOIRSaturationCollection>
    --> ISensorEOIRBand<ISensorEOIRBand>
    --> ISensorEOIRBandCollection<ISensorEOIRBandCollection>
    --> ISensorEOIRPattern<ISensorEOIRPattern>
    --> ISensorPointingTargetedBoresight<ISensorPointingTargetedBoresight>
    --> ISensorPointingTargetedBoresightTrack<ISensorPointingTargetedBoresightTrack>
    --> ISensorPointingTargetedBoresightFixed<ISensorPointingTargetedBoresightFixed>
    --> ISensorTarget<ISensorTarget>
    --> ISensorTargetCollection<ISensorTargetCollection>
    --> ISensorPointing<ISensorPointing>
    --> ISensorPointingTargeted<ISensorPointingTargeted>
    --> ISensorPointingSpinning<ISensorPointingSpinning>
    --> ISensorPointingGrazingAltitude<ISensorPointingGrazingAltitude>
    --> ISensorPointingFixedAxes<ISensorPointingFixedAxes>
    --> ISensorPointingFixed<ISensorPointingFixed>
    --> ISensorPointingExternal<ISensorPointingExternal>
    --> ISensorPointing3DModel<ISensorPointing3DModel>
    --> ISensorPointingAlongVector<ISensorPointingAlongVector>
    --> ISensorPointingSchedule<ISensorPointingSchedule>
    --> IAzElMaskData<IAzElMaskData>
    --> ISensorAzElMaskFile<ISensorAzElMaskFile>
    --> ISensorCommonTasks<ISensorCommonTasks>
    --> ILocationVectorGeometryToolPoint<ILocationVectorGeometryToolPoint>
    --> ISensor<ISensor>
    --> ISensorProjectionConstantAltitude<ISensorProjectionConstantAltitude>
    --> ISensorProjectionObjectAltitude<ISensorProjectionObjectAltitude>
    --> IAtmosphere<IAtmosphere>
    --> IRadarClutterMapInheritable<IRadarClutterMapInheritable>
    --> IRadarCrossSectionInheritable<IRadarCrossSectionInheritable>
    --> IPlatformLaserEnvironment<IPlatformLaserEnvironment>
    --> IPlatformRFEnvironment<IPlatformRFEnvironment>
    --> IRadarCrossSectionGraphics3D<IRadarCrossSectionGraphics3D>
    --> IRadarCrossSectionGraphics<IRadarCrossSectionGraphics>
    --> ITargetGraphics<ITargetGraphics>
    --> ITargetGraphics3D<ITargetGraphics3D>
    --> ITarget<ITarget>
    --> IAreaTypeEllipse<IAreaTypeEllipse>
    --> IAreaTypePatternCollection<IAreaTypePatternCollection>
    --> IAreaTargetCommonTasks<IAreaTargetCommonTasks>
    --> IAreaTypeData<IAreaTypeData>
    --> IAreaTargetGraphics<IAreaTargetGraphics>
    --> IAreaTargetGraphics3D<IAreaTargetGraphics3D>
    --> IAreaTarget<IAreaTarget>
    --> IAreaTypePattern<IAreaTypePattern>
    --> IPlanetPositionFile<IPlanetPositionFile>
    --> IPlanetPositionCentralBody<IPlanetPositionCentralBody>
    --> IPlanetCommonTasks<IPlanetCommonTasks>
    --> IPositionSourceData<IPositionSourceData>
    --> IOrbitDisplayData<IOrbitDisplayData>
    --> IPlanetOrbitDisplayTime<IPlanetOrbitDisplayTime>
    --> IPlanetGraphics<IPlanetGraphics>
    --> IPlanetGraphics3D<IPlanetGraphics3D>
    --> IPlanet<IPlanet>
    --> IStarGraphics<IStarGraphics>
    --> IStarGraphics3D<IStarGraphics3D>
    --> IStar<IStar>
    --> IFacilityGraphics<IFacilityGraphics>
    --> IFacilityGraphics3D<IFacilityGraphics3D>
    --> IFacility<IFacility>
    --> IPlaceGraphics<IPlaceGraphics>
    --> IPlaceGraphics3D<IPlaceGraphics3D>
    --> IPlace<IPlace>
    --> IAntennaNoiseTemperature<IAntennaNoiseTemperature>
    --> ISystemNoiseTemperature<ISystemNoiseTemperature>
    --> IPolarization<IPolarization>
    --> IPolarizationElliptical<IPolarizationElliptical>
    --> IPolarizationCrossPolLeakage<IPolarizationCrossPolLeakage>
    --> IPolarizationLinear<IPolarizationLinear>
    --> IPolarizationHorizontal<IPolarizationHorizontal>
    --> IPolarizationVertical<IPolarizationVertical>
    --> IAdditionalGainLoss<IAdditionalGainLoss>
    --> IAdditionalGainLossCollection<IAdditionalGainLossCollection>
    --> ICRPluginConfiguration<ICRPluginConfiguration>
    --> ICRComplex<ICRComplex>
    --> ICRComplexCollection<ICRComplexCollection>
    --> ICRLocation<ICRLocation>
    --> IPointingStrategy<IPointingStrategy>
    --> IPointingStrategyFixed<IPointingStrategyFixed>
    --> IPointingStrategySpinning<IPointingStrategySpinning>
    --> IPointingStrategyTargeted<IPointingStrategyTargeted>
    --> IWaveformPulseDefinition<IWaveformPulseDefinition>
    --> IWaveform<IWaveform>
    --> IWaveformRectangular<IWaveformRectangular>
    --> IWaveformSelectionStrategy<IWaveformSelectionStrategy>
    --> IWaveformSelectionStrategyFixed<IWaveformSelectionStrategyFixed>
    --> IWaveformSelectionStrategyRangeLimits<IWaveformSelectionStrategyRangeLimits>
    --> IRFInterference<IRFInterference>
    --> IScatteringPointProvider<IScatteringPointProvider>
    --> IScatteringPointProviderSinglePoint<IScatteringPointProviderSinglePoint>
    --> IScatteringPointCollectionElement<IScatteringPointCollectionElement>
    --> IScatteringPointCollection<IScatteringPointCollection>
    --> IScatteringPointProviderPointsFile<IScatteringPointProviderPointsFile>
    --> IScatteringPointProviderRangeOverCFARCells<IScatteringPointProviderRangeOverCFARCells>
    --> IScatteringPointProviderSmoothOblateEarth<IScatteringPointProviderSmoothOblateEarth>
    --> IScatteringPointProviderPlugin<IScatteringPointProviderPlugin>
    --> IScatteringPointModel<IScatteringPointModel>
    --> IScatteringPointModelConstantCoefficient<IScatteringPointModelConstantCoefficient>
    --> IScatteringPointModelWindTurbine<IScatteringPointModelWindTurbine>
    --> IScatteringPointModelPlugin<IScatteringPointModelPlugin>
    --> IScatteringPointProviderCollectionElement<IScatteringPointProviderCollectionElement>
    --> IScatteringPointProviderCollection<IScatteringPointProviderCollection>
    --> IScatteringPointProviderList<IScatteringPointProviderList>
    --> IObjectRFEnvironment<IObjectRFEnvironment>
    --> IObjectLaserEnvironment<IObjectLaserEnvironment>
    --> IAntennaModel<IAntennaModel>
    --> IAntennaModelGaussian<IAntennaModelGaussian>
    --> IAntennaModelParabolic<IAntennaModelParabolic>
    --> IAntennaModelSquareHorn<IAntennaModelSquareHorn>
    --> IAntennaModelScriptPlugin<IAntennaModelScriptPlugin>
    --> IAntennaModelExternal<IAntennaModelExternal>
    --> IAntennaModelGimroc<IAntennaModelGimroc>
    --> IAntennaModelRemcomUanFormat<IAntennaModelRemcomUanFormat>
    --> IAntennaModelANSYSffdFormat<IAntennaModelANSYSffdFormat>
    --> IAntennaModelTicraGRASPFormat<IAntennaModelTicraGRASPFormat>
    --> IAntennaModelElevationAzimuthCuts<IAntennaModelElevationAzimuthCuts>
    --> IAntennaModelIeee1979<IAntennaModelIeee1979>
    --> IAntennaModelDipole<IAntennaModelDipole>
    --> IAntennaModelHelix<IAntennaModelHelix>
    --> IAntennaModelCosecantSquared<IAntennaModelCosecantSquared>
    --> IAntennaModelHemispherical<IAntennaModelHemispherical>
    --> IAntennaModelPencilBeam<IAntennaModelPencilBeam>
    --> IElementConfiguration<IElementConfiguration>
    --> IElementConfigurationCircular<IElementConfigurationCircular>
    --> IElementConfigurationLinear<IElementConfigurationLinear>
    --> IElementConfigurationAsciiFile<IElementConfigurationAsciiFile>
    --> IElementConfigurationHfssEepFile<IElementConfigurationHfssEepFile>
    --> IElementConfigurationPolygon<IElementConfigurationPolygon>
    --> IBeamformer<IBeamformer>
    --> IBeamformerMvdr<IBeamformerMvdr>
    --> IBeamformerUniform<IBeamformerUniform>
    --> IBeamformerAsciiFile<IBeamformerAsciiFile>
    --> IBeamformerScript<IBeamformerScript>
    --> IBeamformerBlackmanHarris<IBeamformerBlackmanHarris>
    --> IBeamformerCosine<IBeamformerCosine>
    --> IBeamformerCosineX<IBeamformerCosineX>
    --> IBeamformerCustomTaperFile<IBeamformerCustomTaperFile>
    --> IBeamformerDolphChebyshev<IBeamformerDolphChebyshev>
    --> IBeamformerHamming<IBeamformerHamming>
    --> IBeamformerHann<IBeamformerHann>
    --> IBeamformerRaisedCosine<IBeamformerRaisedCosine>
    --> IBeamformerRaisedCosineSquared<IBeamformerRaisedCosineSquared>
    --> IDirectionProvider<IDirectionProvider>
    --> IDirectionProviderAsciiFile<IDirectionProviderAsciiFile>
    --> IDirectionProviderObject<IDirectionProviderObject>
    --> IDirectionProviderLink<IDirectionProviderLink>
    --> IDirectionProviderScript<IDirectionProviderScript>
    --> IElement<IElement>
    --> IElementCollection<IElementCollection>
    --> IAntennaModelPhasedArray<IAntennaModelPhasedArray>
    --> IAntennaModelHfssEepArray<IAntennaModelHfssEepArray>
    --> IAntennaModelIsotropic<IAntennaModelIsotropic>
    --> IAntennaModelIntelSat<IAntennaModelIntelSat>
    --> IAntennaModelOpticalSimple<IAntennaModelOpticalSimple>
    --> IAntennaModelRectangularPattern<IAntennaModelRectangularPattern>
    --> IAntennaModelGpsGlobal<IAntennaModelGpsGlobal>
    --> IAntennaModelGpsFrpa<IAntennaModelGpsFrpa>
    --> IAntennaModelItuBO1213CoPolar<IAntennaModelItuBO1213CoPolar>
    --> IAntennaModelItuBO1213CrossPolar<IAntennaModelItuBO1213CrossPolar>
    --> IAntennaModelItuF1245<IAntennaModelItuF1245>
    --> IAntennaModelItuS580<IAntennaModelItuS580>
    --> IAntennaModelItuS465<IAntennaModelItuS465>
    --> IAntennaModelItuS731<IAntennaModelItuS731>
    --> IAntennaModelItuS1528R12Circular<IAntennaModelItuS1528R12Circular>
    --> IAntennaModelItuS1528R13<IAntennaModelItuS1528R13>
    --> IAntennaModelItuS672Circular<IAntennaModelItuS672Circular>
    --> IAntennaModelItuS1528R12Rectangular<IAntennaModelItuS1528R12Rectangular>
    --> IAntennaModelItuS672Rectangular<IAntennaModelItuS672Rectangular>
    --> IAntennaModelApertureCircularCosine<IAntennaModelApertureCircularCosine>
    --> IAntennaModelApertureCircularUniform<IAntennaModelApertureCircularUniform>
    --> IAntennaModelApertureCircularCosineSquared<IAntennaModelApertureCircularCosineSquared>
    --> IAntennaModelApertureCircularBessel<IAntennaModelApertureCircularBessel>
    --> IAntennaModelApertureCircularBesselEnvelope<IAntennaModelApertureCircularBesselEnvelope>
    --> IAntennaModelApertureCircularCosinePedestal<IAntennaModelApertureCircularCosinePedestal>
    --> IAntennaModelApertureCircularCosineSquaredPedestal<IAntennaModelApertureCircularCosineSquaredPedestal>
    --> IAntennaModelApertureCircularSincIntPower<IAntennaModelApertureCircularSincIntPower>
    --> IAntennaModelApertureCircularSincRealPower<IAntennaModelApertureCircularSincRealPower>
    --> IAntennaModelApertureRectangularUniform<IAntennaModelApertureRectangularUniform>
    --> IAntennaModelApertureRectangularCosineSquared<IAntennaModelApertureRectangularCosineSquared>
    --> IAntennaModelApertureRectangularCosine<IAntennaModelApertureRectangularCosine>
    --> IAntennaModelApertureRectangularCosinePedestal<IAntennaModelApertureRectangularCosinePedestal>
    --> IAntennaModelApertureRectangularCosineSquaredPedestal<IAntennaModelApertureRectangularCosineSquaredPedestal>
    --> IAntennaModelApertureRectangularSincIntPower<IAntennaModelApertureRectangularSincIntPower>
    --> IAntennaModelApertureRectangularSincRealPower<IAntennaModelApertureRectangularSincRealPower>
    --> IAntennaVolumeLevel<IAntennaVolumeLevel>
    --> IAntennaVolumeLevelCollection<IAntennaVolumeLevelCollection>
    --> IAntennaVolumeGraphics<IAntennaVolumeGraphics>
    --> IAntennaGraphics3D<IAntennaGraphics3D>
    --> IAntennaContourLevel<IAntennaContourLevel>
    --> IAntennaContourLevelCollection<IAntennaContourLevelCollection>
    --> IAntennaContour<IAntennaContour>
    --> IAntennaContourGain<IAntennaContourGain>
    --> IAntennaContourEirp<IAntennaContourEirp>
    --> IAntennaContourRip<IAntennaContourRip>
    --> IAntennaContourFluxDensity<IAntennaContourFluxDensity>
    --> IAntennaContourSpectralFluxDensity<IAntennaContourSpectralFluxDensity>
    --> IAntennaContourGraphics<IAntennaContourGraphics>
    --> IAntennaGraphics<IAntennaGraphics>
    --> IAntenna<IAntenna>
    --> IAntennaControl<IAntennaControl>
    --> IAntennaBeamSelectionStrategy<IAntennaBeamSelectionStrategy>
    --> IAntennaBeamSelectionStrategyScriptPlugin<IAntennaBeamSelectionStrategyScriptPlugin>
    --> IAntennaBeam<IAntennaBeam>
    --> IAntennaBeamTransmit<IAntennaBeamTransmit>
    --> IAntennaBeamCollection<IAntennaBeamCollection>
    --> IAntennaSystem<IAntennaSystem>
    --> IRFFilterModel<IRFFilterModel>
    --> IModulatorModel<IModulatorModel>
    --> ITransmitterModel<ITransmitterModel>
    --> ITransmitterModelScriptPlugin<ITransmitterModelScriptPlugin>
    --> ITransmitterModelCable<ITransmitterModelCable>
    --> ITransmitterModelSimple<ITransmitterModelSimple>
    --> ITransmitterModelMedium<ITransmitterModelMedium>
    --> ITransmitterModelComplex<ITransmitterModelComplex>
    --> ITransmitterModelMultibeam<ITransmitterModelMultibeam>
    --> ITransmitterModelLaser<ITransmitterModelLaser>
    --> ITransferFunctionInputBackOffCOverImTableRow<ITransferFunctionInputBackOffCOverImTableRow>
    --> ITransferFunctionInputBackOffCOverImTable<ITransferFunctionInputBackOffCOverImTable>
    --> ITransferFunctionInputBackOffOutputBackOffTableRow<ITransferFunctionInputBackOffOutputBackOffTableRow>
    --> ITransferFunctionInputBackOffOutputBackOffTable<ITransferFunctionInputBackOffOutputBackOffTable>
    --> ITransferFunctionPolynomialCollection<ITransferFunctionPolynomialCollection>
    --> IReTransmitterModel<IReTransmitterModel>
    --> IReTransmitterModelSimple<IReTransmitterModelSimple>
    --> IReTransmitterModelMedium<IReTransmitterModelMedium>
    --> IReTransmitterModelComplex<IReTransmitterModelComplex>
    --> ITransmitterGraphics3D<ITransmitterGraphics3D>
    --> ITransmitterGraphics<ITransmitterGraphics>
    --> ITransmitter<ITransmitter>
    --> IDemodulatorModel<IDemodulatorModel>
    --> ILaserPropagationLossModels<ILaserPropagationLossModels>
    --> ILinkMargin<ILinkMargin>
    --> IReceiverModel<IReceiverModel>
    --> IReceiverModelSimple<IReceiverModelSimple>
    --> IReceiverModelMedium<IReceiverModelMedium>
    --> IReceiverModelComplex<IReceiverModelComplex>
    --> IReceiverModelMultibeam<IReceiverModelMultibeam>
    --> IReceiverModelLaser<IReceiverModelLaser>
    --> IReceiverModelScriptPlugin<IReceiverModelScriptPlugin>
    --> IReceiverModelScriptPluginRF<IReceiverModelScriptPluginRF>
    --> IReceiverModelCable<IReceiverModelCable>
    --> IReceiverGraphics3D<IReceiverGraphics3D>
    --> IReceiverGraphics<IReceiverGraphics>
    --> IReceiver<IReceiver>
    --> IRadarActivity<IRadarActivity>
    --> IRadarActivityTimeComponentListElement<IRadarActivityTimeComponentListElement>
    --> IRadarActivityTimeComponentListCollection<IRadarActivityTimeComponentListCollection>
    --> IRadarActivityTimeComponentList<IRadarActivityTimeComponentList>
    --> IRadarActivityTimeIntervalListElement<IRadarActivityTimeIntervalListElement>
    --> IRadarActivityTimeIntervalListCollection<IRadarActivityTimeIntervalListCollection>
    --> IRadarActivityTimeIntervalList<IRadarActivityTimeIntervalList>
    --> IRadarStcAttenuation<IRadarStcAttenuation>
    --> IRadarStcAttenuationDecayFactor<IRadarStcAttenuationDecayFactor>
    --> IRadarStcAttenuationDecaySlope<IRadarStcAttenuationDecaySlope>
    --> IRadarStcAttenuationMap<IRadarStcAttenuationMap>
    --> IRadarJamming<IRadarJamming>
    --> IRadarClutterGeometryModel<IRadarClutterGeometryModel>
    --> IRadarClutterGeometryModelPlugin<IRadarClutterGeometryModelPlugin>
    --> IRadarClutter<IRadarClutter>
    --> IRadarClutterGeometry<IRadarClutterGeometry>
    --> IRadarTransmitter<IRadarTransmitter>
    --> IRadarTransmitterMultifunction<IRadarTransmitterMultifunction>
    --> IRadarReceiver<IRadarReceiver>
    --> IRadarContinuousWaveAnalysisMode<IRadarContinuousWaveAnalysisMode>
    --> IRadarContinuousWaveAnalysisModeGoalSNR<IRadarContinuousWaveAnalysisModeGoalSNR>
    --> IRadarContinuousWaveAnalysisModeFixedTime<IRadarContinuousWaveAnalysisModeFixedTime>
    --> IRadarPulseIntegration<IRadarPulseIntegration>
    --> IRadarPulseIntegrationGoalSNR<IRadarPulseIntegrationGoalSNR>
    --> IRadarPulseIntegrationFixedNumberOfPulses<IRadarPulseIntegrationFixedNumberOfPulses>
    --> IRadarWaveformSearchTrack<IRadarWaveformSearchTrack>
    --> IRadarWaveformSearchTrackPulseDefinition<IRadarWaveformSearchTrackPulseDefinition>
    --> IRadarWaveformSarPulseDefinition<IRadarWaveformSarPulseDefinition>
    --> IRadarWaveformSarPulseIntegration<IRadarWaveformSarPulseIntegration>
    --> IRadarModulator<IRadarModulator>
    --> IRadarProbabilityOfDetection<IRadarProbabilityOfDetection>
    --> IRadarProbabilityOfDetectionPlugin<IRadarProbabilityOfDetectionPlugin>
    --> IRadarProbabilityOfDetectionNonCFAR<IRadarProbabilityOfDetectionNonCFAR>
    --> IRadarProbabilityOfDetectionCFAR<IRadarProbabilityOfDetectionCFAR>
    --> IRadarWaveformMonostaticSearchTrackContinuous<IRadarWaveformMonostaticSearchTrackContinuous>
    --> IRadarMultifunctionDetectionProcessing<IRadarMultifunctionDetectionProcessing>
    --> IRadarWaveformMonostaticSearchTrackFixedPRF<IRadarWaveformMonostaticSearchTrackFixedPRF>
    --> IRadarWaveformBistaticTransmitterSearchTrackContinuous<IRadarWaveformBistaticTransmitterSearchTrackContinuous>
    --> IRadarWaveformBistaticTransmitterSearchTrackFixedPRF<IRadarWaveformBistaticTransmitterSearchTrackFixedPRF>
    --> IRadarWaveformBistaticReceiverSearchTrackContinuous<IRadarWaveformBistaticReceiverSearchTrackContinuous>
    --> IRadarWaveformBistaticReceiverSearchTrackFixedPRF<IRadarWaveformBistaticReceiverSearchTrackFixedPRF>
    --> IRadarDopplerClutterFilters<IRadarDopplerClutterFilters>
    --> IRadarModel<IRadarModel>
    --> IRadarModeMonostatic<IRadarModeMonostatic>
    --> IRadarModeMonostaticSearchTrack<IRadarModeMonostaticSearchTrack>
    --> IRadarModeMonostaticSar<IRadarModeMonostaticSar>
    --> IRadarModelMonostatic<IRadarModelMonostatic>
    --> IRadarAntennaBeam<IRadarAntennaBeam>
    --> IRadarAntennaBeamCollection<IRadarAntennaBeamCollection>
    --> IRadarMultifunctionWaveformStrategySettings<IRadarMultifunctionWaveformStrategySettings>
    --> IRadarModelMultifunction<IRadarModelMultifunction>
    --> IRadarModeBistaticTransmitter<IRadarModeBistaticTransmitter>
    --> IRadarModeBistaticTransmitterSearchTrack<IRadarModeBistaticTransmitterSearchTrack>
    --> IRadarModeBistaticTransmitterSar<IRadarModeBistaticTransmitterSar>
    --> IRadarModelBistaticTransmitter<IRadarModelBistaticTransmitter>
    --> IRadarModeBistaticReceiver<IRadarModeBistaticReceiver>
    --> IRadarModeBistaticReceiverSearchTrack<IRadarModeBistaticReceiverSearchTrack>
    --> IRadarModeBistaticReceiverSar<IRadarModeBistaticReceiverSar>
    --> IRadarModelBistaticReceiver<IRadarModelBistaticReceiver>
    --> IRadarGraphics3D<IRadarGraphics3D>
    --> IRadarMultipathGraphics<IRadarMultipathGraphics>
    --> IRadarAccessGraphics<IRadarAccessGraphics>
    --> IRadarGraphics<IRadarGraphics>
    --> IRadar<IRadar>
    --> IRadarClutterMapModel<IRadarClutterMapModel>
    --> IRadarClutterMapModelPlugin<IRadarClutterMapModelPlugin>
    --> IRadarClutterMapModelConstantCoefficient<IRadarClutterMapModelConstantCoefficient>
    --> IRadarCrossSectionComputeStrategy<IRadarCrossSectionComputeStrategy>
    --> IRadarCrossSectionComputeStrategyConstantValue<IRadarCrossSectionComputeStrategyConstantValue>
    --> IRadarCrossSectionComputeStrategyScriptPlugin<IRadarCrossSectionComputeStrategyScriptPlugin>
    --> IRadarCrossSectionComputeStrategyExternalFile<IRadarCrossSectionComputeStrategyExternalFile>
    --> IRadarCrossSectionComputeStrategyAnsysCsvFile<IRadarCrossSectionComputeStrategyAnsysCsvFile>
    --> IRadarCrossSectionComputeStrategyPlugin<IRadarCrossSectionComputeStrategyPlugin>
    --> IRadarCrossSectionFrequencyBand<IRadarCrossSectionFrequencyBand>
    --> IRadarCrossSectionFrequencyBandCollection<IRadarCrossSectionFrequencyBandCollection>
    --> IRadarCrossSectionModel<IRadarCrossSectionModel>
    --> IRadarStcAttenuationPlugin<IRadarStcAttenuationPlugin>
    --> IRadarCrossSectionVolumeLevel<IRadarCrossSectionVolumeLevel>
    --> IRadarCrossSectionVolumeLevelCollection<IRadarCrossSectionVolumeLevelCollection>
    --> IRadarCrossSectionVolumeGraphics<IRadarCrossSectionVolumeGraphics>
    --> IRadarCrossSectionContourLevel<IRadarCrossSectionContourLevel>
    --> IRadarCrossSectionContourLevelCollection<IRadarCrossSectionContourLevelCollection>
    --> IRFFilterModelBessel<IRFFilterModelBessel>
    --> IRFFilterModelButterworth<IRFFilterModelButterworth>
    --> IRFFilterModelSincEnvSinc<IRFFilterModelSincEnvSinc>
    --> IRFFilterModelElliptic<IRFFilterModelElliptic>
    --> IRFFilterModelChebyshev<IRFFilterModelChebyshev>
    --> IRFFilterModelCosineWindow<IRFFilterModelCosineWindow>
    --> IRFFilterModelGaussianWindow<IRFFilterModelGaussianWindow>
    --> IRFFilterModelHammingWindow<IRFFilterModelHammingWindow>
    --> IRFFilterModelExternal<IRFFilterModelExternal>
    --> IRFFilterModelScriptPlugin<IRFFilterModelScriptPlugin>
    --> IRFFilterModelSinc<IRFFilterModelSinc>
    --> IRFFilterModelRaisedCosine<IRFFilterModelRaisedCosine>
    --> IRFFilterModelRootRaisedCosine<IRFFilterModelRootRaisedCosine>
    --> IRFFilterModelRcLowPass<IRFFilterModelRcLowPass>
    --> IRFFilterModelFirBoxCar<IRFFilterModelFirBoxCar>
    --> IRFFilterModelFir<IRFFilterModelFir>
    --> IRFFilterModelIir<IRFFilterModelIir>
    --> IModulatorModelExternal<IModulatorModelExternal>
    --> IModulatorModelBoc<IModulatorModelBoc>
    --> IModulatorModelPulsedSignal<IModulatorModelPulsedSignal>
    --> IModulatorModelScriptPlugin<IModulatorModelScriptPlugin>
    --> IDemodulatorModelExternal<IDemodulatorModelExternal>
    --> IDemodulatorModelScriptPlugin<IDemodulatorModelScriptPlugin>
    --> IRainLossModelScriptPlugin<IRainLossModelScriptPlugin>
    --> IRainLossModel<IRainLossModel>
    --> IRainLossModelCrane1985<IRainLossModelCrane1985>
    --> IRainLossModelCrane1982<IRainLossModelCrane1982>
    --> IRainLossModelCCIR1983<IRainLossModelCCIR1983>
    --> IRainLossModelITURP618_10<IRainLossModelITURP618_10>
    --> IRainLossModelITURP618_12<IRainLossModelITURP618_12>
    --> IRainLossModelITURP618_13<IRainLossModelITURP618_13>
    --> IUrbanTerrestrialLossModel<IUrbanTerrestrialLossModel>
    --> IUrbanTerrestrialLossModelTwoRay<IUrbanTerrestrialLossModelTwoRay>
    --> IWirelessInSite64GeometryData<IWirelessInSite64GeometryData>
    --> IUrbanTerrestrialLossModelWirelessInSite64<IUrbanTerrestrialLossModelWirelessInSite64>
    --> ITroposphericScintillationFadingLossModel<ITroposphericScintillationFadingLossModel>
    --> ITroposphericScintillationFadingLossModelP618_8<ITroposphericScintillationFadingLossModelP618_8>
    --> ITroposphericScintillationFadingLossModelP618_12<ITroposphericScintillationFadingLossModelP618_12>
    --> IIonosphericFadingLossModel<IIonosphericFadingLossModel>
    --> IIonosphericFadingLossModelP531_13<IIonosphericFadingLossModelP531_13>
    --> ICloudsAndFogFadingLossModel<ICloudsAndFogFadingLossModel>
    --> ICloudsAndFogFadingLossModelP840_6<ICloudsAndFogFadingLossModelP840_6>
    --> ICloudsAndFogFadingLossModelP840_7<ICloudsAndFogFadingLossModelP840_7>
    --> IAtmosphericAbsorptionModel<IAtmosphericAbsorptionModel>
    --> IAtmosphericAbsorptionModelITURP676<IAtmosphericAbsorptionModelITURP676>
    --> IAtmosphericAbsorptionModelTirem<IAtmosphericAbsorptionModelTirem>
    --> ISolarActivityConfiguration<ISolarActivityConfiguration>
    --> ISolarActivityConfigurationSunspotNumber<ISolarActivityConfigurationSunspotNumber>
    --> ISolarActivityConfigurationSolarFlux<ISolarActivityConfigurationSolarFlux>
    --> IAtmosphericAbsorptionModelVoacap<IAtmosphericAbsorptionModelVoacap>
    --> IAtmosphericAbsorptionModelSimpleSatcom<IAtmosphericAbsorptionModelSimpleSatcom>
    --> IAtmosphericAbsorptionModelScriptPlugin<IAtmosphericAbsorptionModelScriptPlugin>
    --> IAtmosphericAbsorptionModelCOMPlugin<IAtmosphericAbsorptionModelCOMPlugin>
    --> ICustomPropagationModel<ICustomPropagationModel>
    --> IPropagationChannel<IPropagationChannel>
    --> IBeerBouguerLambertLawLayer<IBeerBouguerLambertLawLayer>
    --> IBeerBouguerLambertLawLayerCollection<IBeerBouguerLambertLawLayerCollection>
    --> ILaserAtmosphericLossModelBeerBouguerLambertLaw<ILaserAtmosphericLossModelBeerBouguerLambertLaw>
    --> IModtranLookupTablePropagationModel<IModtranLookupTablePropagationModel>
    --> IModtranPropagationModel<IModtranPropagationModel>
    --> ILaserAtmosphericLossModel<ILaserAtmosphericLossModel>
    --> ILaserTroposphericScintillationLossModel<ILaserTroposphericScintillationLossModel>
    --> IAtmosphericTurbulenceModel<IAtmosphericTurbulenceModel>
    --> IAtmosphericTurbulenceModelConstant<IAtmosphericTurbulenceModelConstant>
    --> IAtmosphericTurbulenceModelHufnagelValley<IAtmosphericTurbulenceModelHufnagelValley>
    --> ILaserTroposphericScintillationLossModelITURP1814<ILaserTroposphericScintillationLossModelITURP1814>
    --> ILaserPropagationChannel<ILaserPropagationChannel>
    --> ICommSystemLinkSelectionCriteria<ICommSystemLinkSelectionCriteria>
    --> ICommSystemLinkSelectionCriteriaScriptPlugin<ICommSystemLinkSelectionCriteriaScriptPlugin>
    --> ICommSystemAccessEventDetection<ICommSystemAccessEventDetection>
    --> ICommSystemAccessEventDetectionSubsample<ICommSystemAccessEventDetectionSubsample>
    --> ICommSystemAccessSamplingMethod<ICommSystemAccessSamplingMethod>
    --> ICommSystemAccessSamplingMethodFixed<ICommSystemAccessSamplingMethodFixed>
    --> ICommSystemAccessSamplingMethodAdaptive<ICommSystemAccessSamplingMethodAdaptive>
    --> ICommSystemAccessOptions<ICommSystemAccessOptions>
    --> ICommSystemGraphics<ICommSystemGraphics>
    --> ICommSystemGraphics3D<ICommSystemGraphics3D>
    --> ICommSystem<ICommSystem>
    --> ISRPModelPluginSettings<ISRPModelPluginSettings>
    --> ISRPModelBase<ISRPModelBase>
    --> ISRPModelGPS<ISRPModelGPS>
    --> ISRPModelSpherical<ISRPModelSpherical>
    --> ISRPModelPlugin<ISRPModelPlugin>
    --> IVehicleHPOPDragModelPluginSettings<IVehicleHPOPDragModelPluginSettings>
    --> IVehicleHPOPDragModel<IVehicleHPOPDragModel>
    --> IVehicleHPOPDragModelSpherical<IVehicleHPOPDragModelSpherical>
    --> IVehicleHPOPDragModelPlugin<IVehicleHPOPDragModelPlugin>
    --> IVehicleDuration<IVehicleDuration>
    --> IVehicleRealtimeCartesianPoints<IVehicleRealtimeCartesianPoints>
    --> IVehicleRealtimeLLAHPSPoints<IVehicleRealtimeLLAHPSPoints>
    --> IVehicleRealtimeLLAPoints<IVehicleRealtimeLLAPoints>
    --> IVehicleRealtimeUTMPoints<IVehicleRealtimeUTMPoints>
    --> IVehicleGPSElement<IVehicleGPSElement>
    --> IVehicleGPSElementCollection<IVehicleGPSElementCollection>
    --> IVehicleHPOPSRPModel<IVehicleHPOPSRPModel>
    --> IVehicleThirdBodyGravityElement<IVehicleThirdBodyGravityElement>
    --> IVehicleThirdBodyGravityCollection<IVehicleThirdBodyGravityCollection>
    --> IVehicleSGP4LoadData<IVehicleSGP4LoadData>
    --> IVehicleSGP4OnlineLoad<IVehicleSGP4OnlineLoad>
    --> IVehicleSGP4OnlineAutoLoad<IVehicleSGP4OnlineAutoLoad>
    --> IVehicleSGP4LoadFile<IVehicleSGP4LoadFile>
    --> IVehicleSGP4Segment<IVehicleSGP4Segment>
    --> IVehiclePropagatorSGP4CommonTasks<IVehiclePropagatorSGP4CommonTasks>
    --> IVehicleSGP4AutoUpdateProperties<IVehicleSGP4AutoUpdateProperties>
    --> IVehicleSGP4AutoUpdateFileSource<IVehicleSGP4AutoUpdateFileSource>
    --> IVehicleSGP4AutoUpdateOnlineSource<IVehicleSGP4AutoUpdateOnlineSource>
    --> IVehicleSGP4AutoUpdate<IVehicleSGP4AutoUpdate>
    --> IVehicleSGP4PropagatorSettings<IVehicleSGP4PropagatorSettings>
    --> IVehicleSGP4SegmentCollection<IVehicleSGP4SegmentCollection>
    --> IVehicleInitialState<IVehicleInitialState>
    --> IVehicleHPOPCentralBodyGravity<IVehicleHPOPCentralBodyGravity>
    --> IVehicleRadiationPressure<IVehicleRadiationPressure>
    --> IVehicleHPOPSolarRadiationPressure<IVehicleHPOPSolarRadiationPressure>
    --> IVehicleSolarFluxGeoMagnitudeEnterManually<IVehicleSolarFluxGeoMagnitudeEnterManually>
    --> IVehicleSolarFluxGeoMagnitudeUseFile<IVehicleSolarFluxGeoMagnitudeUseFile>
    --> IVehicleSolarFluxGeoMagnitude<IVehicleSolarFluxGeoMagnitude>
    --> IVehicleHPOPForceModelDrag<IVehicleHPOPForceModelDrag>
    --> IVehicleHPOPForceModelDragOptions<IVehicleHPOPForceModelDragOptions>
    --> IVehicleHPOPSolarRadiationPressureOptions<IVehicleHPOPSolarRadiationPressureOptions>
    --> IVehicleStatic<IVehicleStatic>
    --> IVehicleSolidTides<IVehicleSolidTides>
    --> IVehicleOceanTides<IVehicleOceanTides>
    --> IVehiclePluginSettings<IVehiclePluginSettings>
    --> IVehiclePluginPropagator<IVehiclePluginPropagator>
    --> IVehicleHPOPForceModelMoreOptions<IVehicleHPOPForceModelMoreOptions>
    --> IVehicleEclipsingBodies<IVehicleEclipsingBodies>
    --> IVehicleHPOPForceModel<IVehicleHPOPForceModel>
    --> IVehicleStepSizeControl<IVehicleStepSizeControl>
    --> IVehicleTimeRegularization<IVehicleTimeRegularization>
    --> IVehicleInterpolation<IVehicleInterpolation>
    --> IVehicleIntegrator<IVehicleIntegrator>
    --> IVehicleGravity<IVehicleGravity>
    --> IVehiclePositionVelocityElement<IVehiclePositionVelocityElement>
    --> IVehiclePositionVelocityCollection<IVehiclePositionVelocityCollection>
    --> IVehicleCorrelationListElement<IVehicleCorrelationListElement>
    --> IVehicleCorrelationListCollection<IVehicleCorrelationListCollection>
    --> IVehicleConsiderAnalysisCollectionElement<IVehicleConsiderAnalysisCollectionElement>
    --> IVehicleConsiderAnalysisCollection<IVehicleConsiderAnalysisCollection>
    --> IVehicleCovariance<IVehicleCovariance>
    --> IVehicleJxInitialState<IVehicleJxInitialState>
    --> IVehicleLOPCentralBodyGravity<IVehicleLOPCentralBodyGravity>
    --> IVehicleThirdBodyGravity<IVehicleThirdBodyGravity>
    --> IVehicleExpDensModelParams<IVehicleExpDensModelParams>
    --> IVehicleAdvanced<IVehicleAdvanced>
    --> IVehicleLOPForceModelDrag<IVehicleLOPForceModelDrag>
    --> IVehicleLOPSolarRadiationPressure<IVehicleLOPSolarRadiationPressure>
    --> IVehiclePhysicalData<IVehiclePhysicalData>
    --> IVehicleLOPForceModel<IVehicleLOPForceModel>
    --> IVehicleSPICESegment<IVehicleSPICESegment>
    --> IVehicleSegmentsCollection<IVehicleSegmentsCollection>
    --> IVehiclePropagator<IVehiclePropagator>
    --> IVehiclePropagatorHPOP<IVehiclePropagatorHPOP>
    --> IVehiclePropagatorJ2Perturbation<IVehiclePropagatorJ2Perturbation>
    --> IVehiclePropagatorJ4Perturbation<IVehiclePropagatorJ4Perturbation>
    --> IVehiclePropagatorLOP<IVehiclePropagatorLOP>
    --> IVehiclePropagatorSGP4<IVehiclePropagatorSGP4>
    --> IVehiclePropagatorSPICE<IVehiclePropagatorSPICE>
    --> IVehiclePropagatorStkExternal<IVehiclePropagatorStkExternal>
    --> IVehiclePropagatorTwoBody<IVehiclePropagatorTwoBody>
    --> IVehiclePropagatorUserExternal<IVehiclePropagatorUserExternal>
    --> IVehicleLaunchVehicleInitialState<IVehicleLaunchVehicleInitialState>
    --> IVehiclePropagatorSimpleAscent<IVehiclePropagatorSimpleAscent>
    --> IVehicleWaypointAltitudeReference<IVehicleWaypointAltitudeReference>
    --> IVehicleWaypointAltitudeReferenceTerrain<IVehicleWaypointAltitudeReferenceTerrain>
    --> IVehicleWaypointsElement<IVehicleWaypointsElement>
    --> IVehicleWaypointsCollection<IVehicleWaypointsCollection>
    --> IVehiclePropagatorGreatArc<IVehiclePropagatorGreatArc>
    --> IVehiclePropagatorAviator<IVehiclePropagatorAviator>
    --> IVehicleLaunchLLA<IVehicleLaunchLLA>
    --> IVehicleLaunchLLR<IVehicleLaunchLLR>
    --> IVehicleImpactLLA<IVehicleImpactLLA>
    --> IVehicleImpactLLR<IVehicleImpactLLR>
    --> IVehicleLaunchControlFixedApogeeAltitude<IVehicleLaunchControlFixedApogeeAltitude>
    --> IVehicleLaunchControlFixedDeltaV<IVehicleLaunchControlFixedDeltaV>
    --> IVehicleLaunchControlFixedDeltaVMinEccentricity<IVehicleLaunchControlFixedDeltaVMinEccentricity>
    --> IVehicleLaunchControlFixedTimeOfFlight<IVehicleLaunchControlFixedTimeOfFlight>
    --> IVehicleImpactLocationLaunchAzEl<IVehicleImpactLocationLaunchAzEl>
    --> IVehicleImpact<IVehicleImpact>
    --> IVehicleLaunchControl<IVehicleLaunchControl>
    --> IVehicleImpactLocationPoint<IVehicleImpactLocationPoint>
    --> IVehicleLaunch<IVehicleLaunch>
    --> IVehicleImpactLocation<IVehicleImpactLocation>
    --> IVehiclePropagatorBallistic<IVehiclePropagatorBallistic>
    --> IVehicleRealtimePointBuilder<IVehicleRealtimePointBuilder>
    --> IVehiclePropagatorRealtime<IVehiclePropagatorRealtime>
    --> IVehicleGPSAlmanacProperties<IVehicleGPSAlmanacProperties>
    --> IVehicleGPSAlmanacPropertiesYUMA<IVehicleGPSAlmanacPropertiesYUMA>
    --> IVehicleGPSAlmanacPropertiesSEM<IVehicleGPSAlmanacPropertiesSEM>
    --> IVehicleGPSAlmanacPropertiesSP3<IVehicleGPSAlmanacPropertiesSP3>
    --> IVehicleGPSSpecifyAlmanac<IVehicleGPSSpecifyAlmanac>
    --> IVehicleGPSAutoUpdateProperties<IVehicleGPSAutoUpdateProperties>
    --> IVehicleGPSAutoUpdateFileSource<IVehicleGPSAutoUpdateFileSource>
    --> IVehicleGPSAutoUpdateOnlineSource<IVehicleGPSAutoUpdateOnlineSource>
    --> IVehicleGPSAutoUpdate<IVehicleGPSAutoUpdate>
    --> IVehiclePropagatorGPS<IVehiclePropagatorGPS>
    --> IVehiclePropagator11ParamDescriptor<IVehiclePropagator11ParamDescriptor>
    --> IVehiclePropagator11ParamDescriptorCollection<IVehiclePropagator11ParamDescriptorCollection>
    --> IVehiclePropagator11Param<IVehiclePropagator11Param>
    --> IVehiclePropagatorSP3File<IVehiclePropagatorSP3File>
    --> IVehiclePropagatorSP3FileCollection<IVehiclePropagatorSP3FileCollection>
    --> IVehiclePropagatorSP3<IVehiclePropagatorSP3>
    --> IVehicleTargetPointingElement<IVehicleTargetPointingElement>
    --> IVehicleAccessAdvanced<IVehicleAccessAdvanced>
    --> IVehicleAttitudeTargetSlew<IVehicleAttitudeTargetSlew>
    --> IVehicleTorque<IVehicleTorque>
    --> IVehicleIntegratedAttitude<IVehicleIntegratedAttitude>
    --> IVehicleVector<IVehicleVector>
    --> IVehicleRateOffset<IVehicleRateOffset>
    --> IVehicleAttitudeProfile<IVehicleAttitudeProfile>
    --> IVehicleProfileAlignedAndConstrained<IVehicleProfileAlignedAndConstrained>
    --> IVehicleProfileInertial<IVehicleProfileInertial>
    --> IVehicleProfileYawToNadir<IVehicleProfileYawToNadir>
    --> IVehicleProfileConstraintOffset<IVehicleProfileConstraintOffset>
    --> IVehicleProfileAlignmentOffset<IVehicleProfileAlignmentOffset>
    --> IVehicleProfileFixedInAxes<IVehicleProfileFixedInAxes>
    --> IVehicleProfilePrecessingSpin<IVehicleProfilePrecessingSpin>
    --> IVehicleProfileSpinAboutXXX<IVehicleProfileSpinAboutXXX>
    --> IVehicleProfileSpinning<IVehicleProfileSpinning>
    --> IVehicleProfileCoordinatedTurn<IVehicleProfileCoordinatedTurn>
    --> IVehicleScheduleTimesElement<IVehicleScheduleTimesElement>
    --> IVehicleScheduleTimesCollection<IVehicleScheduleTimesCollection>
    --> IVehicleTargetTimes<IVehicleTargetTimes>
    --> IVehicleTargetPointingIntervalCollection<IVehicleTargetPointingIntervalCollection>
    --> IVehicleTargetPointingCollection<IVehicleTargetPointingCollection>
    --> IVehiclePointing<IVehiclePointing>
    --> IVehicleAttitudePointing<IVehicleAttitudePointing>
    --> IVehicleStandardBasic<IVehicleStandardBasic>
    --> IVehicleAttitudeExternal<IVehicleAttitudeExternal>
    --> IVehicleAttitude<IVehicleAttitude>
    --> IVehicleAttitudeRealTimeDataReference<IVehicleAttitudeRealTimeDataReference>
    --> IVehicleAttitudeRealTime<IVehicleAttitudeRealTime>
    --> IVehicleAttitudeStandard<IVehicleAttitudeStandard>
    --> IVehicleTrajectoryAttitudeStandard<IVehicleTrajectoryAttitudeStandard>
    --> IVehicleOrbitAttitudeStandard<IVehicleOrbitAttitudeStandard>
    --> IVehicleRouteAttitudeStandard<IVehicleRouteAttitudeStandard>
    --> IVehicleProfileGPS<IVehicleProfileGPS>
    --> IVehicleAttitudeTrendControlAviator<IVehicleAttitudeTrendControlAviator>
    --> IVehicleProfileAviator<IVehicleProfileAviator>
    --> IVehicleGraphics2DIntervalsCollection<IVehicleGraphics2DIntervalsCollection>
    --> IVehicleGraphics2DWaypointMarkersElement<IVehicleGraphics2DWaypointMarkersElement>
    --> IVehicleGraphics2DWaypointMarkersCollection<IVehicleGraphics2DWaypointMarkersCollection>
    --> IVehicleGraphics2DWaypointMarker<IVehicleGraphics2DWaypointMarker>
    --> IVehicleGraphics2DPassResolution<IVehicleGraphics2DPassResolution>
    --> IVehicleGraphics2DRouteResolution<IVehicleGraphics2DRouteResolution>
    --> IVehicleGraphics2DTrajectoryResolution<IVehicleGraphics2DTrajectoryResolution>
    --> IVehicleGraphics2DElevationsElement<IVehicleGraphics2DElevationsElement>
    --> IVehicleGraphics2DElevationsCollection<IVehicleGraphics2DElevationsCollection>
    --> IVehicleGraphics2DElevContours<IVehicleGraphics2DElevContours>
    --> IVehicleGraphics2DSAA<IVehicleGraphics2DSAA>
    --> IVehicleGraphics2DPassShowPasses<IVehicleGraphics2DPassShowPasses>
    --> IVehicleGraphics2DPass<IVehicleGraphics2DPass>
    --> IVehicleGraphics2DPasses<IVehicleGraphics2DPasses>
    --> IVehicleGraphics2DTimeEventTypeLine<IVehicleGraphics2DTimeEventTypeLine>
    --> IVehicleGraphics2DTimeEventTypeMarker<IVehicleGraphics2DTimeEventTypeMarker>
    --> IVehicleGraphics2DTimeEventTypeText<IVehicleGraphics2DTimeEventTypeText>
    --> IVehicleGraphics2DTimeEventType<IVehicleGraphics2DTimeEventType>
    --> IVehicleGraphics2DTimeEventsElement<IVehicleGraphics2DTimeEventsElement>
    --> IVehicleGraphics2DTimeEventsCollection<IVehicleGraphics2DTimeEventsCollection>
    --> IVehicleGraphics2DGroundEllipsesElement<IVehicleGraphics2DGroundEllipsesElement>
    --> IVehicleGraphics2DGroundEllipsesCollection<IVehicleGraphics2DGroundEllipsesCollection>
    --> IVehicleGraphics2DLeadTrailData<IVehicleGraphics2DLeadTrailData>
    --> IVehicleGraphics2DTrajectoryPassData<IVehicleGraphics2DTrajectoryPassData>
    --> IVehicleGraphics2DOrbitPassData<IVehicleGraphics2DOrbitPassData>
    --> IVehicleGraphics2DRoutePassData<IVehicleGraphics2DRoutePassData>
    --> IVehicleGraphics2DLightingElement<IVehicleGraphics2DLightingElement>
    --> IVehicleGraphics2DLighting<IVehicleGraphics2DLighting>
    --> IVehicleGraphics2DLine<IVehicleGraphics2DLine>
    --> IVehicleGraphics2DAttributes<IVehicleGraphics2DAttributes>
    --> IVehicleGraphics2DAttributesBasic<IVehicleGraphics2DAttributesBasic>
    --> IVehicleGraphics2DAttributesDisplayState<IVehicleGraphics2DAttributesDisplayState>
    --> IVehicleGraphics2DAttributesAccess<IVehicleGraphics2DAttributesAccess>
    --> IVehicleGraphics2DAttributesTrajectory<IVehicleGraphics2DAttributesTrajectory>
    --> IVehicleGraphics2DAttributesOrbit<IVehicleGraphics2DAttributesOrbit>
    --> IVehicleGraphics2DAttributesRoute<IVehicleGraphics2DAttributesRoute>
    --> IVehicleGraphics2DAttributesRealtime<IVehicleGraphics2DAttributesRealtime>
    --> IVehicleGraphics2DElevationGroundElevation<IVehicleGraphics2DElevationGroundElevation>
    --> IVehicleGraphics2DElevationSwathHalfWidth<IVehicleGraphics2DElevationSwathHalfWidth>
    --> IVehicleGraphics2DElevationVehicleHalfAngle<IVehicleGraphics2DElevationVehicleHalfAngle>
    --> IVehicleGraphics2DElevation<IVehicleGraphics2DElevation>
    --> IVehicleGraphics2DSwath<IVehicleGraphics2DSwath>
    --> IVehicleGraphics2DInterval<IVehicleGraphics2DInterval>
    --> IVehicleGraphics2DAttributesCustom<IVehicleGraphics2DAttributesCustom>
    --> IVehicleGraphics2DTimeComponentsElement<IVehicleGraphics2DTimeComponentsElement>
    --> IVehicleGraphics2DTimeComponentsEventElement<IVehicleGraphics2DTimeComponentsEventElement>
    --> IVehicleGraphics2DTimeComponentsEventCollectionElement<IVehicleGraphics2DTimeComponentsEventCollectionElement>
    --> IVehicleGraphics2DTimeComponentsCollection<IVehicleGraphics2DTimeComponentsCollection>
    --> IVehicleGraphics2DAttributesTimeComponents<IVehicleGraphics2DAttributesTimeComponents>
    --> IVehicleTrajectoryGraphics3DModel<IVehicleTrajectoryGraphics3DModel>
    --> IVehicleRouteGraphics3DModel<IVehicleRouteGraphics3DModel>
    --> IVehicleGraphics3DLeadTrailData<IVehicleGraphics3DLeadTrailData>
    --> IVehicleGraphics3DSystemsElementBase<IVehicleGraphics3DSystemsElementBase>
    --> IVehicleGraphics3DSystemsElement<IVehicleGraphics3DSystemsElement>
    --> IVehicleGraphics3DSystemsSpecialElement<IVehicleGraphics3DSystemsSpecialElement>
    --> IVehicleGraphics3DSystemsCollection<IVehicleGraphics3DSystemsCollection>
    --> IVehicleGraphics3DDropLinePositionItem<IVehicleGraphics3DDropLinePositionItem>
    --> IVehicleGraphics3DDropLinePositionItemCollection<IVehicleGraphics3DDropLinePositionItemCollection>
    --> IVehicleGraphics3DDropLinePathItem<IVehicleGraphics3DDropLinePathItem>
    --> IVehicleGraphics3DDropLinePathItemCollection<IVehicleGraphics3DDropLinePathItemCollection>
    --> IVehicleGraphics3DOrbitDropLines<IVehicleGraphics3DOrbitDropLines>
    --> IVehicleGraphics3DRouteDropLines<IVehicleGraphics3DRouteDropLines>
    --> IVehicleGraphics3DTrajectoryDropLines<IVehicleGraphics3DTrajectoryDropLines>
    --> IVehicleGraphics3DProximityAreaObject<IVehicleGraphics3DProximityAreaObject>
    --> IVehicleGraphics3DEllipsoid<IVehicleGraphics3DEllipsoid>
    --> IVehicleGraphics3DControlBox<IVehicleGraphics3DControlBox>
    --> IVehicleGraphics3DBearingBox<IVehicleGraphics3DBearingBox>
    --> IVehicleGraphics3DBearingEllipse<IVehicleGraphics3DBearingEllipse>
    --> IVehicleGraphics3DLineOfBearing<IVehicleGraphics3DLineOfBearing>
    --> IVehicleGraphics3DGeoBox<IVehicleGraphics3DGeoBox>
    --> IVehicleGraphics3DProximity<IVehicleGraphics3DProximity>
    --> IVehicleGraphics3DRouteProximity<IVehicleGraphics3DRouteProximity>
    --> IVehicleGraphics3DOrbitProximity<IVehicleGraphics3DOrbitProximity>
    --> IVehicleGraphics3DTrajectoryProximity<IVehicleGraphics3DTrajectoryProximity>
    --> IVehicleGraphics3DElevContours<IVehicleGraphics3DElevContours>
    --> IVehicleGraphics3DSAA<IVehicleGraphics3DSAA>
    --> IVehicleGraphics3DSigmaScaleProbability<IVehicleGraphics3DSigmaScaleProbability>
    --> IVehicleGraphics3DSigmaScaleScale<IVehicleGraphics3DSigmaScaleScale>
    --> IVehicleGraphics3DDefaultAttributes<IVehicleGraphics3DDefaultAttributes>
    --> IVehicleGraphics3DIntervalsElement<IVehicleGraphics3DIntervalsElement>
    --> IVehicleGraphics3DIntervalsCollection<IVehicleGraphics3DIntervalsCollection>
    --> IVehicleGraphics3DAttributesBasic<IVehicleGraphics3DAttributesBasic>
    --> IVehicleGraphics3DAttributesIntervals<IVehicleGraphics3DAttributesIntervals>
    --> IVehicleGraphics3DSize<IVehicleGraphics3DSize>
    --> IVehicleGraphics3DSigmaScale<IVehicleGraphics3DSigmaScale>
    --> IVehicleGraphics3DAttributes<IVehicleGraphics3DAttributes>
    --> IVehicleGraphics3DCovariancePointingContour<IVehicleGraphics3DCovariancePointingContour>
    --> IVehicleGraphics3DOrbitPassData<IVehicleGraphics3DOrbitPassData>
    --> IVehicleGraphics3DTrajectoryPassData<IVehicleGraphics3DTrajectoryPassData>
    --> IVehicleGraphics3DOrbitTrackData<IVehicleGraphics3DOrbitTrackData>
    --> IVehicleGraphics3DTrajectoryTrackData<IVehicleGraphics3DTrajectoryTrackData>
    --> IVehicleGraphics3DTickData<IVehicleGraphics3DTickData>
    --> IVehicleGraphics3DPathTickMarks<IVehicleGraphics3DPathTickMarks>
    --> IVehicleGraphics3DTrajectoryTickMarks<IVehicleGraphics3DTrajectoryTickMarks>
    --> IVehicleGraphics3DTrajectory<IVehicleGraphics3DTrajectory>
    --> IVehicleGraphics3DTickDataLine<IVehicleGraphics3DTickDataLine>
    --> IVehicleGraphics3DTickDataPoint<IVehicleGraphics3DTickDataPoint>
    --> IVehicleGraphics3DOrbitTickMarks<IVehicleGraphics3DOrbitTickMarks>
    --> IVehicleGraphics3DPass<IVehicleGraphics3DPass>
    --> IVehicleGraphics3DCovariance<IVehicleGraphics3DCovariance>
    --> IVehicleGraphics3DVelCovariance<IVehicleGraphics3DVelCovariance>
    --> IVehicleGraphics3DWaypointMarkersElement<IVehicleGraphics3DWaypointMarkersElement>
    --> IVehicleGraphics3DWaypointMarkersCollection<IVehicleGraphics3DWaypointMarkersCollection>
    --> IVehicleGraphics3DRoute<IVehicleGraphics3DRoute>
    --> IVehicleEclipseBodies<IVehicleEclipseBodies>
    --> IGreatArcGraphics<IGreatArcGraphics>
    --> IGreatArcGraphics3D<IGreatArcGraphics3D>
    --> IGreatArcVehicle<IGreatArcVehicle>
    --> IVehicleGraphics3DBPlaneTemplateDisplayElement<IVehicleGraphics3DBPlaneTemplateDisplayElement>
    --> IVehicleGraphics3DBPlaneTemplateDisplayCollection<IVehicleGraphics3DBPlaneTemplateDisplayCollection>
    --> IVehicleGraphics3DBPlaneTemplate<IVehicleGraphics3DBPlaneTemplate>
    --> IVehicleGraphics3DBPlaneTemplatesCollection<IVehicleGraphics3DBPlaneTemplatesCollection>
    --> IVehicleGraphics3DBPlaneEvent<IVehicleGraphics3DBPlaneEvent>
    --> IVehicleGraphics3DBPlanePoint<IVehicleGraphics3DBPlanePoint>
    --> IVehicleGraphics3DBPlaneTargetPointPosition<IVehicleGraphics3DBPlaneTargetPointPosition>
    --> IVehicleGraphics3DBPlaneTargetPointPositionCartesian<IVehicleGraphics3DBPlaneTargetPointPositionCartesian>
    --> IVehicleGraphics3DBPlaneTargetPointPositionPolar<IVehicleGraphics3DBPlaneTargetPointPositionPolar>
    --> IVehicleGraphics3DBPlaneTargetPoint<IVehicleGraphics3DBPlaneTargetPoint>
    --> IVehicleGraphics3DBPlanePointCollection<IVehicleGraphics3DBPlanePointCollection>
    --> IVehicleGraphics3DBPlaneInstance<IVehicleGraphics3DBPlaneInstance>
    --> IVehicleGraphics3DBPlaneInstancesCollection<IVehicleGraphics3DBPlaneInstancesCollection>
    --> IVehicleGraphics3DBPlanes<IVehicleGraphics3DBPlanes>
    --> IVehicleSpaceEnvironment<IVehicleSpaceEnvironment>
    --> IEOIR<IEOIR>
    --> ISatelliteGraphics3DModel<ISatelliteGraphics3DModel>
    --> ISatelliteGraphics3D<ISatelliteGraphics3D>
    --> IVehicleCentralBodies<IVehicleCentralBodies>
    --> ISatelliteGraphics<ISatelliteGraphics>
    --> IVehicleRepeatGroundTrackNumbering<IVehicleRepeatGroundTrackNumbering>
    --> IVehicleBreakAngle<IVehicleBreakAngle>
    --> IVehicleBreakAngleBreakByLatitude<IVehicleBreakAngleBreakByLatitude>
    --> IVehicleBreakAngleBreakByLongitude<IVehicleBreakAngleBreakByLongitude>
    --> IVehicleDefinition<IVehicleDefinition>
    --> IVehiclePassNumbering<IVehiclePassNumbering>
    --> IVehiclePassNumberingDateOfFirstPass<IVehiclePassNumberingDateOfFirstPass>
    --> IVehiclePassNumberingFirstPassNum<IVehiclePassNumberingFirstPassNum>
    --> IVehiclePassBreak<IVehiclePassBreak>
    --> IVehicleInertia<IVehicleInertia>
    --> IVehicleMassProperties<IVehicleMassProperties>
    --> IExportToolTimePeriod<IExportToolTimePeriod>
    --> IExportToolStepSize<IExportToolStepSize>
    --> IVehicleEphemerisCode500ExportTool<IVehicleEphemerisCode500ExportTool>
    --> IVehicleEphemerisCCSDSExportTool<IVehicleEphemerisCCSDSExportTool>
    --> IVehicleEphemerisStkExportTool<IVehicleEphemerisStkExportTool>
    --> IVehicleCoordinateAxes<IVehicleCoordinateAxes>
    --> IVehicleCoordinateAxesCustom<IVehicleCoordinateAxesCustom>
    --> IVehicleAttitudeExportTool<IVehicleAttitudeExportTool>
    --> IVehicleEphemerisSpiceExportTool<IVehicleEphemerisSpiceExportTool>
    --> IVehiclePropDefinitionExportTool<IVehiclePropDefinitionExportTool>
    --> IVehicleEphemerisStkBinaryExportTool<IVehicleEphemerisStkBinaryExportTool>
    --> IVehicleEphemerisCCSDSv2ExportTool<IVehicleEphemerisCCSDSv2ExportTool>
    --> ISatelliteExportTools<ISatelliteExportTools>
    --> ISatellite<ISatellite>
    --> ILaunchVehicleGraphics<ILaunchVehicleGraphics>
    --> ILaunchVehicleGraphics3D<ILaunchVehicleGraphics3D>
    --> ILaunchVehicleExportTools<ILaunchVehicleExportTools>
    --> ILaunchVehicle<ILaunchVehicle>
    --> IGroundVehicleGraphics<IGroundVehicleGraphics>
    --> IGroundVehicleGraphics3D<IGroundVehicleGraphics3D>
    --> IGroundVehicleExportTools<IGroundVehicleExportTools>
    --> IGroundVehicle<IGroundVehicle>
    --> IMissileGraphics<IMissileGraphics>
    --> IMissileGraphics3D<IMissileGraphics3D>
    --> IMissileExportTools<IMissileExportTools>
    --> IMissile<IMissile>
    --> IAircraftGraphics<IAircraftGraphics>
    --> IAircraftGraphics3D<IAircraftGraphics3D>
    --> IAircraftExportTools<IAircraftExportTools>
    --> IAircraft<IAircraft>
    --> IShipGraphics<IShipGraphics>
    --> IShipGraphics3D<IShipGraphics3D>
    --> IShipExportTools<IShipExportTools>
    --> IShip<IShip>
    --> IMtoGraphics2DMarker<IMtoGraphics2DMarker>
    --> IMtoGraphics2DLine<IMtoGraphics2DLine>
    --> IMtoGraphics2DFadeTimes<IMtoGraphics2DFadeTimes>
    --> IMtoGraphics2DLeadTrailTimes<IMtoGraphics2DLeadTrailTimes>
    --> IMtoGraphics2DTrack<IMtoGraphics2DTrack>
    --> IMtoGraphics2DTrackCollection<IMtoGraphics2DTrackCollection>
    --> IMtoDefaultGraphics2DTrack<IMtoDefaultGraphics2DTrack>
    --> IMtoGraphics2DGlobalTrackOptions<IMtoGraphics2DGlobalTrackOptions>
    --> IMtoGraphics<IMtoGraphics>
    --> IMtoGraphics3DModelArtic<IMtoGraphics3DModelArtic>
    --> IMtoGraphics3DMarker<IMtoGraphics3DMarker>
    --> IMtoGraphics3DPoint<IMtoGraphics3DPoint>
    --> IMtoGraphics3DModel<IMtoGraphics3DModel>
    --> IMtoGraphics3DSwapDistances<IMtoGraphics3DSwapDistances>
    --> IMtoGraphics3DDropLines<IMtoGraphics3DDropLines>
    --> IMtoGraphics3DTrack<IMtoGraphics3DTrack>
    --> IMtoGraphics3DTrackCollection<IMtoGraphics3DTrackCollection>
    --> IMtoDefaultGraphics3DTrack<IMtoDefaultGraphics3DTrack>
    --> IMtoGraphics3DGlobalTrackOptions<IMtoGraphics3DGlobalTrackOptions>
    --> IMtoGraphics3D<IMtoGraphics3D>
    --> IMtoTrackPoint<IMtoTrackPoint>
    --> IMtoTrackPointCollection<IMtoTrackPointCollection>
    --> IMtoTrack<IMtoTrack>
    --> IMtoTrackCollection<IMtoTrackCollection>
    --> IMtoDefaultTrack<IMtoDefaultTrack>
    --> IMtoGlobalTrackOptions<IMtoGlobalTrackOptions>
    --> IMtoAnalysisPosition<IMtoAnalysisPosition>
    --> IMtoAnalysisVisibility<IMtoAnalysisVisibility>
    --> IMtoAnalysisFieldOfView<IMtoAnalysisFieldOfView>
    --> IMtoAnalysisRange<IMtoAnalysisRange>
    --> IMtoAnalysis<IMtoAnalysis>
    --> IMto<IMto>
    --> ILineTargetGraphics<ILineTargetGraphics>
    --> ILineTargetGraphics3D<ILineTargetGraphics3D>
    --> ILineTargetPoint<ILineTargetPoint>
    --> ILineTargetPointCollection<ILineTargetPointCollection>
    --> ILineTarget<ILineTarget>
    --> IChainGraphics2DStatic<IChainGraphics2DStatic>
    --> IChainGraphics2DAnimation<IChainGraphics2DAnimation>
    --> IChainGraphics<IChainGraphics>
    --> IChainGraphics3D<IChainGraphics3D>
    --> IAccessEventDetection<IAccessEventDetection>
    --> IAccessSampling<IAccessSampling>
    --> IChainConnectionCollection<IChainConnectionCollection>
    --> IChainTimePeriodBase<IChainTimePeriodBase>
    --> IChainUserSpecifiedTimePeriod<IChainUserSpecifiedTimePeriod>
    --> IChainConstraints<IChainConstraints>
    --> IChainConnection<IChainConnection>
    --> IChainOptimalStrandOpts<IChainOptimalStrandOpts>
    --> IChain<IChain>
    --> ICoverageGraphics2DStatic<ICoverageGraphics2DStatic>
    --> ICoverageGraphics2DAnimation<ICoverageGraphics2DAnimation>
    --> ICoverageGraphics2DProgress<ICoverageGraphics2DProgress>
    --> ICoverageGraphics<ICoverageGraphics>
    --> ICoverageGraphics3DAttributes<ICoverageGraphics3DAttributes>
    --> ICoverageGraphics3D<ICoverageGraphics3D>
    --> ICoverageSelectedGridPoint<ICoverageSelectedGridPoint>
    --> ICoverageGridPointSelection<ICoverageGridPointSelection>
    --> ICoverageGridInspector<ICoverageGridInspector>
    --> ICoverageRegionFilesCollection<ICoverageRegionFilesCollection>
    --> ICoverageAreaTargetsCollection<ICoverageAreaTargetsCollection>
    --> ICoveragePointFileListCollection<ICoveragePointFileListCollection>
    --> ICoverageBounds<ICoverageBounds>
    --> ICoverageBoundsCustomBoundary<ICoverageBoundsCustomBoundary>
    --> ICoverageBoundsCustomRegions<ICoverageBoundsCustomRegions>
    --> ICoverageBoundsGlobal<ICoverageBoundsGlobal>
    --> ICoverageBoundsLat<ICoverageBoundsLat>
    --> ICoverageBoundsLatLine<ICoverageBoundsLatLine>
    --> ICoverageBoundsLonLine<ICoverageBoundsLonLine>
    --> ICoverageBoundsLatLonRegion<ICoverageBoundsLatLonRegion>
    --> ICoverageResolution<ICoverageResolution>
    --> ICoverageResolutionArea<ICoverageResolutionArea>
    --> ICoverageResolutionDistance<ICoverageResolutionDistance>
    --> ICoverageResolutionLatLon<ICoverageResolutionLatLon>
    --> ICoverageGrid<ICoverageGrid>
    --> ICoveragePointDefinition<ICoveragePointDefinition>
    --> ICoverageAssetListElement<ICoverageAssetListElement>
    --> ICoverageAdvanced<ICoverageAdvanced>
    --> ICoverageInterval<ICoverageInterval>
    --> ICoverageDefinition<ICoverageDefinition>
    --> IFigureOfMeritGraphics3DLegendWindow<IFigureOfMeritGraphics3DLegendWindow>
    --> IFigureOfMeritGraphics2DRampColor<IFigureOfMeritGraphics2DRampColor>
    --> IFigureOfMeritGraphics2DLevelAttributesElement<IFigureOfMeritGraphics2DLevelAttributesElement>
    --> IFigureOfMeritGraphics2DLevelAttributesCollection<IFigureOfMeritGraphics2DLevelAttributesCollection>
    --> IFigureOfMeritGraphics2DPositionOnMap<IFigureOfMeritGraphics2DPositionOnMap>
    --> IFigureOfMeritGraphics2DLegendWindow<IFigureOfMeritGraphics2DLegendWindow>
    --> IFigureOfMeritGraphics2DColorOptions<IFigureOfMeritGraphics2DColorOptions>
    --> IFigureOfMeritGraphics2DTextOptions<IFigureOfMeritGraphics2DTextOptions>
    --> IFigureOfMeritGraphics2DRangeColorOptions<IFigureOfMeritGraphics2DRangeColorOptions>
    --> IFigureOfMeritGraphics2DLegend<IFigureOfMeritGraphics2DLegend>
    --> IFigureOfMeritGraphics2DContours<IFigureOfMeritGraphics2DContours>
    --> IFigureOfMeritGraphics2DAttributes<IFigureOfMeritGraphics2DAttributes>
    --> IFigureOfMeritGraphics2DContoursAnimation<IFigureOfMeritGraphics2DContoursAnimation>
    --> IFigureOfMeritGraphics2DAttributesAnimation<IFigureOfMeritGraphics2DAttributesAnimation>
    --> IFigureOfMeritGraphics3DAttributes<IFigureOfMeritGraphics3DAttributes>
    --> IFigureOfMeritGraphics3D<IFigureOfMeritGraphics3D>
    --> IFigureOfMeritDefinitionScalarCalculation<IFigureOfMeritDefinitionScalarCalculation>
    --> IFigureOfMeritGridInspector<IFigureOfMeritGridInspector>
    --> IFigureOfMeritNavigationAccuracyMethod<IFigureOfMeritNavigationAccuracyMethod>
    --> IFigureOfMeritNavigationAccuracyMethodElevationAngle<IFigureOfMeritNavigationAccuracyMethodElevationAngle>
    --> IFigureOfMeritNavigationAccuracyMethodConstant<IFigureOfMeritNavigationAccuracyMethodConstant>
    --> IFigureOfMeritAssetListElement<IFigureOfMeritAssetListElement>
    --> IFigureOfMeritAssetListCollection<IFigureOfMeritAssetListCollection>
    --> IFigureOfMeritUncertainties<IFigureOfMeritUncertainties>
    --> IFigureOfMeritSatisfaction<IFigureOfMeritSatisfaction>
    --> IFigureOfMeritDefinitionData<IFigureOfMeritDefinitionData>
    --> IFigureOfMeritDefinitionDataMinMax<IFigureOfMeritDefinitionDataMinMax>
    --> IFigureOfMeritDefinitionDataPercentLevel<IFigureOfMeritDefinitionDataPercentLevel>
    --> IFigureOfMeritDefinitionDataMinAssets<IFigureOfMeritDefinitionDataMinAssets>
    --> IFigureOfMeritDefinitionDataBestN<IFigureOfMeritDefinitionDataBestN>
    --> IFigureOfMeritDefinitionDataBest4<IFigureOfMeritDefinitionDataBest4>
    --> IFigureOfMeritDefinitionResponseTime<IFigureOfMeritDefinitionResponseTime>
    --> IFigureOfMeritDefinitionRevisitTime<IFigureOfMeritDefinitionRevisitTime>
    --> IFigureOfMeritDefinitionSimpleCoverage<IFigureOfMeritDefinitionSimpleCoverage>
    --> IFigureOfMeritDefinitionTimeAverageGap<IFigureOfMeritDefinitionTimeAverageGap>
    --> IFigureOfMeritDefinitionDilutionOfPrecision<IFigureOfMeritDefinitionDilutionOfPrecision>
    --> IFigureOfMeritDefinitionNavigationAccuracy<IFigureOfMeritDefinitionNavigationAccuracy>
    --> IFigureOfMeritDefinitionAccessSeparation<IFigureOfMeritDefinitionAccessSeparation>
    --> IFigureOfMerit<IFigureOfMerit>
    --> IFigureOfMeritDefinitionSystemResponseTime<IFigureOfMeritDefinitionSystemResponseTime>
    --> IFigureOfMeritDefinitionAgeOfData<IFigureOfMeritDefinitionAgeOfData>
    --> IFigureOfMeritDefinitionSystemAgeOfData<IFigureOfMeritDefinitionSystemAgeOfData>
    --> IConstellationConstraintRestriction<IConstellationConstraintRestriction>
    --> IConstellationConstraintObjectRestriction<IConstellationConstraintObjectRestriction>
    --> IConstellationConstraints<IConstellationConstraints>
    --> IConstellationGraphics<IConstellationGraphics>
    --> IConstellationRouting<IConstellationRouting>
    --> IConstellation<IConstellation>
    --> IEventDetectionStrategy<IEventDetectionStrategy>
    --> IEventDetectionNoSubSampling<IEventDetectionNoSubSampling>
    --> IEventDetectionSubSampling<IEventDetectionSubSampling>
    --> ISamplingMethodStrategy<ISamplingMethodStrategy>
    --> ISamplingMethodAdaptive<ISamplingMethodAdaptive>
    --> ISamplingMethodFixedStep<ISamplingMethodFixedStep>
    --> ISpaceEnvironmentRadEnergyMethodSpecify<ISpaceEnvironmentRadEnergyMethodSpecify>
    --> ISpaceEnvironmentRadEnergyValues<ISpaceEnvironmentRadEnergyValues>
    --> ISpaceEnvironmentRadiationEnvironment<ISpaceEnvironmentRadiationEnvironment>
    --> ISpaceEnvironmentMagnitudeFieldGraphics2D<ISpaceEnvironmentMagnitudeFieldGraphics2D>
    --> ISpaceEnvironmentScenarioExtGraphics3D<ISpaceEnvironmentScenarioExtGraphics3D>
    --> ISpaceEnvironmentSAAContour<ISpaceEnvironmentSAAContour>
    --> IVehicleSpaceEnvironmentMagneticField<IVehicleSpaceEnvironmentMagneticField>
    --> IVehicleSpaceEnvironmentVehTemperature<IVehicleSpaceEnvironmentVehTemperature>
    --> IVehicleSpaceEnvironmentParticleFlux<IVehicleSpaceEnvironmentParticleFlux>
    --> IVehicleSpaceEnvironmentRadDoseRateElement<IVehicleSpaceEnvironmentRadDoseRateElement>
    --> IVehicleSpaceEnvironmentRadDoseRateCollection<IVehicleSpaceEnvironmentRadDoseRateCollection>
    --> IVehicleSpaceEnvironmentRadiation<IVehicleSpaceEnvironmentRadiation>
    --> IVehicleSpaceEnvironmentMagnitudeFieldLine<IVehicleSpaceEnvironmentMagnitudeFieldLine>
    --> IVehicleSpaceEnvironmentGraphics<IVehicleSpaceEnvironmentGraphics>
    --> IStkPreferencesVDF<IStkPreferencesVDF>
    --> IStkPreferencesConnect<IStkPreferencesConnect>
    --> IStkPreferencesPythonPlugins<IStkPreferencesPythonPlugins>
    --> IPathCollection<IPathCollection>
    --> IVehicleAttitudeMaximumSlewRate<IVehicleAttitudeMaximumSlewRate>
    --> IVehicleAttitudeMaximumSlewAcceleration<IVehicleAttitudeMaximumSlewAcceleration>
    --> IVehicleAttitudeSlewBase<IVehicleAttitudeSlewBase>
    --> IVehicleAttitudeSlewConstrained<IVehicleAttitudeSlewConstrained>
    --> IVehicleAttitudeSlewFixedRate<IVehicleAttitudeSlewFixedRate>
    --> IVehicleAttitudeSlewFixedTime<IVehicleAttitudeSlewFixedTime>
    --> IVmGridDefinition<IVmGridDefinition>
    --> IVmAnalysisInterval<IVmAnalysisInterval>
    --> IVmAdvanced<IVmAdvanced>
    --> IVmGraphics3D<IVmGraphics3D>
    --> IVmGraphics3DGrid<IVmGraphics3DGrid>
    --> IVmGraphics3DCrossSection<IVmGraphics3DCrossSection>
    --> IVmGraphics3DCrossSectionPlaneCollection<IVmGraphics3DCrossSectionPlaneCollection>
    --> IVmGraphics3DVolume<IVmGraphics3DVolume>
    --> IVmGraphics3DActiveGridPoints<IVmGraphics3DActiveGridPoints>
    --> IVmGraphics3DSpatialCalculationLevels<IVmGraphics3DSpatialCalculationLevels>
    --> IVmGraphics3DSpatialCalculationLevelCollection<IVmGraphics3DSpatialCalculationLevelCollection>
    --> IVmGraphics3DLegend<IVmGraphics3DLegend>
    --> IVmExportTool<IVmExportTool>
    --> IVolumetric<IVolumetric>
    --> IVmGridSpatialCalculation<IVmGridSpatialCalculation>
    --> IVmExternalFile<IVmExternalFile>
    --> IVmGraphics3DCrossSectionPlane<IVmGraphics3DCrossSectionPlane>
    --> IVmGraphics3DSpatialCalculationLevel<IVmGraphics3DSpatialCalculationLevel>
    --> ISatelliteCollection<ISatelliteCollection>
    --> ISubset<ISubset>
    --> IAdvCATAvailableObjectCollection<IAdvCATAvailableObjectCollection>
    --> IAdvCATChosenObjectCollection<IAdvCATChosenObjectCollection>
    --> IAdvCATPreFilters<IAdvCATPreFilters>
    --> IAdvCATAdvancedEllipsoid<IAdvCATAdvancedEllipsoid>
    --> IAdvCATAdvanced<IAdvCATAdvanced>
    --> IAdvCATGraphics3D<IAdvCATGraphics3D>
    --> IAdvCAT<IAdvCAT>
    --> IAdvCATChosenObject<IAdvCATChosenObject>
    --> IEOIRShapeObject<IEOIRShapeObject>
    --> IEOIRShapeBox<IEOIRShapeBox>
    --> IEOIRShapeCone<IEOIRShapeCone>
    --> IEOIRShapePlate<IEOIRShapePlate>
    --> IEOIRShapeSphere<IEOIRShapeSphere>
    --> IEOIRShapeCoupler<IEOIRShapeCoupler>
    --> IEOIRShapeNone<IEOIRShapeNone>
    --> IEOIRShapeGEOComm<IEOIRShapeGEOComm>
    --> IEOIRShapeLEOComm<IEOIRShapeLEOComm>
    --> IEOIRShapeLEOImaging<IEOIRShapeLEOImaging>
    --> IEOIRShapeCustomMesh<IEOIRShapeCustomMesh>
    --> IEOIRShapeTargetSignature<IEOIRShapeTargetSignature>
    --> IEOIRStagePlume<IEOIRStagePlume>
    --> IEOIRShape<IEOIRShape>
    --> IEOIRStage<IEOIRStage>
    --> IEOIRShapeCollection<IEOIRShapeCollection>
    --> IEOIRMaterialElement<IEOIRMaterialElement>
    --> IEOIRMaterialElementCollection<IEOIRMaterialElementCollection>
    --> IMissileEOIR<IMissileEOIR>
    --> IVehicleEOIR<IVehicleEOIR>
    --> IEOIRShapeCylinder<IEOIRShapeCylinder>
    --> IStkObjectChangedEventArgs<IStkObjectChangedEventArgs>
    --> IScenarioBeforeSaveEventArgs<IScenarioBeforeSaveEventArgs>
    --> IPctCmpltEventArgs<IPctCmpltEventArgs>
    --> IStkObjectPreDeleteEventArgs<IStkObjectPreDeleteEventArgs>
    --> IStkObjectCutCopyPasteEventArgs<IStkObjectCutCopyPasteEventArgs>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> StkObject<>
    --> StkObjectRoot<>
    --> LevelAttribute<>
    --> LevelAttributeCollection<>
    --> BasicAzElMask<>
    --> FacilityGraphics<>
    --> PlaceGraphics<>
    --> Graphics2DRangeContours<>
    --> AccessConstraint<>
    --> AccessConstraintCollection<>
    --> Graphics3DRangeContours<>
    --> Graphics3DOffsetRotate<>
    --> Graphics3DOffsetTransformation<>
    --> Graphics3DOffsetAttach<>
    --> Graphics3DOffsetLabel<>
    --> Graphics3DOffset<>
    --> Graphics3DMarkerShape<>
    --> Graphics3DMarkerFile<>
    --> Graphics3DMarker<>
    --> Graphics3DDetailThreshold<>
    --> Graphics3DModelItem<>
    --> Graphics3DModelCollection<>
    --> LabelNote<>
    --> LabelNoteCollection<>
    --> Graphics3DVector<>
    --> FacilityGraphics3D<>
    --> PlaceGraphics3D<>
    --> TerrainNormSlopeAzimuth<>
    --> IntervalCollection<>
    --> ImmutableIntervalCollection<>
    --> DuringAccess<>
    --> DisplayTimesTimeComponent<>
    --> StarGraphics3D<>
    --> StarGraphics<>
    --> PlanetGraphics3D<>
    --> PlanetGraphics<>
    --> AreaTypePattern<>
    --> AreaTypePatternCollection<>
    --> AreaTypeEllipse<>
    --> AreaTargetGraphics3D<>
    --> AreaTargetGraphics<>
    --> Graphics3DAzElMask<>
    --> Graphics3DModelArtic<>
    --> Graphics3DModelTransformationCollection<>
    --> Graphics3DModelTransformation<>
    --> Graphics3DModelFile<>
    --> PlanetPositionFile<>
    --> PlanetPositionCentralBody<>
    --> PlanetOrbitDisplayTime<>
    --> Scenario<>
    --> ScenarioAnimation<>
    --> ScenarioEarthData<>
    --> ScenarioGraphics<>
    --> TerrainCollection<>
    --> Terrain<>
    --> TilesetCollection3D<>
    --> Tileset3D<>
    --> ScenarioGenDatabaseCollection<>
    --> ScenarioGenDatabase<>
    --> ScenarioGraphics3D<>
    --> SensorComplexConicPattern<>
    --> SensorEOIRPattern<>
    --> SensorUnknownPattern<>
    --> SensorEOIRBandCollection<>
    --> SensorEOIRBand<>
    --> SensorEOIRRadiometricPair<>
    --> SensorEOIRSensitivityCollection<>
    --> SensorEOIRSaturationCollection<>
    --> SensorCustomPattern<>
    --> SensorHalfPowerPattern<>
    --> SensorRectangularPattern<>
    --> SensorSARPattern<>
    --> SensorSimpleConicPattern<>
    --> SensorPointingFixed<>
    --> SensorPointingFixedAxes<>
    --> SensorPointing3DModel<>
    --> SensorPointingSpinning<>
    --> SensorPointingTargeted<>
    --> SensorPointingExternal<>
    --> SensorPointingTargetedBoresightTrack<>
    --> SensorPointingTargetedBoresightFixed<>
    --> SensorTargetCollection<>
    --> SensorTarget<>
    --> AccessTime<>
    --> ScheduleTime<>
    --> SensorAzElMaskFile<>
    --> SensorGraphics<>
    --> SensorProjection<>
    --> SensorProjectionDisplayDistance<>
    --> SensorGraphics3D<>
    --> SensorGraphics3DPulse<>
    --> SensorGraphics3DOffset<>
    --> AccessConstraintTimeSlipRange<>
    --> AccessConstraintBackground<>
    --> AccessConstraintGroundTrack<>
    --> AccessConstraintMinMax<>
    --> AccessConstraintCrdnConstellation<>
    --> AccessConstraintCentralBodyObstruction<>
    --> AccessConstraintAngle<>
    --> AccessConstraintCondition<>
    --> AccessTimeCollection<>
    --> ScheduleTimeCollection<>
    --> AccessConstraintIntervals<>
    --> AccessConstraintObjExAngle<>
    --> AccessConstraintZone<>
    --> AccessConstraintThirdBody<>
    --> AccessConstraintExclZonesCollection<>
    --> AccessConstraintGrazingAltitude<>
    --> SensorPointingGrazingAltitude<>
    --> AreaTarget<>
    --> Facility<>
    --> Target<>
    --> Place<>
    --> Planet<>
    --> Sensor<>
    --> SensorCommonTasks<>
    --> AreaTargetCommonTasks<>
    --> PlanetCommonTasks<>
    --> Swath<>
    --> Star<>
    --> DataProviderCollection<>
    --> DataProviderResultTimeArrayElements<>
    --> DataProviderResult<>
    --> DataProviderResultSubSectionCollection<>
    --> DataProviderResultSubSection<>
    --> DataProviderResultIntervalCollection<>
    --> DataProviderResultInterval<>
    --> DataProviderResultDataSetCollection<>
    --> DataProviderResultDataSet<>
    --> DataProviderFixed<>
    --> DataProviderTimeVarying<>
    --> DataProviderInterval<>
    --> DataProviderResultTextMessage<>
    --> DataProviderGroup<>
    --> DataProviderElements<>
    --> DataProviderElement<>
    --> DataProviders<>
    --> StkAccess<>
    --> StkAccessGraphics<>
    --> StkAccessAdvanced<>
    --> AccessTimePeriod<>
    --> AccessTimeEventIntervals<>
    --> StkObjectCoverage<>
    --> ObjectCoverageFigureOfMerit<>
    --> Scenario3dFont<>
    --> Graphics3DBorderWall<>
    --> Graphics3DReferenceAnalysisWorkbenchCollection<>
    --> Graphics3DReferenceVectorGeometryToolVector<>
    --> Graphics3DReferenceVectorGeometryToolAxes<>
    --> Graphics3DReferenceVectorGeometryToolAngle<>
    --> Graphics3DReferenceVectorGeometryToolPlane<>
    --> Graphics3DReferenceVectorGeometryToolPoint<>
    --> TargetGraphics<>
    --> TargetGraphics3D<>
    --> PointTargetGraphics3DModel<>
    --> ObjectLinkCollection<>
    --> ObjectLink<>
    --> LinkToObject<>
    --> LLAPosition<>
    --> Graphics3DDataDisplayElement<>
    --> Graphics3DDataDisplayCollection<>
    --> VehicleInitialState<>
    --> VehicleHPOPCentralBodyGravity<>
    --> VehicleRadiationPressure<>
    --> VehicleHPOPSolarRadiationPressure<>
    --> VehicleSolarFluxGeoMagnitudeEnterManually<>
    --> VehicleSolarFluxGeoMagnitudeUseFile<>
    --> VehicleHPOPForceModelDrag<>
    --> VehicleHPOPForceModelDragOptions<>
    --> VehicleHPOPSolarRadiationPressureOptions<>
    --> VehicleStatic<>
    --> VehicleSolidTides<>
    --> VehicleOceanTides<>
    --> VehiclePluginSettings<>
    --> VehiclePluginPropagator<>
    --> VehicleHPOPForceModelMoreOptions<>
    --> VehicleHPOPForceModel<>
    --> VehicleStepSizeControl<>
    --> VehicleTimeRegularization<>
    --> VehicleInterpolation<>
    --> VehicleIntegrator<>
    --> VehicleGravity<>
    --> VehiclePositionVelocityElement<>
    --> VehiclePositionVelocityCollection<>
    --> VehicleCorrelationListCollection<>
    --> VehicleCorrelationListElement<>
    --> VehicleCovariance<>
    --> VehicleJxInitialState<>
    --> VehicleLOPCentralBodyGravity<>
    --> VehicleThirdBodyGravityElement<>
    --> VehicleThirdBodyGravityCollection<>
    --> VehicleExpDensModelParams<>
    --> VehicleAdvanced<>
    --> VehicleLOPForceModelDrag<>
    --> VehicleLOPSolarRadiationPressure<>
    --> VehiclePhysicalData<>
    --> VehicleLOPForceModel<>
    --> VehicleSegmentsCollection<>
    --> VehiclePropagatorHPOP<>
    --> VehiclePropagatorJ2Perturbation<>
    --> VehiclePropagatorJ4Perturbation<>
    --> VehiclePropagatorLOP<>
    --> VehiclePropagatorSGP4<>
    --> VehiclePropagatorSPICE<>
    --> VehiclePropagatorStkExternal<>
    --> VehiclePropagatorTwoBody<>
    --> VehiclePropagatorUserExternal<>
    --> VehicleLaunchVehicleInitialState<>
    --> VehiclePropagatorSimpleAscent<>
    --> VehicleWaypointsElement<>
    --> VehicleWaypointsCollection<>
    --> VehicleLaunchLLA<>
    --> VehicleLaunchLLR<>
    --> VehicleImpactLLA<>
    --> VehicleImpactLLR<>
    --> VehicleLaunchControlFixedApogeeAltitude<>
    --> VehicleLaunchControlFixedDeltaV<>
    --> VehicleLaunchControlFixedDeltaVMinEccentricity<>
    --> VehicleLaunchControlFixedTimeOfFlight<>
    --> VehicleImpactLocationLaunchAzEl<>
    --> VehicleImpactLocationPoint<>
    --> VehiclePropagatorBallistic<>
    --> VehiclePropagatorGreatArc<>
    --> VehicleSGP4SegmentCollection<>
    --> VehicleSGP4Segment<>
    --> VehicleThirdBodyGravity<>
    --> VehicleConsiderAnalysisCollectionElement<>
    --> VehicleConsiderAnalysisCollection<>
    --> VehicleSPICESegment<>
    --> VehicleWaypointAltitudeReferenceTerrain<>
    --> VehicleWaypointAltitudeReference<>
    --> VehicleSGP4LoadFile<>
    --> VehicleSGP4OnlineLoad<>
    --> VehicleSGP4OnlineAutoLoad<>
    --> VehicleGroundEllipsesCollection<>
    --> Satellite<>
    --> VehicleInertia<>
    --> VehicleMassProperties<>
    --> VehicleBreakAngleBreakByLatitude<>
    --> VehicleBreakAngleBreakByLongitude<>
    --> VehicleDefinition<>
    --> VehicleRepeatGroundTrackNumbering<>
    --> VehiclePassNumberingDateOfFirstPass<>
    --> VehiclePassNumberingFirstPassNum<>
    --> VehiclePassBreak<>
    --> VehicleCentralBodies<>
    --> SatelliteGraphics<>
    --> SatelliteGraphics3D<>
    --> VehicleEllipseDataElement<>
    --> VehicleEllipseDataCollection<>
    --> VehicleGroundEllipseElement<>
    --> SatelliteGraphics3DModel<>
    --> VehicleEclipseBodies<>
    --> VehicleVector<>
    --> VehicleRateOffset<>
    --> VehicleProfileAlignedAndConstrained<>
    --> VehicleProfileInertial<>
    --> VehicleProfileConstraintOffset<>
    --> VehicleProfileFixedInAxes<>
    --> VehicleProfilePrecessingSpin<>
    --> VehicleProfileSpinAboutXXX<>
    --> VehicleProfileSpinning<>
    --> VehicleProfileAlignmentOffset<>
    --> VehicleScheduleTimesCollection<>
    --> VehicleTargetTimes<>
    --> VehicleAttitudePointing<>
    --> VehicleDuration<>
    --> VehicleStandardBasic<>
    --> VehicleAttitudeExternal<>
    --> VehicleAttitudeRealTime<>
    --> VehicleProfileCoordinatedTurn<>
    --> VehicleProfileYawToNadir<>
    --> VehicleAttitudeTrendControlAviator<>
    --> VehicleProfileAviator<>
    --> VehicleTargetPointingElement<>
    --> VehicleTargetPointingCollection<>
    --> VehicleTorque<>
    --> VehicleIntegratedAttitude<>
    --> VehicleScheduleTimesElement<>
    --> VehicleTrajectoryAttitudeStandard<>
    --> VehicleOrbitAttitudeStandard<>
    --> VehicleRouteAttitudeStandard<>
    --> VehicleGraphics2DLine<>
    --> VehicleGraphics2DIntervalsCollection<>
    --> VehicleGraphics2DAttributesAccess<>
    --> VehicleGraphics2DAttributesCustom<>
    --> VehicleGraphics2DAttributesRealtime<>
    --> VehicleGraphics2DLightingElement<>
    --> VehicleGraphics2DLighting<>
    --> VehicleGraphics2DElevationGroundElevation<>
    --> VehicleGraphics2DElevationSwathHalfWidth<>
    --> VehicleGraphics2DElevationVehicleHalfAngle<>
    --> VehicleGraphics2DSwath<>
    --> VehicleGraphics2DLeadDataFraction<>
    --> VehicleGraphics2DLeadDataTime<>
    --> VehicleGraphics2DTrailDataFraction<>
    --> VehicleGraphics2DTrailDataTime<>
    --> VehicleGraphics2DRoutePassData<>
    --> VehicleGraphics2DLeadTrailData<>
    --> VehicleGraphics2DOrbitPassData<>
    --> VehicleGraphics2DTrajectoryPassData<>
    --> VehicleGraphics2DTrajectoryResolution<>
    --> VehicleGraphics2DGroundEllipsesCollection<>
    --> VehicleGraphics2DTimeEventTypeLine<>
    --> VehicleGraphics2DTimeEventTypeMarker<>
    --> VehicleGraphics2DTimeEventTypeText<>
    --> VehicleGraphics2DTimeEventsElement<>
    --> VehicleGraphics2DTimeEventsCollection<>
    --> VehicleGraphics2DPassShowPasses<>
    --> VehicleGraphics2DPasses<>
    --> VehicleGraphics2DSAA<>
    --> VehicleGraphics2DElevationsElement<>
    --> VehicleGraphics2DElevationsCollection<>
    --> VehicleGraphics2DElevContours<>
    --> VehicleGraphics2DRouteResolution<>
    --> VehicleGraphics2DWaypointMarkersElement<>
    --> VehicleGraphics2DWaypointMarkersCollection<>
    --> VehicleGraphics2DWaypointMarker<>
    --> VehicleGraphics2DInterval<>
    --> VehicleGraphics2DPassResolution<>
    --> VehicleGraphics2DGroundEllipsesElement<>
    --> VehicleGraphics2DAttributesRoute<>
    --> VehicleGraphics2DAttributesTrajectory<>
    --> VehicleGraphics2DAttributesOrbit<>
    --> Graphics3DPointableElementsElement<>
    --> Graphics3DPointableElementsCollection<>
    --> VehicleGraphics3DSystemsElement<>
    --> VehicleGraphics3DSystemsSpecialElement<>
    --> VehicleGraphics3DSystemsCollection<>
    --> VehicleGraphics3DEllipsoid<>
    --> VehicleGraphics3DControlBox<>
    --> VehicleGraphics3DBearingBox<>
    --> VehicleGraphics3DBearingEllipse<>
    --> VehicleGraphics3DLineOfBearing<>
    --> VehicleGraphics3DGeoBox<>
    --> VehicleGraphics3DRouteProximity<>
    --> VehicleGraphics3DOrbitProximity<>
    --> VehicleGraphics3DElevContours<>
    --> VehicleGraphics3DSAA<>
    --> VehicleGraphics3DSigmaScaleProbability<>
    --> VehicleGraphics3DSigmaScaleScale<>
    --> VehicleGraphics3DDefaultAttributes<>
    --> VehicleGraphics3DIntervalsElement<>
    --> VehicleGraphics3DIntervalsCollection<>
    --> VehicleGraphics3DAttributesBasic<>
    --> VehicleGraphics3DAttributesIntervals<>
    --> VehicleGraphics3DSize<>
    --> VehicleGraphics3DCovariancePointingContour<>
    --> VehicleGraphics3DDataFraction<>
    --> VehicleGraphics3DDataTime<>
    --> VehicleGraphics3DOrbitPassData<>
    --> VehicleGraphics3DOrbitTrackData<>
    --> VehicleGraphics3DTickDataLine<>
    --> VehicleGraphics3DTickDataPoint<>
    --> VehicleGraphics3DOrbitTickMarks<>
    --> VehicleGraphics3DPass<>
    --> VehicleGraphics3DCovariance<>
    --> VehicleGraphics3DVelCovariance<>
    --> VehicleGraphics3DTrajectoryProximity<>
    --> VehicleGraphics3DTrajectory<>
    --> VehicleGraphics3DTrajectoryTrackData<>
    --> VehicleGraphics3DTrajectoryPassData<>
    --> VehicleGraphics3DLeadTrailData<>
    --> VehicleGraphics3DTrajectoryTickMarks<>
    --> VehicleGraphics3DPathTickMarks<>
    --> VehicleGraphics3DWaypointMarkersElement<>
    --> VehicleGraphics3DWaypointMarkersCollection<>
    --> VehicleGraphics3DRoute<>
    --> Graphics3DModelPointing<>
    --> Graphics3DLabelSwapDistance<>
    --> VehicleGraphics3DDropLinePositionItem<>
    --> VehicleGraphics3DDropLinePositionItemCollection<>
    --> VehicleGraphics3DDropLinePathItem<>
    --> VehicleGraphics3DDropLinePathItemCollection<>
    --> VehicleGraphics3DOrbitDropLines<>
    --> VehicleGraphics3DRouteDropLines<>
    --> VehicleGraphics3DTrajectoryDropLines<>
    --> VehicleTrajectoryGraphics3DModel<>
    --> VehicleRouteGraphics3DModel<>
    --> VehicleGraphics3DBPlaneTemplateDisplayElement<>
    --> VehicleGraphics3DBPlaneTemplateDisplayCollection<>
    --> VehicleGraphics3DBPlaneTemplate<>
    --> VehicleGraphics3DBPlaneTemplatesCollection<>
    --> VehicleGraphics3DBPlaneEvent<>
    --> VehicleGraphics3DBPlanePoint<>
    --> VehicleGraphics3DBPlaneTargetPointPositionCartesian<>
    --> VehicleGraphics3DBPlaneTargetPointPositionPolar<>
    --> VehicleGraphics3DBPlaneTargetPoint<>
    --> VehicleGraphics3DBPlaneInstance<>
    --> VehicleGraphics3DBPlaneInstancesCollection<>
    --> VehicleGraphics3DBPlanePointCollection<>
    --> VehicleGraphics3DBPlanes<>
    --> LaunchVehicle<>
    --> LaunchVehicleGraphics<>
    --> LaunchVehicleGraphics3D<>
    --> GroundVehicle<>
    --> GroundVehicleGraphics<>
    --> GroundVehicleGraphics3D<>
    --> Missile<>
    --> MissileGraphics<>
    --> MissileGraphics3D<>
    --> Aircraft<>
    --> AircraftGraphics<>
    --> AircraftGraphics3D<>
    --> Ship<>
    --> ShipGraphics<>
    --> ShipGraphics3D<>
    --> MtoTrackPoint<>
    --> MtoTrackPointCollection<>
    --> MtoTrack<>
    --> MtoTrackCollection<>
    --> MtoDefaultTrack<>
    --> MtoGlobalTrackOptions<>
    --> Mto<>
    --> MtoGraphics2DMarker<>
    --> MtoGraphics2DLine<>
    --> MtoGraphics2DFadeTimes<>
    --> MtoGraphics2DLeadTrailTimes<>
    --> MtoGraphics2DTrack<>
    --> MtoGraphics2DTrackCollection<>
    --> MtoDefaultGraphics2DTrack<>
    --> MtoGraphics2DGlobalTrackOptions<>
    --> MtoGraphics<>
    --> MtoGraphics3DMarker<>
    --> MtoGraphics3DPoint<>
    --> MtoGraphics3DModel<>
    --> MtoGraphics3DSwapDistances<>
    --> MtoGraphics3DDropLines<>
    --> MtoGraphics3DTrack<>
    --> MtoGraphics3DTrackCollection<>
    --> MtoDefaultGraphics3DTrack<>
    --> MtoGraphics3DGlobalTrackOptions<>
    --> MtoGraphics3D<>
    --> LLAGeocentric<>
    --> LLAGeodetic<>
    --> LineTargetPoint<>
    --> LineTargetPointCollection<>
    --> LineTarget<>
    --> LineTargetGraphics<>
    --> LineTargetGraphics3D<>
    --> CoverageDefinition<>
    --> CoverageBoundsCustomRegions<>
    --> CoverageBoundsCustomBoundary<>
    --> CoverageBoundsGlobal<>
    --> CoverageBoundsLat<>
    --> CoverageBoundsLatLine<>
    --> CoverageBoundsLonLine<>
    --> CoverageBoundsLatLonRegion<>
    --> CoverageGrid<>
    --> CoverageAssetListElement<>
    --> CoverageAssetListCollection<>
    --> CoverageRegionFilesCollection<>
    --> CoverageAreaTargetsCollection<>
    --> CoveragePointDefinition<>
    --> CoveragePointFileListCollection<>
    --> CoverageAdvanced<>
    --> CoverageInterval<>
    --> CoverageResolutionArea<>
    --> CoverageResolutionDistance<>
    --> CoverageResolutionLatLon<>
    --> CoverageGraphics2DStatic<>
    --> CoverageGraphics2DAnimation<>
    --> CoverageGraphics2DProgress<>
    --> CoverageGraphics<>
    --> CoverageGraphics3D<>
    --> CoverageGraphics3DAttributes<>
    --> ChainTimePeriodBase<>
    --> ChainUserSpecifiedTimePeriod<>
    --> ChainConstraints<>
    --> Chain<>
    --> ChainConnection<>
    --> ChainConnectionCollection<>
    --> ChainOptimalStrandOpts<>
    --> ChainGraphics2DStatic<>
    --> ChainGraphics2DAnimation<>
    --> ChainGraphics<>
    --> ChainGraphics3D<>
    --> RefractionCoefficients<>
    --> RefractionModelEffectiveRadiusMethod<>
    --> RefractionModelITURP8344<>
    --> RefractionModelSCFMethod<>
    --> FigureOfMeritDefinitionCompute<>
    --> FigureOfMeritDefinitionDataMinMax<>
    --> FigureOfMeritDefinitionDataMinAssets<>
    --> FigureOfMeritDefinitionDataPercentLevel<>
    --> FigureOfMeritDefinitionDataBestN<>
    --> FigureOfMeritDefinitionDataBest4<>
    --> FigureOfMeritDefinitionAccessConstraint<>
    --> FigureOfMeritSatisfaction<>
    --> FigureOfMerit<>
    --> FigureOfMeritDefinitionAccessSeparation<>
    --> FigureOfMeritDefinitionDilutionOfPrecision<>
    --> FigureOfMeritDefinitionNavigationAccuracy<>
    --> FigureOfMeritAssetListElement<>
    --> FigureOfMeritAssetListCollection<>
    --> FigureOfMeritUncertainties<>
    --> FigureOfMeritDefinitionResponseTime<>
    --> FigureOfMeritDefinitionRevisitTime<>
    --> FigureOfMeritDefinitionSimpleCoverage<>
    --> FigureOfMeritDefinitionTimeAverageGap<>
    --> FigureOfMeritDefinitionSystemAgeOfData<>
    --> FigureOfMeritGraphics2DContours<>
    --> FigureOfMeritGraphics2DAttributes<>
    --> FigureOfMeritGraphics2DContoursAnimation<>
    --> FigureOfMeritGraphics2DAttributesAnimation<>
    --> FigureOfMeritGraphics<>
    --> FigureOfMeritGraphics2DRampColor<>
    --> FigureOfMeritGraphics2DLevelAttributesElement<>
    --> FigureOfMeritGraphics2DLevelAttributesCollection<>
    --> FigureOfMeritGraphics2DPositionOnMap<>
    --> FigureOfMeritGraphics2DColorOptions<>
    --> FigureOfMeritGraphics2DLegendWindow<>
    --> FigureOfMeritGraphics3DLegendWindow<>
    --> FigureOfMeritGraphics2DTextOptions<>
    --> FigureOfMeritGraphics2DRangeColorOptions<>
    --> FigureOfMeritGraphics2DLegend<>
    --> FigureOfMeritNavigationAccuracyMethodElevationAngle<>
    --> FigureOfMeritNavigationAccuracyMethodConstant<>
    --> FigureOfMeritGraphics3DAttributes<>
    --> FigureOfMeritGraphics3D<>
    --> VehicleProfileGPS<>
    --> StkObjectModelContext<>
    --> StdMilitary2525bSymbols<>
    --> CoverageGridInspector<>
    --> FigureOfMeritGridInspector<>
    --> Graphics3DVaporTrail<>
    --> VehicleTargetPointingIntervalCollection<>
    --> AccessConstraintPluginMinMax<>
    --> ConstellationConstraints<>
    --> ConstellationConstraintObjectRestriction<>
    --> ConstellationConstraintRestriction<>
    --> Constellation<>
    --> ConstellationGraphics<>
    --> ConstellationRouting<>
    --> EventDetectionNoSubSampling<>
    --> EventDetectionSubSampling<>
    --> SamplingMethodAdaptive<>
    --> SamplingMethodFixedStep<>
    --> SensorAccessAdvanced<>
    --> VehicleAccessAdvanced<>
    --> AccessSampling<>
    --> AccessEventDetection<>
    --> SensorGraphics3DProjectionElement<>
    --> SensorGraphics3DSpaceProjectionCollection<>
    --> SensorGraphics3DTargetProjectionCollection<>
    --> CentralBodyTerrainCollectionElement<>
    --> CentralBodyTerrainCollection<>
    --> SatelliteExportTools<>
    --> LaunchVehicleExportTools<>
    --> GroundVehicleExportTools<>
    --> MissileExportTools<>
    --> AircraftExportTools<>
    --> ShipExportTools<>
    --> VehicleEphemerisCode500ExportTool<>
    --> VehicleEphemerisCCSDSExportTool<>
    --> VehicleEphemerisStkExportTool<>
    --> VehicleEphemerisSpiceExportTool<>
    --> ExportToolTimePeriod<>
    --> VehicleAttitudeExportTool<>
    --> VehiclePropDefinitionExportTool<>
    --> VehicleCoordinateAxesCustom<>
    --> ExportToolStepSize<>
    --> PctCmpltEventArgs<>
    --> StkObjectChangedEventArgs<>
    --> VehicleEclipsingBodies<>
    --> LocationVectorGeometryToolPoint<>
    --> TimePeriod<>
    --> TimePeriodValue<>
    --> SpatialState<>
    --> VehicleSpatialInfo<>
    --> OnePointAccess<>
    --> OnePointAccessResultCollection<>
    --> OnePointAccessResult<>
    --> OnePointAccessConstraintCollection<>
    --> OnePointAccessConstraint<>
    --> VehiclePropagatorRealtime<>
    --> VehicleRealtimePointBuilder<>
    --> VehicleRealtimeCartesianPoints<>
    --> VehicleRealtimeLLAHPSPoints<>
    --> VehicleRealtimeLLAPoints<>
    --> VehicleRealtimeUTMPoints<>
    --> SRPModelGPS<>
    --> SRPModelSpherical<>
    --> SRPModelPlugin<>
    --> SRPModelPluginSettings<>
    --> VehicleHPOPSRPModel<>
    --> VehicleHPOPDragModelSpherical<>
    --> VehicleHPOPDragModelPlugin<>
    --> VehicleHPOPDragModelPluginSettings<>
    --> VehicleHPOPDragModel<>
    --> ScenarioAnimationTimePeriod<>
    --> SensorProjectionConstantAltitude<>
    --> SensorProjectionObjectAltitude<>
    --> VehicleAttitudeRealTimeDataReference<>
    --> MtoAnalysis<>
    --> MtoAnalysisPosition<>
    --> MtoAnalysisRange<>
    --> MtoAnalysisFieldOfView<>
    --> MtoAnalysisVisibility<>
    --> VehiclePropagatorGPS<>
    --> AvailableFeatures<>
    --> ScenarioBeforeSaveEventArgs<>
    --> StkObjectPreDeleteEventArgs<>
    --> VehiclePropagatorSGP4CommonTasks<>
    --> VehicleSGP4AutoUpdateProperties<>
    --> VehicleSGP4AutoUpdateFileSource<>
    --> VehicleSGP4AutoUpdateOnlineSource<>
    --> VehicleSGP4AutoUpdate<>
    --> VehicleSGP4PropagatorSettings<>
    --> VehicleGPSAutoUpdateProperties<>
    --> VehicleGPSAutoUpdateFileSource<>
    --> VehicleGPSAutoUpdateOnlineSource<>
    --> VehicleGPSAutoUpdate<>
    --> VehicleGPSSpecifyAlmanac<>
    --> VehicleGPSAlmanacProperties<>
    --> VehicleGPSAlmanacPropertiesSEM<>
    --> VehicleGPSAlmanacPropertiesYUMA<>
    --> VehicleGPSAlmanacPropertiesSP3<>
    --> VehicleGPSElementCollection<>
    --> VehicleGPSElement<>
    --> SpaceEnvironmentRadEnergyMethodSpecify<>
    --> SpaceEnvironmentRadEnergyValues<>
    --> SpaceEnvironmentRadiationEnvironment<>
    --> SpaceEnvironmentMagnitudeFieldGraphics2D<>
    --> SpaceEnvironmentScenarioExtGraphics3D<>
    --> ScenSpaceEnvironment<>
    --> VehicleSpaceEnvironmentRadDoseRateElement<>
    --> VehicleSpaceEnvironmentRadDoseRateCollection<>
    --> SpaceEnvironmentSAAContour<>
    --> VehicleSpaceEnvironmentVehTemperature<>
    --> VehicleSpaceEnvironmentParticleFlux<>
    --> VehicleSpaceEnvironmentMagneticField<>
    --> VehicleSpaceEnvironmentRadiation<>
    --> VehicleSpaceEnvironmentMagnitudeFieldLine<>
    --> VehicleSpaceEnvironmentGraphics<>
    --> VehicleSpaceEnvironment<>
    --> CoverageSelectedGridPoint<>
    --> CoverageGridPointSelection<>
    --> CelestialBodyCollection<>
    --> CelestialBodyInfo<>
    --> StkCentralBodyEllipsoid<>
    --> StkCentralBody<>
    --> StkCentralBodyCollection<>
    --> FigureOfMeritDefinitionSystemResponseTime<>
    --> FigureOfMeritDefinitionAgeOfData<>
    --> FigureOfMeritDefinitionScalarCalculation<>
    --> VehiclePropagator11ParamDescriptor<>
    --> VehiclePropagator11ParamDescriptorCollection<>
    --> VehiclePropagator11Param<>
    --> VehiclePropagatorSP3File<>
    --> VehiclePropagatorSP3FileCollection<>
    --> VehiclePropagatorSP3<>
    --> VehicleEphemerisStkBinaryExportTool<>
    --> OrbitState<>
    --> OrbitStateCoordinateSystem<>
    --> OrbitStateCartesian<>
    --> ClassicalSizeShapeAltitude<>
    --> ClassicalSizeShapeMeanMotion<>
    --> ClassicalSizeShapePeriod<>
    --> ClassicalSizeShapeRadius<>
    --> ClassicalSizeShapeSemimajorAxis<>
    --> OrientationAscNodeLAN<>
    --> OrientationAscNodeRAAN<>
    --> ClassicalOrientation<>
    --> ClassicalLocationArgumentOfLatitude<>
    --> ClassicalLocationEccentricAnomaly<>
    --> ClassicalLocationMeanAnomaly<>
    --> ClassicalLocationTimePastAN<>
    --> ClassicalLocationTimePastPerigee<>
    --> ClassicalLocationTrueAnomaly<>
    --> OrbitStateClassical<>
    --> GeodeticSizeAltitude<>
    --> GeodeticSizeRadius<>
    --> OrbitStateGeodetic<>
    --> DelaunayL<>
    --> DelaunayLOverSQRTmu<>
    --> DelaunayH<>
    --> DelaunayHOverSQRTmu<>
    --> DelaunayG<>
    --> DelaunayGOverSQRTmu<>
    --> OrbitStateDelaunay<>
    --> EquinoctialSizeShapeMeanMotion<>
    --> EquinoctialSizeShapeSemimajorAxis<>
    --> OrbitStateEquinoctial<>
    --> MixedSphericalFPAHorizontal<>
    --> MixedSphericalFPAVertical<>
    --> OrbitStateMixedSpherical<>
    --> SphericalFPAHorizontal<>
    --> SphericalFPAVertical<>
    --> OrbitStateSpherical<>
    --> VehicleGraphics2DTimeComponentsEventElement<>
    --> VehicleGraphics2DTimeComponentsEventCollectionElement<>
    --> VehicleGraphics2DTimeComponentsCollection<>
    --> VehicleGraphics2DAttributesTimeComponents<>
    --> StkPreferences<>
    --> StkPreferencesVDF<>
    --> VehicleAttitudeMaximumSlewRate<>
    --> VehicleAttitudeMaximumSlewAcceleration<>
    --> VehicleAttitudeSlewConstrained<>
    --> VehicleAttitudeSlewFixedRate<>
    --> VehicleAttitudeSlewFixedTime<>
    --> VehicleAttitudeTargetSlew<>
    --> MtoGraphics3DModelArtic<>
    --> VehiclePropagatorAviator<>
    --> VehicleEphemerisCCSDSv2ExportTool<>
    --> StkPreferencesConnect<>
    --> Antenna<>
    --> AntennaModel<>
    --> AntennaModelOpticalSimple<>
    --> AntennaModelOpticalGaussian<>
    --> AntennaModelGaussian<>
    --> AntennaModelParabolic<>
    --> AntennaModelSquareHorn<>
    --> AntennaModelScriptPlugin<>
    --> AntennaModelExternal<>
    --> AntennaModelGimroc<>
    --> AntennaModelRemcomUanFormat<>
    --> AntennaModelANSYSffdFormat<>
    --> AntennaModelTicraGRASPFormat<>
    --> AntennaModelElevationAzimuthCuts<>
    --> AntennaModelIeee1979<>
    --> AntennaModelDipole<>
    --> AntennaModelHelix<>
    --> AntennaModelCosecantSquared<>
    --> AntennaModelHemispherical<>
    --> AntennaModelPencilBeam<>
    --> AntennaModelPhasedArray<>
    --> AntennaModelHfssEepArray<>
    --> AntennaModelIsotropic<>
    --> AntennaModelIntelSat<>
    --> AntennaModelGpsGlobal<>
    --> AntennaModelGpsFrpa<>
    --> AntennaModelItuBO1213CoPolar<>
    --> AntennaModelItuBO1213CrossPolar<>
    --> AntennaModelItuF1245<>
    --> AntennaModelItuS580<>
    --> AntennaModelItuS465<>
    --> AntennaModelItuS731<>
    --> AntennaModelItuS1528R12Circular<>
    --> AntennaModelItuS1528R13<>
    --> AntennaModelItuS672Circular<>
    --> AntennaModelItuS1528R12Rectangular<>
    --> AntennaModelItuS672Rectangular<>
    --> AntennaModelApertureCircularCosine<>
    --> AntennaModelApertureCircularUniform<>
    --> AntennaModelApertureCircularCosineSquared<>
    --> AntennaModelApertureCircularBessel<>
    --> AntennaModelApertureCircularBesselEnvelope<>
    --> AntennaModelApertureCircularCosinePedestal<>
    --> AntennaModelApertureCircularCosineSquaredPedestal<>
    --> AntennaModelApertureCircularSincIntPower<>
    --> AntennaModelApertureCircularSincRealPower<>
    --> AntennaModelApertureRectangularCosine<>
    --> AntennaModelApertureRectangularCosinePedestal<>
    --> AntennaModelApertureRectangularCosineSquaredPedestal<>
    --> AntennaModelApertureRectangularSincIntPower<>
    --> AntennaModelApertureRectangularSincRealPower<>
    --> AntennaModelApertureRectangularCosineSquared<>
    --> AntennaModelApertureRectangularUniform<>
    --> AntennaModelRectangularPattern<>
    --> AntennaControl<>
    --> AntennaGraphics3D<>
    --> RadarCrossSectionVolumeGraphics<>
    --> RadarCrossSectionGraphics3D<>
    --> RadarCrossSectionGraphics<>
    --> AntennaVolumeGraphics<>
    --> AntennaContourGraphics<>
    --> AntennaGraphics<>
    --> RadarCrossSectionContourLevelCollection<>
    --> RadarCrossSectionContourLevel<>
    --> RadarCrossSectionVolumeLevelCollection<>
    --> RadarCrossSectionVolumeLevel<>
    --> AntennaVolumeLevelCollection<>
    --> AntennaVolumeLevel<>
    --> AntennaContourLevelCollection<>
    --> AntennaContourLevel<>
    --> AntennaContourGain<>
    --> AntennaContourEirp<>
    --> AntennaContourRip<>
    --> AntennaContourFluxDensity<>
    --> AntennaContourSpectralFluxDensity<>
    --> Transmitter<>
    --> TransmitterModel<>
    --> TransmitterModelScriptPluginRF<>
    --> TransmitterModelScriptPluginLaser<>
    --> TransmitterModelCable<>
    --> TransmitterModelSimple<>
    --> TransmitterModelMedium<>
    --> TransmitterModelComplex<>
    --> TransmitterModelMultibeam<>
    --> TransmitterModelLaser<>
    --> ReTransmitterModelSimple<>
    --> ReTransmitterModelMedium<>
    --> ReTransmitterModelComplex<>
    --> TransmitterGraphics3D<>
    --> TransmitterGraphics<>
    --> Receiver<>
    --> ReceiverModel<>
    --> ReceiverModelCable<>
    --> ReceiverModelSimple<>
    --> ReceiverModelMedium<>
    --> ReceiverModelComplex<>
    --> ReceiverModelMultibeam<>
    --> ReceiverModelLaser<>
    --> ReceiverModelScriptPluginRF<>
    --> ReceiverModelScriptPluginLaser<>
    --> ReceiverGraphics3D<>
    --> ReceiverGraphics<>
    --> RadarDopplerClutterFilters<>
    --> Waveform<>
    --> WaveformRectangular<>
    --> WaveformPulseDefinition<>
    --> RadarMultifunctionWaveformStrategySettings<>
    --> WaveformSelectionStrategy<>
    --> WaveformSelectionStrategyFixed<>
    --> WaveformSelectionStrategyRangeLimits<>
    --> Radar<>
    --> RadarModel<>
    --> RadarModelMonostatic<>
    --> RadarModelMultifunction<>
    --> RadarModelBistaticTransmitter<>
    --> RadarModelBistaticReceiver<>
    --> RadarGraphics3D<>
    --> RadarGraphics<>
    --> RadarAccessGraphics<>
    --> RadarMultipathGraphics<>
    --> RadarModeMonostatic<>
    --> RadarModeMonostaticSearchTrack<>
    --> RadarModeMonostaticSar<>
    --> RadarModeBistaticTransmitter<>
    --> RadarModeBistaticTransmitterSearchTrack<>
    --> RadarModeBistaticTransmitterSar<>
    --> RadarModeBistaticReceiver<>
    --> RadarModeBistaticReceiverSearchTrack<>
    --> RadarModeBistaticReceiverSar<>
    --> RadarWaveformMonostaticSearchTrackContinuous<>
    --> RadarWaveformMonostaticSearchTrackFixedPRF<>
    --> RadarMultifunctionDetectionProcessing<>
    --> RadarWaveformBistaticTransmitterSearchTrackContinuous<>
    --> RadarWaveformBistaticTransmitterSearchTrackFixedPRF<>
    --> RadarWaveformBistaticReceiverSearchTrackContinuous<>
    --> RadarWaveformBistaticReceiverSearchTrackFixedPRF<>
    --> RadarWaveformSearchTrackPulseDefinition<>
    --> RadarModulator<>
    --> RadarProbabilityOfDetection<>
    --> RadarProbabilityOfDetectionCFAR<>
    --> RadarProbabilityOfDetectionNonCFAR<>
    --> RadarProbabilityOfDetectionPlugin<>
    --> RadarProbabilityOfDetectionCFARCellAveraging<>
    --> RadarProbabilityOfDetectionCFAROrderedStatistics<>
    --> RadarPulseIntegrationGoalSNR<>
    --> RadarPulseIntegrationFixedNumberOfPulses<>
    --> RadarContinuousWaveAnalysisModeGoalSNR<>
    --> RadarContinuousWaveAnalysisModeFixedTime<>
    --> RadarWaveformSarPulseDefinition<>
    --> RadarWaveformSarPulseIntegration<>
    --> RadarTransmitter<>
    --> RadarTransmitterMultifunction<>
    --> RadarReceiver<>
    --> AdditionalGainLoss<>
    --> AdditionalGainLossCollection<>
    --> Polarization<>
    --> PolarizationElliptical<>
    --> ReceivePolarizationElliptical<>
    --> PolarizationLHC<>
    --> PolarizationRHC<>
    --> ReceivePolarizationLHC<>
    --> ReceivePolarizationRHC<>
    --> PolarizationLinear<>
    --> ReceivePolarizationLinear<>
    --> PolarizationHorizontal<>
    --> ReceivePolarizationHorizontal<>
    --> PolarizationVertical<>
    --> ReceivePolarizationVertical<>
    --> RadarClutter<>
    --> RadarClutterGeometry<>
    --> ScatteringPointProviderCollectionElement<>
    --> ScatteringPointProviderCollection<>
    --> ScatteringPointProviderList<>
    --> ScatteringPointProvider<>
    --> ScatteringPointProviderSinglePoint<>
    --> ScatteringPointCollectionElement<>
    --> ScatteringPointCollection<>
    --> ScatteringPointProviderPointsFile<>
    --> ScatteringPointProviderRangeOverCFARCells<>
    --> ScatteringPointProviderSmoothOblateEarth<>
    --> ScatteringPointProviderPlugin<>
    --> CRPluginConfiguration<>
    --> RadarJamming<>
    --> RFInterference<>
    --> RFFilterModel<>
    --> RFFilterModelBessel<>
    --> RFFilterModelSincEnvSinc<>
    --> RFFilterModelElliptic<>
    --> RFFilterModelChebyshev<>
    --> RFFilterModelCosineWindow<>
    --> RFFilterModelGaussianWindow<>
    --> RFFilterModelHammingWindow<>
    --> RFFilterModelButterworth<>
    --> RFFilterModelExternal<>
    --> RFFilterModelScriptPlugin<>
    --> RFFilterModelSinc<>
    --> RFFilterModelRaisedCosine<>
    --> RFFilterModelRootRaisedCosine<>
    --> RFFilterModelRcLowPass<>
    --> RFFilterModelRectangular<>
    --> RFFilterModelFirBoxCar<>
    --> RFFilterModelIir<>
    --> RFFilterModelFir<>
    --> SystemNoiseTemperature<>
    --> AntennaNoiseTemperature<>
    --> Atmosphere<>
    --> LaserPropagationLossModels<>
    --> LaserAtmosphericLossModel<>
    --> LaserAtmosphericLossModelBeerBouguerLambertLaw<>
    --> ModtranLookupTablePropagationModel<>
    --> ModtranPropagationModel<>
    --> LaserTroposphericScintillationLossModel<>
    --> AtmosphericTurbulenceModel<>
    --> AtmosphericTurbulenceModelConstant<>
    --> AtmosphericTurbulenceModelHufnagelValley<>
    --> LaserTroposphericScintillationLossModelITURP1814<>
    --> AtmosphericAbsorptionModel<>
    --> AtmosphericAbsorptionModelITURP676_9<>
    --> AtmosphericAbsorptionModelVoacap<>
    --> AtmosphericAbsorptionModelTirem320<>
    --> AtmosphericAbsorptionModelTirem331<>
    --> AtmosphericAbsorptionModelTirem550<>
    --> AtmosphericAbsorptionModelSimpleSatcom<>
    --> AtmosphericAbsorptionModelScriptPlugin<>
    --> AtmosphericAbsorptionModelCOMPlugin<>
    --> ScatteringPointModel<>
    --> ScatteringPointModelPlugin<>
    --> ScatteringPointModelConstantCoefficient<>
    --> ScatteringPointModelWindTurbine<>
    --> RadarCrossSection<>
    --> RadarCrossSectionModel<>
    --> RadarCrossSectionInheritable<>
    --> RadarCrossSectionFrequencyBand<>
    --> RadarCrossSectionFrequencyBandCollection<>
    --> RadarCrossSectionComputeStrategy<>
    --> RadarCrossSectionComputeStrategyConstantValue<>
    --> RadarCrossSectionComputeStrategyScriptPlugin<>
    --> RadarCrossSectionComputeStrategyExternalFile<>
    --> RadarCrossSectionComputeStrategyAnsysCsvFile<>
    --> RadarCrossSectionComputeStrategyPlugin<>
    --> CustomPropagationModel<>
    --> PropagationChannel<>
    --> RFEnvironment<>
    --> LaserEnvironment<>
    --> ObjectRFEnvironment<>
    --> ObjectLaserEnvironment<>
    --> PlatformLaserEnvironment<>
    --> RainLossModel<>
    --> RainLossModelITURP618_12<>
    --> RainLossModelITURP618_13<>
    --> RainLossModelITURP618_10<>
    --> RainLossModelCrane1985<>
    --> RainLossModelCrane1982<>
    --> RainLossModelCCIR1983<>
    --> RainLossModelScriptPlugin<>
    --> CloudsAndFogFadingLossModel<>
    --> CloudsAndFogFadingLossModelP840_6<>
    --> CloudsAndFogFadingLossModelP840_7<>
    --> TroposphericScintillationFadingLossModel<>
    --> TroposphericScintillationFadingLossModelP618_8<>
    --> TroposphericScintillationFadingLossModelP618_12<>
    --> IonosphericFadingLossModel<>
    --> IonosphericFadingLossModelP531_13<>
    --> UrbanTerrestrialLossModel<>
    --> UrbanTerrestrialLossModelTwoRay<>
    --> UrbanTerrestrialLossModelWirelessInSite64<>
    --> WirelessInSite64GeometryData<>
    --> PointingStrategy<>
    --> PointingStrategyFixed<>
    --> PointingStrategySpinning<>
    --> PointingStrategyTargeted<>
    --> CRLocation<>
    --> CRComplex<>
    --> CRComplexCollection<>
    --> ModulatorModel<>
    --> ModulatorModelBpsk<>
    --> ModulatorModelQpsk<>
    --> ModulatorModelExternalSource<>
    --> ModulatorModelExternal<>
    --> ModulatorModelQam16<>
    --> ModulatorModelQam32<>
    --> ModulatorModelQam64<>
    --> ModulatorModelQam128<>
    --> ModulatorModelQam256<>
    --> ModulatorModelQam1024<>
    --> ModulatorModel8psk<>
    --> ModulatorModel16psk<>
    --> ModulatorModelMsk<>
    --> ModulatorModelBoc<>
    --> ModulatorModelDpsk<>
    --> ModulatorModelFsk<>
    --> ModulatorModelNfsk<>
    --> ModulatorModelOqpsk<>
    --> ModulatorModelNarrowbandUniform<>
    --> ModulatorModelWidebandUniform<>
    --> ModulatorModelWidebandGaussian<>
    --> ModulatorModelPulsedSignal<>
    --> ModulatorModelScriptPluginCustomPsd<>
    --> ModulatorModelScriptPluginIdealPsd<>
    --> LinkMargin<>
    --> DemodulatorModel<>
    --> DemodulatorModelBpsk<>
    --> DemodulatorModelQpsk<>
    --> DemodulatorModelExternalSource<>
    --> DemodulatorModelExternal<>
    --> DemodulatorModelQam16<>
    --> DemodulatorModelQam32<>
    --> DemodulatorModelQam64<>
    --> DemodulatorModelQam128<>
    --> DemodulatorModelQam256<>
    --> DemodulatorModelQam1024<>
    --> DemodulatorModel8psk<>
    --> DemodulatorModel16psk<>
    --> DemodulatorModelMsk<>
    --> DemodulatorModelBoc<>
    --> DemodulatorModelDpsk<>
    --> DemodulatorModelFsk<>
    --> DemodulatorModelNfsk<>
    --> DemodulatorModelOqpsk<>
    --> DemodulatorModelNarrowbandUniform<>
    --> DemodulatorModelWidebandUniform<>
    --> DemodulatorModelWidebandGaussian<>
    --> DemodulatorModelPulsedSignal<>
    --> DemodulatorModelScriptPlugin<>
    --> TransferFunctionPolynomialCollection<>
    --> TransferFunctionInputBackOffCOverImTableRow<>
    --> TransferFunctionInputBackOffCOverImTable<>
    --> TransferFunctionInputBackOffOutputBackOffTableRow<>
    --> TransferFunctionInputBackOffOutputBackOffTable<>
    --> BeerBouguerLambertLawLayer<>
    --> BeerBouguerLambertLawLayerCollection<>
    --> RadarActivity<>
    --> RadarActivityAlwaysActive<>
    --> RadarActivityAlwaysInactive<>
    --> RadarActivityTimeComponentListElement<>
    --> RadarActivityTimeComponentListCollection<>
    --> RadarActivityTimeComponentList<>
    --> RadarActivityTimeIntervalListElement<>
    --> RadarActivityTimeIntervalListCollection<>
    --> RadarActivityTimeIntervalList<>
    --> RadarAntennaBeam<>
    --> RadarAntennaBeamCollection<>
    --> AntennaSystem<>
    --> AntennaBeam<>
    --> AntennaBeamTransmit<>
    --> AntennaBeamCollection<>
    --> AntennaBeamSelectionStrategy<>
    --> AntennaBeamSelectionStrategyAggregate<>
    --> AntennaBeamSelectionStrategyMaxGain<>
    --> AntennaBeamSelectionStrategyMinBoresightAngle<>
    --> AntennaBeamSelectionStrategyScriptPlugin<>
    --> CommSystem<>
    --> CommSystemGraphics<>
    --> CommSystemGraphics3D<>
    --> CommSystemAccessOptions<>
    --> CommSystemAccessEventDetection<>
    --> CommSystemAccessEventDetectionSubsample<>
    --> CommSystemAccessEventDetectionSamplesOnly<>
    --> CommSystemAccessSamplingMethod<>
    --> CommSystemAccessSamplingMethodFixed<>
    --> CommSystemAccessSamplingMethodAdaptive<>
    --> CommSystemLinkSelectionCriteria<>
    --> CommSystemLinkSelectionCriteriaMinimumRange<>
    --> CommSystemLinkSelectionCriteriaMaximumElevation<>
    --> CommSystemLinkSelectionCriteriaScriptPlugin<>
    --> ComponentDirectory<>
    --> ComponentInfo<>
    --> ComponentInfoCollection<>
    --> ComponentAttrLinkEmbedControl<>
    --> Volumetric<>
    --> VmGridSpatialCalculation<>
    --> VmExternalFile<>
    --> VmAnalysisInterval<>
    --> VmAdvanced<>
    --> VmGraphics3D<>
    --> VmGraphics3DGrid<>
    --> VmGraphics3DCrossSection<>
    --> VmGraphics3DCrossSectionPlane<>
    --> VmGraphics3DCrossSectionPlaneCollection<>
    --> VmGraphics3DVolume<>
    --> VmGraphics3DActiveGridPoints<>
    --> VmGraphics3DSpatialCalculationLevels<>
    --> VmGraphics3DSpatialCalculationLevel<>
    --> VmGraphics3DSpatialCalculationLevelCollection<>
    --> VmGraphics3DLegend<>
    --> VmExportTool<>
    --> SatelliteCollection<>
    --> Subset<>
    --> ElementConfiguration<>
    --> ElementConfigurationCircular<>
    --> ElementConfigurationLinear<>
    --> ElementConfigurationAsciiFile<>
    --> ElementConfigurationHfssEepFile<>
    --> ElementConfigurationPolygon<>
    --> ElementConfigurationHexagon<>
    --> SolarActivityConfiguration<>
    --> SolarActivityConfigurationSunspotNumber<>
    --> SolarActivityConfigurationSolarFlux<>
    --> Beamformer<>
    --> BeamformerAsciiFile<>
    --> BeamformerMvdr<>
    --> BeamformerUniform<>
    --> BeamformerBlackmanHarris<>
    --> BeamformerCosine<>
    --> BeamformerCosineX<>
    --> BeamformerCustomTaperFile<>
    --> BeamformerDolphChebyshev<>
    --> BeamformerHamming<>
    --> BeamformerHann<>
    --> BeamformerRaisedCosine<>
    --> BeamformerRaisedCosineSquared<>
    --> BeamformerScript<>
    --> DirectionProvider<>
    --> DirectionProviderAsciiFile<>
    --> DirectionProviderObject<>
    --> DirectionProviderLink<>
    --> DirectionProviderScript<>
    --> Element<>
    --> ElementCollection<>
    --> KeyValueCollection<>
    --> RadarStcAttenuation<>
    --> RadarStcAttenuationDecayFactor<>
    --> RadarStcAttenuationDecaySlope<>
    --> RadarStcAttenuationMapRange<>
    --> RadarStcAttenuationMapAzimuthRange<>
    --> RadarStcAttenuationMapElevationRange<>
    --> RadarStcAttenuationPlugin<>
    --> SensorPointingAlongVector<>
    --> SensorPointingSchedule<>
    --> AccessConstraintAnalysisWorkbenchCollection<>
    --> AccessConstraintAnalysisWorkbench<>
    --> Graphics3DArticulationFile<>
    --> DataProviderResultStatisticResult<>
    --> DataProviderResultTimeVaryingExtremumResult<>
    --> DataProviderResultStatistics<>
    --> Graphics3DModelGltfImageBased<>
    --> StkObjectCutCopyPasteEventArgs<>
    --> StkPreferencesPythonPlugins<>
    --> PathCollection<>
    --> AdvCAT<>
    --> AdvCATAvailableObjectCollection<>
    --> AdvCATChosenObject<>
    --> AdvCATChosenObjectCollection<>
    --> AdvCATPreFilters<>
    --> AdvCATAdvancedEllipsoid<>
    --> AdvCATAdvanced<>
    --> AdvCATGraphics3D<>
    --> EOIRShapeObject<>
    --> EOIRShapeBox<>
    --> EOIRShapeCone<>
    --> EOIRShapeCylinder<>
    --> EOIRShapePlate<>
    --> EOIRShapeSphere<>
    --> EOIRShapeCoupler<>
    --> EOIRShapeNone<>
    --> EOIRShapeGEOComm<>
    --> EOIRShapeLEOComm<>
    --> EOIRShapeLEOImaging<>
    --> EOIRShapeCustomMesh<>
    --> EOIRShapeTargetSignature<>
    --> EOIRStagePlume<>
    --> EOIRShape<>
    --> EOIRShapeCollection<>
    --> EOIRMaterialElement<>
    --> EOIRMaterialElementCollection<>
    --> EOIRStage<>
    --> EOIR<>
    --> MissileEOIR<>
    --> VehicleEOIR<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CONSTANTS<CONSTANTS>
    ≔ HELP_CONTEXT_IDS<HELP_CONTEXT_IDS>
    ≔ ERROR_CODES<ERROR_CODES>
    ≔ ABERRATION_TYPE<ABERRATION_TYPE>
    ≔ ANIMATION_MODES<ANIMATION_MODES>
    ≔ ANIMATION_OPTIONS<ANIMATION_OPTIONS>
    ≔ ANIMATION_ACTIONS<ANIMATION_ACTIONS>
    ≔ ANIMATION_DIRECTIONS<ANIMATION_DIRECTIONS>
    ≔ AZ_EL_MASK_TYPE<AZ_EL_MASK_TYPE>
    ≔ ACTION_TYPE<ACTION_TYPE>
    ≔ AXIS_OFFSET<AXIS_OFFSET>
    ≔ DATA_PROVIDER_RESULT_CATEGORIES<DATA_PROVIDER_RESULT_CATEGORIES>
    ≔ DATA_PROVIDER_TYPE<DATA_PROVIDER_TYPE>
    ≔ DATA_PROVIDER_ELEMENT_TYPE<DATA_PROVIDER_ELEMENT_TYPE>
    ≔ ACCESS_TIME_TYPE<ACCESS_TIME_TYPE>
    ≔ ALTITUDE_REFERENCE_TYPE<ALTITUDE_REFERENCE_TYPE>
    ≔ TERRAIN_NORM_TYPE<TERRAIN_NORM_TYPE>
    ≔ LIGHTING_OBSTRUCTION_MODEL_TYPE<LIGHTING_OBSTRUCTION_MODEL_TYPE>
    ≔ DISPLAY_TIMES_TYPE<DISPLAY_TIMES_TYPE>
    ≔ AREA_TYPE<AREA_TYPE>
    ≔ TRAJECTORY_TYPE<TRAJECTORY_TYPE>
    ≔ OFFSET_FRAME_TYPE<OFFSET_FRAME_TYPE>
    ≔ SCENARIO_3D_POINT_SIZE<SCENARIO_3D_POINT_SIZE>
    ≔ TERRAIN_FILE_TYPE<TERRAIN_FILE_TYPE>
    ≔ TILESET_3D_SOURCE_TYPE<TILESET_3D_SOURCE_TYPE>
    ≔ MARKER_TYPE<MARKER_TYPE>
    ≔ VECTOR_AXES_CONNECT_TYPE<VECTOR_AXES_CONNECT_TYPE>
    ≔ GRAPHICS_3D_MARKER_ORIGIN_TYPE<GRAPHICS_3D_MARKER_ORIGIN_TYPE>
    ≔ GRAPHICS_3D_LABEL_SWAP_DISTANCE<GRAPHICS_3D_LABEL_SWAP_DISTANCE>
    ≔ PLANET_POSITION_SOURCE_TYPE<PLANET_POSITION_SOURCE_TYPE>
    ≔ EPHEM_SOURCE_TYPE<EPHEM_SOURCE_TYPE>
    ≔ PLANET_ORBIT_DISPLAY_TYPE<PLANET_ORBIT_DISPLAY_TYPE>
    ≔ SCENARIO_END_LOOP_TYPE<SCENARIO_END_LOOP_TYPE>
    ≔ SCENARIO_REFRESH_DELTA_TYPE<SCENARIO_REFRESH_DELTA_TYPE>
    ≔ SENSOR_PATTERN<SENSOR_PATTERN>
    ≔ SENSOR_POINTING<SENSOR_POINTING>
    ≔ SENSOR_POINTING_TARGETED_BORESIGHT_TYPE<SENSOR_POINTING_TARGETED_BORESIGHT_TYPE>
    ≔ BORESIGHT_TYPE<BORESIGHT_TYPE>
    ≔ TRACK_MODE_TYPE<TRACK_MODE_TYPE>
    ≔ SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE<SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE>
    ≔ SENSOR_REFRACTION_TYPE<SENSOR_REFRACTION_TYPE>
    ≔ SENSOR_PROJECTION_DISTANCE_TYPE<SENSOR_PROJECTION_DISTANCE_TYPE>
    ≔ SENSOR_LOCATION<SENSOR_LOCATION>
    ≔ SCENARIO_TIME_STEP_TYPE<SCENARIO_TIME_STEP_TYPE>
    ≔ NOTE_SHOW_TYPE<NOTE_SHOW_TYPE>
    ≔ GEOMETRIC_ELEM_TYPE<GEOMETRIC_ELEM_TYPE>
    ≔ SENSOR_SCAN_MODE<SENSOR_SCAN_MODE>
    ≔ CONSTRAINT_BACKGROUND<CONSTRAINT_BACKGROUND>
    ≔ CONSTRAINT_GROUND_TRACK<CONSTRAINT_GROUND_TRACK>
    ≔ INTERSECTION_TYPE<INTERSECTION_TYPE>
    ≔ CONSTRAINT_LIGHTING<CONSTRAINT_LIGHTING>
    ≔ SENSOR_GRAPHICS_3D_PROJECTION_TYPE<SENSOR_GRAPHICS_3D_PROJECTION_TYPE>
    ≔ SENSOR_GRAPHICS_3D_PULSE_STYLE<SENSOR_GRAPHICS_3D_PULSE_STYLE>
    ≔ SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET<SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET>
    ≔ LINE_WIDTH<LINE_WIDTH>
    ≔ STK_OBJECT_TYPE<STK_OBJECT_TYPE>
    ≔ ACCESS_CONSTRAINTS<ACCESS_CONSTRAINTS>
    ≔ BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE<BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE>
    ≔ SHADOW_MODEL<SHADOW_MODEL>
    ≔ METHOD_TO_COMPUTE_SUN_POSITION<METHOD_TO_COMPUTE_SUN_POSITION>
    ≔ ATMOSPHERIC_DENSITY_MODEL<ATMOSPHERIC_DENSITY_MODEL>
    ≔ MARKER_SHAPE_3D<MARKER_SHAPE_3D>
    ≔ LEAD_TRAIL_DATA<LEAD_TRAIL_DATA>
    ≔ TICK_DATA<TICK_DATA>
    ≔ LOAD_METHOD_TYPE<LOAD_METHOD_TYPE>
    ≔ LLA_POSITION_TYPE<LLA_POSITION_TYPE>
    ≔ VEHICLE_GRAPHICS_2D_PASS<VEHICLE_GRAPHICS_2D_PASS>
    ≔ VEHICLE_GRAPHICS_2D_VISIBLE_SIDES<VEHICLE_GRAPHICS_2D_VISIBLE_SIDES>
    ≔ VEHICLE_GRAPHICS_2D_OFFSET<VEHICLE_GRAPHICS_2D_OFFSET>
    ≔ VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE<VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE>
    ≔ VEHICLE_GRAPHICS_2D_ATTRIBUTES<VEHICLE_GRAPHICS_2D_ATTRIBUTES>
    ≔ VEHICLE_GRAPHICS_2D_ELEVATION<VEHICLE_GRAPHICS_2D_ELEVATION>
    ≔ VEHICLE_GRAPHICS_2D_OPTIONS<VEHICLE_GRAPHICS_2D_OPTIONS>
    ≔ MODEL_TYPE<MODEL_TYPE>
    ≔ VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE<VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE>
    ≔ VEHICLE_GRAPHICS_3D_SIGMA_SCALE<VEHICLE_GRAPHICS_3D_SIGMA_SCALE>
    ≔ VEHICLE_GRAPHICS_3D_ATTRIBUTES<VEHICLE_GRAPHICS_3D_ATTRIBUTES>
    ≔ ROUTE_GRAPHICS_3D_MARKER_TYPE<ROUTE_GRAPHICS_3D_MARKER_TYPE>
    ≔ VEHICLE_ELLIPSE_OPTIONS<VEHICLE_ELLIPSE_OPTIONS>
    ≔ VEHICLE_PROPAGATOR_TYPE<VEHICLE_PROPAGATOR_TYPE>
    ≔ VEHICLE_SGP4_SWITCH_METHOD<VEHICLE_SGP4_SWITCH_METHOD>
    ≔ VEHICLE_SGP4TLE_SELECTION<VEHICLE_SGP4TLE_SELECTION>
    ≔ VEHICLE_SGP4_AUTO_UPDATE_SOURCE<VEHICLE_SGP4_AUTO_UPDATE_SOURCE>
    ≔ THIRD_BODY_GRAV_SOURCE_TYPE<THIRD_BODY_GRAV_SOURCE_TYPE>
    ≔ VEHICLE_GEOMAG_FLUX_SRC<VEHICLE_GEOMAG_FLUX_SRC>
    ≔ VEHICLE_GEOMAG_FLUX_UPDATE_RATE<VEHICLE_GEOMAG_FLUX_UPDATE_RATE>
    ≔ VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE<VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE>
    ≔ VEHICLE_INTEGRATION_MODEL<VEHICLE_INTEGRATION_MODEL>
    ≔ VEHICLE_PREDICTOR_CORRECTOR_SCHEME<VEHICLE_PREDICTOR_CORRECTOR_SCHEME>
    ≔ VEHICLE_METHOD<VEHICLE_METHOD>
    ≔ VEHICLE_INTERPOLATION_METHOD<VEHICLE_INTERPOLATION_METHOD>
    ≔ VEHICLE_FRAME<VEHICLE_FRAME>
    ≔ VEHICLE_CORRELATION_LIST_TYPE<VEHICLE_CORRELATION_LIST_TYPE>
    ≔ VEHICLE_CONSIDER_ANALYSIS_TYPE<VEHICLE_CONSIDER_ANALYSIS_TYPE>
    ≔ VEHICLE_WAYPOINT_COMP_METHOD<VEHICLE_WAYPOINT_COMP_METHOD>
    ≔ VEHICLE_ALTITUDE_REFERENCE<VEHICLE_ALTITUDE_REFERENCE>
    ≔ VEHICLE_WAYPOINT_INTERP_METHOD<VEHICLE_WAYPOINT_INTERP_METHOD>
    ≔ VEHICLE_LAUNCH<VEHICLE_LAUNCH>
    ≔ VEHICLE_IMPACT<VEHICLE_IMPACT>
    ≔ VEHICLE_LAUNCH_CONTROL<VEHICLE_LAUNCH_CONTROL>
    ≔ VEHICLE_IMPACT_LOCATION<VEHICLE_IMPACT_LOCATION>
    ≔ VEHICLE_PASS_NUMBERING<VEHICLE_PASS_NUMBERING>
    ≔ VEHICLE_PARTIAL_PASS_MEASUREMENT<VEHICLE_PARTIAL_PASS_MEASUREMENT>
    ≔ VEHICLE_COORDINATE_SYSTEM<VEHICLE_COORDINATE_SYSTEM>
    ≔ VEHICLE_BREAK_ANGLE_TYPE<VEHICLE_BREAK_ANGLE_TYPE>
    ≔ VEHICLE_DIRECTION<VEHICLE_DIRECTION>
    ≔ GRAPHICS_3D_LOCATION<GRAPHICS_3D_LOCATION>
    ≔ GRAPHICS_3D_X_ORIGIN<GRAPHICS_3D_X_ORIGIN>
    ≔ GRAPHICS_3D_Y_ORIGIN<GRAPHICS_3D_Y_ORIGIN>
    ≔ GRAPHICS_3D_FONT_SIZE<GRAPHICS_3D_FONT_SIZE>
    ≔ AIRCRAFT_WGS84_WARNING_TYPE<AIRCRAFT_WGS84_WARNING_TYPE>
    ≔ SURFACE_REFERENCE<SURFACE_REFERENCE>
    ≔ GRAPHICS_3D_FORMAT<GRAPHICS_3D_FORMAT>
    ≔ ATTITUDE_STANDARD_TYPE<ATTITUDE_STANDARD_TYPE>
    ≔ VEHICLE_ATTITUDE<VEHICLE_ATTITUDE>
    ≔ VEHICLE_PROFILE<VEHICLE_PROFILE>
    ≔ VEHICLE_LOOK_AHEAD_METHOD<VEHICLE_LOOK_AHEAD_METHOD>
    ≔ VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION<VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION>
    ≔ SENSOR_ALTITUDE_CROSSING_SIDES<SENSOR_ALTITUDE_CROSSING_SIDES>
    ≔ SENSOR_ALTITUDE_CROSSING_DIRECTION<SENSOR_ALTITUDE_CROSSING_DIRECTION>
    ≔ SENSOR_GRAPHICS_3D_INHERIT_FROM_2D<SENSOR_GRAPHICS_3D_INHERIT_FROM_2D>
    ≔ SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE<SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE>
    ≔ CHAIN_TIME_PERIOD_TYPE<CHAIN_TIME_PERIOD_TYPE>
    ≔ CHAIN_CONST_CONSTRAINTS_MODE<CHAIN_CONST_CONSTRAINTS_MODE>
    ≔ CHAIN_COV_ASSET_MODE<CHAIN_COV_ASSET_MODE>
    ≔ CHAIN_PARENT_PLATFORM_RESTRICTION<CHAIN_PARENT_PLATFORM_RESTRICTION>
    ≔ CHAIN_OPTIMAL_STRAND_METRIC_TYPE<CHAIN_OPTIMAL_STRAND_METRIC_TYPE>
    ≔ CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE<CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE>
    ≔ CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE<CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE>
    ≔ CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE<CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE>
    ≔ DATA_SAVE_MODE<DATA_SAVE_MODE>
    ≔ COVERAGE_BOUNDS<COVERAGE_BOUNDS>
    ≔ COVERAGE_POINT_LOC_METHOD<COVERAGE_POINT_LOC_METHOD>
    ≔ COVERAGE_POINT_ALTITUDE_METHOD<COVERAGE_POINT_ALTITUDE_METHOD>
    ≔ COVERAGE_GRID_CLASS<COVERAGE_GRID_CLASS>
    ≔ COVERAGE_ALTITUDE_METHOD<COVERAGE_ALTITUDE_METHOD>
    ≔ COVERAGE_GROUND_ALTITUDE_METHOD<COVERAGE_GROUND_ALTITUDE_METHOD>
    ≔ COVERAGE_DATA_RETENTION<COVERAGE_DATA_RETENTION>
    ≔ COVERAGE_REGION_ACCESS_ACCEL<COVERAGE_REGION_ACCESS_ACCEL>
    ≔ COVERAGE_RESOLUTION<COVERAGE_RESOLUTION>
    ≔ COVERAGE_ASSET_STATUS<COVERAGE_ASSET_STATUS>
    ≔ COVERAGE_ASSET_GROUPING<COVERAGE_ASSET_GROUPING>
    ≔ FIGURE_OF_MERIT_DEFINITION_TYPE<FIGURE_OF_MERIT_DEFINITION_TYPE>
    ≔ FIGURE_OF_MERIT_SATISFACTION_TYPE<FIGURE_OF_MERIT_SATISFACTION_TYPE>
    ≔ FIGURE_OF_MERIT_CONSTRAINT_NAME<FIGURE_OF_MERIT_CONSTRAINT_NAME>
    ≔ FIGURE_OF_MERIT_COMPUTE<FIGURE_OF_MERIT_COMPUTE>
    ≔ FIGURE_OF_MERIT_ACROSS_ASSETS<FIGURE_OF_MERIT_ACROSS_ASSETS>
    ≔ FIGURE_OF_MERIT_COMPUTE_TYPE<FIGURE_OF_MERIT_COMPUTE_TYPE>
    ≔ FIGURE_OF_MERIT_METHOD<FIGURE_OF_MERIT_METHOD>
    ≔ FIGURE_OF_MERIT_END_GAP_OPTION<FIGURE_OF_MERIT_END_GAP_OPTION>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE<FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD<FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT<FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION<FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION<FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION>
    ≔ FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE<FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE>
    ≔ IV_CLOCK_HOST<IV_CLOCK_HOST>
    ≔ IV_TIME_SENSE<IV_TIME_SENSE>
    ≔ GPS_ATTITUDE_MODEL_TYPE<GPS_ATTITUDE_MODEL_TYPE>
    ≔ CONSTELLATION_CONSTRAINT_RESTRICTION<CONSTELLATION_CONSTRAINT_RESTRICTION>
    ≔ EVENT_DETECTION<EVENT_DETECTION>
    ≔ SAMPLING_METHOD<SAMPLING_METHOD>
    ≔ COVERAGE_SATISFACTION_TYPE<COVERAGE_SATISFACTION_TYPE>
    ≔ CCSDS_REFERENCE_FRAME<CCSDS_REFERENCE_FRAME>
    ≔ CCSDS_DATE_FORMAT<CCSDS_DATE_FORMAT>
    ≔ CCSDS_EPHEM_FORMAT<CCSDS_EPHEM_FORMAT>
    ≔ CCSDS_TIME_SYSTEM<CCSDS_TIME_SYSTEM>
    ≔ STK_EPHEM_COORDINATE_SYSTEM<STK_EPHEM_COORDINATE_SYSTEM>
    ≔ STK_EPHEM_COVARIANCE_TYPE<STK_EPHEM_COVARIANCE_TYPE>
    ≔ EXPORT_TOOL_VERSION_FORMAT<EXPORT_TOOL_VERSION_FORMAT>
    ≔ EXPORT_TOOL_TIME_PERIOD<EXPORT_TOOL_TIME_PERIOD>
    ≔ SPICE_INTERPOLATION<SPICE_INTERPOLATION>
    ≔ ATTITUDE_COORDINATE_AXES<ATTITUDE_COORDINATE_AXES>
    ≔ ATTITUDE_INCLUDE<ATTITUDE_INCLUDE>
    ≔ EXPORT_TOOL_STEP_SIZE<EXPORT_TOOL_STEP_SIZE>
    ≔ TEXT_OUTLINE_STYLE<TEXT_OUTLINE_STYLE>
    ≔ MTO_RANGE_MODE<MTO_RANGE_MODE>
    ≔ MTO_TRACK_EVAL<MTO_TRACK_EVAL>
    ≔ MTO_ENTIRETY<MTO_ENTIRETY>
    ≔ MTO_VISIBILITY_MODE<MTO_VISIBILITY_MODE>
    ≔ MTO_OBJECT_INTERVAL<MTO_OBJECT_INTERVAL>
    ≔ MTO_INPUT_DATA_TYPE<MTO_INPUT_DATA_TYPE>
    ≔ SOLID_TIDE<SOLID_TIDE>
    ≔ TIME_PERIOD_VALUE_TYPE<TIME_PERIOD_VALUE_TYPE>
    ≔ ONE_POINT_ACCESS_STATUS<ONE_POINT_ACCESS_STATUS>
    ≔ ONE_POINT_ACCESS_SUMMARY<ONE_POINT_ACCESS_SUMMARY>
    ≔ LOOK_AHEAD_PROPAGATOR<LOOK_AHEAD_PROPAGATOR>
    ≔ GRAPHICS_3D_MARKER_ORIENTATION<GRAPHICS_3D_MARKER_ORIENTATION>
    ≔ SRP_MODEL<SRP_MODEL>
    ≔ DRAG_MODEL<DRAG_MODEL>
    ≔ VEHICLE_PROPAGATION_FRAME<VEHICLE_PROPAGATION_FRAME>
    ≔ STAR_REFERENCE_FRAME<STAR_REFERENCE_FRAME>
    ≔ GPS_REFERENCE_WEEK<GPS_REFERENCE_WEEK>
    ≔ COVERAGE_CUSTOM_REGION_ALGORITHM<COVERAGE_CUSTOM_REGION_ALGORITHM>
    ≔ VEHICLE_GPS_SWITCH_METHOD<VEHICLE_GPS_SWITCH_METHOD>
    ≔ VEHICLE_GPS_ELEM_SELECTION<VEHICLE_GPS_ELEM_SELECTION>
    ≔ VEHICLE_GPS_AUTO_UPDATE_SOURCE<VEHICLE_GPS_AUTO_UPDATE_SOURCE>
    ≔ VEHICLE_GPS_ALMANAC_TYPE<VEHICLE_GPS_ALMANAC_TYPE>
    ≔ STK_EXTERNAL_EPHEMERIS_FORMAT<STK_EXTERNAL_EPHEMERIS_FORMAT>
    ≔ STK_EXTERNAL_FILE_MESSAGE_LEVEL<STK_EXTERNAL_FILE_MESSAGE_LEVEL>
    ≔ COVERAGE_3D_DRAW_AT_ALTITUDE_MODE<COVERAGE_3D_DRAW_AT_ALTITUDE_MODE>
    ≔ DISTANCE_ON_SPHERE<DISTANCE_ON_SPHERE>
    ≔ FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE<FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE>
    ≔ VEHICLE_SLEW_TIMING_BETWEEN_TARGETS<VEHICLE_SLEW_TIMING_BETWEEN_TARGETS>
    ≔ VEHICLE_SLEW_MODE<VEHICLE_SLEW_MODE>
    ≔ COMPONENT<COMPONENT>
    ≔ VM_DEFINITION_TYPE<VM_DEFINITION_TYPE>
    ≔ VM_SPATIAL_CALC_EVAL_TYPE<VM_SPATIAL_CALC_EVAL_TYPE>
    ≔ VM_SAVE_COMPUTED_DATA_TYPE<VM_SAVE_COMPUTED_DATA_TYPE>
    ≔ VM_DISPLAY_VOLUME_TYPE<VM_DISPLAY_VOLUME_TYPE>
    ≔ VM_DISPLAY_QUALITY_TYPE<VM_DISPLAY_QUALITY_TYPE>
    ≔ VM_LEGEND_NUMERIC_NOTATION<VM_LEGEND_NUMERIC_NOTATION>
    ≔ VM_LEVEL_ORDER<VM_LEVEL_ORDER>
    ≔ SENSOR_EOIR_PROCESSING_LEVELS<SENSOR_EOIR_PROCESSING_LEVELS>
    ≔ SENSOR_EOIR_JITTER_TYPES<SENSOR_EOIR_JITTER_TYPES>
    ≔ SENSOR_EOIR_SCAN_MODES<SENSOR_EOIR_SCAN_MODES>
    ≔ SENSOR_EOIR_BAND_IMAGE_QUALITY<SENSOR_EOIR_BAND_IMAGE_QUALITY>
    ≔ SENSOR_EOIR_BAND_SPECTRAL_SHAPE<SENSOR_EOIR_BAND_SPECTRAL_SHAPE>
    ≔ SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE<SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE>
    ≔ SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS<SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS>
    ≔ SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE<SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE>
    ≔ SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE<SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE>
    ≔ SENSOR_EOIR_BAND_RAD_PARAM_LEVEL<SENSOR_EOIR_BAND_RAD_PARAM_LEVEL>
    ≔ SENSOR_EOIR_BAND_QE_MODE<SENSOR_EOIR_BAND_QE_MODE>
    ≔ SENSOR_EOIR_BAND_QUANTIZATION_MODE<SENSOR_EOIR_BAND_QUANTIZATION_MODE>
    ≔ SENSOR_EOIR_BAND_WAVELENGTH_TYPE<SENSOR_EOIR_BAND_WAVELENGTH_TYPE>
    ≔ SENSOR_EOIR_BAND_SATURATION_MODE<SENSOR_EOIR_BAND_SATURATION_MODE>
    ≔ VM_VOLUME_GRID_EXPORT_TYPE<VM_VOLUME_GRID_EXPORT_TYPE>
    ≔ VM_DATA_EXPORT_FORMAT_TYPE<VM_DATA_EXPORT_FORMAT_TYPE>
    ≔ CONSTELLATION_FROM_TO_PARENT_CONSTRAINT<CONSTELLATION_FROM_TO_PARENT_CONSTRAINT>
    ≔ ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS<ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS>
    ≔ STATISTICS<STATISTICS>
    ≔ TIME_VARYING_EXTREMUM<TIME_VARYING_EXTREMUM>
    ≔ MODEL_GLTF_REFLECTION_MAP_TYPE<MODEL_GLTF_REFLECTION_MAP_TYPE>
    ≔ SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE<SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE>
    ≔ LOP_ATMOSPHERIC_DENSITY_MODEL<LOP_ATMOSPHERIC_DENSITY_MODEL>
    ≔ LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL<LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL>
    ≔ EPHEM_EXPORT_TOOL_FILE_FORMAT<EPHEM_EXPORT_TOOL_FILE_FORMAT>
    ≔ ADV_CAT_ELLIPSOID_CLASS<ADV_CAT_ELLIPSOID_CLASS>
    ≔ ADV_CAT_CONJUNCTION_TYPE<ADV_CAT_CONJUNCTION_TYPE>
    ≔ ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE<ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE>
    ≔ EOIR_SHAPE_TYPE<EOIR_SHAPE_TYPE>
    ≔ EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE<EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE>
    ≔ EOIR_THERMAL_MODEL_TYPE<EOIR_THERMAL_MODEL_TYPE>
    ≔ EOIR_FLIGHT_TYPE<EOIR_FLIGHT_TYPE>
    ≔ COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE<COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE>
    ≔ SWATH_COMPUTATIONAL_METHOD<SWATH_COMPUTATIONAL_METHOD>
    ≔ CLASSICAL_LOCATION<CLASSICAL_LOCATION>
    ≔ ORIENTATION_ASC_NODE<ORIENTATION_ASC_NODE>
    ≔ GEODETIC_SIZE<GEODETIC_SIZE>
    ≔ DELAUNAY_L_TYPE<DELAUNAY_L_TYPE>
    ≔ DELAUNAY_H_TYPE<DELAUNAY_H_TYPE>
    ≔ DELAUNAY_G_TYPE<DELAUNAY_G_TYPE>
    ≔ EQUINOCTIAL_SIZE_SHAPE<EQUINOCTIAL_SIZE_SHAPE>
    ≔ MIXED_SPHERICAL_FPA<MIXED_SPHERICAL_FPA>
    ≔ SPHERICAL_FPA<SPHERICAL_FPA>
    ≔ CLASSICAL_SIZE_SHAPE<CLASSICAL_SIZE_SHAPE>
    ≔ EQUINOCTIAL_FORMULATION<EQUINOCTIAL_FORMULATION>
    ≔ SCATTERING_POINT_PROVIDER_TYPE<SCATTERING_POINT_PROVIDER_TYPE>
    ≔ SCATTERING_POINT_MODEL_TYPE<SCATTERING_POINT_MODEL_TYPE>
    ≔ SCATTERING_POINT_PROVIDER_LIST_TYPE<SCATTERING_POINT_PROVIDER_LIST_TYPE>
    ≔ POLARIZATION_TYPE<POLARIZATION_TYPE>
    ≔ POLARIZATION_REFERENCE_AXIS<POLARIZATION_REFERENCE_AXIS>
    ≔ NOISE_TEMP_COMPUTE_TYPE<NOISE_TEMP_COMPUTE_TYPE>
    ≔ POINTING_STRATEGY_TYPE<POINTING_STRATEGY_TYPE>
    ≔ WAVEFORM_TYPE<WAVEFORM_TYPE>
    ≔ FREQUENCY_SPEC<FREQUENCY_SPEC>
    ≔ PRF_MODE<PRF_MODE>
    ≔ PULSE_WIDTH_MODE<PULSE_WIDTH_MODE>
    ≔ WAVEFORM_SELECTION_STRATEGY_TYPE<WAVEFORM_SELECTION_STRATEGY_TYPE>
    ≔ ANTENNA_CONTROL_REFERENCE_TYPE<ANTENNA_CONTROL_REFERENCE_TYPE>
    ≔ ANTENNA_MODEL_TYPE<ANTENNA_MODEL_TYPE>
    ≔ ANTENNA_CONTOUR_TYPE<ANTENNA_CONTOUR_TYPE>
    ≔ CIRCULAR_APERTURE_INPUT_TYPE<CIRCULAR_APERTURE_INPUT_TYPE>
    ≔ RECTANGULAR_APERTURE_INPUT_TYPE<RECTANGULAR_APERTURE_INPUT_TYPE>
    ≔ DIRECTION_PROVIDER_TYPE<DIRECTION_PROVIDER_TYPE>
    ≔ BEAMFORMER_TYPE<BEAMFORMER_TYPE>
    ≔ ELEMENT_CONFIGURATION_TYPE<ELEMENT_CONFIGURATION_TYPE>
    ≔ LATTICE_TYPE<LATTICE_TYPE>
    ≔ SPACING_UNIT<SPACING_UNIT>
    ≔ LIMITS_EXCEEDED_BEHAVIOR_TYPE<LIMITS_EXCEEDED_BEHAVIOR_TYPE>
    ≔ ANTENNA_GRAPHICS_COORDINATE_SYSTEM<ANTENNA_GRAPHICS_COORDINATE_SYSTEM>
    ≔ ANTENNA_MODEL_INPUT_TYPE<ANTENNA_MODEL_INPUT_TYPE>
    ≔ HFSS_FFD_GAIN_TYPE<HFSS_FFD_GAIN_TYPE>
    ≔ ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE<ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE>
    ≔ BEAM_SELECTION_STRATEGY_TYPE<BEAM_SELECTION_STRATEGY_TYPE>
    ≔ TRANSMITTER_MODEL_TYPE<TRANSMITTER_MODEL_TYPE>
    ≔ TRANSFER_FUNCTION_TYPE<TRANSFER_FUNCTION_TYPE>
    ≔ RE_TRANSMITTER_OP_MODE<RE_TRANSMITTER_OP_MODE>
    ≔ RECEIVER_MODEL_TYPE<RECEIVER_MODEL_TYPE>
    ≔ LINK_MARGIN_TYPE<LINK_MARGIN_TYPE>
    ≔ RADAR_STC_ATTENUATION_TYPE<RADAR_STC_ATTENUATION_TYPE>
    ≔ RADAR_FREQUENCY_SPEC<RADAR_FREQUENCY_SPEC>
    ≔ RADAR_SNR_CONTOUR_TYPE<RADAR_SNR_CONTOUR_TYPE>
    ≔ RADAR_MODEL_TYPE<RADAR_MODEL_TYPE>
    ≔ RADAR_MODE_TYPE<RADAR_MODE_TYPE>
    ≔ RADAR_WAVEFORM_SEARCH_TRACK_TYPE<RADAR_WAVEFORM_SEARCH_TRACK_TYPE>
    ≔ RADAR_SEARCH_TRACK_PRF_MODE<RADAR_SEARCH_TRACK_PRF_MODE>
    ≔ RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE<RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE>
    ≔ RADAR_SAR_PRF_MODE<RADAR_SAR_PRF_MODE>
    ≔ RADAR_SAR_RANGE_RESOLUTION_MODE<RADAR_SAR_RANGE_RESOLUTION_MODE>
    ≔ RADAR_SAR_PCR_MODE<RADAR_SAR_PCR_MODE>
    ≔ RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE<RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE>
    ≔ RADAR_P_DET_TYPE<RADAR_P_DET_TYPE>
    ≔ RADAR_PULSE_INTEGRATION_TYPE<RADAR_PULSE_INTEGRATION_TYPE>
    ≔ RADAR_PULSE_INTEGRATOR_TYPE<RADAR_PULSE_INTEGRATOR_TYPE>
    ≔ RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE<RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE>
    ≔ RADAR_CLUTTER_GEOMETRY_MODEL_TYPE<RADAR_CLUTTER_GEOMETRY_MODEL_TYPE>
    ≔ RADAR_CLUTTER_MAP_MODEL_TYPE<RADAR_CLUTTER_MAP_MODEL_TYPE>
    ≔ RADAR_SWERLING_CASE<RADAR_SWERLING_CASE>
    ≔ RCS_COMPUTE_STRATEGY<RCS_COMPUTE_STRATEGY>
    ≔ RADAR_ACTIVITY_TYPE<RADAR_ACTIVITY_TYPE>
    ≔ RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION<RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION>
    ≔ RF_FILTER_MODEL_TYPE<RF_FILTER_MODEL_TYPE>
    ≔ MODULATOR_MODEL_TYPE<MODULATOR_MODEL_TYPE>
    ≔ DEMODULATOR_MODEL_TYPE<DEMODULATOR_MODEL_TYPE>
    ≔ RAIN_LOSS_MODEL_TYPE<RAIN_LOSS_MODEL_TYPE>
    ≔ ATMOSPHERIC_ABSORPTION_MODEL_TYPE<ATMOSPHERIC_ABSORPTION_MODEL_TYPE>
    ≔ URBAN_TERRESTRIAL_LOSS_MODEL_TYPE<URBAN_TERRESTRIAL_LOSS_MODEL_TYPE>
    ≔ CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE<CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE>
    ≔ CLOUDS_AND_FOG_LIQUID_WATER_CHOICES<CLOUDS_AND_FOG_LIQUID_WATER_CHOICES>
    ≔ IONOSPHERIC_FADING_LOSS_MODEL_TYPE<IONOSPHERIC_FADING_LOSS_MODEL_TYPE>
    ≔ TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE<TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE>
    ≔ TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES<TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES>
    ≔ PROJECTION_HORIZONTAL_DATUM_TYPE<PROJECTION_HORIZONTAL_DATUM_TYPE>
    ≔ BUILD_HEIGHT_REFERENCE_METHOD<BUILD_HEIGHT_REFERENCE_METHOD>
    ≔ BUILD_HEIGHT_UNIT<BUILD_HEIGHT_UNIT>
    ≔ TIREM_POLARIZATION_TYPE<TIREM_POLARIZATION_TYPE>
    ≔ VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE<VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE>
    ≔ VOACAP_COEFFICIENT_DATA_TYPE<VOACAP_COEFFICIENT_DATA_TYPE>
    ≔ LASER_PROPAGATION_LOSS_MODEL_TYPE<LASER_PROPAGATION_LOSS_MODEL_TYPE>
    ≔ LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE<LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE>
    ≔ ATMOSPHERIC_TURBULENCE_MODEL_TYPE<ATMOSPHERIC_TURBULENCE_MODEL_TYPE>
    ≔ MODTRAN_AEROSOL_MODEL_TYPE<MODTRAN_AEROSOL_MODEL_TYPE>
    ≔ MODTRAN_CLOUD_MODEL_TYPE<MODTRAN_CLOUD_MODEL_TYPE>
    ≔ COMM_SYSTEM_REFERENCE_BANDWIDTH<COMM_SYSTEM_REFERENCE_BANDWIDTH>
    ≔ COMM_SYSTEM_CONSTRAINING_ROLE<COMM_SYSTEM_CONSTRAINING_ROLE>
    ≔ COMM_SYSTEM_SAVE_MODE<COMM_SYSTEM_SAVE_MODE>
    ≔ COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE<COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE>
    ≔ COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE<COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE>
    ≔ COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE<COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE>
    ≔ SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY<SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY>
    ≔ SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY<SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY>
    ≔ SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY<SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY>
    ≔ SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE<SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE>
    ≔ SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE<SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE>
    ≔ SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD<SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD>
    ≔ SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD<SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD>
    ≔ SPACE_ENVIRONMENT_SAA_CHANNEL<SPACE_ENVIRONMENT_SAA_CHANNEL>
    ≔ SPACE_ENVIRONMENT_SAA_FLUX_LEVEL<SPACE_ENVIRONMENT_SAA_FLUX_LEVEL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL<VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE<VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE>
    ≔ VEHICLE_SPACE_ENVIRONMENT_MATERIAL<VEHICLE_SPACE_ENVIRONMENT_MATERIAL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE<VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL<VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY<VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE<VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE>
    ≔ VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE<VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE>
    ≔ NOTIFICATION_FILTER_MASK<NOTIFICATION_FILTER_MASK>

