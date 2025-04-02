PySTK code snippets
###################

The following code snippets demonstrate tasks that are commonly encountered when working with the PySTK API.

How do I
========

Analysis Workbench
  - :ref:`Create a new collection of interval list <CreateCollectionList>`
  - :ref:`Create a new time interval <CreateTimeInterval>`
  - :ref:`Create a new time instant <CreateTimeInstant>`
  - :ref:`Get times from defined time instant and create an cell array <GetTimesFromTimeInstant>`
  - :ref:`Create a new orbit parameter set <CreateOrbitParameterSet>`
  - :ref:`Create a new attitude parameter set <CreateAttitudeParameterSet>`
  - :ref:`Get a scalar component and evaluate at a time <GetScalarAndEvaluate>`
  - :ref:`Create a data element scalar <CreateDataElementScalar>`
  - :ref:`Create a new vector magnitude scalar <CreateVectorMagScalar>`
  - :ref:`Create a new assembled system <CreateAssembledSystem>`
  - :ref:`Create a new aligned and constrained axes <CreateAlignedConstrainedAxes>`
  - :ref:`Create a new between vectors angle <CreateBetweenAngle>`
  - :ref:`Create a new fixed at time instant point <CreateFixedTimeInstantPoint>`
  - :ref:`Create a new model attachment point <CreateModelAttachmentPoint>`
  - :ref:`Create a new fixed in system point <CreateFixedPoint>`
  - :ref:`Create a new projection vector <CreateProjectionVector>`
  - :ref:`Create a new custom script vector <CreateScriptVector>`
  - :ref:`Create a new cross product vector <CreateCrossProductVector>`
  - :ref:`Create a new fixed in axes vector <CreateFixedAxesVector>`
  - :ref:`Create a new displacement vector <CreateDisplacementVector>`
  - :ref:`Get default vgt component on vehicle <GetVGTCompVehicle>`
  - :ref:`Get center point and inertial system of earth central body <GetVGTPoint>`
Camera
  - :ref:`Change camera reference frame <CameraReferenceFrame>`
  - :ref:`Change camera view to imagery extents <CameraExtents>`
Colors
  - :ref:`Get and set a four-channel color for the graphics of an STK object <GetSetRGBAColor>`
  - :ref:`Get and set a three-channel color for the graphics of an stk object <GetSetRGBColor>`
Connect
  - :ref:`Extract data from connect result <ResultsConnectCommand>`
  - :ref:`Use arrays to send and retrieve data with connect <ConnectCommandArrays>`
  - :ref:`Execute multiple connect commands <ConnectCommandMultiple>`
  - :ref:`Execute connect command <ConnectCommand>`
Graphics
  GlobeOverlays
    - :ref:`Control the lighting of the 3d scene <SceneLighting>`
    - :ref:`Control display of stars and water texture <DisplayStarsWater>`
    - :ref:`Add imagery and terrain to the scene <AddTerrainImagery>`

  - :ref:`Display a primitive during an interval <DisplayPrimitiveInterval>`
  - :ref:`Draw a solid cylinder primitive and set properties <SolidCylinderPrimitive>`
  - :ref:`Draw a solid ellipsoid primitive and set properties <SolidEllipsoidPrimitive>`
  - :ref:`Draw a solid box primitive and set properties <SolidBoxPrimitive>`
  - :ref:`Draw a point primitive and set properties <PointPrimitive>`
  - :ref:`Create a bounding sphere <BoundingSpherePrimitive>`
  - :ref:`Draw a new texture screen overlay <DrawNewTextureScreenOverlay>`
  - :ref:`Draw a new text primitive <TextPrimitive>`
  - :ref:`Draw a new surface extent triangulator <SurfaceExtentTriangulator>`
  - :ref:`Draw a new surface mesh <DrawNewSurfaceMeshPrimitive>`
  - :ref:`Great arc interpolator primitives <GreatArcInterpolatorPrimitives>`
  - :ref:`Combine intflag enumerations with the logical or operator <CylinderFillEnumeration>`
Initialization
  - :ref:`Attach to an already running stk runtime and get a reference to stk object root <AttachSTKRuntimeSnippet>`
  - :ref:`Start stk runtime and get a reference to stk object root <CreateSTKRuntimeNewSnippet>`
  - :ref:`Start stk desktop and get a reference to stk object root <CreateSTKNew>`
  - :ref:`Get a reference to stk object root using a running stk desktop instance <AttachSTK>`
  - :ref:`Initialize stk engine in no graphics mode and get a reference to stk object root <StartSTKEngineSnippetWithoutGfx>`
  - :ref:`Initialize stk engine with graphics and get a reference to stk object root <StartSTKEngineWithGfx>`
Scenario
  Scenario Management
    - :ref:`Change scenario font <ScenarioFont>`
    - :ref:`Reset the scenario time <ScenarioReset>`
    - :ref:`Change animation mode <ScenarioAnimationMode>`
    - :ref:`Set unit preferences for object model <SetUnitPreferences>`
    - :ref:`Create a new scenario <CreateScenario>`
    - :ref:`Close stk <CloseSTK>`
    - :ref:`Manage stk desktop events <STKDesktopEvents>`
    - :ref:`Manage stk engine events <STKEngineEvents>`
    - :ref:`Close an open scenario <CloseScenario>`
    - :ref:`Open a viewer data file <OpenVdfSTK>`
STK Objects
  Access
    - :ref:`Get access between objects by path using the existing accesses <GetAccesses>`
    - :ref:`Configure the access interval to the availability time span of the object where access is being computed to <ConfigureAccessIntervalAvailability>`
    - :ref:`Configure the access analysis time period to specified time instants <ConfigureAccessInterval>`
    - :ref:`Compute and extract access interval times <ExtractAccessIntervals>`
    - :ref:`Compute an access for one point <ComputeAccessPoint>`
    - :ref:`Compute access with advanced settings <ComputeAccessAdvancedSettings>`
    - :ref:`Compute an access between two stk objects (using object path) <ComputeAccessPaths>`
    - :ref:`Compute an access between two stk objects (using istkobject interface) <ComputeAccess>`
    - :ref:`Remove all access constraints except for line of sight <RemoveAllConstraints>`
    - :ref:`Add an exclusion zone access constraint <AddExclusionZoneConstraint>`
    - :ref:`Add multiple access constraints of the same type to an stk object <AddMultipleConstraint>`
    - :ref:`Add and configure an altitude access constraint <AddAltitudeConstraint>`
    - :ref:`Add and configure a central body obstruction access constraint <AddCbObstructionConstraint>`
    - :ref:`Add and configure a sun elevation angle access constraint <AddSunElevationAngleConstraint>`
    - :ref:`Add and configure a lunar elevation angle access constraint <AddLunarElevationAngleConstraint>`
    - :ref:`Add and configure a line of sight sun exclusion access constraint <AddSunExclusionConstraint>`
    - :ref:`Add and configure a lighting condition access constraint <AddLightingConstraint>`
    - :ref:`Return a list of available constraints <AvailableAccessConstraints>`
    - :ref:`Get handle to the object access constraints <AccessConstraints>`
  AdvCAT
    - :ref:`Create a new advcat object <CreateCAT>`
  Aircraft
    - :ref:`Set the attitude of the aircraft <AircraftAttitude>`
    - :ref:`Add array of waypoints to aircraft <AddAircraftArrayPoints>`
    - :ref:`Set great arc propagator and add individual waypoints to aircraft <AddAircraftPoints>`
    - :ref:`Create a new aircraft (on the current scenario central body) <CreateAircraft>`
  Area Target
    - :ref:`List all points in an area target <ListAreaTargetPoints>`
    - :ref:`Define area target boundary and position from list of lat/lon/alt (using common tasks) <CreateBoundaryAreaTargetList>`
    - :ref:`Define area target boundary and position from list of lat/lon/alt <CreateBoundaryAreaTarget>`
    - :ref:`Set an elliptical area target (using common tasks) <CreateAreaTargetCommon>`
    - :ref:`Set an elliptical area target <CreateEllipticalAreaTarget>`
    - :ref:`Create an area target (on the current scenario central body) <CreateAreaTarget>`
  Chain
    - :ref:`Prints the strand intervals of chain object <ChainStrandIntervals>`
    - :ref:`Define and compute a chain (advanced) <CreateChainAdvanced>`
    - :ref:`Define and compute a chain (basic) <ComputeChain>`
    - :ref:`Create a chain (on the current scenario central body) <CreateChain>`
  Constellation
    - :ref:`Define a constellation <CreateConstellation>`
  Coverage Definition
    - :ref:`Compute coverage <CoverageCompute>`
    - :ref:`Set advanced settings for coverage <CoverageAdvanced>`
    - :ref:`Set the coverage interval to an object's availability analysis interval <SetCoverageIntervalToAvailability>`
    - :ref:`Create a new coverage definition (on the current scenario central body) <CreateCoverage>`
  Data Providers
    - :ref:`Getting data for specific points and elements <SingleTimesDataProvider>`
    - :ref:`Getting data for a single point in time <SingleTimeDataProvider>`
    - :ref:`Extracting elements from data providers with pre-data <DataProviderPreData>`
    - :ref:`Extracting elements from data providers with groups <GroupsDataProvider>`
    - :ref:`Using a time dependent data provider and requesting only specified elements <TimeDependentDataProviderElements>`
    - :ref:`Using an interval data provider <IntervalDataProvider>`
  Facility
    Graphics
      - :ref:`Display the azel mask in 2d/3d <FacilityAzElMaskDisplay>`

    - :ref:`Add an azel mask to a facility <AzElMaskFacility>`
    - :ref:`Get the cartesian position of the facility <GetPositionFacility>`
    - :ref:`Set the geodetic position of the facility <SetPositionFacility>`
    - :ref:`Create a facility and set its height above ground level <SetHeightFacility>`
    - :ref:`Create a facility (on the current scenario central body) <CreateFacility>`
  Figure Of Merit
    - :ref:`Configure the contours of the fom and define a color ramp <FOMContoursColorRamp>`
    - :ref:`Create a new figure of merit of type access duration <CreateFOM>`
  Ground Vehicle
    - :ref:`Add array of waypoints to ground vehicle and interpolate over terrain <AddGroundVehicleArrayPoints>`
    - :ref:`Set great arc propagator and add individual waypoints to ground vehicle <AddGroundVehiclePoints>`
    - :ref:`Create a new ground vehicle (on the current scenario central body) <CreateVehicle>`
  Line Target
    - :ref:`Create a new line target (on the current scenario central body) <CreateLineTarget>`
  Missile
    - :ref:`Create a new missile (on the current scenario central body) <CreateMissile>`
  MTO
    - :ref:`Load mto track points from file <MTOLoadTrack>`
    - :ref:`Create a new mto (on the current scenario central body) <CreateMTO>`
  Object Coverage
    - :ref:`Compute object coverage <ComputeObjectCoverage>`
  Planet
    Graphics
      - :ref:`Modify planet 2d properties <ModifyPlanet2DGraphics>`

    - :ref:`Create a new planet <CreatePlanet>`
  Satellite
    Graphics
      - :ref:`Add a vector to display in 3d <AddGraphicsVector>`
      - :ref:`Add fixed system orbit system in 3d display <GraphicsOrbitSystem>`
      - :ref:`Modify the detail thresholds levels <GraphicsDetails>`
      - :ref:`Change the 3d model and marker properties <GraphicsModel>`
      - :ref:`Display drop lines in 3d window <GraphicsDropline>`
      - :ref:`Add a data display to the 3d window <GraphicsDataDisplay>`
      - :ref:`Change the display label of the vehicle <GraphicsLabel>`
      - :ref:`Set 2d/3d pass display properties <GraphicsPass>`
      - :ref:`Set vehicle lighting properties <GraphicsLighting>`
      - :ref:`Set 2d swath <GraphicsSwath>`
      - :ref:`Set 2d/3d range contours <GraphicsRangeContours>`
      - :ref:`Set 2d/3d elevation contours <GraphicsElevationContours>`
      - :ref:`Set 2d display times to custom and add intervals <CustomGraphics2D>`
      - :ref:`Set 2d graphics display properties <BasicGraphics2D>`
      - :ref:`Change the graphics resolution of the orbit for a smooth path <SatelliteGraphicsResolution>`
    Astrogator
      - :ref:`Run the astrogator mcs <AstrogatorRunMCS>`

    - :ref:`Set satellite attitude external <SatelliteAttitudeExternal>`
    - :ref:`Set satellite attitude targeting <SatelliteAttitudeTarget>`
    - :ref:`Set satellite attitude basic spinning <SatelliteAttitudeSpinning>`
    - :ref:`Export an ephemeris file to scenario folder <ExportEphemerisFile>`
    - :ref:`Set satellite propagator to sgp4 and propagate <SGP4Satellite>`
    - :ref:`Set satellite propagator to spice and propagate <SPICESatellite>`
    - :ref:`Set satellite propagator to astrogator and clear segments <AstrogatorSatellite>`
    - :ref:`Set satellite propagator to hpop and set force model properties <HPOPSatellite>`
    - :ref:`Set satellite propagator to j4 and assign cartesian position <J4Satellite>`
    - :ref:`Set initial state of satellite and propagate <SatelliteInitialState>`
    - :ref:`Create a satellite (on the current scenario central body) <CreateSatellite>`
  Sensor
    Graphics
      - :ref:`Sensor persistence <SensorPersistence>`

    - :ref:`Sensor body mask <SensorBodyMask>`
    - :ref:`Define sensor pointing fixed axes ypr <DefineSensorPointingFixedAxesYPR>`
    - :ref:`Define sensor pointing fixed ypr <DefineSensorPointingFixedYPR>`
    - :ref:`Define sensor pointing fixed axes quaternion <DefineSensorPointingFixedAxesQuaternion>`
    - :ref:`Define sensor pointing fixed quaternion <DefineSensorPointingFixedQuaternion>`
    - :ref:`Define sensor pointing fixed axes euler <DefineSensorPointingFixedAxesEuler>`
    - :ref:`Define sensor pointing fixed euler <DefineSensorPointingFixedEuler>`
    - :ref:`Define sensor pointing fixed axes azel <DefineSensorPointingFixedAxesAzEl>`
    - :ref:`Define sensor pointing fixed azel <DefineSensorPointingFixedAzEl>`
    - :ref:`Set sensor properties <SensorProperties>`
    - :ref:`Attach a sensor object to a vehicle <CreateSensor>`
  Communications
    Antenna
      - :ref:`Modify antenna graphics <ModifyAntennaGraphics>`
      - :ref:`Modify antenna orientation and position <ModifyAntennaOrientation>`
      - :ref:`Modify antenna refraction <ModifyAntennaRefraction>`
      - :ref:`Modify antenna model type <ModifyAntenna>`
      - :ref:`Create a new antenna object <CreateAntenna>`
    Receiver
      - :ref:`Receiver additional gain <ReceiverAdditionalGain>`
      - :ref:`Modify receiver filter properties <ModifyReceiverFilter>`
      - :ref:`Modify receiver demodulator properties <ModifyReceiverDemodulator>`
      - :ref:`Modify receiver system noise temperature <ModifyReceiverSysNoiseTemp>`
      - :ref:`Modify orientation of the receiver antenna <ModifyReceiverOrientation>`
      - :ref:`Modify receiver polarization properties <ModifyReceiverPolarization>`
      - :ref:`Modify receiver embedded antenna <ModifyReceiverAntenna>`
      - :ref:`Modify receiver model type <ModifyReceiverModel>`
      - :ref:`Create a new receiver object <CreateReceiver>`
    Transmitter
      - :ref:`Transmitter additional gain <TransmitteradditionalGain>`
      - :ref:`Modify transmitter filter <ModifyTransmitterFilter>`
      - :ref:`Modify transmitter modulator properties <ModifyTransmitterModulator>`
      - :ref:`Modify transmitter orientation and position <ModifyTransmitterPolarizationOrientationAndPosition>`
      - :ref:`Modify transmitter polarization properties <ModifyTransmitterPolarizationProperties>`
      - :ref:`Modify transmitter embedded antenna <ModifyTransmitterAntenna>`
      - :ref:`Modify transmitter model type <ModifyTransmitter>`
      - :ref:`Create a new transmitter object <CreateTransmitter>`
  Vehicles
    Common
      Propagators
        Aviator
          - :ref:`Configure the advanced fixed wing tool and set the aircraft to use the resulting performance models <SetupAdvancedFixedWingTool>`
          - :ref:`Set the configuration used for the mission <SetTheConfiguration>`
          - :ref:`Set the aircraft used for the mission to an aircraft found in the aviator catalog <SetAviatorVehicle>`
          - :ref:`Create a new performance model for an aircraft <CreatePerformanceModel>`
          - :ref:`Configure the weather and atmosphere of the mission <ConfigureWeatherAtmosphere>`
          - :ref:`Configure a runway site <ConfigureRunwaySite>`
          - :ref:`Configure a runway site from a runway in the aviator catalog <ConfigureRunwayFromCatalog>`
          - :ref:`Configure the wind and atmosphere for a procedure <ConfigureProcedureWindAtmos>`
          - :ref:`Configure a procedure time options <ConfigureProcedureTimeOptions>`
          - :ref:`Rename a procedure and its site <ConfigureProcedure>`
          - :ref:`Configure the performance models to be used in the phase <ConfigurePhasePerformanceModels>`
          - :ref:`Configure the basic cruise performance model of an aircraft <ConfigureBasicCruisePerfModel>`
          - :ref:`Configure the basic acceleration performance model of an aircraft <ConfigureBasicAccelerationPerfModel>`
          - :ref:`Configure the aviator propagator <ConfigureAviatorPropagator>`
          - :ref:`Add a takeoff procedure from a runway <AddTakeoffProcedure>`
          - :ref:`Add a new phase and use the same performance models as the first phase <AddPhase>`
          - :ref:`Add and configure a landing procedure <AddLandingProcedure>`
          - :ref:`Add and configure an en-route procedure <AddEnrouteProcedure>`
          - :ref:`Add and configure a basic maneuver procedure <AddBasicManeuverProcedure>`
          - :ref:`Add and remove procedures <AddAndRemoveProcedures>`


