
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
        
            * - :py:obj: aviator

    .. tab-item:: Submodules

        .. list-table::
            :header-rows: 0
            :widths: auto
        
            * - :py:mod: astrogator

             
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~IDataProviderResult`
              - Provide methods to access the results returned by the data provider.

            * - :py:class:`~IDataProviderTimeVarying`
              - Represents the Time-dependent Data Provider (for instance satellite position).

            * - :py:class:`~IDataProviderInterval`
              - Represents the Interval Data Provider (for instance facility lighting times).

            * - :py:class:`~IDataProviderFixed`
              - Represents the Fixed Data Provider (i.e. non time dependent like facility position).

            * - :py:class:`~IDataProviderResultStatistics`
              - Compute statistics and time varying extremums on a data set when available.

            * - :py:class:`~IDataProviderInfo`
              - Provide methods for retrieving the information about data providers.

            * - :py:class:`~IDataProviderCollection`
              - Represents a collection of data providers.

            * - :py:class:`~IDataProviderResultDataSet`
              - Represents a dataset element.

            * - :py:class:`~IDataProviderResultDataSetCollection`
              - Represents a collection of dataset elements.

            * - :py:class:`~IDataProviderResultInterval`
              - Represents a data interval element.

            * - :py:class:`~IDataProviderResultIntervalCollection`
              - Represents a collection of intervals.

            * - :py:class:`~IDataProviderResultSubSection`
              - Represents a sub-section data element.

            * - :py:class:`~IDataProviderResultSubSectionCollection`
              - Represents a collection of sub-section data elements.

            * - :py:class:`~IDataProviderResultTextMessage`
              - Represents notification/failure message returned by the data provider.

            * - :py:class:`~IDataProviderElement`
              - Provide methods to access the information about the element (for instance ``x``).

            * - :py:class:`~IDataProviderElements`
              - Represents a collection of elements in the data provider (for instance ``x``, ``y``, ``z``).

            * - :py:class:`~IDataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :py:class:`~IDataProvider`
              - Represents the Sub Data Provider (i.e. ``Fixed`` in ``Cartesian Position`` group on satellites, or ``Cartesian Position`` on facilities).

            * - :py:class:`~IDataProviders`
              - Represents a collection of data providers.

            * - :py:class:`~IDataProviderGroup`
              - Represents a group of data providers (for instance ``Cartesian Position`` on satellite).

            * - :py:class:`~IDataProviderResultStatisticResult`
              - Represents the results of computing a data set statistics using IAgDrStatistics.ComputeStatistic method.

            * - :py:class:`~IDataProviderResultTimeVaryingExtremumResult`
              - Represents the results of computing a data set time varying extremum using IAgDrStatistics.ComputeTimeVarExtremum method.

            * - :py:class:`~IGraphics3DDataDisplayCollection`
              - Data Display Text.

            * - :py:class:`~IIntervalCollection`
              - AgIntervalCollection used to access the Intervals Collection interface.

            * - :py:class:`~ITimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :py:class:`~IStkObject`
              - Represents the instance of STK object.

            * - :py:class:`~IAccessInterval`
              - Base interface for IAgTimePeriod and IAgIntervalCollection.

            * - :py:class:`~IAccessTimeEventIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :py:class:`~IAccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :py:class:`~IStkAccessGraphics`
              - Provide access to the Graphics for Access Computations.

            * - :py:class:`~IStkAccessAdvanced`
              - Provide access to the Advanced properties for Access Computations.

            * - :py:class:`~IStkAccess`
              - Provide access to the Data Providers and access computations.

            * - :py:class:`~IAccessConstraintCollection`
              - AgAccessConstraintCollection used to access the list of constraints.

            * - :py:class:`~IImmutableIntervalCollection`
              - IAgImmutableIntervalCollection represents a immutable (read-only) collection of intervals.

            * - :py:class:`~IFigureOfMeritDefinition`
              - Figure of Merit definition.

            * - :py:class:`~IFigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~IFigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :py:class:`~IFigureOfMeritGraphics`
              - 2D graphics for a Figure of Merit.

            * - :py:class:`~ICoverageAssetListCollection`
              - Asset List.

            * - :py:class:`~IAvailableFeatures`
              - Define methods to inquiry available and supported features, object types, etc.

            * - :py:class:`~IStkCentralBodyCollection`
              - A collection of available central bodies.

            * - :py:class:`~IStkPreferences`
              - Configures STK preferences.

            * - :py:class:`~IOnePointAccessConstraint`
              - One Point Access Result.

            * - :py:class:`~IOnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :py:class:`~IOnePointAccessResult`
              - One Point Access Result.

            * - :py:class:`~IOnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :py:class:`~IOnePointAccess`
              - One Point Access.

            * - :py:class:`~IKeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :py:class:`~IStkObjectElementCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~IStkObjectCollection`
              - Represents a collection of STK objects.

            * - :py:class:`~IObjectCoverageFigureOfMerit`
              - Provide access to the Figure of Merit on the Object Coverage tool.

            * - :py:class:`~IStkObjectCoverage`
              - Provide access to the Data Providers on an ObjectCoverage Object.

            * - :py:class:`~IStdMilitary2525bSymbols`
              - Represents the automation interface to generate 2525b symbology markers (military standard).

            * - :py:class:`~IStkObjectRoot`
              - Represents the automation interface supported by the root object of the Automation Object Model.

            * - :py:class:`~IObjectLink`
              - IAgObjectLink provides methods and properties of elements stored in IAgObjectLinkCollection collection.

            * - :py:class:`~ILinkToObject`
              - IAgLinkToObject represents a link to STK object.

            * - :py:class:`~IObjectLinkCollection`
              - IAgObjectLinkCollection represents a collection of names of STK objects that are available in the current scenario.

            * - :py:class:`~IAnimation`
              - Provide methods to control scenario animation.

            * - :py:class:`~IStkObjectModelContext`
              - Represents a factory class to create instances of the AgStkObjectRoot class.

            * - :py:class:`~IComponentInfo`
              - Interface for a component.

            * - :py:class:`~IComponentInfoCollection`
              - The collection of components and component folders.

            * - :py:class:`~IComponentDirectory`
              - Manages all components.

            * - :py:class:`~ICloneable`
              - Interface for a component.

            * - :py:class:`~IComponentLinkEmbedControl`
              - Interface for a control which manages the linking or embedding of a component from the component browser.

            * - :py:class:`~ISwath`
              - Provide access to the Swath properties.

            * - :py:class:`~IDisplayTimesData`
              - Base Interface IAgDisplayTimesData. IAgIntervalCollection, IAgDuringAccess and IAgDisplayTimesTimeComponent derive from this.

            * - :py:class:`~IDisplayTime`
              - The display time interface.

            * - :py:class:`~IBasicAzElMask`
              - AgAzElMask Azimuth-elevation access points.

            * - :py:class:`~ILabelNote`
              - AgLabelNote used to access the label note.

            * - :py:class:`~ILabelNoteCollection`
              - AgLabelNoteCollection used to access the list of label notes.

            * - :py:class:`~IDuringAccess`
              - AgDuringAccess used to access the display intervals and Access objects.

            * - :py:class:`~IDisplayTimesTimeComponent`
              - Interface provides methods to configure the display times using Timeline API components.

            * - :py:class:`~ITerrainNormSlopeAzimuth`
              - AgTerrainNormSlopeAzimuth used to access the Slope/Azimuth data for the TerrainNormal.

            * - :py:class:`~IAccessTime`
              - IAgAccessTime Interface, part of the target times scheme for specifying when a satellite or sensor can access a given object.

            * - :py:class:`~IAccessTimeCollection`
              - IAgAccessTimeCollection Interface.

            * - :py:class:`~ITerrainNormData`
              - Base Interface IAgTerrainNormData. IAgTerrainNormSlopeAzimuth derives from this interface.

            * - :py:class:`~ILifetimeInformation`
              - Provide the information about the lifetime of the object.

            * - :py:class:`~IVehicleLeadTrailData`
              - Base interface IAgVeLeadTrailData.

            * - :py:class:`~IVehicleLeadTrailDataFraction`
              - The percentage of the leading or trailing portion of a vehicle's path that will display in the 2D or 3D window.

            * - :py:class:`~IVehicleLeadTrailDataTime`
              - Configure the amount of time to display the vehicle's path in 2D or 3D window.

            * - :py:class:`~IStkCentralBodyEllipsoid`
              - Provide information about the central body's equatorial and polar radii.

            * - :py:class:`~IStkCentralBody`
              - A central body interface.

            * - :py:class:`~IAccessConstraint`
              - AgAccessConstraint used to access the AccessConstraint attributes.

            * - :py:class:`~IAccessConstraintTimeSlipRange`
              - IAgAccessCnstrTimeSlipRange used to access the Time Slip Range.

            * - :py:class:`~IAccessConstraintZone`
              - IAgAccessCnstrZone used to access the Zone access constraints.

            * - :py:class:`~IAccessConstraintExclZonesCollection`
              - AgAccessCnstrExclZonesCollection used to access the Exclusion Zones List interface.

            * - :py:class:`~IAccessConstraintThirdBody`
              - Do not use this interface, as it is deprecated. Use IAgAccessCnstrCbObstruction instead. Access Constraint Used for Third Body Obstructions.

            * - :py:class:`~IAccessConstraintIntervals`
              - Access Constraint used for time intervals.

            * - :py:class:`~IAccessConstraintObjExAngle`
              - Access Constraint used for Object Exclusion Angles.

            * - :py:class:`~IAccessConstraintCondition`
              - Access Constraint used for lighting conditions.

            * - :py:class:`~IAccessConstraintCentralBodyObstruction`
              - Access Constraint used for Central Body Obstruction.

            * - :py:class:`~IAccessConstraintAngle`
              - Access Constraint used for angle constraints.

            * - :py:class:`~IAccessConstraintMinMax`
              - Access Constraint used for min/max constraints.

            * - :py:class:`~IAccessConstraintPluginMinMax`
              - Access Constraint used for min/max plugin constraints.

            * - :py:class:`~IAccessConstraintCrdnConstellation`
              - Access Constraint used for Vector Constraints.

            * - :py:class:`~IAccessConstraintBackground`
              - Access Constraint used for Background Constraints.

            * - :py:class:`~IAccessConstraintGroundTrack`
              - Access Constraint used for GroundTrack Constraints.

            * - :py:class:`~IAccessConstraintAnalysisWorkbench`
              - Access Constraint used for Analysis Workbench Constraints.

            * - :py:class:`~IAccessConstraintAnalysisWorkbenchCollection`
              - IAgAccessCnstrAWBCollection used to access angle, vector and condition constraint List interface.

            * - :py:class:`~IAccessConstraintGrazingAltitude`
              - Access Constraint used for Grazing Altitude Constraint.

            * - :py:class:`~ILevelAttribute`
              - AgLevelAttribute used to access individual contour level attributes.

            * - :py:class:`~ILevelAttributeCollection`
              - AgLevelAttributeCollection used to access level attributes.

            * - :py:class:`~IGraphics2DRangeContours`
              - AgGfxRangeContours used to access contours of 2-d object.

            * - :py:class:`~IGraphics3DModelFile`
              - IAgVOModelFile Interface. Used to specify the model's file.

            * - :py:class:`~IGraphics3DArticulationFile`
              - Interface for VO model articulations.

            * - :py:class:`~IGraphics3DModelGltfImageBased`
              - glTF Reflection Settings Interface.

            * - :py:class:`~IVehicleEllipseDataElement`
              - Ground ellipse data.

            * - :py:class:`~IVehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :py:class:`~IVehicleGroundEllipseElement`
              - Ground ellipse.

            * - :py:class:`~IVehicleGroundEllipsesCollection`
              - Ground Ellipses.

            * - :py:class:`~IGraphics3DDataDisplayElement`
              - Interface for 3D Graphics window data display element.

            * - :py:class:`~IGraphics3DPointableElementsElement`
              - Pointable elements interface for 3D model pointing.

            * - :py:class:`~IGraphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :py:class:`~IGraphics3DModelPointing`
              - List of pointable model elements.

            * - :py:class:`~IGraphics3DLabelSwapDistance`
              - Interface to control the level of detail in labels and other screen objects at specified distances.

            * - :py:class:`~IGraphics3DAzElMask`
              - Use to display labels and adjust the translucency of the azimuth-elevation mask for a facility, place or target.

            * - :py:class:`~IGraphics3DBorderWall`
              - Border Wall Properties.

            * - :py:class:`~IGraphics3DRangeContours`
              - AgVORangeContour used to access the 3D RangeContour attributes.

            * - :py:class:`~IGraphics3DOffsetLabel`
              - AgVOOffsetLabel used to access the 3D Label attributes.

            * - :py:class:`~IGraphics3DOffsetRotate`
              - AgVOOffsetRotate used to access the 3D Rotational attributes.

            * - :py:class:`~IGraphics3DOffsetTransformation`
              - AgVOOffsetTrans used to access the 3D Translational attributes.

            * - :py:class:`~IGraphics3DOffsetAttach`
              - Interface for specifying attach points for the attachment of lines to objects.

            * - :py:class:`~IGraphics3DOffset`
              - AgVOOffset used to access the 3D offset attributes.

            * - :py:class:`~IGraphics3DMarkerData`
              - Base Interface IAgVOMarkerData.

            * - :py:class:`~IGraphics3DMarkerShape`
              - AgVOMarkerShape used to access the 3D markerShape attributes.

            * - :py:class:`~IGraphics3DMarkerFile`
              - AgVOMarkerFile used to access the 3D MarkerFile attributes.

            * - :py:class:`~IGraphics3DMarker`
              - AgVOMarker used to access the Marker values.

            * - :py:class:`~IGraphics3DModelTransformation`
              - IAgVOModelTrans Interface. Used to modify the transformation value.

            * - :py:class:`~IGraphics3DModelTransformationCollection`
              - IAgVOModelTransCollection Interface. A collection of available transformations in the model.

            * - :py:class:`~IGraphics3DModelArtic`
              - ModelArticulation Interface.

            * - :py:class:`~IGraphics3DDetailThreshold`
              - AgVODetailThreshold used to access the 3D DetailThreshold values.

            * - :py:class:`~IGraphics3DModelItem`
              - AgVOModelItem used to access the Model Item in the ModelCollection.

            * - :py:class:`~IGraphics3DModelCollection`
              - IAgVOModelCollection used to access the 3D Model List.

            * - :py:class:`~IGraphics3DModelData`
              - IAgVOModelData base interface. IAgVOModelFile and IAgVOModelCollection derive from this.

            * - :py:class:`~IGraphics3DModel`
              - AgVOModel used to access the 3D model attributes.

            * - :py:class:`~IPointTargetGraphics3DModel`
              - AgPtTargetVOModel used to access the 3D model attributes.

            * - :py:class:`~IGraphics3DReferenceAnalysisWorkbenchComponent`
              - IAgVORefCrdn used to access the shared properties of all 3D RefCrdn.

            * - :py:class:`~IGraphics3DReferenceVectorGeometryToolVector`
              - Configure the visual representation of a Vector Geometry vector component in 3D.

            * - :py:class:`~IGraphics3DReferenceVectorGeometryToolAxes`
              - Configure the visual representation of a Vector Geometry axes component in 3D.

            * - :py:class:`~IGraphics3DReferenceVectorGeometryToolAngle`
              - Configure the visual representation of a Vector Geometry angle component in 3D.

            * - :py:class:`~IGraphics3DReferenceVectorGeometryToolPoint`
              - Configure the visual representation of a Vector Geometry point component in 3D.

            * - :py:class:`~IGraphics3DReferenceVectorGeometryToolPlane`
              - Configure the visual representation of a Vector Geometry plane component in 3D.

            * - :py:class:`~IGraphics3DReferenceAnalysisWorkbenchCollection`
              - Manages the collection of elements that are used to visualize the Vector Geometry Tool components in 3D.

            * - :py:class:`~IGraphics3DVector`
              - Configures the Vector Geometry Tool 3D visualization.

            * - :py:class:`~IGraphics3DVaporTrail`
              - Configure the vapor trail 3D attributes.

            * - :py:class:`~ILLAPosition`
              - Interface to set and retrieve the LLA position type.

            * - :py:class:`~ILLAGeocentric`
              - Geocentric LLA position interface:.

            * - :py:class:`~ILLAGeodetic`
              - Geodetic LLA position interface.

            * - :py:class:`~IOrbitStateCoordinateSystem`
              - Interface for selecting coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :py:class:`~IOrbitStateCartesian`
              - Cartesian coordinate type.

            * - :py:class:`~IClassicalSizeShape`
              - Base Interface for SizeShape property. IAgClassicalSizeShapeAltitude, IAgClassicalSizeShapeMeanMotion, IAgClassicalSizeShapePeriod, IAgClassicalSizeShapeRadius and IAgClassicalSizeShapeSemimajorAxis derive from this.

            * - :py:class:`~IClassicalSizeShapeAltitude`
              - Interface for specifying orbit size and shape using altitude.

            * - :py:class:`~IClassicalSizeShapeMeanMotion`
              - Interface for specifying orbit size and shape using Mean Motion and Eccentricity.

            * - :py:class:`~IClassicalSizeShapePeriod`
              - Interface for specifying orbit size and shape using Period and Eccentricity.

            * - :py:class:`~IClassicalSizeShapeRadius`
              - Interface for specifying orbit size and shape using Radius.

            * - :py:class:`~IClassicalSizeShapeSemimajorAxis`
              - Interface for specifying orbit size and shape using Semimajor Axis and Eccentricity.

            * - :py:class:`~IOrientationAscNode`
              - Base Interface to IAgOrientationAscNodeLAN and IAgOrientationAscNodeRAAN.

            * - :py:class:`~IOrientationAscNodeLAN`
              - Longitude of Ascending Node: the Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :py:class:`~IOrientationAscNodeRAAN`
              - Right Ascension of Ascending Node: the angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :py:class:`~IClassicalOrientation`
              - Interface for specifying orbit orientation in the Classical (Keplerian) system.

            * - :py:class:`~IClassicalLocation`
              - Base Interface of all IAgClassicalLocation* interfaces.

            * - :py:class:`~IClassicalLocationArgumentOfLatitude`
              - Interface for Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~IClassicalLocationEccentricAnomaly`
              - Interface for Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~IClassicalLocationMeanAnomaly`
              - Interface for Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~IClassicalLocationTimePastAN`
              - Interface for Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~IClassicalLocationTimePastPerigee`
              - Interface for Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~IClassicalLocationTrueAnomaly`
              - Interface for True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~IOrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :py:class:`~IGeodeticSize`
              - Base Interface IAgGeodeticSize. IAgGeodeticSizeAltitude and IAgGeodeticSizeRadius derive from this.

            * - :py:class:`~IGeodeticSizeAltitude`
              - Interface for Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :py:class:`~IGeodeticSizeRadius`
              - Interface for Radius and Radius Rate (for Geodetic coordinate type).

            * - :py:class:`~IOrbitStateGeodetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :py:class:`~IDelaunayActionVariable`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~IDelaunayL`
              - Interface for Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~IDelaunayLOverSQRTmu`
              - Interface for Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~IDelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :py:class:`~IDelaunayHOverSQRTmu`
              - Interface for Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~IDelaunayG`
              - Interface for Delaunay Variagle G, the magnitude of the orbital angular momentum.

            * - :py:class:`~IDelaunayGOverSQRTmu`
              - Interface for Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~IOrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :py:class:`~IEquinoctialSizeShapeMeanMotion`
              - Interface for Mean Motion, an element of the Equinoctial coordinate type.

            * - :py:class:`~IEquinoctialSizeShapeSemimajorAxis`
              - Interface for Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :py:class:`~IOrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :py:class:`~IFlightPathAngle`
              - Base Interface IAgFlightPathAngle. IAgMixedSphericalFPAHorizontal, IAgMixedSphericalFPAVertical, IAgSphericalFPAHorizontal and IAgSphericalFPAVertical derive from this.

            * - :py:class:`~IMixedSphericalFPAHorizontal`
              - Interface for Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~IMixedSphericalFPAVertical`
              - Interface for Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~IOrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :py:class:`~ISphericalFPAHorizontal`
              - Interface for Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~ISphericalFPAVertical`
              - Interface for Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~IOrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :py:class:`~ISpatialState`
              - Represents a position and an attitude of an object.

            * - :py:class:`~IVehicleSpatialInfo`
              - Represents a spatial information of the vehicle.

            * - :py:class:`~IProvideSpatialInfo`
              - Provide methods for accessing spatial information for an object.

            * - :py:class:`~IScenSpaceEnvironment`
              - no helpstring provided.

            * - :py:class:`~IRadarClutterMap`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar clutter map.

            * - :py:class:`~IRadarCrossSection`
              - Provide access to the properties and methods defining radar cross section.

            * - :py:class:`~IRFEnvironment`
              - Provide access to the properties and methods defining the RF environment.

            * - :py:class:`~ILaserEnvironment`
              - Provide access to the properties and methods defining the laser environment.

            * - :py:class:`~IScenarioGraphics`
              - IAgScGraphics Interface for Scenario-level 2D Graphics attributes.

            * - :py:class:`~IScenarioEarthData`
              - IAgScEarthData Interface for Earth Orientation Parameters.

            * - :py:class:`~IScenarioAnimationTimePeriod`
              - IAgScAnimationTimePeriod defines methods and properties to configure the scenario's animation time.

            * - :py:class:`~IScenarioAnimation`
              - IAgScAnimation Interface for Scenario-level properties that control the animation cycle, animation step definition and the intervals between refresh updates in the 2D and 3D windows.

            * - :py:class:`~ITerrain`
              - IAgTerrain Interface.

            * - :py:class:`~ITerrainCollection`
              - IAgTerrainCollection lists all the terrain data files available in this scenario for visualization and analysis.

            * - :py:class:`~ICentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :py:class:`~ICentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :py:class:`~ITileset3D`
              - IAg3DTileset Interface.

            * - :py:class:`~ITilesetCollection3D`
              - IAg3DTilesetCollection lists all the terrain data files available in this scenario for visualization and analysis.

            * - :py:class:`~IScenarioGenDatabase`
              - Represents a scenario database.

            * - :py:class:`~IScenarioGenDatabaseCollection`
              - Represents a collection of the scenario's databases.

            * - :py:class:`~IScenario3dFont`
              - IAgSc3dFont Interface.

            * - :py:class:`~IScenarioGraphics3D`
              - Scenario 3D Graphics Attributes.

            * - :py:class:`~ITimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~IScenario`
              - IAgScenario Interface for Scenario-level properties.

            * - :py:class:`~ICelestialBodyInfo`
              - The interface represents information associated with a celestial body.

            * - :py:class:`~ICelestialBodyCollection`
              - Represents a collection of celestial bodies.

            * - :py:class:`~IAccessAdvanced`
              - Interface for configuring advanced targeting access computation properties.

            * - :py:class:`~ISensorAccessAdvanced`
              - Interface for configuring sensor's advanced targeting access computation properties.

            * - :py:class:`~IRefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :py:class:`~IRefractionModelBase`
              - A base interface for the Refraction Models.

            * - :py:class:`~IRefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :py:class:`~IRefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :py:class:`~IRefractionModelSCFMethod`
              - SCF Method.

            * - :py:class:`~IScheduleTime`
              - IAgScheduleTime Interface, part of the target times scheme for specifying when a satellite or sensor can access a given object.

            * - :py:class:`~IScheduleTimeCollection`
              - You can modify the scheduled times by disabling Use Access Times.

            * - :py:class:`~IDisplayDistance`
              - Base interface IAgDisplayDistance. IAgSnProjDisplayDistance, IAgSnProjConstantAlt and IAgSnProjObjectAlt derive from this.

            * - :py:class:`~ISensorProjectionDisplayDistance`
              - IAgSnProjDisplayDistance Interface for setting projection altitude options for a sensor.

            * - :py:class:`~ISensorProjection`
              - IAgSnProjection Interface for setting and retrieving 2D Graphics Projection properties for a sensor.

            * - :py:class:`~ISensorGraphics`
              - IAgSnGraphics Interface for a sensor's 2D Graphics properties.

            * - :py:class:`~ISensorGraphics3DPulse`
              - IAgSnVOPulse Interface, for setting and retrieving 3D Graphics Pulse properties of a sensor.

            * - :py:class:`~ISensorGraphics3DOffset`
              - IAgSnVOOffset Interface for setting and retrieving 3D Graphics Vertex Offset properties of a sensor.

            * - :py:class:`~ISensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :py:class:`~ISensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :py:class:`~ISensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :py:class:`~ISensorGraphics3D`
              - IAgSnVO Interface for a sensor's 3D Graphics properties.

            * - :py:class:`~ISensorPattern`
              - Base interface IAgSnPattern. IAgSnComplexConicPattern, IAgSnCustomPattern, IAgSnHalfPowerPattern, IAgSnRectangularPattern, IAgSnSARPattern, IAgSnEOIRPattern and IAgSnSimpleConicPattern implement this interface.

            * - :py:class:`~ISensorSimpleConicPattern`
              - IAgSnSimpleConicPattern Interface for a sensor pattern defined by a simple cone angle.

            * - :py:class:`~ISensorSARPattern`
              - IAgSnSARPattern Interface for the Synthetic Aperture Radar (SAR) sensor type, designed to model the field of regard of a SAR sensor with respect to the surface of the Earth.

            * - :py:class:`~ISensorRectangularPattern`
              - IAgSnRectangularPattern Interface for rectangular sensor types typically used with satellites or aircraft for modeling the field of view of instruments such as push broom sensors and star trackers.

            * - :py:class:`~ISensorHalfPowerPattern`
              - IAgSnHalfPowerPattern Interface for half power sensors designed to model parabolic antennas.

            * - :py:class:`~ISensorCustomPattern`
              - IAgSnCustomPattern Interface for custom sensor patterns.

            * - :py:class:`~ISensorComplexConicPattern`
              - IAgSnComplexConicPattern Interface for defining sensor patterns by the inner and outer half angles and minimum and maximum clock angles of the sensor's cone.

            * - :py:class:`~ISensorEOIRRadiometricPair`
              - IAgSnEOIRRadiometricPair Interface for defining the individual band properties.

            * - :py:class:`~ISensorEOIRSensitivityCollection`
              - IAgSnEOIRFCollection Interface. A collection of Radiometric pairs defining the Sensitivities.

            * - :py:class:`~ISensorEOIRSaturationCollection`
              - IAgSnEOIRSaturationCollection Interface. A collection of Radiometric pairs defining the saturations.

            * - :py:class:`~ISensorEOIRBand`
              - IAgSnEOIRBand Interface for defining the individual band properties.

            * - :py:class:`~ISensorEOIRBandCollection`
              - IAgSnEOIRBandCollection Interface. A collection of EOIR bands.

            * - :py:class:`~ISensorEOIRPattern`
              - IAgSnEOIRPattern Interface for a sensor pattern.

            * - :py:class:`~ISensorPointingTargetedBoresight`
              - Base interface IAgSnPtTrgtBsight. IAgSnPtTrgtBsightFixed and IAgSnPtTrgtBsightTrack derive from this.

            * - :py:class:`~ISensorPointingTargetedBoresightTrack`
              - IAgSnPtTrgtBsightTrack Interface for targeted sensor with fixed boresight.

            * - :py:class:`~ISensorPointingTargetedBoresightFixed`
              - IAgSnPtTrgtBsightFixed Interface for targeted sensors with fixed boresight.

            * - :py:class:`~ISensorTarget`
              - IAgSnTarget Interface.

            * - :py:class:`~ISensorTargetCollection`
              - IAgSnTargetCollection Interface. A collection of targets.

            * - :py:class:`~ISensorPointing`
              - Base interface IAgSnPointing. IAgSnPt3DModel, IAgSnPtExternal, IAgSnPtFixed, IAgSnPtFixedAxes, IAgSnPtGrazingAlt, IAgSnPtTargeted, IAgSnPtAlongVector and IAgSnPtSchedule implement this interface.

            * - :py:class:`~ISensorPointingTargeted`
              - IAgSnPtTargeted Interface for targeted sensors.

            * - :py:class:`~ISensorPointingSpinning`
              - IAgSnPtSpinning Interface for defining the pointing properties of a spinning sensor.

            * - :py:class:`~ISensorPointingGrazingAltitude`
              - IAgSnPtGrazingAlt Interface for a sensor pointed in such a way that the boresight vector will graze the central body at a specified altitude.

            * - :py:class:`~ISensorPointingFixedAxes`
              - IAgSnPtFixedAxes Interface for sensors pointed with reference to a set of reference axes.

            * - :py:class:`~ISensorPointingFixed`
              - IAgSnPtFixed Interface for sensors that are fixed in the parent object's body coordinate frame, so that they always point in the same direction relative to the parent.

            * - :py:class:`~ISensorPointingExternal`
              - IAgSnPtExternal Interface for antennas oriented with a custom pointing file.

            * - :py:class:`~ISensorPointing3DModel`
              - IAgSnPt3DModel Interface for a sensor with pointing along one of the available elements of a 3D model.

            * - :py:class:`~ISensorPointingAlongVector`
              - IAgSnPtAlongVector Interface for a sensor whose alignment is controlled by a pair of vectors defined using the Vector Geometry tool.

            * - :py:class:`~ISensorPointingSchedule`
              - IAgSnPtSchedule is a placeholder interface to handle Sensor Schedule pointing type. Use Point path/to/sensor Schedule connect command to control scheduled sensor pointing.

            * - :py:class:`~IAzElMaskData`
              - Base interface IAgAzElMaskData. IAgSnAzElMaskFile implements this interface.

            * - :py:class:`~ISensorAzElMaskFile`
              - IAgSnAzElMaskFile Interface.

            * - :py:class:`~ISensorCommonTasks`
              - The common tasks available for the sensor object.

            * - :py:class:`~ILocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :py:class:`~ISensor`
              - Provide access to the properties and methods used in defining a sensor object.

            * - :py:class:`~ISensorProjectionConstantAltitude`
              - IAgSnProjConstantAlt Interface for setting projection altitude options for constant altitude for a sensor.

            * - :py:class:`~ISensorProjectionObjectAltitude`
              - IAgSnProjObjectAlt Interface for setting projection altitude options for object altitude for a sensor.

            * - :py:class:`~IAtmosphere`
              - Provide access to the properties and methods defining the local atmosphere.

            * - :py:class:`~IRadarClutterMapInheritable`
              - Do not use this interface, as it is deprecated. This interface is no longer used and there is no alternative. Provides access to the properties and methods defining a radar inheritable clutter map.

            * - :py:class:`~IRadarCrossSectionInheritable`
              - Provide access to the properties and methods defining a inheritable radar cross section.

            * - :py:class:`~IPlatformLaserEnvironment`
              - Provide access to the properties and methods defining the laser environment for a platform.

            * - :py:class:`~IPlatformRFEnvironment`
              - Provide access to the properties and methods defining the platform RF environment.

            * - :py:class:`~IRadarCrossSectionGraphics3D`
              - IAgRadarCrossSectionVO Interface for radar cross section 3D properties.

            * - :py:class:`~IRadarCrossSectionGraphics`
              - IAgRadarCrossSectionGraphics Interface for radar cross section graphics properties.

            * - :py:class:`~ITargetGraphics`
              - IAgTargetGraphics used to access the 2-d graphics properties for a Target object.

            * - :py:class:`~ITargetGraphics3D`
              - IAgTargetVO Interface. For 3D properties of a Target object.

            * - :py:class:`~ITarget`
              - Provide access to the properties and methods used in defining a target object.

            * - :py:class:`~IAreaTypeEllipse`
              - AgAreaTypeEllipse used to access the MajorAxis MinorAxis and Bearing of the AreaTarget AreaType.

            * - :py:class:`~IAreaTypePatternCollection`
              - AgAreaTypePatternCollection used to access the List of coords of the AreaTarget AreaType.

            * - :py:class:`~IAreaTargetCommonTasks`
              - AreaTarget common tasks.

            * - :py:class:`~IAreaTypeData`
              - Base interface IAgAreaTypeData. IAgAreaTypePatternCollection and IAgAreaTypeEllipse derive from it.

            * - :py:class:`~IAreaTargetGraphics`
              - AgATGraphics used to access the 2D Graphics attributes of an AreaTarget interface.

            * - :py:class:`~IAreaTargetGraphics3D`
              - AgATVO used to access the 3D attributes of an AreaTarget interface.

            * - :py:class:`~IAreaTarget`
              - Provide access to the properties and methods defining an AreaTarget object.

            * - :py:class:`~IAreaTypePattern`
              - AgAreaTypePattern used to access the List of coordinates of the AreaTarget AreaType interface.

            * - :py:class:`~IPlanetPositionFile`
              - IAgPlPosFile Interface.

            * - :py:class:`~IPlanetPositionCentralBody`
              - IAgPlPosCentralBody Interface.

            * - :py:class:`~IPlanetCommonTasks`
              - IAgPlCommonTasks.

            * - :py:class:`~IPositionSourceData`
              - Base interface to IAgPlPosCentralBody and IAgPlPosFile.

            * - :py:class:`~IOrbitDisplayData`
              - IAgOrbitDisplayData Interface. IAgPlOrbitDisplayTime derives from this.

            * - :py:class:`~IPlanetOrbitDisplayTime`
              - IAgPlOrbitDisplayTime Interface.

            * - :py:class:`~IPlanetGraphics`
              - AgPlGraphics used to access the 2D graphics of the planet.

            * - :py:class:`~IPlanetGraphics3D`
              - AgPlVO interface. Used to access the 3D graphics of the planet.

            * - :py:class:`~IPlanet`
              - Provide access to the properties and methods used in defining a planet object.

            * - :py:class:`~IStarGraphics`
              - AgStGraphics used to access the Star's 2D graphics.

            * - :py:class:`~IStarGraphics3D`
              - AgStVO used to access the Star's 3D graphics.

            * - :py:class:`~IStar`
              - Provide access to the properties and methods used in defining a star object.

            * - :py:class:`~IFacilityGraphics`
              - AgFaGraphics used to access the 2D graphics for a Facility object interface.

            * - :py:class:`~IFacilityGraphics3D`
              - AgFaVO Interface. For 3D properties of a Facility object interface.

            * - :py:class:`~IFacility`
              - Provide access to the properties and methods used in defining a facility object.

            * - :py:class:`~IPlaceGraphics`
              - IAgPlaceGraphics used to access the 2-d graphics properties for a Place object.

            * - :py:class:`~IPlaceGraphics3D`
              - IAgPlaceVO Interface. For 3D properties of a Place object.

            * - :py:class:`~IPlace`
              - Provide access to the properties and methods used in defining a place object.

            * - :py:class:`~IAntennaNoiseTemperature`
              - Provide access to the antenna noise temperature parameters.

            * - :py:class:`~ISystemNoiseTemperature`
              - Provide access to the system noise temperature parameters.

            * - :py:class:`~IPolarization`
              - Provide the base interface for the a polarization object.

            * - :py:class:`~IPolarizationElliptical`
              - Provide the interface for elliptical polarization.

            * - :py:class:`~IPolarizationCrossPolLeakage`
              - Provide the interface for polarization cross pol leakage.

            * - :py:class:`~IPolarizationLinear`
              - Provide the interface for linear polarization.

            * - :py:class:`~IPolarizationHorizontal`
              - Provide the interface for linear polarization.

            * - :py:class:`~IPolarizationVertical`
              - Provide the interface for linear polarization.

            * - :py:class:`~IAdditionalGainLoss`
              - Provide access to an additional gain/loss.

            * - :py:class:`~IAdditionalGainLossCollection`
              - Represents a collection of gains and losses.

            * - :py:class:`~ICRPluginConfiguration`
              - Provide access to plugin properties.

            * - :py:class:`~ICRComplex`
              - Provide access to the real and imaginary parts of a complex number.

            * - :py:class:`~ICRComplexCollection`
              - Represents a collection of complex numbers.

            * - :py:class:`~ICRLocation`
              - Provide the interface for a location.

            * - :py:class:`~IPointingStrategy`
              - Provide the base interface for a pointing strategy.

            * - :py:class:`~IPointingStrategyFixed`
              - Provide the interface for a fixed pointing strategy.

            * - :py:class:`~IPointingStrategySpinning`
              - Provide the interface for a spinning pointing strategy.

            * - :py:class:`~IPointingStrategyTargeted`
              - Provide the interface for a targeted pointing strategy.

            * - :py:class:`~IWaveformPulseDefinition`
              - Provide access to the properties and methods defining the pulse definition for a rectangular pulsed waveform.

            * - :py:class:`~IWaveform`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~IWaveformRectangular`
              - Provide access to a rectangular waveform.

            * - :py:class:`~IWaveformSelectionStrategy`
              - Provide the base interface for a waveform selection strategy.

            * - :py:class:`~IWaveformSelectionStrategyFixed`
              - Provide the base interface for a waveform selection strategy which produces a Fixed waveform.

            * - :py:class:`~IWaveformSelectionStrategyRangeLimits`
              - Provide the base interface for a waveform selection strategy which produces a waveform based on target range.

            * - :py:class:`~IRFInterference`
              - Provide access to the properties and methods defining a radio frequency interference.

            * - :py:class:`~IScatteringPointProvider`
              - Provide access to the properties and methods defining a scattering point provider.

            * - :py:class:`~IScatteringPointProviderSinglePoint`
              - Provide access to the properties and methods defining a single point scattering point provider.

            * - :py:class:`~IScatteringPointCollectionElement`
              - Provide access to the properties and methods defining a scattering point collection element.

            * - :py:class:`~IScatteringPointCollection`
              - Represents a collection of scattering points.

            * - :py:class:`~IScatteringPointProviderPointsFile`
              - Provide access to the properties and methods defining a scattering point provider where the scattering points are defined in a ascii text file.

            * - :py:class:`~IScatteringPointProviderRangeOverCFARCells`
              - Provide access to the properties and methods defining a range over CFAR cells scattering point provider.

            * - :py:class:`~IScatteringPointProviderSmoothOblateEarth`
              - Provide access to the properties and methods defining a smooth oblate earth scattering point provider.

            * - :py:class:`~IScatteringPointProviderPlugin`
              - Provide access to the properties and methods defining a plugin scattering point provider.

            * - :py:class:`~IScatteringPointModel`
              - Provide access to the properties and methods defining a scattering point model model.

            * - :py:class:`~IScatteringPointModelConstantCoefficient`
              - Provide access to the properties and methods defining a constant coefficient scattering point model.

            * - :py:class:`~IScatteringPointModelWindTurbine`
              - Provide access to the properties and methods defining a wind turbine scattering point model.

            * - :py:class:`~IScatteringPointModelPlugin`
              - Provide access to the properties and methods defining a plugin scattering point model.

            * - :py:class:`~IScatteringPointProviderCollectionElement`
              - Provide access to the properties and methods defining an entry in the scattering point provider collection.

            * - :py:class:`~IScatteringPointProviderCollection`
              - Represents a collection of scattering point provider elements.

            * - :py:class:`~IScatteringPointProviderList`
              - Provide access to the properties and methods defining a scattering point provider list.

            * - :py:class:`~IObjectRFEnvironment`
              - Provide access to the properties and methods defining the RF environment for an object.

            * - :py:class:`~IObjectLaserEnvironment`
              - Provide access to the properties and methods defining the laser environment for an object.

            * - :py:class:`~IAntennaModel`
              - Provide access to the properties and methods defining an antenna model.

            * - :py:class:`~IAntennaModelGaussian`
              - Provide access to the properties and methods defining a gaussian antenna model.

            * - :py:class:`~IAntennaModelParabolic`
              - Provide access to the properties and methods defining a parabolic antenna model.

            * - :py:class:`~IAntennaModelSquareHorn`
              - Provide access to the properties and methods defining a square horn antenna model.

            * - :py:class:`~IAntennaModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin antenna model.

            * - :py:class:`~IAntennaModelExternal`
              - Provide access to the properties and methods defining a external antenna model.

            * - :py:class:`~IAntennaModelGimroc`
              - Provide access to the properties and methods defining a GIMROC antenna model.

            * - :py:class:`~IAntennaModelRemcomUanFormat`
              - Provide access to the properties and methods defining an antnna pattern Remcom uan format model.

            * - :py:class:`~IAntennaModelANSYSffdFormat`
              - Provide access to the properties and methods defining an antnna pattern ANSYS ffd format model.

            * - :py:class:`~IAntennaModelTicraGRASPFormat`
              - Provide access to the properties and methods defining an antnna pattern Ticra GRASP format model.

            * - :py:class:`~IAntennaModelElevationAzimuthCuts`
              - Provide access to the properties and methods defining a pattern elevation/azimuth cuts antenna model.

            * - :py:class:`~IAntennaModelIeee1979`
              - Provide access to the properties and methods defining a IEEE 1979 antenna model.

            * - :py:class:`~IAntennaModelDipole`
              - Provide access to the properties and methods defining a dipole antenna model.

            * - :py:class:`~IAntennaModelHelix`
              - Provide access to the properties and methods defining a helix antenna model.

            * - :py:class:`~IAntennaModelCosecantSquared`
              - Provide access to the properties and methods defining a cosecant squared antenna model.

            * - :py:class:`~IAntennaModelHemispherical`
              - Provide access to the properties and methods defining a hemispherical antenna model.

            * - :py:class:`~IAntennaModelPencilBeam`
              - Provide access to the properties and methods defining a pencil beam antenna model.

            * - :py:class:`~IElementConfiguration`
              - Provide access to the properties and methods defining an element configuration.

            * - :py:class:`~IElementConfigurationCircular`
              - Provide access to the properties and methods defining a circular element configuration.

            * - :py:class:`~IElementConfigurationLinear`
              - Provide access to the properties and methods defining a linear element configuration.

            * - :py:class:`~IElementConfigurationAsciiFile`
              - Provide access to the properties and methods defining a ascii file element configuration.

            * - :py:class:`~IElementConfigurationHfssEepFile`
              - Provide access to the properties and methods defining an HFSS EEP file element configuration.

            * - :py:class:`~IElementConfigurationPolygon`
              - Provide access to the properties and methods defining a polygon element configuration.

            * - :py:class:`~IBeamformer`
              - Provide access to the properties and methods defining a beamformer.

            * - :py:class:`~IBeamformerMvdr`
              - Provide access to the properties and methods defining an MVDR beamformer.

            * - :py:class:`~IBeamformerUniform`
              - Provide access to the properties and methods defining a uniform tapered beamformer.

            * - :py:class:`~IBeamformerAsciiFile`
              - Provide access to the properties and methods defining an ascii file beamformer.

            * - :py:class:`~IBeamformerScript`
              - Provide access to the properties and methods defining an script plugin beamformer.

            * - :py:class:`~IBeamformerBlackmanHarris`
              - Provide access to the properties and methods defining a Blackman-Harris tapered beamformer.

            * - :py:class:`~IBeamformerCosine`
              - Provide access to the properties and methods defining a cosine tapered beamformer.

            * - :py:class:`~IBeamformerCosineX`
              - Provide access to the properties and methods defining an cosine^X tapered beamformer.

            * - :py:class:`~IBeamformerCustomTaperFile`
              - Provide access to the properties and methods defining a custom taper file beamformer.

            * - :py:class:`~IBeamformerDolphChebyshev`
              - Provide access to the properties and methods defining a Dolph-Chebyshev tapered beamformer.

            * - :py:class:`~IBeamformerHamming`
              - Provide access to the properties and methods defining a Hamming tapered beamformer.

            * - :py:class:`~IBeamformerHann`
              - Provide access to the properties and methods defining a Hann tapered beamformer.

            * - :py:class:`~IBeamformerRaisedCosine`
              - Provide access to the properties and methods defining a raised cosine tapered beamformer.

            * - :py:class:`~IBeamformerRaisedCosineSquared`
              - Provide access to the properties and methods defining a raised cosine-squared tapered beamformer.

            * - :py:class:`~IDirectionProvider`
              - Provide access to the properties and methods defining an direction provider.

            * - :py:class:`~IDirectionProviderAsciiFile`
              - Provide access to the properties and methods defining an ascii file direction provider.

            * - :py:class:`~IDirectionProviderObject`
              - Provide access to the properties and methods defining an object direction provider.

            * - :py:class:`~IDirectionProviderLink`
              - Provide access to the properties and methods defining an link direction provider.

            * - :py:class:`~IDirectionProviderScript`
              - Provide access to the properties and methods defining an script plugin direction provider.

            * - :py:class:`~IElement`
              - Provide access to the properties and methods defining a phased array element.

            * - :py:class:`~IElementCollection`
              - Represents a collection of phased array elements.

            * - :py:class:`~IAntennaModelPhasedArray`
              - Provide access to the properties and methods defining a phased array antenna model.

            * - :py:class:`~IAntennaModelHfssEepArray`
              - Provide access to the properties and methods defining an HFSS EEP array antenna model.

            * - :py:class:`~IAntennaModelIsotropic`
              - Provide access to the properties and methods defining an isotropic antenna model.

            * - :py:class:`~IAntennaModelIntelSat`
              - Provide access to the properties and methods defining an IntelSat antenna model.

            * - :py:class:`~IAntennaModelOpticalSimple`
              - Provide access to the properties and methods defining a simple optical antenna model.

            * - :py:class:`~IAntennaModelRectangularPattern`
              - Provide access to the properties and methods defining a rectangular pattern antenna model.

            * - :py:class:`~IAntennaModelGpsGlobal`
              - Provide access to the properties and methods defining a GPS global antenna model.

            * - :py:class:`~IAntennaModelGpsFrpa`
              - Provide access to the properties and methods defining a GPS FRPA antenna model.

            * - :py:class:`~IAntennaModelItuBO1213CoPolar`
              - Provide access to the properties and methods defining an ITU-R BO1213 co-polar antenna model.

            * - :py:class:`~IAntennaModelItuBO1213CrossPolar`
              - Provide access to the properties and methods defining an ITU-R BO1213 cross-polar antenna model.

            * - :py:class:`~IAntennaModelItuF1245`
              - Provide access to the properties and methods defining an ITU-R F1245-3 antenna model.

            * - :py:class:`~IAntennaModelItuS580`
              - Provide access to the properties and methods defining an ITU-R S580-6 antenna model.

            * - :py:class:`~IAntennaModelItuS465`
              - Provide access to the properties and methods defining an ITU-R S465-6 antenna model.

            * - :py:class:`~IAntennaModelItuS731`
              - Provide access to the properties and methods defining an ITU-R S731 antenna model.

            * - :py:class:`~IAntennaModelItuS1528R12Circular`
              - Provide access to the properties and methods defining an ITU-R S1528 1.2 circular antenna model.

            * - :py:class:`~IAntennaModelItuS1528R13`
              - Provide access to the properties and methods defining an ITU-R S1528 1.3 antenna model.

            * - :py:class:`~IAntennaModelItuS672Circular`
              - Provide access to the properties and methods defining an ITU-R S672-4 circular antenna model.

            * - :py:class:`~IAntennaModelItuS1528R12Rectangular`
              - Provide access to the properties and methods defining an ITU-R S1528 1.2 rectangular antenna model.

            * - :py:class:`~IAntennaModelItuS672Rectangular`
              - Provide access to the properties and methods defining an ITU-R S672-4 1.2 rectangular antenna model.

            * - :py:class:`~IAntennaModelApertureCircularCosine`
              - Provide access to the properties and methods defining a circular cosine aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularUniform`
              - Provide access to the properties and methods defining a circular uniform aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularCosineSquared`
              - Provide access to the properties and methods defining a circular cosine squared aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularBessel`
              - Provide access to the properties and methods defining a circular bessel aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularBesselEnvelope`
              - Provide access to the properties and methods defining a circular bessel envelope aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularCosinePedestal`
              - Provide access to the properties and methods defining a circular cosine pedestal aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularCosineSquaredPedestal`
              - Provide access to the properties and methods defining a circular cosine squared pedestal aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularSincIntPower`
              - Provide access to the properties and methods defining a circular sinc integer power aperture antenna model.

            * - :py:class:`~IAntennaModelApertureCircularSincRealPower`
              - Provide access to the properties and methods defining a circular sinc real power aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularUniform`
              - Provide access to the properties and methods defining a rectangular uniform aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularCosineSquared`
              - Provide access to the properties and methods defining a rectangular cosine squared aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularCosine`
              - Provide access to the properties and methods defining a rectangular cosine aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularCosinePedestal`
              - Provide access to the properties and methods defining a rectangular cosine pedestal aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularCosineSquaredPedestal`
              - Provide access to the properties and methods defining a rectangular cosine squared pedestal aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularSincIntPower`
              - Provide access to the properties and methods defining a rectangular sinc integer power aperture antenna model.

            * - :py:class:`~IAntennaModelApertureRectangularSincRealPower`
              - Provide access to the properties and methods defining a rectangular sinc real power aperture antenna model.

            * - :py:class:`~IAntennaVolumeLevel`
              - IAgRadarCrossSectionVolumeLevel Interface for an radar cross section volume level.

            * - :py:class:`~IAntennaVolumeLevelCollection`
              - Represents a collection of antenna volume levels.

            * - :py:class:`~IAntennaVolumeGraphics`
              - IAgAntennaVolumeGraphics Interface for a antenna's 3D volume properties.

            * - :py:class:`~IAntennaGraphics3D`
              - IAgAntennaVO Interface for a antenna's 3D Graphics properties.

            * - :py:class:`~IAntennaContourLevel`
              - IAgAntennaContourLevel Interface for an antenna contour level.

            * - :py:class:`~IAntennaContourLevelCollection`
              - Represents a collection of antenna contour levels.

            * - :py:class:`~IAntennaContour`
              - IAgAntennaContour Interface for a antenna's contour properties.

            * - :py:class:`~IAntennaContourGain`
              - IAgAntennaContourGain Interface for a antenna's gain contour properties.

            * - :py:class:`~IAntennaContourEirp`
              - IAgAntennaContourEirp Interface for a antenna's eirp contour properties.

            * - :py:class:`~IAntennaContourRip`
              - IAgAntennaContourRip Interface for a antenna's rip contour properties.

            * - :py:class:`~IAntennaContourFluxDensity`
              - IAgAntennaContourFluxDensity Interface for a antenna's flux density contour properties.

            * - :py:class:`~IAntennaContourSpectralFluxDensity`
              - IAgAntennaContourSpectralFluxDensity Interface for a antenna's spectral flux density contour properties.

            * - :py:class:`~IAntennaContourGraphics`
              - IAgAntennaContourGraphics Interface for a antenna's contour properties.

            * - :py:class:`~IAntennaGraphics`
              - IAgAntennaGraphics Interface for a antenna's 2D Graphics properties.

            * - :py:class:`~IAntenna`
              - Provide access to the properties and methods defining an Antenna object.

            * - :py:class:`~IAntennaControl`
              - Provide access to the properties and methods of the antenna control.

            * - :py:class:`~IAntennaBeamSelectionStrategy`
              - Provide access to a beam selection strategy.

            * - :py:class:`~IAntennaBeamSelectionStrategyScriptPlugin`
              - Provide access to a script plugin beam selection strategy.

            * - :py:class:`~IAntennaBeam`
              - Provide access to an antenna beam.

            * - :py:class:`~IAntennaBeamTransmit`
              - Provide access to an transmit antenna beam.

            * - :py:class:`~IAntennaBeamCollection`
              - Represents a collection of antenna beams.

            * - :py:class:`~IAntennaSystem`
              - Provide access to the properties for a antenna system.

            * - :py:class:`~IRFFilterModel`
              - Provide access to the properties and methods defining an RF filter model.

            * - :py:class:`~IModulatorModel`
              - Provide access to the properties and methods defining a modulator model.

            * - :py:class:`~ITransmitterModel`
              - Provide access to the properties and methods defining a transmitter model.

            * - :py:class:`~ITransmitterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin transmitter model.

            * - :py:class:`~ITransmitterModelCable`
              - Provide access to the properties and methods defining a cable transmitter model.

            * - :py:class:`~ITransmitterModelSimple`
              - Provide access to the properties and methods defining a simple transmitter model.

            * - :py:class:`~ITransmitterModelMedium`
              - Provide access to the properties and methods defining a medium transmitter model.

            * - :py:class:`~ITransmitterModelComplex`
              - Provide access to the properties and methods defining a complex transmitter model.

            * - :py:class:`~ITransmitterModelMultibeam`
              - Provide access to the properties and methods defining a multibeam transmitter model.

            * - :py:class:`~ITransmitterModelLaser`
              - Provide access to the properties and methods defining a laser transmitter model.

            * - :py:class:`~ITransferFunctionInputBackOffCOverImTableRow`
              - Provide access to the row of an input back off vs C/Im table.

            * - :py:class:`~ITransferFunctionInputBackOffCOverImTable`
              - Represents a collection of input back off vs C/Im values.

            * - :py:class:`~ITransferFunctionInputBackOffOutputBackOffTableRow`
              - Provide access to the row of an input back off vs output back off table.

            * - :py:class:`~ITransferFunctionInputBackOffOutputBackOffTable`
              - Represents a collection of input back off vs output back off values.

            * - :py:class:`~ITransferFunctionPolynomialCollection`
              - Represents a transfer function polynomial collection.

            * - :py:class:`~IReTransmitterModel`
              - Provide access to the properties and methods defining a re-transmitter model.

            * - :py:class:`~IReTransmitterModelSimple`
              - Provide access to the properties and methods defining a simple re-transmitter model.

            * - :py:class:`~IReTransmitterModelMedium`
              - Provide access to the properties and methods defining a medium re-transmitter model.

            * - :py:class:`~IReTransmitterModelComplex`
              - Provide access to the properties and methods defining a complex re-transmitter model.

            * - :py:class:`~ITransmitterGraphics3D`
              - IAgTransmitterVO Interface for a transmitter's 3D Graphics properties.

            * - :py:class:`~ITransmitterGraphics`
              - IAgTransmitterGraphics Interface for a transmitter's 2D Graphics properties.

            * - :py:class:`~ITransmitter`
              - Provide access to the properties and methods defining an Transmitter object.

            * - :py:class:`~IDemodulatorModel`
              - Provide access to the properties and methods defining a demodulator model.

            * - :py:class:`~ILaserPropagationLossModels`
              - Provide access to laser propagation loss models.

            * - :py:class:`~ILinkMargin`
              - Provide access to the properties for configuring the link margin computation.

            * - :py:class:`~IReceiverModel`
              - Provide access to the properties and methods defining a receiver model.

            * - :py:class:`~IReceiverModelSimple`
              - Provide access to the properties and methods defining a simple receiver model.

            * - :py:class:`~IReceiverModelMedium`
              - Provide access to the properties and methods defining a medium receiver model.

            * - :py:class:`~IReceiverModelComplex`
              - Provide access to the properties and methods defining a complex receiver model.

            * - :py:class:`~IReceiverModelMultibeam`
              - Provide access to the properties and methods defining a multibeam receiver model.

            * - :py:class:`~IReceiverModelLaser`
              - Provide access to the properties and methods defining a laser receiver model.

            * - :py:class:`~IReceiverModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin receiver model.

            * - :py:class:`~IReceiverModelScriptPluginRF`
              - Provide access to the properties and methods defining a radio frequency script plugin receiver model.

            * - :py:class:`~IReceiverModelCable`
              - Provide access to the properties and methods defining a cable receiver model.

            * - :py:class:`~IReceiverGraphics3D`
              - IAgReceiverVO Interface for a receiver's 3D Graphics properties.

            * - :py:class:`~IReceiverGraphics`
              - IAgReceiverGraphics Interface for a receiver's 2D Graphics properties.

            * - :py:class:`~IReceiver`
              - Provide access to the properties and methods defining an Receiver object.

            * - :py:class:`~IRadarActivity`
              - Provide access to the properties and methods defining radar activity.

            * - :py:class:`~IRadarActivityTimeComponentListElement`
              - Provide access to the properties and methods defining an entry in the time components activity list.

            * - :py:class:`~IRadarActivityTimeComponentListCollection`
              - Represents a collection of time component activity elements.

            * - :py:class:`~IRadarActivityTimeComponentList`
              - Provide access to the properties and methods defining radar time components list activity.

            * - :py:class:`~IRadarActivityTimeIntervalListElement`
              - Provide access to the properties and methods defining an entry in the time interval activity list.

            * - :py:class:`~IRadarActivityTimeIntervalListCollection`
              - Represents a collection of time interval activity elements.

            * - :py:class:`~IRadarActivityTimeIntervalList`
              - Provide access to the properties and methods defining radar time interval list activity.

            * - :py:class:`~IRadarStcAttenuation`
              - Provide access to the properties and methods defining a radar STC attenuation.

            * - :py:class:`~IRadarStcAttenuationDecayFactor`
              - Provide access to the properties and methods defining a radar decay factor STC attenuation.

            * - :py:class:`~IRadarStcAttenuationDecaySlope`
              - Provide access to the properties and methods defining a radar decay slope STC attenuation.

            * - :py:class:`~IRadarStcAttenuationMap`
              - Provide access to the properties and methods defining a radar STC attenuation map.

            * - :py:class:`~IRadarJamming`
              - Provide access to the properties and methods defining a radar jamming.

            * - :py:class:`~IRadarClutterGeometryModel`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointProvider interface instead. Provides access to the properties and methods defining a radar clutter geometry model.

            * - :py:class:`~IRadarClutterGeometryModelPlugin`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointProviderPlugin interface instead. Provides access to the properties and methods defining a radar clutter geometry plugin model.

            * - :py:class:`~IRadarClutter`
              - Interface which defines a radar's clutter.

            * - :py:class:`~IRadarClutterGeometry`
              - Do not use this interface, as it is deprecated. Use IAgRadarClutter interface instead. Interface which defines a radar's clutter geometry.

            * - :py:class:`~IRadarTransmitter`
              - Interface which defines a radar transmitter.

            * - :py:class:`~IRadarTransmitterMultifunction`
              - Interface which defines a multifunction radar transmitter.

            * - :py:class:`~IRadarReceiver`
              - Interface which defines a radar receiver.

            * - :py:class:`~IRadarContinuousWaveAnalysisMode`
              - Interface which defines an continuous wave analysis.

            * - :py:class:`~IRadarContinuousWaveAnalysisModeGoalSNR`
              - Interface which defines an continuous wave goal SNR analysis.

            * - :py:class:`~IRadarContinuousWaveAnalysisModeFixedTime`
              - Interface which defines an continuous wave fixed time analysis.

            * - :py:class:`~IRadarPulseIntegration`
              - Interface which defines an integration method.

            * - :py:class:`~IRadarPulseIntegrationGoalSNR`
              - Interface which defines a goal SNR integration method.

            * - :py:class:`~IRadarPulseIntegrationFixedNumberOfPulses`
              - Interface which defines a fixed number of pulses integration method.

            * - :py:class:`~IRadarWaveformSearchTrack`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarWaveformSearchTrackPulseDefinition`
              - Provide access to the properties and methods defining the pulse definition for a search track waveform.

            * - :py:class:`~IRadarWaveformSarPulseDefinition`
              - Provide access to the properties and methods defining the pulse definition for a Sar waveform.

            * - :py:class:`~IRadarWaveformSarPulseIntegration`
              - Provide access to the properties and methods defining the pulse integration for a SAR waveform.

            * - :py:class:`~IRadarModulator`
              - Provide access to the properties and methods defining the radar modulator.

            * - :py:class:`~IRadarProbabilityOfDetection`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~IRadarProbabilityOfDetectionPlugin`
              - Provide access to the properties and methods defining a radar clutter geometry plugin model.

            * - :py:class:`~IRadarProbabilityOfDetectionNonCFAR`
              - Provide access to the properties and methods for configuring non CFAR probability of detection parameters.

            * - :py:class:`~IRadarProbabilityOfDetectionCFAR`
              - Provide access to the properties and methods for configuring probability of detection parameters.

            * - :py:class:`~IRadarWaveformMonostaticSearchTrackContinuous`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarMultifunctionDetectionProcessing`
              - Interface which represents multifunction radar detection processing.

            * - :py:class:`~IRadarWaveformMonostaticSearchTrackFixedPRF`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarWaveformBistaticReceiverSearchTrackContinuous`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Interface which is implemented by a search/track waveform.

            * - :py:class:`~IRadarDopplerClutterFilters`
              - Provide access to the properties and methods defining a radar doppler clutter filter.

            * - :py:class:`~IRadarModel`
              - Provide access to the properties and methods defining a radar model.

            * - :py:class:`~IRadarModeMonostatic`
              - Provide access to the properties and methods defining a monostatic mode.

            * - :py:class:`~IRadarModeMonostaticSearchTrack`
              - Provide access to the properties and methods defining a monostatic search/track mode.

            * - :py:class:`~IRadarModeMonostaticSar`
              - Provide access to the properties and methods defining a monostatic sar mode.

            * - :py:class:`~IRadarModelMonostatic`
              - Provide access to the properties and methods defining a monostatic radar model.

            * - :py:class:`~IRadarAntennaBeam`
              - Provide access to a radar antenna beam.

            * - :py:class:`~IRadarAntennaBeamCollection`
              - Represents a collection of antenna beams.

            * - :py:class:`~IRadarMultifunctionWaveformStrategySettings`
              - Interface which defines a multifunction radar waveform strategy settings.

            * - :py:class:`~IRadarModelMultifunction`
              - Provide access to the properties and methods defining a multifunction radar model.

            * - :py:class:`~IRadarModeBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter mode.

            * - :py:class:`~IRadarModeBistaticTransmitterSearchTrack`
              - Provide access to the properties and methods defining a bistatic transmitter search/track mode.

            * - :py:class:`~IRadarModeBistaticTransmitterSar`
              - Provide access to the properties and methods defining a bistatic transmitter sar mode.

            * - :py:class:`~IRadarModelBistaticTransmitter`
              - Provide access to the properties and methods defining a bistatic transmitter radar model.

            * - :py:class:`~IRadarModeBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver mode.

            * - :py:class:`~IRadarModeBistaticReceiverSearchTrack`
              - Provide access to the properties and methods defining a bistatic receiver search/track mode.

            * - :py:class:`~IRadarModeBistaticReceiverSar`
              - Provide access to the properties and methods defining a bistatic receiver sar mode.

            * - :py:class:`~IRadarModelBistaticReceiver`
              - Provide access to the properties and methods defining a bistatic receiver radar model.

            * - :py:class:`~IRadarGraphics3D`
              - IAgRadarVO Interface for a radar's 3D Graphics properties.

            * - :py:class:`~IRadarMultipathGraphics`
              - IAgRadarMultipathGraphics Interface for a radar's multipath graphics properties.

            * - :py:class:`~IRadarAccessGraphics`
              - IAgRadarAccessGraphics Interface for a radar's access graphics properties.

            * - :py:class:`~IRadarGraphics`
              - IAgRadarGraphics Interface for a radar's 2D Graphics properties.

            * - :py:class:`~IRadar`
              - Provide access to the properties and methods defining an Radar object.

            * - :py:class:`~IRadarClutterMapModel`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModel interface instead. Provides access to the properties and methods defining a radar clutter map model.

            * - :py:class:`~IRadarClutterMapModelPlugin`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModelPlugin interface instead. Provides access to the properties and methods defining a radar clutter map plugin model.

            * - :py:class:`~IRadarClutterMapModelConstantCoefficient`
              - Do not use this interface, as it is deprecated. Use IAgScatteringPointModelConstantCoefficient interface instead. Provides access to the properties and methods defining a radar clutter map constant coefficient model.

            * - :py:class:`~IRadarCrossSectionComputeStrategy`
              - Provide access to the properties and methods defining a radar cross section compute Strategy.

            * - :py:class:`~IRadarCrossSectionComputeStrategyConstantValue`
              - Provide access to the properties and methods defining a radar cross section constant value compute Strategy.

            * - :py:class:`~IRadarCrossSectionComputeStrategyScriptPlugin`
              - Provide access to the properties and methods defining a radar cross section script plugin compute Strategy.

            * - :py:class:`~IRadarCrossSectionComputeStrategyExternalFile`
              - Provide access to the properties and methods defining a radar cross section external file compute Strategy.

            * - :py:class:`~IRadarCrossSectionComputeStrategyAnsysCsvFile`
              - Provide access to the properties and methods defining a radar cross section Ansys Csv file compute Strategy.

            * - :py:class:`~IRadarCrossSectionComputeStrategyPlugin`
              - Provide access to the properties and methods defining a radar cross section plugin compute Strategy.

            * - :py:class:`~IRadarCrossSectionFrequencyBand`
              - Provide access to the properties and methods defining radar cross section frequency band.

            * - :py:class:`~IRadarCrossSectionFrequencyBandCollection`
              - Represents a collection of radar cross section frequency bands.

            * - :py:class:`~IRadarCrossSectionModel`
              - Provide access to the properties and methods defining a radar cross section model.

            * - :py:class:`~IRadarStcAttenuationPlugin`
              - Provide access to the properties and methods defining a radar STC plugin model.

            * - :py:class:`~IRadarCrossSectionVolumeLevel`
              - IAgRadarCrossSectionVolumeLevel Interface for an radar cross section volume level.

            * - :py:class:`~IRadarCrossSectionVolumeLevelCollection`
              - Represents a collection of radar cross section volume levels.

            * - :py:class:`~IRadarCrossSectionVolumeGraphics`
              - IAgRadarCrossSectionVolumeGraphics Interface for radar cross section 3D volume properties.

            * - :py:class:`~IRadarCrossSectionContourLevel`
              - IAgRadarCrossSectionContourLevel Interface for an radar cross section contour level.

            * - :py:class:`~IRadarCrossSectionContourLevelCollection`
              - Represents a collection of radar cross section contour levels.

            * - :py:class:`~IRFFilterModelBessel`
              - Provide access to the properties and methods defining an bessel RF filter model.

            * - :py:class:`~IRFFilterModelButterworth`
              - Provide access to the properties and methods defining an butterworth RF filter model.

            * - :py:class:`~IRFFilterModelSincEnvSinc`
              - Provide access to the properties and methods defining a sinc envelope sinc analog RF filter model.

            * - :py:class:`~IRFFilterModelElliptic`
              - Provide access to the properties and methods defining an elliptic analog RF filter model.

            * - :py:class:`~IRFFilterModelChebyshev`
              - Provide access to the properties and methods defining an Chebyshev analog RF filter model.

            * - :py:class:`~IRFFilterModelCosineWindow`
              - Provide access to the properties and methods defining a cosine window RF filter model.

            * - :py:class:`~IRFFilterModelGaussianWindow`
              - Provide access to the properties and methods defining a gaussian window RF filter model.

            * - :py:class:`~IRFFilterModelHammingWindow`
              - Provide access to the properties and methods defining a Hamming window RF filter model.

            * - :py:class:`~IRFFilterModelExternal`
              - Provide access to the properties and methods defining a external RF filter model.

            * - :py:class:`~IRFFilterModelScriptPlugin`
              - Provide access to the properties and methods defining a script plugin RF filter model.

            * - :py:class:`~IRFFilterModelSinc`
              - Provide access to the properties and methods defining a sinc RF filter model.

            * - :py:class:`~IRFFilterModelRaisedCosine`
              - Provide access to the properties and methods defining a raised cosine RF filter model.

            * - :py:class:`~IRFFilterModelRootRaisedCosine`
              - Provide access to the properties and methods defining a root raised cosine RF filter model.

            * - :py:class:`~IRFFilterModelRcLowPass`
              - Provide access to the properties and methods defining a rc low pass RF filter model.

            * - :py:class:`~IRFFilterModelFirBoxCar`
              - Provide access to the properties and methods defining a FIR box car RF filter model.

            * - :py:class:`~IRFFilterModelFir`
              - Provide access to the properties and methods defining a FIR RF filter model.

            * - :py:class:`~IRFFilterModelIir`
              - Provide access to the properties and methods defining a IIR RF filter model.

            * - :py:class:`~IModulatorModelExternal`
              - Provide access to the properties and methods defining an external file modulator model.

            * - :py:class:`~IModulatorModelBoc`
              - Provide access to the properties and methods defining a BOC modulator model.

            * - :py:class:`~IModulatorModelPulsedSignal`
              - Provide access to the properties and methods defining a pulsed signal modulator model.

            * - :py:class:`~IModulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin modulator model.

            * - :py:class:`~IDemodulatorModelExternal`
              - Provide access to the properties and methods defining an external file demodulator model.

            * - :py:class:`~IDemodulatorModelScriptPlugin`
              - Provide access to the properties and methods defining an script plugin demodulator model.

            * - :py:class:`~IRainLossModelScriptPlugin`
              - Provide access to the properties and methods of a script plugin rain loss model.

            * - :py:class:`~IRainLossModel`
              - Provide access to the properties and methods a rain loss model.

            * - :py:class:`~IRainLossModelCrane1985`
              - Provide access to the properties and methods for a Crane 1985 rain loss model.

            * - :py:class:`~IRainLossModelCrane1982`
              - Provide access to the properties and methods for a Crane 1982 rain loss model.

            * - :py:class:`~IRainLossModelCCIR1983`
              - Provide access to the properties and methods for a CCIR 1983 rain loss model.

            * - :py:class:`~IRainLossModelITURP618_10`
              - Provide access to the properties and methods for a ITU-R P618-10 rain loss model.

            * - :py:class:`~IRainLossModelITURP618_12`
              - Provide access to the properties and methods for a ITU-R P618-12 rain loss model.

            * - :py:class:`~IRainLossModelITURP618_13`
              - Provide access to the properties and methods for a ITU-R P618-13 rain loss model.

            * - :py:class:`~IUrbanTerrestrialLossModel`
              - Provide access to the properties and methods for an urban/terrestrial loss model.

            * - :py:class:`~IUrbanTerrestrialLossModelTwoRay`
              - Provide access to the properties and methods for an urban/terrestrial loss two ray model.

            * - :py:class:`~IWirelessInSite64GeometryData`
              - Provide access to the properties and methods for geometry data for the Wireless InSite RT model.

            * - :py:class:`~IUrbanTerrestrialLossModelWirelessInSite64`
              - Provide access to the properties and methods for an urban/terrestrial loss Wireless InSite 64 model.

            * - :py:class:`~ITroposphericScintillationFadingLossModel`
              - Provide access to the properties and methods for a TropoSpheric Scintillation Fading loss model.

            * - :py:class:`~ITroposphericScintillationFadingLossModelP618_8`
              - Provide access to the properties and methods a Tropospheric Scintillation loss model ITU-R P.618_8.

            * - :py:class:`~ITroposphericScintillationFadingLossModelP618_12`
              - Provide access to the properties and methods of a Tropospheric Scintillation loss model ITU-R P.618_12.

            * - :py:class:`~IIonosphericFadingLossModel`
              - Provide access to the properties and methods for an Ionospheric Fading loss model.

            * - :py:class:`~IIonosphericFadingLossModelP531_13`
              - Provide access to the properties and methods for the Ionospheric Fading loss model ITU-R P.531_13.

            * - :py:class:`~ICloudsAndFogFadingLossModel`
              - Provide access to the properties and methods for Clouds and Fog loss models.

            * - :py:class:`~ICloudsAndFogFadingLossModelP840_6`
              - Provide access to the properties and methods for clouds and fog loss model ITU-R P.840-6.

            * - :py:class:`~ICloudsAndFogFadingLossModelP840_7`
              - Provide access to the properties and methods for clouds and fog loss model ITU-R P.840-7.

            * - :py:class:`~IAtmosphericAbsorptionModel`
              - Provide access to the properties and methods an atmospheric absorption model.

            * - :py:class:`~IAtmosphericAbsorptionModelITURP676`
              - Provide access to the properties and methods of the ITU-R P676 atmospheric absorption model.

            * - :py:class:`~IAtmosphericAbsorptionModelTirem`
              - Provide access to the properties and methods of the TIREM atmospheric absorption model.

            * - :py:class:`~ISolarActivityConfiguration`
              - Provide access to the properties and methods defining the solar activity configuration.

            * - :py:class:`~ISolarActivityConfigurationSunspotNumber`
              - Provide access to the properties and methods defining the sunspot number.

            * - :py:class:`~ISolarActivityConfigurationSolarFlux`
              - Provide access to the properties and methods defining the solar flux.

            * - :py:class:`~IAtmosphericAbsorptionModelVoacap`
              - Provide access to the properties and methods of the VOACAP atmospheric absorption model.

            * - :py:class:`~IAtmosphericAbsorptionModelSimpleSatcom`
              - Provide access to the properties and methods of the Simple Satcom atmospheric absorption model.

            * - :py:class:`~IAtmosphericAbsorptionModelScriptPlugin`
              - Provide access to the properties and methods of the script plugin atmospheric absorption model.

            * - :py:class:`~IAtmosphericAbsorptionModelCOMPlugin`
              - Provide access to the properties and methods of the COM plugin atmospheric absorption model.

            * - :py:class:`~ICustomPropagationModel`
              - Provide access to the properties and methods for a custom propagation model.

            * - :py:class:`~IPropagationChannel`
              - Provide access to the properties and methods defining a propagation channel.

            * - :py:class:`~IBeerBouguerLambertLawLayer`
              - Provide access to a atmosphere layer used in the Beer-Bouguer-Lambert law propagation loss model.

            * - :py:class:`~IBeerBouguerLambertLawLayerCollection`
              - Represents a collection of complex numbers.

            * - :py:class:`~ILaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Provide access to the properties and methods a Beer-Bouguer-Lambert law laser propagation loss model.

            * - :py:class:`~IModtranLookupTablePropagationModel`
              - Provide access to the properties and methods of the MODTRAN lookup table model.

            * - :py:class:`~IModtranPropagationModel`
              - Provide access to the properties and methods of the MODTRAN propagation model.

            * - :py:class:`~ILaserAtmosphericLossModel`
              - Provide access to the properties and methods for a laser atmospheric absorption loss model.

            * - :py:class:`~ILaserTroposphericScintillationLossModel`
              - Provide access to the properties and methods for a laser tropospheric scintillation loss model.

            * - :py:class:`~IAtmosphericTurbulenceModel`
              - Provide access to a refractive index structure parameter model.

            * - :py:class:`~IAtmosphericTurbulenceModelConstant`
              - Provide access to a constant atmospheric turbulence model.

            * - :py:class:`~IAtmosphericTurbulenceModelHufnagelValley`
              - Provide access to a Hufnagel Valley atmospheric turbulence model.

            * - :py:class:`~ILaserTroposphericScintillationLossModelITURP1814`
              - Provide access to the properties and methods an ITU-R P.1814 laser tropospheric scintillation propagation loss model.

            * - :py:class:`~ILaserPropagationChannel`
              - Provide access to laser propagation loss models.

            * - :py:class:`~ICommSystemLinkSelectionCriteria`
              - Provide access to a link selection criteria.

            * - :py:class:`~ICommSystemLinkSelectionCriteriaScriptPlugin`
              - Provide access to a script plugin link selection criteria.

            * - :py:class:`~ICommSystemAccessEventDetection`
              - Provide access to the properties an access event detection algorithm.

            * - :py:class:`~ICommSystemAccessEventDetectionSubsample`
              - Provide access to the properties an access sub-sample event detection algorithm.

            * - :py:class:`~ICommSystemAccessSamplingMethod`
              - Provide access to the properties for the sampling method.

            * - :py:class:`~ICommSystemAccessSamplingMethodFixed`
              - Provide access to the properties for a fixed sampling method.

            * - :py:class:`~ICommSystemAccessSamplingMethodAdaptive`
              - Provide access to the properties for a adaptive sampling method.

            * - :py:class:`~ICommSystemAccessOptions`
              - Provide access to the CommSystem object access options.

            * - :py:class:`~ICommSystemGraphics`
              - IAgCommSystemGraphics Interface for a CommSystem's 2D Graphics properties.

            * - :py:class:`~ICommSystemGraphics3D`
              - IAgCommSystemVO Interface for a CommSystem's 3D Graphics properties.

            * - :py:class:`~ICommSystem`
              - Provide access to the properties and methods defining an CommSystem object.

            * - :py:class:`~ISRPModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :py:class:`~ISRPModelBase`
              - A base interface for solar radiation pressure models.

            * - :py:class:`~ISRPModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :py:class:`~ISRPModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :py:class:`~ISRPModelPlugin`
              - Plugin Light Reflection Model.

            * - :py:class:`~IVehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :py:class:`~IVehicleHPOPDragModel`
              - A base interface for drag models.

            * - :py:class:`~IVehicleHPOPDragModelSpherical`
              - Spherical Drag Model.

            * - :py:class:`~IVehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :py:class:`~IVehicleDuration`
              - Look ahead and look behind duration options.

            * - :py:class:`~IVehicleRealtimeCartesianPoints`
              - Add one ephemeris point using cartesian coordinates.

            * - :py:class:`~IVehicleRealtimeLLAHPSPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~IVehicleRealtimeLLAPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~IVehicleRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :py:class:`~IVehicleGPSElement`
              - An element of the GPS element collection.

            * - :py:class:`~IVehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :py:class:`~IVehicleHPOPSRPModel`
              - HPOP Solar Radiation Pressure Model.

            * - :py:class:`~IVehicleThirdBodyGravityElement`
              - Third-body gravity interface.

            * - :py:class:`~IVehicleThirdBodyGravityCollection`
              - Third Body Gravity Collection.

            * - :py:class:`~IVehicleSGP4LoadData`
              - Load Method Data interface.

            * - :py:class:`~IVehicleSGP4OnlineLoad`
              - Interface for SGP4 propagator. Loads segments from online.

            * - :py:class:`~IVehicleSGP4OnlineAutoLoad`
              - Do not use this interface, as it is deprecated. Use IAgVeSGP4OnlineLoad instead. Interface for SGP4 propagator. Loads the most current segment from online.

            * - :py:class:`~IVehicleSGP4LoadFile`
              - Interface for SGP4 propagator.

            * - :py:class:`~IVehicleSGP4Segment`
              - Interface for SGP4 propagator.

            * - :py:class:`~IVehiclePropagatorSGP4CommonTasks`
              - Interface provides methods encapsulating most commonly used functionality when working with SGP4 propagator.

            * - :py:class:`~IVehicleSGP4AutoUpdateProperties`
              - SGP4 Element AutoUpdate properties.

            * - :py:class:`~IVehicleSGP4AutoUpdateFileSource`
              - Interface to configure the SGP4 automatic updates using file(s).

            * - :py:class:`~IVehicleSGP4AutoUpdateOnlineSource`
              - Interface to configure the SGP4 automatic updates using online source (AGI server).

            * - :py:class:`~IVehicleSGP4AutoUpdate`
              - SGP4 Automatic Update properties.

            * - :py:class:`~IVehicleSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :py:class:`~IVehicleSGP4SegmentCollection`
              - Set of Trajectories.

            * - :py:class:`~IVehicleInitialState`
              - Propagator Initial State.

            * - :py:class:`~IVehicleHPOPCentralBodyGravity`
              - Central Body Gravity interface.

            * - :py:class:`~IVehicleRadiationPressure`
              - Interface for additional radiation pressure options.

            * - :py:class:`~IVehicleHPOPSolarRadiationPressure`
              - Solar Radiation Pressure (SRP) interface.

            * - :py:class:`~IVehicleSolarFluxGeoMagnitudeEnterManually`
              - Interface for specifying solar and geomagnetic flux directly.

            * - :py:class:`~IVehicleSolarFluxGeoMagnitudeUseFile`
              - Interface for specifying solar and geomagnetic flux via a file.

            * - :py:class:`~IVehicleSolarFluxGeoMagnitude`
              - Base Interface IAgVeSolarFluxGeoMag. IAgVeSolarFluxGeoMagEnterManually and IAgVeSolarFluxGeoMagUseFile derive from this interface.

            * - :py:class:`~IVehicleHPOPForceModelDrag`
              - Atmospheric Drag interface.

            * - :py:class:`~IVehicleHPOPForceModelDragOptions`
              - Interface for additional options for atmospheric drag.

            * - :py:class:`~IVehicleHPOPSolarRadiationPressureOptions`
              - Interface for additional solar radiation pressure options.

            * - :py:class:`~IVehicleStatic`
              - Interface for additional static force model options.

            * - :py:class:`~IVehicleSolidTides`
              - Interface for additional force model options related to solid tides.

            * - :py:class:`~IVehicleOceanTides`
              - Interface for additional force model options related to ocean tides.

            * - :py:class:`~IVehiclePluginSettings`
              - Interface for HPOP plugin settings.

            * - :py:class:`~IVehiclePluginPropagator`
              - Interface for propagator plugin.

            * - :py:class:`~IVehicleHPOPForceModelMoreOptions`
              - Interface for additional force model options.

            * - :py:class:`~IVehicleEclipsingBodies`
              - Interface for eclipsing bodies.

            * - :py:class:`~IVehicleHPOPForceModel`
              - Interface for HPOP force models.

            * - :py:class:`~IVehicleStepSizeControl`
              - Interface for step size control.

            * - :py:class:`~IVehicleTimeRegularization`
              - Interface for time regularization.

            * - :py:class:`~IVehicleInterpolation`
              - Interpolation interface.

            * - :py:class:`~IVehicleIntegrator`
              - Interface for HPOP integrator.

            * - :py:class:`~IVehicleGravity`
              - Gravity options for covariance matrix.

            * - :py:class:`~IVehiclePositionVelocityElement`
              - Covariance matrix interface.

            * - :py:class:`~IVehiclePositionVelocityCollection`
              - An initial state error covariance matrix used to represent the uncertainty in the vehicle's position and velocity. Because the matrix is symmetric, you only need to enter the lower triangle of the 6x6 matrix.

            * - :py:class:`~IVehicleCorrelationListElement`
              - Item in Consider Cross Correlation list.

            * - :py:class:`~IVehicleCorrelationListCollection`
              - Consider Analysis list for HPOP covariance.

            * - :py:class:`~IVehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :py:class:`~IVehicleConsiderAnalysisCollection`
              - AgVeConsiderAnalysisCollection.

            * - :py:class:`~IVehicleCovariance`
              - HPOP covariance interface.

            * - :py:class:`~IVehicleJxInitialState`
              - Initial state interface for J2/J4 perturbation propagators.

            * - :py:class:`~IVehicleLOPCentralBodyGravity`
              - Central body gravity interface for Long-range Orbit Predictor (LOP) propagator.

            * - :py:class:`~IVehicleThirdBodyGravity`
              - Third body gravity interface options for Long-range Orbit Predictor (LOP) propagator.

            * - :py:class:`~IVehicleExpDensModelParams`
              - Interface for exponential density model (for LOP propagator).

            * - :py:class:`~IVehicleAdvanced`
              - Interface for advanced drag options for LOP propagator.

            * - :py:class:`~IVehicleLOPForceModelDrag`
              - Interface for atmospheric drag for LOP propagator.

            * - :py:class:`~IVehicleLOPSolarRadiationPressure`
              - Solar radiation pressure interface for LOP propagator.

            * - :py:class:`~IVehiclePhysicalData`
              - Physical data interface for LOP propagator.

            * - :py:class:`~IVehicleLOPForceModel`
              - Force model interface for LOP propagator.

            * - :py:class:`~IVehicleSPICESegment`
              - Interface for SPICE propagator segment.

            * - :py:class:`~IVehicleSegmentsCollection`
              - Set of segments.

            * - :py:class:`~IVehiclePropagator`
              - Base vehicle propagator interface.

            * - :py:class:`~IVehiclePropagatorHPOP`
              - HPOP propagator interface.

            * - :py:class:`~IVehiclePropagatorJ2Perturbation`
              - J2 Perturbation propagator interface.

            * - :py:class:`~IVehiclePropagatorJ4Perturbation`
              - J4 Perturbation propagator interface.

            * - :py:class:`~IVehiclePropagatorLOP`
              - LOP (Long-Range Orbit Predictor) propagator interface.

            * - :py:class:`~IVehiclePropagatorSGP4`
              - SGP4 propagator interface.

            * - :py:class:`~IVehiclePropagatorSPICE`
              - SPICE propagator interface.

            * - :py:class:`~IVehiclePropagatorStkExternal`
              - StkExternal propagator interface.

            * - :py:class:`~IVehiclePropagatorTwoBody`
              - Two-body propagator interface.

            * - :py:class:`~IVehiclePropagatorUserExternal`
              - User-external propagator interface.

            * - :py:class:`~IVehicleLaunchVehicleInitialState`
              - Simple Ascent propagator initial state interface.

            * - :py:class:`~IVehiclePropagatorSimpleAscent`
              - SimpleAscent Propagator.

            * - :py:class:`~IVehicleWaypointAltitudeReference`
              - Base interface for the altitude references.

            * - :py:class:`~IVehicleWaypointAltitudeReferenceTerrain`
              - Interface for terrain altitude reference.

            * - :py:class:`~IVehicleWaypointsElement`
              - Interface for representing a waypoint in a collection of waypoints.

            * - :py:class:`~IVehicleWaypointsCollection`
              - Represents a collection of waypoints used with GreatArc vehicles.

            * - :py:class:`~IVehiclePropagatorGreatArc`
              - Great arc propagator interface.

            * - :py:class:`~IVehiclePropagatorAviator`
              - Aviator propagator interface.

            * - :py:class:`~IVehicleLaunchLLA`
              - Interface for geodetic LLA position.

            * - :py:class:`~IVehicleLaunchLLR`
              - Interface for geocentric LLR position.

            * - :py:class:`~IVehicleImpactLLA`
              - Interface for LLA (geodetic) coordinates for a missile's impact location.

            * - :py:class:`~IVehicleImpactLLR`
              - Interface for LLR (geocentric) coordinates for a missile's impact location.

            * - :py:class:`~IVehicleLaunchControlFixedApogeeAltitude`
              - Fixed apogee altitude interface for missile flight parameters.

            * - :py:class:`~IVehicleLaunchControlFixedDeltaV`
              - Fixed Delta V interface for missile flight parameters.

            * - :py:class:`~IVehicleLaunchControlFixedDeltaVMinEccentricity`
              - Fixed Delta V minimum eccentricity interface for missile flight parameters.

            * - :py:class:`~IVehicleLaunchControlFixedTimeOfFlight`
              - Fixed time of flight interface for missile flight parameters.

            * - :py:class:`~IVehicleImpactLocationLaunchAzEl`
              - Launch AzEl interface for missile impact location. All properties on this interface should be set explicitly.

            * - :py:class:`~IVehicleImpact`
              - Base Interface IAgVeImpact. IAgVeImpactLLA and IAgVeImpactLLR derive from this.

            * - :py:class:`~IVehicleLaunchControl`
              - Base Interface IAgVeLaunchControl. IAgVeLaunchControlFixedApogeeAlt, IAgVeLaunchControlFixedDeltaV, IAgVeLaunchControlDixedDeltaVMinEcc and IAgVeLaunchControlTimeOfFlight derive from this.

            * - :py:class:`~IVehicleImpactLocationPoint`
              - Missile impact point interface.

            * - :py:class:`~IVehicleLaunch`
              - Base interface IAgVeLaunch. IAgVeLaunchLLA and IAgVeLaunchLLR derive from this.

            * - :py:class:`~IVehicleImpactLocation`
              - Base interface IAgVeImpactLocation. IAgVeImpactLocationLaunchAzEl and IAgVeImpactLocationPoint derive from this.

            * - :py:class:`~IVehiclePropagatorBallistic`
              - Ballistic propagator interface.

            * - :py:class:`~IVehicleRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :py:class:`~IVehiclePropagatorRealtime`
              - Realtime propagator interface.

            * - :py:class:`~IVehicleGPSAlmanacProperties`
              - A common base interface for GPS almanac properties.

            * - :py:class:`~IVehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :py:class:`~IVehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :py:class:`~IVehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :py:class:`~IVehicleGPSSpecifyAlmanac`
              - Interface to specify a GPS almanac.

            * - :py:class:`~IVehicleGPSAutoUpdateProperties`
              - Interface for GPS AutoUpdate properties.

            * - :py:class:`~IVehicleGPSAutoUpdateFileSource`
              - Interface to configure the GPS automatic updates using almanac file(s).

            * - :py:class:`~IVehicleGPSAutoUpdateOnlineSource`
              - Interface to configure the GPS automatic updates using online source (AGI server).

            * - :py:class:`~IVehicleGPSAutoUpdate`
              - Interface for GPS AutoUpdate.

            * - :py:class:`~IVehiclePropagatorGPS`
              - Allow the user to configure and propagate a vehicle using the GPS propagator.

            * - :py:class:`~IVehiclePropagator11ParamDescriptor`
              - 11-Param file definition.

            * - :py:class:`~IVehiclePropagator11ParamDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :py:class:`~IVehiclePropagator11Param`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :py:class:`~IVehiclePropagatorSP3File`
              - SP3 file data.

            * - :py:class:`~IVehiclePropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :py:class:`~IVehiclePropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :py:class:`~IVehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :py:class:`~IVehicleAccessAdvanced`
              - Interface for configuring a vehicle's advanced targeting access computation properties.

            * - :py:class:`~IVehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :py:class:`~IVehicleTorque`
              - Torque file to use in defining integrated attitude.

            * - :py:class:`~IVehicleIntegratedAttitude`
              - Integrated Attitude interface generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :py:class:`~IVehicleVector`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~IVehicleRateOffset`
              - Rate and offset interface for precession and spin.

            * - :py:class:`~IVehicleAttitudeProfile`
              - The base interface that all vehicle attitude profiles are derived from.

            * - :py:class:`~IVehicleProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~IVehicleProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :py:class:`~IVehicleProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :py:class:`~IVehicleProfileConstraintOffset`
              - Interface for constraint offset for various attitude profiles.

            * - :py:class:`~IVehicleProfileAlignmentOffset`
              - Interface for alignment offset for various attitude profiles.

            * - :py:class:`~IVehicleProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :py:class:`~IVehicleProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :py:class:`~IVehicleProfileSpinAboutXXX`
              - Shared interface for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :py:class:`~IVehicleProfileSpinning`
              - Spinning attitude profile.

            * - :py:class:`~IVehicleProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :py:class:`~IVehicleScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :py:class:`~IVehicleScheduleTimesCollection`
              - List of scheduled accesses.

            * - :py:class:`~IVehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :py:class:`~IVehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :py:class:`~IVehicleTargetPointingCollection`
              - Attitude Targets.

            * - :py:class:`~IVehiclePointing`
              - Interface for target pointing attitude profiles, which override the basic attitude profile for a satellite and have a selected axis point in the direction of one or more selected targets, subject to applicable access constraints.

            * - :py:class:`~IVehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :py:class:`~IVehicleStandardBasic`
              - Basic attitude profile.

            * - :py:class:`~IVehicleAttitudeExternal`
              - Interface for using an external attitude (.a) file.

            * - :py:class:`~IVehicleAttitude`
              - Base interface for vehicle attitude options.

            * - :py:class:`~IVehicleAttitudeRealTimeDataReference`
              - Real time attitude data reference.

            * - :py:class:`~IVehicleAttitudeRealTime`
              - Real time attitude interface.

            * - :py:class:`~IVehicleAttitudeStandard`
              - Standard attitude profile.

            * - :py:class:`~IVehicleTrajectoryAttitudeStandard`
              - Standard attitude profile for launch vehicle or missile.

            * - :py:class:`~IVehicleOrbitAttitudeStandard`
              - Standard attitude profile for satellite.

            * - :py:class:`~IVehicleRouteAttitudeStandard`
              - Standard attitude profile for aircraft.

            * - :py:class:`~IVehicleProfileGPS`
              - GPS Attitude profile.

            * - :py:class:`~IVehicleAttitudeTrendControlAviator`
              - Trending controls for Aviator attitude.

            * - :py:class:`~IVehicleProfileAviator`
              - The profile used for Aviator aircraft.

            * - :py:class:`~IVehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :py:class:`~IVehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :py:class:`~IVehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :py:class:`~IVehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :py:class:`~IVehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :py:class:`~IVehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :py:class:`~IVehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :py:class:`~IVehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :py:class:`~IVehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :py:class:`~IVehicleGraphics2DElevContours`
              - General settings regarding display of elevation contours.

            * - :py:class:`~IVehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :py:class:`~IVehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :py:class:`~IVehicleGraphics2DPass`
              - interface IAgVeGfxPass. IAgVeGfxPassShowPasses and IAgVeGfxPassResolution derive from this.

            * - :py:class:`~IVehicleGraphics2DPasses`
              - Interface for setting satellite pass display graphics.

            * - :py:class:`~IVehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :py:class:`~IVehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :py:class:`~IVehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :py:class:`~IVehicleGraphics2DTimeEventType`
              - Base Interface IAgVeGfxTimeEventType. IAgVeGfxTimeEventTypeLine, IAgVeGfxTimeEventTypeMarker and IAgVeGfxTimeEventTypeText derive from this.

            * - :py:class:`~IVehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :py:class:`~IVehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :py:class:`~IVehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :py:class:`~IVehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :py:class:`~IVehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :py:class:`~IVehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :py:class:`~IVehicleGraphics2DOrbitPassData`
              - 2D Graphics ground track and orbit pass properties.

            * - :py:class:`~IVehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :py:class:`~IVehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :py:class:`~IVehicleGraphics2DLighting`
              - Lighting.

            * - :py:class:`~IVehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :py:class:`~IVehicleGraphics2DAttributes`
              - Base Interface for Vehicle 2D Graphics Attributes.

            * - :py:class:`~IVehicleGraphics2DAttributesBasic`
              - Basic 2D Graphics Attributes for a vehicle.

            * - :py:class:`~IVehicleGraphics2DAttributesDisplayState`
              - Provide access to non-trivial properties of 2D vehicle attributes.

            * - :py:class:`~IVehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :py:class:`~IVehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :py:class:`~IVehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :py:class:`~IVehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :py:class:`~IVehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :py:class:`~IVehicleGraphics2DElevationGroundElevation`
              - Ground elevation interface for vehicle swath.

            * - :py:class:`~IVehicleGraphics2DElevationSwathHalfWidth`
              - Half width interface for vehicle swath.

            * - :py:class:`~IVehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle interface for vehicle swath.

            * - :py:class:`~IVehicleGraphics2DElevation`
              - Base Interface IAgVeGfxElevation. IAgVeGfxElevationGroundElevation, IAgVeGfxElevationsSwathHalfWidth and IAgVeGfxElevationsSwathHalfAngle derive from this.

            * - :py:class:`~IVehicleGraphics2DSwath`
              - Vehicle swath interface.

            * - :py:class:`~IVehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :py:class:`~IVehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :py:class:`~IVehicleGraphics2DTimeComponentsElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views.

            * - :py:class:`~IVehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :py:class:`~IVehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :py:class:`~IVehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :py:class:`~IVehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :py:class:`~IVehicleTrajectoryGraphics3DModel`
              - Marker interface for launch vehicle or missile.

            * - :py:class:`~IVehicleRouteGraphics3DModel`
              - 3D marker interface for great arc vehicles.

            * - :py:class:`~IVehicleGraphics3DLeadTrailData`
              - Interface for vehicle's lead/trail data.

            * - :py:class:`~IVehicleGraphics3DSystemsElementBase`
              - Define methods and properties used to configure the 3D properties of a reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~IVehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~IVehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~IVehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :py:class:`~IVehicleGraphics3DDropLinePositionItem`
              - Interface for drop lines from the vehicle's current position.

            * - :py:class:`~IVehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :py:class:`~IVehicleGraphics3DDropLinePathItem`
              - Interface for drop lines at intervals along the vehicle's path.

            * - :py:class:`~IVehicleGraphics3DDropLinePathItemCollection`
              - Interface for drop lines from the vehicle's orbit or trajectory.

            * - :py:class:`~IVehicleGraphics3DOrbitDropLines`
              - Interface for droplines collections.

            * - :py:class:`~IVehicleGraphics3DRouteDropLines`
              - Interface for droplines for great arc vehicles.

            * - :py:class:`~IVehicleGraphics3DTrajectoryDropLines`
              - Interface for droplines for launch vehicles and missiles.

            * - :py:class:`~IVehicleGraphics3DProximityAreaObject`
              - A base class that defines methods and properties common to all proximity area objects.

            * - :py:class:`~IVehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :py:class:`~IVehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :py:class:`~IVehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :py:class:`~IVehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :py:class:`~IVehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :py:class:`~IVehicleGraphics3DGeoBox`
              - Interface for geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :py:class:`~IVehicleGraphics3DProximity`
              - Base Proximity graphics interface.

            * - :py:class:`~IVehicleGraphics3DRouteProximity`
              - Proximity graphics interface for GreatArc Vehicles.

            * - :py:class:`~IVehicleGraphics3DOrbitProximity`
              - Proximity graphics interface.

            * - :py:class:`~IVehicleGraphics3DTrajectoryProximity`
              - Proximity graphics for a launch vehicle or missile.

            * - :py:class:`~IVehicleGraphics3DElevContours`
              - Interface for 3D elevation angle contours.

            * - :py:class:`~IVehicleGraphics3DSAA`
              - Interface for 3D South Atlantic Anomaly contours.

            * - :py:class:`~IVehicleGraphics3DSigmaScaleProbability`
              - Interface for sigma probability for indirect sizing of covariance pointing contours.

            * - :py:class:`~IVehicleGraphics3DSigmaScaleScale`
              - Interface for sigma scale for direct sizing of covariance pointing contours.

            * - :py:class:`~IVehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :py:class:`~IVehicleGraphics3DIntervalsElement`
              - Intervals graphics interface for covariance pointing contour.

            * - :py:class:`~IVehicleGraphics3DIntervalsCollection`
              - Intervals.

            * - :py:class:`~IVehicleGraphics3DAttributesBasic`
              - Interface for basic 3D graphics for covariance pointing contours.

            * - :py:class:`~IVehicleGraphics3DAttributesIntervals`
              - Interface for 3D graphics based on intervals for covariance pointing contours.

            * - :py:class:`~IVehicleGraphics3DSize`
              - 3D graphics vector size interface.

            * - :py:class:`~IVehicleGraphics3DSigmaScale`
              - Base Interface IAgVeVOSigmaScale. IAgVeVOSigmaScaleScale and IAgVeVOSigmaScaleProbability derive from this.

            * - :py:class:`~IVehicleGraphics3DAttributes`
              - Base Interface IAgVeVOAttributes. IAgVeVOAttributesBasic and IAgVeVOAttributesIntervals derive from this.

            * - :py:class:`~IVehicleGraphics3DCovariancePointingContour`
              - Interface for covariance pointing contours.

            * - :py:class:`~IVehicleGraphics3DOrbitPassData`
              - Interface for satellite 3D ground and orbit track data.

            * - :py:class:`~IVehicleGraphics3DTrajectoryPassData`
              - Interface for 3D ground track and trajectory data for a launch vehicle or missile.

            * - :py:class:`~IVehicleGraphics3DOrbitTrackData`
              - Interface for 3D leading/trailing track data for satellites.

            * - :py:class:`~IVehicleGraphics3DTrajectoryTrackData`
              - Interface for 3D leading/trailing track data for launch vehicles and missiles.

            * - :py:class:`~IVehicleGraphics3DTickData`
              - Base interface IAgVeVOTickData. IAgVeVOTickDataLine and IAgVeVOTickDataPoint derive from this.

            * - :py:class:`~IVehicleGraphics3DPathTickMarks`
              - Interface for tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :py:class:`~IVehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data interface for launch vehicles and missiles.

            * - :py:class:`~IVehicleGraphics3DTrajectory`
              - 3D pass interface for launch vehicles and missiles.

            * - :py:class:`~IVehicleGraphics3DTickDataLine`
              - Interface for line type tick marks.

            * - :py:class:`~IVehicleGraphics3DTickDataPoint`
              - Interface for point type tick mark.

            * - :py:class:`~IVehicleGraphics3DOrbitTickMarks`
              - Tick mark interface for satellites.

            * - :py:class:`~IVehicleGraphics3DPass`
              - 3D pass interface for satellites.

            * - :py:class:`~IVehicleGraphics3DCovariance`
              - Interface for 3D covariance ellipsoids.

            * - :py:class:`~IVehicleGraphics3DVelCovariance`
              - Interface for 3D velocity covariance ellipsoids.

            * - :py:class:`~IVehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint interface.

            * - :py:class:`~IVehicleGraphics3DWaypointMarkersCollection`
              - Waypoint markers collection interface.

            * - :py:class:`~IVehicleGraphics3DRoute`
              - 3D route graphics interface for great arc vehicles.

            * - :py:class:`~IVehicleEclipseBodies`
              - Satellite Eclipse Bodies interface, for defining the eclipse central body list used for lighting computations.

            * - :py:class:`~IGreatArcGraphics`
              - 2D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~IGreatArcGraphics3D`
              - 3D Graphics common for all Great Arc Vehicles.

            * - :py:class:`~IGreatArcVehicle`
              - A base interface for all Great Arc Vehicles.

            * - :py:class:`~IVehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of IAgVeVOBPlaneTemplateDisplayCollection.

            * - :py:class:`~IVehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :py:class:`~IVehicleGraphics3DBPlaneTemplate`
              - An element of IAgVeVOBPlaneTemplatesCollection.

            * - :py:class:`~IVehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :py:class:`~IVehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :py:class:`~IVehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :py:class:`~IVehicleGraphics3DBPlaneTargetPointPosition`
              - A base class for BPlane target point position interfaces.

            * - :py:class:`~IVehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :py:class:`~IVehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :py:class:`~IVehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :py:class:`~IVehicleGraphics3DBPlanePointCollection`
              - A list of available additional points.

            * - :py:class:`~IVehicleGraphics3DBPlaneInstance`
              - Properties of an instance of a B-Plane template.

            * - :py:class:`~IVehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :py:class:`~IVehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :py:class:`~IVehicleSpaceEnvironment`
              - no helpstring provided.

            * - :py:class:`~IEOIR`
              - Property used to access IAgEOIR interface.

            * - :py:class:`~ISatelliteGraphics3DModel`
              - Interface IAgSaVOModel exposes all Satellite's VO Model properties.

            * - :py:class:`~ISatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :py:class:`~IVehicleCentralBodies`
              - Satellite Central Bodies interface.

            * - :py:class:`~ISatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :py:class:`~IVehicleRepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :py:class:`~IVehicleBreakAngle`
              - Base Interface IAgVeBreakAngle. IAgVeBreakAngleBreakByLatitude and IAgVeBreakAngleBreakByLongitude derive from this.

            * - :py:class:`~IVehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :py:class:`~IVehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :py:class:`~IVehicleDefinition`
              - Pass break definition properties.

            * - :py:class:`~IVehiclePassNumbering`
              - Base Interaface IAgVePassNumbering. IAgVePassNumberingDateOfFirstPass and IAgVePassNumberingFirstPassNum derive from this.

            * - :py:class:`~IVehiclePassNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :py:class:`~IVehiclePassNumberingFirstPassNum`
              - First pass number.

            * - :py:class:`~IVehiclePassBreak`
              - Satellite Pass Break properties.

            * - :py:class:`~IVehicleInertia`
              - Satellite inertia matrix parameters.

            * - :py:class:`~IVehicleMassProperties`
              - Satellite Mass properties.

            * - :py:class:`~IExportToolTimePeriod`
              - Specify Time Period.

            * - :py:class:`~IExportToolStepSize`
              - The step size.

            * - :py:class:`~IVehicleEphemerisCode500ExportTool`
              - The Code 500 Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :py:class:`~IVehicleEphemerisCCSDSExportTool`
              - The CCSDS Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :py:class:`~IVehicleEphemerisStkExportTool`
              - The STK Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :py:class:`~IVehicleCoordinateAxes`
              - IAgVeCoordinateAxes.

            * - :py:class:`~IVehicleCoordinateAxesCustom`
              - Custom.

            * - :py:class:`~IVehicleAttitudeExportTool`
              - Attitude file for the Export Ephemeris/Attitude File Tool.

            * - :py:class:`~IVehicleEphemerisSpiceExportTool`
              - The SPICE Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :py:class:`~IVehiclePropDefinitionExportTool`
              - Interface used to define the export to data file options.

            * - :py:class:`~IVehicleEphemerisStkBinaryExportTool`
              - The STK Binary Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :py:class:`~IVehicleEphemerisCCSDSv2ExportTool`
              - The CCSDSv2 Ephemeris type for the Export Ephemeris/Attitude Tool.

            * - :py:class:`~ISatelliteExportTools`
              - Interface used to define the export to data file options.

            * - :py:class:`~ISatellite`
              - Satellite properties.

            * - :py:class:`~ILaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :py:class:`~ILaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :py:class:`~ILaunchVehicleExportTools`
              - Interface for a launch vehicle object.

            * - :py:class:`~ILaunchVehicle`
              - Interface for a launch vehicle object.

            * - :py:class:`~IGroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :py:class:`~IGroundVehicleGraphics3D`
              - 3D Graphics properties for ground vehicles.

            * - :py:class:`~IGroundVehicleExportTools`
              - Interface used to define the export to data file options.

            * - :py:class:`~IGroundVehicle`
              - Interface for a ground vehicle object.

            * - :py:class:`~IMissileGraphics`
              - 2D Graphics for missiles.

            * - :py:class:`~IMissileGraphics3D`
              - 3D Graphics for missiles.

            * - :py:class:`~IMissileExportTools`
              - Interface used to define the export to data file options.

            * - :py:class:`~IMissile`
              - Interface for a missile object.

            * - :py:class:`~IAircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :py:class:`~IAircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :py:class:`~IAircraftExportTools`
              - Interface used to define the export to data file options.

            * - :py:class:`~IAircraft`
              - Interface for aircraft object.

            * - :py:class:`~IShipGraphics`
              - 2D Graphics options for a ship.

            * - :py:class:`~IShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :py:class:`~IShipExportTools`
              - Interface used to define the export to data file options.

            * - :py:class:`~IShip`
              - Interface for a ship object.

            * - :py:class:`~IMtoGraphics2DMarker`
              - Interface to define the 2D graphics attributes of the selected MTO track or tracks.

            * - :py:class:`~IMtoGraphics2DLine`
              - MTO track line display options.

            * - :py:class:`~IMtoGraphics2DFadeTimes`
              - MTO track fade times interface.

            * - :py:class:`~IMtoGraphics2DLeadTrailTimes`
              - MTO track lead/trail times interface.

            * - :py:class:`~IMtoGraphics2DTrack`
              - Interface to set 2D graphics attributes for each track in the MTO.

            * - :py:class:`~IMtoGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :py:class:`~IMtoDefaultGraphics2DTrack`
              - Interface to set 2D graphics attributes for default MTO tracks.

            * - :py:class:`~IMtoGraphics2DGlobalTrackOptions`
              - Interface for global 2D graphics options for an MTO.

            * - :py:class:`~IMtoGraphics`
              - MTO 2D Graphics interface.

            * - :py:class:`~IMtoGraphics3DModelArtic`
              - MTO ModelArticulation Interface.

            * - :py:class:`~IMtoGraphics3DMarker`
              - Interface for MTO 3D graphics marker options.

            * - :py:class:`~IMtoGraphics3DPoint`
              - MTO track 3D marker point options interface.

            * - :py:class:`~IMtoGraphics3DModel`
              - Interface for MTO track model options.

            * - :py:class:`~IMtoGraphics3DSwapDistances`
              - Interface for MTO track 3D swap distances.

            * - :py:class:`~IMtoGraphics3DDropLines`
              - Interface for MTO droplines.

            * - :py:class:`~IMtoGraphics3DTrack`
              - Interface for setting 3D graphics properties for MTO tracks.

            * - :py:class:`~IMtoGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :py:class:`~IMtoDefaultGraphics3DTrack`
              - Interface for setting 3D graphics properties for default MTO tracks.

            * - :py:class:`~IMtoGraphics3DGlobalTrackOptions`
              - Interface for global 3D graphics MTO track options.

            * - :py:class:`~IMtoGraphics3D`
              - Interface for MTO 3D graphics properties.

            * - :py:class:`~IMtoTrackPoint`
              - The points defined for the selected track.

            * - :py:class:`~IMtoTrackPointCollection`
              - MTO track point list.

            * - :py:class:`~IMtoTrack`
              - List of MTO tracks with basic information about each.

            * - :py:class:`~IMtoTrackCollection`
              - MTO Track List.

            * - :py:class:`~IMtoDefaultTrack`
              - Default MTO track.

            * - :py:class:`~IMtoGlobalTrackOptions`
              - Global MTO track options.

            * - :py:class:`~IMtoAnalysisPosition`
              - MTO position.

            * - :py:class:`~IMtoAnalysisVisibility`
              - MTO Visibility computation.

            * - :py:class:`~IMtoAnalysisFieldOfView`
              - MTO Field Of View computation.

            * - :py:class:`~IMtoAnalysisRange`
              - MTO range computation.

            * - :py:class:`~IMtoAnalysis`
              - MTO spatial state info.

            * - :py:class:`~IMto`
              - Multi-Track Object (MTO) interface.

            * - :py:class:`~ILineTargetGraphics`
              - Line Target 2D graphics.

            * - :py:class:`~ILineTargetGraphics3D`
              - Line Target 3D Graphics properties.

            * - :py:class:`~ILineTargetPoint`
              - Line Target Point interface.

            * - :py:class:`~ILineTargetPointCollection`
              - The collection of points for the line target.

            * - :py:class:`~ILineTarget`
              - Line Target Path properties.

            * - :py:class:`~IChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :py:class:`~IChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :py:class:`~IChainGraphics`
              - 2D graphics properties of a chain.

            * - :py:class:`~IChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :py:class:`~IAccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :py:class:`~IAccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :py:class:`~IChainConnectionCollection`
              - Represents a collection of connections.

            * - :py:class:`~IChainTimePeriodBase`
              - Chain time period options.

            * - :py:class:`~IChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :py:class:`~IChainConstraints`
              - Chain constraints.

            * - :py:class:`~IChainConnection`
              - Provide access to a Chain connection.

            * - :py:class:`~IChainOptimalStrandOpts`
              - Chain optimal strand options.

            * - :py:class:`~IChain`
              - Configuration options for chains.

            * - :py:class:`~ICoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :py:class:`~ICoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :py:class:`~ICoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :py:class:`~ICoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :py:class:`~ICoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :py:class:`~ICoverageGraphics3D`
              - 3D graphics options for the coverage grid.

            * - :py:class:`~ICoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :py:class:`~ICoverageGridPointSelection`
              - Represents a set of coverage grid points.

            * - :py:class:`~ICoverageGridInspector`
              - Provide access to the Coverage Definition grid inspector properties.

            * - :py:class:`~ICoverageRegionFilesCollection`
              - Region Files.

            * - :py:class:`~ICoverageAreaTargetsCollection`
              - Area Targets.

            * - :py:class:`~ICoveragePointFileListCollection`
              - Point file list collection.

            * - :py:class:`~ICoverageBounds`
              - Base interface for IAgCvBoundsCustom, IAgCvBoundsGlobal, IAgCvBoundsLat, IAgCvBoundsLatLines, IAgCvBoundsLonLines, IAgCvBoundsCustomBoundary.

            * - :py:class:`~ICoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :py:class:`~ICoverageBoundsCustomRegions`
              - Custom Regions.

            * - :py:class:`~ICoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :py:class:`~ICoverageBoundsLat`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :py:class:`~ICoverageBoundsLatLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :py:class:`~ICoverageBoundsLonLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :py:class:`~ICoverageBoundsLatLonRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :py:class:`~ICoverageResolution`
              - Base interface for IAgCvResolutionArea, IAgCvResolutionDistance and IAgCvResolutionLatLon, used to define coverage resolution (spacing between grid points).

            * - :py:class:`~ICoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~ICoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~ICoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :py:class:`~ICoverageGrid`
              - Grid Definition and resolution.

            * - :py:class:`~ICoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :py:class:`~ICoverageAssetListElement`
              - Coverage asset.

            * - :py:class:`~ICoverageAdvanced`
              - Advanced Properties.

            * - :py:class:`~ICoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :py:class:`~ICoverageDefinition`
              - Coverage definition properties.

            * - :py:class:`~IFigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :py:class:`~IFigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :py:class:`~IFigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :py:class:`~IFigureOfMeritGraphics2DLevelAttributesCollection`
              - Level Attributes.

            * - :py:class:`~IFigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :py:class:`~IFigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :py:class:`~IFigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :py:class:`~IFigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :py:class:`~IFigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :py:class:`~IFigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :py:class:`~IFigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~IFigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~IFigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :py:class:`~IFigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :py:class:`~IFigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :py:class:`~IFigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :py:class:`~IFigureOfMeritDefinitionScalarCalculation`
              - Figure of Merit using an Analysis Workbench scalar calculation component as the metric.

            * - :py:class:`~IFigureOfMeritGridInspector`
              - Provide access to the FOM grid inspector properties.

            * - :py:class:`~IFigureOfMeritNavigationAccuracyMethod`
              - Navigation Accuracy Figure of Merit type.

            * - :py:class:`~IFigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~IFigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~IFigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :py:class:`~IFigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~IFigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~IFigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionData`
              - IAgFmDefinitionData.

            * - :py:class:`~IFigureOfMeritDefinitionDataMinMax`
              - IAgFmDefDataMinMax.

            * - :py:class:`~IFigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :py:class:`~IFigureOfMeritDefinitionDataMinAssets`
              - Minimum number of assets.

            * - :py:class:`~IFigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :py:class:`~IFigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best four satellites.

            * - :py:class:`~IFigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :py:class:`~IFigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :py:class:`~IFigureOfMerit`
              - Figure of Merit properties.

            * - :py:class:`~IFigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :py:class:`~IFigureOfMeritDefinitionSystemAgeOfData`
              - System Age of Data Figure of Merit.

            * - :py:class:`~IConstellationConstraintRestriction`
              - A base interface for all interfaces returned by the Restriction property of the IAgCnConstraints interface. It can be cast to IAgCnCnstrObjectRestriction.

            * - :py:class:`~IConstellationConstraintObjectRestriction`
              - A restriction interface that is satisfied only when specified number of objects meets the conditions for the chain access.

            * - :py:class:`~IConstellationConstraints`
              - Constellation Constraints.

            * - :py:class:`~IConstellationGraphics`
              - Graphics options for constellation.

            * - :py:class:`~IConstellationRouting`
              - Routing options for constellation.

            * - :py:class:`~IConstellation`
              - Configuration options for constellations.

            * - :py:class:`~IEventDetectionStrategy`
              - Define a base interface for the event detection strategies.

            * - :py:class:`~IEventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :py:class:`~IEventDetectionSubSampling`
              - Interface for event detection strategy involving subsampling.

            * - :py:class:`~ISamplingMethodStrategy`
              - Define a base interface for the sampling method strategies.

            * - :py:class:`~ISamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :py:class:`~ISamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :py:class:`~ISpaceEnvironmentRadEnergyMethodSpecify`
              - Customized energy lists for protons and electrons.

            * - :py:class:`~ISpaceEnvironmentRadEnergyValues`
              - Energy values for computing electron and proton flux.

            * - :py:class:`~ISpaceEnvironmentRadiationEnvironment`
              - Radiation environment settings.

            * - :py:class:`~ISpaceEnvironmentMagnitudeFieldGraphics2D`
              - Graphics settings for showing magnetic field.

            * - :py:class:`~ISpaceEnvironmentScenarioExtGraphics3D`
              - Graphics settings for space environment.

            * - :py:class:`~ISpaceEnvironmentSAAContour`
              - SAA Contour settings.

            * - :py:class:`~IVehicleSpaceEnvironmentMagneticField`
              - Magnetic field model.

            * - :py:class:`~IVehicleSpaceEnvironmentVehTemperature`
              - Vehicle temperature model.

            * - :py:class:`~IVehicleSpaceEnvironmentParticleFlux`
              - Particle Flux model.

            * - :py:class:`~IVehicleSpaceEnvironmentRadDoseRateElement`
              - Dose rate interface.

            * - :py:class:`~IVehicleSpaceEnvironmentRadDoseRateCollection`
              - The collection holds dose rate elements computed for each shielding thickness.

            * - :py:class:`~IVehicleSpaceEnvironmentRadiation`
              - Radiation model.

            * - :py:class:`~IVehicleSpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for showing magnetic field line.

            * - :py:class:`~IVehicleSpaceEnvironmentGraphics`
              - Graphics settings for space environment.

            * - :py:class:`~IStkPreferencesVDF`
              - VDF Load/Save settings.

            * - :py:class:`~IStkPreferencesConnect`
              - Connect settings.

            * - :py:class:`~IStkPreferencesPythonPlugins`
              - Python plugin settings.

            * - :py:class:`~IPathCollection`
              - Collection to add and remove paths.

            * - :py:class:`~IVehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~IVehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~IVehicleAttitudeSlewBase`
              - Represents an attitude slew base type.

            * - :py:class:`~IVehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :py:class:`~IVehicleAttitudeSlewFixedRate`
              - Fixed Rate slew.

            * - :py:class:`~IVehicleAttitudeSlewFixedTime`
              - Fixed Time slew.

            * - :py:class:`~IVmGridDefinition`
              - Base interface IAgVmGridDefinition. IAgVmGridSpatialCalculation and IAgVmExternalFile implement this interface.

            * - :py:class:`~IVmAnalysisInterval`
              - IAgVmAnalysisInterval Interface for volume analysis interval.

            * - :py:class:`~IVmAdvanced`
              - IAgVmAdvanced Interface for advanced volumetric options.

            * - :py:class:`~IVmGraphics3D`
              - IAgVmVO Interface for a volumetric object's 3D Graphics properties.

            * - :py:class:`~IVmGraphics3DGrid`
              - IAgVmVO Interface for a volumetric object's 3D Graphics properties.

            * - :py:class:`~IVmGraphics3DCrossSection`
              - IAgVmVOCrossSection Interface for defining planar cross-sections through the volumetric grid.

            * - :py:class:`~IVmGraphics3DCrossSectionPlaneCollection`
              - IAgVmVOCrossSectionPlaneCollection Interface for defining collections of planar cross-sections for the volumetric grid.

            * - :py:class:`~IVmGraphics3DVolume`
              - IAgVmVOVolume Interface for defining volume for volumetric object.

            * - :py:class:`~IVmGraphics3DActiveGridPoints`
              - IAgVmVOActiveGridPoints Interface for defining Active Grid Points for Volumetric Object.

            * - :py:class:`~IVmGraphics3DSpatialCalculationLevels`
              - IAgVmVOSpatialCalculationLevels Interface for defining Spatial Calculation Levels for Volumetric Object.

            * - :py:class:`~IVmGraphics3DSpatialCalculationLevelCollection`
              - IAgVmVOSpatialCalculationLevelCollection Interface for defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~IVmGraphics3DLegend`
              - IAgVmVOLegend Interface for defining boundary/fill legend for volumetric object.

            * - :py:class:`~IVmExportTool`
              - The Volumetric Export Tool.

            * - :py:class:`~IVolumetric`
              - Volumetric properties.

            * - :py:class:`~IVmGridSpatialCalculation`
              - IAgVmGridSpatialCalculation Interface volume grid spatial calculation.

            * - :py:class:`~IVmExternalFile`
              - IAgVmExternalFile Interface for volume external file.

            * - :py:class:`~IVmGraphics3DCrossSectionPlane`
              - IAgVmVOCrossSectionPlane Interface for defining planar cross-sections through the volumetric grid.

            * - :py:class:`~IVmGraphics3DSpatialCalculationLevel`
              - IAgVmVOSpatialCalculationLevel Interface for defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~ISatelliteCollection`
              - SatelliteCollection properties.

            * - :py:class:`~ISubset`
              - Subset properties.

            * - :py:class:`~IAdvCATAvailableObjectCollection`
              - IAgAdvCATAvailableObjectCollection represents available objects.

            * - :py:class:`~IAdvCATChosenObjectCollection`
              - Chosen object collection.

            * - :py:class:`~IAdvCATPreFilters`
              - Pre-Filters.

            * - :py:class:`~IAdvCATAdvancedEllipsoid`
              - Advanced ellipsoid properties.

            * - :py:class:`~IAdvCATAdvanced`
              - AdvCAT Advanced properties.

            * - :py:class:`~IAdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :py:class:`~IAdvCAT`
              - AgAdvCAT properties.

            * - :py:class:`~IAdvCATChosenObject`
              - Chosen object.

            * - :py:class:`~IEOIRShapeObject`
              - A shape object interface.

            * - :py:class:`~IEOIRShapeBox`
              - A box shape interface.

            * - :py:class:`~IEOIRShapeCone`
              - A cone shape interface.

            * - :py:class:`~IEOIRShapePlate`
              - A plate shape interface.

            * - :py:class:`~IEOIRShapeSphere`
              - A sphere shape interface.

            * - :py:class:`~IEOIRShapeCoupler`
              - A coupler shape interface.

            * - :py:class:`~IEOIRShapeNone`
              - A none shape interface.

            * - :py:class:`~IEOIRShapeGEOComm`
              - A GEOComm shape interface.

            * - :py:class:`~IEOIRShapeLEOComm`
              - A LEOComm shape interface.

            * - :py:class:`~IEOIRShapeLEOImaging`
              - A LEOImaging shape interface.

            * - :py:class:`~IEOIRShapeCustomMesh`
              - A custom mesh shape interface.

            * - :py:class:`~IEOIRShapeTargetSignature`
              - A target signature shape interface.

            * - :py:class:`~IEOIRStagePlume`
              - A stage interface.

            * - :py:class:`~IEOIRShape`
              - A shape interface.

            * - :py:class:`~IEOIRStage`
              - A stage interface.

            * - :py:class:`~IEOIRShapeCollection`
              - IAgEOIRShapeCollection Interface.

            * - :py:class:`~IEOIRMaterialElement`
              - A material element interface.

            * - :py:class:`~IEOIRMaterialElementCollection`
              - IAgEOIRMaterialElementCollection Interface.

            * - :py:class:`~IMissileEOIR`
              - EOIR interface.

            * - :py:class:`~IVehicleEOIR`
              - Property used to access the IAgEOIR interface.

            * - :py:class:`~IEOIRShapeCylinder`
              - A cylinder shape interface.

            * - :py:class:`~IStkObjectChangedEventArgs`
              - Contains information about the changes in the object's state.

            * - :py:class:`~IScenarioBeforeSaveEventArgs`
              - Contains information about the changes in the object's state.

            * - :py:class:`~IPctCmpltEventArgs`
              - Represents a structure used by the Percent Complete events.

            * - :py:class:`~IStkObjectPreDeleteEventArgs`
              - Arguments for the OnStkObjectPreDelete event.

            * - :py:class:`~IStkObjectCutCopyPasteEventArgs`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~StkObject`
              - Represents a generic STK object.

            * - :py:class:`~StkObjectRoot`
              - Top-level object in the Object Model Hierarchy.

            * - :py:class:`~LevelAttribute`
              - Properties defining display of contour levels.

            * - :py:class:`~LevelAttributeCollection`
              - Collection of properties defining display of contour levels.

            * - :py:class:`~BasicAzElMask`
              - The Azimuth-Elevation Mask class.

            * - :py:class:`~FacilityGraphics`
              - 2D Graphics properties of a Facility.

            * - :py:class:`~PlaceGraphics`
              - 2D Graphics properties of a Place.

            * - :py:class:`~Graphics2DRangeContours`
              - Class defining 2D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~AccessConstraint`
              - Class defining access constraints.

            * - :py:class:`~AccessConstraintCollection`
              - Collection of access constraints.

            * - :py:class:`~Graphics3DRangeContours`
              - Class defining 3D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

            * - :py:class:`~Graphics3DOffsetRotate`
              - Class defining rotation in the object body frame's X, Y and Z directions.

            * - :py:class:`~Graphics3DOffsetTransformation`
              - Class defining model translation in the object body frame's X, Y and Z directions.

            * - :py:class:`~Graphics3DOffsetAttach`
              - Class defining attach points for the attachment of lines to objects.

            * - :py:class:`~Graphics3DOffsetLabel`
              - Class defining the offset of the position of an object label in the 3D Graphics window.

            * - :py:class:`~Graphics3DOffset`
              - Class defining 3D offset attributes.

            * - :py:class:`~Graphics3DMarkerShape`
              - Class defining the marker type that represents the object in the 3D Graphics window.

            * - :py:class:`~Graphics3DMarkerFile`
              - Class defining 3D marker file attributes.

            * - :py:class:`~Graphics3DMarker`
              - Class defining the 3D marker to represent an object at a specified threshold.

            * - :py:class:`~Graphics3DDetailThreshold`
              - Class defining detail thresholds as an aid for improving performance when viewing in 3D.

            * - :py:class:`~Graphics3DModelItem`
              - Class defining selection and display of 3D models.

            * - :py:class:`~Graphics3DModelCollection`
              - Collection representing 3D model list.

            * - :py:class:`~LabelNote`
              - Class defining label notes.

            * - :py:class:`~LabelNoteCollection`
              - Collection representing label notes list.

            * - :py:class:`~Graphics3DVector`
              - Class defining 3D vectors.

            * - :py:class:`~FacilityGraphics3D`
              - 3D Graphics properties of a Facility.

            * - :py:class:`~PlaceGraphics3D`
              - 3D Graphics properties of a Place.

            * - :py:class:`~TerrainNormSlopeAzimuth`
              - Class defining Slope/Azimuth data for the TerrainNormal.

            * - :py:class:`~IntervalCollection`
              - Class defining display intervals.

            * - :py:class:`~ImmutableIntervalCollection`
              - Read-only collection of intervals.

            * - :py:class:`~DuringAccess`
              - Class defining display intervals in terms of access to objects.

            * - :py:class:`~DisplayTimesTimeComponent`
              - Provide methods to configure the display times using Timeline API components.

            * - :py:class:`~StarGraphics3D`
              - Class defining 3D Graphics properties of a Star.

            * - :py:class:`~StarGraphics`
              - Class defining 2D Graphics properties of a Star.

            * - :py:class:`~PlanetGraphics3D`
              - Class defining 3D Graphics properties of a Planet.

            * - :py:class:`~PlanetGraphics`
              - Class defining 2D Graphics properties of a Planet.

            * - :py:class:`~AreaTypePattern`
              - Class defining coordinates of the AreaTarget AreaType.

            * - :py:class:`~AreaTypePatternCollection`
              - Class defining the list of coordinates of the AreaTarget AreaType.

            * - :py:class:`~AreaTypeEllipse`
              - Class defining the AreaTarget AreaType in terms of MajorAxis, MinorAxis and Bearing.

            * - :py:class:`~AreaTargetGraphics3D`
              - Class to define the 3D attributes of an AreaTarget.

            * - :py:class:`~AreaTargetGraphics`
              - Class to define the 2D attributes of an AreaTarget.

            * - :py:class:`~Graphics3DAzElMask`
              - Class to define display labels and adjust the translucency of the 3D azimuth-elevation mask for a facility, place or target.

            * - :py:class:`~Graphics3DModelArtic`
              - Class defining 3D model articulations.

            * - :py:class:`~Graphics3DModelTransformationCollection`
              - Collection of available transformations in a model.

            * - :py:class:`~Graphics3DModelTransformation`
              - Class to modify transformation values.

            * - :py:class:`~Graphics3DModelFile`
              - Class defining 3D model file.

            * - :py:class:`~PlanetPositionFile`
              - Class defining the planetary ephemeris file.

            * - :py:class:`~PlanetPositionCentralBody`
              - Class defining central body used to define Planet object.

            * - :py:class:`~PlanetOrbitDisplayTime`
              - Class defining display time of a planet's orbit.

            * - :py:class:`~Scenario`
              - Class defining the Scenario object.

            * - :py:class:`~ScenarioAnimation`
              - Class defining the animation properties of a Scenario.

            * - :py:class:`~ScenarioEarthData`
              - Class defining the Earth Orientation Parameters of a Scenario.

            * - :py:class:`~ScenarioGraphics`
              - Class defining the 2D Graphics properties of a Scenario.

            * - :py:class:`~TerrainCollection`
              - Collection of terrain data files available in the Scenario for visualization and analysis.

            * - :py:class:`~Terrain`
              - Class defining terrain data for a Scenario.

            * - :py:class:`~TilesetCollection3D`
              - Collection of 3DTilesets available in the Scenario for analysis.

            * - :py:class:`~Tileset3D`
              - Class defining Analytical 3DTileset for a Scenario.

            * - :py:class:`~ScenarioGenDatabaseCollection`
              - Collection of Scenario database settings.

            * - :py:class:`~ScenarioGenDatabase`
              - Class defining database settings of the Scenario.

            * - :py:class:`~ScenarioGraphics3D`
              - Class defining 3D Graphics properties of the Scenario.

            * - :py:class:`~SensorComplexConicPattern`
              - Class defining the complex conic pattern for a Sensor.

            * - :py:class:`~SensorEOIRPattern`
              - Class defining the EOIR pattern for a Sensor.

            * - :py:class:`~SensorUnknownPattern`
              - Unsupported/unknown sensor pattern.

            * - :py:class:`~SensorEOIRBandCollection`
              - Class defining the band collection for an EOIR Sensor.

            * - :py:class:`~SensorEOIRBand`
              - Class defining an EOIR band.

            * - :py:class:`~SensorEOIRRadiometricPair`
              - Class defining an Sensitivities item.

            * - :py:class:`~SensorEOIRSensitivityCollection`
              - Class defining the Sensitivities collection for an EOIR Sensor.

            * - :py:class:`~SensorEOIRSaturationCollection`
              - Class defining the Saturations collection for an EOIR Sensor.

            * - :py:class:`~SensorCustomPattern`
              - Class defining the custom pattern for a Sensor.

            * - :py:class:`~SensorHalfPowerPattern`
              - Class defining the half-power pattern for a Sensor.

            * - :py:class:`~SensorRectangularPattern`
              - Class defining the rectangular pattern for a Sensor.

            * - :py:class:`~SensorSARPattern`
              - Class defining the Synthetic Aperture Radar (SAR) pattern for a Sensor.

            * - :py:class:`~SensorSimpleConicPattern`
              - Class defining the simple conic pattern for a Sensor.

            * - :py:class:`~SensorPointingFixed`
              - Class defining the fixed pointing type for a Sensor.

            * - :py:class:`~SensorPointingFixedAxes`
              - Class defining the fixed in axes pointing type for a Sensor.

            * - :py:class:`~SensorPointing3DModel`
              - Class defining the 3D model pointing type for a Sensor.

            * - :py:class:`~SensorPointingSpinning`
              - Class defining the spinning pointing type for a Sensor.

            * - :py:class:`~SensorPointingTargeted`
              - Class defining the targeted pointing type for a Sensor.

            * - :py:class:`~SensorPointingExternal`
              - Class defining the external file-defined pointing type for a Sensor.

            * - :py:class:`~SensorPointingTargetedBoresightTrack`
              - Class defining a targeted sensor with tracking boresight.

            * - :py:class:`~SensorPointingTargetedBoresightFixed`
              - Class defining a targeted Sensor with fixed boresight.

            * - :py:class:`~SensorTargetCollection`
              - Class defining the target collection for a target-pointing Sensor.

            * - :py:class:`~SensorTarget`
              - Class defining a Sensor target.

            * - :py:class:`~AccessTime`
              - Class for defining Sensor target times in terms of access.

            * - :py:class:`~ScheduleTime`
              - Class for defining Sensor target times in terms of a specified schedule.

            * - :py:class:`~SensorAzElMaskFile`
              - Class to define a Sensor's Azimuth-Elevation mask.

            * - :py:class:`~SensorGraphics`
              - Class defining the 2D Graphics properties of a Sensor.

            * - :py:class:`~SensorProjection`
              - Class defining the projection properties of a Sensor.

            * - :py:class:`~SensorProjectionDisplayDistance`
              - Class defining projection altitude options for a sensor.

            * - :py:class:`~SensorGraphics3D`
              - Class defining 3D Graphics properties of a Sensor.

            * - :py:class:`~SensorGraphics3DPulse`
              - Class defining 3D pulse properties of a Sensor.

            * - :py:class:`~SensorGraphics3DOffset`
              - Class defining 3D Graphics vertex offset properties of a Sensor.

            * - :py:class:`~AccessConstraintTimeSlipRange`
              - Class for controlling the use the Time Slip constraint for a missile or launch vehicle, used with the Close Approach Tool.

            * - :py:class:`~AccessConstraintBackground`
              - Class related to the Background constraint, which constrains access periods based on whether the Earth is or is not in the background.

            * - :py:class:`~AccessConstraintGroundTrack`
              - Class related to the Ground Track constraint, which constrains access to the Ascending or Descending side of the Satellite's ground track.

            * - :py:class:`~AccessConstraintMinMax`
              - Class related to defining constraints in terms of minimum and/or maximum values.

            * - :py:class:`~AccessConstraintCrdnConstellation`
              - Class related to Vector constraints.

            * - :py:class:`~AccessConstraintCentralBodyObstruction`
              - Class defining constraints in terms of obstruction by a specified central body.

            * - :py:class:`~AccessConstraintAngle`
              - Class defining Angle constraints, limiting access to intervals during which the selected angle is within the specified minimum and maximum limits.

            * - :py:class:`~AccessConstraintCondition`
              - Class defining access constraints in terms of lighting conditions.

            * - :py:class:`~AccessTimeCollection`
              - Collection of access times.

            * - :py:class:`~ScheduleTimeCollection`
              - Collection of user-scheduled access times.

            * - :py:class:`~AccessConstraintIntervals`
              - Class defining the Intervals constraint.

            * - :py:class:`~AccessConstraintObjExAngle`
              - Class defining the Object Exclusion Angle constraint.

            * - :py:class:`~AccessConstraintZone`
              - Class defining the Exclusion Zone constraint.

            * - :py:class:`~AccessConstraintThirdBody`
              - Do not use this class, as it is deprecated. Use AgAccessCnstrCbObstruction instead. Class defining Central Body Obstruction constraints.

            * - :py:class:`~AccessConstraintExclZonesCollection`
              - Collection of Exclusion Zones used in Exclusion Zone constraint.

            * - :py:class:`~AccessConstraintGrazingAltitude`
              - Class defining the Grazing Altidude constraint.

            * - :py:class:`~SensorPointingGrazingAltitude`
              - Class defining Grazing Altitude pointing type for a Sensor.

            * - :py:class:`~AreaTarget`
              - Class defining the AreaTarget object.

            * - :py:class:`~Facility`
              - Class defining the Facility object.

            * - :py:class:`~Target`
              - Class defining the Target object.

            * - :py:class:`~Place`
              - Class defining the Place object.

            * - :py:class:`~Planet`
              - Class defining the Planet object.

            * - :py:class:`~Sensor`
              - Class defining the Sensor class.

            * - :py:class:`~SensorCommonTasks`
              - Class defining the Sensor Common class.

            * - :py:class:`~AreaTargetCommonTasks`
              - Class defining the Area Target Common class.

            * - :py:class:`~PlanetCommonTasks`
              - Class defining the Planet Common class.

            * - :py:class:`~Swath`
              - Class defining Swath properties.

            * - :py:class:`~Star`
              - Class defining the Star object.

            * - :py:class:`~DataProviderCollection`
              - Collection of data providers attached to the current STK object.

            * - :py:class:`~DataProviderResultTimeArrayElements`
              - Provide a array result of element values for each time array value.

            * - :py:class:`~DataProviderResult`
              - Results returned by the data provider.

            * - :py:class:`~DataProviderResultSubSectionCollection`
              - Represents a collection of subsections returned by the data providers.

            * - :py:class:`~DataProviderResultSubSection`
              - Represents a subsection in the data returned by the data providers.

            * - :py:class:`~DataProviderResultIntervalCollection`
              - Represents a collection of intervals returned by the data providers.

            * - :py:class:`~DataProviderResultInterval`
              - Represents a interval in the collection of intervals returned by the data providers.

            * - :py:class:`~DataProviderResultDataSetCollection`
              - Represents a collection of datasets in the interval returned by the data providers.

            * - :py:class:`~DataProviderResultDataSet`
              - Represents a dataset in the collection of datasets returned by the data providers.

            * - :py:class:`~DataProviderFixed`
              - Support for fixed data providers (i.e. non time-dependent like Facility position).

            * - :py:class:`~DataProviderTimeVarying`
              - Support for time-dependent data providers (e.g. Satellite position).

            * - :py:class:`~DataProviderInterval`
              - Support for interval data providers (e.g. Facility lighting times).

            * - :py:class:`~DataProviderResultTextMessage`
              - Notification or failure messages returned by the data provider.

            * - :py:class:`~DataProviderGroup`
              - Group of sub data providers (e.g. ``Cartesian Position`` on Satellites).

            * - :py:class:`~DataProviderElements`
              - Elements returned by the data provider (e.g. ``x``, ``y``, ``z``).

            * - :py:class:`~DataProviderElement`
              - Class defining a data provider element.

            * - :py:class:`~DataProviders`
              - Class defining data providers.

            * - :py:class:`~StkAccess`
              - Class defining Access.

            * - :py:class:`~StkAccessGraphics`
              - Class defining 2D Graphics for Access.

            * - :py:class:`~StkAccessAdvanced`
              - Class defining advanced Access settings.

            * - :py:class:`~AccessTimePeriod`
              - Allow configuring the object's access interval.

            * - :py:class:`~AccessTimeEventIntervals`
              - Allow configuring the access time period using a list of timeline intervals.

            * - :py:class:`~StkObjectCoverage`
              - Class defining object coverage.

            * - :py:class:`~ObjectCoverageFigureOfMerit`
              - Class defining the fom on the coverage object tool.

            * - :py:class:`~Scenario3dFont`
              - Font properties for Scenario 3D Graphics.

            * - :py:class:`~Graphics3DBorderWall`
              - Class defining 3D Graphics border wall properties.

            * - :py:class:`~Graphics3DReferenceAnalysisWorkbenchCollection`
              - Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~Graphics3DReferenceVectorGeometryToolVector`
              - Class defining a reference vector (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~Graphics3DReferenceVectorGeometryToolAxes`
              - Class defining a set of reference axes (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~Graphics3DReferenceVectorGeometryToolAngle`
              - Class defining a reference angle (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~Graphics3DReferenceVectorGeometryToolPlane`
              - Class defining a reference plane (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~Graphics3DReferenceVectorGeometryToolPoint`
              - Class defining a reference point (3D Graphics, Vector Geometry Tool).

            * - :py:class:`~TargetGraphics`
              - Class defining 2D Graphics for a Target object.

            * - :py:class:`~TargetGraphics3D`
              - Class defining 3D Graphics for a Target object.

            * - :py:class:`~PointTargetGraphics3DModel`
              - Point properties for a 3D model.

            * - :py:class:`~ObjectLinkCollection`
              - Collection of names of STK objects that are available in the current Scenario.

            * - :py:class:`~ObjectLink`
              - Class defining name of an STK object.

            * - :py:class:`~LinkToObject`
              - Class defining a link to an STK object.

            * - :py:class:`~LLAPosition`
              - Class defining position defined in terms of latitude, longitude and altitude (LLA).

            * - :py:class:`~Graphics3DDataDisplayElement`
              - Class defining 3D Graphics data display element.

            * - :py:class:`~Graphics3DDataDisplayCollection`
              - Collection of 3D Graphics data display text.

            * - :py:class:`~VehicleInitialState`
              - Class defining the initial state of the vehicle.

            * - :py:class:`~VehicleHPOPCentralBodyGravity`
              - Class defining Central Body Gravity options for the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~VehicleRadiationPressure`
              - Class defining solar radiation pressure on a vehicle.

            * - :py:class:`~VehicleHPOPSolarRadiationPressure`
              - Class defining HPOP solar radiation pressure properties.

            * - :py:class:`~VehicleSolarFluxGeoMagnitudeEnterManually`
              - Class defining the option to enter a vehicle's solar flux and/or GeoMag properties manually, depending on the selected atmospheric density model.

            * - :py:class:`~VehicleSolarFluxGeoMagnitudeUseFile`
              - Class defining the option to load a vehicle's solar flux and/or GeoMag properties from an external file.

            * - :py:class:`~VehicleHPOPForceModelDrag`
              - Class defining the HPOP atmospheric drag model.

            * - :py:class:`~VehicleHPOPForceModelDragOptions`
              - Class defining HPOP atmospheric drag options.

            * - :py:class:`~VehicleHPOPSolarRadiationPressureOptions`
              - Class defining HPOP solar radiation pressure options.

            * - :py:class:`~VehicleStatic`
              - Class defining static force model options for the HPOP propagator.

            * - :py:class:`~VehicleSolidTides`
              - Class defining the contribution of solid tides.

            * - :py:class:`~VehicleOceanTides`
              - Class defining the contribution of ocean tides.

            * - :py:class:`~VehiclePluginSettings`
              - Class defining force model plugin settings for HPOP.

            * - :py:class:`~VehiclePluginPropagator`
              - Class defining a propagator plugin for HPOP for customization of the accelerations used in the propagation of the satellite trajectory.

            * - :py:class:`~VehicleHPOPForceModelMoreOptions`
              - Class defining additional force model options for HPOP.

            * - :py:class:`~VehicleHPOPForceModel`
              - Class defining HPOP force models.

            * - :py:class:`~VehicleStepSizeControl`
              - Class defining step size control for the HPOP integrator.

            * - :py:class:`~VehicleTimeRegularization`
              - Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

            * - :py:class:`~VehicleInterpolation`
              - Class defining interpolation for the HPOP integrator.

            * - :py:class:`~VehicleIntegrator`
              - Class defining the HPOP integrator.

            * - :py:class:`~VehicleGravity`
              - Class defining gravity modeling options for a vehicle.

            * - :py:class:`~VehiclePositionVelocityElement`
              - Class defining position and velocity elements for HPOP covariance.

            * - :py:class:`~VehiclePositionVelocityCollection`
              - Collection of position and velocity elements for HPOP covariance.

            * - :py:class:`~VehicleCorrelationListCollection`
              - Collection representing HPOP covariance matrix.

            * - :py:class:`~VehicleCorrelationListElement`
              - Class representing an element of an HPOP covariance matrix.

            * - :py:class:`~VehicleCovariance`
              - Class defining HPOP covariance.

            * - :py:class:`~VehicleJxInitialState`
              - Class defining initial state for the J2/4 propagators.

            * - :py:class:`~VehicleLOPCentralBodyGravity`
              - Class defining gravity options for the LOP propagator.

            * - :py:class:`~VehicleThirdBodyGravityElement`
              - Class defining third-body gravity options for the LOP propagator.

            * - :py:class:`~VehicleThirdBodyGravityCollection`
              - Collection of third-body gravity options for the LOP propagator.

            * - :py:class:`~VehicleExpDensModelParams`
              - Class defining the Exponential atmospheric density model for the LOP propagator.

            * - :py:class:`~VehicleAdvanced`
              - Class defining advanced atmospheric density options for the LOP propagator.

            * - :py:class:`~VehicleLOPForceModelDrag`
              - Class defining the atmospheric drag model for the LOP propagator.

            * - :py:class:`~VehicleLOPSolarRadiationPressure`
              - Class defining the solar radiation pressure model for the LOP propagator.

            * - :py:class:`~VehiclePhysicalData`
              - Class defining physical data for the LOP force model.

            * - :py:class:`~VehicleLOPForceModel`
              - Class defining the force model for the LOP propagator.

            * - :py:class:`~VehicleSegmentsCollection`
              - Collection of segments for a vehicle.

            * - :py:class:`~VehiclePropagatorHPOP`
              - Class defining the High Precision Orbit Propagator (HPOP).

            * - :py:class:`~VehiclePropagatorJ2Perturbation`
              - Class defining the J2 perturbation propagator.

            * - :py:class:`~VehiclePropagatorJ4Perturbation`
              - Class defining the J4 perturbation propagator.

            * - :py:class:`~VehiclePropagatorLOP`
              - Class defining the Long-term Orbit Predictor (LOP).

            * - :py:class:`~VehiclePropagatorSGP4`
              - Class defining the SGP4 propagator.

            * - :py:class:`~VehiclePropagatorSPICE`
              - Class defining the SPICE propagator.

            * - :py:class:`~VehiclePropagatorStkExternal`
              - Class defining the STK External propagator.

            * - :py:class:`~VehiclePropagatorTwoBody`
              - Class defining the two body propagator.

            * - :py:class:`~VehiclePropagatorUserExternal`
              - Class defining the user-external propagator.

            * - :py:class:`~VehicleLaunchVehicleInitialState`
              - Class defining launch vehicle initial state.

            * - :py:class:`~VehiclePropagatorSimpleAscent`
              - Class defining the simple ascent propagator for a launch vehicle.

            * - :py:class:`~VehicleWaypointsElement`
              - Class defining a waypoint for a Great Arc vehicle.

            * - :py:class:`~VehicleWaypointsCollection`
              - Collection of waypoints for a Great Arc vehicle.

            * - :py:class:`~VehicleLaunchLLA`
              - Class defining geodetic launch latitude, longitude and altitude for a Missile or LaunchVehicle.

            * - :py:class:`~VehicleLaunchLLR`
              - Class defining geocentric launch latitude, longitude and radius for a Missile or LaunchVehicle.

            * - :py:class:`~VehicleImpactLLA`
              - Class defining geodetic impact latitude, longitude and altitude for a Missile.

            * - :py:class:`~VehicleImpactLLR`
              - Class defining geocentric impact latitude, longitude and radius for a Missile.

            * - :py:class:`~VehicleLaunchControlFixedApogeeAltitude`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed apogee altitude.

            * - :py:class:`~VehicleLaunchControlFixedDeltaV`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V.

            * - :py:class:`~VehicleLaunchControlFixedDeltaVMinEccentricity`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed delta V with minimum eccentricity.

            * - :py:class:`~VehicleLaunchControlFixedTimeOfFlight`
              - Class defining the option to set a Missile's flight parameters by specifying a fixed time of flight.

            * - :py:class:`~VehicleImpactLocationLaunchAzEl`
              - Class defining the option to use azimuth and elevation to specify the Missile's impact location.

            * - :py:class:`~VehicleImpactLocationPoint`
              - Class defining a Missile's impact location.

            * - :py:class:`~VehiclePropagatorBallistic`
              - Class defining the ballistic propagator for a Missile.

            * - :py:class:`~VehiclePropagatorGreatArc`
              - Class defining the Great Arc propagator for an Aircraft, Ship or GroundVehicle.

            * - :py:class:`~VehicleSGP4SegmentCollection`
              - Set of Trajectories.

            * - :py:class:`~VehicleSGP4Segment`
              - SGP4 propagator segment.

            * - :py:class:`~VehicleThirdBodyGravity`
              - Third body gravity options for Long-range Orbit Predictor (LOP) propagator.

            * - :py:class:`~VehicleConsiderAnalysisCollectionElement`
              - Item in Consider Analysis list for HPOP covariance.

            * - :py:class:`~VehicleConsiderAnalysisCollection`
              - The Consider Analysis list for HPOP covariance.

            * - :py:class:`~VehicleSPICESegment`
              - SPICE propagator segment.

            * - :py:class:`~VehicleWaypointAltitudeReferenceTerrain`
              - Terrain altitude reference.

            * - :py:class:`~VehicleWaypointAltitudeReference`
              - Altitude references.

            * - :py:class:`~VehicleSGP4LoadFile`
              - SGP4 propagator. Allows the user to load segments from file.

            * - :py:class:`~VehicleSGP4OnlineLoad`
              - SGP4 propagator. Allows the user to load segments from online.

            * - :py:class:`~VehicleSGP4OnlineAutoLoad`
              - Do not use this class, as it is deprecated. Use AgVeSGP4OnlineLoad instead. SGP4 propagator. Allows the user to load the most current segment from online.

            * - :py:class:`~VehicleGroundEllipsesCollection`
              - List of Ground Ellipses.

            * - :py:class:`~Satellite`
              - Satellite properties.

            * - :py:class:`~VehicleInertia`
              - Satellite inertia matrix parameters.

            * - :py:class:`~VehicleMassProperties`
              - Satellite Mass properties.

            * - :py:class:`~VehicleBreakAngleBreakByLatitude`
              - Pass break latitude.

            * - :py:class:`~VehicleBreakAngleBreakByLongitude`
              - Pass break longitude.

            * - :py:class:`~VehicleDefinition`
              - Pass break definition properties.

            * - :py:class:`~VehicleRepeatGroundTrackNumbering`
              - Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

            * - :py:class:`~VehiclePassNumberingDateOfFirstPass`
              - Date of first pass for pass numbering.

            * - :py:class:`~VehiclePassNumberingFirstPassNum`
              - First pass number.

            * - :py:class:`~VehiclePassBreak`
              - Satellite Pass Break properties.

            * - :py:class:`~VehicleCentralBodies`
              - Satellite Central Bodies.

            * - :py:class:`~SatelliteGraphics`
              - Satellite 2D Graphics properties.

            * - :py:class:`~SatelliteGraphics3D`
              - 3D Graphics properties of a satellite.

            * - :py:class:`~VehicleEllipseDataElement`
              - Ground ellipse data.

            * - :py:class:`~VehicleEllipseDataCollection`
              - Ellipse Data Collection.

            * - :py:class:`~VehicleGroundEllipseElement`
              - Ground ellipse.

            * - :py:class:`~SatelliteGraphics3DModel`
              - All Satellite's VO Model properties.

            * - :py:class:`~VehicleEclipseBodies`
              - Satellite Eclipse Bodies, for defining the eclipse central body list used for lighting computations.

            * - :py:class:`~VehicleVector`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~VehicleRateOffset`
              - AgVeSpin Class.

            * - :py:class:`~VehicleProfileAlignedAndConstrained`
              - Aligned and Constrained attitude profile.

            * - :py:class:`~VehicleProfileInertial`
              - Inertially fixed attitude profile: maintains a constant orientation of the body-fixed axes with respect to the inertial axes, using the selected coordinate type.

            * - :py:class:`~VehicleProfileConstraintOffset`
              - Constraint offset for various attitude profiles.

            * - :py:class:`~VehicleProfileFixedInAxes`
              - Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

            * - :py:class:`~VehicleProfilePrecessingSpin`
              - Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

            * - :py:class:`~VehicleProfileSpinAboutXXX`
              - Shared for Spin About Nadir and Spin About Sun Vector profile parameters.

            * - :py:class:`~VehicleProfileSpinning`
              - Spinning attitude profile.

            * - :py:class:`~VehicleProfileAlignmentOffset`
              - Alignment offset for various attitude profiles.

            * - :py:class:`~VehicleScheduleTimesCollection`
              - List of scheduled accesses.

            * - :py:class:`~VehicleTargetTimes`
              - Target times for target pointing attitude.

            * - :py:class:`~VehicleAttitudePointing`
              - Target pointing attitude parameters.

            * - :py:class:`~VehicleDuration`
              - Look ahead and look behind duration options.

            * - :py:class:`~VehicleStandardBasic`
              - Basic attitude profile.

            * - :py:class:`~VehicleAttitudeExternal`
              - External attitude (.a) file.

            * - :py:class:`~VehicleAttitudeRealTime`
              - Real time attitude.

            * - :py:class:`~VehicleProfileCoordinatedTurn`
              - Coordinated turn attitude profile for aircraft.

            * - :py:class:`~VehicleProfileYawToNadir`
              - A profile useful for satellites with highly elliptical orbits.

            * - :py:class:`~VehicleAttitudeTrendControlAviator`
              - Trending controls for Aviator attitude.

            * - :py:class:`~VehicleProfileAviator`
              - The profile used for Aviator aircraft.

            * - :py:class:`~VehicleTargetPointingElement`
              - Target pointing data for target pointing attitude.

            * - :py:class:`~VehicleTargetPointingCollection`
              - List of Attitude Targets.

            * - :py:class:`~VehicleTorque`
              - Torque file to use in defining integrated attitude.

            * - :py:class:`~VehicleIntegratedAttitude`
              - Integrated Attitude generates an external attitude file for a satellite by numerically integrating Euler's equations for the current satellite.

            * - :py:class:`~VehicleScheduleTimesElement`
              - Parameters for scheduled times for target pointing attitude.

            * - :py:class:`~VehicleTrajectoryAttitudeStandard`
              - Standard attitude profile for launch vehicle or missile.

            * - :py:class:`~VehicleOrbitAttitudeStandard`
              - Standard attitude profile for satellite.

            * - :py:class:`~VehicleRouteAttitudeStandard`
              - Standard attitude profile for aircraft.

            * - :py:class:`~VehicleGraphics2DLine`
              - Line Style and Line Width properties used in displaying vehicle tracks.

            * - :py:class:`~VehicleGraphics2DIntervalsCollection`
              - Custom Intervals Graphics List.

            * - :py:class:`~VehicleGraphics2DAttributesAccess`
              - Vehicle 2D Graphics display based on access intervals.

            * - :py:class:`~VehicleGraphics2DAttributesCustom`
              - Vehicle 2D graphics display based on custom intervals.

            * - :py:class:`~VehicleGraphics2DAttributesRealtime`
              - 2D Graphics attributes for a vehicle based on real time data state.

            * - :py:class:`~VehicleGraphics2DLightingElement`
              - Lighting condition properties.

            * - :py:class:`~VehicleGraphics2DLighting`
              - Lighting.

            * - :py:class:`~VehicleGraphics2DElevationGroundElevation`
              - Ground elevation for vehicle swath.

            * - :py:class:`~VehicleGraphics2DElevationSwathHalfWidth`
              - Half width for vehicle swath.

            * - :py:class:`~VehicleGraphics2DElevationVehicleHalfAngle`
              - Half angle for vehicle swath.

            * - :py:class:`~VehicleGraphics2DSwath`
              - Vehicle swath.

            * - :py:class:`~VehicleGraphics2DLeadDataFraction`
              - 2D Graphics pass: fraction of leading portion of vehicle track to display.

            * - :py:class:`~VehicleGraphics2DLeadDataTime`
              - 2D Graphics pass: time-defined segment of leading portion of vehicle track to display.

            * - :py:class:`~VehicleGraphics2DTrailDataFraction`
              - 2D Graphics pass: fraction of trailing portion of vehicle track to display.

            * - :py:class:`~VehicleGraphics2DTrailDataTime`
              - 2D Graphics pass: time-defined segment of trailing portion of vehicle track to display.

            * - :py:class:`~VehicleGraphics2DRoutePassData`
              - Great arc route pass data.

            * - :py:class:`~VehicleGraphics2DLeadTrailData`
              - 2D Graphics pass properties: lead/trail for ground tracks.

            * - :py:class:`~VehicleGraphics2DOrbitPassData`
              - AgVeGfxPassData Class.

            * - :py:class:`~VehicleGraphics2DTrajectoryPassData`
              - 2D Graphics ground track and trajectory properties.

            * - :py:class:`~VehicleGraphics2DTrajectoryResolution`
              - Ground track and trajectory resolution for launch vehicles and missiles in terms of ephemeris steps.

            * - :py:class:`~VehicleGraphics2DGroundEllipsesCollection`
              - Collection of ground ellipse 2D graphics properties.

            * - :py:class:`~VehicleGraphics2DTimeEventTypeLine`
              - 2D Graphics time event: line type.

            * - :py:class:`~VehicleGraphics2DTimeEventTypeMarker`
              - 2D Graphics time event: marker type.

            * - :py:class:`~VehicleGraphics2DTimeEventTypeText`
              - 2D Graphics time event: text type.

            * - :py:class:`~VehicleGraphics2DTimeEventsElement`
              - 2D Graphics time event.

            * - :py:class:`~VehicleGraphics2DTimeEventsCollection`
              - A satellite's time events collection.

            * - :py:class:`~VehicleGraphics2DPassShowPasses`
              - Beginning and end pass numbers to display.

            * - :py:class:`~VehicleGraphics2DPasses`
              - Settings for satellite pass display graphics.

            * - :py:class:`~VehicleGraphics2DSAA`
              - South Atlantic Anomaly contour settings.

            * - :py:class:`~VehicleGraphics2DElevationsElement`
              - 2D Graphics settings for elevation contours.

            * - :py:class:`~VehicleGraphics2DElevationsCollection`
              - Collection for elevation contours. Used by vehicles.

            * - :py:class:`~VehicleGraphics2DElevContours`
              - General settings regarding display of elevation contours.

            * - :py:class:`~VehicleGraphics2DRouteResolution`
              - Route resolution for great arc vehicles defined in terms of ephemeris steps.

            * - :py:class:`~VehicleGraphics2DWaypointMarkersElement`
              - 2D Graphics properties of element of waypoint collection.

            * - :py:class:`~VehicleGraphics2DWaypointMarkersCollection`
              - A list of 2D definitions for the vehicle way points.

            * - :py:class:`~VehicleGraphics2DWaypointMarker`
              - Display options for waypoint and turn markers in the 2D Graphics window.

            * - :py:class:`~VehicleGraphics2DInterval`
              - 2D Graphics display based on custom intervals.

            * - :py:class:`~VehicleGraphics2DPassResolution`
              - Ground track and orbit resolution for satellites defined in terms of ephemeris steps.

            * - :py:class:`~VehicleGraphics2DGroundEllipsesElement`
              - Ground ellipse 2D graphics properties.

            * - :py:class:`~VehicleGraphics2DAttributesRoute`
              - 2D Graphics attributes for aircraft, ships and ground vehicles.

            * - :py:class:`~VehicleGraphics2DAttributesTrajectory`
              - 2D Graphics attributes for launch vehicles and missiles.

            * - :py:class:`~VehicleGraphics2DAttributesOrbit`
              - 2D Graphics attributes for a satellite.

            * - :py:class:`~Graphics3DPointableElementsElement`
              - Pointable elements for 3D model pointing.

            * - :py:class:`~Graphics3DPointableElementsCollection`
              - List of Pointable Elements.

            * - :py:class:`~VehicleGraphics3DSystemsElement`
              - Element for reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~VehicleGraphics3DSystemsSpecialElement`
              - Define methods and properties to configure 3D properties of Inertial or Fixed reference system used for displaying vehicle orbits and trajectories.

            * - :py:class:`~VehicleGraphics3DSystemsCollection`
              - List of Systems.

            * - :py:class:`~VehicleGraphics3DEllipsoid`
              - Define an ellipsoid around the vehicle object.

            * - :py:class:`~VehicleGraphics3DControlBox`
              - Define a volume around the object that moves with the object.

            * - :py:class:`~VehicleGraphics3DBearingBox`
              - Define a volume, relative to a bearing from the North, around an object.

            * - :py:class:`~VehicleGraphics3DBearingEllipse`
              - Define an ellipse, relative to a bearing from the North, around the object.

            * - :py:class:`~VehicleGraphics3DLineOfBearing`
              - Define a line of bearing which is drawn from an origin in the direction of a bearing.

            * - :py:class:`~VehicleGraphics3DGeoBox`
              - Geostationary box, a fixed plane used to visually check that a GEO satellite stays within a certain area.

            * - :py:class:`~VehicleGraphics3DRouteProximity`
              - Proximity graphics for GreatArc Vehicles.

            * - :py:class:`~VehicleGraphics3DOrbitProximity`
              - Proximity graphics.

            * - :py:class:`~VehicleGraphics3DElevContours`
              - 3D elevation angle contours.

            * - :py:class:`~VehicleGraphics3DSAA`
              - 3D South Atlantic Anomaly contours.

            * - :py:class:`~VehicleGraphics3DSigmaScaleProbability`
              - Sigma probability for indirect sizing of covariance pointing contours.

            * - :py:class:`~VehicleGraphics3DSigmaScaleScale`
              - Sigma scale for direct sizing of covariance pointing contours.

            * - :py:class:`~VehicleGraphics3DDefaultAttributes`
              - Default graphics attributes for covariance pointing contours.

            * - :py:class:`~VehicleGraphics3DIntervalsElement`
              - Intervals graphics for covariance pointing contour.

            * - :py:class:`~VehicleGraphics3DIntervalsCollection`
              - List of Intervals.

            * - :py:class:`~VehicleGraphics3DAttributesBasic`
              - Basic 3D graphics for covariance pointing contours.

            * - :py:class:`~VehicleGraphics3DAttributesIntervals`
              - 3D graphics based on intervals for covariance pointing contours.

            * - :py:class:`~VehicleGraphics3DSize`
              - 3D graphics vector size.

            * - :py:class:`~VehicleGraphics3DCovariancePointingContour`
              - Covariance pointing contours.

            * - :py:class:`~VehicleGraphics3DDataFraction`
              - Fraction for 3D track display.

            * - :py:class:`~VehicleGraphics3DDataTime`
              - Time.

            * - :py:class:`~VehicleGraphics3DOrbitPassData`
              - Satellite 3D ground and orbit track data.

            * - :py:class:`~VehicleGraphics3DOrbitTrackData`
              - 3D leading/trailing track data for satellites.

            * - :py:class:`~VehicleGraphics3DTickDataLine`
              - Line type tick marks.

            * - :py:class:`~VehicleGraphics3DTickDataPoint`
              - Point type tick mark.

            * - :py:class:`~VehicleGraphics3DOrbitTickMarks`
              - Tick mark for satellites.

            * - :py:class:`~VehicleGraphics3DPass`
              - 3D pass for satellites.

            * - :py:class:`~VehicleGraphics3DCovariance`
              - 3D position covariance ellipsoids.

            * - :py:class:`~VehicleGraphics3DVelCovariance`
              - 3D velocity covariance ellipsoids.

            * - :py:class:`~VehicleGraphics3DTrajectoryProximity`
              - AgVeTrajectoryProximity Class.

            * - :py:class:`~VehicleGraphics3DTrajectory`
              - AgLvVOTrajectory Class.

            * - :py:class:`~VehicleGraphics3DTrajectoryTrackData`
              - 3D leading/trailing track data for launch vehicles and missiles.

            * - :py:class:`~VehicleGraphics3DTrajectoryPassData`
              - 3D ground track and trajectory data for a launch vehicle or missile.

            * - :py:class:`~VehicleGraphics3DLeadTrailData`
              - AgLvVOTrajectory2 Class.

            * - :py:class:`~VehicleGraphics3DTrajectoryTickMarks`
              - Tick mark data for launch vehicles and missiles.

            * - :py:class:`~VehicleGraphics3DPathTickMarks`
              - Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

            * - :py:class:`~VehicleGraphics3DWaypointMarkersElement`
              - 3D waypoint.

            * - :py:class:`~VehicleGraphics3DWaypointMarkersCollection`
              - Collection of Waypoint Markers .

            * - :py:class:`~VehicleGraphics3DRoute`
              - AgVeVORoute2 Class.

            * - :py:class:`~Graphics3DModelPointing`
              - List of pointable model elements.

            * - :py:class:`~Graphics3DLabelSwapDistance`
              - Control the level of detail in labels and other screen objects at specified distances.

            * - :py:class:`~VehicleGraphics3DDropLinePositionItem`
              - Drop lines from the vehicle's current position.

            * - :py:class:`~VehicleGraphics3DDropLinePositionItemCollection`
              - Lines dropped from the vehicle's position.

            * - :py:class:`~VehicleGraphics3DDropLinePathItem`
              - Drop lines at intervals along the vehicle's path.

            * - :py:class:`~VehicleGraphics3DDropLinePathItemCollection`
              - Collection of drop lines from the vehicle's orbit or trajectory.

            * - :py:class:`~VehicleGraphics3DOrbitDropLines`
              - Droplines collections.

            * - :py:class:`~VehicleGraphics3DRouteDropLines`
              - Droplines for great arc vehicles.

            * - :py:class:`~VehicleGraphics3DTrajectoryDropLines`
              - Droplines for launch vehicles and missiles.

            * - :py:class:`~VehicleTrajectoryGraphics3DModel`
              - Marker for launch vehicle or missile.

            * - :py:class:`~VehicleRouteGraphics3DModel`
              - 3D marker for great arc vehicles.

            * - :py:class:`~VehicleGraphics3DBPlaneTemplateDisplayElement`
              - Element of IAgVeVOBPlaneTemplateDisplayCollection.

            * - :py:class:`~VehicleGraphics3DBPlaneTemplateDisplayCollection`
              - 3D DisplayElements collection for BPlane.

            * - :py:class:`~VehicleGraphics3DBPlaneTemplate`
              - An element of IAgVeVOBPlaneTemplatesCollection.

            * - :py:class:`~VehicleGraphics3DBPlaneTemplatesCollection`
              - A list of available b-plane templates.

            * - :py:class:`~VehicleGraphics3DBPlaneEvent`
              - 3D BPlane Event.

            * - :py:class:`~VehicleGraphics3DBPlanePoint`
              - 3D BPlane Additional Point.

            * - :py:class:`~VehicleGraphics3DBPlaneTargetPointPositionCartesian`
              - Cartesian.

            * - :py:class:`~VehicleGraphics3DBPlaneTargetPointPositionPolar`
              - 3D BPlane target point position polar.

            * - :py:class:`~VehicleGraphics3DBPlaneTargetPoint`
              - 3D BPlane TargetPoint.

            * - :py:class:`~VehicleGraphics3DBPlaneInstance`
              - An element in the IAgVeVOBPlanePointCollection.

            * - :py:class:`~VehicleGraphics3DBPlaneInstancesCollection`
              - A list of available b-plane instances.

            * - :py:class:`~VehicleGraphics3DBPlanePointCollection`
              - AgVeVOBPlaneCollection Class.

            * - :py:class:`~VehicleGraphics3DBPlanes`
              - 3D BPlanes properties.

            * - :py:class:`~LaunchVehicle`
              - Launch vehicle object.

            * - :py:class:`~LaunchVehicleGraphics`
              - 2D Graphics for a launch vehicle.

            * - :py:class:`~LaunchVehicleGraphics3D`
              - 3D Graphics for a launch vehicle.

            * - :py:class:`~GroundVehicle`
              - Ground vehicle object.

            * - :py:class:`~GroundVehicleGraphics`
              - 2D Graphics properties for ground vehicles.

            * - :py:class:`~GroundVehicleGraphics3D`
              - AgGvVOVO Class.

            * - :py:class:`~Missile`
              - Missile object.

            * - :py:class:`~MissileGraphics`
              - 2D Graphics for missiles.

            * - :py:class:`~MissileGraphics3D`
              - 3D Graphics for missiles.

            * - :py:class:`~Aircraft`
              - Aircraft object.

            * - :py:class:`~AircraftGraphics`
              - 2D Graphics for an aircraft.

            * - :py:class:`~AircraftGraphics3D`
              - 3D Graphics properties for an aircraft.

            * - :py:class:`~Ship`
              - Ship object.

            * - :py:class:`~ShipGraphics`
              - 2D Graphics options for a ship.

            * - :py:class:`~ShipGraphics3D`
              - 3D Graphics attributes for a ship.

            * - :py:class:`~MtoTrackPoint`
              - The points defined for the selected track.

            * - :py:class:`~MtoTrackPointCollection`
              - MTO track point list.

            * - :py:class:`~MtoTrack`
              - List of MTO tracks with basic information about each.

            * - :py:class:`~MtoTrackCollection`
              - MTO Track List.

            * - :py:class:`~MtoDefaultTrack`
              - Default MTO track.

            * - :py:class:`~MtoGlobalTrackOptions`
              - Global MTO track options.

            * - :py:class:`~Mto`
              - Multi-Track Object (MTO).

            * - :py:class:`~MtoGraphics2DMarker`
              - Define the 2D graphics attributes of the selected MTO track or tracks.

            * - :py:class:`~MtoGraphics2DLine`
              - MTO track line display options.

            * - :py:class:`~MtoGraphics2DFadeTimes`
              - MTO track fade times.

            * - :py:class:`~MtoGraphics2DLeadTrailTimes`
              - MTO track lead/trail times.

            * - :py:class:`~MtoGraphics2DTrack`
              - 2D graphics attributes for each track in the MTO.

            * - :py:class:`~MtoGraphics2DTrackCollection`
              - MTO 2D Graphics Track List.

            * - :py:class:`~MtoDefaultGraphics2DTrack`
              - 2D graphics attributes for default MTO tracks.

            * - :py:class:`~MtoGraphics2DGlobalTrackOptions`
              - Global 2D graphics options for an MTO.

            * - :py:class:`~MtoGraphics`
              - MTO 2D Graphics.

            * - :py:class:`~MtoGraphics3DMarker`
              - MTO 3D graphics marker options.

            * - :py:class:`~MtoGraphics3DPoint`
              - MTO track 3D marker point options.

            * - :py:class:`~MtoGraphics3DModel`
              - MTO track model options.

            * - :py:class:`~MtoGraphics3DSwapDistances`
              - MTO track 3D swap distances.

            * - :py:class:`~MtoGraphics3DDropLines`
              - MTO droplines.

            * - :py:class:`~MtoGraphics3DTrack`
              - 3D graphics properties for MTO tracks.

            * - :py:class:`~MtoGraphics3DTrackCollection`
              - MTO 3D Graphics Track List.

            * - :py:class:`~MtoDefaultGraphics3DTrack`
              - 3D graphics properties for default MTO tracks.

            * - :py:class:`~MtoGraphics3DGlobalTrackOptions`
              - Global 3D graphics MTO track options.

            * - :py:class:`~MtoGraphics3D`
              - MTO 3D graphics properties.

            * - :py:class:`~LLAGeocentric`
              - Geocentric LLA position.

            * - :py:class:`~LLAGeodetic`
              - Geodetic LLA position.

            * - :py:class:`~LineTargetPoint`
              - Line Target Point.

            * - :py:class:`~LineTargetPointCollection`
              - The collection of points for the line target.

            * - :py:class:`~LineTarget`
              - Line Target Path properties.

            * - :py:class:`~LineTargetGraphics`
              - The AgLtGraphics class.

            * - :py:class:`~LineTargetGraphics3D`
              - The AgLtVO class.

            * - :py:class:`~CoverageDefinition`
              - The AgCoverageDefinition class.

            * - :py:class:`~CoverageBoundsCustomRegions`
              - Custom Regions.

            * - :py:class:`~CoverageBoundsCustomBoundary`
              - Custom Boundary.

            * - :py:class:`~CoverageBoundsGlobal`
              - Global: grid covering the entire globe.

            * - :py:class:`~CoverageBoundsLat`
              - Latitude Bounds: create a grid between user-specified Minimum and Maximum Latitude boundaries.

            * - :py:class:`~CoverageBoundsLatLine`
              - Latitude Line: Create a set of points along a single latitude line, useful when the coverage is only expected to vary with longitude.

            * - :py:class:`~CoverageBoundsLonLine`
              - Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

            * - :py:class:`~CoverageBoundsLatLonRegion`
              - LatLon Region: create a region between user-specified Minimum and Maximum Latitude and Longitude boundaries.

            * - :py:class:`~CoverageGrid`
              - Grid Definition and resolution.

            * - :py:class:`~CoverageAssetListElement`
              - Coverage asset.

            * - :py:class:`~CoverageAssetListCollection`
              - Asset List.

            * - :py:class:`~CoverageRegionFilesCollection`
              - Collection of Region Files.

            * - :py:class:`~CoverageAreaTargetsCollection`
              - Collection of Area Targets.

            * - :py:class:`~CoveragePointDefinition`
              - Point Definition: methods and parameters for specifying the location of points on the coverage grid.

            * - :py:class:`~CoveragePointFileListCollection`
              - Point file list collection.

            * - :py:class:`~CoverageAdvanced`
              - Advanced Properties.

            * - :py:class:`~CoverageInterval`
              - Coverage interval: the time period over which coverage is computed.

            * - :py:class:`~CoverageResolutionArea`
              - Area: Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~CoverageResolutionDistance`
              - Distance: Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :py:class:`~CoverageResolutionLatLon`
              - Lat/Lon: Determine the location of grid coordinates by specifying a latitude/longitude resolution value.

            * - :py:class:`~CoverageGraphics2DStatic`
              - Static 2D graphics display options for the coverage grid.

            * - :py:class:`~CoverageGraphics2DAnimation`
              - 2D animation graphics options for the coverage grid.

            * - :py:class:`~CoverageGraphics2DProgress`
              - Progress graphics for access calculations.

            * - :py:class:`~CoverageGraphics`
              - 2D graphics display options for the coverage grid.

            * - :py:class:`~CoverageGraphics3D`
              - AgCvVOStatic Class.

            * - :py:class:`~CoverageGraphics3DAttributes`
              - 3D animation or static graphics options.

            * - :py:class:`~ChainTimePeriodBase`
              - Chain time period options.

            * - :py:class:`~ChainUserSpecifiedTimePeriod`
              - User-specified time period for the chain.

            * - :py:class:`~ChainConstraints`
              - Chain constraints.

            * - :py:class:`~Chain`
              - AgChain Class is used to access the methods and properties of the STK Chain Object.

            * - :py:class:`~ChainConnection`
              - Class defining Chain connections.

            * - :py:class:`~ChainConnectionCollection`
              - Class defining a collection of Chain connections.

            * - :py:class:`~ChainOptimalStrandOpts`
              - Class defining Chain optimal strand options.

            * - :py:class:`~ChainGraphics2DStatic`
              - 2D static graphics for a chain.

            * - :py:class:`~ChainGraphics2DAnimation`
              - 2D Animation graphics for a chain.

            * - :py:class:`~ChainGraphics`
              - 2D graphics properties of a chain.

            * - :py:class:`~ChainGraphics3D`
              - 3D graphics properties of a chain.

            * - :py:class:`~RefractionCoefficients`
              - Coefficients for a polynomial in time_since_year_start that models the refraction index.

            * - :py:class:`~RefractionModelEffectiveRadiusMethod`
              - Effective Radius Method.

            * - :py:class:`~RefractionModelITURP8344`
              - ITU-R P.834-4.

            * - :py:class:`~RefractionModelSCFMethod`
              - SCF Method.

            * - :py:class:`~FigureOfMeritDefinitionCompute`
              - Compute options for navigation accuracy.

            * - :py:class:`~FigureOfMeritDefinitionDataMinMax`
              - Minimum and maximum data values for navigation accuracy.

            * - :py:class:`~FigureOfMeritDefinitionDataMinAssets`
              - Minimum number of assets.

            * - :py:class:`~FigureOfMeritDefinitionDataPercentLevel`
              - Specified percent level for the 'percent below' Navigation Accuracy compute option.

            * - :py:class:`~FigureOfMeritDefinitionDataBestN`
              - Navigation accuracy based on best N satellites.

            * - :py:class:`~FigureOfMeritDefinitionDataBest4`
              - Navigation accuracy based on best 4 satellites.

            * - :py:class:`~FigureOfMeritDefinitionAccessConstraint`
              - Access Constraint Figure of Merit.

            * - :py:class:`~FigureOfMeritSatisfaction`
              - Satisfaction properties for a Figure of Merit.

            * - :py:class:`~FigureOfMerit`
              - Figure of Merit properties.

            * - :py:class:`~FigureOfMeritDefinitionAccessSeparation`
              - Access Separation Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionDilutionOfPrecision`
              - Dilution Of Precision Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionNavigationAccuracy`
              - Navigation Accuracy.

            * - :py:class:`~FigureOfMeritAssetListElement`
              - Asset list item (for Navigation Accuracy FOM).

            * - :py:class:`~FigureOfMeritAssetListCollection`
              - List of assets available for specifying range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~FigureOfMeritUncertainties`
              - Receiver range uncertainty (for Navigation Accuracy FOM).

            * - :py:class:`~FigureOfMeritDefinitionResponseTime`
              - Response Time Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionRevisitTime`
              - Revisit Time Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionSimpleCoverage`
              - Simple Coverage Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionTimeAverageGap`
              - Time Average Gap Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionSystemAgeOfData`
              - System Age Of Data Figure of Merit.

            * - :py:class:`~FigureOfMeritGraphics2DContours`
              - Coverage contours.

            * - :py:class:`~FigureOfMeritGraphics2DAttributes`
              - Figure of Merit 2D graphics properties.

            * - :py:class:`~FigureOfMeritGraphics2DContoursAnimation`
              - Animation contour properties.

            * - :py:class:`~FigureOfMeritGraphics2DAttributesAnimation`
              - Animation graphics for a Figure of Merit.

            * - :py:class:`~FigureOfMeritGraphics`
              - AgFmGfxGraphics Class.

            * - :py:class:`~FigureOfMeritGraphics2DRampColor`
              - Color ramp method for contours: select start and end colors to define spectrum segment.

            * - :py:class:`~FigureOfMeritGraphics2DLevelAttributesElement`
              - 2D graphics attributes of contour levels.

            * - :py:class:`~FigureOfMeritGraphics2DLevelAttributesCollection`
              - Collection of Level Attributes.

            * - :py:class:`~FigureOfMeritGraphics2DPositionOnMap`
              - Coordinates of contour legend in pixels on 2D map.

            * - :py:class:`~FigureOfMeritGraphics2DColorOptions`
              - Color options for contour legend.

            * - :py:class:`~FigureOfMeritGraphics2DLegendWindow`
              - Properties of contour legend on 2D map.

            * - :py:class:`~FigureOfMeritGraphics3DLegendWindow`
              - 3D graphics contours legend.

            * - :py:class:`~FigureOfMeritGraphics2DTextOptions`
              - Text display options for contour legend.

            * - :py:class:`~FigureOfMeritGraphics2DRangeColorOptions`
              - Range color options for contour legend.

            * - :py:class:`~FigureOfMeritGraphics2DLegend`
              - Contour legend properties.

            * - :py:class:`~FigureOfMeritNavigationAccuracyMethodElevationAngle`
              - Elevation Angle method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~FigureOfMeritNavigationAccuracyMethodConstant`
              - Constant Value method for uncertainty in range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~FigureOfMeritGraphics3DAttributes`
              - 3D static graphics properties for a Figure of Merit.

            * - :py:class:`~FigureOfMeritGraphics3D`
              - Figure of Merit 3D graphics.

            * - :py:class:`~VehicleProfileGPS`
              - GPS Attitude profile.

            * - :py:class:`~StkObjectModelContext`
              - AgStkObjectModelContext class provides methods to create instance of AgStkObjectRoot class.

            * - :py:class:`~StdMilitary2525bSymbols`
              - AgStdMil2525bSymbols class provides methods to create 2525b symbols.

            * - :py:class:`~CoverageGridInspector`
              - AgCvGridInspector class provides methods to use the grid inspector tool for coverage definition.

            * - :py:class:`~FigureOfMeritGridInspector`
              - AgFmGridInspector class provides methods to use the grid inspector tool for FOM.

            * - :py:class:`~Graphics3DVaporTrail`
              - Vapor trail attributes.

            * - :py:class:`~VehicleTargetPointingIntervalCollection`
              - Represents a collection of scheduled targeting intervals.

            * - :py:class:`~AccessConstraintPluginMinMax`
              - Class related to defining access plugin constraints in terms of minimum and/or maximum values.

            * - :py:class:`~ConstellationConstraints`
              - Class related to the constellation constraints.

            * - :py:class:`~ConstellationConstraintObjectRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~ConstellationConstraintRestriction`
              - Class related to the constellation constraint restrictions.

            * - :py:class:`~Constellation`
              - Class represents the STK Constellation.

            * - :py:class:`~ConstellationGraphics`
              - 2D Graphics properties of the STK Constellation.

            * - :py:class:`~ConstellationRouting`
              - Routing properties of the STK Constellation.

            * - :py:class:`~EventDetectionNoSubSampling`
              - Define event detection strategy that uses samples only (without sub-sampling).

            * - :py:class:`~EventDetectionSubSampling`
              - Event detection strategy involving subsampling.

            * - :py:class:`~SamplingMethodAdaptive`
              - Define an adaptive sampling method.

            * - :py:class:`~SamplingMethodFixedStep`
              - Define a fixed time-step sampling method.

            * - :py:class:`~SensorAccessAdvanced`
              - Sensor's advanced targeting access computation properties.

            * - :py:class:`~VehicleAccessAdvanced`
              - Vehicle advanced targeting access computation properties.

            * - :py:class:`~AccessSampling`
              - Define properties and methods to configure the sampling strategy used in access computations.

            * - :py:class:`~AccessEventDetection`
              - Define properties and methods to configure the event detection strategy used in access computations.

            * - :py:class:`~SensorGraphics3DProjectionElement`
              - Represents elements of the space and target projection collections.

            * - :py:class:`~SensorGraphics3DSpaceProjectionCollection`
              - Time Dependent Space Projection List.

            * - :py:class:`~SensorGraphics3DTargetProjectionCollection`
              - Time Dependent Target Projection List.

            * - :py:class:`~CentralBodyTerrainCollectionElement`
              - Element of collection of terrain associated with central body.

            * - :py:class:`~CentralBodyTerrainCollection`
              - Represents a collection of terrains associated with central bodies. This collection enables adding terrain to any central bodies and not just to the current scenario's central body.

            * - :py:class:`~SatelliteExportTools`
              - The Satellite Export Tools.

            * - :py:class:`~LaunchVehicleExportTools`
              - The LaunchVehicle Export Tools.

            * - :py:class:`~GroundVehicleExportTools`
              - The GroundVehicle Export Tools.

            * - :py:class:`~MissileExportTools`
              - The Missile Export Tools.

            * - :py:class:`~AircraftExportTools`
              - The Aircraft Export Tools.

            * - :py:class:`~ShipExportTools`
              - The Ship Export Tools.

            * - :py:class:`~VehicleEphemerisCode500ExportTool`
              - AgVeEphemerisTypeCode500 Class.

            * - :py:class:`~VehicleEphemerisCCSDSExportTool`
              - AgVeEphemerisTypeCCSDS Class.

            * - :py:class:`~VehicleEphemerisStkExportTool`
              - AgVeEphemerisTypeSTK Class.

            * - :py:class:`~VehicleEphemerisSpiceExportTool`
              - AgVeEphemerisTypeSpice Class.

            * - :py:class:`~ExportToolTimePeriod`
              - Specify Time Period.

            * - :py:class:`~VehicleAttitudeExportTool`
              - AgVeExternalFileAttitude Class.

            * - :py:class:`~VehiclePropDefinitionExportTool`
              - AgVeExternalFileAttitude Class.

            * - :py:class:`~VehicleCoordinateAxesCustom`
              - Custom.

            * - :py:class:`~ExportToolStepSize`
              - AgStepSize Class.

            * - :py:class:`~PctCmpltEventArgs`
              - Represents a structure used by the Percent Complete events.

            * - :py:class:`~StkObjectChangedEventArgs`
              - Contains information about the changes in the object's state.

            * - :py:class:`~VehicleEclipsingBodies`
              - Eclipsing bodies.

            * - :py:class:`~LocationVectorGeometryToolPoint`
              - The location based upon a Vector Geometry Tool Point.

            * - :py:class:`~TimePeriod`
              - Provide methods and properties to configure start and stop times.

            * - :py:class:`~TimePeriodValue`
              - Provide methods and properties to configure a time value.

            * - :py:class:`~SpatialState`
              - Represents a position and an attitude of an object.

            * - :py:class:`~VehicleSpatialInfo`
              - Represents a spatial information of the vehicle.

            * - :py:class:`~OnePointAccess`
              - One Point Access.

            * - :py:class:`~OnePointAccessResultCollection`
              - Represents the data sets for one point access.

            * - :py:class:`~OnePointAccessResult`
              - One Point Access Result.

            * - :py:class:`~OnePointAccessConstraintCollection`
              - Represents the access constraints for the one point access computation.

            * - :py:class:`~OnePointAccessConstraint`
              - One Point Access Result.

            * - :py:class:`~VehiclePropagatorRealtime`
              - Realtime propagator.

            * - :py:class:`~VehicleRealtimePointBuilder`
              - Allow the user to create vehicle's ephemeris by appending ephemeris points.

            * - :py:class:`~VehicleRealtimeCartesianPoints`
              - AgVeRealtimeCartesianPoint Class.

            * - :py:class:`~VehicleRealtimeLLAHPSPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~VehicleRealtimeLLAPoints`
              - Add one ephemeris point using latitude/longitude/altitude coordinate system.

            * - :py:class:`~VehicleRealtimeUTMPoints`
              - Add one ephemeris point.

            * - :py:class:`~SRPModelGPS`
              - GPS Solar Radiation Pressure Model.

            * - :py:class:`~SRPModelSpherical`
              - Spherical Solar Radiation Pressure Model.

            * - :py:class:`~SRPModelPlugin`
              - Plugin Light Reflection Model.

            * - :py:class:`~SRPModelPluginSettings`
              - Plugin Light Reflection Model Settings.

            * - :py:class:`~VehicleHPOPSRPModel`
              - SRP Model Base CoClass.

            * - :py:class:`~VehicleHPOPDragModelSpherical`
              - Spherical Drag Pressure Model.

            * - :py:class:`~VehicleHPOPDragModelPlugin`
              - Plugin Drag Model.

            * - :py:class:`~VehicleHPOPDragModelPluginSettings`
              - Plugin Drag Model Settings.

            * - :py:class:`~VehicleHPOPDragModel`
              - HPOP Drag Model Base CoClass.

            * - :py:class:`~ScenarioAnimationTimePeriod`
              - Configure the scenario's animation time.

            * - :py:class:`~SensorProjectionConstantAltitude`
              - Class defining projection altitude options for constant altitude for a sensor.

            * - :py:class:`~SensorProjectionObjectAltitude`
              - Class defining projection altitude options for object altitude for a sensor.

            * - :py:class:`~VehicleAttitudeRealTimeDataReference`
              - Reference attitude profile for the incoming attitude data.

            * - :py:class:`~MtoAnalysis`
              - MTO Spatial State Info.

            * - :py:class:`~MtoAnalysisPosition`
              - MTO Position Computation.

            * - :py:class:`~MtoAnalysisRange`
              - MTO Range Computation.

            * - :py:class:`~MtoAnalysisFieldOfView`
              - MTO Field Of View Computation.

            * - :py:class:`~MtoAnalysisVisibility`
              - MTO Visibility Computation.

            * - :py:class:`~VehiclePropagatorGPS`
              - GPS propagator.

            * - :py:class:`~AvailableFeatures`
              - Class is used to check the availability of the features such as Astrogator, etc.

            * - :py:class:`~ScenarioBeforeSaveEventArgs`
              - Contains information about the changes in the object's state.

            * - :py:class:`~StkObjectPreDeleteEventArgs`
              - Arguments for the OnStkObjectPreDelete event.

            * - :py:class:`~VehiclePropagatorSGP4CommonTasks`
              - Most commonly used functionality when working with SGP4 propagator.

            * - :py:class:`~VehicleSGP4AutoUpdateProperties`
              - SGP4 AutoUpdate properties.

            * - :py:class:`~VehicleSGP4AutoUpdateFileSource`
              - Configure the SGP4 automatic updates using file(s).

            * - :py:class:`~VehicleSGP4AutoUpdateOnlineSource`
              - Configure the SGP4 automatic updates using online source (AGI server).

            * - :py:class:`~VehicleSGP4AutoUpdate`
              - SGP4 AutoUpdate.

            * - :py:class:`~VehicleSGP4PropagatorSettings`
              - Encapsulates the SGP4 propagator settings.

            * - :py:class:`~VehicleGPSAutoUpdateProperties`
              - GPS AutoUpdate properties.

            * - :py:class:`~VehicleGPSAutoUpdateFileSource`
              - GPS automatic updates using almanac file(s).

            * - :py:class:`~VehicleGPSAutoUpdateOnlineSource`
              - GPS automatic updates using online source (AGI server).

            * - :py:class:`~VehicleGPSAutoUpdate`
              - GPS AutoUpdate.

            * - :py:class:`~VehicleGPSSpecifyAlmanac`
              - Specify a GPS almanac.

            * - :py:class:`~VehicleGPSAlmanacProperties`
              - A common base for GPS almanac properties.

            * - :py:class:`~VehicleGPSAlmanacPropertiesSEM`
              - SEM almanac properties.

            * - :py:class:`~VehicleGPSAlmanacPropertiesYUMA`
              - YUMA almanac properties.

            * - :py:class:`~VehicleGPSAlmanacPropertiesSP3`
              - SP3 almanac properties.

            * - :py:class:`~VehicleGPSElementCollection`
              - A collection of GPS elements.

            * - :py:class:`~VehicleGPSElement`
              - An element of the GPS element collection.

            * - :py:class:`~SpaceEnvironmentRadEnergyMethodSpecify`
              - Set the electron and proton energies to consider.

            * - :py:class:`~SpaceEnvironmentRadEnergyValues`
              - Energy values used by the Radiation Environment model.

            * - :py:class:`~SpaceEnvironmentRadiationEnvironment`
              - Radiation Environment model settings.

            * - :py:class:`~SpaceEnvironmentMagnitudeFieldGraphics2D`
              - Geomagnetic field graphics settings.

            * - :py:class:`~SpaceEnvironmentScenarioExtGraphics3D`
              - 3D Graphics settings.

            * - :py:class:`~ScenSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~VehicleSpaceEnvironmentRadDoseRateElement`
              - Class defining dose rate information computed for a shielding thickness.

            * - :py:class:`~VehicleSpaceEnvironmentRadDoseRateCollection`
              - Collection of dose rate elements computed for a shielding thickness.

            * - :py:class:`~SpaceEnvironmentSAAContour`
              - SAA settings.

            * - :py:class:`~VehicleSpaceEnvironmentVehTemperature`
              - Vehicle Temperature settings.

            * - :py:class:`~VehicleSpaceEnvironmentParticleFlux`
              - Particle Flux settings.

            * - :py:class:`~VehicleSpaceEnvironmentMagneticField`
              - Magnetic field settings.

            * - :py:class:`~VehicleSpaceEnvironmentRadiation`
              - Radiation model settings.

            * - :py:class:`~VehicleSpaceEnvironmentMagnitudeFieldLine`
              - Graphics settings for displaying magnetic field lines.

            * - :py:class:`~VehicleSpaceEnvironmentGraphics`
              - Graphics settings.

            * - :py:class:`~VehicleSpaceEnvironment`
              - SpaceEnvironment settings.

            * - :py:class:`~CoverageSelectedGridPoint`
              - Represents a point selected with the grid inspector.

            * - :py:class:`~CoverageGridPointSelection`
              - Represents a set of points selected with the grid inspector.

            * - :py:class:`~CelestialBodyCollection`
              - Represents a collection of stars.

            * - :py:class:`~CelestialBodyInfo`
              - Represents a celestial body information.

            * - :py:class:`~StkCentralBodyEllipsoid`
              - Central body's ellipsoid information.

            * - :py:class:`~StkCentralBody`
              - A central body coclass.

            * - :py:class:`~StkCentralBodyCollection`
              - Central body collection coclass.

            * - :py:class:`~FigureOfMeritDefinitionSystemResponseTime`
              - System Response Time Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionAgeOfData`
              - Age of Data Figure of Merit.

            * - :py:class:`~FigureOfMeritDefinitionScalarCalculation`
              - Scalar Calculation Figure of Merit.

            * - :py:class:`~VehiclePropagator11ParamDescriptor`
              - 11-Param file definition.

            * - :py:class:`~VehiclePropagator11ParamDescriptorCollection`
              - A collection of 11-Parameter files.

            * - :py:class:`~VehiclePropagator11Param`
              - The 11-Parameter propagator models geostationary satellites using 11-Parameter files. The propagator uses an algorithm documented in Intelsat Earth Station Standards (IESS) IESS-412 (Rev. 2), available at www.celestrak.com.

            * - :py:class:`~VehiclePropagatorSP3File`
              - SP3 file data.

            * - :py:class:`~VehiclePropagatorSP3FileCollection`
              - A collection of SP3 files.

            * - :py:class:`~VehiclePropagatorSP3`
              - The SP3 propagator reads .sp3 files of type 'a' and 'c' and allows you to use multiple files in sequence. These files are used to provide precise GPS orbits from the National Geodetic Survey (NGS).

            * - :py:class:`~VehicleEphemerisStkBinaryExportTool`
              - AgVeEphemerisTypeSTKBinary Class.

            * - :py:class:`~OrbitState`
              - Class defining orbit state.

            * - :py:class:`~OrbitStateCoordinateSystem`
              - Selection of coordinate epoch for coordinate systems that do not have pre-established epochs.

            * - :py:class:`~OrbitStateCartesian`
              - Cartesian coordinate type.

            * - :py:class:`~ClassicalSizeShapeAltitude`
              - Orbit size and shape using altitude.

            * - :py:class:`~ClassicalSizeShapeMeanMotion`
              - Orbit size and shape using Mean Motion and Eccentricity.

            * - :py:class:`~ClassicalSizeShapePeriod`
              - Orbit size and shape using Period and Eccentricity.

            * - :py:class:`~ClassicalSizeShapeRadius`
              - Orbit size and shape using Radius.

            * - :py:class:`~ClassicalSizeShapeSemimajorAxis`
              - Orbit size and shape using Semimajor Axis and Eccentricity.

            * - :py:class:`~OrientationAscNodeLAN`
              - Earth-fixed longitude where the satellite crosses the inertial equator from south to north.

            * - :py:class:`~OrientationAscNodeRAAN`
              - Angle from the inertial X axis to the ascending node measured in a right-handed sense about the inertial Z axis in the equatorial plane.

            * - :py:class:`~ClassicalOrientation`
              - Orbit orientation in the Classical (Keplerian) system.

            * - :py:class:`~ClassicalLocationArgumentOfLatitude`
              - Argument of Latitude, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ClassicalLocationEccentricAnomaly`
              - Eccentric Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ClassicalLocationMeanAnomaly`
              - Mean Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ClassicalLocationTimePastAN`
              - Time Past Ascending Node, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ClassicalLocationTimePastPerigee`
              - Time Past Perigee, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ClassicalLocationTrueAnomaly`
              - True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

            * - :py:class:`~OrbitStateClassical`
              - Classical (Keplerian) coordinate type.

            * - :py:class:`~GeodeticSizeAltitude`
              - Altitude and Altitude Rate (for Geodetic coordinate type).

            * - :py:class:`~GeodeticSizeRadius`
              - Radius and Radius Rate (for Geodetic coordinate type).

            * - :py:class:`~OrbitStateGeodetic`
              - Geodetic coordinate type (available only with a Fixed coordinate system).

            * - :py:class:`~DelaunayL`
              - Delaunay Variable L, which is related to the two-body orbital energy.

            * - :py:class:`~DelaunayLOverSQRTmu`
              - Delaunay Variable L/SQRT(mu), i.e. L divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~DelaunayH`
              - Value of Delaunay Variable H, which is the Z component of the orbital angular momentum.

            * - :py:class:`~DelaunayHOverSQRTmu`
              - Delaunay Variable H/SQRT(mu), i.e. H divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~DelaunayG`
              - Delaunay Variable G, the magnitude of the orbital angular momentum.

            * - :py:class:`~DelaunayGOverSQRTmu`
              - Delaunay Variable G/SQRT(mu), i.e. G divided the square root of the central-body gravitational constant, yielding a geometric version of the Delaunay set that is independent of the central body.

            * - :py:class:`~OrbitStateDelaunay`
              - Delaunay coordinate type, using a set of canonical action-angle variables, which are commonly used in general perturbation theories.

            * - :py:class:`~EquinoctialSizeShapeMeanMotion`
              - Mean Motion, an element of the Equinoctial coordinate type.

            * - :py:class:`~EquinoctialSizeShapeSemimajorAxis`
              - Semimajor Axis, an element of the Equinoctial coordinate type.

            * - :py:class:`~OrbitStateEquinoctial`
              - Equinoctial coordinate type, which uses the center of the Earth as the origin and the plane of the satellite's orbit as the reference plane.

            * - :py:class:`~MixedSphericalFPAHorizontal`
              - Horizontal Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~MixedSphericalFPAVertical`
              - Vertical Flight Path Angle, an element of the Mixed Spherical coordinate type.

            * - :py:class:`~OrbitStateMixedSpherical`
              - Mixed Spherical coordinate type, using a variation of the spherical elements that combines Earth-fixed position parameters with inertial velocity parameters.

            * - :py:class:`~SphericalFPAHorizontal`
              - Horizontal Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~SphericalFPAVertical`
              - Vertical Flight Path Angle, an element of the Spherical coordinate type.

            * - :py:class:`~OrbitStateSpherical`
              - Spherical coordinate type: defines the path of an orbit using polar coordinates.

            * - :py:class:`~VehicleGraphics2DTimeComponentsEventElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with all types of event components except for the event interval collections.

            * - :py:class:`~VehicleGraphics2DTimeComponentsEventCollectionElement`
              - Provide properties to configure the vehicle's appearance in 2D and 3D views. The interface is used with event interval collections only.

            * - :py:class:`~VehicleGraphics2DTimeComponentsCollection`
              - A collection of time components used to configure the object appearance in 2D and 3D views.

            * - :py:class:`~VehicleGraphics2DAttributesTimeComponents`
              - Allow configuring the 2D attributes using the time components.

            * - :py:class:`~StkPreferences`
              - Allow configuring STK preferences.

            * - :py:class:`~StkPreferencesVDF`
              - Allow configuring VDF preferences.

            * - :py:class:`~VehicleAttitudeMaximumSlewRate`
              - Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~VehicleAttitudeMaximumSlewAcceleration`
              - Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

            * - :py:class:`~VehicleAttitudeSlewConstrained`
              - Constrained slew mode.

            * - :py:class:`~VehicleAttitudeSlewFixedRate`
              - Fixed rate slew.

            * - :py:class:`~VehicleAttitudeSlewFixedTime`
              - Fixed time slew.

            * - :py:class:`~VehicleAttitudeTargetSlew`
              - Define the time required for a vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.

            * - :py:class:`~MtoGraphics3DModelArtic`
              - Class defining MTO model articulations.

            * - :py:class:`~VehiclePropagatorAviator`
              - Class defining the Mission Modler propagator for an Aircraft.

            * - :py:class:`~VehicleEphemerisCCSDSv2ExportTool`
              - The Ephemeris/Attitude Export Tool for CCSDSv2 Ephemeris type.

            * - :py:class:`~StkPreferencesConnect`
              - Allow configuring connect preferences.

            * - :py:class:`~Antenna`
              - Class defining the antenna object.

            * - :py:class:`~AntennaModel`
              - Class defining a generic antenna model.

            * - :py:class:`~AntennaModelOpticalSimple`
              - Class defining a simple optical antenna model.

            * - :py:class:`~AntennaModelOpticalGaussian`
              - Class defining a gaussian optical antenna model.

            * - :py:class:`~AntennaModelGaussian`
              - Class defining a gaussian antenna model.

            * - :py:class:`~AntennaModelParabolic`
              - Class defining a parabolic antenna model.

            * - :py:class:`~AntennaModelSquareHorn`
              - Class defining a square horn antenna model.

            * - :py:class:`~AntennaModelScriptPlugin`
              - Class defining a script plguin antenna model.

            * - :py:class:`~AntennaModelExternal`
              - Class defining a external antenna model.

            * - :py:class:`~AntennaModelGimroc`
              - Class defining a GIMROC antenna model.

            * - :py:class:`~AntennaModelRemcomUanFormat`
              - Class defining an antenna pattern Remcom uan model.

            * - :py:class:`~AntennaModelANSYSffdFormat`
              - Class defining an antenna pattern ANSYS ffd model.

            * - :py:class:`~AntennaModelTicraGRASPFormat`
              - Class defining an antenna pattern Ticra GRASP model.

            * - :py:class:`~AntennaModelElevationAzimuthCuts`
              - Class defining a pattern elevation/azimuth cuts antenna model.

            * - :py:class:`~AntennaModelIeee1979`
              - Class defining a IEEE 1979 antenna model.

            * - :py:class:`~AntennaModelDipole`
              - Class defining a dipole antenna model.

            * - :py:class:`~AntennaModelHelix`
              - Class defining a helix antenna model.

            * - :py:class:`~AntennaModelCosecantSquared`
              - Class defining a cosecant squared antenna model.

            * - :py:class:`~AntennaModelHemispherical`
              - Class defining a hemispherical antenna model.

            * - :py:class:`~AntennaModelPencilBeam`
              - Class defining a pencil beam antenna model.

            * - :py:class:`~AntennaModelPhasedArray`
              - Class defining a phased array antenna model.

            * - :py:class:`~AntennaModelHfssEepArray`
              - Class defining an HFSS EEP array antenna model.

            * - :py:class:`~AntennaModelIsotropic`
              - Class defining a isotropic antenna model.

            * - :py:class:`~AntennaModelIntelSat`
              - Class defining a IntelSat antenna model.

            * - :py:class:`~AntennaModelGpsGlobal`
              - Class defining a GPS global antenna model.

            * - :py:class:`~AntennaModelGpsFrpa`
              - Class defining a GPS FRPA antenna model.

            * - :py:class:`~AntennaModelItuBO1213CoPolar`
              - Class defining a ITU-R BO1213 co-polar antenna model.

            * - :py:class:`~AntennaModelItuBO1213CrossPolar`
              - Class defining a ITU-R BO1213 cross-polar antenna model.

            * - :py:class:`~AntennaModelItuF1245`
              - Class defining a ITU-R F1245-3 antenna model.

            * - :py:class:`~AntennaModelItuS580`
              - Class defining a ITU-R S580-6 antenna model.

            * - :py:class:`~AntennaModelItuS465`
              - Class defining a ITU-R S465-6 antenna model.

            * - :py:class:`~AntennaModelItuS731`
              - Class defining a ITU-R S731 antenna model.

            * - :py:class:`~AntennaModelItuS1528R12Circular`
              - Class defining a ITU-R S1528 1.2 circular antenna model.

            * - :py:class:`~AntennaModelItuS1528R13`
              - Class defining a ITU-R S1528 1.3 antenna model.

            * - :py:class:`~AntennaModelItuS672Circular`
              - Class defining a ITU-R S672 circular antenna model.

            * - :py:class:`~AntennaModelItuS1528R12Rectangular`
              - Class defining a ITU-R S1528 1.2 rectangular antenna model.

            * - :py:class:`~AntennaModelItuS672Rectangular`
              - Class defining a ITU-R S672-4 rectangular antenna model.

            * - :py:class:`~AntennaModelApertureCircularCosine`
              - Class defining a circular cosine aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularUniform`
              - Class defining a circular uniform aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularCosineSquared`
              - Class defining a circular cosine squared aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularBessel`
              - Class defining a circular bessel aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularBesselEnvelope`
              - Class defining a circular bessel envelope aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularCosinePedestal`
              - Class defining a circular cosine pedestal aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularCosineSquaredPedestal`
              - Class defining a circular cosine squared pedestal aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularSincIntPower`
              - Class defining a circular sinc integer power aperture antenna model.

            * - :py:class:`~AntennaModelApertureCircularSincRealPower`
              - Class defining a circular sinc real power aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularCosine`
              - Class defining a rectangular cosine aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularCosinePedestal`
              - Class defining a rectangular cosine pedestal aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularCosineSquaredPedestal`
              - Class defining a rectangular cosine squared pedestal aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularSincIntPower`
              - Class defining a rectangular sinc integer power aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularSincRealPower`
              - Class defining a rectangular sinc real power aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularCosineSquared`
              - Class defining a rectangular cosine squared aperture antenna model.

            * - :py:class:`~AntennaModelApertureRectangularUniform`
              - Class defining a rectangular uniform aperture antenna model.

            * - :py:class:`~AntennaModelRectangularPattern`
              - Class defining a rectangular pattern antenna model.

            * - :py:class:`~AntennaControl`
              - Class defining the properties for a antenna control.

            * - :py:class:`~AntennaGraphics3D`
              - Class defining 3D Graphics properties of a Antenna.

            * - :py:class:`~RadarCrossSectionVolumeGraphics`
              - Class defining 3D Volume Graphics properties of radar cross section.

            * - :py:class:`~RadarCrossSectionGraphics3D`
              - Class defining 3D Graphics properties of radar cross section.

            * - :py:class:`~RadarCrossSectionGraphics`
              - Class defining graphics properties of radar cross section.

            * - :py:class:`~AntennaVolumeGraphics`
              - Class defining 3D Volume Graphics properties of a Antenna.

            * - :py:class:`~AntennaContourGraphics`
              - Class defining contour Graphics properties of a Antenna.

            * - :py:class:`~AntennaGraphics`
              - Class defining 2D Graphics properties of a Antenna.

            * - :py:class:`~RadarCrossSectionContourLevelCollection`
              - Class defining a collection of radar cross section contour levels.

            * - :py:class:`~RadarCrossSectionContourLevel`
              - Class defining an radar cross section contour level.

            * - :py:class:`~RadarCrossSectionVolumeLevelCollection`
              - Class defining a collection of radar cross section volume levels.

            * - :py:class:`~RadarCrossSectionVolumeLevel`
              - Class defining an radar cross section volume level.

            * - :py:class:`~AntennaVolumeLevelCollection`
              - Class defining a collection of antenna volume levels.

            * - :py:class:`~AntennaVolumeLevel`
              - Class defining an antenna volume level.

            * - :py:class:`~AntennaContourLevelCollection`
              - Class defining a collection of antenna contour levels.

            * - :py:class:`~AntennaContourLevel`
              - Class defining an antenna contour level.

            * - :py:class:`~AntennaContourGain`
              - Class defining an antenna gain contour properties.

            * - :py:class:`~AntennaContourEirp`
              - Class defining an antenna eirp contour properties.

            * - :py:class:`~AntennaContourRip`
              - Class defining an antenna rip contour properties.

            * - :py:class:`~AntennaContourFluxDensity`
              - Class defining an antenna flux density contour properties.

            * - :py:class:`~AntennaContourSpectralFluxDensity`
              - Class defining an antenna spectral flux density contour properties.

            * - :py:class:`~Transmitter`
              - Class defining the transmitter object.

            * - :py:class:`~TransmitterModel`
              - Class defining a generic transmitter model.

            * - :py:class:`~TransmitterModelScriptPluginRF`
              - Class defining a RF script plugin transmitter model.

            * - :py:class:`~TransmitterModelScriptPluginLaser`
              - Class defining a laser script plugin transmitter model.

            * - :py:class:`~TransmitterModelCable`
              - Class defining a cable transmitter model.

            * - :py:class:`~TransmitterModelSimple`
              - Class defining a simple transmitter model.

            * - :py:class:`~TransmitterModelMedium`
              - Class defining a medium transmitter model.

            * - :py:class:`~TransmitterModelComplex`
              - Class defining a complex transmitter model.

            * - :py:class:`~TransmitterModelMultibeam`
              - Class defining a multibeam transmitter model.

            * - :py:class:`~TransmitterModelLaser`
              - Class defining a laser transmitter model.

            * - :py:class:`~ReTransmitterModelSimple`
              - Class defining a simple re-transmitter model.

            * - :py:class:`~ReTransmitterModelMedium`
              - Class defining a medium re-transmitter model.

            * - :py:class:`~ReTransmitterModelComplex`
              - Class defining a complex re-transmitter model.

            * - :py:class:`~TransmitterGraphics3D`
              - Class defining 3D Graphics properties of a Transmitter.

            * - :py:class:`~TransmitterGraphics`
              - Class defining 2D Graphics properties of a Transmitter.

            * - :py:class:`~Receiver`
              - Class defining the receiver object.

            * - :py:class:`~ReceiverModel`
              - Class defining a generic receiver model.

            * - :py:class:`~ReceiverModelCable`
              - Class defining a cable receiver model.

            * - :py:class:`~ReceiverModelSimple`
              - Class defining a simple receiver model.

            * - :py:class:`~ReceiverModelMedium`
              - Class defining a medium receiver model.

            * - :py:class:`~ReceiverModelComplex`
              - Class defining a complex receiver model.

            * - :py:class:`~ReceiverModelMultibeam`
              - Class defining a mutibeam receiver model.

            * - :py:class:`~ReceiverModelLaser`
              - Class defining a laser receiver model.

            * - :py:class:`~ReceiverModelScriptPluginRF`
              - Class defining a RF script plugin receiver model.

            * - :py:class:`~ReceiverModelScriptPluginLaser`
              - Class defining a laser script plugin receiver model.

            * - :py:class:`~ReceiverGraphics3D`
              - Class defining 3D Graphics properties of a Receiver.

            * - :py:class:`~ReceiverGraphics`
              - Class defining 2D Graphics properties of a Receiver.

            * - :py:class:`~RadarDopplerClutterFilters`
              - Class defining the properties for doppler clutter filters.

            * - :py:class:`~Waveform`
              - Class defining a waveform.

            * - :py:class:`~WaveformRectangular`
              - Class defining a rectangular waveform.

            * - :py:class:`~WaveformPulseDefinition`
              - Class defining the pulse definition for a rectangular waveform.

            * - :py:class:`~RadarMultifunctionWaveformStrategySettings`
              - Class defining the waveform selection strategy settings.

            * - :py:class:`~WaveformSelectionStrategy`
              - Class defining the waveform selection strategy.

            * - :py:class:`~WaveformSelectionStrategyFixed`
              - Class defining the waveform selection strategy.

            * - :py:class:`~WaveformSelectionStrategyRangeLimits`
              - Class defining the range limits waveform selection strategy.

            * - :py:class:`~Radar`
              - Class defining the radar object.

            * - :py:class:`~RadarModel`
              - Class defining a generic radar model.

            * - :py:class:`~RadarModelMonostatic`
              - Class defining a monostatic radar model.

            * - :py:class:`~RadarModelMultifunction`
              - Class defining a multifunction radar model.

            * - :py:class:`~RadarModelBistaticTransmitter`
              - Class defining a bistatic transmitter radar model.

            * - :py:class:`~RadarModelBistaticReceiver`
              - Class defining a bistatic receiver radar model.

            * - :py:class:`~RadarGraphics3D`
              - Class defining 3D Graphics properties of a Radar.

            * - :py:class:`~RadarGraphics`
              - Class defining 2D Graphics properties of a Radar.

            * - :py:class:`~RadarAccessGraphics`
              - Class defining access graphics properties of a Radar.

            * - :py:class:`~RadarMultipathGraphics`
              - Class defining multipath graphics properties of a Radar.

            * - :py:class:`~RadarModeMonostatic`
              - Class defining a monostatic radar mode.

            * - :py:class:`~RadarModeMonostaticSearchTrack`
              - Class defining a monostatic search/track radar mode.

            * - :py:class:`~RadarModeMonostaticSar`
              - Class defining a monostatic sar radar mode.

            * - :py:class:`~RadarModeBistaticTransmitter`
              - Class defining a bistatic transmitter radar mode.

            * - :py:class:`~RadarModeBistaticTransmitterSearchTrack`
              - Class defining a bistatic transmitter search/track radar mode.

            * - :py:class:`~RadarModeBistaticTransmitterSar`
              - Class defining a bistatic transmitter sar radar mode.

            * - :py:class:`~RadarModeBistaticReceiver`
              - Class defining a bistatic receiver radar mode.

            * - :py:class:`~RadarModeBistaticReceiverSearchTrack`
              - Class defining a bistatic receiver search/track radar mode.

            * - :py:class:`~RadarModeBistaticReceiverSar`
              - Class defining a bistatic receiver sar radar mode.

            * - :py:class:`~RadarWaveformMonostaticSearchTrackContinuous`
              - Class defining a monostatic continuous waveform.

            * - :py:class:`~RadarWaveformMonostaticSearchTrackFixedPRF`
              - Class defining a monostatic fixed PRF waveform.

            * - :py:class:`~RadarMultifunctionDetectionProcessing`
              - Class defining multifunction radar detection processing.

            * - :py:class:`~RadarWaveformBistaticTransmitterSearchTrackContinuous`
              - Class defining a bistatic transmitter continuous waveform.

            * - :py:class:`~RadarWaveformBistaticTransmitterSearchTrackFixedPRF`
              - Class defining a bistatic transmitter fixed PRF waveform.

            * - :py:class:`~RadarWaveformBistaticReceiverSearchTrackContinuous`
              - Class defining a bistatic receiver continuous waveform.

            * - :py:class:`~RadarWaveformBistaticReceiverSearchTrackFixedPRF`
              - Class defining a bistatic receiver fixed PRF waveform.

            * - :py:class:`~RadarWaveformSearchTrackPulseDefinition`
              - Class defining the pulse definition for a search track waveform.

            * - :py:class:`~RadarModulator`
              - Class defining a radar modulator.

            * - :py:class:`~RadarProbabilityOfDetection`
              - Class defining the probability of detection.

            * - :py:class:`~RadarProbabilityOfDetectionCFAR`
              - Class defining the probability of detection cfar.

            * - :py:class:`~RadarProbabilityOfDetectionNonCFAR`
              - Class defining the non CFAR probability of detection cfar.

            * - :py:class:`~RadarProbabilityOfDetectionPlugin`
              - Class defining the probability of detection plugin.

            * - :py:class:`~RadarProbabilityOfDetectionCFARCellAveraging`
              - Class defining the probability of detection cell averaging cfar.

            * - :py:class:`~RadarProbabilityOfDetectionCFAROrderedStatistics`
              - Class defining the probability of detection ordered statistics cfar.

            * - :py:class:`~RadarPulseIntegrationGoalSNR`
              - Class defining the goal SNR integration method.

            * - :py:class:`~RadarPulseIntegrationFixedNumberOfPulses`
              - Class defining the fixed number of pulses integration method.

            * - :py:class:`~RadarContinuousWaveAnalysisModeGoalSNR`
              - Class defining the continuous wave goal SNR analysis mode.

            * - :py:class:`~RadarContinuousWaveAnalysisModeFixedTime`
              - Class defining the continuous wave fixed time analysis mode.

            * - :py:class:`~RadarWaveformSarPulseDefinition`
              - Class defining the pulse definition for a SAR waveform.

            * - :py:class:`~RadarWaveformSarPulseIntegration`
              - Class defining the pulse integration for a SAR waveform.

            * - :py:class:`~RadarTransmitter`
              - Class defining the radar transmitter.

            * - :py:class:`~RadarTransmitterMultifunction`
              - Class defining the multifunction radar transmitter.

            * - :py:class:`~RadarReceiver`
              - Class defining the radar transmitter.

            * - :py:class:`~AdditionalGainLoss`
              - Class defining additional gains and losses.

            * - :py:class:`~AdditionalGainLossCollection`
              - Class defining a collection of additional gains and losses.

            * - :py:class:`~Polarization`
              - Class defining an polarization.

            * - :py:class:`~PolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~ReceivePolarizationElliptical`
              - Class defining an elliptical polarization.

            * - :py:class:`~PolarizationLHC`
              - Class defining a LHC polarization.

            * - :py:class:`~PolarizationRHC`
              - Class defining a RHC polarization.

            * - :py:class:`~ReceivePolarizationLHC`
              - Class defining a LHC polarization.

            * - :py:class:`~ReceivePolarizationRHC`
              - Class defining a RHC polarization.

            * - :py:class:`~PolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~ReceivePolarizationLinear`
              - Class defining a linear polarization.

            * - :py:class:`~PolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~ReceivePolarizationHorizontal`
              - Class defining a horizontal polarization.

            * - :py:class:`~PolarizationVertical`
              - Class defining a vertical polarization.

            * - :py:class:`~ReceivePolarizationVertical`
              - Class defining a receive vertical polarization.

            * - :py:class:`~RadarClutter`
              - Class defining a radar clutter.

            * - :py:class:`~RadarClutterGeometry`
              - Class defining a radar clutter geometry.

            * - :py:class:`~ScatteringPointProviderCollectionElement`
              - Class defining a scattering point provider collection element.

            * - :py:class:`~ScatteringPointProviderCollection`
              - Class defining an scattering point provider collection.

            * - :py:class:`~ScatteringPointProviderList`
              - Class defining a scattering point provider list.

            * - :py:class:`~ScatteringPointProvider`
              - Class defining a scattering point provider.

            * - :py:class:`~ScatteringPointProviderSinglePoint`
              - Class defining a single point scattring point provider.

            * - :py:class:`~ScatteringPointCollectionElement`
              - Class defining a scattering point collection element.

            * - :py:class:`~ScatteringPointCollection`
              - Class defining a collection of scattering points.

            * - :py:class:`~ScatteringPointProviderPointsFile`
              - Class defining a scattring point provider where the points are defined in an ascii text file.

            * - :py:class:`~ScatteringPointProviderRangeOverCFARCells`
              - Class defining a range over CFAR cells scattering point provider.

            * - :py:class:`~ScatteringPointProviderSmoothOblateEarth`
              - Class defining a smooth oblate earth scattering point provider.

            * - :py:class:`~ScatteringPointProviderPlugin`
              - Class defining a plugin scattering point provider.

            * - :py:class:`~CRPluginConfiguration`
              - Class defining plugin configuration.

            * - :py:class:`~RadarJamming`
              - Class defining radar jamming.

            * - :py:class:`~RFInterference`
              - Class defining radar jamming.

            * - :py:class:`~RFFilterModel`
              - Class defining a generic RF filter model.

            * - :py:class:`~RFFilterModelBessel`
              - Class defining a bessel filter model.

            * - :py:class:`~RFFilterModelSincEnvSinc`
              - Class defining a Sinc Envelope Sinc filter model.

            * - :py:class:`~RFFilterModelElliptic`
              - Class defining a elliptic filter model.

            * - :py:class:`~RFFilterModelChebyshev`
              - Class defining a Chebyshev filter model.

            * - :py:class:`~RFFilterModelCosineWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~RFFilterModelGaussianWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~RFFilterModelHammingWindow`
              - Class defining a cosine window filter model.

            * - :py:class:`~RFFilterModelButterworth`
              - Class defining a butterworth filter model.

            * - :py:class:`~RFFilterModelExternal`
              - Class defining a external filter model.

            * - :py:class:`~RFFilterModelScriptPlugin`
              - Class defining a script plugin filter model.

            * - :py:class:`~RFFilterModelSinc`
              - Class defining a sinc filter model.

            * - :py:class:`~RFFilterModelRaisedCosine`
              - Class defining a raised cosine filter model.

            * - :py:class:`~RFFilterModelRootRaisedCosine`
              - Class defining a root raised cosine filter model.

            * - :py:class:`~RFFilterModelRcLowPass`
              - Class defining a rc low pass filter model.

            * - :py:class:`~RFFilterModelRectangular`
              - Class defining a rectangular filter model.

            * - :py:class:`~RFFilterModelFirBoxCar`
              - Class defining a FIR box car filter model.

            * - :py:class:`~RFFilterModelIir`
              - Class defining a IIR box car filter model.

            * - :py:class:`~RFFilterModelFir`
              - Class defining a FIR filter model.

            * - :py:class:`~SystemNoiseTemperature`
              - Class defining system noise temperature.

            * - :py:class:`~AntennaNoiseTemperature`
              - Class defining antenna noise temperature.

            * - :py:class:`~Atmosphere`
              - Class defining local atmosphere.

            * - :py:class:`~LaserPropagationLossModels`
              - Class defining the properties for laser propagatoin models.

            * - :py:class:`~LaserAtmosphericLossModel`
              - Class defining an laser propagation loss model.

            * - :py:class:`~LaserAtmosphericLossModelBeerBouguerLambertLaw`
              - Class defining an laser propagation loss model.

            * - :py:class:`~ModtranLookupTablePropagationModel`
              - Class defining an MODTRAN-based lookup table propagation model.

            * - :py:class:`~ModtranPropagationModel`
              - Class defining a MODTRAN propagation model.

            * - :py:class:`~LaserTroposphericScintillationLossModel`
              - Class defining an laser tropospheric scintillation loss model.

            * - :py:class:`~AtmosphericTurbulenceModel`
              - Class defining a atmospheric turbulence model.

            * - :py:class:`~AtmosphericTurbulenceModelConstant`
              - Class defining a constant atmospheric turbulence model.

            * - :py:class:`~AtmosphericTurbulenceModelHufnagelValley`
              - Class defining a Hufnagel Valley atmospheric turbulence model.

            * - :py:class:`~LaserTroposphericScintillationLossModelITURP1814`
              - Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

            * - :py:class:`~AtmosphericAbsorptionModel`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelITURP676_9`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelVoacap`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelTirem320`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelTirem331`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelTirem550`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelSimpleSatcom`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelScriptPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~AtmosphericAbsorptionModelCOMPlugin`
              - Class defining an atmospheric absorption model.

            * - :py:class:`~ScatteringPointModel`
              - Class defining a scattering point model.

            * - :py:class:`~ScatteringPointModelPlugin`
              - Class defining a plugin scattering point model.

            * - :py:class:`~ScatteringPointModelConstantCoefficient`
              - Class defining a constant coefficient scattering point model.

            * - :py:class:`~ScatteringPointModelWindTurbine`
              - Class defining a wind turbine scattering point model.

            * - :py:class:`~RadarCrossSection`
              - Class defining a radar cross section.

            * - :py:class:`~RadarCrossSectionModel`
              - Class defining a radar cross section model.

            * - :py:class:`~RadarCrossSectionInheritable`
              - Class defining a inheritable radar cross section.

            * - :py:class:`~RadarCrossSectionFrequencyBand`
              - Class defining a inheritable radar cross section frequency band.

            * - :py:class:`~RadarCrossSectionFrequencyBandCollection`
              - Class defining a inheritable radar cross section frequency band collection.

            * - :py:class:`~RadarCrossSectionComputeStrategy`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~RadarCrossSectionComputeStrategyConstantValue`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~RadarCrossSectionComputeStrategyScriptPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~RadarCrossSectionComputeStrategyExternalFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~RadarCrossSectionComputeStrategyAnsysCsvFile`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~RadarCrossSectionComputeStrategyPlugin`
              - Class defining a inheritable radar cross section compute strategy.

            * - :py:class:`~CustomPropagationModel`
              - Class defining a custom propatation model.

            * - :py:class:`~PropagationChannel`
              - Class defining the propagation channel.

            * - :py:class:`~RFEnvironment`
              - Class defining the RF environment.

            * - :py:class:`~LaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~ObjectRFEnvironment`
              - Class defining the RF environment for an object.

            * - :py:class:`~ObjectLaserEnvironment`
              - Class defining the laser environment for an object.

            * - :py:class:`~PlatformLaserEnvironment`
              - Class defining the laser environment for an platform.

            * - :py:class:`~RainLossModel`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelITURP618_12`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelITURP618_13`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelITURP618_10`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelCrane1985`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelCrane1982`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelCCIR1983`
              - Class defining a rain loss model.

            * - :py:class:`~RainLossModelScriptPlugin`
              - Class defining a rain loss model.

            * - :py:class:`~CloudsAndFogFadingLossModel`
              - Class defining a clouds and fog fading loss model.

            * - :py:class:`~CloudsAndFogFadingLossModelP840_6`
              - Class defining a clouds and fog Loss ITU-R P.840-6 model.

            * - :py:class:`~CloudsAndFogFadingLossModelP840_7`
              - Class defining a clouds and fog Loss ITU-R P.840-7 model.

            * - :py:class:`~TroposphericScintillationFadingLossModel`
              - Class defining a tropospheric scintillation fading loss model.

            * - :py:class:`~TroposphericScintillationFadingLossModelP618_8`
              - Class defining a tropospheric scintillation fading loss P.618-8 model.

            * - :py:class:`~TroposphericScintillationFadingLossModelP618_12`
              - Class defining a tropospheric scintillation fading loss P.618-12 model.

            * - :py:class:`~IonosphericFadingLossModel`
              - Class defining a Ionospheric fading loss model.

            * - :py:class:`~IonosphericFadingLossModelP531_13`
              - Class defining a Ionospheric fading loss P.531-13 model.

            * - :py:class:`~UrbanTerrestrialLossModel`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~UrbanTerrestrialLossModelTwoRay`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~UrbanTerrestrialLossModelWirelessInSite64`
              - Class defining an urban/terrestrial loss model.

            * - :py:class:`~WirelessInSite64GeometryData`
              - Class defining the REMCOM Wireless InSite 64 geometry data.

            * - :py:class:`~PointingStrategy`
              - Class defining a pointing strategy.

            * - :py:class:`~PointingStrategyFixed`
              - Class defining a fixed pointing strategy.

            * - :py:class:`~PointingStrategySpinning`
              - Class defining a spinning pointing strategy.

            * - :py:class:`~PointingStrategyTargeted`
              - Class defining a targeted pointing strategy.

            * - :py:class:`~CRLocation`
              - Class defining a location.

            * - :py:class:`~CRComplex`
              - Class defining a complex number.

            * - :py:class:`~CRComplexCollection`
              - Class defining a collection of complex numbers.

            * - :py:class:`~ModulatorModel`
              - Class defining a modulator model.

            * - :py:class:`~ModulatorModelBpsk`
              - Class defining a BPSK modulator model.

            * - :py:class:`~ModulatorModelQpsk`
              - Class defining a QPSK modulator model.

            * - :py:class:`~ModulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~ModulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~ModulatorModelQam16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~ModulatorModelQam32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~ModulatorModelQam64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~ModulatorModelQam128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~ModulatorModelQam256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~ModulatorModelQam1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~ModulatorModel8psk`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~ModulatorModel16psk`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~ModulatorModelMsk`
              - Class defining a MSK modulator model.

            * - :py:class:`~ModulatorModelBoc`
              - Class defining a BOC modulator model.

            * - :py:class:`~ModulatorModelDpsk`
              - Class defining a DPSK modulator model.

            * - :py:class:`~ModulatorModelFsk`
              - Class defining a FSK modulator model.

            * - :py:class:`~ModulatorModelNfsk`
              - Class defining a NFSK modulator model.

            * - :py:class:`~ModulatorModelOqpsk`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~ModulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~ModulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~ModulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~ModulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~ModulatorModelScriptPluginCustomPsd`
              - Class defining a custom PSD script plugin modulator model.

            * - :py:class:`~ModulatorModelScriptPluginIdealPsd`
              - Class defining a ideal PSD script plugin modulator model.

            * - :py:class:`~LinkMargin`
              - Class defining a link margin computation object.

            * - :py:class:`~DemodulatorModel`
              - Class defining a demodulator model.

            * - :py:class:`~DemodulatorModelBpsk`
              - Class defining a BPSK modulator model.

            * - :py:class:`~DemodulatorModelQpsk`
              - Class defining a QPSK modulator model.

            * - :py:class:`~DemodulatorModelExternalSource`
              - Class defining a external source modulator model.

            * - :py:class:`~DemodulatorModelExternal`
              - Class defining a external modulator model.

            * - :py:class:`~DemodulatorModelQam16`
              - Class defining a QAM 16 modulator model.

            * - :py:class:`~DemodulatorModelQam32`
              - Class defining a QAM 32 modulator model.

            * - :py:class:`~DemodulatorModelQam64`
              - Class defining a QAM 64 modulator model.

            * - :py:class:`~DemodulatorModelQam128`
              - Class defining a QAM 128 modulator model.

            * - :py:class:`~DemodulatorModelQam256`
              - Class defining a QAM 256 modulator model.

            * - :py:class:`~DemodulatorModelQam1024`
              - Class defining a QAM 1024 modulator model.

            * - :py:class:`~DemodulatorModel8psk`
              - Class defining a 8PSK modulator model.

            * - :py:class:`~DemodulatorModel16psk`
              - Class defining a 16PSK modulator model.

            * - :py:class:`~DemodulatorModelMsk`
              - Class defining a MSK modulator model.

            * - :py:class:`~DemodulatorModelBoc`
              - Class defining a BOC modulator model.

            * - :py:class:`~DemodulatorModelDpsk`
              - Class defining a DPSK modulator model.

            * - :py:class:`~DemodulatorModelFsk`
              - Class defining a FSK modulator model.

            * - :py:class:`~DemodulatorModelNfsk`
              - Class defining a NFSK modulator model.

            * - :py:class:`~DemodulatorModelOqpsk`
              - Class defining a OQPSK modulator model.

            * - :py:class:`~DemodulatorModelNarrowbandUniform`
              - Class defining a narrowband uniform modulator model.

            * - :py:class:`~DemodulatorModelWidebandUniform`
              - Class defining a wideband uniform modulator model.

            * - :py:class:`~DemodulatorModelWidebandGaussian`
              - Class defining a wideband gaussian modulator model.

            * - :py:class:`~DemodulatorModelPulsedSignal`
              - Class defining a pulsed signal modulator model.

            * - :py:class:`~DemodulatorModelScriptPlugin`
              - Class defining a script plugin modulator model.

            * - :py:class:`~TransferFunctionPolynomialCollection`
              - Class defining a collection of polynomial coefficients.

            * - :py:class:`~TransferFunctionInputBackOffCOverImTableRow`
              - Class defining a row of an input back off vs C/Im table.

            * - :py:class:`~TransferFunctionInputBackOffCOverImTable`
              - Class defining an input back off vs C/Im table.

            * - :py:class:`~TransferFunctionInputBackOffOutputBackOffTableRow`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~TransferFunctionInputBackOffOutputBackOffTable`
              - Class defining an input back off vs output back off table.

            * - :py:class:`~BeerBouguerLambertLawLayer`
              - Class defining a row of an input back off vs output back off table.

            * - :py:class:`~BeerBouguerLambertLawLayerCollection`
              - Class defining collection of Beer-Bouguer-Lamber Law atmosphere layers.

            * - :py:class:`~RadarActivity`
              - Class defining radar activity.

            * - :py:class:`~RadarActivityAlwaysActive`
              - Class defining radar always active activity.

            * - :py:class:`~RadarActivityAlwaysInactive`
              - Class defining radar always active inactivity.

            * - :py:class:`~RadarActivityTimeComponentListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~RadarActivityTimeComponentListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~RadarActivityTimeComponentList`
              - Class defining a radar time component list activity.

            * - :py:class:`~RadarActivityTimeIntervalListElement`
              - Class defining an element of the time components activity list.

            * - :py:class:`~RadarActivityTimeIntervalListCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~RadarActivityTimeIntervalList`
              - Class defining a radar time component list activity.

            * - :py:class:`~RadarAntennaBeam`
              - Class defining a radar antenna beam.

            * - :py:class:`~RadarAntennaBeamCollection`
              - Class defining an radar antenna beam collection.

            * - :py:class:`~AntennaSystem`
              - Class defining an antenna system.

            * - :py:class:`~AntennaBeam`
              - Class defining an antenna beam.

            * - :py:class:`~AntennaBeamTransmit`
              - Class defining a transmit antenna beam.

            * - :py:class:`~AntennaBeamCollection`
              - Class defining an antenna beam collection.

            * - :py:class:`~AntennaBeamSelectionStrategy`
              - Class defining a beam selection strategy.

            * - :py:class:`~AntennaBeamSelectionStrategyAggregate`
              - Class defining a aggregated beam selection strategy.

            * - :py:class:`~AntennaBeamSelectionStrategyMaxGain`
              - Class defining a maximum gain beam selection strategy.

            * - :py:class:`~AntennaBeamSelectionStrategyMinBoresightAngle`
              - Class defining a minimum boresight angle beam selection strategy.

            * - :py:class:`~AntennaBeamSelectionStrategyScriptPlugin`
              - Class defining a script plugin beam selection strategy.

            * - :py:class:`~CommSystem`
              - Class defining a CommSystem object.

            * - :py:class:`~CommSystemGraphics`
              - Class defining 2D Graphics properties of a CommSystem.

            * - :py:class:`~CommSystemGraphics3D`
              - Class defining 3D Graphics properties of a CommSystem.

            * - :py:class:`~CommSystemAccessOptions`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemAccessEventDetection`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemAccessEventDetectionSubsample`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemAccessEventDetectionSamplesOnly`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemAccessSamplingMethod`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemAccessSamplingMethodFixed`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemAccessSamplingMethodAdaptive`
              - Class defining a CommSystem access options.

            * - :py:class:`~CommSystemLinkSelectionCriteria`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~CommSystemLinkSelectionCriteriaMinimumRange`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~CommSystemLinkSelectionCriteriaMaximumElevation`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~CommSystemLinkSelectionCriteriaScriptPlugin`
              - Class defining a CommSystem link selection criteria.

            * - :py:class:`~ComponentDirectory`
              - Manages all components.

            * - :py:class:`~ComponentInfo`
              - Class defining a component.

            * - :py:class:`~ComponentInfoCollection`
              - The collection of components and component folders.

            * - :py:class:`~ComponentAttrLinkEmbedControl`
              - Attribute based component link/embed control.

            * - :py:class:`~Volumetric`
              - The AgVolumetric class.

            * - :py:class:`~VmGridSpatialCalculation`
              - Class defining the volume grid spatial calculation.

            * - :py:class:`~VmExternalFile`
              - Class defining the volume external file.

            * - :py:class:`~VmAnalysisInterval`
              - Class defining the volumetric analysis interval.

            * - :py:class:`~VmAdvanced`
              - Class defining the volumetric Computed Data Save options.

            * - :py:class:`~VmGraphics3D`
              - Class defining 3D graphics properties of volumetric object.

            * - :py:class:`~VmGraphics3DGrid`
              - Class defining grid properties of 3D graphics for volumetric object.

            * - :py:class:`~VmGraphics3DCrossSection`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~VmGraphics3DCrossSectionPlane`
              - Class defining cross-section plane for volumetric grid.

            * - :py:class:`~VmGraphics3DCrossSectionPlaneCollection`
              - Class defining collection of cross-section planes for volumetric grid.

            * - :py:class:`~VmGraphics3DVolume`
              - Class defining planar cross-sections through the volumetric grid.

            * - :py:class:`~VmGraphics3DActiveGridPoints`
              - Class defining Active Grid Points for Volumetric Object.

            * - :py:class:`~VmGraphics3DSpatialCalculationLevels`
              - Class defining Spatial Calculation Levels for Volumetric Object.

            * - :py:class:`~VmGraphics3DSpatialCalculationLevel`
              - Class defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~VmGraphics3DSpatialCalculationLevelCollection`
              - Class defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

            * - :py:class:`~VmGraphics3DLegend`
              - Class defining Boundary/Fill legend for volumetric object.

            * - :py:class:`~VmExportTool`
              - The Volumetric Export Tool.

            * - :py:class:`~SatelliteCollection`
              - The AgSatelliteCollection class.

            * - :py:class:`~Subset`
              - The AgSubset class.

            * - :py:class:`~ElementConfiguration`
              - Class defining an element configuration.

            * - :py:class:`~ElementConfigurationCircular`
              - Class defining a circular element configuration.

            * - :py:class:`~ElementConfigurationLinear`
              - Class defining a linear element configuration.

            * - :py:class:`~ElementConfigurationAsciiFile`
              - Class defining a ascii file element configuration.

            * - :py:class:`~ElementConfigurationHfssEepFile`
              - Class defining an HFSS EEP file element configuration.

            * - :py:class:`~ElementConfigurationPolygon`
              - Class defining a polygon element configuration.

            * - :py:class:`~ElementConfigurationHexagon`
              - Class defining a hexagon element configuration.

            * - :py:class:`~SolarActivityConfiguration`
              - Class defining a solar activity configuration.

            * - :py:class:`~SolarActivityConfigurationSunspotNumber`
              - Class defining sunspot number configuration.

            * - :py:class:`~SolarActivityConfigurationSolarFlux`
              - Class defining the solar flux configuration.

            * - :py:class:`~Beamformer`
              - Class defining a beamformer.

            * - :py:class:`~BeamformerAsciiFile`
              - Class defining a beamformer ascii file.

            * - :py:class:`~BeamformerMvdr`
              - Class defining a beamformer mvdr.

            * - :py:class:`~BeamformerUniform`
              - Class defining a uniform tapered beamformer.

            * - :py:class:`~BeamformerBlackmanHarris`
              - Class defining a Blackman-Harris tapered beamformer.

            * - :py:class:`~BeamformerCosine`
              - Class defining a cosine tapered beamformer.

            * - :py:class:`~BeamformerCosineX`
              - Class defining a cosine^X tapered beamformer.

            * - :py:class:`~BeamformerCustomTaperFile`
              - Class defining a custom taper file beamformer.

            * - :py:class:`~BeamformerDolphChebyshev`
              - Class defining a Dolph-Chebyshev tapered beamformer.

            * - :py:class:`~BeamformerHamming`
              - Class defining a Hamming tapered beamformer.

            * - :py:class:`~BeamformerHann`
              - Class defining a Hann tapered beamformer.

            * - :py:class:`~BeamformerRaisedCosine`
              - Class defining a raised cosine tapered beamformer.

            * - :py:class:`~BeamformerRaisedCosineSquared`
              - Class defining a raised cosine squared tapered beamformer.

            * - :py:class:`~BeamformerScript`
              - Class defining a beamformer script plugin.

            * - :py:class:`~DirectionProvider`
              - Class defining a direction provider.

            * - :py:class:`~DirectionProviderAsciiFile`
              - Class defining an ascii file direction provider.

            * - :py:class:`~DirectionProviderObject`
              - Class defining an object direction provider.

            * - :py:class:`~DirectionProviderLink`
              - Class defining an link direction provider.

            * - :py:class:`~DirectionProviderScript`
              - Class defining an script plugin direction provider.

            * - :py:class:`~Element`
              - Class defining a phased array element.

            * - :py:class:`~ElementCollection`
              - Class defining a phased array element collection.

            * - :py:class:`~KeyValueCollection`
              - A collection of keys and values associated with the keys.

            * - :py:class:`~RadarStcAttenuation`
              - Class defining an radar stc.

            * - :py:class:`~RadarStcAttenuationDecayFactor`
              - Class defining an radar decay factor stc.

            * - :py:class:`~RadarStcAttenuationDecaySlope`
              - Class defining an radar decay slope stc.

            * - :py:class:`~RadarStcAttenuationMapRange`
              - Class defining an radar stc range map.

            * - :py:class:`~RadarStcAttenuationMapAzimuthRange`
              - Class defining an radar stc azimuth-range map.

            * - :py:class:`~RadarStcAttenuationMapElevationRange`
              - Class defining an radar stc elevation-range map.

            * - :py:class:`~RadarStcAttenuationPlugin`
              - Class defining an radar stc Com Plugin.

            * - :py:class:`~SensorPointingAlongVector`
              - Class defining the along vector pointing type for a Sensor.

            * - :py:class:`~SensorPointingSchedule`
              - Allow to schedule a sensor to point at a specific location at a specific time.

            * - :py:class:`~AccessConstraintAnalysisWorkbenchCollection`
              - Collection of Analysis Workbench constraints.

            * - :py:class:`~AccessConstraintAnalysisWorkbench`
              - Class related to Analysis Workbench constraints.

            * - :py:class:`~Graphics3DArticulationFile`
              - Class defining the vo articulation file.

            * - :py:class:`~DataProviderResultStatisticResult`
              - Results returned by statistics computation.

            * - :py:class:`~DataProviderResultTimeVaryingExtremumResult`
              - Results returned by time varying extremum computation.

            * - :py:class:`~DataProviderResultStatistics`
              - Class used to compute statistics and time varying extremum on data provider result data sets.

            * - :py:class:`~Graphics3DModelGltfImageBased`
              - Class defining glTF Reflection Settings.

            * - :py:class:`~StkObjectCutCopyPasteEventArgs`
              - Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

            * - :py:class:`~StkPreferencesPythonPlugins`
              - Allow configuring Python plugin preferences.

            * - :py:class:`~PathCollection`
              - Allow adding and removing of paths.

            * - :py:class:`~AdvCAT`
              - AdvCAT properties.

            * - :py:class:`~AdvCATAvailableObjectCollection`
              - Read-only collection of available objects.

            * - :py:class:`~AdvCATChosenObject`
              - A chosen object.

            * - :py:class:`~AdvCATChosenObjectCollection`
              - The chosen object collection.

            * - :py:class:`~AdvCATPreFilters`
              - AdvCAT pre-filters properties.

            * - :py:class:`~AdvCATAdvancedEllipsoid`
              - AdvCAT advanced ellipsoid properties.

            * - :py:class:`~AdvCATAdvanced`
              - AdvCAT advanced properties.

            * - :py:class:`~AdvCATGraphics3D`
              - AdvCAT VO properties.

            * - :py:class:`~EOIRShapeObject`
              - Represents a generic shape object.

            * - :py:class:`~EOIRShapeBox`
              - Box shape class.

            * - :py:class:`~EOIRShapeCone`
              - Cone shape class.

            * - :py:class:`~EOIRShapeCylinder`
              - Cylinder shape class.

            * - :py:class:`~EOIRShapePlate`
              - Plate shape class.

            * - :py:class:`~EOIRShapeSphere`
              - Sphere shape class.

            * - :py:class:`~EOIRShapeCoupler`
              - Coupler shape class.

            * - :py:class:`~EOIRShapeNone`
              - None shape class.

            * - :py:class:`~EOIRShapeGEOComm`
              - GEOComm shape class.

            * - :py:class:`~EOIRShapeLEOComm`
              - LEOComm shape class.

            * - :py:class:`~EOIRShapeLEOImaging`
              - LEOImaging shape class.

            * - :py:class:`~EOIRShapeCustomMesh`
              - CustomMesh shape class.

            * - :py:class:`~EOIRShapeTargetSignature`
              - TargetSignature shape class.

            * - :py:class:`~EOIRStagePlume`
              - Plume shape class.

            * - :py:class:`~EOIRShape`
              - AgEOIRShape class.

            * - :py:class:`~EOIRShapeCollection`
              - Collection of shapes.

            * - :py:class:`~EOIRMaterialElement`
              - AgEOIRMaterialElement class.

            * - :py:class:`~EOIRMaterialElementCollection`
              - Collection of material elements.

            * - :py:class:`~EOIRStage`
              - Stage base class.

            * - :py:class:`~EOIR`
              - AgEOIR interface class.

            * - :py:class:`~MissileEOIR`
              - AgMsEOIR interface class.

            * - :py:class:`~VehicleEOIR`
              - AgVeEOIR interface class.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~CONSTANTS`
              - AgEConstants contains base IDs for various structures.

            * - :py:class:`~HELP_CONTEXT_IDS`
              - Help context IDs.

            * - :py:class:`~ERROR_CODES`
              - Error codes.

            * - :py:class:`~ABERRATION_TYPE`
              - The model of aberration to be used in access computations.

            * - :py:class:`~ANIMATION_MODES`
              - Animation modes.

            * - :py:class:`~ANIMATION_OPTIONS`
              - Animation Options.

            * - :py:class:`~ANIMATION_ACTIONS`
              - Animation action options.

            * - :py:class:`~ANIMATION_DIRECTIONS`
              - Animation direction options.

            * - :py:class:`~AZ_EL_MASK_TYPE`
              - Obscura types of the facility, place or target for AzElMask definition.

            * - :py:class:`~ACTION_TYPE`
              - Specify the action type for the Interval Access Constraint.

            * - :py:class:`~AXIS_OFFSET`
              - Specify the axis offset for the sensor 3D Vertex Offset.

            * - :py:class:`~DATA_PROVIDER_RESULT_CATEGORIES`
              - Specify the category of results returned by the data providers.

            * - :py:class:`~DATA_PROVIDER_TYPE`
              - Specify the type of the result returned by data providers.

            * - :py:class:`~DATA_PROVIDER_ELEMENT_TYPE`
              - Specify the type of data returned by data providers.

            * - :py:class:`~ACCESS_TIME_TYPE`
              - The time period to use for the access computation.

            * - :py:class:`~ALTITUDE_REFERENCE_TYPE`
              - Altitude reference options.

            * - :py:class:`~TERRAIN_NORM_TYPE`
              - Methods of defining the slope of the local terrain for the facility, place or target.

            * - :py:class:`~LIGHTING_OBSTRUCTION_MODEL_TYPE`
              - Obstruction model used in lighting computations.

            * - :py:class:`~DISPLAY_TIMES_TYPE`
              - Display times options for the object.

            * - :py:class:`~AREA_TYPE`
              - Methods of defining the area target's boundaries.

            * - :py:class:`~TRAJECTORY_TYPE`
              - Trajectory type for a point.

            * - :py:class:`~OFFSET_FRAME_TYPE`
              - Frame options for label offset.

            * - :py:class:`~SCENARIO_3D_POINT_SIZE`
              - Font size in points.

            * - :py:class:`~TERRAIN_FILE_TYPE`
              - Terrain file type options.

            * - :py:class:`~TILESET_3D_SOURCE_TYPE`
              - 3DTileset source type options.

            * - :py:class:`~MARKER_TYPE`
              - Marker style options for a waypoint.

            * - :py:class:`~VECTOR_AXES_CONNECT_TYPE`
              - Methods for connecting geometric elements.

            * - :py:class:`~GRAPHICS_3D_MARKER_ORIGIN_TYPE`
              - Options for the AgVOMarker X or Y Origin property.

            * - :py:class:`~GRAPHICS_3D_LABEL_SWAP_DISTANCE`
              - Label swap distance options.

            * - :py:class:`~PLANET_POSITION_SOURCE_TYPE`
              - Options for defining a planet.

            * - :py:class:`~EPHEM_SOURCE_TYPE`
              - Central body ephemeris sources.

            * - :py:class:`~PLANET_ORBIT_DISPLAY_TYPE`
              - Orbit display options for a planet.

            * - :py:class:`~SCENARIO_END_LOOP_TYPE`
              - Scenario animation cycle options.

            * - :py:class:`~SCENARIO_REFRESH_DELTA_TYPE`
              - Scenario animation refresh update options.

            * - :py:class:`~SENSOR_PATTERN`
              - Sensor patterns.

            * - :py:class:`~SENSOR_POINTING`
              - Sensor pointing options.

            * - :py:class:`~SENSOR_POINTING_TARGETED_BORESIGHT_TYPE`
              - Boresight types for sensors of targeted pointing type.

            * - :py:class:`~BORESIGHT_TYPE`
              - About boresight options for sensors of targeted pointing type.

            * - :py:class:`~TRACK_MODE_TYPE`
              - Track mode options for tracking boresights.

            * - :py:class:`~SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE`
              - Primary boresight axis for Sensor Az-El mask.

            * - :py:class:`~SENSOR_REFRACTION_TYPE`
              - Sensor refraction models.

            * - :py:class:`~SENSOR_PROJECTION_DISTANCE_TYPE`
              - Sensor 2D Graphics Projection 'Project To' options.

            * - :py:class:`~SENSOR_LOCATION`
              - Sensor Location Type options.

            * - :py:class:`~SCENARIO_TIME_STEP_TYPE`
              - Scenario animation time step options.

            * - :py:class:`~NOTE_SHOW_TYPE`
              - Options for specifying when a label note displays.

            * - :py:class:`~GEOMETRIC_ELEM_TYPE`
              - Options for the VORefCrdn Type.

            * - :py:class:`~SENSOR_SCAN_MODE`
              - Options for the Sensor Spinning Scan Mode.

            * - :py:class:`~CONSTRAINT_BACKGROUND`
              - Options for the Background constraint, and Advanced vehicle constraint.

            * - :py:class:`~CONSTRAINT_GROUND_TRACK`
              - Options for the Ground Track constraint, an Advanced vehicle constraint.

            * - :py:class:`~INTERSECTION_TYPE`
              - Intersection display options for sensor projection.

            * - :py:class:`~CONSTRAINT_LIGHTING`
              - Options for the Lighting access constraint.

            * - :py:class:`~SENSOR_GRAPHICS_3D_PROJECTION_TYPE`
              - Options for a sensor's 3D Graphics Projection Type.

            * - :py:class:`~SENSOR_GRAPHICS_3D_PULSE_STYLE`
              - Options for a sensor's 3D Graphics Pulse Style.

            * - :py:class:`~SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET`
              - Options for a sensor's 3D Graphics Pulse Frequency presets.

            * - :py:class:`~LINE_WIDTH`
              - Line widths.

            * - :py:class:`~STK_OBJECT_TYPE`
              - STK objects.

            * - :py:class:`~ACCESS_CONSTRAINTS`
              - Available Access Constraint.

            * - :py:class:`~BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE`
              - Border Wall upper and lower edge altitude references.

            * - :py:class:`~SHADOW_MODEL`
              - Shadow model options for solar radiation pressure.

            * - :py:class:`~METHOD_TO_COMPUTE_SUN_POSITION`
              - Methods to compute sun position.

            * - :py:class:`~ATMOSPHERIC_DENSITY_MODEL`
              - Atmospheric density models.

            * - :py:class:`~MARKER_SHAPE_3D`
              - 3D marker shapes.

            * - :py:class:`~LEAD_TRAIL_DATA`
              - Lead and trail types for track display.

            * - :py:class:`~TICK_DATA`
              - Tick mark options. Tick marks represent milestones at specified intervals along a vehicle's track in the 3D Graphics window.

            * - :py:class:`~LOAD_METHOD_TYPE`
              - TLE load options.

            * - :py:class:`~LLA_POSITION_TYPE`
              - LLA Position Types.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_PASS`
              - Pass display options.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_VISIBLE_SIDES`
              - Pass display direction options.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_OFFSET`
              - Options for offset direction for 2D time events graphics.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE`
              - 2D Graphics time event graphics options.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_ATTRIBUTES`
              - Criteria for displaying a vehicle's 2D Graphics attributes.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_ELEVATION`
              - Options for vehicle swath.

            * - :py:class:`~VEHICLE_GRAPHICS_2D_OPTIONS`
              - Display options for vehicle swath.

            * - :py:class:`~MODEL_TYPE`
              - Display options 3D model.

            * - :py:class:`~VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE`
              - Options for where to end drop lines.

            * - :py:class:`~VEHICLE_GRAPHICS_3D_SIGMA_SCALE`
              - Sigma scale options for sizing covariance pointing contours.

            * - :py:class:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`
              - Options for 3D graphics for covariance pointing contours.

            * - :py:class:`~ROUTE_GRAPHICS_3D_MARKER_TYPE`
              - Waypoint marker options.

            * - :py:class:`~VEHICLE_ELLIPSE_OPTIONS`
              - Elliptical motion modeling options.

            * - :py:class:`~VEHICLE_PROPAGATOR_TYPE`
              - Vehicle propagators (available for vehicle types listed in parentheses).

            * - :py:class:`~VEHICLE_SGP4_SWITCH_METHOD`
              - TLE Switch method for the SGP4 propagator.

            * - :py:class:`~VEHICLE_SGP4TLE_SELECTION`
              - TLE Selection method for the SGP4 propagator.

            * - :py:class:`~VEHICLE_SGP4_AUTO_UPDATE_SOURCE`
              - The TLE sources where the SGP4 propagator retrieves TLEs from automatically upon propagation.

            * - :py:class:`~THIRD_BODY_GRAV_SOURCE_TYPE`
              - Sources for 3rd body gravitation data.

            * - :py:class:`~VEHICLE_GEOMAG_FLUX_SRC`
              - GeomagFluxSrc.

            * - :py:class:`~VEHICLE_GEOMAG_FLUX_UPDATE_RATE`
              - Geomagnetic flux update rate options.

            * - :py:class:`~VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE`
              - Options for specifying solar and geomagnetic flux.

            * - :py:class:`~VEHICLE_INTEGRATION_MODEL`
              - Integration methods.

            * - :py:class:`~VEHICLE_PREDICTOR_CORRECTOR_SCHEME`
              - Predictor Corrector schemes.

            * - :py:class:`~VEHICLE_METHOD`
              - Step size control options.

            * - :py:class:`~VEHICLE_INTERPOLATION_METHOD`
              - Interpolation methods.

            * - :py:class:`~VEHICLE_FRAME`
              - Frame options for covariance matrix.

            * - :py:class:`~VEHICLE_CORRELATION_LIST_TYPE`
              - Correlation List row and column values.

            * - :py:class:`~VEHICLE_CONSIDER_ANALYSIS_TYPE`
              - Consider parameters for HPOP covariance.

            * - :py:class:`~VEHICLE_WAYPOINT_COMP_METHOD`
              - Methods for computing waypoints.

            * - :py:class:`~VEHICLE_ALTITUDE_REFERENCE`
              - Reference altitude options for waypoints.

            * - :py:class:`~VEHICLE_WAYPOINT_INTERP_METHOD`
              - Interpolation methods.

            * - :py:class:`~VEHICLE_LAUNCH`
              - Options for launch coordinates.

            * - :py:class:`~VEHICLE_IMPACT`
              - Impact location options.

            * - :py:class:`~VEHICLE_LAUNCH_CONTROL`
              - Flight parameters for a missile.

            * - :py:class:`~VEHICLE_IMPACT_LOCATION`
              - Options for specifying missile impact point.

            * - :py:class:`~VEHICLE_PASS_NUMBERING`
              - Pass numbering options.

            * - :py:class:`~VEHICLE_PARTIAL_PASS_MEASUREMENT`
              - Partial Pass Measurement methods (typically used for reporting data).

            * - :py:class:`~VEHICLE_COORDINATE_SYSTEM`
              - Coordinate system used for measurement of latitude and longitude.

            * - :py:class:`~VEHICLE_BREAK_ANGLE_TYPE`
              - Definition options for setting pass breaks:.

            * - :py:class:`~VEHICLE_DIRECTION`
              - Direction of latitude crossing at the beginning of a pass.

            * - :py:class:`~GRAPHICS_3D_LOCATION`
              - Location options for the display of textual data in the 3D Graphics window.

            * - :py:class:`~GRAPHICS_3D_X_ORIGIN`
              - X origin options for positioning data display.

            * - :py:class:`~GRAPHICS_3D_Y_ORIGIN`
              - Y origin options for positioning data display.

            * - :py:class:`~GRAPHICS_3D_FONT_SIZE`
              - Font size for data display.

            * - :py:class:`~AIRCRAFT_WGS84_WARNING_TYPE`
              - Display mode options for aircraft mission modeler WGS84 warning.

            * - :py:class:`~SURFACE_REFERENCE`
              - Options for surface reference of earth globes.

            * - :py:class:`~GRAPHICS_3D_FORMAT`
              - Font format for data display.

            * - :py:class:`~ATTITUDE_STANDARD_TYPE`
              - AgEAttitudeStandardType tells the user which interface to cast to. eRouteAttitudeStandard -> IAgVeRouteAttitudeStandard, eTrajectoryAttitudeStandard -> IAgVeTrajectoryAttitudeStandard, eOrbitAttitudeStanard -> IAgVeOrbitAttitudeStandard.

            * - :py:class:`~VEHICLE_ATTITUDE`
              - Available attitude types.

            * - :py:class:`~VEHICLE_PROFILE`
              - Predefined attitude profiles.

            * - :py:class:`~VEHICLE_LOOK_AHEAD_METHOD`
              - Look ahead duration methods.

            * - :py:class:`~VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~SENSOR_ALTITUDE_CROSSING_SIDES`
              - Options for specifying which crossings are computed and displayed in the 2D Graphics window.

            * - :py:class:`~SENSOR_ALTITUDE_CROSSING_DIRECTION`
              - Options for specifying the direction in which the sensor's field of view crosses the specified altitude.

            * - :py:class:`~SENSOR_GRAPHICS_3D_INHERIT_FROM_2D`
              - Options for how projection distances that are computed based on 2D Graphics projection settings are displayed in the 3D Graphics window.

            * - :py:class:`~SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE`
              - Options optimizing the visual appearance of projections.

            * - :py:class:`~CHAIN_TIME_PERIOD_TYPE`
              - Compute Time Period Type.

            * - :py:class:`~CHAIN_CONST_CONSTRAINTS_MODE`
              - Constellation Constraints Mode.

            * - :py:class:`~CHAIN_COV_ASSET_MODE`
              - Chain Cov Asset Mode.

            * - :py:class:`~CHAIN_PARENT_PLATFORM_RESTRICTION`
              - Options for a chain's From and To Parent Platform Restriction.

            * - :py:class:`~CHAIN_OPTIMAL_STRAND_METRIC_TYPE`
              - Chain optimal strand metric type.

            * - :py:class:`~CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE`
              - Chain optimal strand calculation scalar type.

            * - :py:class:`~CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE`
              - Chain optimal strand link comparison type.

            * - :py:class:`~CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE`
              - Chain optimal strand link comparison type.

            * - :py:class:`~DATA_SAVE_MODE`
              - Access Save Mode.

            * - :py:class:`~COVERAGE_BOUNDS`
              - Coverage bounds options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~COVERAGE_POINT_LOC_METHOD`
              - Point location method.

            * - :py:class:`~COVERAGE_POINT_ALTITUDE_METHOD`
              - Custom point altitude method.

            * - :py:class:`~COVERAGE_GRID_CLASS`
              - Classes of objects that can be used as templates to associate access constraints, basic object properties and, in some cases, altitude with points in the grid.

            * - :py:class:`~COVERAGE_ALTITUDE_METHOD`
              - Method for specifying the altitude of a grid point.

            * - :py:class:`~COVERAGE_GROUND_ALTITUDE_METHOD`
              - Method for specifying the ground altitude of a grid point.

            * - :py:class:`~COVERAGE_DATA_RETENTION`
              - Data retention options.

            * - :py:class:`~COVERAGE_REGION_ACCESS_ACCEL`
              - Regional acceleration options.

            * - :py:class:`~COVERAGE_RESOLUTION`
              - Coverage grid resolution options: values of the enumeration represent polymorphic object types.

            * - :py:class:`~COVERAGE_ASSET_STATUS`
              - Coverage asset status.

            * - :py:class:`~COVERAGE_ASSET_GROUPING`
              - Coverage asset grouping options.

            * - :py:class:`~FIGURE_OF_MERIT_DEFINITION_TYPE`
              - Figure of Merit types: values of the enumeration represent polymorphic object types.

            * - :py:class:`~FIGURE_OF_MERIT_SATISFACTION_TYPE`
              - Satisfaction options: determine whether satisfaction is achieved based on the value of the figure of merit.

            * - :py:class:`~FIGURE_OF_MERIT_CONSTRAINT_NAME`
              - Available constraints to use for the Access Constraint Figure of Merit.

            * - :py:class:`~FIGURE_OF_MERIT_COMPUTE`
              - Figure of Merit compute options.

            * - :py:class:`~FIGURE_OF_MERIT_ACROSS_ASSETS`
              - Across Assets options: specify which value of the constraint is to be selected based on all currently available assets.

            * - :py:class:`~FIGURE_OF_MERIT_COMPUTE_TYPE`
              - Allowed number of assets for the navigation solution.

            * - :py:class:`~FIGURE_OF_MERIT_METHOD`
              - Dilution of Precision method.

            * - :py:class:`~FIGURE_OF_MERIT_END_GAP_OPTION`
              - End gap options: control consideration of gaps at ends of analysis intervals.

            * - :py:class:`~FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE`
              - Contour fill options.

            * - :py:class:`~FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD`
              - Methods for assigning colors to contour levels.

            * - :py:class:`~FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT`
              - Format options for floating point numbers.

            * - :py:class:`~FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION`
              - Level order display options for the contour legend.

            * - :py:class:`~FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION`
              - Accumulation options: control the sense and persistence of animation graphics for a Figure of Merit.

            * - :py:class:`~FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE`
              - Options for uncertainty in one-way range measurements for the Navigation Accuracy Figure of Merit.

            * - :py:class:`~IV_CLOCK_HOST`
              - Clock host options for access. Time values are reported with a clock colocated with the clock host object.

            * - :py:class:`~IV_TIME_SENSE`
              - Mode of signal transmission of the designated clock host.

            * - :py:class:`~GPS_ATTITUDE_MODEL_TYPE`
              - GPS attitude profile model types.

            * - :py:class:`~CONSTELLATION_CONSTRAINT_RESTRICTION`
              - The values of the enumeration are used to define constellation constraints that allow you to specify the criteria to be used when constellations are combined with other objects in a chain.

            * - :py:class:`~EVENT_DETECTION`
              - Available event detection strategies.

            * - :py:class:`~SAMPLING_METHOD`
              - Available sampling methods.

            * - :py:class:`~COVERAGE_SATISFACTION_TYPE`
              - The condition on the number of assets covering a grid point that must be satisfied for a valid access.

            * - :py:class:`~CCSDS_REFERENCE_FRAME`
              - Reference Frame.

            * - :py:class:`~CCSDS_DATE_FORMAT`
              - The date format of the file.

            * - :py:class:`~CCSDS_EPHEM_FORMAT`
              - The ephemeris format of the file.

            * - :py:class:`~CCSDS_TIME_SYSTEM`
              - Time System.

            * - :py:class:`~STK_EPHEM_COORDINATE_SYSTEM`
              - The Coordinate System of the file.

            * - :py:class:`~STK_EPHEM_COVARIANCE_TYPE`
              - The covariance data export type.

            * - :py:class:`~EXPORT_TOOL_VERSION_FORMAT`
              - The version format of the file.

            * - :py:class:`~EXPORT_TOOL_TIME_PERIOD`
              - Values of the enumeration represent polymorphic object types.

            * - :py:class:`~SPICE_INTERPOLATION`
              - The SPICE interpolation type.

            * - :py:class:`~ATTITUDE_COORDINATE_AXES`
              - Attitude export options.

            * - :py:class:`~ATTITUDE_INCLUDE`
              - Details to include in an exported Attitude file.

            * - :py:class:`~EXPORT_TOOL_STEP_SIZE`
              - The Step Size type for an attitude file.

            * - :py:class:`~TEXT_OUTLINE_STYLE`
              - The text outline style for 2D graphics display.

            * - :py:class:`~MTO_RANGE_MODE`
              - MTO Range Mode.

            * - :py:class:`~MTO_TRACK_EVAL`
              - MTO Track Eval Mode.

            * - :py:class:`~MTO_ENTIRETY`
              - MTO Entirety Mode.

            * - :py:class:`~MTO_VISIBILITY_MODE`
              - MTO Visibility Mode.

            * - :py:class:`~MTO_OBJECT_INTERVAL`
              - MTO object interval type.

            * - :py:class:`~MTO_INPUT_DATA_TYPE`
              - MTO Input Data Type.

            * - :py:class:`~SOLID_TIDE`
              - The Solid Tide Type for force modeling.

            * - :py:class:`~TIME_PERIOD_VALUE_TYPE`
              - Time value types.

            * - :py:class:`~ONE_POINT_ACCESS_STATUS`
              - One point access status.

            * - :py:class:`~ONE_POINT_ACCESS_SUMMARY`
              - One point access summary type.

            * - :py:class:`~LOOK_AHEAD_PROPAGATOR`
              - Propagators used for calculating ephemeris for look ahead purposes. The enumeration is used with realtime propagators.

            * - :py:class:`~GRAPHICS_3D_MARKER_ORIENTATION`
              - 3D graphics marker orientations.

            * - :py:class:`~SRP_MODEL`
              - Solar radiation pressure model types.

            * - :py:class:`~DRAG_MODEL`
              - Drag model types.

            * - :py:class:`~VEHICLE_PROPAGATION_FRAME`
              - Propagation frames used by J2/J4/TwoBody propagators.

            * - :py:class:`~STAR_REFERENCE_FRAME`
              - Star reference frame types.

            * - :py:class:`~GPS_REFERENCE_WEEK`
              - GPS almanac reference week.

            * - :py:class:`~COVERAGE_CUSTOM_REGION_ALGORITHM`
              - The enumerations are used to enable/disable the special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).

            * - :py:class:`~VEHICLE_GPS_SWITCH_METHOD`
              - GPS Switch method for the GPS propagator.

            * - :py:class:`~VEHICLE_GPS_ELEM_SELECTION`
              - GPS Selection method for the GPS propagator.

            * - :py:class:`~VEHICLE_GPS_AUTO_UPDATE_SOURCE`
              - The sources to retrieve GPS elements from upon propagation.

            * - :py:class:`~VEHICLE_GPS_ALMANAC_TYPE`
              - GPS Almanac types.

            * - :py:class:`~STK_EXTERNAL_EPHEMERIS_FORMAT`
              - Ephemeris file formats supported by the Stk external propagator.

            * - :py:class:`~STK_EXTERNAL_FILE_MESSAGE_LEVEL`
              - Ephemeris file message level used by the Stk external propagator.

            * - :py:class:`~COVERAGE_3D_DRAW_AT_ALTITUDE_MODE`
              - Coverage definition drawing modes for filled graphics when showing at altitude in 3D Graphics window.

            * - :py:class:`~DISTANCE_ON_SPHERE`
              - Type of line which connects the two points.

            * - :py:class:`~FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE`
              - Invalid Value Action: Controls consideration of time samples usage for computing navigation solution when insufficient number of assets are available at one or more of the time samples used.

            * - :py:class:`~VEHICLE_SLEW_TIMING_BETWEEN_TARGETS`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

            * - :py:class:`~VEHICLE_SLEW_MODE`
              - Target slew modes.

            * - :py:class:`~COMPONENT`
              - The different types of components in the component browser.

            * - :py:class:`~VM_DEFINITION_TYPE`
              - Volume grid definition types.

            * - :py:class:`~VM_SPATIAL_CALC_EVAL_TYPE`
              - Evaluation of Spatial Calculation types.

            * - :py:class:`~VM_SAVE_COMPUTED_DATA_TYPE`
              - Save Computed Data types.

            * - :py:class:`~VM_DISPLAY_VOLUME_TYPE`
              - Graphics volume display type.

            * - :py:class:`~VM_DISPLAY_QUALITY_TYPE`
              - Quality of the graphics display types.

            * - :py:class:`~VM_LEGEND_NUMERIC_NOTATION`
              - Legend numeric notation types.

            * - :py:class:`~VM_LEVEL_ORDER`
              - Legend level display order.

            * - :py:class:`~SENSOR_EOIR_PROCESSING_LEVELS`
              - EOIR processing levels.

            * - :py:class:`~SENSOR_EOIR_JITTER_TYPES`
              - EOIR jitter type.

            * - :py:class:`~SENSOR_EOIR_SCAN_MODES`
              - EOIR sensor scan mode.

            * - :py:class:`~SENSOR_EOIR_BAND_IMAGE_QUALITY`
              - EOIR band image quality levels.

            * - :py:class:`~SENSOR_EOIR_BAND_SPECTRAL_SHAPE`
              - EOIR overall system spectral shape determination.

            * - :py:class:`~SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE`
              - EOIR spatial input parameter specification.

            * - :py:class:`~SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS`
              - EOIR spectral relative system response units specification.

            * - :py:class:`~SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE`
              - EOIR optical input parameter specification.

            * - :py:class:`~SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE`
              - EOIR optical transmission parameter specification mode.

            * - :py:class:`~SENSOR_EOIR_BAND_RAD_PARAM_LEVEL`
              - EOIR radiometric detector parameter level of specification.

            * - :py:class:`~SENSOR_EOIR_BAND_QE_MODE`
              - EOIR quantum efficiency specification mode.

            * - :py:class:`~SENSOR_EOIR_BAND_QUANTIZATION_MODE`
              - EOIR mode of determining quantization step size.

            * - :py:class:`~SENSOR_EOIR_BAND_WAVELENGTH_TYPE`
              - EOIR band diffraction wavelength reference type.

            * - :py:class:`~SENSOR_EOIR_BAND_SATURATION_MODE`
              - EOIR band irradiance or radiance reference mode.

            * - :py:class:`~VM_VOLUME_GRID_EXPORT_TYPE`
              - Volumetric data export types.

            * - :py:class:`~VM_DATA_EXPORT_FORMAT_TYPE`
              - Volumetric data export format types.

            * - :py:class:`~CONSTELLATION_FROM_TO_PARENT_CONSTRAINT`
              - Options for a chain's From and To Parent Constraints.

            * - :py:class:`~ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS`
              - Available Analysis Workbench Access Constraints.

            * - :py:class:`~STATISTICS`
              - The different statistics that might be available for a data set.

            * - :py:class:`~TIME_VARYING_EXTREMUM`
              - The different time varying extremum that might be available for a data set.

            * - :py:class:`~MODEL_GLTF_REFLECTION_MAP_TYPE`
              - Settings for glTF Reflection.

            * - :py:class:`~SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE`
              - The different ways to determine the sensor's space projection distance in the 3D window.

            * - :py:class:`~LOP_ATMOSPHERIC_DENSITY_MODEL`
              - LOP Atmospheric density models.

            * - :py:class:`~LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL`
              - Low Altitude Atmospheric density models.

            * - :py:class:`~EPHEM_EXPORT_TOOL_FILE_FORMAT`
              - Ephemeris Export Tool file formats.

            * - :py:class:`~ADV_CAT_ELLIPSOID_CLASS`
              - Method for determining Ellipsoid Sizing method (class).

            * - :py:class:`~ADV_CAT_CONJUNCTION_TYPE`
              - Mode for computing events involving conjunction TCA.

            * - :py:class:`~ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE`
              - Type of visible Secondary Ellipsoids.

            * - :py:class:`~EOIR_SHAPE_TYPE`
              - The object geometry which will be rendered in the synthetic scene window.

            * - :py:class:`~EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE`
              - Designation of how material properties are specified.

            * - :py:class:`~EOIR_THERMAL_MODEL_TYPE`
              - EOIR thermal models.

            * - :py:class:`~EOIR_FLIGHT_TYPE`
              - EOIR Flight Types.

            * - :py:class:`~COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE`
              - Component link/embed control reference type.

            * - :py:class:`~SWATH_COMPUTATIONAL_METHOD`
              - Computationals methods for generating swaths.

            * - :py:class:`~CLASSICAL_LOCATION`
              - Classical (Keplerian) element used to specify the spacecraft's location within its orbit at epoch.

            * - :py:class:`~ORIENTATION_ASC_NODE`
              - Ascending node-related options for use in specifying orbit orientation.

            * - :py:class:`~GEODETIC_SIZE`
              - Size options for the Geodetic coordinate type.

            * - :py:class:`~DELAUNAY_L_TYPE`
              - Select whether to use the default representation of Delaunay L or L/SQRT(mu).

            * - :py:class:`~DELAUNAY_H_TYPE`
              - Select whether to use the default representation of Delaunay H or H/SQRT(mu).

            * - :py:class:`~DELAUNAY_G_TYPE`
              - Select whether to use the default representation of Delaunay G or G/SQRT(mu).

            * - :py:class:`~EQUINOCTIAL_SIZE_SHAPE`
              - Opt whether to use Mean Motion or Semimajor Axis to specify the orbit size (Equinoctial coordinate type).

            * - :py:class:`~MIXED_SPHERICAL_FPA`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~SPHERICAL_FPA`
              - Opt whether to use Horizontal or Vertical Flight Path Angle.

            * - :py:class:`~CLASSICAL_SIZE_SHAPE`
              - Pairs of Classical (Keplerian) elements used to specify orbit size and shape.

            * - :py:class:`~EQUINOCTIAL_FORMULATION`
              - Formulation: retrograde or posigrade.

            * - :py:class:`~SCATTERING_POINT_PROVIDER_TYPE`
              - Scattering point provider type.

            * - :py:class:`~SCATTERING_POINT_MODEL_TYPE`
              - Scattering point model type.

            * - :py:class:`~SCATTERING_POINT_PROVIDER_LIST_TYPE`
              - Scattering Point Provider List Type.

            * - :py:class:`~POLARIZATION_TYPE`
              - Polarization Type.

            * - :py:class:`~POLARIZATION_REFERENCE_AXIS`
              - Polarization reference axis.

            * - :py:class:`~NOISE_TEMP_COMPUTE_TYPE`
              - System noise temperature compute type.

            * - :py:class:`~POINTING_STRATEGY_TYPE`
              - Pointing strategy type.

            * - :py:class:`~WAVEFORM_TYPE`
              - Waveform types.

            * - :py:class:`~FREQUENCY_SPEC`
              - Frequency Specification Type.

            * - :py:class:`~PRF_MODE`
              - Radar search/track prf modes.

            * - :py:class:`~PULSE_WIDTH_MODE`
              - Radar search/track pulse width modes.

            * - :py:class:`~WAVEFORM_SELECTION_STRATEGY_TYPE`
              - Waveform selection strategy type.

            * - :py:class:`~ANTENNA_CONTROL_REFERENCE_TYPE`
              - Antenna control reference type.

            * - :py:class:`~ANTENNA_MODEL_TYPE`
              - Antenna model types.

            * - :py:class:`~ANTENNA_CONTOUR_TYPE`
              - Antenna contour types.

            * - :py:class:`~CIRCULAR_APERTURE_INPUT_TYPE`
              - Circular aperture antenna input type.

            * - :py:class:`~RECTANGULAR_APERTURE_INPUT_TYPE`
              - Rectangular aperture antenna input type.

            * - :py:class:`~DIRECTION_PROVIDER_TYPE`
              - Direction Provider types.

            * - :py:class:`~BEAMFORMER_TYPE`
              - Beamformer types.

            * - :py:class:`~ELEMENT_CONFIGURATION_TYPE`
              - Element configuration types.

            * - :py:class:`~LATTICE_TYPE`
              - Lattice types.

            * - :py:class:`~SPACING_UNIT`
              - Spacing Units.

            * - :py:class:`~LIMITS_EXCEEDED_BEHAVIOR_TYPE`
              - Limits Exceeded Behavior types.

            * - :py:class:`~ANTENNA_GRAPHICS_COORDINATE_SYSTEM`
              - Coordinate system for defining antenna graphics resolution.

            * - :py:class:`~ANTENNA_MODEL_INPUT_TYPE`
              - Diameter computation input type.

            * - :py:class:`~HFSS_FFD_GAIN_TYPE`
              - Gain type.

            * - :py:class:`~ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE`
              - Cosecant Squared antenna sidelobe selection types.

            * - :py:class:`~BEAM_SELECTION_STRATEGY_TYPE`
              - Beam selection strategy types.

            * - :py:class:`~TRANSMITTER_MODEL_TYPE`
              - Transmitter model types.

            * - :py:class:`~TRANSFER_FUNCTION_TYPE`
              - Transmitter model types.

            * - :py:class:`~RE_TRANSMITTER_OP_MODE`
              - Re-Transmitter operational mode.

            * - :py:class:`~RECEIVER_MODEL_TYPE`
              - Receiver model types.

            * - :py:class:`~LINK_MARGIN_TYPE`
              - Link margin types.

            * - :py:class:`~RADAR_STC_ATTENUATION_TYPE`
              - Stc Attenuation Type.

            * - :py:class:`~RADAR_FREQUENCY_SPEC`
              - SNR Contour Type.

            * - :py:class:`~RADAR_SNR_CONTOUR_TYPE`
              - SNR Contour Type.

            * - :py:class:`~RADAR_MODEL_TYPE`
              - Radar system types.

            * - :py:class:`~RADAR_MODE_TYPE`
              - Radar mode types.

            * - :py:class:`~RADAR_WAVEFORM_SEARCH_TRACK_TYPE`
              - Radar search/track waveform types.

            * - :py:class:`~RADAR_SEARCH_TRACK_PRF_MODE`
              - Radar search/track prf modes.

            * - :py:class:`~RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE`
              - Radar search/track pulse width modes.

            * - :py:class:`~RADAR_SAR_PRF_MODE`
              - Radar SAR prf modes.

            * - :py:class:`~RADAR_SAR_RANGE_RESOLUTION_MODE`
              - Radar SAR range resolution modes.

            * - :py:class:`~RADAR_SAR_PCR_MODE`
              - Radar SAR pulse compression ratio modes.

            * - :py:class:`~RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE`
              - Radar sar pulse integration mode.

            * - :py:class:`~RADAR_P_DET_TYPE`
              - Radar probability of detection type.

            * - :py:class:`~RADAR_PULSE_INTEGRATION_TYPE`
              - Radar pulse integration type.

            * - :py:class:`~RADAR_PULSE_INTEGRATOR_TYPE`
              - Radar pulse integrator type.

            * - :py:class:`~RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE`
              - Radar continuous wave analysis mode.

            * - :py:class:`~RADAR_CLUTTER_GEOMETRY_MODEL_TYPE`
              - Radar clutter geometry model type.

            * - :py:class:`~RADAR_CLUTTER_MAP_MODEL_TYPE`
              - Radar clutter map model type.

            * - :py:class:`~RADAR_SWERLING_CASE`
              - Radar swerling case.

            * - :py:class:`~RCS_COMPUTE_STRATEGY`
              - Radar cross section compute strategy.

            * - :py:class:`~RADAR_ACTIVITY_TYPE`
              - Radar activity times strategy.

            * - :py:class:`~RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION`
              - Radar cross section contour graphics polarization.

            * - :py:class:`~RF_FILTER_MODEL_TYPE`
              - RF filter model types.

            * - :py:class:`~MODULATOR_MODEL_TYPE`
              - Modulator model types.

            * - :py:class:`~DEMODULATOR_MODEL_TYPE`
              - Demodulator model types.

            * - :py:class:`~RAIN_LOSS_MODEL_TYPE`
              - Rain loss model types.

            * - :py:class:`~ATMOSPHERIC_ABSORPTION_MODEL_TYPE`
              - Atmospheric absorption model types.

            * - :py:class:`~URBAN_TERRESTRIAL_LOSS_MODEL_TYPE`
              - urban/terrestrial loss model types.

            * - :py:class:`~CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE`
              - Clouds and Fog loss model types.

            * - :py:class:`~CLOUDS_AND_FOG_LIQUID_WATER_CHOICES`
              - Clouds and Fog loss model liquid water content choices.

            * - :py:class:`~IONOSPHERIC_FADING_LOSS_MODEL_TYPE`
              - Ionospheric loss model types.

            * - :py:class:`~TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE`
              - TropoScintillation loss model types.

            * - :py:class:`~TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES`
              - TroposphericScintillation loss model average time choices.

            * - :py:class:`~PROJECTION_HORIZONTAL_DATUM_TYPE`
              - REMCOM Wireless InSite RT project/horizontal datum type.

            * - :py:class:`~BUILD_HEIGHT_REFERENCE_METHOD`
              - REMCOM Wireless InSite RT building height reference method.

            * - :py:class:`~BUILD_HEIGHT_UNIT`
              - REMCOM Wireless InSite RT building height unit.

            * - :py:class:`~TIREM_POLARIZATION_TYPE`
              - TIREM polarization type.

            * - :py:class:`~VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE`
              - VOACAP solar activity configuration type.

            * - :py:class:`~VOACAP_COEFFICIENT_DATA_TYPE`
              - VOACAP coefficient data type.

            * - :py:class:`~LASER_PROPAGATION_LOSS_MODEL_TYPE`
              - Laser propagation loss model types.

            * - :py:class:`~LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE`
              - Laser tropospheric scintillation loss model types.

            * - :py:class:`~ATMOSPHERIC_TURBULENCE_MODEL_TYPE`
              - Refractive index structure parameter model types.

            * - :py:class:`~MODTRAN_AEROSOL_MODEL_TYPE`
              - MODTRAN-derived lookup table aerosol model extinction types.

            * - :py:class:`~MODTRAN_CLOUD_MODEL_TYPE`
              - MODTRAN Cloud model types.

            * - :py:class:`~COMM_SYSTEM_REFERENCE_BANDWIDTH`
              - CommSystem reference bandwidth.

            * - :py:class:`~COMM_SYSTEM_CONSTRAINING_ROLE`
              - CommSystem constraining role.

            * - :py:class:`~COMM_SYSTEM_SAVE_MODE`
              - CommSystem save mode.

            * - :py:class:`~COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE`
              - CommSystem access options event detection type.

            * - :py:class:`~COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE`
              - CommSystem access options sampling method type.

            * - :py:class:`~COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE`
              - Link selection strategy types.

            * - :py:class:`~SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY`
              - Activity level for the NASA models NASAELE and NASAPRO.

            * - :py:class:`~SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY`
              - Activity level for CRRESPRO model.

            * - :py:class:`~SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY`
              - Activity level for CRRESRAD model.

            * - :py:class:`~SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE`
              - Mode by which color is assigned.

            * - :py:class:`~SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE`
              - Scaling of magnetic field to use when assigning color/translucency.

            * - :py:class:`~SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD`
              - Main magnetic field.

            * - :py:class:`~SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD`
              - External magnetic field.

            * - :py:class:`~SPACE_ENVIRONMENT_SAA_CHANNEL`
              - Energy level for SAA protons.

            * - :py:class:`~SPACE_ENVIRONMENT_SAA_FLUX_LEVEL`
              - Flux level for SAA contour.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL`
              - Thermal shape model.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE`
              - Mode for computing 13-month average F10.7.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_MATERIAL`
              - Material.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE`
              - Models that are to be included when modeling radiation.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL`
              - Dose channel.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY`
              - Detector geometry.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE`
              - Detector material.

            * - :py:class:`~VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE`
              - Mode for computing 15 day average Ap.

            * - :py:class:`~NOTIFICATION_FILTER_MASK`
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

     IDataProviderResult<stkobjects/IDataProviderResult>
     IDataProviderTimeVarying<stkobjects/IDataProviderTimeVarying>
     IDataProviderInterval<stkobjects/IDataProviderInterval>
     IDataProviderFixed<stkobjects/IDataProviderFixed>
     IDataProviderResultStatistics<stkobjects/IDataProviderResultStatistics>
     IDataProviderInfo<stkobjects/IDataProviderInfo>
     IDataProviderCollection<stkobjects/IDataProviderCollection>
     IDataProviderResultDataSet<stkobjects/IDataProviderResultDataSet>
     IDataProviderResultDataSetCollection<stkobjects/IDataProviderResultDataSetCollection>
     IDataProviderResultInterval<stkobjects/IDataProviderResultInterval>
     IDataProviderResultIntervalCollection<stkobjects/IDataProviderResultIntervalCollection>
     IDataProviderResultSubSection<stkobjects/IDataProviderResultSubSection>
     IDataProviderResultSubSectionCollection<stkobjects/IDataProviderResultSubSectionCollection>
     IDataProviderResultTextMessage<stkobjects/IDataProviderResultTextMessage>
     IDataProviderElement<stkobjects/IDataProviderElement>
     IDataProviderElements<stkobjects/IDataProviderElements>
     IDataProviderResultTimeArrayElements<stkobjects/IDataProviderResultTimeArrayElements>
     IDataProvider<stkobjects/IDataProvider>
     IDataProviders<stkobjects/IDataProviders>
     IDataProviderGroup<stkobjects/IDataProviderGroup>
     IDataProviderResultStatisticResult<stkobjects/IDataProviderResultStatisticResult>
     IDataProviderResultTimeVaryingExtremumResult<stkobjects/IDataProviderResultTimeVaryingExtremumResult>
     IGraphics3DDataDisplayCollection<stkobjects/IGraphics3DDataDisplayCollection>
     IIntervalCollection<stkobjects/IIntervalCollection>
     ITimePeriodValue<stkobjects/ITimePeriodValue>
     IStkObject<stkobjects/IStkObject>
     IAccessInterval<stkobjects/IAccessInterval>
     IAccessTimeEventIntervals<stkobjects/IAccessTimeEventIntervals>
     IAccessTimePeriod<stkobjects/IAccessTimePeriod>
     IStkAccessGraphics<stkobjects/IStkAccessGraphics>
     IStkAccessAdvanced<stkobjects/IStkAccessAdvanced>
     IStkAccess<stkobjects/IStkAccess>
     IAccessConstraintCollection<stkobjects/IAccessConstraintCollection>
     IImmutableIntervalCollection<stkobjects/IImmutableIntervalCollection>
     IFigureOfMeritDefinition<stkobjects/IFigureOfMeritDefinition>
     IFigureOfMeritDefinitionCompute<stkobjects/IFigureOfMeritDefinitionCompute>
     IFigureOfMeritDefinitionAccessConstraint<stkobjects/IFigureOfMeritDefinitionAccessConstraint>
     IFigureOfMeritGraphics<stkobjects/IFigureOfMeritGraphics>
     ICoverageAssetListCollection<stkobjects/ICoverageAssetListCollection>
     IAvailableFeatures<stkobjects/IAvailableFeatures>
     IStkCentralBodyCollection<stkobjects/IStkCentralBodyCollection>
     IStkPreferences<stkobjects/IStkPreferences>
     IOnePointAccessConstraint<stkobjects/IOnePointAccessConstraint>
     IOnePointAccessConstraintCollection<stkobjects/IOnePointAccessConstraintCollection>
     IOnePointAccessResult<stkobjects/IOnePointAccessResult>
     IOnePointAccessResultCollection<stkobjects/IOnePointAccessResultCollection>
     IOnePointAccess<stkobjects/IOnePointAccess>
     IKeyValueCollection<stkobjects/IKeyValueCollection>
     IStkObjectElementCollection<stkobjects/IStkObjectElementCollection>
     IStkObjectCollection<stkobjects/IStkObjectCollection>
     IObjectCoverageFigureOfMerit<stkobjects/IObjectCoverageFigureOfMerit>
     IStkObjectCoverage<stkobjects/IStkObjectCoverage>
     IStdMilitary2525bSymbols<stkobjects/IStdMilitary2525bSymbols>
     IStkObjectRoot<stkobjects/IStkObjectRoot>
     IObjectLink<stkobjects/IObjectLink>
     ILinkToObject<stkobjects/ILinkToObject>
     IObjectLinkCollection<stkobjects/IObjectLinkCollection>
     IAnimation<stkobjects/IAnimation>
     IStkObjectModelContext<stkobjects/IStkObjectModelContext>
     IComponentInfo<stkobjects/IComponentInfo>
     IComponentInfoCollection<stkobjects/IComponentInfoCollection>
     IComponentDirectory<stkobjects/IComponentDirectory>
     ICloneable<stkobjects/ICloneable>
     IComponentLinkEmbedControl<stkobjects/IComponentLinkEmbedControl>
     ISwath<stkobjects/ISwath>
     IDisplayTimesData<stkobjects/IDisplayTimesData>
     IDisplayTime<stkobjects/IDisplayTime>
     IBasicAzElMask<stkobjects/IBasicAzElMask>
     ILabelNote<stkobjects/ILabelNote>
     ILabelNoteCollection<stkobjects/ILabelNoteCollection>
     IDuringAccess<stkobjects/IDuringAccess>
     IDisplayTimesTimeComponent<stkobjects/IDisplayTimesTimeComponent>
     ITerrainNormSlopeAzimuth<stkobjects/ITerrainNormSlopeAzimuth>
     IAccessTime<stkobjects/IAccessTime>
     IAccessTimeCollection<stkobjects/IAccessTimeCollection>
     ITerrainNormData<stkobjects/ITerrainNormData>
     ILifetimeInformation<stkobjects/ILifetimeInformation>
     IVehicleLeadTrailData<stkobjects/IVehicleLeadTrailData>
     IVehicleLeadTrailDataFraction<stkobjects/IVehicleLeadTrailDataFraction>
     IVehicleLeadTrailDataTime<stkobjects/IVehicleLeadTrailDataTime>
     IStkCentralBodyEllipsoid<stkobjects/IStkCentralBodyEllipsoid>
     IStkCentralBody<stkobjects/IStkCentralBody>
     IAccessConstraint<stkobjects/IAccessConstraint>
     IAccessConstraintTimeSlipRange<stkobjects/IAccessConstraintTimeSlipRange>
     IAccessConstraintZone<stkobjects/IAccessConstraintZone>
     IAccessConstraintExclZonesCollection<stkobjects/IAccessConstraintExclZonesCollection>
     IAccessConstraintThirdBody<stkobjects/IAccessConstraintThirdBody>
     IAccessConstraintIntervals<stkobjects/IAccessConstraintIntervals>
     IAccessConstraintObjExAngle<stkobjects/IAccessConstraintObjExAngle>
     IAccessConstraintCondition<stkobjects/IAccessConstraintCondition>
     IAccessConstraintCentralBodyObstruction<stkobjects/IAccessConstraintCentralBodyObstruction>
     IAccessConstraintAngle<stkobjects/IAccessConstraintAngle>
     IAccessConstraintMinMax<stkobjects/IAccessConstraintMinMax>
     IAccessConstraintPluginMinMax<stkobjects/IAccessConstraintPluginMinMax>
     IAccessConstraintCrdnConstellation<stkobjects/IAccessConstraintCrdnConstellation>
     IAccessConstraintBackground<stkobjects/IAccessConstraintBackground>
     IAccessConstraintGroundTrack<stkobjects/IAccessConstraintGroundTrack>
     IAccessConstraintAnalysisWorkbench<stkobjects/IAccessConstraintAnalysisWorkbench>
     IAccessConstraintAnalysisWorkbenchCollection<stkobjects/IAccessConstraintAnalysisWorkbenchCollection>
     IAccessConstraintGrazingAltitude<stkobjects/IAccessConstraintGrazingAltitude>
     ILevelAttribute<stkobjects/ILevelAttribute>
     ILevelAttributeCollection<stkobjects/ILevelAttributeCollection>
     IGraphics2DRangeContours<stkobjects/IGraphics2DRangeContours>
     IGraphics3DModelFile<stkobjects/IGraphics3DModelFile>
     IGraphics3DArticulationFile<stkobjects/IGraphics3DArticulationFile>
     IGraphics3DModelGltfImageBased<stkobjects/IGraphics3DModelGltfImageBased>
     IVehicleEllipseDataElement<stkobjects/IVehicleEllipseDataElement>
     IVehicleEllipseDataCollection<stkobjects/IVehicleEllipseDataCollection>
     IVehicleGroundEllipseElement<stkobjects/IVehicleGroundEllipseElement>
     IVehicleGroundEllipsesCollection<stkobjects/IVehicleGroundEllipsesCollection>
     IGraphics3DDataDisplayElement<stkobjects/IGraphics3DDataDisplayElement>
     IGraphics3DPointableElementsElement<stkobjects/IGraphics3DPointableElementsElement>
     IGraphics3DPointableElementsCollection<stkobjects/IGraphics3DPointableElementsCollection>
     IGraphics3DModelPointing<stkobjects/IGraphics3DModelPointing>
     IGraphics3DLabelSwapDistance<stkobjects/IGraphics3DLabelSwapDistance>
     IGraphics3DAzElMask<stkobjects/IGraphics3DAzElMask>
     IGraphics3DBorderWall<stkobjects/IGraphics3DBorderWall>
     IGraphics3DRangeContours<stkobjects/IGraphics3DRangeContours>
     IGraphics3DOffsetLabel<stkobjects/IGraphics3DOffsetLabel>
     IGraphics3DOffsetRotate<stkobjects/IGraphics3DOffsetRotate>
     IGraphics3DOffsetTransformation<stkobjects/IGraphics3DOffsetTransformation>
     IGraphics3DOffsetAttach<stkobjects/IGraphics3DOffsetAttach>
     IGraphics3DOffset<stkobjects/IGraphics3DOffset>
     IGraphics3DMarkerData<stkobjects/IGraphics3DMarkerData>
     IGraphics3DMarkerShape<stkobjects/IGraphics3DMarkerShape>
     IGraphics3DMarkerFile<stkobjects/IGraphics3DMarkerFile>
     IGraphics3DMarker<stkobjects/IGraphics3DMarker>
     IGraphics3DModelTransformation<stkobjects/IGraphics3DModelTransformation>
     IGraphics3DModelTransformationCollection<stkobjects/IGraphics3DModelTransformationCollection>
     IGraphics3DModelArtic<stkobjects/IGraphics3DModelArtic>
     IGraphics3DDetailThreshold<stkobjects/IGraphics3DDetailThreshold>
     IGraphics3DModelItem<stkobjects/IGraphics3DModelItem>
     IGraphics3DModelCollection<stkobjects/IGraphics3DModelCollection>
     IGraphics3DModelData<stkobjects/IGraphics3DModelData>
     IGraphics3DModel<stkobjects/IGraphics3DModel>
     IPointTargetGraphics3DModel<stkobjects/IPointTargetGraphics3DModel>
     IGraphics3DReferenceAnalysisWorkbenchComponent<stkobjects/IGraphics3DReferenceAnalysisWorkbenchComponent>
     IGraphics3DReferenceVectorGeometryToolVector<stkobjects/IGraphics3DReferenceVectorGeometryToolVector>
     IGraphics3DReferenceVectorGeometryToolAxes<stkobjects/IGraphics3DReferenceVectorGeometryToolAxes>
     IGraphics3DReferenceVectorGeometryToolAngle<stkobjects/IGraphics3DReferenceVectorGeometryToolAngle>
     IGraphics3DReferenceVectorGeometryToolPoint<stkobjects/IGraphics3DReferenceVectorGeometryToolPoint>
     IGraphics3DReferenceVectorGeometryToolPlane<stkobjects/IGraphics3DReferenceVectorGeometryToolPlane>
     IGraphics3DReferenceAnalysisWorkbenchCollection<stkobjects/IGraphics3DReferenceAnalysisWorkbenchCollection>
     IGraphics3DVector<stkobjects/IGraphics3DVector>
     IGraphics3DVaporTrail<stkobjects/IGraphics3DVaporTrail>
     ILLAPosition<stkobjects/ILLAPosition>
     ILLAGeocentric<stkobjects/ILLAGeocentric>
     ILLAGeodetic<stkobjects/ILLAGeodetic>
     IOrbitStateCoordinateSystem<stkobjects/IOrbitStateCoordinateSystem>
     IOrbitStateCartesian<stkobjects/IOrbitStateCartesian>
     IClassicalSizeShape<stkobjects/IClassicalSizeShape>
     IClassicalSizeShapeAltitude<stkobjects/IClassicalSizeShapeAltitude>
     IClassicalSizeShapeMeanMotion<stkobjects/IClassicalSizeShapeMeanMotion>
     IClassicalSizeShapePeriod<stkobjects/IClassicalSizeShapePeriod>
     IClassicalSizeShapeRadius<stkobjects/IClassicalSizeShapeRadius>
     IClassicalSizeShapeSemimajorAxis<stkobjects/IClassicalSizeShapeSemimajorAxis>
     IOrientationAscNode<stkobjects/IOrientationAscNode>
     IOrientationAscNodeLAN<stkobjects/IOrientationAscNodeLAN>
     IOrientationAscNodeRAAN<stkobjects/IOrientationAscNodeRAAN>
     IClassicalOrientation<stkobjects/IClassicalOrientation>
     IClassicalLocation<stkobjects/IClassicalLocation>
     IClassicalLocationArgumentOfLatitude<stkobjects/IClassicalLocationArgumentOfLatitude>
     IClassicalLocationEccentricAnomaly<stkobjects/IClassicalLocationEccentricAnomaly>
     IClassicalLocationMeanAnomaly<stkobjects/IClassicalLocationMeanAnomaly>
     IClassicalLocationTimePastAN<stkobjects/IClassicalLocationTimePastAN>
     IClassicalLocationTimePastPerigee<stkobjects/IClassicalLocationTimePastPerigee>
     IClassicalLocationTrueAnomaly<stkobjects/IClassicalLocationTrueAnomaly>
     IOrbitStateClassical<stkobjects/IOrbitStateClassical>
     IGeodeticSize<stkobjects/IGeodeticSize>
     IGeodeticSizeAltitude<stkobjects/IGeodeticSizeAltitude>
     IGeodeticSizeRadius<stkobjects/IGeodeticSizeRadius>
     IOrbitStateGeodetic<stkobjects/IOrbitStateGeodetic>
     IDelaunayActionVariable<stkobjects/IDelaunayActionVariable>
     IDelaunayL<stkobjects/IDelaunayL>
     IDelaunayLOverSQRTmu<stkobjects/IDelaunayLOverSQRTmu>
     IDelaunayH<stkobjects/IDelaunayH>
     IDelaunayHOverSQRTmu<stkobjects/IDelaunayHOverSQRTmu>
     IDelaunayG<stkobjects/IDelaunayG>
     IDelaunayGOverSQRTmu<stkobjects/IDelaunayGOverSQRTmu>
     IOrbitStateDelaunay<stkobjects/IOrbitStateDelaunay>
     IEquinoctialSizeShapeMeanMotion<stkobjects/IEquinoctialSizeShapeMeanMotion>
     IEquinoctialSizeShapeSemimajorAxis<stkobjects/IEquinoctialSizeShapeSemimajorAxis>
     IOrbitStateEquinoctial<stkobjects/IOrbitStateEquinoctial>
     IFlightPathAngle<stkobjects/IFlightPathAngle>
     IMixedSphericalFPAHorizontal<stkobjects/IMixedSphericalFPAHorizontal>
     IMixedSphericalFPAVertical<stkobjects/IMixedSphericalFPAVertical>
     IOrbitStateMixedSpherical<stkobjects/IOrbitStateMixedSpherical>
     ISphericalFPAHorizontal<stkobjects/ISphericalFPAHorizontal>
     ISphericalFPAVertical<stkobjects/ISphericalFPAVertical>
     IOrbitStateSpherical<stkobjects/IOrbitStateSpherical>
     ISpatialState<stkobjects/ISpatialState>
     IVehicleSpatialInfo<stkobjects/IVehicleSpatialInfo>
     IProvideSpatialInfo<stkobjects/IProvideSpatialInfo>
     IScenSpaceEnvironment<stkobjects/IScenSpaceEnvironment>
     IRadarClutterMap<stkobjects/IRadarClutterMap>
     IRadarCrossSection<stkobjects/IRadarCrossSection>
     IRFEnvironment<stkobjects/IRFEnvironment>
     ILaserEnvironment<stkobjects/ILaserEnvironment>
     IScenarioGraphics<stkobjects/IScenarioGraphics>
     IScenarioEarthData<stkobjects/IScenarioEarthData>
     IScenarioAnimationTimePeriod<stkobjects/IScenarioAnimationTimePeriod>
     IScenarioAnimation<stkobjects/IScenarioAnimation>
     ITerrain<stkobjects/ITerrain>
     ITerrainCollection<stkobjects/ITerrainCollection>
     ICentralBodyTerrainCollectionElement<stkobjects/ICentralBodyTerrainCollectionElement>
     ICentralBodyTerrainCollection<stkobjects/ICentralBodyTerrainCollection>
     ITileset3D<stkobjects/ITileset3D>
     ITilesetCollection3D<stkobjects/ITilesetCollection3D>
     IScenarioGenDatabase<stkobjects/IScenarioGenDatabase>
     IScenarioGenDatabaseCollection<stkobjects/IScenarioGenDatabaseCollection>
     IScenario3dFont<stkobjects/IScenario3dFont>
     IScenarioGraphics3D<stkobjects/IScenarioGraphics3D>
     ITimePeriod<stkobjects/ITimePeriod>
     IScenario<stkobjects/IScenario>
     ICelestialBodyInfo<stkobjects/ICelestialBodyInfo>
     ICelestialBodyCollection<stkobjects/ICelestialBodyCollection>
     IAccessAdvanced<stkobjects/IAccessAdvanced>
     ISensorAccessAdvanced<stkobjects/ISensorAccessAdvanced>
     IRefractionCoefficients<stkobjects/IRefractionCoefficients>
     IRefractionModelBase<stkobjects/IRefractionModelBase>
     IRefractionModelEffectiveRadiusMethod<stkobjects/IRefractionModelEffectiveRadiusMethod>
     IRefractionModelITURP8344<stkobjects/IRefractionModelITURP8344>
     IRefractionModelSCFMethod<stkobjects/IRefractionModelSCFMethod>
     IScheduleTime<stkobjects/IScheduleTime>
     IScheduleTimeCollection<stkobjects/IScheduleTimeCollection>
     IDisplayDistance<stkobjects/IDisplayDistance>
     ISensorProjectionDisplayDistance<stkobjects/ISensorProjectionDisplayDistance>
     ISensorProjection<stkobjects/ISensorProjection>
     ISensorGraphics<stkobjects/ISensorGraphics>
     ISensorGraphics3DPulse<stkobjects/ISensorGraphics3DPulse>
     ISensorGraphics3DOffset<stkobjects/ISensorGraphics3DOffset>
     ISensorGraphics3DProjectionElement<stkobjects/ISensorGraphics3DProjectionElement>
     ISensorGraphics3DSpaceProjectionCollection<stkobjects/ISensorGraphics3DSpaceProjectionCollection>
     ISensorGraphics3DTargetProjectionCollection<stkobjects/ISensorGraphics3DTargetProjectionCollection>
     ISensorGraphics3D<stkobjects/ISensorGraphics3D>
     ISensorPattern<stkobjects/ISensorPattern>
     ISensorSimpleConicPattern<stkobjects/ISensorSimpleConicPattern>
     ISensorSARPattern<stkobjects/ISensorSARPattern>
     ISensorRectangularPattern<stkobjects/ISensorRectangularPattern>
     ISensorHalfPowerPattern<stkobjects/ISensorHalfPowerPattern>
     ISensorCustomPattern<stkobjects/ISensorCustomPattern>
     ISensorComplexConicPattern<stkobjects/ISensorComplexConicPattern>
     ISensorEOIRRadiometricPair<stkobjects/ISensorEOIRRadiometricPair>
     ISensorEOIRSensitivityCollection<stkobjects/ISensorEOIRSensitivityCollection>
     ISensorEOIRSaturationCollection<stkobjects/ISensorEOIRSaturationCollection>
     ISensorEOIRBand<stkobjects/ISensorEOIRBand>
     ISensorEOIRBandCollection<stkobjects/ISensorEOIRBandCollection>
     ISensorEOIRPattern<stkobjects/ISensorEOIRPattern>
     ISensorPointingTargetedBoresight<stkobjects/ISensorPointingTargetedBoresight>
     ISensorPointingTargetedBoresightTrack<stkobjects/ISensorPointingTargetedBoresightTrack>
     ISensorPointingTargetedBoresightFixed<stkobjects/ISensorPointingTargetedBoresightFixed>
     ISensorTarget<stkobjects/ISensorTarget>
     ISensorTargetCollection<stkobjects/ISensorTargetCollection>
     ISensorPointing<stkobjects/ISensorPointing>
     ISensorPointingTargeted<stkobjects/ISensorPointingTargeted>
     ISensorPointingSpinning<stkobjects/ISensorPointingSpinning>
     ISensorPointingGrazingAltitude<stkobjects/ISensorPointingGrazingAltitude>
     ISensorPointingFixedAxes<stkobjects/ISensorPointingFixedAxes>
     ISensorPointingFixed<stkobjects/ISensorPointingFixed>
     ISensorPointingExternal<stkobjects/ISensorPointingExternal>
     ISensorPointing3DModel<stkobjects/ISensorPointing3DModel>
     ISensorPointingAlongVector<stkobjects/ISensorPointingAlongVector>
     ISensorPointingSchedule<stkobjects/ISensorPointingSchedule>
     IAzElMaskData<stkobjects/IAzElMaskData>
     ISensorAzElMaskFile<stkobjects/ISensorAzElMaskFile>
     ISensorCommonTasks<stkobjects/ISensorCommonTasks>
     ILocationVectorGeometryToolPoint<stkobjects/ILocationVectorGeometryToolPoint>
     ISensor<stkobjects/ISensor>
     ISensorProjectionConstantAltitude<stkobjects/ISensorProjectionConstantAltitude>
     ISensorProjectionObjectAltitude<stkobjects/ISensorProjectionObjectAltitude>
     IAtmosphere<stkobjects/IAtmosphere>
     IRadarClutterMapInheritable<stkobjects/IRadarClutterMapInheritable>
     IRadarCrossSectionInheritable<stkobjects/IRadarCrossSectionInheritable>
     IPlatformLaserEnvironment<stkobjects/IPlatformLaserEnvironment>
     IPlatformRFEnvironment<stkobjects/IPlatformRFEnvironment>
     IRadarCrossSectionGraphics3D<stkobjects/IRadarCrossSectionGraphics3D>
     IRadarCrossSectionGraphics<stkobjects/IRadarCrossSectionGraphics>
     ITargetGraphics<stkobjects/ITargetGraphics>
     ITargetGraphics3D<stkobjects/ITargetGraphics3D>
     ITarget<stkobjects/ITarget>
     IAreaTypeEllipse<stkobjects/IAreaTypeEllipse>
     IAreaTypePatternCollection<stkobjects/IAreaTypePatternCollection>
     IAreaTargetCommonTasks<stkobjects/IAreaTargetCommonTasks>
     IAreaTypeData<stkobjects/IAreaTypeData>
     IAreaTargetGraphics<stkobjects/IAreaTargetGraphics>
     IAreaTargetGraphics3D<stkobjects/IAreaTargetGraphics3D>
     IAreaTarget<stkobjects/IAreaTarget>
     IAreaTypePattern<stkobjects/IAreaTypePattern>
     IPlanetPositionFile<stkobjects/IPlanetPositionFile>
     IPlanetPositionCentralBody<stkobjects/IPlanetPositionCentralBody>
     IPlanetCommonTasks<stkobjects/IPlanetCommonTasks>
     IPositionSourceData<stkobjects/IPositionSourceData>
     IOrbitDisplayData<stkobjects/IOrbitDisplayData>
     IPlanetOrbitDisplayTime<stkobjects/IPlanetOrbitDisplayTime>
     IPlanetGraphics<stkobjects/IPlanetGraphics>
     IPlanetGraphics3D<stkobjects/IPlanetGraphics3D>
     IPlanet<stkobjects/IPlanet>
     IStarGraphics<stkobjects/IStarGraphics>
     IStarGraphics3D<stkobjects/IStarGraphics3D>
     IStar<stkobjects/IStar>
     IFacilityGraphics<stkobjects/IFacilityGraphics>
     IFacilityGraphics3D<stkobjects/IFacilityGraphics3D>
     IFacility<stkobjects/IFacility>
     IPlaceGraphics<stkobjects/IPlaceGraphics>
     IPlaceGraphics3D<stkobjects/IPlaceGraphics3D>
     IPlace<stkobjects/IPlace>
     IAntennaNoiseTemperature<stkobjects/IAntennaNoiseTemperature>
     ISystemNoiseTemperature<stkobjects/ISystemNoiseTemperature>
     IPolarization<stkobjects/IPolarization>
     IPolarizationElliptical<stkobjects/IPolarizationElliptical>
     IPolarizationCrossPolLeakage<stkobjects/IPolarizationCrossPolLeakage>
     IPolarizationLinear<stkobjects/IPolarizationLinear>
     IPolarizationHorizontal<stkobjects/IPolarizationHorizontal>
     IPolarizationVertical<stkobjects/IPolarizationVertical>
     IAdditionalGainLoss<stkobjects/IAdditionalGainLoss>
     IAdditionalGainLossCollection<stkobjects/IAdditionalGainLossCollection>
     ICRPluginConfiguration<stkobjects/ICRPluginConfiguration>
     ICRComplex<stkobjects/ICRComplex>
     ICRComplexCollection<stkobjects/ICRComplexCollection>
     ICRLocation<stkobjects/ICRLocation>
     IPointingStrategy<stkobjects/IPointingStrategy>
     IPointingStrategyFixed<stkobjects/IPointingStrategyFixed>
     IPointingStrategySpinning<stkobjects/IPointingStrategySpinning>
     IPointingStrategyTargeted<stkobjects/IPointingStrategyTargeted>
     IWaveformPulseDefinition<stkobjects/IWaveformPulseDefinition>
     IWaveform<stkobjects/IWaveform>
     IWaveformRectangular<stkobjects/IWaveformRectangular>
     IWaveformSelectionStrategy<stkobjects/IWaveformSelectionStrategy>
     IWaveformSelectionStrategyFixed<stkobjects/IWaveformSelectionStrategyFixed>
     IWaveformSelectionStrategyRangeLimits<stkobjects/IWaveformSelectionStrategyRangeLimits>
     IRFInterference<stkobjects/IRFInterference>
     IScatteringPointProvider<stkobjects/IScatteringPointProvider>
     IScatteringPointProviderSinglePoint<stkobjects/IScatteringPointProviderSinglePoint>
     IScatteringPointCollectionElement<stkobjects/IScatteringPointCollectionElement>
     IScatteringPointCollection<stkobjects/IScatteringPointCollection>
     IScatteringPointProviderPointsFile<stkobjects/IScatteringPointProviderPointsFile>
     IScatteringPointProviderRangeOverCFARCells<stkobjects/IScatteringPointProviderRangeOverCFARCells>
     IScatteringPointProviderSmoothOblateEarth<stkobjects/IScatteringPointProviderSmoothOblateEarth>
     IScatteringPointProviderPlugin<stkobjects/IScatteringPointProviderPlugin>
     IScatteringPointModel<stkobjects/IScatteringPointModel>
     IScatteringPointModelConstantCoefficient<stkobjects/IScatteringPointModelConstantCoefficient>
     IScatteringPointModelWindTurbine<stkobjects/IScatteringPointModelWindTurbine>
     IScatteringPointModelPlugin<stkobjects/IScatteringPointModelPlugin>
     IScatteringPointProviderCollectionElement<stkobjects/IScatteringPointProviderCollectionElement>
     IScatteringPointProviderCollection<stkobjects/IScatteringPointProviderCollection>
     IScatteringPointProviderList<stkobjects/IScatteringPointProviderList>
     IObjectRFEnvironment<stkobjects/IObjectRFEnvironment>
     IObjectLaserEnvironment<stkobjects/IObjectLaserEnvironment>
     IAntennaModel<stkobjects/IAntennaModel>
     IAntennaModelGaussian<stkobjects/IAntennaModelGaussian>
     IAntennaModelParabolic<stkobjects/IAntennaModelParabolic>
     IAntennaModelSquareHorn<stkobjects/IAntennaModelSquareHorn>
     IAntennaModelScriptPlugin<stkobjects/IAntennaModelScriptPlugin>
     IAntennaModelExternal<stkobjects/IAntennaModelExternal>
     IAntennaModelGimroc<stkobjects/IAntennaModelGimroc>
     IAntennaModelRemcomUanFormat<stkobjects/IAntennaModelRemcomUanFormat>
     IAntennaModelANSYSffdFormat<stkobjects/IAntennaModelANSYSffdFormat>
     IAntennaModelTicraGRASPFormat<stkobjects/IAntennaModelTicraGRASPFormat>
     IAntennaModelElevationAzimuthCuts<stkobjects/IAntennaModelElevationAzimuthCuts>
     IAntennaModelIeee1979<stkobjects/IAntennaModelIeee1979>
     IAntennaModelDipole<stkobjects/IAntennaModelDipole>
     IAntennaModelHelix<stkobjects/IAntennaModelHelix>
     IAntennaModelCosecantSquared<stkobjects/IAntennaModelCosecantSquared>
     IAntennaModelHemispherical<stkobjects/IAntennaModelHemispherical>
     IAntennaModelPencilBeam<stkobjects/IAntennaModelPencilBeam>
     IElementConfiguration<stkobjects/IElementConfiguration>
     IElementConfigurationCircular<stkobjects/IElementConfigurationCircular>
     IElementConfigurationLinear<stkobjects/IElementConfigurationLinear>
     IElementConfigurationAsciiFile<stkobjects/IElementConfigurationAsciiFile>
     IElementConfigurationHfssEepFile<stkobjects/IElementConfigurationHfssEepFile>
     IElementConfigurationPolygon<stkobjects/IElementConfigurationPolygon>
     IBeamformer<stkobjects/IBeamformer>
     IBeamformerMvdr<stkobjects/IBeamformerMvdr>
     IBeamformerUniform<stkobjects/IBeamformerUniform>
     IBeamformerAsciiFile<stkobjects/IBeamformerAsciiFile>
     IBeamformerScript<stkobjects/IBeamformerScript>
     IBeamformerBlackmanHarris<stkobjects/IBeamformerBlackmanHarris>
     IBeamformerCosine<stkobjects/IBeamformerCosine>
     IBeamformerCosineX<stkobjects/IBeamformerCosineX>
     IBeamformerCustomTaperFile<stkobjects/IBeamformerCustomTaperFile>
     IBeamformerDolphChebyshev<stkobjects/IBeamformerDolphChebyshev>
     IBeamformerHamming<stkobjects/IBeamformerHamming>
     IBeamformerHann<stkobjects/IBeamformerHann>
     IBeamformerRaisedCosine<stkobjects/IBeamformerRaisedCosine>
     IBeamformerRaisedCosineSquared<stkobjects/IBeamformerRaisedCosineSquared>
     IDirectionProvider<stkobjects/IDirectionProvider>
     IDirectionProviderAsciiFile<stkobjects/IDirectionProviderAsciiFile>
     IDirectionProviderObject<stkobjects/IDirectionProviderObject>
     IDirectionProviderLink<stkobjects/IDirectionProviderLink>
     IDirectionProviderScript<stkobjects/IDirectionProviderScript>
     IElement<stkobjects/IElement>
     IElementCollection<stkobjects/IElementCollection>
     IAntennaModelPhasedArray<stkobjects/IAntennaModelPhasedArray>
     IAntennaModelHfssEepArray<stkobjects/IAntennaModelHfssEepArray>
     IAntennaModelIsotropic<stkobjects/IAntennaModelIsotropic>
     IAntennaModelIntelSat<stkobjects/IAntennaModelIntelSat>
     IAntennaModelOpticalSimple<stkobjects/IAntennaModelOpticalSimple>
     IAntennaModelRectangularPattern<stkobjects/IAntennaModelRectangularPattern>
     IAntennaModelGpsGlobal<stkobjects/IAntennaModelGpsGlobal>
     IAntennaModelGpsFrpa<stkobjects/IAntennaModelGpsFrpa>
     IAntennaModelItuBO1213CoPolar<stkobjects/IAntennaModelItuBO1213CoPolar>
     IAntennaModelItuBO1213CrossPolar<stkobjects/IAntennaModelItuBO1213CrossPolar>
     IAntennaModelItuF1245<stkobjects/IAntennaModelItuF1245>
     IAntennaModelItuS580<stkobjects/IAntennaModelItuS580>
     IAntennaModelItuS465<stkobjects/IAntennaModelItuS465>
     IAntennaModelItuS731<stkobjects/IAntennaModelItuS731>
     IAntennaModelItuS1528R12Circular<stkobjects/IAntennaModelItuS1528R12Circular>
     IAntennaModelItuS1528R13<stkobjects/IAntennaModelItuS1528R13>
     IAntennaModelItuS672Circular<stkobjects/IAntennaModelItuS672Circular>
     IAntennaModelItuS1528R12Rectangular<stkobjects/IAntennaModelItuS1528R12Rectangular>
     IAntennaModelItuS672Rectangular<stkobjects/IAntennaModelItuS672Rectangular>
     IAntennaModelApertureCircularCosine<stkobjects/IAntennaModelApertureCircularCosine>
     IAntennaModelApertureCircularUniform<stkobjects/IAntennaModelApertureCircularUniform>
     IAntennaModelApertureCircularCosineSquared<stkobjects/IAntennaModelApertureCircularCosineSquared>
     IAntennaModelApertureCircularBessel<stkobjects/IAntennaModelApertureCircularBessel>
     IAntennaModelApertureCircularBesselEnvelope<stkobjects/IAntennaModelApertureCircularBesselEnvelope>
     IAntennaModelApertureCircularCosinePedestal<stkobjects/IAntennaModelApertureCircularCosinePedestal>
     IAntennaModelApertureCircularCosineSquaredPedestal<stkobjects/IAntennaModelApertureCircularCosineSquaredPedestal>
     IAntennaModelApertureCircularSincIntPower<stkobjects/IAntennaModelApertureCircularSincIntPower>
     IAntennaModelApertureCircularSincRealPower<stkobjects/IAntennaModelApertureCircularSincRealPower>
     IAntennaModelApertureRectangularUniform<stkobjects/IAntennaModelApertureRectangularUniform>
     IAntennaModelApertureRectangularCosineSquared<stkobjects/IAntennaModelApertureRectangularCosineSquared>
     IAntennaModelApertureRectangularCosine<stkobjects/IAntennaModelApertureRectangularCosine>
     IAntennaModelApertureRectangularCosinePedestal<stkobjects/IAntennaModelApertureRectangularCosinePedestal>
     IAntennaModelApertureRectangularCosineSquaredPedestal<stkobjects/IAntennaModelApertureRectangularCosineSquaredPedestal>
     IAntennaModelApertureRectangularSincIntPower<stkobjects/IAntennaModelApertureRectangularSincIntPower>
     IAntennaModelApertureRectangularSincRealPower<stkobjects/IAntennaModelApertureRectangularSincRealPower>
     IAntennaVolumeLevel<stkobjects/IAntennaVolumeLevel>
     IAntennaVolumeLevelCollection<stkobjects/IAntennaVolumeLevelCollection>
     IAntennaVolumeGraphics<stkobjects/IAntennaVolumeGraphics>
     IAntennaGraphics3D<stkobjects/IAntennaGraphics3D>
     IAntennaContourLevel<stkobjects/IAntennaContourLevel>
     IAntennaContourLevelCollection<stkobjects/IAntennaContourLevelCollection>
     IAntennaContour<stkobjects/IAntennaContour>
     IAntennaContourGain<stkobjects/IAntennaContourGain>
     IAntennaContourEirp<stkobjects/IAntennaContourEirp>
     IAntennaContourRip<stkobjects/IAntennaContourRip>
     IAntennaContourFluxDensity<stkobjects/IAntennaContourFluxDensity>
     IAntennaContourSpectralFluxDensity<stkobjects/IAntennaContourSpectralFluxDensity>
     IAntennaContourGraphics<stkobjects/IAntennaContourGraphics>
     IAntennaGraphics<stkobjects/IAntennaGraphics>
     IAntenna<stkobjects/IAntenna>
     IAntennaControl<stkobjects/IAntennaControl>
     IAntennaBeamSelectionStrategy<stkobjects/IAntennaBeamSelectionStrategy>
     IAntennaBeamSelectionStrategyScriptPlugin<stkobjects/IAntennaBeamSelectionStrategyScriptPlugin>
     IAntennaBeam<stkobjects/IAntennaBeam>
     IAntennaBeamTransmit<stkobjects/IAntennaBeamTransmit>
     IAntennaBeamCollection<stkobjects/IAntennaBeamCollection>
     IAntennaSystem<stkobjects/IAntennaSystem>
     IRFFilterModel<stkobjects/IRFFilterModel>
     IModulatorModel<stkobjects/IModulatorModel>
     ITransmitterModel<stkobjects/ITransmitterModel>
     ITransmitterModelScriptPlugin<stkobjects/ITransmitterModelScriptPlugin>
     ITransmitterModelCable<stkobjects/ITransmitterModelCable>
     ITransmitterModelSimple<stkobjects/ITransmitterModelSimple>
     ITransmitterModelMedium<stkobjects/ITransmitterModelMedium>
     ITransmitterModelComplex<stkobjects/ITransmitterModelComplex>
     ITransmitterModelMultibeam<stkobjects/ITransmitterModelMultibeam>
     ITransmitterModelLaser<stkobjects/ITransmitterModelLaser>
     ITransferFunctionInputBackOffCOverImTableRow<stkobjects/ITransferFunctionInputBackOffCOverImTableRow>
     ITransferFunctionInputBackOffCOverImTable<stkobjects/ITransferFunctionInputBackOffCOverImTable>
     ITransferFunctionInputBackOffOutputBackOffTableRow<stkobjects/ITransferFunctionInputBackOffOutputBackOffTableRow>
     ITransferFunctionInputBackOffOutputBackOffTable<stkobjects/ITransferFunctionInputBackOffOutputBackOffTable>
     ITransferFunctionPolynomialCollection<stkobjects/ITransferFunctionPolynomialCollection>
     IReTransmitterModel<stkobjects/IReTransmitterModel>
     IReTransmitterModelSimple<stkobjects/IReTransmitterModelSimple>
     IReTransmitterModelMedium<stkobjects/IReTransmitterModelMedium>
     IReTransmitterModelComplex<stkobjects/IReTransmitterModelComplex>
     ITransmitterGraphics3D<stkobjects/ITransmitterGraphics3D>
     ITransmitterGraphics<stkobjects/ITransmitterGraphics>
     ITransmitter<stkobjects/ITransmitter>
     IDemodulatorModel<stkobjects/IDemodulatorModel>
     ILaserPropagationLossModels<stkobjects/ILaserPropagationLossModels>
     ILinkMargin<stkobjects/ILinkMargin>
     IReceiverModel<stkobjects/IReceiverModel>
     IReceiverModelSimple<stkobjects/IReceiverModelSimple>
     IReceiverModelMedium<stkobjects/IReceiverModelMedium>
     IReceiverModelComplex<stkobjects/IReceiverModelComplex>
     IReceiverModelMultibeam<stkobjects/IReceiverModelMultibeam>
     IReceiverModelLaser<stkobjects/IReceiverModelLaser>
     IReceiverModelScriptPlugin<stkobjects/IReceiverModelScriptPlugin>
     IReceiverModelScriptPluginRF<stkobjects/IReceiverModelScriptPluginRF>
     IReceiverModelCable<stkobjects/IReceiverModelCable>
     IReceiverGraphics3D<stkobjects/IReceiverGraphics3D>
     IReceiverGraphics<stkobjects/IReceiverGraphics>
     IReceiver<stkobjects/IReceiver>
     IRadarActivity<stkobjects/IRadarActivity>
     IRadarActivityTimeComponentListElement<stkobjects/IRadarActivityTimeComponentListElement>
     IRadarActivityTimeComponentListCollection<stkobjects/IRadarActivityTimeComponentListCollection>
     IRadarActivityTimeComponentList<stkobjects/IRadarActivityTimeComponentList>
     IRadarActivityTimeIntervalListElement<stkobjects/IRadarActivityTimeIntervalListElement>
     IRadarActivityTimeIntervalListCollection<stkobjects/IRadarActivityTimeIntervalListCollection>
     IRadarActivityTimeIntervalList<stkobjects/IRadarActivityTimeIntervalList>
     IRadarStcAttenuation<stkobjects/IRadarStcAttenuation>
     IRadarStcAttenuationDecayFactor<stkobjects/IRadarStcAttenuationDecayFactor>
     IRadarStcAttenuationDecaySlope<stkobjects/IRadarStcAttenuationDecaySlope>
     IRadarStcAttenuationMap<stkobjects/IRadarStcAttenuationMap>
     IRadarJamming<stkobjects/IRadarJamming>
     IRadarClutterGeometryModel<stkobjects/IRadarClutterGeometryModel>
     IRadarClutterGeometryModelPlugin<stkobjects/IRadarClutterGeometryModelPlugin>
     IRadarClutter<stkobjects/IRadarClutter>
     IRadarClutterGeometry<stkobjects/IRadarClutterGeometry>
     IRadarTransmitter<stkobjects/IRadarTransmitter>
     IRadarTransmitterMultifunction<stkobjects/IRadarTransmitterMultifunction>
     IRadarReceiver<stkobjects/IRadarReceiver>
     IRadarContinuousWaveAnalysisMode<stkobjects/IRadarContinuousWaveAnalysisMode>
     IRadarContinuousWaveAnalysisModeGoalSNR<stkobjects/IRadarContinuousWaveAnalysisModeGoalSNR>
     IRadarContinuousWaveAnalysisModeFixedTime<stkobjects/IRadarContinuousWaveAnalysisModeFixedTime>
     IRadarPulseIntegration<stkobjects/IRadarPulseIntegration>
     IRadarPulseIntegrationGoalSNR<stkobjects/IRadarPulseIntegrationGoalSNR>
     IRadarPulseIntegrationFixedNumberOfPulses<stkobjects/IRadarPulseIntegrationFixedNumberOfPulses>
     IRadarWaveformSearchTrack<stkobjects/IRadarWaveformSearchTrack>
     IRadarWaveformSearchTrackPulseDefinition<stkobjects/IRadarWaveformSearchTrackPulseDefinition>
     IRadarWaveformSarPulseDefinition<stkobjects/IRadarWaveformSarPulseDefinition>
     IRadarWaveformSarPulseIntegration<stkobjects/IRadarWaveformSarPulseIntegration>
     IRadarModulator<stkobjects/IRadarModulator>
     IRadarProbabilityOfDetection<stkobjects/IRadarProbabilityOfDetection>
     IRadarProbabilityOfDetectionPlugin<stkobjects/IRadarProbabilityOfDetectionPlugin>
     IRadarProbabilityOfDetectionNonCFAR<stkobjects/IRadarProbabilityOfDetectionNonCFAR>
     IRadarProbabilityOfDetectionCFAR<stkobjects/IRadarProbabilityOfDetectionCFAR>
     IRadarWaveformMonostaticSearchTrackContinuous<stkobjects/IRadarWaveformMonostaticSearchTrackContinuous>
     IRadarMultifunctionDetectionProcessing<stkobjects/IRadarMultifunctionDetectionProcessing>
     IRadarWaveformMonostaticSearchTrackFixedPRF<stkobjects/IRadarWaveformMonostaticSearchTrackFixedPRF>
     IRadarWaveformBistaticTransmitterSearchTrackContinuous<stkobjects/IRadarWaveformBistaticTransmitterSearchTrackContinuous>
     IRadarWaveformBistaticTransmitterSearchTrackFixedPRF<stkobjects/IRadarWaveformBistaticTransmitterSearchTrackFixedPRF>
     IRadarWaveformBistaticReceiverSearchTrackContinuous<stkobjects/IRadarWaveformBistaticReceiverSearchTrackContinuous>
     IRadarWaveformBistaticReceiverSearchTrackFixedPRF<stkobjects/IRadarWaveformBistaticReceiverSearchTrackFixedPRF>
     IRadarDopplerClutterFilters<stkobjects/IRadarDopplerClutterFilters>
     IRadarModel<stkobjects/IRadarModel>
     IRadarModeMonostatic<stkobjects/IRadarModeMonostatic>
     IRadarModeMonostaticSearchTrack<stkobjects/IRadarModeMonostaticSearchTrack>
     IRadarModeMonostaticSar<stkobjects/IRadarModeMonostaticSar>
     IRadarModelMonostatic<stkobjects/IRadarModelMonostatic>
     IRadarAntennaBeam<stkobjects/IRadarAntennaBeam>
     IRadarAntennaBeamCollection<stkobjects/IRadarAntennaBeamCollection>
     IRadarMultifunctionWaveformStrategySettings<stkobjects/IRadarMultifunctionWaveformStrategySettings>
     IRadarModelMultifunction<stkobjects/IRadarModelMultifunction>
     IRadarModeBistaticTransmitter<stkobjects/IRadarModeBistaticTransmitter>
     IRadarModeBistaticTransmitterSearchTrack<stkobjects/IRadarModeBistaticTransmitterSearchTrack>
     IRadarModeBistaticTransmitterSar<stkobjects/IRadarModeBistaticTransmitterSar>
     IRadarModelBistaticTransmitter<stkobjects/IRadarModelBistaticTransmitter>
     IRadarModeBistaticReceiver<stkobjects/IRadarModeBistaticReceiver>
     IRadarModeBistaticReceiverSearchTrack<stkobjects/IRadarModeBistaticReceiverSearchTrack>
     IRadarModeBistaticReceiverSar<stkobjects/IRadarModeBistaticReceiverSar>
     IRadarModelBistaticReceiver<stkobjects/IRadarModelBistaticReceiver>
     IRadarGraphics3D<stkobjects/IRadarGraphics3D>
     IRadarMultipathGraphics<stkobjects/IRadarMultipathGraphics>
     IRadarAccessGraphics<stkobjects/IRadarAccessGraphics>
     IRadarGraphics<stkobjects/IRadarGraphics>
     IRadar<stkobjects/IRadar>
     IRadarClutterMapModel<stkobjects/IRadarClutterMapModel>
     IRadarClutterMapModelPlugin<stkobjects/IRadarClutterMapModelPlugin>
     IRadarClutterMapModelConstantCoefficient<stkobjects/IRadarClutterMapModelConstantCoefficient>
     IRadarCrossSectionComputeStrategy<stkobjects/IRadarCrossSectionComputeStrategy>
     IRadarCrossSectionComputeStrategyConstantValue<stkobjects/IRadarCrossSectionComputeStrategyConstantValue>
     IRadarCrossSectionComputeStrategyScriptPlugin<stkobjects/IRadarCrossSectionComputeStrategyScriptPlugin>
     IRadarCrossSectionComputeStrategyExternalFile<stkobjects/IRadarCrossSectionComputeStrategyExternalFile>
     IRadarCrossSectionComputeStrategyAnsysCsvFile<stkobjects/IRadarCrossSectionComputeStrategyAnsysCsvFile>
     IRadarCrossSectionComputeStrategyPlugin<stkobjects/IRadarCrossSectionComputeStrategyPlugin>
     IRadarCrossSectionFrequencyBand<stkobjects/IRadarCrossSectionFrequencyBand>
     IRadarCrossSectionFrequencyBandCollection<stkobjects/IRadarCrossSectionFrequencyBandCollection>
     IRadarCrossSectionModel<stkobjects/IRadarCrossSectionModel>
     IRadarStcAttenuationPlugin<stkobjects/IRadarStcAttenuationPlugin>
     IRadarCrossSectionVolumeLevel<stkobjects/IRadarCrossSectionVolumeLevel>
     IRadarCrossSectionVolumeLevelCollection<stkobjects/IRadarCrossSectionVolumeLevelCollection>
     IRadarCrossSectionVolumeGraphics<stkobjects/IRadarCrossSectionVolumeGraphics>
     IRadarCrossSectionContourLevel<stkobjects/IRadarCrossSectionContourLevel>
     IRadarCrossSectionContourLevelCollection<stkobjects/IRadarCrossSectionContourLevelCollection>
     IRFFilterModelBessel<stkobjects/IRFFilterModelBessel>
     IRFFilterModelButterworth<stkobjects/IRFFilterModelButterworth>
     IRFFilterModelSincEnvSinc<stkobjects/IRFFilterModelSincEnvSinc>
     IRFFilterModelElliptic<stkobjects/IRFFilterModelElliptic>
     IRFFilterModelChebyshev<stkobjects/IRFFilterModelChebyshev>
     IRFFilterModelCosineWindow<stkobjects/IRFFilterModelCosineWindow>
     IRFFilterModelGaussianWindow<stkobjects/IRFFilterModelGaussianWindow>
     IRFFilterModelHammingWindow<stkobjects/IRFFilterModelHammingWindow>
     IRFFilterModelExternal<stkobjects/IRFFilterModelExternal>
     IRFFilterModelScriptPlugin<stkobjects/IRFFilterModelScriptPlugin>
     IRFFilterModelSinc<stkobjects/IRFFilterModelSinc>
     IRFFilterModelRaisedCosine<stkobjects/IRFFilterModelRaisedCosine>
     IRFFilterModelRootRaisedCosine<stkobjects/IRFFilterModelRootRaisedCosine>
     IRFFilterModelRcLowPass<stkobjects/IRFFilterModelRcLowPass>
     IRFFilterModelFirBoxCar<stkobjects/IRFFilterModelFirBoxCar>
     IRFFilterModelFir<stkobjects/IRFFilterModelFir>
     IRFFilterModelIir<stkobjects/IRFFilterModelIir>
     IModulatorModelExternal<stkobjects/IModulatorModelExternal>
     IModulatorModelBoc<stkobjects/IModulatorModelBoc>
     IModulatorModelPulsedSignal<stkobjects/IModulatorModelPulsedSignal>
     IModulatorModelScriptPlugin<stkobjects/IModulatorModelScriptPlugin>
     IDemodulatorModelExternal<stkobjects/IDemodulatorModelExternal>
     IDemodulatorModelScriptPlugin<stkobjects/IDemodulatorModelScriptPlugin>
     IRainLossModelScriptPlugin<stkobjects/IRainLossModelScriptPlugin>
     IRainLossModel<stkobjects/IRainLossModel>
     IRainLossModelCrane1985<stkobjects/IRainLossModelCrane1985>
     IRainLossModelCrane1982<stkobjects/IRainLossModelCrane1982>
     IRainLossModelCCIR1983<stkobjects/IRainLossModelCCIR1983>
     IRainLossModelITURP618_10<stkobjects/IRainLossModelITURP618_10>
     IRainLossModelITURP618_12<stkobjects/IRainLossModelITURP618_12>
     IRainLossModelITURP618_13<stkobjects/IRainLossModelITURP618_13>
     IUrbanTerrestrialLossModel<stkobjects/IUrbanTerrestrialLossModel>
     IUrbanTerrestrialLossModelTwoRay<stkobjects/IUrbanTerrestrialLossModelTwoRay>
     IWirelessInSite64GeometryData<stkobjects/IWirelessInSite64GeometryData>
     IUrbanTerrestrialLossModelWirelessInSite64<stkobjects/IUrbanTerrestrialLossModelWirelessInSite64>
     ITroposphericScintillationFadingLossModel<stkobjects/ITroposphericScintillationFadingLossModel>
     ITroposphericScintillationFadingLossModelP618_8<stkobjects/ITroposphericScintillationFadingLossModelP618_8>
     ITroposphericScintillationFadingLossModelP618_12<stkobjects/ITroposphericScintillationFadingLossModelP618_12>
     IIonosphericFadingLossModel<stkobjects/IIonosphericFadingLossModel>
     IIonosphericFadingLossModelP531_13<stkobjects/IIonosphericFadingLossModelP531_13>
     ICloudsAndFogFadingLossModel<stkobjects/ICloudsAndFogFadingLossModel>
     ICloudsAndFogFadingLossModelP840_6<stkobjects/ICloudsAndFogFadingLossModelP840_6>
     ICloudsAndFogFadingLossModelP840_7<stkobjects/ICloudsAndFogFadingLossModelP840_7>
     IAtmosphericAbsorptionModel<stkobjects/IAtmosphericAbsorptionModel>
     IAtmosphericAbsorptionModelITURP676<stkobjects/IAtmosphericAbsorptionModelITURP676>
     IAtmosphericAbsorptionModelTirem<stkobjects/IAtmosphericAbsorptionModelTirem>
     ISolarActivityConfiguration<stkobjects/ISolarActivityConfiguration>
     ISolarActivityConfigurationSunspotNumber<stkobjects/ISolarActivityConfigurationSunspotNumber>
     ISolarActivityConfigurationSolarFlux<stkobjects/ISolarActivityConfigurationSolarFlux>
     IAtmosphericAbsorptionModelVoacap<stkobjects/IAtmosphericAbsorptionModelVoacap>
     IAtmosphericAbsorptionModelSimpleSatcom<stkobjects/IAtmosphericAbsorptionModelSimpleSatcom>
     IAtmosphericAbsorptionModelScriptPlugin<stkobjects/IAtmosphericAbsorptionModelScriptPlugin>
     IAtmosphericAbsorptionModelCOMPlugin<stkobjects/IAtmosphericAbsorptionModelCOMPlugin>
     ICustomPropagationModel<stkobjects/ICustomPropagationModel>
     IPropagationChannel<stkobjects/IPropagationChannel>
     IBeerBouguerLambertLawLayer<stkobjects/IBeerBouguerLambertLawLayer>
     IBeerBouguerLambertLawLayerCollection<stkobjects/IBeerBouguerLambertLawLayerCollection>
     ILaserAtmosphericLossModelBeerBouguerLambertLaw<stkobjects/ILaserAtmosphericLossModelBeerBouguerLambertLaw>
     IModtranLookupTablePropagationModel<stkobjects/IModtranLookupTablePropagationModel>
     IModtranPropagationModel<stkobjects/IModtranPropagationModel>
     ILaserAtmosphericLossModel<stkobjects/ILaserAtmosphericLossModel>
     ILaserTroposphericScintillationLossModel<stkobjects/ILaserTroposphericScintillationLossModel>
     IAtmosphericTurbulenceModel<stkobjects/IAtmosphericTurbulenceModel>
     IAtmosphericTurbulenceModelConstant<stkobjects/IAtmosphericTurbulenceModelConstant>
     IAtmosphericTurbulenceModelHufnagelValley<stkobjects/IAtmosphericTurbulenceModelHufnagelValley>
     ILaserTroposphericScintillationLossModelITURP1814<stkobjects/ILaserTroposphericScintillationLossModelITURP1814>
     ILaserPropagationChannel<stkobjects/ILaserPropagationChannel>
     ICommSystemLinkSelectionCriteria<stkobjects/ICommSystemLinkSelectionCriteria>
     ICommSystemLinkSelectionCriteriaScriptPlugin<stkobjects/ICommSystemLinkSelectionCriteriaScriptPlugin>
     ICommSystemAccessEventDetection<stkobjects/ICommSystemAccessEventDetection>
     ICommSystemAccessEventDetectionSubsample<stkobjects/ICommSystemAccessEventDetectionSubsample>
     ICommSystemAccessSamplingMethod<stkobjects/ICommSystemAccessSamplingMethod>
     ICommSystemAccessSamplingMethodFixed<stkobjects/ICommSystemAccessSamplingMethodFixed>
     ICommSystemAccessSamplingMethodAdaptive<stkobjects/ICommSystemAccessSamplingMethodAdaptive>
     ICommSystemAccessOptions<stkobjects/ICommSystemAccessOptions>
     ICommSystemGraphics<stkobjects/ICommSystemGraphics>
     ICommSystemGraphics3D<stkobjects/ICommSystemGraphics3D>
     ICommSystem<stkobjects/ICommSystem>
     ISRPModelPluginSettings<stkobjects/ISRPModelPluginSettings>
     ISRPModelBase<stkobjects/ISRPModelBase>
     ISRPModelGPS<stkobjects/ISRPModelGPS>
     ISRPModelSpherical<stkobjects/ISRPModelSpherical>
     ISRPModelPlugin<stkobjects/ISRPModelPlugin>
     IVehicleHPOPDragModelPluginSettings<stkobjects/IVehicleHPOPDragModelPluginSettings>
     IVehicleHPOPDragModel<stkobjects/IVehicleHPOPDragModel>
     IVehicleHPOPDragModelSpherical<stkobjects/IVehicleHPOPDragModelSpherical>
     IVehicleHPOPDragModelPlugin<stkobjects/IVehicleHPOPDragModelPlugin>
     IVehicleDuration<stkobjects/IVehicleDuration>
     IVehicleRealtimeCartesianPoints<stkobjects/IVehicleRealtimeCartesianPoints>
     IVehicleRealtimeLLAHPSPoints<stkobjects/IVehicleRealtimeLLAHPSPoints>
     IVehicleRealtimeLLAPoints<stkobjects/IVehicleRealtimeLLAPoints>
     IVehicleRealtimeUTMPoints<stkobjects/IVehicleRealtimeUTMPoints>
     IVehicleGPSElement<stkobjects/IVehicleGPSElement>
     IVehicleGPSElementCollection<stkobjects/IVehicleGPSElementCollection>
     IVehicleHPOPSRPModel<stkobjects/IVehicleHPOPSRPModel>
     IVehicleThirdBodyGravityElement<stkobjects/IVehicleThirdBodyGravityElement>
     IVehicleThirdBodyGravityCollection<stkobjects/IVehicleThirdBodyGravityCollection>
     IVehicleSGP4LoadData<stkobjects/IVehicleSGP4LoadData>
     IVehicleSGP4OnlineLoad<stkobjects/IVehicleSGP4OnlineLoad>
     IVehicleSGP4OnlineAutoLoad<stkobjects/IVehicleSGP4OnlineAutoLoad>
     IVehicleSGP4LoadFile<stkobjects/IVehicleSGP4LoadFile>
     IVehicleSGP4Segment<stkobjects/IVehicleSGP4Segment>
     IVehiclePropagatorSGP4CommonTasks<stkobjects/IVehiclePropagatorSGP4CommonTasks>
     IVehicleSGP4AutoUpdateProperties<stkobjects/IVehicleSGP4AutoUpdateProperties>
     IVehicleSGP4AutoUpdateFileSource<stkobjects/IVehicleSGP4AutoUpdateFileSource>
     IVehicleSGP4AutoUpdateOnlineSource<stkobjects/IVehicleSGP4AutoUpdateOnlineSource>
     IVehicleSGP4AutoUpdate<stkobjects/IVehicleSGP4AutoUpdate>
     IVehicleSGP4PropagatorSettings<stkobjects/IVehicleSGP4PropagatorSettings>
     IVehicleSGP4SegmentCollection<stkobjects/IVehicleSGP4SegmentCollection>
     IVehicleInitialState<stkobjects/IVehicleInitialState>
     IVehicleHPOPCentralBodyGravity<stkobjects/IVehicleHPOPCentralBodyGravity>
     IVehicleRadiationPressure<stkobjects/IVehicleRadiationPressure>
     IVehicleHPOPSolarRadiationPressure<stkobjects/IVehicleHPOPSolarRadiationPressure>
     IVehicleSolarFluxGeoMagnitudeEnterManually<stkobjects/IVehicleSolarFluxGeoMagnitudeEnterManually>
     IVehicleSolarFluxGeoMagnitudeUseFile<stkobjects/IVehicleSolarFluxGeoMagnitudeUseFile>
     IVehicleSolarFluxGeoMagnitude<stkobjects/IVehicleSolarFluxGeoMagnitude>
     IVehicleHPOPForceModelDrag<stkobjects/IVehicleHPOPForceModelDrag>
     IVehicleHPOPForceModelDragOptions<stkobjects/IVehicleHPOPForceModelDragOptions>
     IVehicleHPOPSolarRadiationPressureOptions<stkobjects/IVehicleHPOPSolarRadiationPressureOptions>
     IVehicleStatic<stkobjects/IVehicleStatic>
     IVehicleSolidTides<stkobjects/IVehicleSolidTides>
     IVehicleOceanTides<stkobjects/IVehicleOceanTides>
     IVehiclePluginSettings<stkobjects/IVehiclePluginSettings>
     IVehiclePluginPropagator<stkobjects/IVehiclePluginPropagator>
     IVehicleHPOPForceModelMoreOptions<stkobjects/IVehicleHPOPForceModelMoreOptions>
     IVehicleEclipsingBodies<stkobjects/IVehicleEclipsingBodies>
     IVehicleHPOPForceModel<stkobjects/IVehicleHPOPForceModel>
     IVehicleStepSizeControl<stkobjects/IVehicleStepSizeControl>
     IVehicleTimeRegularization<stkobjects/IVehicleTimeRegularization>
     IVehicleInterpolation<stkobjects/IVehicleInterpolation>
     IVehicleIntegrator<stkobjects/IVehicleIntegrator>
     IVehicleGravity<stkobjects/IVehicleGravity>
     IVehiclePositionVelocityElement<stkobjects/IVehiclePositionVelocityElement>
     IVehiclePositionVelocityCollection<stkobjects/IVehiclePositionVelocityCollection>
     IVehicleCorrelationListElement<stkobjects/IVehicleCorrelationListElement>
     IVehicleCorrelationListCollection<stkobjects/IVehicleCorrelationListCollection>
     IVehicleConsiderAnalysisCollectionElement<stkobjects/IVehicleConsiderAnalysisCollectionElement>
     IVehicleConsiderAnalysisCollection<stkobjects/IVehicleConsiderAnalysisCollection>
     IVehicleCovariance<stkobjects/IVehicleCovariance>
     IVehicleJxInitialState<stkobjects/IVehicleJxInitialState>
     IVehicleLOPCentralBodyGravity<stkobjects/IVehicleLOPCentralBodyGravity>
     IVehicleThirdBodyGravity<stkobjects/IVehicleThirdBodyGravity>
     IVehicleExpDensModelParams<stkobjects/IVehicleExpDensModelParams>
     IVehicleAdvanced<stkobjects/IVehicleAdvanced>
     IVehicleLOPForceModelDrag<stkobjects/IVehicleLOPForceModelDrag>
     IVehicleLOPSolarRadiationPressure<stkobjects/IVehicleLOPSolarRadiationPressure>
     IVehiclePhysicalData<stkobjects/IVehiclePhysicalData>
     IVehicleLOPForceModel<stkobjects/IVehicleLOPForceModel>
     IVehicleSPICESegment<stkobjects/IVehicleSPICESegment>
     IVehicleSegmentsCollection<stkobjects/IVehicleSegmentsCollection>
     IVehiclePropagator<stkobjects/IVehiclePropagator>
     IVehiclePropagatorHPOP<stkobjects/IVehiclePropagatorHPOP>
     IVehiclePropagatorJ2Perturbation<stkobjects/IVehiclePropagatorJ2Perturbation>
     IVehiclePropagatorJ4Perturbation<stkobjects/IVehiclePropagatorJ4Perturbation>
     IVehiclePropagatorLOP<stkobjects/IVehiclePropagatorLOP>
     IVehiclePropagatorSGP4<stkobjects/IVehiclePropagatorSGP4>
     IVehiclePropagatorSPICE<stkobjects/IVehiclePropagatorSPICE>
     IVehiclePropagatorStkExternal<stkobjects/IVehiclePropagatorStkExternal>
     IVehiclePropagatorTwoBody<stkobjects/IVehiclePropagatorTwoBody>
     IVehiclePropagatorUserExternal<stkobjects/IVehiclePropagatorUserExternal>
     IVehicleLaunchVehicleInitialState<stkobjects/IVehicleLaunchVehicleInitialState>
     IVehiclePropagatorSimpleAscent<stkobjects/IVehiclePropagatorSimpleAscent>
     IVehicleWaypointAltitudeReference<stkobjects/IVehicleWaypointAltitudeReference>
     IVehicleWaypointAltitudeReferenceTerrain<stkobjects/IVehicleWaypointAltitudeReferenceTerrain>
     IVehicleWaypointsElement<stkobjects/IVehicleWaypointsElement>
     IVehicleWaypointsCollection<stkobjects/IVehicleWaypointsCollection>
     IVehiclePropagatorGreatArc<stkobjects/IVehiclePropagatorGreatArc>
     IVehiclePropagatorAviator<stkobjects/IVehiclePropagatorAviator>
     IVehicleLaunchLLA<stkobjects/IVehicleLaunchLLA>
     IVehicleLaunchLLR<stkobjects/IVehicleLaunchLLR>
     IVehicleImpactLLA<stkobjects/IVehicleImpactLLA>
     IVehicleImpactLLR<stkobjects/IVehicleImpactLLR>
     IVehicleLaunchControlFixedApogeeAltitude<stkobjects/IVehicleLaunchControlFixedApogeeAltitude>
     IVehicleLaunchControlFixedDeltaV<stkobjects/IVehicleLaunchControlFixedDeltaV>
     IVehicleLaunchControlFixedDeltaVMinEccentricity<stkobjects/IVehicleLaunchControlFixedDeltaVMinEccentricity>
     IVehicleLaunchControlFixedTimeOfFlight<stkobjects/IVehicleLaunchControlFixedTimeOfFlight>
     IVehicleImpactLocationLaunchAzEl<stkobjects/IVehicleImpactLocationLaunchAzEl>
     IVehicleImpact<stkobjects/IVehicleImpact>
     IVehicleLaunchControl<stkobjects/IVehicleLaunchControl>
     IVehicleImpactLocationPoint<stkobjects/IVehicleImpactLocationPoint>
     IVehicleLaunch<stkobjects/IVehicleLaunch>
     IVehicleImpactLocation<stkobjects/IVehicleImpactLocation>
     IVehiclePropagatorBallistic<stkobjects/IVehiclePropagatorBallistic>
     IVehicleRealtimePointBuilder<stkobjects/IVehicleRealtimePointBuilder>
     IVehiclePropagatorRealtime<stkobjects/IVehiclePropagatorRealtime>
     IVehicleGPSAlmanacProperties<stkobjects/IVehicleGPSAlmanacProperties>
     IVehicleGPSAlmanacPropertiesYUMA<stkobjects/IVehicleGPSAlmanacPropertiesYUMA>
     IVehicleGPSAlmanacPropertiesSEM<stkobjects/IVehicleGPSAlmanacPropertiesSEM>
     IVehicleGPSAlmanacPropertiesSP3<stkobjects/IVehicleGPSAlmanacPropertiesSP3>
     IVehicleGPSSpecifyAlmanac<stkobjects/IVehicleGPSSpecifyAlmanac>
     IVehicleGPSAutoUpdateProperties<stkobjects/IVehicleGPSAutoUpdateProperties>
     IVehicleGPSAutoUpdateFileSource<stkobjects/IVehicleGPSAutoUpdateFileSource>
     IVehicleGPSAutoUpdateOnlineSource<stkobjects/IVehicleGPSAutoUpdateOnlineSource>
     IVehicleGPSAutoUpdate<stkobjects/IVehicleGPSAutoUpdate>
     IVehiclePropagatorGPS<stkobjects/IVehiclePropagatorGPS>
     IVehiclePropagator11ParamDescriptor<stkobjects/IVehiclePropagator11ParamDescriptor>
     IVehiclePropagator11ParamDescriptorCollection<stkobjects/IVehiclePropagator11ParamDescriptorCollection>
     IVehiclePropagator11Param<stkobjects/IVehiclePropagator11Param>
     IVehiclePropagatorSP3File<stkobjects/IVehiclePropagatorSP3File>
     IVehiclePropagatorSP3FileCollection<stkobjects/IVehiclePropagatorSP3FileCollection>
     IVehiclePropagatorSP3<stkobjects/IVehiclePropagatorSP3>
     IVehicleTargetPointingElement<stkobjects/IVehicleTargetPointingElement>
     IVehicleAccessAdvanced<stkobjects/IVehicleAccessAdvanced>
     IVehicleAttitudeTargetSlew<stkobjects/IVehicleAttitudeTargetSlew>
     IVehicleTorque<stkobjects/IVehicleTorque>
     IVehicleIntegratedAttitude<stkobjects/IVehicleIntegratedAttitude>
     IVehicleVector<stkobjects/IVehicleVector>
     IVehicleRateOffset<stkobjects/IVehicleRateOffset>
     IVehicleAttitudeProfile<stkobjects/IVehicleAttitudeProfile>
     IVehicleProfileAlignedAndConstrained<stkobjects/IVehicleProfileAlignedAndConstrained>
     IVehicleProfileInertial<stkobjects/IVehicleProfileInertial>
     IVehicleProfileYawToNadir<stkobjects/IVehicleProfileYawToNadir>
     IVehicleProfileConstraintOffset<stkobjects/IVehicleProfileConstraintOffset>
     IVehicleProfileAlignmentOffset<stkobjects/IVehicleProfileAlignmentOffset>
     IVehicleProfileFixedInAxes<stkobjects/IVehicleProfileFixedInAxes>
     IVehicleProfilePrecessingSpin<stkobjects/IVehicleProfilePrecessingSpin>
     IVehicleProfileSpinAboutXXX<stkobjects/IVehicleProfileSpinAboutXXX>
     IVehicleProfileSpinning<stkobjects/IVehicleProfileSpinning>
     IVehicleProfileCoordinatedTurn<stkobjects/IVehicleProfileCoordinatedTurn>
     IVehicleScheduleTimesElement<stkobjects/IVehicleScheduleTimesElement>
     IVehicleScheduleTimesCollection<stkobjects/IVehicleScheduleTimesCollection>
     IVehicleTargetTimes<stkobjects/IVehicleTargetTimes>
     IVehicleTargetPointingIntervalCollection<stkobjects/IVehicleTargetPointingIntervalCollection>
     IVehicleTargetPointingCollection<stkobjects/IVehicleTargetPointingCollection>
     IVehiclePointing<stkobjects/IVehiclePointing>
     IVehicleAttitudePointing<stkobjects/IVehicleAttitudePointing>
     IVehicleStandardBasic<stkobjects/IVehicleStandardBasic>
     IVehicleAttitudeExternal<stkobjects/IVehicleAttitudeExternal>
     IVehicleAttitude<stkobjects/IVehicleAttitude>
     IVehicleAttitudeRealTimeDataReference<stkobjects/IVehicleAttitudeRealTimeDataReference>
     IVehicleAttitudeRealTime<stkobjects/IVehicleAttitudeRealTime>
     IVehicleAttitudeStandard<stkobjects/IVehicleAttitudeStandard>
     IVehicleTrajectoryAttitudeStandard<stkobjects/IVehicleTrajectoryAttitudeStandard>
     IVehicleOrbitAttitudeStandard<stkobjects/IVehicleOrbitAttitudeStandard>
     IVehicleRouteAttitudeStandard<stkobjects/IVehicleRouteAttitudeStandard>
     IVehicleProfileGPS<stkobjects/IVehicleProfileGPS>
     IVehicleAttitudeTrendControlAviator<stkobjects/IVehicleAttitudeTrendControlAviator>
     IVehicleProfileAviator<stkobjects/IVehicleProfileAviator>
     IVehicleGraphics2DIntervalsCollection<stkobjects/IVehicleGraphics2DIntervalsCollection>
     IVehicleGraphics2DWaypointMarkersElement<stkobjects/IVehicleGraphics2DWaypointMarkersElement>
     IVehicleGraphics2DWaypointMarkersCollection<stkobjects/IVehicleGraphics2DWaypointMarkersCollection>
     IVehicleGraphics2DWaypointMarker<stkobjects/IVehicleGraphics2DWaypointMarker>
     IVehicleGraphics2DPassResolution<stkobjects/IVehicleGraphics2DPassResolution>
     IVehicleGraphics2DRouteResolution<stkobjects/IVehicleGraphics2DRouteResolution>
     IVehicleGraphics2DTrajectoryResolution<stkobjects/IVehicleGraphics2DTrajectoryResolution>
     IVehicleGraphics2DElevationsElement<stkobjects/IVehicleGraphics2DElevationsElement>
     IVehicleGraphics2DElevationsCollection<stkobjects/IVehicleGraphics2DElevationsCollection>
     IVehicleGraphics2DElevContours<stkobjects/IVehicleGraphics2DElevContours>
     IVehicleGraphics2DSAA<stkobjects/IVehicleGraphics2DSAA>
     IVehicleGraphics2DPassShowPasses<stkobjects/IVehicleGraphics2DPassShowPasses>
     IVehicleGraphics2DPass<stkobjects/IVehicleGraphics2DPass>
     IVehicleGraphics2DPasses<stkobjects/IVehicleGraphics2DPasses>
     IVehicleGraphics2DTimeEventTypeLine<stkobjects/IVehicleGraphics2DTimeEventTypeLine>
     IVehicleGraphics2DTimeEventTypeMarker<stkobjects/IVehicleGraphics2DTimeEventTypeMarker>
     IVehicleGraphics2DTimeEventTypeText<stkobjects/IVehicleGraphics2DTimeEventTypeText>
     IVehicleGraphics2DTimeEventType<stkobjects/IVehicleGraphics2DTimeEventType>
     IVehicleGraphics2DTimeEventsElement<stkobjects/IVehicleGraphics2DTimeEventsElement>
     IVehicleGraphics2DTimeEventsCollection<stkobjects/IVehicleGraphics2DTimeEventsCollection>
     IVehicleGraphics2DGroundEllipsesElement<stkobjects/IVehicleGraphics2DGroundEllipsesElement>
     IVehicleGraphics2DGroundEllipsesCollection<stkobjects/IVehicleGraphics2DGroundEllipsesCollection>
     IVehicleGraphics2DLeadTrailData<stkobjects/IVehicleGraphics2DLeadTrailData>
     IVehicleGraphics2DTrajectoryPassData<stkobjects/IVehicleGraphics2DTrajectoryPassData>
     IVehicleGraphics2DOrbitPassData<stkobjects/IVehicleGraphics2DOrbitPassData>
     IVehicleGraphics2DRoutePassData<stkobjects/IVehicleGraphics2DRoutePassData>
     IVehicleGraphics2DLightingElement<stkobjects/IVehicleGraphics2DLightingElement>
     IVehicleGraphics2DLighting<stkobjects/IVehicleGraphics2DLighting>
     IVehicleGraphics2DLine<stkobjects/IVehicleGraphics2DLine>
     IVehicleGraphics2DAttributes<stkobjects/IVehicleGraphics2DAttributes>
     IVehicleGraphics2DAttributesBasic<stkobjects/IVehicleGraphics2DAttributesBasic>
     IVehicleGraphics2DAttributesDisplayState<stkobjects/IVehicleGraphics2DAttributesDisplayState>
     IVehicleGraphics2DAttributesAccess<stkobjects/IVehicleGraphics2DAttributesAccess>
     IVehicleGraphics2DAttributesTrajectory<stkobjects/IVehicleGraphics2DAttributesTrajectory>
     IVehicleGraphics2DAttributesOrbit<stkobjects/IVehicleGraphics2DAttributesOrbit>
     IVehicleGraphics2DAttributesRoute<stkobjects/IVehicleGraphics2DAttributesRoute>
     IVehicleGraphics2DAttributesRealtime<stkobjects/IVehicleGraphics2DAttributesRealtime>
     IVehicleGraphics2DElevationGroundElevation<stkobjects/IVehicleGraphics2DElevationGroundElevation>
     IVehicleGraphics2DElevationSwathHalfWidth<stkobjects/IVehicleGraphics2DElevationSwathHalfWidth>
     IVehicleGraphics2DElevationVehicleHalfAngle<stkobjects/IVehicleGraphics2DElevationVehicleHalfAngle>
     IVehicleGraphics2DElevation<stkobjects/IVehicleGraphics2DElevation>
     IVehicleGraphics2DSwath<stkobjects/IVehicleGraphics2DSwath>
     IVehicleGraphics2DInterval<stkobjects/IVehicleGraphics2DInterval>
     IVehicleGraphics2DAttributesCustom<stkobjects/IVehicleGraphics2DAttributesCustom>
     IVehicleGraphics2DTimeComponentsElement<stkobjects/IVehicleGraphics2DTimeComponentsElement>
     IVehicleGraphics2DTimeComponentsEventElement<stkobjects/IVehicleGraphics2DTimeComponentsEventElement>
     IVehicleGraphics2DTimeComponentsEventCollectionElement<stkobjects/IVehicleGraphics2DTimeComponentsEventCollectionElement>
     IVehicleGraphics2DTimeComponentsCollection<stkobjects/IVehicleGraphics2DTimeComponentsCollection>
     IVehicleGraphics2DAttributesTimeComponents<stkobjects/IVehicleGraphics2DAttributesTimeComponents>
     IVehicleTrajectoryGraphics3DModel<stkobjects/IVehicleTrajectoryGraphics3DModel>
     IVehicleRouteGraphics3DModel<stkobjects/IVehicleRouteGraphics3DModel>
     IVehicleGraphics3DLeadTrailData<stkobjects/IVehicleGraphics3DLeadTrailData>
     IVehicleGraphics3DSystemsElementBase<stkobjects/IVehicleGraphics3DSystemsElementBase>
     IVehicleGraphics3DSystemsElement<stkobjects/IVehicleGraphics3DSystemsElement>
     IVehicleGraphics3DSystemsSpecialElement<stkobjects/IVehicleGraphics3DSystemsSpecialElement>
     IVehicleGraphics3DSystemsCollection<stkobjects/IVehicleGraphics3DSystemsCollection>
     IVehicleGraphics3DDropLinePositionItem<stkobjects/IVehicleGraphics3DDropLinePositionItem>
     IVehicleGraphics3DDropLinePositionItemCollection<stkobjects/IVehicleGraphics3DDropLinePositionItemCollection>
     IVehicleGraphics3DDropLinePathItem<stkobjects/IVehicleGraphics3DDropLinePathItem>
     IVehicleGraphics3DDropLinePathItemCollection<stkobjects/IVehicleGraphics3DDropLinePathItemCollection>
     IVehicleGraphics3DOrbitDropLines<stkobjects/IVehicleGraphics3DOrbitDropLines>
     IVehicleGraphics3DRouteDropLines<stkobjects/IVehicleGraphics3DRouteDropLines>
     IVehicleGraphics3DTrajectoryDropLines<stkobjects/IVehicleGraphics3DTrajectoryDropLines>
     IVehicleGraphics3DProximityAreaObject<stkobjects/IVehicleGraphics3DProximityAreaObject>
     IVehicleGraphics3DEllipsoid<stkobjects/IVehicleGraphics3DEllipsoid>
     IVehicleGraphics3DControlBox<stkobjects/IVehicleGraphics3DControlBox>
     IVehicleGraphics3DBearingBox<stkobjects/IVehicleGraphics3DBearingBox>
     IVehicleGraphics3DBearingEllipse<stkobjects/IVehicleGraphics3DBearingEllipse>
     IVehicleGraphics3DLineOfBearing<stkobjects/IVehicleGraphics3DLineOfBearing>
     IVehicleGraphics3DGeoBox<stkobjects/IVehicleGraphics3DGeoBox>
     IVehicleGraphics3DProximity<stkobjects/IVehicleGraphics3DProximity>
     IVehicleGraphics3DRouteProximity<stkobjects/IVehicleGraphics3DRouteProximity>
     IVehicleGraphics3DOrbitProximity<stkobjects/IVehicleGraphics3DOrbitProximity>
     IVehicleGraphics3DTrajectoryProximity<stkobjects/IVehicleGraphics3DTrajectoryProximity>
     IVehicleGraphics3DElevContours<stkobjects/IVehicleGraphics3DElevContours>
     IVehicleGraphics3DSAA<stkobjects/IVehicleGraphics3DSAA>
     IVehicleGraphics3DSigmaScaleProbability<stkobjects/IVehicleGraphics3DSigmaScaleProbability>
     IVehicleGraphics3DSigmaScaleScale<stkobjects/IVehicleGraphics3DSigmaScaleScale>
     IVehicleGraphics3DDefaultAttributes<stkobjects/IVehicleGraphics3DDefaultAttributes>
     IVehicleGraphics3DIntervalsElement<stkobjects/IVehicleGraphics3DIntervalsElement>
     IVehicleGraphics3DIntervalsCollection<stkobjects/IVehicleGraphics3DIntervalsCollection>
     IVehicleGraphics3DAttributesBasic<stkobjects/IVehicleGraphics3DAttributesBasic>
     IVehicleGraphics3DAttributesIntervals<stkobjects/IVehicleGraphics3DAttributesIntervals>
     IVehicleGraphics3DSize<stkobjects/IVehicleGraphics3DSize>
     IVehicleGraphics3DSigmaScale<stkobjects/IVehicleGraphics3DSigmaScale>
     IVehicleGraphics3DAttributes<stkobjects/IVehicleGraphics3DAttributes>
     IVehicleGraphics3DCovariancePointingContour<stkobjects/IVehicleGraphics3DCovariancePointingContour>
     IVehicleGraphics3DOrbitPassData<stkobjects/IVehicleGraphics3DOrbitPassData>
     IVehicleGraphics3DTrajectoryPassData<stkobjects/IVehicleGraphics3DTrajectoryPassData>
     IVehicleGraphics3DOrbitTrackData<stkobjects/IVehicleGraphics3DOrbitTrackData>
     IVehicleGraphics3DTrajectoryTrackData<stkobjects/IVehicleGraphics3DTrajectoryTrackData>
     IVehicleGraphics3DTickData<stkobjects/IVehicleGraphics3DTickData>
     IVehicleGraphics3DPathTickMarks<stkobjects/IVehicleGraphics3DPathTickMarks>
     IVehicleGraphics3DTrajectoryTickMarks<stkobjects/IVehicleGraphics3DTrajectoryTickMarks>
     IVehicleGraphics3DTrajectory<stkobjects/IVehicleGraphics3DTrajectory>
     IVehicleGraphics3DTickDataLine<stkobjects/IVehicleGraphics3DTickDataLine>
     IVehicleGraphics3DTickDataPoint<stkobjects/IVehicleGraphics3DTickDataPoint>
     IVehicleGraphics3DOrbitTickMarks<stkobjects/IVehicleGraphics3DOrbitTickMarks>
     IVehicleGraphics3DPass<stkobjects/IVehicleGraphics3DPass>
     IVehicleGraphics3DCovariance<stkobjects/IVehicleGraphics3DCovariance>
     IVehicleGraphics3DVelCovariance<stkobjects/IVehicleGraphics3DVelCovariance>
     IVehicleGraphics3DWaypointMarkersElement<stkobjects/IVehicleGraphics3DWaypointMarkersElement>
     IVehicleGraphics3DWaypointMarkersCollection<stkobjects/IVehicleGraphics3DWaypointMarkersCollection>
     IVehicleGraphics3DRoute<stkobjects/IVehicleGraphics3DRoute>
     IVehicleEclipseBodies<stkobjects/IVehicleEclipseBodies>
     IGreatArcGraphics<stkobjects/IGreatArcGraphics>
     IGreatArcGraphics3D<stkobjects/IGreatArcGraphics3D>
     IGreatArcVehicle<stkobjects/IGreatArcVehicle>
     IVehicleGraphics3DBPlaneTemplateDisplayElement<stkobjects/IVehicleGraphics3DBPlaneTemplateDisplayElement>
     IVehicleGraphics3DBPlaneTemplateDisplayCollection<stkobjects/IVehicleGraphics3DBPlaneTemplateDisplayCollection>
     IVehicleGraphics3DBPlaneTemplate<stkobjects/IVehicleGraphics3DBPlaneTemplate>
     IVehicleGraphics3DBPlaneTemplatesCollection<stkobjects/IVehicleGraphics3DBPlaneTemplatesCollection>
     IVehicleGraphics3DBPlaneEvent<stkobjects/IVehicleGraphics3DBPlaneEvent>
     IVehicleGraphics3DBPlanePoint<stkobjects/IVehicleGraphics3DBPlanePoint>
     IVehicleGraphics3DBPlaneTargetPointPosition<stkobjects/IVehicleGraphics3DBPlaneTargetPointPosition>
     IVehicleGraphics3DBPlaneTargetPointPositionCartesian<stkobjects/IVehicleGraphics3DBPlaneTargetPointPositionCartesian>
     IVehicleGraphics3DBPlaneTargetPointPositionPolar<stkobjects/IVehicleGraphics3DBPlaneTargetPointPositionPolar>
     IVehicleGraphics3DBPlaneTargetPoint<stkobjects/IVehicleGraphics3DBPlaneTargetPoint>
     IVehicleGraphics3DBPlanePointCollection<stkobjects/IVehicleGraphics3DBPlanePointCollection>
     IVehicleGraphics3DBPlaneInstance<stkobjects/IVehicleGraphics3DBPlaneInstance>
     IVehicleGraphics3DBPlaneInstancesCollection<stkobjects/IVehicleGraphics3DBPlaneInstancesCollection>
     IVehicleGraphics3DBPlanes<stkobjects/IVehicleGraphics3DBPlanes>
     IVehicleSpaceEnvironment<stkobjects/IVehicleSpaceEnvironment>
     IEOIR<stkobjects/IEOIR>
     ISatelliteGraphics3DModel<stkobjects/ISatelliteGraphics3DModel>
     ISatelliteGraphics3D<stkobjects/ISatelliteGraphics3D>
     IVehicleCentralBodies<stkobjects/IVehicleCentralBodies>
     ISatelliteGraphics<stkobjects/ISatelliteGraphics>
     IVehicleRepeatGroundTrackNumbering<stkobjects/IVehicleRepeatGroundTrackNumbering>
     IVehicleBreakAngle<stkobjects/IVehicleBreakAngle>
     IVehicleBreakAngleBreakByLatitude<stkobjects/IVehicleBreakAngleBreakByLatitude>
     IVehicleBreakAngleBreakByLongitude<stkobjects/IVehicleBreakAngleBreakByLongitude>
     IVehicleDefinition<stkobjects/IVehicleDefinition>
     IVehiclePassNumbering<stkobjects/IVehiclePassNumbering>
     IVehiclePassNumberingDateOfFirstPass<stkobjects/IVehiclePassNumberingDateOfFirstPass>
     IVehiclePassNumberingFirstPassNum<stkobjects/IVehiclePassNumberingFirstPassNum>
     IVehiclePassBreak<stkobjects/IVehiclePassBreak>
     IVehicleInertia<stkobjects/IVehicleInertia>
     IVehicleMassProperties<stkobjects/IVehicleMassProperties>
     IExportToolTimePeriod<stkobjects/IExportToolTimePeriod>
     IExportToolStepSize<stkobjects/IExportToolStepSize>
     IVehicleEphemerisCode500ExportTool<stkobjects/IVehicleEphemerisCode500ExportTool>
     IVehicleEphemerisCCSDSExportTool<stkobjects/IVehicleEphemerisCCSDSExportTool>
     IVehicleEphemerisStkExportTool<stkobjects/IVehicleEphemerisStkExportTool>
     IVehicleCoordinateAxes<stkobjects/IVehicleCoordinateAxes>
     IVehicleCoordinateAxesCustom<stkobjects/IVehicleCoordinateAxesCustom>
     IVehicleAttitudeExportTool<stkobjects/IVehicleAttitudeExportTool>
     IVehicleEphemerisSpiceExportTool<stkobjects/IVehicleEphemerisSpiceExportTool>
     IVehiclePropDefinitionExportTool<stkobjects/IVehiclePropDefinitionExportTool>
     IVehicleEphemerisStkBinaryExportTool<stkobjects/IVehicleEphemerisStkBinaryExportTool>
     IVehicleEphemerisCCSDSv2ExportTool<stkobjects/IVehicleEphemerisCCSDSv2ExportTool>
     ISatelliteExportTools<stkobjects/ISatelliteExportTools>
     ISatellite<stkobjects/ISatellite>
     ILaunchVehicleGraphics<stkobjects/ILaunchVehicleGraphics>
     ILaunchVehicleGraphics3D<stkobjects/ILaunchVehicleGraphics3D>
     ILaunchVehicleExportTools<stkobjects/ILaunchVehicleExportTools>
     ILaunchVehicle<stkobjects/ILaunchVehicle>
     IGroundVehicleGraphics<stkobjects/IGroundVehicleGraphics>
     IGroundVehicleGraphics3D<stkobjects/IGroundVehicleGraphics3D>
     IGroundVehicleExportTools<stkobjects/IGroundVehicleExportTools>
     IGroundVehicle<stkobjects/IGroundVehicle>
     IMissileGraphics<stkobjects/IMissileGraphics>
     IMissileGraphics3D<stkobjects/IMissileGraphics3D>
     IMissileExportTools<stkobjects/IMissileExportTools>
     IMissile<stkobjects/IMissile>
     IAircraftGraphics<stkobjects/IAircraftGraphics>
     IAircraftGraphics3D<stkobjects/IAircraftGraphics3D>
     IAircraftExportTools<stkobjects/IAircraftExportTools>
     IAircraft<stkobjects/IAircraft>
     IShipGraphics<stkobjects/IShipGraphics>
     IShipGraphics3D<stkobjects/IShipGraphics3D>
     IShipExportTools<stkobjects/IShipExportTools>
     IShip<stkobjects/IShip>
     IMtoGraphics2DMarker<stkobjects/IMtoGraphics2DMarker>
     IMtoGraphics2DLine<stkobjects/IMtoGraphics2DLine>
     IMtoGraphics2DFadeTimes<stkobjects/IMtoGraphics2DFadeTimes>
     IMtoGraphics2DLeadTrailTimes<stkobjects/IMtoGraphics2DLeadTrailTimes>
     IMtoGraphics2DTrack<stkobjects/IMtoGraphics2DTrack>
     IMtoGraphics2DTrackCollection<stkobjects/IMtoGraphics2DTrackCollection>
     IMtoDefaultGraphics2DTrack<stkobjects/IMtoDefaultGraphics2DTrack>
     IMtoGraphics2DGlobalTrackOptions<stkobjects/IMtoGraphics2DGlobalTrackOptions>
     IMtoGraphics<stkobjects/IMtoGraphics>
     IMtoGraphics3DModelArtic<stkobjects/IMtoGraphics3DModelArtic>
     IMtoGraphics3DMarker<stkobjects/IMtoGraphics3DMarker>
     IMtoGraphics3DPoint<stkobjects/IMtoGraphics3DPoint>
     IMtoGraphics3DModel<stkobjects/IMtoGraphics3DModel>
     IMtoGraphics3DSwapDistances<stkobjects/IMtoGraphics3DSwapDistances>
     IMtoGraphics3DDropLines<stkobjects/IMtoGraphics3DDropLines>
     IMtoGraphics3DTrack<stkobjects/IMtoGraphics3DTrack>
     IMtoGraphics3DTrackCollection<stkobjects/IMtoGraphics3DTrackCollection>
     IMtoDefaultGraphics3DTrack<stkobjects/IMtoDefaultGraphics3DTrack>
     IMtoGraphics3DGlobalTrackOptions<stkobjects/IMtoGraphics3DGlobalTrackOptions>
     IMtoGraphics3D<stkobjects/IMtoGraphics3D>
     IMtoTrackPoint<stkobjects/IMtoTrackPoint>
     IMtoTrackPointCollection<stkobjects/IMtoTrackPointCollection>
     IMtoTrack<stkobjects/IMtoTrack>
     IMtoTrackCollection<stkobjects/IMtoTrackCollection>
     IMtoDefaultTrack<stkobjects/IMtoDefaultTrack>
     IMtoGlobalTrackOptions<stkobjects/IMtoGlobalTrackOptions>
     IMtoAnalysisPosition<stkobjects/IMtoAnalysisPosition>
     IMtoAnalysisVisibility<stkobjects/IMtoAnalysisVisibility>
     IMtoAnalysisFieldOfView<stkobjects/IMtoAnalysisFieldOfView>
     IMtoAnalysisRange<stkobjects/IMtoAnalysisRange>
     IMtoAnalysis<stkobjects/IMtoAnalysis>
     IMto<stkobjects/IMto>
     ILineTargetGraphics<stkobjects/ILineTargetGraphics>
     ILineTargetGraphics3D<stkobjects/ILineTargetGraphics3D>
     ILineTargetPoint<stkobjects/ILineTargetPoint>
     ILineTargetPointCollection<stkobjects/ILineTargetPointCollection>
     ILineTarget<stkobjects/ILineTarget>
     IChainGraphics2DStatic<stkobjects/IChainGraphics2DStatic>
     IChainGraphics2DAnimation<stkobjects/IChainGraphics2DAnimation>
     IChainGraphics<stkobjects/IChainGraphics>
     IChainGraphics3D<stkobjects/IChainGraphics3D>
     IAccessEventDetection<stkobjects/IAccessEventDetection>
     IAccessSampling<stkobjects/IAccessSampling>
     IChainConnectionCollection<stkobjects/IChainConnectionCollection>
     IChainTimePeriodBase<stkobjects/IChainTimePeriodBase>
     IChainUserSpecifiedTimePeriod<stkobjects/IChainUserSpecifiedTimePeriod>
     IChainConstraints<stkobjects/IChainConstraints>
     IChainConnection<stkobjects/IChainConnection>
     IChainOptimalStrandOpts<stkobjects/IChainOptimalStrandOpts>
     IChain<stkobjects/IChain>
     ICoverageGraphics2DStatic<stkobjects/ICoverageGraphics2DStatic>
     ICoverageGraphics2DAnimation<stkobjects/ICoverageGraphics2DAnimation>
     ICoverageGraphics2DProgress<stkobjects/ICoverageGraphics2DProgress>
     ICoverageGraphics<stkobjects/ICoverageGraphics>
     ICoverageGraphics3DAttributes<stkobjects/ICoverageGraphics3DAttributes>
     ICoverageGraphics3D<stkobjects/ICoverageGraphics3D>
     ICoverageSelectedGridPoint<stkobjects/ICoverageSelectedGridPoint>
     ICoverageGridPointSelection<stkobjects/ICoverageGridPointSelection>
     ICoverageGridInspector<stkobjects/ICoverageGridInspector>
     ICoverageRegionFilesCollection<stkobjects/ICoverageRegionFilesCollection>
     ICoverageAreaTargetsCollection<stkobjects/ICoverageAreaTargetsCollection>
     ICoveragePointFileListCollection<stkobjects/ICoveragePointFileListCollection>
     ICoverageBounds<stkobjects/ICoverageBounds>
     ICoverageBoundsCustomBoundary<stkobjects/ICoverageBoundsCustomBoundary>
     ICoverageBoundsCustomRegions<stkobjects/ICoverageBoundsCustomRegions>
     ICoverageBoundsGlobal<stkobjects/ICoverageBoundsGlobal>
     ICoverageBoundsLat<stkobjects/ICoverageBoundsLat>
     ICoverageBoundsLatLine<stkobjects/ICoverageBoundsLatLine>
     ICoverageBoundsLonLine<stkobjects/ICoverageBoundsLonLine>
     ICoverageBoundsLatLonRegion<stkobjects/ICoverageBoundsLatLonRegion>
     ICoverageResolution<stkobjects/ICoverageResolution>
     ICoverageResolutionArea<stkobjects/ICoverageResolutionArea>
     ICoverageResolutionDistance<stkobjects/ICoverageResolutionDistance>
     ICoverageResolutionLatLon<stkobjects/ICoverageResolutionLatLon>
     ICoverageGrid<stkobjects/ICoverageGrid>
     ICoveragePointDefinition<stkobjects/ICoveragePointDefinition>
     ICoverageAssetListElement<stkobjects/ICoverageAssetListElement>
     ICoverageAdvanced<stkobjects/ICoverageAdvanced>
     ICoverageInterval<stkobjects/ICoverageInterval>
     ICoverageDefinition<stkobjects/ICoverageDefinition>
     IFigureOfMeritGraphics3DLegendWindow<stkobjects/IFigureOfMeritGraphics3DLegendWindow>
     IFigureOfMeritGraphics2DRampColor<stkobjects/IFigureOfMeritGraphics2DRampColor>
     IFigureOfMeritGraphics2DLevelAttributesElement<stkobjects/IFigureOfMeritGraphics2DLevelAttributesElement>
     IFigureOfMeritGraphics2DLevelAttributesCollection<stkobjects/IFigureOfMeritGraphics2DLevelAttributesCollection>
     IFigureOfMeritGraphics2DPositionOnMap<stkobjects/IFigureOfMeritGraphics2DPositionOnMap>
     IFigureOfMeritGraphics2DLegendWindow<stkobjects/IFigureOfMeritGraphics2DLegendWindow>
     IFigureOfMeritGraphics2DColorOptions<stkobjects/IFigureOfMeritGraphics2DColorOptions>
     IFigureOfMeritGraphics2DTextOptions<stkobjects/IFigureOfMeritGraphics2DTextOptions>
     IFigureOfMeritGraphics2DRangeColorOptions<stkobjects/IFigureOfMeritGraphics2DRangeColorOptions>
     IFigureOfMeritGraphics2DLegend<stkobjects/IFigureOfMeritGraphics2DLegend>
     IFigureOfMeritGraphics2DContours<stkobjects/IFigureOfMeritGraphics2DContours>
     IFigureOfMeritGraphics2DAttributes<stkobjects/IFigureOfMeritGraphics2DAttributes>
     IFigureOfMeritGraphics2DContoursAnimation<stkobjects/IFigureOfMeritGraphics2DContoursAnimation>
     IFigureOfMeritGraphics2DAttributesAnimation<stkobjects/IFigureOfMeritGraphics2DAttributesAnimation>
     IFigureOfMeritGraphics3DAttributes<stkobjects/IFigureOfMeritGraphics3DAttributes>
     IFigureOfMeritGraphics3D<stkobjects/IFigureOfMeritGraphics3D>
     IFigureOfMeritDefinitionScalarCalculation<stkobjects/IFigureOfMeritDefinitionScalarCalculation>
     IFigureOfMeritGridInspector<stkobjects/IFigureOfMeritGridInspector>
     IFigureOfMeritNavigationAccuracyMethod<stkobjects/IFigureOfMeritNavigationAccuracyMethod>
     IFigureOfMeritNavigationAccuracyMethodElevationAngle<stkobjects/IFigureOfMeritNavigationAccuracyMethodElevationAngle>
     IFigureOfMeritNavigationAccuracyMethodConstant<stkobjects/IFigureOfMeritNavigationAccuracyMethodConstant>
     IFigureOfMeritAssetListElement<stkobjects/IFigureOfMeritAssetListElement>
     IFigureOfMeritAssetListCollection<stkobjects/IFigureOfMeritAssetListCollection>
     IFigureOfMeritUncertainties<stkobjects/IFigureOfMeritUncertainties>
     IFigureOfMeritSatisfaction<stkobjects/IFigureOfMeritSatisfaction>
     IFigureOfMeritDefinitionData<stkobjects/IFigureOfMeritDefinitionData>
     IFigureOfMeritDefinitionDataMinMax<stkobjects/IFigureOfMeritDefinitionDataMinMax>
     IFigureOfMeritDefinitionDataPercentLevel<stkobjects/IFigureOfMeritDefinitionDataPercentLevel>
     IFigureOfMeritDefinitionDataMinAssets<stkobjects/IFigureOfMeritDefinitionDataMinAssets>
     IFigureOfMeritDefinitionDataBestN<stkobjects/IFigureOfMeritDefinitionDataBestN>
     IFigureOfMeritDefinitionDataBest4<stkobjects/IFigureOfMeritDefinitionDataBest4>
     IFigureOfMeritDefinitionResponseTime<stkobjects/IFigureOfMeritDefinitionResponseTime>
     IFigureOfMeritDefinitionRevisitTime<stkobjects/IFigureOfMeritDefinitionRevisitTime>
     IFigureOfMeritDefinitionSimpleCoverage<stkobjects/IFigureOfMeritDefinitionSimpleCoverage>
     IFigureOfMeritDefinitionTimeAverageGap<stkobjects/IFigureOfMeritDefinitionTimeAverageGap>
     IFigureOfMeritDefinitionDilutionOfPrecision<stkobjects/IFigureOfMeritDefinitionDilutionOfPrecision>
     IFigureOfMeritDefinitionNavigationAccuracy<stkobjects/IFigureOfMeritDefinitionNavigationAccuracy>
     IFigureOfMeritDefinitionAccessSeparation<stkobjects/IFigureOfMeritDefinitionAccessSeparation>
     IFigureOfMerit<stkobjects/IFigureOfMerit>
     IFigureOfMeritDefinitionSystemResponseTime<stkobjects/IFigureOfMeritDefinitionSystemResponseTime>
     IFigureOfMeritDefinitionAgeOfData<stkobjects/IFigureOfMeritDefinitionAgeOfData>
     IFigureOfMeritDefinitionSystemAgeOfData<stkobjects/IFigureOfMeritDefinitionSystemAgeOfData>
     IConstellationConstraintRestriction<stkobjects/IConstellationConstraintRestriction>
     IConstellationConstraintObjectRestriction<stkobjects/IConstellationConstraintObjectRestriction>
     IConstellationConstraints<stkobjects/IConstellationConstraints>
     IConstellationGraphics<stkobjects/IConstellationGraphics>
     IConstellationRouting<stkobjects/IConstellationRouting>
     IConstellation<stkobjects/IConstellation>
     IEventDetectionStrategy<stkobjects/IEventDetectionStrategy>
     IEventDetectionNoSubSampling<stkobjects/IEventDetectionNoSubSampling>
     IEventDetectionSubSampling<stkobjects/IEventDetectionSubSampling>
     ISamplingMethodStrategy<stkobjects/ISamplingMethodStrategy>
     ISamplingMethodAdaptive<stkobjects/ISamplingMethodAdaptive>
     ISamplingMethodFixedStep<stkobjects/ISamplingMethodFixedStep>
     ISpaceEnvironmentRadEnergyMethodSpecify<stkobjects/ISpaceEnvironmentRadEnergyMethodSpecify>
     ISpaceEnvironmentRadEnergyValues<stkobjects/ISpaceEnvironmentRadEnergyValues>
     ISpaceEnvironmentRadiationEnvironment<stkobjects/ISpaceEnvironmentRadiationEnvironment>
     ISpaceEnvironmentMagnitudeFieldGraphics2D<stkobjects/ISpaceEnvironmentMagnitudeFieldGraphics2D>
     ISpaceEnvironmentScenarioExtGraphics3D<stkobjects/ISpaceEnvironmentScenarioExtGraphics3D>
     ISpaceEnvironmentSAAContour<stkobjects/ISpaceEnvironmentSAAContour>
     IVehicleSpaceEnvironmentMagneticField<stkobjects/IVehicleSpaceEnvironmentMagneticField>
     IVehicleSpaceEnvironmentVehTemperature<stkobjects/IVehicleSpaceEnvironmentVehTemperature>
     IVehicleSpaceEnvironmentParticleFlux<stkobjects/IVehicleSpaceEnvironmentParticleFlux>
     IVehicleSpaceEnvironmentRadDoseRateElement<stkobjects/IVehicleSpaceEnvironmentRadDoseRateElement>
     IVehicleSpaceEnvironmentRadDoseRateCollection<stkobjects/IVehicleSpaceEnvironmentRadDoseRateCollection>
     IVehicleSpaceEnvironmentRadiation<stkobjects/IVehicleSpaceEnvironmentRadiation>
     IVehicleSpaceEnvironmentMagnitudeFieldLine<stkobjects/IVehicleSpaceEnvironmentMagnitudeFieldLine>
     IVehicleSpaceEnvironmentGraphics<stkobjects/IVehicleSpaceEnvironmentGraphics>
     IStkPreferencesVDF<stkobjects/IStkPreferencesVDF>
     IStkPreferencesConnect<stkobjects/IStkPreferencesConnect>
     IStkPreferencesPythonPlugins<stkobjects/IStkPreferencesPythonPlugins>
     IPathCollection<stkobjects/IPathCollection>
     IVehicleAttitudeMaximumSlewRate<stkobjects/IVehicleAttitudeMaximumSlewRate>
     IVehicleAttitudeMaximumSlewAcceleration<stkobjects/IVehicleAttitudeMaximumSlewAcceleration>
     IVehicleAttitudeSlewBase<stkobjects/IVehicleAttitudeSlewBase>
     IVehicleAttitudeSlewConstrained<stkobjects/IVehicleAttitudeSlewConstrained>
     IVehicleAttitudeSlewFixedRate<stkobjects/IVehicleAttitudeSlewFixedRate>
     IVehicleAttitudeSlewFixedTime<stkobjects/IVehicleAttitudeSlewFixedTime>
     IVmGridDefinition<stkobjects/IVmGridDefinition>
     IVmAnalysisInterval<stkobjects/IVmAnalysisInterval>
     IVmAdvanced<stkobjects/IVmAdvanced>
     IVmGraphics3D<stkobjects/IVmGraphics3D>
     IVmGraphics3DGrid<stkobjects/IVmGraphics3DGrid>
     IVmGraphics3DCrossSection<stkobjects/IVmGraphics3DCrossSection>
     IVmGraphics3DCrossSectionPlaneCollection<stkobjects/IVmGraphics3DCrossSectionPlaneCollection>
     IVmGraphics3DVolume<stkobjects/IVmGraphics3DVolume>
     IVmGraphics3DActiveGridPoints<stkobjects/IVmGraphics3DActiveGridPoints>
     IVmGraphics3DSpatialCalculationLevels<stkobjects/IVmGraphics3DSpatialCalculationLevels>
     IVmGraphics3DSpatialCalculationLevelCollection<stkobjects/IVmGraphics3DSpatialCalculationLevelCollection>
     IVmGraphics3DLegend<stkobjects/IVmGraphics3DLegend>
     IVmExportTool<stkobjects/IVmExportTool>
     IVolumetric<stkobjects/IVolumetric>
     IVmGridSpatialCalculation<stkobjects/IVmGridSpatialCalculation>
     IVmExternalFile<stkobjects/IVmExternalFile>
     IVmGraphics3DCrossSectionPlane<stkobjects/IVmGraphics3DCrossSectionPlane>
     IVmGraphics3DSpatialCalculationLevel<stkobjects/IVmGraphics3DSpatialCalculationLevel>
     ISatelliteCollection<stkobjects/ISatelliteCollection>
     ISubset<stkobjects/ISubset>
     IAdvCATAvailableObjectCollection<stkobjects/IAdvCATAvailableObjectCollection>
     IAdvCATChosenObjectCollection<stkobjects/IAdvCATChosenObjectCollection>
     IAdvCATPreFilters<stkobjects/IAdvCATPreFilters>
     IAdvCATAdvancedEllipsoid<stkobjects/IAdvCATAdvancedEllipsoid>
     IAdvCATAdvanced<stkobjects/IAdvCATAdvanced>
     IAdvCATGraphics3D<stkobjects/IAdvCATGraphics3D>
     IAdvCAT<stkobjects/IAdvCAT>
     IAdvCATChosenObject<stkobjects/IAdvCATChosenObject>
     IEOIRShapeObject<stkobjects/IEOIRShapeObject>
     IEOIRShapeBox<stkobjects/IEOIRShapeBox>
     IEOIRShapeCone<stkobjects/IEOIRShapeCone>
     IEOIRShapePlate<stkobjects/IEOIRShapePlate>
     IEOIRShapeSphere<stkobjects/IEOIRShapeSphere>
     IEOIRShapeCoupler<stkobjects/IEOIRShapeCoupler>
     IEOIRShapeNone<stkobjects/IEOIRShapeNone>
     IEOIRShapeGEOComm<stkobjects/IEOIRShapeGEOComm>
     IEOIRShapeLEOComm<stkobjects/IEOIRShapeLEOComm>
     IEOIRShapeLEOImaging<stkobjects/IEOIRShapeLEOImaging>
     IEOIRShapeCustomMesh<stkobjects/IEOIRShapeCustomMesh>
     IEOIRShapeTargetSignature<stkobjects/IEOIRShapeTargetSignature>
     IEOIRStagePlume<stkobjects/IEOIRStagePlume>
     IEOIRShape<stkobjects/IEOIRShape>
     IEOIRStage<stkobjects/IEOIRStage>
     IEOIRShapeCollection<stkobjects/IEOIRShapeCollection>
     IEOIRMaterialElement<stkobjects/IEOIRMaterialElement>
     IEOIRMaterialElementCollection<stkobjects/IEOIRMaterialElementCollection>
     IMissileEOIR<stkobjects/IMissileEOIR>
     IVehicleEOIR<stkobjects/IVehicleEOIR>
     IEOIRShapeCylinder<stkobjects/IEOIRShapeCylinder>
     IStkObjectChangedEventArgs<stkobjects/IStkObjectChangedEventArgs>
     IScenarioBeforeSaveEventArgs<stkobjects/IScenarioBeforeSaveEventArgs>
     IPctCmpltEventArgs<stkobjects/IPctCmpltEventArgs>
     IStkObjectPreDeleteEventArgs<stkobjects/IStkObjectPreDeleteEventArgs>
     IStkObjectCutCopyPasteEventArgs<stkobjects/IStkObjectCutCopyPasteEventArgs>

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
     VehiclePropDefinitionExportTool<stkobjects/VehiclePropDefinitionExportTool>
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
     MixedSphericalFPAHorizontal<stkobjects/MixedSphericalFPAHorizontal>
     MixedSphericalFPAVertical<stkobjects/MixedSphericalFPAVertical>
     OrbitStateMixedSpherical<stkobjects/OrbitStateMixedSpherical>
     SphericalFPAHorizontal<stkobjects/SphericalFPAHorizontal>
     SphericalFPAVertical<stkobjects/SphericalFPAVertical>
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
     VmGridSpatialCalculation<stkobjects/VmGridSpatialCalculation>
     VmExternalFile<stkobjects/VmExternalFile>
     VmAnalysisInterval<stkobjects/VmAnalysisInterval>
     VmAdvanced<stkobjects/VmAdvanced>
     VmGraphics3D<stkobjects/VmGraphics3D>
     VmGraphics3DGrid<stkobjects/VmGraphics3DGrid>
     VmGraphics3DCrossSection<stkobjects/VmGraphics3DCrossSection>
     VmGraphics3DCrossSectionPlane<stkobjects/VmGraphics3DCrossSectionPlane>
     VmGraphics3DCrossSectionPlaneCollection<stkobjects/VmGraphics3DCrossSectionPlaneCollection>
     VmGraphics3DVolume<stkobjects/VmGraphics3DVolume>
     VmGraphics3DActiveGridPoints<stkobjects/VmGraphics3DActiveGridPoints>
     VmGraphics3DSpatialCalculationLevels<stkobjects/VmGraphics3DSpatialCalculationLevels>
     VmGraphics3DSpatialCalculationLevel<stkobjects/VmGraphics3DSpatialCalculationLevel>
     VmGraphics3DSpatialCalculationLevelCollection<stkobjects/VmGraphics3DSpatialCalculationLevelCollection>
     VmGraphics3DLegend<stkobjects/VmGraphics3DLegend>
     VmExportTool<stkobjects/VmExportTool>
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

    ≔ CONSTANTS<stkobjects/CONSTANTS>
    ≔ HELP_CONTEXT_IDS<stkobjects/HELP_CONTEXT_IDS>
    ≔ ERROR_CODES<stkobjects/ERROR_CODES>
    ≔ ABERRATION_TYPE<stkobjects/ABERRATION_TYPE>
    ≔ ANIMATION_MODES<stkobjects/ANIMATION_MODES>
    ≔ ANIMATION_OPTIONS<stkobjects/ANIMATION_OPTIONS>
    ≔ ANIMATION_ACTIONS<stkobjects/ANIMATION_ACTIONS>
    ≔ ANIMATION_DIRECTIONS<stkobjects/ANIMATION_DIRECTIONS>
    ≔ AZ_EL_MASK_TYPE<stkobjects/AZ_EL_MASK_TYPE>
    ≔ ACTION_TYPE<stkobjects/ACTION_TYPE>
    ≔ AXIS_OFFSET<stkobjects/AXIS_OFFSET>
    ≔ DATA_PROVIDER_RESULT_CATEGORIES<stkobjects/DATA_PROVIDER_RESULT_CATEGORIES>
    ≔ DATA_PROVIDER_TYPE<stkobjects/DATA_PROVIDER_TYPE>
    ≔ DATA_PROVIDER_ELEMENT_TYPE<stkobjects/DATA_PROVIDER_ELEMENT_TYPE>
    ≔ ACCESS_TIME_TYPE<stkobjects/ACCESS_TIME_TYPE>
    ≔ ALTITUDE_REFERENCE_TYPE<stkobjects/ALTITUDE_REFERENCE_TYPE>
    ≔ TERRAIN_NORM_TYPE<stkobjects/TERRAIN_NORM_TYPE>
    ≔ LIGHTING_OBSTRUCTION_MODEL_TYPE<stkobjects/LIGHTING_OBSTRUCTION_MODEL_TYPE>
    ≔ DISPLAY_TIMES_TYPE<stkobjects/DISPLAY_TIMES_TYPE>
    ≔ AREA_TYPE<stkobjects/AREA_TYPE>
    ≔ TRAJECTORY_TYPE<stkobjects/TRAJECTORY_TYPE>
    ≔ OFFSET_FRAME_TYPE<stkobjects/OFFSET_FRAME_TYPE>
    ≔ SCENARIO_3D_POINT_SIZE<stkobjects/SCENARIO_3D_POINT_SIZE>
    ≔ TERRAIN_FILE_TYPE<stkobjects/TERRAIN_FILE_TYPE>
    ≔ TILESET_3D_SOURCE_TYPE<stkobjects/TILESET_3D_SOURCE_TYPE>
    ≔ MARKER_TYPE<stkobjects/MARKER_TYPE>
    ≔ VECTOR_AXES_CONNECT_TYPE<stkobjects/VECTOR_AXES_CONNECT_TYPE>
    ≔ GRAPHICS_3D_MARKER_ORIGIN_TYPE<stkobjects/GRAPHICS_3D_MARKER_ORIGIN_TYPE>
    ≔ GRAPHICS_3D_LABEL_SWAP_DISTANCE<stkobjects/GRAPHICS_3D_LABEL_SWAP_DISTANCE>
    ≔ PLANET_POSITION_SOURCE_TYPE<stkobjects/PLANET_POSITION_SOURCE_TYPE>
    ≔ EPHEM_SOURCE_TYPE<stkobjects/EPHEM_SOURCE_TYPE>
    ≔ PLANET_ORBIT_DISPLAY_TYPE<stkobjects/PLANET_ORBIT_DISPLAY_TYPE>
    ≔ SCENARIO_END_LOOP_TYPE<stkobjects/SCENARIO_END_LOOP_TYPE>
    ≔ SCENARIO_REFRESH_DELTA_TYPE<stkobjects/SCENARIO_REFRESH_DELTA_TYPE>
    ≔ SENSOR_PATTERN<stkobjects/SENSOR_PATTERN>
    ≔ SENSOR_POINTING<stkobjects/SENSOR_POINTING>
    ≔ SENSOR_POINTING_TARGETED_BORESIGHT_TYPE<stkobjects/SENSOR_POINTING_TARGETED_BORESIGHT_TYPE>
    ≔ BORESIGHT_TYPE<stkobjects/BORESIGHT_TYPE>
    ≔ TRACK_MODE_TYPE<stkobjects/TRACK_MODE_TYPE>
    ≔ SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE<stkobjects/SENSOR_AZ_EL_BORESIGHT_AXIS_TYPE>
    ≔ SENSOR_REFRACTION_TYPE<stkobjects/SENSOR_REFRACTION_TYPE>
    ≔ SENSOR_PROJECTION_DISTANCE_TYPE<stkobjects/SENSOR_PROJECTION_DISTANCE_TYPE>
    ≔ SENSOR_LOCATION<stkobjects/SENSOR_LOCATION>
    ≔ SCENARIO_TIME_STEP_TYPE<stkobjects/SCENARIO_TIME_STEP_TYPE>
    ≔ NOTE_SHOW_TYPE<stkobjects/NOTE_SHOW_TYPE>
    ≔ GEOMETRIC_ELEM_TYPE<stkobjects/GEOMETRIC_ELEM_TYPE>
    ≔ SENSOR_SCAN_MODE<stkobjects/SENSOR_SCAN_MODE>
    ≔ CONSTRAINT_BACKGROUND<stkobjects/CONSTRAINT_BACKGROUND>
    ≔ CONSTRAINT_GROUND_TRACK<stkobjects/CONSTRAINT_GROUND_TRACK>
    ≔ INTERSECTION_TYPE<stkobjects/INTERSECTION_TYPE>
    ≔ CONSTRAINT_LIGHTING<stkobjects/CONSTRAINT_LIGHTING>
    ≔ SENSOR_GRAPHICS_3D_PROJECTION_TYPE<stkobjects/SENSOR_GRAPHICS_3D_PROJECTION_TYPE>
    ≔ SENSOR_GRAPHICS_3D_PULSE_STYLE<stkobjects/SENSOR_GRAPHICS_3D_PULSE_STYLE>
    ≔ SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET<stkobjects/SENSOR_GRAPHICS_3D_PULSE_FREQUENCY_PRESET>
    ≔ LINE_WIDTH<stkobjects/LINE_WIDTH>
    ≔ STK_OBJECT_TYPE<stkobjects/STK_OBJECT_TYPE>
    ≔ ACCESS_CONSTRAINTS<stkobjects/ACCESS_CONSTRAINTS>
    ≔ BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE<stkobjects/BORDER_WALL_UPPER_LOWER_EDGE_ALTITUDE_REFERENCE>
    ≔ SHADOW_MODEL<stkobjects/SHADOW_MODEL>
    ≔ METHOD_TO_COMPUTE_SUN_POSITION<stkobjects/METHOD_TO_COMPUTE_SUN_POSITION>
    ≔ ATMOSPHERIC_DENSITY_MODEL<stkobjects/ATMOSPHERIC_DENSITY_MODEL>
    ≔ MARKER_SHAPE_3D<stkobjects/MARKER_SHAPE_3D>
    ≔ LEAD_TRAIL_DATA<stkobjects/LEAD_TRAIL_DATA>
    ≔ TICK_DATA<stkobjects/TICK_DATA>
    ≔ LOAD_METHOD_TYPE<stkobjects/LOAD_METHOD_TYPE>
    ≔ LLA_POSITION_TYPE<stkobjects/LLA_POSITION_TYPE>
    ≔ VEHICLE_GRAPHICS_2D_PASS<stkobjects/VEHICLE_GRAPHICS_2D_PASS>
    ≔ VEHICLE_GRAPHICS_2D_VISIBLE_SIDES<stkobjects/VEHICLE_GRAPHICS_2D_VISIBLE_SIDES>
    ≔ VEHICLE_GRAPHICS_2D_OFFSET<stkobjects/VEHICLE_GRAPHICS_2D_OFFSET>
    ≔ VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE<stkobjects/VEHICLE_GRAPHICS_2D_TIME_EVENT_TYPE>
    ≔ VEHICLE_GRAPHICS_2D_ATTRIBUTES<stkobjects/VEHICLE_GRAPHICS_2D_ATTRIBUTES>
    ≔ VEHICLE_GRAPHICS_2D_ELEVATION<stkobjects/VEHICLE_GRAPHICS_2D_ELEVATION>
    ≔ VEHICLE_GRAPHICS_2D_OPTIONS<stkobjects/VEHICLE_GRAPHICS_2D_OPTIONS>
    ≔ MODEL_TYPE<stkobjects/MODEL_TYPE>
    ≔ VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE<stkobjects/VEHICLE_GRAPHICS_3D_DROP_LINE_TYPE>
    ≔ VEHICLE_GRAPHICS_3D_SIGMA_SCALE<stkobjects/VEHICLE_GRAPHICS_3D_SIGMA_SCALE>
    ≔ VEHICLE_GRAPHICS_3D_ATTRIBUTES<stkobjects/VEHICLE_GRAPHICS_3D_ATTRIBUTES>
    ≔ ROUTE_GRAPHICS_3D_MARKER_TYPE<stkobjects/ROUTE_GRAPHICS_3D_MARKER_TYPE>
    ≔ VEHICLE_ELLIPSE_OPTIONS<stkobjects/VEHICLE_ELLIPSE_OPTIONS>
    ≔ VEHICLE_PROPAGATOR_TYPE<stkobjects/VEHICLE_PROPAGATOR_TYPE>
    ≔ VEHICLE_SGP4_SWITCH_METHOD<stkobjects/VEHICLE_SGP4_SWITCH_METHOD>
    ≔ VEHICLE_SGP4TLE_SELECTION<stkobjects/VEHICLE_SGP4TLE_SELECTION>
    ≔ VEHICLE_SGP4_AUTO_UPDATE_SOURCE<stkobjects/VEHICLE_SGP4_AUTO_UPDATE_SOURCE>
    ≔ THIRD_BODY_GRAV_SOURCE_TYPE<stkobjects/THIRD_BODY_GRAV_SOURCE_TYPE>
    ≔ VEHICLE_GEOMAG_FLUX_SRC<stkobjects/VEHICLE_GEOMAG_FLUX_SRC>
    ≔ VEHICLE_GEOMAG_FLUX_UPDATE_RATE<stkobjects/VEHICLE_GEOMAG_FLUX_UPDATE_RATE>
    ≔ VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE<stkobjects/VEHICLE_SOLAR_FLUX_GEO_MAGNITUDE>
    ≔ VEHICLE_INTEGRATION_MODEL<stkobjects/VEHICLE_INTEGRATION_MODEL>
    ≔ VEHICLE_PREDICTOR_CORRECTOR_SCHEME<stkobjects/VEHICLE_PREDICTOR_CORRECTOR_SCHEME>
    ≔ VEHICLE_METHOD<stkobjects/VEHICLE_METHOD>
    ≔ VEHICLE_INTERPOLATION_METHOD<stkobjects/VEHICLE_INTERPOLATION_METHOD>
    ≔ VEHICLE_FRAME<stkobjects/VEHICLE_FRAME>
    ≔ VEHICLE_CORRELATION_LIST_TYPE<stkobjects/VEHICLE_CORRELATION_LIST_TYPE>
    ≔ VEHICLE_CONSIDER_ANALYSIS_TYPE<stkobjects/VEHICLE_CONSIDER_ANALYSIS_TYPE>
    ≔ VEHICLE_WAYPOINT_COMP_METHOD<stkobjects/VEHICLE_WAYPOINT_COMP_METHOD>
    ≔ VEHICLE_ALTITUDE_REFERENCE<stkobjects/VEHICLE_ALTITUDE_REFERENCE>
    ≔ VEHICLE_WAYPOINT_INTERP_METHOD<stkobjects/VEHICLE_WAYPOINT_INTERP_METHOD>
    ≔ VEHICLE_LAUNCH<stkobjects/VEHICLE_LAUNCH>
    ≔ VEHICLE_IMPACT<stkobjects/VEHICLE_IMPACT>
    ≔ VEHICLE_LAUNCH_CONTROL<stkobjects/VEHICLE_LAUNCH_CONTROL>
    ≔ VEHICLE_IMPACT_LOCATION<stkobjects/VEHICLE_IMPACT_LOCATION>
    ≔ VEHICLE_PASS_NUMBERING<stkobjects/VEHICLE_PASS_NUMBERING>
    ≔ VEHICLE_PARTIAL_PASS_MEASUREMENT<stkobjects/VEHICLE_PARTIAL_PASS_MEASUREMENT>
    ≔ VEHICLE_COORDINATE_SYSTEM<stkobjects/VEHICLE_COORDINATE_SYSTEM>
    ≔ VEHICLE_BREAK_ANGLE_TYPE<stkobjects/VEHICLE_BREAK_ANGLE_TYPE>
    ≔ VEHICLE_DIRECTION<stkobjects/VEHICLE_DIRECTION>
    ≔ GRAPHICS_3D_LOCATION<stkobjects/GRAPHICS_3D_LOCATION>
    ≔ GRAPHICS_3D_X_ORIGIN<stkobjects/GRAPHICS_3D_X_ORIGIN>
    ≔ GRAPHICS_3D_Y_ORIGIN<stkobjects/GRAPHICS_3D_Y_ORIGIN>
    ≔ GRAPHICS_3D_FONT_SIZE<stkobjects/GRAPHICS_3D_FONT_SIZE>
    ≔ AIRCRAFT_WGS84_WARNING_TYPE<stkobjects/AIRCRAFT_WGS84_WARNING_TYPE>
    ≔ SURFACE_REFERENCE<stkobjects/SURFACE_REFERENCE>
    ≔ GRAPHICS_3D_FORMAT<stkobjects/GRAPHICS_3D_FORMAT>
    ≔ ATTITUDE_STANDARD_TYPE<stkobjects/ATTITUDE_STANDARD_TYPE>
    ≔ VEHICLE_ATTITUDE<stkobjects/VEHICLE_ATTITUDE>
    ≔ VEHICLE_PROFILE<stkobjects/VEHICLE_PROFILE>
    ≔ VEHICLE_LOOK_AHEAD_METHOD<stkobjects/VEHICLE_LOOK_AHEAD_METHOD>
    ≔ VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION<stkobjects/VEHICLE_GRAPHICS_3D_B_PLANE_TARGET_POINT_POSITION>
    ≔ SENSOR_ALTITUDE_CROSSING_SIDES<stkobjects/SENSOR_ALTITUDE_CROSSING_SIDES>
    ≔ SENSOR_ALTITUDE_CROSSING_DIRECTION<stkobjects/SENSOR_ALTITUDE_CROSSING_DIRECTION>
    ≔ SENSOR_GRAPHICS_3D_INHERIT_FROM_2D<stkobjects/SENSOR_GRAPHICS_3D_INHERIT_FROM_2D>
    ≔ SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE<stkobjects/SENSOR_GRAPHICS_3D_VISUAL_APPEARANCE>
    ≔ CHAIN_TIME_PERIOD_TYPE<stkobjects/CHAIN_TIME_PERIOD_TYPE>
    ≔ CHAIN_CONST_CONSTRAINTS_MODE<stkobjects/CHAIN_CONST_CONSTRAINTS_MODE>
    ≔ CHAIN_COV_ASSET_MODE<stkobjects/CHAIN_COV_ASSET_MODE>
    ≔ CHAIN_PARENT_PLATFORM_RESTRICTION<stkobjects/CHAIN_PARENT_PLATFORM_RESTRICTION>
    ≔ CHAIN_OPTIMAL_STRAND_METRIC_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_METRIC_TYPE>
    ≔ CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE>
    ≔ CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE>
    ≔ CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE<stkobjects/CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE>
    ≔ DATA_SAVE_MODE<stkobjects/DATA_SAVE_MODE>
    ≔ COVERAGE_BOUNDS<stkobjects/COVERAGE_BOUNDS>
    ≔ COVERAGE_POINT_LOC_METHOD<stkobjects/COVERAGE_POINT_LOC_METHOD>
    ≔ COVERAGE_POINT_ALTITUDE_METHOD<stkobjects/COVERAGE_POINT_ALTITUDE_METHOD>
    ≔ COVERAGE_GRID_CLASS<stkobjects/COVERAGE_GRID_CLASS>
    ≔ COVERAGE_ALTITUDE_METHOD<stkobjects/COVERAGE_ALTITUDE_METHOD>
    ≔ COVERAGE_GROUND_ALTITUDE_METHOD<stkobjects/COVERAGE_GROUND_ALTITUDE_METHOD>
    ≔ COVERAGE_DATA_RETENTION<stkobjects/COVERAGE_DATA_RETENTION>
    ≔ COVERAGE_REGION_ACCESS_ACCEL<stkobjects/COVERAGE_REGION_ACCESS_ACCEL>
    ≔ COVERAGE_RESOLUTION<stkobjects/COVERAGE_RESOLUTION>
    ≔ COVERAGE_ASSET_STATUS<stkobjects/COVERAGE_ASSET_STATUS>
    ≔ COVERAGE_ASSET_GROUPING<stkobjects/COVERAGE_ASSET_GROUPING>
    ≔ FIGURE_OF_MERIT_DEFINITION_TYPE<stkobjects/FIGURE_OF_MERIT_DEFINITION_TYPE>
    ≔ FIGURE_OF_MERIT_SATISFACTION_TYPE<stkobjects/FIGURE_OF_MERIT_SATISFACTION_TYPE>
    ≔ FIGURE_OF_MERIT_CONSTRAINT_NAME<stkobjects/FIGURE_OF_MERIT_CONSTRAINT_NAME>
    ≔ FIGURE_OF_MERIT_COMPUTE<stkobjects/FIGURE_OF_MERIT_COMPUTE>
    ≔ FIGURE_OF_MERIT_ACROSS_ASSETS<stkobjects/FIGURE_OF_MERIT_ACROSS_ASSETS>
    ≔ FIGURE_OF_MERIT_COMPUTE_TYPE<stkobjects/FIGURE_OF_MERIT_COMPUTE_TYPE>
    ≔ FIGURE_OF_MERIT_METHOD<stkobjects/FIGURE_OF_MERIT_METHOD>
    ≔ FIGURE_OF_MERIT_END_GAP_OPTION<stkobjects/FIGURE_OF_MERIT_END_GAP_OPTION>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_CONTOUR_TYPE>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_FLOATING_POINT_FORMAT>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_DIRECTION>
    ≔ FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION<stkobjects/FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION>
    ≔ FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE<stkobjects/FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE>
    ≔ IV_CLOCK_HOST<stkobjects/IV_CLOCK_HOST>
    ≔ IV_TIME_SENSE<stkobjects/IV_TIME_SENSE>
    ≔ GPS_ATTITUDE_MODEL_TYPE<stkobjects/GPS_ATTITUDE_MODEL_TYPE>
    ≔ CONSTELLATION_CONSTRAINT_RESTRICTION<stkobjects/CONSTELLATION_CONSTRAINT_RESTRICTION>
    ≔ EVENT_DETECTION<stkobjects/EVENT_DETECTION>
    ≔ SAMPLING_METHOD<stkobjects/SAMPLING_METHOD>
    ≔ COVERAGE_SATISFACTION_TYPE<stkobjects/COVERAGE_SATISFACTION_TYPE>
    ≔ CCSDS_REFERENCE_FRAME<stkobjects/CCSDS_REFERENCE_FRAME>
    ≔ CCSDS_DATE_FORMAT<stkobjects/CCSDS_DATE_FORMAT>
    ≔ CCSDS_EPHEM_FORMAT<stkobjects/CCSDS_EPHEM_FORMAT>
    ≔ CCSDS_TIME_SYSTEM<stkobjects/CCSDS_TIME_SYSTEM>
    ≔ STK_EPHEM_COORDINATE_SYSTEM<stkobjects/STK_EPHEM_COORDINATE_SYSTEM>
    ≔ STK_EPHEM_COVARIANCE_TYPE<stkobjects/STK_EPHEM_COVARIANCE_TYPE>
    ≔ EXPORT_TOOL_VERSION_FORMAT<stkobjects/EXPORT_TOOL_VERSION_FORMAT>
    ≔ EXPORT_TOOL_TIME_PERIOD<stkobjects/EXPORT_TOOL_TIME_PERIOD>
    ≔ SPICE_INTERPOLATION<stkobjects/SPICE_INTERPOLATION>
    ≔ ATTITUDE_COORDINATE_AXES<stkobjects/ATTITUDE_COORDINATE_AXES>
    ≔ ATTITUDE_INCLUDE<stkobjects/ATTITUDE_INCLUDE>
    ≔ EXPORT_TOOL_STEP_SIZE<stkobjects/EXPORT_TOOL_STEP_SIZE>
    ≔ TEXT_OUTLINE_STYLE<stkobjects/TEXT_OUTLINE_STYLE>
    ≔ MTO_RANGE_MODE<stkobjects/MTO_RANGE_MODE>
    ≔ MTO_TRACK_EVAL<stkobjects/MTO_TRACK_EVAL>
    ≔ MTO_ENTIRETY<stkobjects/MTO_ENTIRETY>
    ≔ MTO_VISIBILITY_MODE<stkobjects/MTO_VISIBILITY_MODE>
    ≔ MTO_OBJECT_INTERVAL<stkobjects/MTO_OBJECT_INTERVAL>
    ≔ MTO_INPUT_DATA_TYPE<stkobjects/MTO_INPUT_DATA_TYPE>
    ≔ SOLID_TIDE<stkobjects/SOLID_TIDE>
    ≔ TIME_PERIOD_VALUE_TYPE<stkobjects/TIME_PERIOD_VALUE_TYPE>
    ≔ ONE_POINT_ACCESS_STATUS<stkobjects/ONE_POINT_ACCESS_STATUS>
    ≔ ONE_POINT_ACCESS_SUMMARY<stkobjects/ONE_POINT_ACCESS_SUMMARY>
    ≔ LOOK_AHEAD_PROPAGATOR<stkobjects/LOOK_AHEAD_PROPAGATOR>
    ≔ GRAPHICS_3D_MARKER_ORIENTATION<stkobjects/GRAPHICS_3D_MARKER_ORIENTATION>
    ≔ SRP_MODEL<stkobjects/SRP_MODEL>
    ≔ DRAG_MODEL<stkobjects/DRAG_MODEL>
    ≔ VEHICLE_PROPAGATION_FRAME<stkobjects/VEHICLE_PROPAGATION_FRAME>
    ≔ STAR_REFERENCE_FRAME<stkobjects/STAR_REFERENCE_FRAME>
    ≔ GPS_REFERENCE_WEEK<stkobjects/GPS_REFERENCE_WEEK>
    ≔ COVERAGE_CUSTOM_REGION_ALGORITHM<stkobjects/COVERAGE_CUSTOM_REGION_ALGORITHM>
    ≔ VEHICLE_GPS_SWITCH_METHOD<stkobjects/VEHICLE_GPS_SWITCH_METHOD>
    ≔ VEHICLE_GPS_ELEM_SELECTION<stkobjects/VEHICLE_GPS_ELEM_SELECTION>
    ≔ VEHICLE_GPS_AUTO_UPDATE_SOURCE<stkobjects/VEHICLE_GPS_AUTO_UPDATE_SOURCE>
    ≔ VEHICLE_GPS_ALMANAC_TYPE<stkobjects/VEHICLE_GPS_ALMANAC_TYPE>
    ≔ STK_EXTERNAL_EPHEMERIS_FORMAT<stkobjects/STK_EXTERNAL_EPHEMERIS_FORMAT>
    ≔ STK_EXTERNAL_FILE_MESSAGE_LEVEL<stkobjects/STK_EXTERNAL_FILE_MESSAGE_LEVEL>
    ≔ COVERAGE_3D_DRAW_AT_ALTITUDE_MODE<stkobjects/COVERAGE_3D_DRAW_AT_ALTITUDE_MODE>
    ≔ DISTANCE_ON_SPHERE<stkobjects/DISTANCE_ON_SPHERE>
    ≔ FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE<stkobjects/FIGURE_OF_MERIT_INVALID_VALUE_ACTION_TYPE>
    ≔ VEHICLE_SLEW_TIMING_BETWEEN_TARGETS<stkobjects/VEHICLE_SLEW_TIMING_BETWEEN_TARGETS>
    ≔ VEHICLE_SLEW_MODE<stkobjects/VEHICLE_SLEW_MODE>
    ≔ COMPONENT<stkobjects/COMPONENT>
    ≔ VM_DEFINITION_TYPE<stkobjects/VM_DEFINITION_TYPE>
    ≔ VM_SPATIAL_CALC_EVAL_TYPE<stkobjects/VM_SPATIAL_CALC_EVAL_TYPE>
    ≔ VM_SAVE_COMPUTED_DATA_TYPE<stkobjects/VM_SAVE_COMPUTED_DATA_TYPE>
    ≔ VM_DISPLAY_VOLUME_TYPE<stkobjects/VM_DISPLAY_VOLUME_TYPE>
    ≔ VM_DISPLAY_QUALITY_TYPE<stkobjects/VM_DISPLAY_QUALITY_TYPE>
    ≔ VM_LEGEND_NUMERIC_NOTATION<stkobjects/VM_LEGEND_NUMERIC_NOTATION>
    ≔ VM_LEVEL_ORDER<stkobjects/VM_LEVEL_ORDER>
    ≔ SENSOR_EOIR_PROCESSING_LEVELS<stkobjects/SENSOR_EOIR_PROCESSING_LEVELS>
    ≔ SENSOR_EOIR_JITTER_TYPES<stkobjects/SENSOR_EOIR_JITTER_TYPES>
    ≔ SENSOR_EOIR_SCAN_MODES<stkobjects/SENSOR_EOIR_SCAN_MODES>
    ≔ SENSOR_EOIR_BAND_IMAGE_QUALITY<stkobjects/SENSOR_EOIR_BAND_IMAGE_QUALITY>
    ≔ SENSOR_EOIR_BAND_SPECTRAL_SHAPE<stkobjects/SENSOR_EOIR_BAND_SPECTRAL_SHAPE>
    ≔ SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE<stkobjects/SENSOR_EOIR_BAND_SPATIAL_INPUT_MODE>
    ≔ SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS<stkobjects/SENSOR_EOIR_BAND_SPECTRAL_RSR_UNITS>
    ≔ SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE<stkobjects/SENSOR_EOIR_BAND_OPTICAL_INPUT_MODE>
    ≔ SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE<stkobjects/SENSOR_EOIR_BAND_OPTICAL_TRANSMISSION_MODE>
    ≔ SENSOR_EOIR_BAND_RAD_PARAM_LEVEL<stkobjects/SENSOR_EOIR_BAND_RAD_PARAM_LEVEL>
    ≔ SENSOR_EOIR_BAND_QE_MODE<stkobjects/SENSOR_EOIR_BAND_QE_MODE>
    ≔ SENSOR_EOIR_BAND_QUANTIZATION_MODE<stkobjects/SENSOR_EOIR_BAND_QUANTIZATION_MODE>
    ≔ SENSOR_EOIR_BAND_WAVELENGTH_TYPE<stkobjects/SENSOR_EOIR_BAND_WAVELENGTH_TYPE>
    ≔ SENSOR_EOIR_BAND_SATURATION_MODE<stkobjects/SENSOR_EOIR_BAND_SATURATION_MODE>
    ≔ VM_VOLUME_GRID_EXPORT_TYPE<stkobjects/VM_VOLUME_GRID_EXPORT_TYPE>
    ≔ VM_DATA_EXPORT_FORMAT_TYPE<stkobjects/VM_DATA_EXPORT_FORMAT_TYPE>
    ≔ CONSTELLATION_FROM_TO_PARENT_CONSTRAINT<stkobjects/CONSTELLATION_FROM_TO_PARENT_CONSTRAINT>
    ≔ ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS<stkobjects/ANALYSIS_WORKBENCH_ACCESS_CONSTRAINTS>
    ≔ STATISTICS<stkobjects/STATISTICS>
    ≔ TIME_VARYING_EXTREMUM<stkobjects/TIME_VARYING_EXTREMUM>
    ≔ MODEL_GLTF_REFLECTION_MAP_TYPE<stkobjects/MODEL_GLTF_REFLECTION_MAP_TYPE>
    ≔ SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE<stkobjects/SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE>
    ≔ LOP_ATMOSPHERIC_DENSITY_MODEL<stkobjects/LOP_ATMOSPHERIC_DENSITY_MODEL>
    ≔ LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL<stkobjects/LOW_ALTITUDE_ATMOSPHERIC_DENSITY_MODEL>
    ≔ EPHEM_EXPORT_TOOL_FILE_FORMAT<stkobjects/EPHEM_EXPORT_TOOL_FILE_FORMAT>
    ≔ ADV_CAT_ELLIPSOID_CLASS<stkobjects/ADV_CAT_ELLIPSOID_CLASS>
    ≔ ADV_CAT_CONJUNCTION_TYPE<stkobjects/ADV_CAT_CONJUNCTION_TYPE>
    ≔ ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE<stkobjects/ADV_CAT_SECONDARY_ELLIPSOIDS_VISIBILITY_TYPE>
    ≔ EOIR_SHAPE_TYPE<stkobjects/EOIR_SHAPE_TYPE>
    ≔ EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE<stkobjects/EOIR_SHAPE_MATERIAL_SPECIFICATION_TYPE>
    ≔ EOIR_THERMAL_MODEL_TYPE<stkobjects/EOIR_THERMAL_MODEL_TYPE>
    ≔ EOIR_FLIGHT_TYPE<stkobjects/EOIR_FLIGHT_TYPE>
    ≔ COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE<stkobjects/COMPONENT_LINK_EMBED_CONTROL_REFERENCE_TYPE>
    ≔ SWATH_COMPUTATIONAL_METHOD<stkobjects/SWATH_COMPUTATIONAL_METHOD>
    ≔ CLASSICAL_LOCATION<stkobjects/CLASSICAL_LOCATION>
    ≔ ORIENTATION_ASC_NODE<stkobjects/ORIENTATION_ASC_NODE>
    ≔ GEODETIC_SIZE<stkobjects/GEODETIC_SIZE>
    ≔ DELAUNAY_L_TYPE<stkobjects/DELAUNAY_L_TYPE>
    ≔ DELAUNAY_H_TYPE<stkobjects/DELAUNAY_H_TYPE>
    ≔ DELAUNAY_G_TYPE<stkobjects/DELAUNAY_G_TYPE>
    ≔ EQUINOCTIAL_SIZE_SHAPE<stkobjects/EQUINOCTIAL_SIZE_SHAPE>
    ≔ MIXED_SPHERICAL_FPA<stkobjects/MIXED_SPHERICAL_FPA>
    ≔ SPHERICAL_FPA<stkobjects/SPHERICAL_FPA>
    ≔ CLASSICAL_SIZE_SHAPE<stkobjects/CLASSICAL_SIZE_SHAPE>
    ≔ EQUINOCTIAL_FORMULATION<stkobjects/EQUINOCTIAL_FORMULATION>
    ≔ SCATTERING_POINT_PROVIDER_TYPE<stkobjects/SCATTERING_POINT_PROVIDER_TYPE>
    ≔ SCATTERING_POINT_MODEL_TYPE<stkobjects/SCATTERING_POINT_MODEL_TYPE>
    ≔ SCATTERING_POINT_PROVIDER_LIST_TYPE<stkobjects/SCATTERING_POINT_PROVIDER_LIST_TYPE>
    ≔ POLARIZATION_TYPE<stkobjects/POLARIZATION_TYPE>
    ≔ POLARIZATION_REFERENCE_AXIS<stkobjects/POLARIZATION_REFERENCE_AXIS>
    ≔ NOISE_TEMP_COMPUTE_TYPE<stkobjects/NOISE_TEMP_COMPUTE_TYPE>
    ≔ POINTING_STRATEGY_TYPE<stkobjects/POINTING_STRATEGY_TYPE>
    ≔ WAVEFORM_TYPE<stkobjects/WAVEFORM_TYPE>
    ≔ FREQUENCY_SPEC<stkobjects/FREQUENCY_SPEC>
    ≔ PRF_MODE<stkobjects/PRF_MODE>
    ≔ PULSE_WIDTH_MODE<stkobjects/PULSE_WIDTH_MODE>
    ≔ WAVEFORM_SELECTION_STRATEGY_TYPE<stkobjects/WAVEFORM_SELECTION_STRATEGY_TYPE>
    ≔ ANTENNA_CONTROL_REFERENCE_TYPE<stkobjects/ANTENNA_CONTROL_REFERENCE_TYPE>
    ≔ ANTENNA_MODEL_TYPE<stkobjects/ANTENNA_MODEL_TYPE>
    ≔ ANTENNA_CONTOUR_TYPE<stkobjects/ANTENNA_CONTOUR_TYPE>
    ≔ CIRCULAR_APERTURE_INPUT_TYPE<stkobjects/CIRCULAR_APERTURE_INPUT_TYPE>
    ≔ RECTANGULAR_APERTURE_INPUT_TYPE<stkobjects/RECTANGULAR_APERTURE_INPUT_TYPE>
    ≔ DIRECTION_PROVIDER_TYPE<stkobjects/DIRECTION_PROVIDER_TYPE>
    ≔ BEAMFORMER_TYPE<stkobjects/BEAMFORMER_TYPE>
    ≔ ELEMENT_CONFIGURATION_TYPE<stkobjects/ELEMENT_CONFIGURATION_TYPE>
    ≔ LATTICE_TYPE<stkobjects/LATTICE_TYPE>
    ≔ SPACING_UNIT<stkobjects/SPACING_UNIT>
    ≔ LIMITS_EXCEEDED_BEHAVIOR_TYPE<stkobjects/LIMITS_EXCEEDED_BEHAVIOR_TYPE>
    ≔ ANTENNA_GRAPHICS_COORDINATE_SYSTEM<stkobjects/ANTENNA_GRAPHICS_COORDINATE_SYSTEM>
    ≔ ANTENNA_MODEL_INPUT_TYPE<stkobjects/ANTENNA_MODEL_INPUT_TYPE>
    ≔ HFSS_FFD_GAIN_TYPE<stkobjects/HFSS_FFD_GAIN_TYPE>
    ≔ ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE<stkobjects/ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE>
    ≔ BEAM_SELECTION_STRATEGY_TYPE<stkobjects/BEAM_SELECTION_STRATEGY_TYPE>
    ≔ TRANSMITTER_MODEL_TYPE<stkobjects/TRANSMITTER_MODEL_TYPE>
    ≔ TRANSFER_FUNCTION_TYPE<stkobjects/TRANSFER_FUNCTION_TYPE>
    ≔ RE_TRANSMITTER_OP_MODE<stkobjects/RE_TRANSMITTER_OP_MODE>
    ≔ RECEIVER_MODEL_TYPE<stkobjects/RECEIVER_MODEL_TYPE>
    ≔ LINK_MARGIN_TYPE<stkobjects/LINK_MARGIN_TYPE>
    ≔ RADAR_STC_ATTENUATION_TYPE<stkobjects/RADAR_STC_ATTENUATION_TYPE>
    ≔ RADAR_FREQUENCY_SPEC<stkobjects/RADAR_FREQUENCY_SPEC>
    ≔ RADAR_SNR_CONTOUR_TYPE<stkobjects/RADAR_SNR_CONTOUR_TYPE>
    ≔ RADAR_MODEL_TYPE<stkobjects/RADAR_MODEL_TYPE>
    ≔ RADAR_MODE_TYPE<stkobjects/RADAR_MODE_TYPE>
    ≔ RADAR_WAVEFORM_SEARCH_TRACK_TYPE<stkobjects/RADAR_WAVEFORM_SEARCH_TRACK_TYPE>
    ≔ RADAR_SEARCH_TRACK_PRF_MODE<stkobjects/RADAR_SEARCH_TRACK_PRF_MODE>
    ≔ RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE<stkobjects/RADAR_SEARCH_TRACK_PULSE_WIDTH_MODE>
    ≔ RADAR_SAR_PRF_MODE<stkobjects/RADAR_SAR_PRF_MODE>
    ≔ RADAR_SAR_RANGE_RESOLUTION_MODE<stkobjects/RADAR_SAR_RANGE_RESOLUTION_MODE>
    ≔ RADAR_SAR_PCR_MODE<stkobjects/RADAR_SAR_PCR_MODE>
    ≔ RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE<stkobjects/RADAR_SAR_PULSE_INTEGRATION_ANALYSIS_MODE_TYPE>
    ≔ RADAR_P_DET_TYPE<stkobjects/RADAR_P_DET_TYPE>
    ≔ RADAR_PULSE_INTEGRATION_TYPE<stkobjects/RADAR_PULSE_INTEGRATION_TYPE>
    ≔ RADAR_PULSE_INTEGRATOR_TYPE<stkobjects/RADAR_PULSE_INTEGRATOR_TYPE>
    ≔ RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE<stkobjects/RADAR_CONTINUOUS_WAVE_ANALYSIS_MODE_TYPE>
    ≔ RADAR_CLUTTER_GEOMETRY_MODEL_TYPE<stkobjects/RADAR_CLUTTER_GEOMETRY_MODEL_TYPE>
    ≔ RADAR_CLUTTER_MAP_MODEL_TYPE<stkobjects/RADAR_CLUTTER_MAP_MODEL_TYPE>
    ≔ RADAR_SWERLING_CASE<stkobjects/RADAR_SWERLING_CASE>
    ≔ RCS_COMPUTE_STRATEGY<stkobjects/RCS_COMPUTE_STRATEGY>
    ≔ RADAR_ACTIVITY_TYPE<stkobjects/RADAR_ACTIVITY_TYPE>
    ≔ RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION<stkobjects/RADAR_CROSS_SECTION_CONTOUR_GRAPHICS_POLARIZATION>
    ≔ RF_FILTER_MODEL_TYPE<stkobjects/RF_FILTER_MODEL_TYPE>
    ≔ MODULATOR_MODEL_TYPE<stkobjects/MODULATOR_MODEL_TYPE>
    ≔ DEMODULATOR_MODEL_TYPE<stkobjects/DEMODULATOR_MODEL_TYPE>
    ≔ RAIN_LOSS_MODEL_TYPE<stkobjects/RAIN_LOSS_MODEL_TYPE>
    ≔ ATMOSPHERIC_ABSORPTION_MODEL_TYPE<stkobjects/ATMOSPHERIC_ABSORPTION_MODEL_TYPE>
    ≔ URBAN_TERRESTRIAL_LOSS_MODEL_TYPE<stkobjects/URBAN_TERRESTRIAL_LOSS_MODEL_TYPE>
    ≔ CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE<stkobjects/CLOUDS_AND_FOG_FADING_LOSS_MODEL_TYPE>
    ≔ CLOUDS_AND_FOG_LIQUID_WATER_CHOICES<stkobjects/CLOUDS_AND_FOG_LIQUID_WATER_CHOICES>
    ≔ IONOSPHERIC_FADING_LOSS_MODEL_TYPE<stkobjects/IONOSPHERIC_FADING_LOSS_MODEL_TYPE>
    ≔ TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE<stkobjects/TROPOSPHERIC_SCINTILLATION_FADING_LOSS_MODEL_TYPE>
    ≔ TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES<stkobjects/TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES>
    ≔ PROJECTION_HORIZONTAL_DATUM_TYPE<stkobjects/PROJECTION_HORIZONTAL_DATUM_TYPE>
    ≔ BUILD_HEIGHT_REFERENCE_METHOD<stkobjects/BUILD_HEIGHT_REFERENCE_METHOD>
    ≔ BUILD_HEIGHT_UNIT<stkobjects/BUILD_HEIGHT_UNIT>
    ≔ TIREM_POLARIZATION_TYPE<stkobjects/TIREM_POLARIZATION_TYPE>
    ≔ VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE<stkobjects/VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE>
    ≔ VOACAP_COEFFICIENT_DATA_TYPE<stkobjects/VOACAP_COEFFICIENT_DATA_TYPE>
    ≔ LASER_PROPAGATION_LOSS_MODEL_TYPE<stkobjects/LASER_PROPAGATION_LOSS_MODEL_TYPE>
    ≔ LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE<stkobjects/LASER_TROPOSPHERIC_SCINTILLATION_LOSS_MODEL_TYPE>
    ≔ ATMOSPHERIC_TURBULENCE_MODEL_TYPE<stkobjects/ATMOSPHERIC_TURBULENCE_MODEL_TYPE>
    ≔ MODTRAN_AEROSOL_MODEL_TYPE<stkobjects/MODTRAN_AEROSOL_MODEL_TYPE>
    ≔ MODTRAN_CLOUD_MODEL_TYPE<stkobjects/MODTRAN_CLOUD_MODEL_TYPE>
    ≔ COMM_SYSTEM_REFERENCE_BANDWIDTH<stkobjects/COMM_SYSTEM_REFERENCE_BANDWIDTH>
    ≔ COMM_SYSTEM_CONSTRAINING_ROLE<stkobjects/COMM_SYSTEM_CONSTRAINING_ROLE>
    ≔ COMM_SYSTEM_SAVE_MODE<stkobjects/COMM_SYSTEM_SAVE_MODE>
    ≔ COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE<stkobjects/COMM_SYSTEM_ACCESS_EVENT_DETECTION_TYPE>
    ≔ COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE<stkobjects/COMM_SYSTEM_ACCESS_SAMPLING_METHOD_TYPE>
    ≔ COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE<stkobjects/COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE>
    ≔ SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY<stkobjects/SPACE_ENVIRONMENT_NASA_MODELS_ACTIVITY>
    ≔ SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY<stkobjects/SPACE_ENVIRONMENT_CRRES_PROTON_ACTIVITY>
    ≔ SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY<stkobjects/SPACE_ENVIRONMENT_CRRES_RADIATION_ACTIVITY>
    ≔ SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE<stkobjects/SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_MODE>
    ≔ SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE<stkobjects/SPACE_ENVIRONMENT_MAGNITUDE_FIELD_COLOR_SCALE>
    ≔ SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD<stkobjects/SPACE_ENVIRONMENT_MAGNETIC_MAIN_FIELD>
    ≔ SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD<stkobjects/SPACE_ENVIRONMENT_MAGNETIC_EXTERNAL_FIELD>
    ≔ SPACE_ENVIRONMENT_SAA_CHANNEL<stkobjects/SPACE_ENVIRONMENT_SAA_CHANNEL>
    ≔ SPACE_ENVIRONMENT_SAA_FLUX_LEVEL<stkobjects/SPACE_ENVIRONMENT_SAA_FLUX_LEVEL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL<stkobjects/VEHICLE_SPACE_ENVIRONMENT_SHAPE_MODEL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_F_10_P7_SOURCE>
    ≔ VEHICLE_SPACE_ENVIRONMENT_MATERIAL<stkobjects/VEHICLE_SPACE_ENVIRONMENT_MATERIAL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_COMPUTATION_MODE>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL<stkobjects/VEHICLE_SPACE_ENVIRONMENT_DOSE_CHANNEL>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY<stkobjects/VEHICLE_SPACE_ENVIRONMENT_DETECTOR_GEOMETRY>
    ≔ VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_DETECTOR_TYPE>
    ≔ VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE<stkobjects/VEHICLE_SPACE_ENVIRONMENT_AP_SOURCE>
    ≔ NOTIFICATION_FILTER_MASK<stkobjects/NOTIFICATION_FILTER_MASK>