.. _CreateCollectionList:

Create a new collection of interval list
========================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryPoint centerPtSat: point component
    timeCollListFactory = vgtSat.time_interval_collections.factory
    timeColl = timeCollListFactory.create_lighting("LightingList", "Collection of lighting intervals")
    timeColl.use_object_eclipsing_bodies = True
    timeColl.location = centerPtSat

.. _CreateTimeInterval:

Create a new time interval
==========================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Change DateFormat dimension to epoch seconds to make the time easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    timeIntFactory = vgtSat.time_intervals.factory
    timeInterval = timeIntFactory.create_fixed("TimeInterval", "Fixed time interval")
    timeInterval.set_interval(60, 120)

.. _CreateTimeInstant:

Create a new time instant
=========================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Change DateFormat dimension to epoch seconds to make the time easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    timeInstFactory = vgtSat.time_instants.factory
    timeEpoch = timeInstFactory.create_epoch("FixedTime", "Fixed Epoch Time")
    timeEpoch.epoch = 3600

.. _GetTimesFromTimeInstant:

Get times from defined time instant and create an cell array
============================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Change DateFormat dimension to epoch seconds to make the time easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    satStart = vgtSat.time_instants.item("AvailabilityStartTime")
    start = satStart.find_occurrence().epoch

    satStop = vgtSat.time_instants.item("AvailabilityStopTime")
    stop = satStop.find_occurrence().epoch
    interval = [[start], [540], [600], [stop]]  # EpSec

.. _CreateOrbitParameterSet:

Create a new orbit parameter set
================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    paraFactory = vgtSat.parameter_sets.factory
    paraSetOribit = paraFactory.create("orbitSun", "Orbit", ParameterSetType.ORBIT)
    paraSetOribit.orbiting_point = vgtSat.points.item("Center")
    paraSetOribit.central_body = "Sun"
    paraSetOribit.use_central_body_gravitational_parameter = False
    paraSetOribit.gravitational_parameter = 398600  # km^3/sec^2

.. _CreateAttitudeParameterSet:

Create a new attitude parameter set
===================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryToolAxes bodyAxes: axes component
    # IVectorGeometryToolAxes icrfAxes: axes component
    paraFactory = vgtSat.parameter_sets.factory
    paraSet = paraFactory.create("attitudeICRF", "Attitude Set", ParameterSetType.ATTITUDE)
    paraSet.axes = bodyAxes
    paraSet.reference_axes = icrfAxes

.. _GetScalarAndEvaluate:

Get a scalar component and evaluate at a time
=============================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Scenario scenario: Scenario object
    deticLatitude = vgtSat.calculation_scalars.item("GroundTrajectory.Detic.LLA.Latitude")
    result = deticLatitude.evaluate(scenario.start_time)
    print("The value of detic latitude is %s" % result.value)

.. _CreateDataElementScalar:

Create a data element scalar
============================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    calcFactory = vgtSat.calculation_scalars.factory
    trueAnom = calcFactory.create("TrueAnomaly", "", CalculationScalarType.DATA_ELEMENT)
    trueAnom.set_with_group("Classical Elements", "ICRF", "True Anomaly")

.. _CreateVectorMagScalar:

Create a new vector magnitude scalar
====================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    calcFactory = vgtSat.calculation_scalars.factory
    displScalar = calcFactory.create_vector_magnitude(
        "VectorDisplacement", "Vector Magnitude of Displacement Vector"
    )
    displScalar.input_vector = Sat2EarthCenter

.. _CreateAssembledSystem:

Create a new assembled system
=============================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryPointFixedInSystem fixedPt: point component
    # IVectorGeometryToolAxes bodyAxes: axes component
    SysFactory = vgtSat.systems.factory
    assemSys = SysFactory.create("FixedPtSystem", "System with origin at the new point", SystemType.ASSEMBLED)
    assemSys.origin_point.set_point(fixedPt)
    assemSys.reference_axes.set_axes(bodyAxes)

.. _CreateAlignedConstrainedAxes:

Create a new aligned and constrained axes
=========================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    # VectorGeometryToolVectorFixedInAxes bodyYSat: vector component
    AxesFactory = vgtSat.axes.factory
    AlignConstain = AxesFactory.create(
        "AlignConstrain",
        "Aligned to displacement vector and constrained to Body Y",
        AxesType.ALIGNED_AND_CONSTRAINED,
    )
    AlignConstain.alignment_reference_vector.set_vector(Sat2EarthCenter)
    AlignConstain.alignment_direction.assign_xyz(1, 0, 0)
    AlignConstain.constraint_reference_vector.set_vector(bodyYSat)
    AlignConstain.constraint_direction.assign_xyz(0, 0, 1)

.. _CreateBetweenAngle:

Create a new between vectors angle
==================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    # VectorGeometryToolVectorFixedInAxes bodyYSat: vector component
    AngFactory = vgtSat.angles.factory
    betwVect = AngFactory.create("SatEarth2Y", "Displacement Vector to Sat Body Y", AngleType.BETWEEN_VECTORS)
    betwVect.from_vector.set_vector(Sat2EarthCenter)
    betwVect.to_vector.set_vector(bodyYSat)

.. _CreateFixedTimeInstantPoint:

Create a new fixed at time instant point
========================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolSystemAssembled icrf: system component
    PtFactory = vgtSat.points.factory
    timeInstantPt = PtFactory.create("AtTimePt", "Point at time instant", PointType.AT_TIME_INSTANT)
    timeInstantPt.source_point = vgtSat.points.item("Center")
    timeInstantPt.reference_system = icrf
    timeInstantPt.reference_time_instant = vgtSat.time_instants.item("AvailabilityStartTime")

.. _CreateModelAttachmentPoint:

Create a new model attachment point
===================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    PtFactory = vgtSat.points.factory
    modelPt = PtFactory.create("ModelPt", "Attach point defined in model", PointType.MODEL_ATTACHMENT)
    modelPt.pointable_element_name = "MainSensor-000000"

.. _CreateFixedPoint:

Create a new fixed in system point
==================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    PtFactory = vgtSat.points.factory
    fixedPt = PtFactory.create("FixedPt", "Point offset from Center", PointType.FIXED_IN_SYSTEM)
    fixedPt.fixed_point.assign_cartesian(0.005, 0, 0.005)

.. _CreateProjectionVector:

Create a new projection vector
==============================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    VectFactory = vgtSat.vectors.factory
    projectionVector = VectFactory.create("Projection", "", VectorType.PROJECTION)
    projectionVector.source.set_vector(Sat2EarthCenter)
    horizontalPlane = vgtSat.planes.item("LocalHorizontal")
    projectionVector.reference_plane.set_plane(horizontalPlane)

.. _CreateScriptVector:

Create a new custom script vector
=================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    VectFactory = vgtSat.vectors.factory
    customScript = VectFactory.create("Script", "Description", VectorType.CUSTOM_SCRIPT)
    # Initialization script if needed
    # customScript.InitializationScriptFile = ''
    customScript.script_file = r"C:\Program Files\AGI\STK 12\Data\Resources\stktraining\samples\Heliograph\Scripting\VectorTool\Vector\vector.vbs"
    if customScript.is_valid is False:
        print("Script component not valid!")
        from os import getenv

        print(
            r"Copy vbs file from C:\Program Files\AGI\STK 12\Data\Resources\stktraining\samples\Heliograph\Scripting\VectorTool\Vector\vector.vbs to C:\Users\%s\Documents\STK 12\Config\Scripting\VectorTool"
            % getenv("USERNAME")
        )

.. _CreateCrossProductVector:

Create a new cross product vector
=================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    # VectorGeometryToolVectorDisplacement fixedAxesVector: vector component
    VectFactory = vgtSat.vectors.factory
    lineOfNodesVector = VectFactory.create_cross_product("CrossProduct", Sat2EarthCenter, fixedAxesVector)

.. _CreateFixedAxesVector:

Create a new fixed in axes vector
=================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryToolAxes bodyAxes: axes component
    VectFactory = vgtSat.vectors.factory
    fixedAxesVector = VectFactory.create("FixedInAxes", "", VectorType.FIXED_IN_AXES)
    fixedAxesVector.reference_axes.set_axes(bodyAxes)
    fixedAxesVector.direction.assign_xyz(0, 0, 1)

.. _CreateDisplacementVector:

Create a new displacement vector
================================

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryPoint centerPtSat: point component
    # IVectorGeometryPoint centerPtEarth: point component
    VectFactory = vgtSat.vectors.factory
    Sat2EarthCenter = VectFactory.create_displacement_vector("Sat2EarthCenter", centerPtSat, centerPtEarth)

.. _GetVGTCompVehicle:

Get default VGT component on vehicle
====================================

.. code-block:: python

    # Satellite satellite: Satellite object
    vgtSat = satellite.analysis_workbench_components
    # Get handle to the Center point on the satellite
    centerPtSat = vgtSat.points.item("Center")
    # Get handle to the Body Y Vector
    bodyYSat = vgtSat.vectors.item("Body.Y")
    # Get handle to the Body Axes
    bodyAxes = vgtSat.axes.item("Body")
    icrfAxes = vgtSat.axes.item("ICRF")

.. _GetVGTPoint:

Get center point and inertial system of Earth central body
==========================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    centerPtEarth = root.central_bodies.earth.analysis_workbench_components.points.item("Center")
    icrf = root.central_bodies.earth.analysis_workbench_components.systems.item("ICRF")

.. _CameraReferenceFrame:

Change camera reference frame
=============================

.. code-block:: python

    # Scenario scenario: Scenario object
    # StkObjectRoot root: STK Object Model Root
    manager = scenario.scene_manager
    manager.scenes.item(0).camera.view_central_body(
        "Earth", root.central_bodies.earth.analysis_workbench_components.axes.item("Fixed")
    )
    manager.render()

.. _CameraExtents:

Change camera view to imagery extents
=====================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # AGIProcessedImageGlobeOverlay imageryTile: Image Overlay object
    manager = scenario.scene_manager
    extent = imageryTile.extent
    # Change extent in the default 3D window
    manager.scenes.item(0).camera.view_extent("Earth", extent)
    manager.render()

.. _GetSetRGBAColor:

Get and set a four-channel color for the graphics of an STK object
===================================================================

.. code-block:: python

    from ansys.stk.core.utilities.colors import Colors, ColorRGBA

    manager = root.current_scenario.scene_manager
    point = manager.initializers.point_batch_primitive.initialize()

    lla_pts = [ 39.88, -75.25, 0,
                38.85, -77.04, 0,
                37.37, -121.92, 0 ]

    colors = [ Colors.Red,
            ColorRGBA(Colors.Blue, 127),
            Colors.from_rgba(0, 255, 0, 127) ]

    point.set_cartographic_with_colors('Earth', lla_pts, colors)

.. _GetSetRGBColor:

Get and set a three-channel color for the graphics of an STK object
===================================================================

.. code-block:: python

    from ansys.stk.core.stkobjects import STKObjectType
    from ansys.stk.core.utilities.colors import Color, Colors

    facility = root.current_scenario.children.new(STKObjectType.FACILITY, "facility1")

    facility.graphics.color = Colors.Blue
    facility.graphics.color = Color.from_rgb(127, 255, 212)
    (r, g, b) = facility.graphics.color.get_rgb()

.. _ResultsConnectCommand:

Extract data from connect result
================================

.. code-block:: python

    result = root.execute_command('Report_RM */Place/MyPlace Style "Cartesian Position"')

    for i in range(0, result.count):
        cmdRes = result.item(i)
        print(cmdRes)

.. _ConnectCommandArrays:

Use arrays to send and retrieve data with connect
=================================================

.. code-block:: python

    from ansys.stk.core.stkutil import ExecuteMultipleCommandsMode

    connect_commands = ['GetStkVersion /', 'New / Scenario ExampleScenario']
    command_results = root.execute_multiple_commands(connect_commands, ExecuteMultipleCommandsMode.CONTINUE_ON_ERROR)

    first_message = command_results.item(0)
    also_first_message = command_results[0]

    for message in command_results:
        print(message.count)

.. _ConnectCommandMultiple:

Execute multiple connect commands
=================================

.. code-block:: python

    commandList = [["New / */Place MyPlace"], ["SetPosition */Place/MyPlace Geodetic 37.9 -75.5 0.0"]]
    root.execute_multiple_commands(commandList, ExecuteMultipleCommandsMode.EXCEPTION_ON_ERROR)

.. _ConnectCommand:

Execute connect command
=======================

.. code-block:: python

    root.execute_command("New / */Target MyTarget")

.. _DisplayPrimitiveInterval:

Display a primitive during an interval
======================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # ModelPrimitive model: Graphics Primitive
    manager = scenario.scene_manager
    composite = manager.initializers.composite_display_condition.initialize()
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    start = root.conversion_utility.new_date("EpSec", str(scenario.start_time))
    stop = root.conversion_utility.new_date("EpSec", str(scenario.start_time + 600))
    timeInterval = manager.initializers.time_interval_display_condition.initialize_with_times(start, stop)
    composite.add(timeInterval)
    model.display_condition = composite

.. _SolidCylinderPrimitive:

Draw a solid cylinder primitive and set properties
==================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    originCylinder = root.conversion_utility.new_position_on_earth()
    originCylinder.assign_geodetic(0, 7, 100)

    orientCylinder = root.conversion_utility.new_orientation()
    orientCylinder.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

    cylinder = manager.initializers.cylinder_triangulator.create_simple(200, 100)
    solidCylinder = manager.initializers.solid_primitive.initialize()
    solidCylinder.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item("Fixed")
    solidCylinder.position = originCylinder.query_cartesian_array()
    solidCylinder.set_with_result(cylinder)
    solidCylinder.color = Colors.Lime
    solidCylinder.outline_color = Colors.Blue
    solidCylinder.outline_width = 3
    solidCylinder.translucency = 0.75
    solidCylinder.rotation = orientCylinder
    manager.primitives.add(solidCylinder)
    manager.render()

.. _SolidEllipsoidPrimitive:

Draw a solid ellipsoid primitive and set properties
===================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    originEllipsoid = root.conversion_utility.new_position_on_earth()
    originEllipsoid.assign_geodetic(0, 5, 100)

    orientEllipsoid = root.conversion_utility.new_orientation()
    orientEllipsoid.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

    radii = [[200], [100], [100]]
    ellipsoid = manager.initializers.ellipsoid_triangulator.compute_simple(radii)
    solidEllipsoid = manager.initializers.solid_primitive.initialize()
    solidEllipsoid.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item(
        "Fixed"
    )  # vgtSat.Systems.item('Body')
    solidEllipsoid.position = originEllipsoid.query_cartesian_array()
    solidEllipsoid.set_with_result(ellipsoid)
    solidEllipsoid.color = Colors.White
    solidEllipsoid.outline_color = Colors.DeepPink
    solidEllipsoid.translucency = 0.75
    solidEllipsoid.rotation = orientEllipsoid
    manager.primitives.add(solidEllipsoid)
    manager.render()

.. _SolidBoxPrimitive:

Draw a solid box primitive and set properties
=============================================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    originBox = root.conversion_utility.new_position_on_earth()
    originBox.assign_geodetic(0, 3, 100)

    orientBox = root.conversion_utility.new_orientation()
    orientBox.assign_az_el(0, 0, AzElAboutBoresight.ROTATE)

    size = [[100], [100], [200]]
    result = manager.initializers.box_triangulator.compute(size)
    solidBox = manager.initializers.solid_primitive.initialize()
    solidBox.reference_frame = root.central_bodies.earth.analysis_workbench_components.systems.item("Fixed")
    solidBox.position = originBox.query_cartesian_array()
    solidBox.set_with_result(result)
    solidBox.color = Colors.Red
    solidBox.outline_color = Colors.Cyan
    solidBox.translucency = 0.75
    solidBox.rotation = orientBox
    manager.primitives.add(solidBox)
    manager.render()

.. _PointPrimitive:

Draw a point primitive and set properties
=========================================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    point = manager.initializers.point_batch_primitive.initialize()
    ptPosition = [[0], [-1], [0]]  # Lat, Lon, Alt

    point.set_cartographic("Earth", ptPosition)
    point.pixel_size = 15
    point.color = Colors.Lime
    point.display_outline = True
    point.outline_width = 5
    point.outline_color = Colors.Red

    manager.primitives.add(point)
    # Render the Scene
    manager.render()

.. _BoundingSpherePrimitive:

Create a bounding sphere
========================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    sphere = manager.initializers.bounding_sphere.initialize([[-1061.22], [-5773.98], [4456.04]], 100)

.. _DrawNewTextureScreenOverlay:

Draw a new texture screen overlay
=================================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    overlays = manager.screen_overlays.overlays
    textureOverlay = manager.initializers.texture_screen_overlay.initialize_with_xy_width_height(0, 0, 128, 128)
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    textureOverlay.texture = manager.textures.load_from_string_uri(
        os.path.join(installPath, "STKData", "VO", "Textures", "agilogo3.ppm")
    )
    textureOverlay.maintain_aspect_ratio = True
    textureOverlay.origin = ScreenOverlayOrigin.TOP_LEFT
    textureOverlay.position = [
        [0],
        [20],
        [int(ScreenOverlayUnit.PIXEL)],
        [int(ScreenOverlayUnit.PIXEL)],
    ]
    overlays.add(textureOverlay)
    # Render the Scene
    manager.render()

.. _TextPrimitive:

Draw a new text primitive
=========================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    font = manager.initializers.graphics_font.initialize_with_name_size_font_style_outline(
        "MS Sans Serif", 24, FontStyle.BOLD, True
    )
    textBatch = manager.initializers.text_batch_primitive.initialize_with_graphics_font(font)
    textBatch.set_cartographic("Earth", [[0], [0], [0]], ["Example Text"])  # Lat, Lon, Alt
    manager.primitives.add(textBatch)

.. _SurfaceExtentTriangulator:

Draw a new surface extent triangulator
======================================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    texture_path = os.path.join(installPath, "STKData", "VO", "Textures", "AGI_logo_small.png")
    texture = manager.textures.load_from_string_uri(texture_path)
    mesh = manager.initializers.surface_mesh_primitive.initialize()
    mesh.texture = texture
    mesh.translucency = 0
    cartographicExtent = [[-55], [10], [-24], [30]]

    triangles = manager.initializers.surface_extent_triangulator.compute_simple("Earth", cartographicExtent)
    mesh.set(triangles)
    mesh.translucency = 0.25
    c0 = [[10], [-55]]
    c1 = [[30], [-55]]
    c2 = [[30], [-24]]
    c3 = [[10], [-24]]

    mesh.texture_matrix = manager.initializers.texture_matrix.initialize_with_rectangles(c0, c1, c2, c3)
    mesh.transparent_texture_border = True
    manager.primitives.add(mesh)
    manager.render()

.. _DrawNewSurfaceMeshPrimitive:

Draw a new surface mesh
=======================

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    cartesianPts = [
        [6030.721052],
        [1956.627139],
        [-692.397578],
        [5568.375825],
        [2993.600713],
        [-841.076362],
        [5680.743568],
        [2490.379622],
        [-1480.882721],
    ]  # X, Y, Z (km)

    triangles = manager.initializers.surface_polygon_triangulator.compute("Earth", cartesianPts)
    surfaceMesh = manager.initializers.surface_mesh_primitive.initialize()
    surfaceMesh.color = Colors.Red
    surfaceMesh.set(triangles)
    manager.primitives.add(surfaceMesh)
    manager.render()

.. _GreatArcInterpolatorPrimitives:

Great arc interpolator primitives
=================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # Create a array of LLA values and interoplate them over the specified
    # central body
    positionArray = [[35.017], [-118.540], [0], [44.570], [-96.474], [0], [31.101], [-82.619], [0]]
    manager = scenario.scene_manager
    # Interpolate points over great arc
    interpolator = manager.initializers.great_arc_interpolator.initialize_with_central_body("Earth")
    interpolator.granularity = 0.1
    result = interpolator.interpolate(positionArray)

.. _CylinderFillEnumeration:

Combine intflag enumerations with the logical or operator
=========================================================

.. code-block:: python

    from ansys.stk.core.graphics import CylinderFillOptions

    # CylinderFillOptions inherits from enum.IntFlag and may be combined
    # using the `|` operator
    cyl_fill = CylinderFillOptions.BOTTOM_CAP | CylinderFillOptions.TOP_CAP

.. _AttachSTKRuntimeSnippet:

Attach to an already running STK runtime and get a reference to STK object root
===============================================================================

.. code-block:: python

    # Attach to already running instance of STK Runtime
    from ansys.stk.core.stkruntime import STKRuntime

    stk = STKRuntime.attach_to_application()

    # Get the STK Object Root interface
    root = stk.new_object_root()

.. _CreateSTKRuntimeNewSnippet:

Start STK runtime and get a reference to STK object root
========================================================

.. code-block:: python

    # Start new instance of STK Runtime
    from ansys.stk.core.stkruntime import STKRuntime

    stk = STKRuntime.start_application()

    # Get the STK Object Root interface
    root = stk.new_object_root()

.. _CreateSTKNew:

Start STK desktop and get a reference to STK object root
========================================================

.. code-block:: python

    # Start new instance of STK Desktop
    from ansys.stk.core.stkdesktop import STKDesktop

    stk = STKDesktop.start_application(visible=True)  # using optional visible argument

    # Get the STK Object Root interface
    root = stk.root

    # ...

    # Clean-up when done
    stk.shutdown()

.. _AttachSTK:

Get a reference to STK object root using a running STK desktop instance
=======================================================================

.. code-block:: python

    # Get reference to running STK Desktop instance
    from ansys.stk.core.stkdesktop import STKDesktop

    stk = STKDesktop.attach_to_application()

    # Get the STK Object Root interface
    root = stk.root

.. _StartSTKEngineSnippetWithoutGfx:

Initialize STK Engine in no graphics mode and get a reference to STK object root
================================================================================

.. code-block:: python

    # Initialize STK Engine without graphics in the current process
    from ansys.stk.core.stkengine import STKEngine

    stk = STKEngine.start_application(no_graphics=True)

    # Get the STK Object Root interface
    root = stk.new_object_root()

.. _StartSTKEngineWithGfx:

Initialize STK Engine with graphics and get a reference to STK object root
==========================================================================

.. code-block:: python

    # Initialize STK Engine with graphics in the current process
    from ansys.stk.core.stkengine import STKEngine

    stk = STKEngine.start_application(no_graphics=False)

    # Get the STK Object Root interface
    root = stk.new_object_root()

.. _SceneLighting:

Control the lighting of the 3D scene
====================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # Modify the lighting levels
    manager = scenario.scene_manager
    lighting = manager.scenes.item(0).lighting
    lighting.ambient_intensity = 0.20  # Percent
    lighting.diffuse_intensity = 4  # Percent
    lighting.night_lights_intensity = 5  # Percent

.. _DisplayStarsWater:

Control display of stars and water texture
==========================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # Turn off the stars and water texture
    manager = scenario.scene_manager
    manager.scenes.item(0).show_stars = False
    manager.scenes.item(0).show_water_surface = False

.. _AddTerrainImagery:

Add imagery and terrain to the scene
====================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # Retrieve the boundaries of the imported files
    manager = scenario.scene_manager
    # Add Terrain
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    terrainTile = manager.scenes.item(0).central_bodies.earth.terrain.add_uri_string(
        os.path.join(installPath, "Data", "Resources", "stktraining", "samples", "SRTM_Skopje.pdtt")
    )
    extentTerrain = terrainTile.extent
    print(
        "Terrain boundaries: LatMin: %s LatMax: %s LonMin: %s LonMax: %s"
        % (str(extentTerrain[0]), str(extentTerrain[2]), str(extentTerrain[1]), str(extentTerrain[3]))
    )
    # Add Imagery
    imageryTile = manager.scenes.item(0).central_bodies.earth.imagery.add_uri_string(
        os.path.join(installPath, "Data", "Resources", "stktraining", "imagery", "NPS_OrganPipeCactus_Map.pdttx")
    )
    extentImagery = imageryTile.extent
    print(
        "Imagery boundaries: LatMin: %s LatMax: %s LonMin: %s LonMax: %s"
        % (str(extentImagery[0]), str(extentImagery[2]), str(extentImagery[1]), str(extentImagery[3]))
    )

.. _ScenarioFont:

Change scenario font
====================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    scenario = root.current_scenario
    scenario.graphics_3d.medium_font.name = "Arial"
    scenario.graphics_3d.medium_font.point_size = 18
    scenario.graphics_3d.medium_font.bold = True
    scenario.graphics_3d.medium_font.italic = False

.. _ScenarioReset:

Reset the scenario time
=======================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.rewind()

.. _ScenarioAnimationMode:

Change animation mode
=====================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    scenario = root.current_scenario
    root.animation_options = AnimationOptionType.STOP
    root.mode = AnimationEndTimeMode.X_REAL_TIME
    scenario.animation_settings.animation_step_value = 1  # second
    scenario.animation_settings.refresh_delta = 0.03  # second

.. _SetUnitPreferences:

Set unit preferences for object model
=====================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.units_preferences.item("DateFormat").set_current_unit("UTCG")
    root.units_preferences.item("Distance").set_current_unit("km")

.. _CreateScenario:

Create a new scenario
=====================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.new_scenario("Example_Scenario")

.. _CloseSTK:

Close STK
=========

.. code-block:: python

    # AgUiApplication uiApplication: STK Application
    uiApplication.shutdown()

.. _STKDesktopEvents:

Manage STK desktop events
=========================

.. code-block:: python

    from ansys.stk.core.stkdesktop import STKDesktop
    from ansys.stk.core.stkobjects import STKObjectType

    def on_stk_object_added_custom_callback(path:str):
        print(f'{path} has been added.')

    stk = STKDesktop.start_application(visible=True)
    root = stk.root
    root.new_scenario('ExampleScenario')
    skt_object_root_events = root.subscribe()
    skt_object_root_events.on_stk_object_added += on_stk_object_added_custom_callback
    scenario = root.current_scenario

    # on_stk_object_added_custom_callback is successfully called when the next line is executed
    facility = scenario.children.new(STKObjectType.FACILITY, 'AGI_HQ')

    # Now switch control to the desktop application and create another facility.
    # The user interface becomes unresponsive.

    # Now open a tkinter window that processing COM messages.
    from tkinter import Tk

    window = Tk()
    window.mainloop()

.. _STKEngineEvents:

Manage STK Engine events
========================

.. code-block:: python

    from ansys.stk.core.stkengine import STKEngine

    def on_scenario_new_custom_callback(path:str):
        print(f'Scenario {path} has been created.')

    stk = STKEngine.start_application()
    root = stk.new_object_root()
    skt_object_root_events = root.subscribe()
    skt_object_root_events.on_scenario_new += on_scenario_new_custom_callback

    root.new_scenario('ExampleScenario')
    # callback should be executed now

    # remove the callback from the handler
    skt_object_root_events.on_scenario_new -= on_scenario_new_custom_callback

    # all finished with events, unsubscribe
    skt_object_root_events.unsubscribe()

.. _CloseScenario:

Close an open scenario
======================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.close_scenario()

.. _OpenVdfSTK:

Open a viewer data file
=======================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    root.load_vdf(os.path.join(installPath, "Data", "ExampleScenarios", "Intro_STK_Space_Systems.vdf"), "")

.. _GetAccesses:

Get access between objects by path using the existing accesses
==============================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    scenario = root.current_scenario
    accesses = scenario.get_existing_accesses()

    size = len(accesses)  # number of accesses

    object1 = accesses[0][0]  # e.g. "Satellite/MySatellite"
    object2 = accesses[0][1]  # e.g.  "Facility/MyFacility"
    computed = accesses[0][2]  # e.g. True  (if access has been computed)

    access = scenario.get_access_between_objects_by_path(object1, object2)

.. _ConfigureAccessIntervalAvailability:

Configure the access interval to the availability time span of the object where access is being computed to
===========================================================================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root

    satellite = root.get_object_from_path("Satellite/MySatellite")
    facility = root.get_object_from_path("Facility/MyFacility")
    access = satellite.get_access_to_object(facility)

    access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
    accessTimePeriod = access.access_time_period_data

    if satellite.analysis_workbench_components.time_intervals.contains("AvailabilityTimeSpan"):
        availabilityTimeSpan = satellite.analysis_workbench_components.time_intervals.item("AvailabilityTimeSpan")
        accessTimePeriod.access_interval.set_implicit_interval(availabilityTimeSpan)

.. _ConfigureAccessInterval:

Configure the access analysis time period to specified time instants
====================================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root

    satellite = root.get_object_from_path("Satellite/MySatellite")
    facility = root.get_object_from_path("Facility/MyFacility")

    # For this code snippet, let's use the time interval when the satellite reached min and max altitude values.
    # Note, this assumes time at min happens before time at max.
    timeOfAltMin = satellite.analysis_workbench_components.time_instants.item(
        "GroundTrajectory.Detic.LLA.Altitude.TimeOfMin"
    )
    timeOfAltMax = satellite.analysis_workbench_components.time_instants.item(
        "GroundTrajectory.Detic.LLA.Altitude.TimeOfMax"
    )

    # Set the access time period with the times we figured out above.
    access = satellite.get_access_to_object(facility)
    access.access_time_period = AccessTimeType.SPECIFIED_TIME_PERIOD
    accessTimePeriod = access.access_time_period_data

    accessTimePeriod.access_interval.state = SmartIntervalState.START_STOP

    accessStartEpoch = accessTimePeriod.access_interval.get_start_epoch()
    accessStartEpoch.set_implicit_time(timeOfAltMin)
    accessTimePeriod.access_interval.set_start_epoch(accessStartEpoch)

    accessStopEpoch = accessTimePeriod.access_interval.get_stop_epoch()
    accessStopEpoch.set_implicit_time(timeOfAltMax)
    accessTimePeriod.access_interval.set_stop_epoch(accessStopEpoch)

.. _ExtractAccessIntervals:

Compute and extract access interval times
=========================================

.. code-block:: python

    # Access access: Access calculation
    # Get and display the Computed Access Intervals
    intervalCollection = access.computed_access_interval_times

    # Set the intervals to use to the Computed Access Intervals
    computedIntervals = intervalCollection.to_array(0, -1)
    access.specify_access_intervals(computedIntervals)

.. _ComputeAccessPoint:

Compute an access for one point
===============================

.. code-block:: python

    # IStkObject facility: Facility object
    onePtAccess = facility.create_one_point_access("Satellite/MySatellite")

    # Configure properties (if necessary)
    onePtAccess.start_time = root.current_scenario.start_time
    onePtAccess.stop_time = root.current_scenario.stop_time
    onePtAccess.step_size = 600
    onePtAccess.summary_option = OnePointAccessSummary.DETAILED

    # Compute results
    results = onePtAccess.compute()

    # Print results
    for i in range(0, results.count):
        result = results.item(i)
        print("Time: %s HasAccess: %s" % (result.time, str(result.access_is_satisfied)))

        for j in range(0, result.constraints.count):
            constraint = result.constraints.item(j)
            print(
                "Constraint: %s Object: %s Status: %s Value:%s"
                % (constraint.constraint, constraint.object_path, constraint.status, str(constraint.value))
            )

.. _ComputeAccessAdvancedSettings:

Compute access with advanced settings
=====================================

.. code-block:: python

    # Access access: Access object

    access.advanced.enable_light_time_delay = True
    access.advanced.time_light_delay_convergence = 0.00005
    access.advanced.aberration_type = AberrationType.ANNUAL
    access.advanced.use_default_clock_host_and_signal_sense = False
    access.advanced.clock_host = IvClockHost.BASE
    access.advanced.signal_sense_of_clock_host = IvTimeSense.TRANSMIT
    access.compute_access()

.. _ComputeAccessPaths:

Compute an access between two STK objects (using object path)
=============================================================

.. code-block:: python

    # Satellite satellite: Satellite object

    # Get access by object path
    access = satellite.get_access("Facility/MyFacility")

    # Compute access
    access.compute_access()

.. _ComputeAccess:

Compute an access between two STK objects (using istkobject interface)
======================================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    # Facility facility: Facility object

    # Get access by STK Object
    access = satellite.get_access_to_object(facility)

    # Compute access
    access.compute_access()

.. _RemoveAllConstraints:

Remove all access constraints except for line of sight
======================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    for i in range(accessConstraints.count - 1, 0, -1):
        constraint = accessConstraints.Item(i).ConstraintName

        if (constraint == "LineOfSight") is False:
            if constraint == "ThirdBodyObstruction":
                thirdBodyConstraint = accessConstraints.GetActiveNamedConstraint("ThirdBodyObstruction")
                assignedArray = thirdBodyConstraint.AssignedObstructions

                for j in range(0, len(assignedArray)):
                    thirdBodyConstraint.RemoveObstruction(assignedArray[j])

            elif constraint == "ExclusionZone":
                accessConstraints.GetActiveNamedConstraint("ExclusionZone").RemoveAll()

            else:
                accessConstraints.RemoveNamedConstraint(constraint)

.. _AddExclusionZoneConstraint:

Add an exclusion zone access constraint
=======================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    excludeZone = accessConstraints.add_named_constraint("ExclusionZone")
    excludeZone.maximum_latitude = 45
    excludeZone.minimum_latitude = 15
    excludeZone.minimum_longitude = -75
    excludeZone.maximum_longitude = -35

.. _AddMultipleConstraint:

Add multiple access constraints of the same type to an STK object
=================================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # Add constraints
    # Only the eCstrApparentTime (4), eCstrDuration (13), eCstrGMT (16), eCstrIntervals (22), eCstrLocalTime (27) constraint
    # types can be added multiple times to the constraint collection.
    time1 = accessConstraints.add_constraint(AccessConstraintType.LOCAL_TIME)
    time1.minimum = "00:00:00.000"
    time1.maximum = "23:00:00.000"

.. _AddAltitudeConstraint:

Add and configure an altitude access constraint
===============================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
    # Attitude constraint
    altitude = accessConstraints.add_constraint(AccessConstraintType.ALTITUDE)
    altitude.enable_minimum = True
    altitude.minimum = 20.5  # km

.. _AddCbObstructionConstraint:

Add and configure a central body obstruction access constraint
==============================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    # Get IAgAccessCnstrCbObstruction interface
    cbObstrConstraint = accessConstraints.add_constraint(AccessConstraintType.CENTRAL_BODY_OBSTRUCTION)

    # AvailableObstructions returns a one dimensional array of obstruction paths
    availableArray = cbObstrConstraint.available_obstructions

    # In this example add all available obstructions
    print("Available obstructions")
    for i in range(0, len(availableArray)):
        print(availableArray[i])
        if availableArray[i] != "Sun":  # Sun is enabled by default
            cbObstrConstraint.add_obstruction(availableArray[i])

    # AssignedObstructions returns a one dimensional array of obstruction paths
    assignedArray = cbObstrConstraint.assigned_obstructions

    print("Assigned obstructions")
    for i in range(0, len(assignedArray)):
        print(assignedArray[i])

.. _AddSunElevationAngleConstraint:

Add and configure a sun elevation angle access constraint
=========================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
    minmax = accessConstraints.add_constraint(AccessConstraintType.SUN_ELEVATION_ANGLE)
    minmax.enable_minimum = True
    minmax.minimum = 22.2
    minmax.enable_maximum = True
    minmax.maximum = 77.7

.. _AddLunarElevationAngleConstraint:

Add and configure a lunar elevation angle access constraint
===========================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # To make this more efficient, wrap this method between calls to root.BeginUpdate() and root.EndUpdate()
    minmax = accessConstraints.add_constraint(AccessConstraintType.LUNAR_ELEVATION_ANGLE)
    minmax.enable_minimum = True
    minmax.minimum = 11.1
    minmax.enable_maximum = True
    minmax.maximum = 88.8

.. _AddSunExclusionConstraint:

Add and configure a line of sight sun exclusion access constraint
=================================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # Angle constraint
    cnstrAngle = accessConstraints.add_constraint(AccessConstraintType.LIGHT_OF_SIGHT_SOLAR_EXCLUSION_ANGLE)
    cnstrAngle.angle = 176.0

.. _AddLightingConstraint:

Add and configure a lighting condition access constraint
========================================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection

    # Condition constraint
    light = accessConstraints.add_constraint(AccessConstraintType.LIGHTING)
    light.condition = ConstraintLighting.DIRECT_SUN

.. _AvailableAccessConstraints:

Return a list of available constraints
======================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    constraintArray = accessConstraints.available_constraints()

    print("List of Available Constraints:")
    for i in range(0, len(constraintArray)):
        print(constraintArray[i])

.. _AccessConstraints:

Get handle to the object access constraints
===========================================

.. code-block:: python

    # Satellite satellite: Satellite object
    accessConstraints = satellite.access_constraints

.. _CreateCAT:

Create a new AdvCat object
==========================

.. code-block:: python

    # Scenario scenario: Scenario object
    advCAT = scenario.children.new(STKObjectType.ADVCAT, "MyAdvCAT")

.. _AircraftAttitude:

Set the attitude of the aircraft
================================

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    aircraft.attitude.basic.set_profile_type(AttitudeProfile.COORDINATED_TURN)

.. _AddAircraftArrayPoints:

Add array of waypoints to aircraft
==================================

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    route = aircraft.route
    ptsArray = [[37.5378, 14.2207, 3.0480, 0.0772, 2], [47.2602, 30.5517, 3.0480, 0.0772, 2]]
    route.set_points_smooth_rate_and_propagate(ptsArray)
    # Propagate the route
    route.propagate()

.. _AddAircraftPoints:

Set great arc propagator and add individual waypoints to aircraft
=================================================================

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    # Set route to great arc, method and altitude reference
    aircraft.set_route_type(PropagatorType.GREAT_ARC)
    route = aircraft.route
    route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
    route.set_altitude_reference_type(VehicleAltitudeReference.MEAN_SEA_LEVEL)
    # Add first point
    waypoint = route.waypoints.add()
    waypoint.latitude = 37.5378
    waypoint.longitude = 14.2207
    waypoint.altitude = 5  # km
    waypoint.speed = 0.1  # km/sec
    # Add second point
    waypoint2 = route.waypoints.add()
    waypoint2.latitude = 47.2602
    waypoint2.longitude = 30.5517
    waypoint2.altitude = 5  # km
    waypoint2.speed = 0.1  # km/sec
    # Propagate the route
    route.propagate()

.. _CreateAircraft:

Create a new aircraft (on the current scenario central body)
============================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    aircraft = root.current_scenario.children.new(STKObjectType.AIRCRAFT, "MyAircraft")

.. _ListAreaTargetPoints:

List all points in an area target
=================================

.. code-block:: python

    # AreaTarget areaTarget: AreaTarget object
    if areaTarget.area_type == AreaType.PATTERN:
        # Get IAgAreaTypePatternCollection interface from AreaTypeData
        patternPoints = areaTarget.area_type_data

        # ToArray returns a two dimensional array of latitude and longitude points
        areaTargetPoints = patternPoints.to_array()

        print("All points in Area Target")
        for i in range(0, len(areaTargetPoints)):
            print("Latitude: %s Longitude: %s" % (str(areaTargetPoints[i][0]), str(areaTargetPoints[i][1])))

.. _CreateBoundaryAreaTargetList:

Define area target boundary and position from list of lat/lon/alt (using common tasks)
======================================================================================

.. code-block:: python

    # AreaTarget areaTarget: AreaTarget object
    # Remove all points in the area target
    areaTarget.area_type_data.remove_all()

    # By using the CommonTasks interface,
    # make an array of latitude and longitude boundary points
    boundary = [[29, -12], [29, 34], [6, 34], [6, -12]]

    # SetAreaTypePattern expects a two dimensional array of latitude and longitude values
    areaTarget.common_tasks.set_area_type_pattern(boundary)

.. _CreateBoundaryAreaTarget:

Define area target boundary and position from list of lat/lon/alt
=================================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AreaTarget areaTarget: AreaTarget object

    # By using the fine grained interfaces,
    # BeginUpdate/EndUpdate prevent intermediate redraws
    root.begin_update()
    areaTarget.area_type = AreaType.PATTERN
    patterns = areaTarget.area_type_data
    patterns.add(48.897, 18.637)
    patterns.add(46.534, 13.919)
    patterns.add(44.173, 21.476)
    root.end_update()
    areaTarget.automatic_computation_of_centroid = True

.. _CreateAreaTargetCommon:

Set an elliptical area target (using common tasks)
==================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AreaTarget areaTarget: AreaTarget object

    # By using the CommonTasks interface
    areaTarget.common_tasks.set_area_type_ellipse(85.25, 80.75, 44)

.. _CreateEllipticalAreaTarget:

Set an elliptical area target
=============================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AreaTarget areaTarget: AreaTarget object

    # By using the fine grained interfaces,
    # BeginUpdate/EndUpdate prevent intermediate redraws
    root.begin_update()
    areaTarget.area_type = AreaType.ELLIPSE
    ellipse = areaTarget.area_type_data
    ellipse.semi_major_axis = 85.25  # in km (distance dimension)
    ellipse.semi_minor_axis = 80.75  # in km (distance dimension)
    ellipse.bearing = 44  # in deg (angle dimension)
    root.end_update()

.. _CreateAreaTarget:

Create an area target (on the current scenario central body)
============================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root

    # Create the AreaTarget on the current scenario central body (use
    # NewOnCentralBody to specify explicitly the central body)
    areaTarget = root.current_scenario.children.new(STKObjectType.AREA_TARGET, "MyAreaTarget")

.. _ChainStrandIntervals:

Prints the strand intervals of chain object
===========================================

.. code-block:: python

    # Chain chain: Chain Object
    # Compute the chain access if not done already.
    chain.compute_access()

    # Considered Start and Stop time
    print(
        "Chain considered start time: %s"
        % chain.analysis_workbench_components.time_instants.item("ConsideredStartTime").find_occurrence().epoch
    )
    print(
        "Chain considered stop time: %s"
        % chain.analysis_workbench_components.time_instants.item("ConsideredStopTime").find_occurrence().epoch
    )

    objectParticipationIntervals = chain.analysis_workbench_components.time_interval_collections.item(
        "StrandAccessIntervals"
    )
    intervalListResult = objectParticipationIntervals.find_interval_collection()

    for i in range(0, intervalListResult.interval_collections.count):
        if intervalListResult.IsValid:
            print("Link Name: %s" % objectParticipationIntervals.Labels(i + 1))
            print("--------------")
            for j in range(0, intervalListResult.IntervalCollections.Item(i).Count):
                startTime = intervalListResult.IntervalCollections.Item(i).Item(j).Start
                stopTime = intervalListResult.IntervalCollections.Item(i).Item(j).Stop
                print("Start: %s Stop: %s" % (startTime, stopTime))

.. _CreateChainAdvanced:

Define and compute a chain (advanced)
=====================================

.. code-block:: python

    # Chain chain: Chain object
    # Satellite satellite: Satellite object

    # Remove all previous accesses
    chain.clear_access()

    # Add some objects to chain
    chain.objects.add("Facility/MyFacility")
    chain.objects.add_object(satellite)

    # Configure chain parameters
    chain.recompute_automatically = False
    chain.enable_light_time_delay = False
    chain.time_convergence = 0.001
    chain.data_save_mode = DataSaveMode.SAVE_ACCESSES

    # Specify our own time period
    chain.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)

    # Get chain time period interface
    chainUserTimePeriod = chain.time_period
    chainUserTimePeriod.time_interval.set_explicit_interval(
        root.current_scenario.analysis_interval.find_start_time(),
        root.current_scenario.analysis_interval.find_stop_time(),
    )  # Set to scenario period

    # Compute the chain
    chain.compute_access()

.. _ComputeChain:

Define and compute a chain (basic)
==================================

.. code-block:: python

    # Chain chain: Chain object

    # Add some objects to chain (using STK path)
    chain.objects.add("Facility/MyFacility")
    chain.objects.add("Satellite/MySatellite")

    # Compute the chain
    chain.compute_access()

.. _CreateChain:

Create a chain (on the current scenario central body)
=====================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # Create the Chain on the current scenario central body (use
    # NewOnCentralBody to specify explicitly the central body)
    chain = root.current_scenario.children.new(STKObjectType.CHAIN, "MyChain")

.. _CreateConstellation:

Define a constellation
======================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # Satellite satellite: Satellite object
    constellation = root.current_scenario.children.new(STKObjectType.CONSTELLATION, "MyConstellation")
    constellation.objects.add_object(satellite)
    constellation.objects.add("*/Facility/MyFacility")

.. _CoverageCompute:

Compute coverage
================

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    coverage.compute_accesses()

.. _CoverageAdvanced:

Set advanced settings for coverage
==================================

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    advanced = coverage.advanced
    advanced.recompute_automatically = False
    advanced.data_retention = CoverageDataRetention.ALL_DATA
    advanced.save_mode = DataSaveMode.SAVE_ACCESSES

.. _SetCoverageIntervalToAvailability:

Set the coverage interval to an object's availability analysis interval
=======================================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    # CoverageDefinition coverage: Coverage object
    satVGT = satellite.analysis_workbench_components
    AvailTimeSpan = satVGT.time_intervals.item("AvailabilityTimeSpan")
    IntResult = AvailTimeSpan.find_interval()
    coverage.interval.analysis_interval.set_start_and_stop_times(IntResult.interval.start, IntResult.interval.stop)

.. _CreateCoverage:

Create a new coverage definition (on the current scenario central body)
=======================================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    # Create new Coverage Definition and set the Bounds to an area target
    coverage = scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "MyCoverage")
    coverage.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
    covGrid = coverage.grid
    bounds = covGrid.bounds
    bounds.area_targets.add("AreaTarget/MyAreaTarget")
    # Define the Grid Resolution
    Res = covGrid.resolution
    Res.latitude_longitude = 0.5  # deg
    # Set the satellite as the Asset
    coverage.asset_list.add("Satellite/MySatellite")

    # Turn off Show Grid Points
    coverage.graphics.static.show_points = False

.. _SingleTimesDataProvider:

Getting data for specific points and elements
=============================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    times = [[0], [15000], [20000], [55000]]
    elems = [["Time"], ["Precision Pass Number"]]
    satPassesDP = satellite.data_providers.item("Precision Passes").execute_single_elements_array(times, elems)
    passes = satPassesDP.get_array(1)

.. _SingleTimeDataProvider:

Getting data for a single point in time
=======================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    satPassDP = satellite.data_providers.item("Precision Passes").execute_single(2600)
    passes = satPassDP.data_sets.get_data_set_by_name("Precision Pass Number").get_values()

.. _DataProviderPreData:

Extracting elements from data providers with pre-data
=====================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Facility facility: Facility object
    # Scenario scenario: Scenario object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    facChooseDP = facility.data_providers.item("Points Choose System")
    dataProvCenter = facChooseDP.group.item("Center")
    # Choose the reference system you want to report the Center point in
    dataProvCenter.pre_data = "CentralBody/Earth TOD"
    rptElems = [["Time"], ["x"], ["y"], ["z"]]
    results = dataProvCenter.execute_elements(scenario.start_time, scenario.stop_time, 60, rptElems)
    datasets = results.data_sets
    Time = datasets.get_data_set_by_name("Time").get_values()
    facTODx = datasets.get_data_set_by_name("x").get_values()
    facTODy = datasets.get_data_set_by_name("y").get_values()
    facTODz = datasets.get_data_set_by_name("z").get_values()

.. _GroupsDataProvider:

Extracting elements from data providers with groups
===================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Scenario scenario: Scenario object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    satPosDP = (
        satellite.data_providers.item("Cartesian Position")
        .group.item("ICRF")
        .execute(scenario.start_time, scenario.stop_time, 60)
    )
    satx = satPosDP.data_sets.get_data_set_by_name("x").get_values()
    saty = satPosDP.data_sets.get_data_set_by_name("y").get_values()
    satz = satPosDP.data_sets.get_data_set_by_name("z").get_values()

    satVelDP = satellite.data_providers.get_data_provider_time_varying_from_path("Cartesian Velocity/ICRF").execute(
        scenario.start_time, scenario.stop_time, 60
    )
    # There are 4 Methods to get DP From a Path depending on the kind of DP:
    #   GetDataPrvTimeVarFromPath
    #   GetDataPrvIntervalFromPath
    #   GetDataPrvInfoFromPath
    #   GetDataPrvFixedFromPath
    satvx = satVelDP.data_sets.get_data_set_by_name("x").get_values()
    satvy = satVelDP.data_sets.get_data_set_by_name("y").get_values()
    satvz = satVelDP.data_sets.get_data_set_by_name("z").get_values()

.. _TimeDependentDataProviderElements:

Using a time dependent data provider and requesting only specified elements
===========================================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Scenario scenario: Scenario object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    elems = [["Time"], ["q1"], ["q2"], ["q3"], ["q4"]]
    satDP = satellite.data_providers.item("Attitude Quaternions").execute_elements(
        scenario.start_time, scenario.stop_time, 60, elems
    )
    # Whenever you pass an index to an array, you need to cast it to a long
    # equivalent (int32)
    satTime = satDP.data_sets.item(0).get_values()
    satq1 = satDP.data_sets.item(1).get_values()
    satq2 = satDP.data_sets.item(2).get_values()
    satq3 = satDP.data_sets.item(3).get_values()
    satq4 = satDP.data_sets.item(4).get_values()

.. _IntervalDataProvider:

Using an interval data provider
===============================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Facility facility: Facility object

    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    # Get the current scenario
    scenario = root.current_scenario
    # Set up the access object
    access = satellite.get_access_to_object(facility)
    access.compute_access()
    # Get the Access AER Data Provider
    accessDP = access.data_providers.item("Access Data").execute(scenario.start_time, scenario.stop_time)

    accessStartTimes = accessDP.data_sets.get_data_set_by_name("Start Time").get_values()
    accessStopTimes = accessDP.data_sets.get_data_set_by_name("Stop Time").get_values()

.. _FacilityAzElMaskDisplay:

Display the AzEl mask in 2D/3D
==============================

.. code-block:: python

    # Facility facility: Facility Object
    azelMask = facility.graphics.az_el_mask
    azelMask.show_mask_over_range = True
    azelMask.number_of_range_steps = 10
    azelMask.display_range_minimum = 0  # km
    azelMask.display_range_maximum = 100  # km
    azelMask.show_color_at_range = True
    azelMask.range_color = Colors.Cyan

.. _AzElMaskFacility:

Add an AzEl mask to a facility
==============================

.. code-block:: python

    # Facility facility: Facility Object
    facility.set_az_el_mask(AzElMaskType.TERRAIN_DATA, 0)

.. _GetPositionFacility:

Get the Cartesian position of the facility
==========================================

.. code-block:: python

    # Facility facility: Facility Object
    (x, y, z) = facility.position.query_cartesian()

.. _SetPositionFacility:

Set the geodetic position of the facility
=========================================

.. code-block:: python

    # Facility facility: Facility Object
    facility.position.assign_geodetic(41.9849, 21.4039, 0)  # Latitude, Longitude, Altitude

    # Set altitude to height of terrain
    facility.use_terrain = True

    # Set altitude to a distance above the ground
    facility.height_above_ground = 0.05  # km

.. _SetHeightFacility:

Create a facility and set its height above ground level
=======================================================

.. code-block:: python

    from ansys.stk.core.utilities.exceptions import STKRuntimeError
    from ansys.stk.core.stkobjects import Facility, STKObjectType

    try:
        # this facility is not a valid STK reference
        my_facility_attempt = Facility()
        my_facility_attempt.height_above_ground = 123.4
    except STKRuntimeError as e:
        print(e)

    # this facility represents a valid STK object
    facility = Facility(root.current_scenario.children.new(STKObjectType.FACILITY, "facility1"))
    facility.height_above_ground = 123.4

.. _CreateFacility:

Create a facility (on the current scenario central body)
========================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    facility = root.current_scenario.children.new(STKObjectType.FACILITY, "MyFacility")

.. _FOMContoursColorRamp:

Configure the contours of the fom and define a color ramp
=========================================================

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    # FigureOfMerit fom: Figure Of Merit object
    satisfaction = coverage.graphics.static
    satisfaction.show_region = False
    Animation = fom.graphics_3d.animation_graphics_3d_settings
    Animation.show_graphics = False
    VOcontours = fom.graphics_3d.static
    VOcontours.show_graphics = True
    contours = fom.graphics.static.contours
    contours.show_graphics = True
    contours.contour_type = FigureOfMeritGraphics2DContourType.SMOOTH_FILL
    contours.color_method = FigureOfMeritGraphics2DColorMethod.COLOR_RAMP
    contours.level_attributes.remove_all()

    contours.level_attributes.add_level_range(590, 660, 10)  # Start, Start, Step
    contours.ramp_color.start_color = Colors.Red
    contours.ramp_color.end_color = Colors.Blue

.. _CreateFOM:

Create a new figure of merit of type access duration
====================================================

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    fom = coverage.children.new(STKObjectType.FIGURE_OF_MERIT, "AccessDuration")
    fom.set_definition_type(FigureOfMeritDefinitionType.ACCESS_DURATION)
    fom.definition.set_compute_type(FigureOfMeritCompute.MAXIMUM)

.. _AddGroundVehicleArrayPoints:

Add array of waypoints to ground vehicle and interpolate over terrain
=====================================================================

.. code-block:: python

    # GroundVehicle grndVehicle: Ground Vehicle object
    route = grndVehicle.route
    ptsArray = [
        [41.97766217, 21.44863761, 0, 0.026, 0.5],
        [41.97422351, 21.39956154, 0, 0.026, 0.5],
        [41.99173299, 21.40796942, 0, 0.026, 0.5],
    ]
    route.set_points_smooth_rate_and_propagate(ptsArray)
    route.set_altitude_reference_type(VehicleAltitudeReference.TERRAIN)
    route.altitude_reference.granularity = 0.001
    route.altitude_reference.interpolation_method = VehicleWaypointInterpolationMethod.TERRAIN_HEIGHT
    # Propagate the route
    route.propagate()

.. _AddGroundVehiclePoints:

Set great arc propagator and add individual waypoints to ground vehicle
=======================================================================

.. code-block:: python

    # GroundVehicle grndVehicle: Ground Vehicle object
    # Set route to great arc, method and altitude reference
    groundVehicle.set_route_type(PropagatorType.GREAT_ARC)
    route = groundVehicle.route
    route.method = VehicleWaypointComputationMethod.DETERMINE_TIME_ACCELERATION_FROM_VELOCITY
    route.set_altitude_reference_type(VehicleAltitudeReference.WGS84)
    # Add first point
    waypoint = route.waypoints.add()
    waypoint.latitude = 56.18
    waypoint.longitude = 40.91
    waypoint.altitude = 0  # km
    waypoint.speed = 0.026  # km/sec
    # Add second point
    waypoint2 = route.waypoints.add()
    waypoint2.latitude = 50.22
    waypoint2.longitude = 11.05
    waypoint2.altitude = 0  # km
    waypoint2.speed = 0.026  # km/sec
    # Propagate the route
    route.propagate()

.. _CreateVehicle:

Create a new ground vehicle (on the current scenario central body)
==================================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    grndVehicle = scenario.children.new(STKObjectType.GROUND_VEHICLE, "MyVehicle")
    grndVehicle.set_route_type(PropagatorType.GREAT_ARC)

.. _CreateLineTarget:

Create a new line target (on the current scenario central body)
===============================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    lineTarget = scenario.children.new(STKObjectType.LINE_TARGET, "MyLineTarget")
    point1 = lineTarget.points.add(34.72, -118.34)
    point2 = lineTarget.points.add(30.83, -82.67)

.. _CreateMissile:

Create a new missile (on the current scenario central body)
===========================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    missile = scenario.children.new(STKObjectType.MISSILE, "MyMissile")
    missile.set_trajectory_type(PropagatorType.BALLISTIC)
    trajectory = missile.trajectory
    root.units_preferences.set_current_unit("DateFormat", "EpSec")
    trajectory.ephemeris_interval.set_explicit_interval(0, 0)  # stop time later computed based on propagation
    trajectory.launch.latitude = 29
    trajectory.launch.longitude = -81
    trajectory.impact_location.impact.latitude = 27
    trajectory.impact_location.impact.longitude = -43
    trajectory.impact_location.set_launch_control_type(VehicleLaunchControl.FIXED_APOGEE_ALTITUDE)
    trajectory.impact_location.launch_control.apogee_altitude = 1200  # km
    trajectory.propagate()

.. _MTOLoadTrack:

Load MTO track points from file
===============================

.. code-block:: python

    # load_points expects the path an Ephemeris file path
    # MTO mto: MTO Object
    track2 = mto.tracks.add(2)
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    track2.points.load_points(
        os.path.join(installPath, "Data", "Resources", "stktraining", "text", "EphemerisLLATimePosVel_Example.e")
    )
    track2.interpolate = True

.. _CreateMTO:

Create a new MTO (on the current scenario central body)
=======================================================

.. code-block:: python

    # Scenario scenario: Scenario object
    mto = scenario.children.new(STKObjectType.MTO, "MyMTO")

    root.units_preferences.set_current_unit("DateFormat", "EpSec")

    mtoTimes = [[0], [7200]]
    mtoLats = [[36.77], [34.80]]
    mtoLons = [[-77.25], [-78.37]]
    mtoAlts = [[5], [5]]

    track1 = mto.tracks.add_track(1, mtoTimes, mtoLats, mtoLons, mtoAlts)
    track1.interpolate = True
    # Change the color of the track
    mto.graphics.tracks.get_track_from_identifier(1).color = Colors.Red

.. _ComputeObjectCoverage:

Compute object coverage
=======================

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    objCoverage = aircraft.object_coverage
    objCoverage.assets.remove_all
    objCoverage.assets.add("Satellite/MySatellite")
    objCoverage.use_object_times = True
    objCoverage.compute()

    objCoverageFOM = objCoverage.figure_of_merit
    objCoverageFOM.set_definition_type(FigureOfMeritDefinitionType.COVERAGE_TIME)
    objCoverageFOM.definition.set_compute_type(FigureOfMeritCompute.TOTAL)

.. _ModifyPlanet2DGraphics:

Modify planet 2D properties
===========================

.. code-block:: python

    # Planet planet: Planet object
    planet2D = planet.graphics
    planet2D.color = Colors.Red
    planet2D.inherit = False
    planet2D.show_orbit = True
    planet2D.show_sub_planet_point = False
    planet2D.show_sub_planet_label = False

.. _CreatePlanet:

Create a new planet
===================

.. code-block:: python

    # Scenario scenario: Scenario object
    planet = scenario.children.new(STKObjectType.PLANET, "Mars")
    planet.common_tasks.set_position_source_central_body("Mars", EphemSourceType.JPL_DEVELOPMENTAL_EPHEMERIS)

.. _AddGraphicsVector:

Add a vector to display in 3D
=============================

.. code-block:: python

    # Satellite satellite: Satellite object
    vector = satellite.graphics_3d.vector
    angVel = vector.vector_geometry_tool_components.add(0, "Satellite/MySatellite AngVelocity")
    angVel.show_label = True

.. _GraphicsOrbitSystem:

Add fixed system orbit system in 3D display
===========================================

.. code-block:: python

    # Satellite satellite: Satellite object
    orbitsystems = satellite.graphics_3d.orbit_systems
    orbitsystems.fixed_by_window.show_graphics = True
    orbitsystems.fixed_by_window.inherit = False
    orbitsystems.fixed_by_window.color = Colors.Yellow

.. _GraphicsDetails:

Modify the detail thresholds levels
===================================

.. code-block:: python

    # Satellite satellite: Satellite object
    details = satellite.graphics_3d.model.detail_threshold
    details.enable_detail_threshold = True
    details.all = 1  # km
    details.model_label = 2  # km
    details.marker_label = 40000  # km
    details.marker = 500000  # km
    details.point = 500000  # km

.. _GraphicsModel:

Change the 3D model and marker properties
=========================================

.. code-block:: python

    # Satellite satellite: Satellite object
    model = satellite.graphics_3d.model
    model.model_data.filename = r"STKData\VO\Models\Space\dsp.glb"
    orbitmarker = model.orbit_marker
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    orbitmarker.set_marker_image_filename(os.path.join(installPath, "STKData", "VO", "Markers", "Satellite.ppm"))
    orbitmarker.marker_data.is_transparent = True
    orbitmarker.pixel_size = 18
    orbitmarker.orientation_mode = Graphics3DMarkerOrientation.FOLLOW_DIRECTION

.. _GraphicsDropline:

Display drop lines in 3D window
===============================

.. code-block:: python

    # Satellite satellite: Satellite object
    orbitDroplines = satellite.graphics_3d.drop_lines.orbit
    wgs84 = orbitDroplines.item(0)  # Droplines to WGS84 surface
    wgs84.show_graphics = True
    wgs84.line_width = LineWidth.WIDTH2
    wgs84.use_2d_color = False
    wgs84.color = Colors.Red

.. _GraphicsDataDisplay:

Add a data display to the 3D window
===================================

.. code-block:: python

    # Satellite satellite: Satellite object
    # Remove all data displays so you can easily pick one that may already be in
    # the list
    satellite.graphics_3d.data_display.remove_all()
    # Add LLA data display and change size/title
    datadisplay = satellite.graphics_3d.data_display.add("LLA Position")
    datadisplay.show_graphics = True
    datadisplay.font_size = Graphics3DFontSize.MEDIUM
    datadisplay.title_text = "My Data Display"
    datadisplay.show_name = False

.. _GraphicsLabel:

Change the display label of the vehicle
=======================================

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.graphics.use_instance_name_label = False
    satellite.graphics.label_name = "Python Satellite"

.. _GraphicsPass:

Set 2D/3D pass display properties
=================================

.. code-block:: python

    # Satellite satellite: Satellite object
    # Display one pass for ground track and orbit on 2D
    passdata = satellite.graphics.pass_data
    groundTrack = passdata.ground_track
    groundTrack.set_lead_data_type(LeadTrailData.ONE_PASS)
    groundTrack.set_trail_same_as_lead
    orbit = passdata.orbit
    orbit.set_lead_data_type(LeadTrailData.ONE_PASS)
    orbit.set_trail_same_as_lead
    # Display one orbit pass and no ground track on 3D
    passdata3D = satellite.graphics_3d.satellite_pass.track_data.pass_data
    groundTrack3D = passdata3D.ground_track
    groundTrack3D.set_lead_data_type(LeadTrailData.NONE)
    groundTrack3D.set_trail_same_as_lead
    orbit3D = passdata3D.orbit
    orbit3D.set_lead_data_type(LeadTrailData.ONE_PASS)
    orbit3D.set_trail_same_as_lead

.. _GraphicsLighting:

Set vehicle lighting properties
===============================

.. code-block:: python

    # Satellite satellite: Satellite object
    lighting = satellite.graphics.lighting
    # Settings for vehicle in sunlight
    sunlight = lighting.sunlight
    sunlight.visible = True
    sunlight.color = Colors.Yellow
    sunlight.line_width = LineWidth.WIDTH4
    # Settings for vehicle in penumbra
    penumbra = lighting.penumbra
    penumbra.visible = True
    penumbra.color = Colors.Orange
    penumbra.line_width = LineWidth.WIDTH3
    # Settings for vehicle in umbra
    umbra = lighting.umbra
    umbra.visible = True
    umbra.color = Colors.Red
    umbra.line_width = LineWidth.WIDTH2

.. _GraphicsSwath:

Set 2D swath
============

.. code-block:: python

    # Satellite satellite: Satellite object
    # Set swath in the 2D properties
    swath = satellite.graphics.swath
    swath.set_elevation_type(VehicleGraphics2DElevation.ELEVATION_GROUND_ELEVATION)
    swath.elevation.angle = 30  # deg
    satellite.graphics.swath.options = VehicleGraphics2DOptionType.OPTIONS_EDGE_LIMITS

.. _GraphicsRangeContours:

Set 2D/3D range contours
========================

.. code-block:: python

    # Satellite satellite: Satellite object
    # Set a contour level in the 2D properties
    rangeContours = satellite.graphics.range_contours
    rangeContours.show_graphics = True
    rangeLevel = rangeContours.level_attributes.add_level(2000)  # km
    rangeLevel.color = Colors.Fuchsia
    rangeLevel.line_width = LineWidth.WIDTH5
    rangeLevel.label_angle = 90
    rangeLevel.show_user_text_visible = True
    rangeLevel.user_text = "Range"
    # Turn the contours on in the 3D properties
    satellite.graphics_3d.range_contours.show_graphics = True

.. _GraphicsElevationContours:

Set 2D/3D elevation contours
============================

.. code-block:: python

    # Satellite satellite: Satellite object
    # Set the contours in the 2D properties
    contours = satellite.graphics.elevation_contours
    contours.show_graphics = True
    contours.number_of_decimal_digits = 0
    contours.elevations.add_level_range(0, 90, 10)  # Min, Max, Step
    # Turn the contours on in the 3D properties
    satellite.graphics_3d.elevation_contours.show_graphics = True

.. _CustomGraphics2D:

Set 2D display times to custom and add intervals
================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    graphics = satellite.graphics
    graphics.set_attributes_type(VehicleGraphics2DAttributeType.CUSTOM)
    graphics.attributes.default.show_graphics = False

    interval1 = graphics.attributes.intervals.add(0, 3600)
    interval1.graphics_2d_attributes.show_graphics = True
    interval1.graphics_2d_attributes.inherit = False
    interval1.graphics_2d_attributes.line.width = LineWidth.WIDTH2
    interval1.graphics_2d_attributes.line.style = LineStyle.LONG_DASH
    interval1.graphics_2d_attributes.color = Colors.Fuchsia
    interval1.graphics_2d_attributes.marker_style = "X"

    interval2 = satellite.graphics.attributes.intervals.add(7200, 86400)
    interval2.graphics_2d_attributes.show_graphics = True
    interval2.graphics_2d_attributes.inherit = False
    interval2.graphics_2d_attributes.line.width = LineWidth.WIDTH2
    interval2.graphics_2d_attributes.line.style = LineStyle.DASHED
    interval2.graphics_2d_attributes.color = Colors.Lime
    interval2.graphics_2d_attributes.marker_style = "Point"

.. _BasicGraphics2D:

Set 2D graphics display properties
==================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Change the line width, style, color and marker

    graphics = satellite.graphics
    graphics.set_attributes_type(VehicleGraphics2DAttributeType.BASIC)
    attributes = graphics.attributes
    attributes.inherit = False
    attributes.line.width = LineWidth.WIDTH4
    attributes.line.style = LineStyle.LONG_DASH
    attributes.color = Colors.Lime
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    attributes.marker_style = os.path.join(installPath, "STKData", "Pixmaps", "MarkersWin", "m010Satellite.bmp")

.. _SatelliteGraphicsResolution:

Change the graphics resolution of the orbit for a smooth path
=============================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    resolution = satellite.graphics.resolution
    resolution.orbit = 60

.. _SatelliteAttitudeExternal:

Set satellite attitude external
===============================

.. code-block:: python

    # Satellite satellite: Satellite object
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    satellite.attitude.external.load(
        os.path.join(installPath, "Data", "Resources", "stktraining", "text", "AttitudeTimeEulerAngles_Example.a")
    )

.. _SatelliteAttitudeTarget:

Set satellite attitude targeting
================================

.. code-block:: python

    # Satellite satellite: Satellite object
    attitudePointing = satellite.attitude.pointing
    attitudePointing.use_target_pointing = True
    attitudePointing.targets.remove_all()
    attitudePointing.targets.add("AreaTarget/MyAreaTarget")
    attitudePointing.target_times.use_access_times = True

.. _SatelliteAttitudeSpinning:

Set satellite attitude basic spinning
=====================================

.. code-block:: python

    # Satellite satellite: Satellite object
    basic = satellite.attitude.basic
    basic.set_profile_type(AttitudeProfile.SPINNING)
    basic.profile.body.assign_xyz(0, 0, 1)
    basic.profile.inertial.assign_xyz(0, 1, 0)
    basic.profile.rate = 6  # rev/sec

.. _ExportEphemerisFile:

Export an ephemeris file to scenario folder
===========================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # Satellite satellite: Satellite object
    scenPath = root.execute_command("GetDirectory / Scenario").item(0)
    satelliteFilePath = "%s\\%s.e" % (scenPath, satellite.instance_name)
    satelliteFilePath = satelliteFilePath.replace("\\", "\\\\")
    satellite.export_tools.get_ephemeris_stk_export_tool().export(satelliteFilePath)

.. _SGP4Satellite:

Set satellite propagator to sgp4 and propagate
==============================================

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.ephemeris_interval.set_implicit_interval(
        root.current_scenario.analysis_workbench_components.time_intervals.item("AnalysisInterval")
    )  # Link to scenario period
    propagator.common_tasks.add_segments_from_online_source("25544")  # International Space Station
    propagator.automatic_update_enabled = True
    propagator.propagate()

.. _SPICESatellite:

Set satellite propagator to spice and propagate
===============================================

.. code-block:: python

    # Satellite satellite: Satellite object
    # StkObjectRoot root: STK Object Model Root
    satellite.set_propagator_type(PropagatorType.SPICE)
    propagator = satellite.propagator
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    propagator.spice = os.path.join(
        installPath, "STKData", "Spice", "planets.bsp"
    )  # Make sure this is a valid path
    propagator.body_name = "MARS"

    propagator.ephemeris_interval.set_implicit_interval(
        root.current_scenario.analysis_workbench_components.time_intervals.item("AnalysisInterval")
    )  # Link to scenario period
    propagator.step = 60.0
    propagator.propagate()

.. _AstrogatorSatellite:

Set satellite propagator to Astrogator and clear segments
=========================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.set_propagator_type(PropagatorType.ASTROGATOR)
    driver = satellite.propagator
    # Clear all segments from the MCS
    driver.main_sequence.remove_all()

.. _HPOPSatellite:

Set satellite propagator to HPOP and set force model properties
===============================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.set_propagator_type(PropagatorType.HPOP)
    satellite.propagator.step = 60
    satellite.propagator.initial_state.representation.assign_cartesian(
        CoordinateSystem.FIXED, 6406.92, -1787.59, -506.422, 2.10185, 6.48871, 3.64041
    )

    forceModel = satellite.propagator.force_model
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    forceModel.central_body_gravity.file = os.path.join(
        installPath, "STKData", "CentralBodies", "Earth", "WGS84_EGM96.grv"
    )
    forceModel.central_body_gravity.maximum_degree = 21
    forceModel.central_body_gravity.maximum_order = 21
    forceModel.drag.use = True
    forceModel.drag.drag_model.cd = 0.01
    forceModel.drag.drag_model.area_mass_ratio = 0.01
    forceModel.solar_radiation_pressure.use = False

    integrator = satellite.propagator.integrator
    integrator.do_not_propagate_below_altitude = -1e6
    integrator.integration_model = VehicleIntegrationModel.RUNGE_KUTTA_FEHLBERG_78
    integrator.step_size_control.method = VehicleMethod.RELATIVE_ERROR
    integrator.step_size_control.error_tolerance = 1e-13
    integrator.step_size_control.minimum_step_size = 0.1
    integrator.step_size_control.maximum_step_size = 30
    integrator.interpolation.method = VehicleInterpolationMethod.LAGRANGE
    integrator.interpolation.order = 7

    satellite.propagator.propagate()

.. _J4Satellite:

Set satellite propagator to j4 and assign Cartesian position
============================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    satellite.set_propagator_type(PropagatorType.J4_PERTURBATION)
    propagator = satellite.propagator
    propagator.initial_state.representation.assign_cartesian(
        CoordinateSystem.ICRF, 6678.14, 0, 0, 0, 6.78953, 3.68641
    )
    propagator.propagate()

.. _SatelliteInitialState:

Set initial state of satellite and propagate
============================================

.. code-block:: python

    # Satellite satellite: Satellite object
    keplerian = satellite.propagator.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
    keplerian.size_shape_type = ClassicalSizeShape.ALTITUDE
    keplerian.location_type = ClassicalLocation.TRUE_ANOMALY
    keplerian.orientation.ascending_node_type = OrientationAscNode.LONGITUDE_ASCENDING_NODE

    # Assign the perigee and apogee altitude values:
    keplerian.size_shape.perigee_altitude = 500  # km
    keplerian.size_shape.apogee_altitude = 600  # km

    # Assign the other desired orbital parameters:
    keplerian.orientation.inclination = 90  # deg
    keplerian.orientation.argument_of_periapsis = 12  # deg
    keplerian.orientation.ascending_node.value = 24  # deg
    keplerian.location.value = 180  # deg

    # Apply the changes made to the satellite's state and propagate:
    satellite.propagator.initial_state.representation.assign(keplerian)
    satellite.propagator.propagate()

.. _CreateSatellite:

Create a satellite (on the current scenario central body)
=========================================================

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    satellite = root.current_scenario.children.new(STKObjectType.SATELLITE, "MySatellite")

.. _SensorPersistence:

Sensor persistence
==================

.. code-block:: python

    # Sensor sensor: Sensor object
    projection = sensor.graphics.projection
    projection.persistence = 7200  # sec
    projection.forward_persistence = True
    projection.fill_persistence = True
    sensor.graphics.show_fill = True
    sensor.graphics.percent_translucency = 50

.. _SensorBodyMask:

Sensor body mask
================

.. code-block:: python

    # Sensor sensor: Sensor object
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    sensor.set_az_el_mask_file(
        os.path.join(installPath, "Data", "Resources", "stktraining", "text", "BodyMask_hga.bmsk")
    )

.. _DefineSensorPointingFixedAxesYPR:

Define sensor pointing fixed axes YPR
=====================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_ypr("CentralBody/Sun J2000 Axes", YPRAnglesSequence.RYP, 11, 22, 33)

.. _DefineSensorPointingFixedYPR:

Define sensor pointing fixed YPR
================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_ypr(YPRAnglesSequence.RPY, 12, 24, 36)

.. _DefineSensorPointingFixedAxesQuaternion:

Define sensor pointing fixed axes quaternion
============================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_quaternion("CentralBody/Sun J2000 Axes", 0.1, 0.2, 0.3, 0.4)

.. _DefineSensorPointingFixedQuaternion:

Define sensor pointing fixed quaternion
=======================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_quaternion(0.1, 0.2, 0.3, 0.4)

.. _DefineSensorPointingFixedAxesEuler:

Define sensor pointing fixed axes Euler
=======================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_euler(
        "CentralBody/Sun J2000 Axes", EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50
    )

.. _DefineSensorPointingFixedEuler:

Define sensor pointing fixed Euler
==================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_euler(EulerOrientationSequenceType.SEQUENCE_132, 30, 40, 50)

.. _DefineSensorPointingFixedAxesAzEl:

Define sensor pointing fixed axes AzEl
======================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_axes_az_el("CentralBody/Sun J2000 Axes", 11, 22, AzElAboutBoresight.HOLD)

.. _DefineSensorPointingFixedAzEl:

Define sensor pointing fixed AzEl
=================================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_az_el(4.5, -45.0, AzElAboutBoresight.ROTATE)

.. _SensorProperties:

Set sensor properties
=====================

.. code-block:: python

    # Sensor sensor: Sensor object
    # Change pattern and set
    sensor.common_tasks.set_pattern_rectangular(20, 25)
    # Change pointing and set
    sensor.common_tasks.set_pointing_fixed_az_el(90, 60, AzElAboutBoresight.ROTATE)
    # Change location and set
    sensor.set_location_type(SensorLocation.FIXED)
    sensor.location_data.assign_cartesian(-0.0004, -0.0004, 0.004)

.. _CreateSensor:

Attach a sensor object to a vehicle
===================================

.. code-block:: python

    # Satellite satellite: Satellite object
    sensor = satellite.children.new(STKObjectType.SENSOR, "MySensor")

.. _ModifyAntennaGraphics:

Modify antenna graphics
=======================

.. code-block:: python

    # Antenna antenna: Antenna object
    contours = antenna.graphics.contour_graphics
    contours.set_contour_type(AntennaContourType.GAIN)
    contours.show = True
    for i in range(-30, 30, 5):
        contours.contour.levels.add(i)
    antenna.graphics_3d.show_contours = True
    antenna.graphics_3d.volume_graphics.show = True

.. _ModifyAntennaOrientation:

Modify antenna orientation and position
=======================================

.. code-block:: python

    # Antenna antenna: Antenna object
    antOrientation = antenna.orientation
    antOrientation.assign_az_el(0, -90, AzElAboutBoresight.ROTATE)
    antOrientation.position_offset.x = 0.0  # m
    antOrientation.position_offset.y = 1  # m
    antOrientation.position_offset.z = 0.25  # m

.. _ModifyAntennaRefraction:

Modify antenna refraction
=========================

.. code-block:: python

    # Antenna antenna: Antenna object
    antenna.use_refraction_in_access = True
    antenna.refraction = SensorRefractionType.ITU_R_P834_4
    refraction = antenna.refraction_model
    refraction.ceiling = 5000  # m
    refraction.atmosphere_altitude = 10000  # m
    refraction.knee_bend_factor = 0.2

.. _ModifyAntenna:

Modify antenna model type
=========================

.. code-block:: python

    # Antenna antenna: Antenna object
    antenna.set_model("Dipole")
    antennaModel = antenna.model
    antennaModel.design_frequency = 15  # GHz
    antennaModel.length = 1.5  # m
    antennaModel.length_to_wavelength_ratio = 45
    antennaModel.efficiency = 85  # Percent

.. _CreateAntenna:

Create a new antenna object
===========================

.. code-block:: python

    # IStkObject satellite: STK object
    antenna = satellite.children.new(STKObjectType.ANTENNA, "MyAntenna")

.. _ReceiverAdditionalGain:

Receiver additional gain
========================

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    gain = recModel.pre_receive_gains_losses.add(5)  # dB
    gain.identifier = "Example Gain"

.. _ModifyReceiverFilter:

Modify receiver filter properties
=================================

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    recModel.enable_filter = True
    recModel.set_filter("Bessel")
    recFilter = recModel.filter
    recFilter.lower_bandwidth_limit = -20
    recFilter.upper_bandwidth_limit = 20
    recFilter.cut_off_frequency = 10

.. _ModifyReceiverDemodulator:

Modify receiver demodulator properties
======================================

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    recModel.select_demodulator_automatically = False
    recModel.set_demodulator("16PSK")

.. _ModifyReceiverSysNoiseTemp:

Modify receiver system noise temperature
========================================

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    recModel.system_noise_temperature.constant_noise_temperature = 280  # K

.. _ModifyReceiverOrientation:

Modify orientation of the receiver antenna
==========================================

.. code-block:: python

    # Complex receivers Only
    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    antennaControl = recModel.antenna_control
    antOrientation = antennaControl.embedded_model_orientation
    antOrientation.assign_az_el(45, 85, AzElAboutBoresight.ROTATE)
    antOrientation.position_offset.x = 0.5  # m
    antOrientation.position_offset.y = 0.75  # m
    antOrientation.position_offset.z = 1  # m

.. _ModifyReceiverPolarization:

Modify receiver polarization properties
=======================================

.. code-block:: python

    # Receiver receiver: Receiver object
    recModel = receiver.model
    recModel.enable_polarization = True
    recModel.set_polarization_type(PolarizationType.LINEAR)
    polarization = recModel.polarization
    polarization.reference_axis = PolarizationReferenceAxis.Z
    polarization.cross_polarization_leakage = -60  # dB

.. _ModifyReceiverAntenna:

Modify receiver embedded antenna
================================

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    antennaControl = recModel.antenna_control
    antennaControl.set_embedded_model("Hemispherical")
    antennaControl.embedded_model.efficiency = 85  # Percent

.. _ModifyReceiverModel:

Modify receiver model type
==========================

.. code-block:: python

    # Receiver receiver: Receiver object
    receiver.set_model("Complex Receiver Model")
    recModel = receiver.model
    recModel.track_frequency_automatically = False
    recModel.frequency = 11.81

.. _CreateReceiver:

Create a new receiver object
============================

.. code-block:: python

    # IStkObject satellite: STK object
    receiver = satellite.children.new(STKObjectType.RECEIVER, "MyReceiver")

.. _TransmitteradditionalGain:

Transmitter additional gain
===========================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    txModel = transmitter.model
    gain = txModel.post_transmit_gains_losses.add(-5)  # dB
    gain.identifier = "Example Loss"

.. _ModifyTransmitterFilter:

Modify transmitter filter
=========================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    txModel = transmitter.model
    txModel.enable_filter = True
    txModel.set_filter("Butterworth")
    recFilter = txModel.filter
    recFilter.lower_bandwidth_limit = -20
    recFilter.upper_bandwidth_limit = 20
    recFilter.cut_off_frequency = 10

.. _ModifyTransmitterModulator:

Modify transmitter modulator properties
=======================================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    txModel = transmitter.model
    txModel.set_modulator("BPSK")
    txModel.modulator.scale_bandwidth_automatically = True

.. _ModifyTransmitterPolarizationOrientationAndPosition:

Modify transmitter orientation and position
===========================================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    antennaControl = txModel.antenna_control
    antOrientation = antennaControl.embedded_model_orientation
    antOrientation.assign_az_el(0, 90, 1)  # 1 represents Rotate About Boresight
    antOrientation.position_offset.x = 0.0  # m
    antOrientation.position_offset.y = 1  # m
    antOrientation.position_offset.z = 0.25  # m

.. _ModifyTransmitterPolarizationProperties:

Modify transmitter polarization properties
==========================================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    txModel.enable_polarization = True
    txModel.set_polarization_type(PolarizationType.LINEAR)
    polarization = txModel.polarization
    polarization.reference_axis = PolarizationReferenceAxis.Y
    polarization.tilt_angle = 15  # deg

.. _ModifyTransmitterAntenna:

Modify transmitter embedded antenna
===================================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    antennaControl = txModel.antenna_control
    antennaControl.set_embedded_model("Isotropic")
    antennaControl.embedded_model.efficiency = 85  # Percent

.. _ModifyTransmitter:

Modify transmitter model type
=============================

.. code-block:: python

    # Transmitter transmitter: Transmitter object
    transmitter.set_model("Complex Transmitter Model")
    txModel = transmitter.model
    txModel.frequency = 14  # GHz
    txModel.power = 25  # dBW
    txModel.data_rate = 15  # Mb/sec

.. _CreateTransmitter:

Create a new transmitter object
===============================

.. code-block:: python

    # IStkObject satellite: STK object
    transmitter = satellite.children.new(STKObjectType.TRANSMITTER, "MyTransmitter")

.. _AstrogatorRunMCS:

Run the Astrogator MCS
======================

.. code-block:: python

    # MCSDriver driver: MCS driver interface
    driver.run_mcs()

.. _SetupAdvancedFixedWingTool:

Configure the advanced fixed wing tool and set the aircraft to use the resulting performance models
===================================================================================================

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the advanced fixed wing tool
    advFixedWingTool = aviatorAircraft.advanced_fixed_wing_tool
    # Set the basic geometry
    advFixedWingTool.wing_area = 300
    advFixedWingTool.flaps_area = 50
    advFixedWingTool.speedbrakes_area = 10
    # Set the structural and human factor limits
    advFixedWingTool.max_altitude = 65000
    advFixedWingTool.max_mach = 0.98
    advFixedWingTool.max_eas = 460
    advFixedWingTool.min_load_factor = -2.5
    advFixedWingTool.max_load_factor = 4.5

    # Opt to enforce the max temperature limit
    advFixedWingTool.use_max_temperature_limit = True
    advFixedWingTool.max_temperature = 900

    # Use a subsonic aerodynamic strategy
    advFixedWingTool.aerodynamic_strategy = AdvancedFixedWingAerodynamicStrategy.SUBSONIC_AERODYNAMIC
    # Cache the aerodynamic data to improve calculation speed
    advFixedWingTool.cache_aerodynamic_data = True
    # Use a high bypass turbofan
    advFixedWingTool.powerplant_strategy = AdvancedFixedWingPowerplantStrategy.TURBOFAN_HIGH_BYPASS
    # Cache the fuel flow data to improve calculation speed
    advFixedWingTool.cache_fuel_flow = True

    # Create the corresponding performance models that reference the advanced fixed wing tool
    # Specify the name, whether to override any existing models with the same name, and whether to set the new models as the default performance models
    advFixedWingTool.create_all_performance_models("AdvancedModels", True, True)

    # Save the changes in the catalog
    aviatorAircraft.save()

.. _SetTheConfiguration:

Set the configuration used for the mission
==========================================

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the configuration used for the mission
    configuration = mission.configuration
    # Set the max landing weight
    configuration.max_landing_weight = 300000
    # Set the empty weight
    configuration.empty_weight = 210000
    # Update the center of gravity of the aircraft when empty
    configuration.set_empty_cg(2, 0, 1)

    # Get the stations
    stations = configuration.get_stations()
    # Check if there is an internal fuel station
    if stations.contains_station("Internal Fuel") is True:
        # Get the fuel tank
        fuelTank = stations.get_internal_fuel_tank_by_name("Internal Fuel")
        # Set the capacity of the fuel tank
        fuelTank.capacity = 175000
        # Set the initial state of the fuel tank
        fuelTank.initial_fuel_state = 125000

    # Add a new payload station
    newPayload = stations.add_payload_station()
    # Set the position of the payload station
    newPayload.set_position(0, 2, 0)
    # Add an external fuel tank
    externalTank = newPayload.add_external_fuel_tank()
    # Set the empty weight of the tank
    externalTank.empty_weight = 2000

.. _SetAviatorVehicle:

Set the aircraft used for the mission to an aircraft found in the aviator catalog
=================================================================================

.. code-block:: python

    # AviatorPropagator propagator: Aviator Propagator object
    # Get the Aviator catalog
    catalog = propagator.aviator_catalog
    # Get the aircraft category
    category = catalog.aircraft_category
    # Get the user aircraft models
    aircraftModels = category.aircraft_models
    # Get the basic fighter
    fighter = aircraftModels.get_aircraft("Basic Fighter")
    # Get the mission
    mission = propagator.aviator_mission
    # Set the vehicle used for the mission
    mission.vehicle = fighter

.. _CreatePerformanceModel:

Create a new performance model for an aircraft
==============================================

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the acceleration type
    acceleration = aviatorAircraft.acceleration
    # Get the names of the current acceleration models
    modelNames = acceleration.child_names
    # Check how many models there are
    modelCount = len(modelNames)
    # Get the child types (for example AGI Basic Acceleration Model, Advanced Acceleration Model)
    modelTypes = acceleration.child_types
    # Create a new performance model of type "Advanced Acceleration Model"
    newPerformanceModel = acceleration.add_child_of_type("Advanced Acceleration Model", "Model Name")
    # Save the changes to the catalog
    aviatorAircraft.save()

.. _ConfigureWeatherAtmosphere:

Configure the weather and atmosphere of the mission
===================================================

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the wind model used for the mission
    windModel = mission.wind_model
    # Let's use the mission model
    windModel.wind_model_source = WindAtmosModelSource.MISSION_MODEL
    # Let's use constant wind
    windModel.wind_model_type = WindModelType.CONSTANT_WIND
    # Get the constant wind model options
    constantWind = windModel.mode_as_constant
    # Set the wind bearing
    constantWind.wind_bearing = 30
    # Set the wind speed
    constantWind.wind_speed = 5

    # Get the atmosphere model used for the mission
    atmosphere = mission.atmosphere_model
    # Let's use the mission model
    atmosphere.atmosphere_model_source = WindAtmosModelSource.MISSION_MODEL
    # Get the basic atmosphere options
    basicAtmosphere = atmosphere.mode_as_basic
    # Use standard 1976 atmosphere
    basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976
    # Opt to override the values
    basicAtmosphere.use_non_standard_atmosphere = True
    # Override the temperature
    basicAtmosphere.temperature = 290

.. _ConfigureRunwaySite:

Configure a runway site
=======================

.. code-block:: python

    # SiteRunway runway: Runway object
    # Set the latitude, longitude, and altitude
    runway.latitude = 41
    runway.longitude = 77
    runway.altitude = 5

    # Set the altitude reference
    runway.altitude_reference = AGLMSL.ALTITUDE_MSL

    # Set the heading
    runway.high_end_heading = 195
    # Opt to use true heading
    runway.is_magnetic = False

    # Set the length of the runway
    runway.length = 5

    # Rename the runway
    runway.name = "New User Runway"
    # Add the runway to the catalog to use it for next time
    runway.add_to_catalog(1)

.. _ConfigureRunwayFromCatalog:

Configure a runway site from a runway in the aviator catalog
============================================================

.. code-block:: python

    # SiteRunway runway: Runway object
    # Catalog catalog: Aviator catalog object
    # Get the source of user runways
    userRunways = catalog.runway_category.user_runways
    # Check that the runway exists in the catalog
    if userRunways.contains("New User Runway") is True:
        # If so, get the user runway with the given name
        runwayFromCatalog = userRunways.get_user_runway("New User Runway")
        # Copy the parameters of that runway
        runway.copy_from_catalog(runwayFromCatalog)

.. _ConfigureProcedureWindAtmos:

Configure the wind and atmosphere for a procedure
=================================================

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Get the wind model for the procedure
    windModel = procedure.wind_model
    # Use the procedure model
    windModel.wind_model_source = WindAtmosModelSource.PROCEDURE_MODEL
    # Let's use constant wind
    windModel.wind_model_type = WindModelType.CONSTANT_WIND
    # Get the constant wind model options
    constantWind = windModel.mode_as_constant
    # Set the wind bearing
    constantWind.wind_bearing = 30
    # Set the wind speed
    constantWind.wind_speed = 5

    # Get the atmosphere model used for the procedure
    atmosphere = procedure.atmosphere_model
    # Let's use the procedure model
    atmosphere.atmosphere_model_source = WindAtmosModelSource.PROCEDURE_MODEL
    # Get the basic atmosphere options
    basicAtmosphere = atmosphere.mode_as_basic
    # Use standard 1976 atmosphere
    basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976

.. _ConfigureProcedureTimeOptions:

Configure a procedure time options
==================================

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Get the time in epoch seconds
    root.units_preferences.set_current_unit("DateFormat", "EpSec")
    # Get the time options
    timeOptions = procedure.time_options
    # Get the start time
    startTime = timeOptions.start_time
    # Set the procedure to interrupt after 15 seconds
    timeOptions.set_interrupt_time(15)

.. _ConfigureProcedure:

Rename a procedure and its site
===============================

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Rename the procedure
    procedure.name = "New Procedure"
    # Get the site corresponding to the procedure
    site = procedure.site
    # Rename the site
    site.name = "New Site"

.. _ConfigurePhasePerformanceModels:

Configure the performance models to be used in the phase
========================================================

.. code-block:: python

    # Phase phase: Phase object
    # Get the acceleration performance model used for the current phase
    acceleration = phase.get_performance_model_by_type("Acceleration")
    # Check if it is linked to the catalog
    isLinkedToCatalog = acceleration.is_linked_to_catalog
    # Use the performance model in the catalog named "Built-In Model"
    acceleration.link_to_catalog("Built-In Model")

    # Get the VTOL performance model
    vtol = phase.get_performance_model_by_type("VTOL")
    # Create a new vtol model of type AGI VTOL Model. Note that this new model does not exist in the catalog and only exists in the phase.
    vtol.create_new("AGI VTOL Model")
    # Rename the performance model
    vtol.rename("Temporary VTOL Model")

.. _ConfigureBasicCruisePerfModel:

Configure the basic cruise performance model of an aircraft
===========================================================

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the cruise type
    cruise = aviatorAircraft.cruise
    # Get the build in performance model
    basicCruiseModel = cruise.get_built_in_model()

    # Set the ceiling altitude
    basicCruiseModel.ceiling_altitude = 50000
    # Set the default cruise altitude
    basicCruiseModel.default_cruise_altitude = 10000
    # Set the airspeed type
    basicCruiseModel.airspeed_type = AirspeedType.TAS
    # Opt to not use the fuel flow calculated by the aero/prop model and instead specify the values
    basicCruiseModel.use_aerodynamic_propulsion_fuel = False

    # Set the various airspeeds and fuel flows
    basicCruiseModel.min_airspeed = 110
    basicCruiseModel.min_airspeed_fuel_flow = 10000

    basicCruiseModel.max_endurance_airspeed = 135
    basicCruiseModel.max_endurance_fuel_flow = 8000

    basicCruiseModel.max_airspeed = 570
    basicCruiseModel.max_airspeed_fuel_flow = 30000

    basicCruiseModel.max_range_airspeed = 140
    basicCruiseModel.max_range_fuel_flow = 9000

    basicCruiseModel.max_performance_airspeed = 150
    basicCruiseModel.max_performance_airspeed_fuel_flow = 12000

    # Save the changes to the catalog
    aviatorAircraft.save()

.. _ConfigureBasicAccelerationPerfModel:

Configure the basic acceleration performance model of an aircraft
=================================================================

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the acceleration type
    acceleration = aviatorAircraft.acceleration
    # Get the build in performance model
    basicAccModel = acceleration.get_built_in_model()

    # Get the level turns options
    levelTurns = basicAccModel.level_turns
    # Set a max bank angle of 25
    levelTurns.set_level_turn(TurnMode.TURN_MODE_BANK_ANGLE, 25)
    # Get the climb and descent transition options
    climbAndDescent = basicAccModel.climb_and_descent_transitions
    # Set the max pull up G to 1
    climbAndDescent.max_pull_up_g = 1.2
    # Get the attitude transition options
    attitudeTransitions = basicAccModel.attitude_transitions
    # Set the max roll rate to 25
    attitudeTransitions.roll_rate = 25

    # Get the aerodynamics
    aero = basicAccModel.aerodynamics
    # Use simple aerodynamics
    aero.aerodynamic_strategy = AircraftAerodynamicStrategy.AIRCRAFT_AERODYNAMIC_SIMPLE
    # Get the options for the simple aerodynamics and set some parameters
    simpleAero = aero.mode_as_simple
    simpleAero.s_reference = 5
    simpleAero.cl_max = 3.1
    simpleAero.cd = 0.05

    # Get the propulsion
    prop = basicAccModel.propulsion
    # Use simple propulsion
    prop.propulsion_strategy = AircraftPropulsionStrategy.AIRCRAFT_PROPULSION_SIMPLE
    # Get the simple propulsion options and set some parameters
    simpleProp = prop.mode_as_simple
    simpleProp.max_thrust_acceleration = 0.6
    simpleProp.min_thrust_deceleration = 0.4
    simpleProp.set_density_scaling(True, 0.02)

    # Save the changes to the catalog
    aviatorAircraft.save()

.. _ConfigureAviatorPropagator:

Configure the aviator propagator
================================

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    # Set to Propagator to Aviator
    aircraft.set_route_type(PropagatorType.AVIATOR)
    # Get the aircraft's route
    aircraftRoute = aircraft.route
    # Get the Aviator propagator
    propagator = aircraftRoute.aviator_propagator
    # Get the Aviator mission
    mission = propagator.aviator_mission
    # Get the list of phases from the mission
    phases = mission.phases
    # Get the list of procedures from the first phase
    procedures = phases[0].procedures
    # Propagate the route
    propagator.propagate()

.. _AddTakeoffProcedure:

Add a takeoff procedure from a runway
=====================================

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a takeoff procedure with a runway as a site
    takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)

    # Get the runway heading options
    headingOptions = takeoff.runway_heading_options
    # Opt to use the headwind runway
    headingOptions.runway_mode = RunwayHighLowEnd.HEADWIND

    # Set the takeoff mode and get that interface
    takeoff.takeoff_mode = TakeoffMode.TAKEOFF_NORMAL
    takeoffNormal = takeoff.mode_as_normal

    # Set the takeoff climb angle
    takeoffNormal.takeoff_climb_angle = 5
    # Set the departure altitude above the runway
    takeoffNormal.departure_altitude = 600
    # Set the altitude offset for the runway
    takeoffNormal.runway_altitude_offset = 10
    # Use terrain for the runway's altitude
    takeoffNormal.use_runway_terrain = True

.. _AddPhase:

Add a new phase and use the same performance models as the first phase
======================================================================

.. code-block:: python

    # PhaseCollection phases: Phase Collection object
    # Add a new phase at the end of the mission
    newPhase = phases.add()
    # Rename the phase
    newPhase.name = "New Phase"
    # Copy the performance models from the first phase and paste it to the new phase
    phases[0].copy_performance_models()
    newPhase.paste_performance_models()

.. _AddLandingProcedure:

Add and configure a landing procedure
=====================================

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a landing procedure
    landing = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_LANDING)

    # Get the runway heading options
    headingOptions = landing.runway_heading_options
    # Land from the low end
    headingOptions.runway_mode = RunwayHighLowEnd.LOW_END

    # Use a standard instrument approach
    landing.approach_mode = ApproachMode.STANDARD_INSTRUMENT_APPROACH
    # Get the options for a standard instrument approach
    sia = landing.mode_as_standard_instrument_approach
    # Change the approach altitude
    sia.approach_altitude = 1000
    # Change the glideslope
    sia.glideslope = 4
    # Offset the runway altitude
    sia.runway_altitude_offset = 10
    # Use the terrain as an altitude reference for the runway
    sia.use_runway_terrain = True

.. _AddEnrouteProcedure:

Add and configure an en-route procedure
=======================================

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add an enroute procedure with a site type of End of Previous Procedure
    enroute = procedures.add_at_index(1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)
    # Get the altitude options
    altitudeOptions = enroute.altitude_msl_options
    # To specify an altitude, turn off the option to use the default cruise altitude
    altitudeOptions.use_default_cruise_altitude = False
    # Set the altitude
    altitudeOptions.msl_altitude = 10000

    # Get the navigation options
    navigationOptions = enroute.navigation_options
    # Set the route to arrive on a specified course
    navigationOptions.navigation_mode = PointToPointMode.ARRIVE_ON_COURSE
    # Set the course
    navigationOptions.arrive_on_course = 30
    # Use a magnetic heading
    navigationOptions.use_magnetic_heading = True

    # Get the navigation options
    airspeedOptions = enroute.enroute_cruise_airspeed_options
    # Fly at max speed
    airspeedOptions.cruise_speed_type = CruiseSpeed.MAX_AIRSPEED
    # To specify an airspeed to fly at, set the speed type to other airspeed
    airspeedOptions.cruise_speed_type = CruiseSpeed.OTHER_AIRSPEED
    # Then set the airspeed and airspeed type
    airspeedOptions.set_other_airspeed(AirspeedType.TAS, 200)

.. _AddBasicManeuverProcedure:

Add and configure a basic maneuver procedure
============================================

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # Add a basic maneuver procedure
    basicManeuver = procedures.add(SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_BASIC_MANEUVER)

    # Set the navigation to use a Straight Ahead strategy
    basicManeuver.navigation_strategy_type = "Straight Ahead"
    # Get the options for the straight ahead strategy
    straightAhead = basicManeuver.navigation
    # Opt to maintain course (as opposed to maintain heading)
    straightAhead.reference_frame = StraightAheadReferenceFrame.MAINTAIN_COURSE

    # Set the profile to use a Autopilot - Vertical Plane strategy
    basicManeuver.profile_strategy_type = "Autopilot - Vertical Plane"
    # Get the options for the profile strategy
    autopilot = basicManeuver.profile
    # Opt to maintain the initial altitude
    autopilot.altitude_mode = AutopilotAltitudeMode.AUTOPILOT_HOLD_INIT_ALTITUDE
    airspeedOptions = autopilot.airspeed_options
    # Opt to maintain a specified airspeed
    airspeedOptions.airspeed_mode = BasicManeuverAirspeedMode.MAINTAIN_SPECIFIED_AIRSPEED
    # Specify the airspeed
    airspeedOptions.specified_airspeed = 250

    # Configure the options on the Attitude / Performance / Fuel page
    basicManeuver.flight_mode = PhaseOfFlight.FLIGHT_PHASE_CRUISE
    # Override the fuel flow
    basicManeuver.fuel_flow_type = BasicManeuverFuelFlowType.BASIC_MANEUVER_FUEL_FLOW_OVERRIDE
    basicManeuver.override_fuel_flow_value = 1000

    # Set the basic stopping conditions
    basicManeuver.use_max_downrange = True
    basicManeuver.max_downrange = 10
    basicManeuver.use_stop_fuel_state = False
    basicManeuver.use_max_time_of_flight = False

.. _AddAndRemoveProcedures:

Add and remove procedures
=========================

.. code-block:: python

    # IProcedureCollection procedures: Procedure Collection object
    # AviatorPropagator propagator: Aviator Propagator object
    # Add a takeoff procedure with a runway as a site. This will add the procedure
    takeoff = procedures.add(SiteType.SITE_RUNWAY, ProcedureType.PROCEDURE_TAKEOFF)
    # Add a procedure at a given index (starting from 0)
    enroute = procedures.add_at_index(1, SiteType.SITE_END_OF_PREV_PROCEDURE, ProcedureType.PROCEDURE_ENROUTE)

    # Make sure to propagate the mission to calculate the route
    propagator.propagate()
    # Get the mission
    mission = propagator.aviator_mission
    # Check to see if the mission is valid (must first be propagated)
    isValid = mission.is_valid

    # Get the number of procedures
    procedureCount = procedures.count
    # Remove the procedure at the given index
    procedures.remove_at_index(1)
    # Remove the given procedure
    procedures.remove(takeoff)

    # Propagate the mission
    propagator.propagate()
