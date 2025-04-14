AnalysisWorkbenchComponentProvider
==================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider

   Allow accessing existing Vector Geometry Tool components.

.. py:currentmodule:: AnalysisWorkbenchComponentProvider

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.supports`
              - Test whether the specified VGT feature is supported.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.import_components`
              - Import Analysis Workbench components from a file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.vectors`
              - Return a group of vectors.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.points`
              - Return a group of points.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.angles`
              - Return a group of angles.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.axes`
              - Return a group of axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.planes`
              - Return a group of planes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.systems`
              - Return a group of systems.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_systems`
              - Return well-known systems.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_axes`
              - Return well-known axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_instants`
              - Return a group of events.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_intervals`
              - Return a group of event intervals.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.calculation_scalars`
              - Return a group of calc scalars.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_arrays`
              - Return a group of event arrays.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_lists`
              - Return a group of event interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_collections`
              - Return a group of event interval collections.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.parameter_sets`
              - Access, add new or remove existing parameter set components.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.conditions`
              - Return a group of condition objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.condition_sets`
              - Return a group of condition set objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volume_grids`
              - Return a group of volume grid objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volumes`
              - Return a group of volume objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.spatial_calculations`
              - Return a group of volume calc objects.



Examples
--------

Create a new Collection of Interval List

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryPoint centerPtSat: point component
    timeCollListFactory = vgtSat.time_interval_collections.factory
    timeColl = timeCollListFactory.create_lighting("LightingList", "Collection of lighting intervals")
    timeColl.use_object_eclipsing_bodies = True
    timeColl.location = centerPtSat


Create a new Time Interval

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Change DateFormat dimension to epoch seconds to make the time easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    timeIntFactory = vgtSat.time_intervals.factory
    timeInterval = timeIntFactory.create_fixed("TimeInterval", "Fixed time interval")
    timeInterval.set_interval(60, 120)


Create a new Time Instant

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Change DateFormat dimension to epoch seconds to make the time easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    timeInstFactory = vgtSat.time_instants.factory
    timeEpoch = timeInstFactory.create_epoch("FixedTime", "Fixed Epoch Time")
    timeEpoch.epoch = 3600


Get Times From a Defined Time Instant and create an cell array

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


Create a new Orbit Parameter Set

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    paraFactory = vgtSat.parameter_sets.factory
    paraSetOribit = paraFactory.create("orbitSun", "Orbit", ParameterSetType.ORBIT)
    paraSetOribit.orbiting_point = vgtSat.points.item("Center")
    paraSetOribit.central_body = "Sun"
    paraSetOribit.use_central_body_gravitational_parameter = False
    paraSetOribit.gravitational_parameter = 398600  # km^3/sec^2


Create a new Attitude Parameter Set

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryToolAxes bodyAxes: axes component
    # IVectorGeometryToolAxes icrfAxes: axes component
    paraFactory = vgtSat.parameter_sets.factory
    paraSet = paraFactory.create("attitudeICRF", "Attitude Set", ParameterSetType.ATTITUDE)
    paraSet.axes = bodyAxes
    paraSet.reference_axes = icrfAxes


Get a Scalar component and evaluate at a specific time

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # Scenario scenario: Scenario object
    deticLatitude = vgtSat.calculation_scalars.item("GroundTrajectory.Detic.LLA.Latitude")
    result = deticLatitude.evaluate(scenario.start_time)
    print("The value of detic latitude is %s" % result.value)


Create a Data Element Scalar

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    calcFactory = vgtSat.calculation_scalars.factory
    trueAnom = calcFactory.create("TrueAnomaly", "", CalculationScalarType.DATA_ELEMENT)
    trueAnom.set_with_group("Classical Elements", "ICRF", "True Anomaly")


Create a new Vector Magnitude Scalar

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    calcFactory = vgtSat.calculation_scalars.factory
    displScalar = calcFactory.create_vector_magnitude(
        "VectorDisplacement", "Vector Magnitude of Displacement Vector"
    )
    displScalar.input_vector = Sat2EarthCenter


Create a new Assembled System

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryPointFixedInSystem fixedPt: point component
    # IVectorGeometryToolAxes bodyAxes: axes component
    SysFactory = vgtSat.systems.factory
    assemSys = SysFactory.create("FixedPtSystem", "System with origin at the new point", SystemType.ASSEMBLED)
    assemSys.origin_point.set_point(fixedPt)
    assemSys.reference_axes.set_axes(bodyAxes)


Create new Aligned and Constrained Axes

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


Create a new Between Vectors Angle

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    # VectorGeometryToolVectorFixedInAxes bodyYSat: vector component
    AngFactory = vgtSat.angles.factory
    betwVect = AngFactory.create("SatEarth2Y", "Displacement Vector to Sat Body Y", AngleType.BETWEEN_VECTORS)
    betwVect.from_vector.set_vector(Sat2EarthCenter)
    betwVect.to_vector.set_vector(bodyYSat)


Create a new Fixed at Time Instant Point

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolSystemAssembled icrf: system component
    PtFactory = vgtSat.points.factory
    timeInstantPt = PtFactory.create("AtTimePt", "Point at time instant", PointType.AT_TIME_INSTANT)
    timeInstantPt.source_point = vgtSat.points.item("Center")
    timeInstantPt.reference_system = icrf
    timeInstantPt.reference_time_instant = vgtSat.time_instants.item("AvailabilityStartTime")


Create a new Model Attachment Point

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    PtFactory = vgtSat.points.factory
    modelPt = PtFactory.create("ModelPt", "Attach point defined in model", PointType.MODEL_ATTACHMENT)
    modelPt.pointable_element_name = "MainSensor-000000"


Create a new Fixed in System Point

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    PtFactory = vgtSat.points.factory
    fixedPt = PtFactory.create("FixedPt", "Point offset from Center", PointType.FIXED_IN_SYSTEM)
    fixedPt.fixed_point.assign_cartesian(0.005, 0, 0.005)


Create a new Projection Vector

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    VectFactory = vgtSat.vectors.factory
    projectionVector = VectFactory.create("Projection", "", VectorType.PROJECTION)
    projectionVector.source.set_vector(Sat2EarthCenter)
    horizontalPlane = vgtSat.planes.item("LocalHorizontal")
    projectionVector.reference_plane.set_plane(horizontalPlane)


Create a new Custom Script Vector

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


Create a new Cross Product Vector

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
    # VectorGeometryToolVectorDisplacement fixedAxesVector: vector component
    VectFactory = vgtSat.vectors.factory
    lineOfNodesVector = VectFactory.create_cross_product("CrossProduct", Sat2EarthCenter, fixedAxesVector)


Create a new Fixed in Axes Vector

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryToolAxes bodyAxes: axes component
    VectFactory = vgtSat.vectors.factory
    fixedAxesVector = VectFactory.create("FixedInAxes", "", VectorType.FIXED_IN_AXES)
    fixedAxesVector.reference_axes.set_axes(bodyAxes)
    fixedAxesVector.direction.assign_xyz(0, 0, 1)


Create a new Displacement Vector

.. code-block:: python

    # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
    # IVectorGeometryPoint centerPtSat: point component
    # IVectorGeometryPoint centerPtEarth: point component
    VectFactory = vgtSat.vectors.factory
    Sat2EarthCenter = VectFactory.create_displacement_vector("Sat2EarthCenter", centerPtSat, centerPtEarth)


Get a default VGT component on vehicle

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


Get the Center point and Inertial System of Earth's central body

.. code-block:: python

    # StkObjectRoot root: STK Object Model root
    centerPtEarth = root.central_bodies.earth.analysis_workbench_components.points.item("Center")
    icrf = root.central_bodies.earth.analysis_workbench_components.systems.item("ICRF")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchComponentProvider


Property detail
---------------

.. py:property:: vectors
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.vectors
    :type: VectorGeometryToolVectorGroup

    Return a group of vectors.

.. py:property:: points
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.points
    :type: VectorGeometryToolPointGroup

    Return a group of points.

.. py:property:: angles
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.angles
    :type: VectorGeometryToolAngleGroup

    Return a group of angles.

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.axes
    :type: VectorGeometryToolAxesGroup

    Return a group of axes.

.. py:property:: planes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.planes
    :type: VectorGeometryToolPlaneGroup

    Return a group of planes.

.. py:property:: systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.systems
    :type: VectorGeometryToolSystemGroup

    Return a group of systems.

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_systems
    :type: VectorGeometryToolWellKnownSystems

    Return well-known systems.

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_axes
    :type: VectorGeometryToolWellKnownAxes

    Return well-known axes.

.. py:property:: time_instants
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_instants
    :type: TimeToolInstantGroup

    Return a group of events.

.. py:property:: time_intervals
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_intervals
    :type: TimeToolTimeIntervalGroup

    Return a group of event intervals.

.. py:property:: calculation_scalars
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.calculation_scalars
    :type: CalculationToolScalarGroup

    Return a group of calc scalars.

.. py:property:: time_arrays
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_arrays
    :type: TimeToolTimeArrayGroup

    Return a group of event arrays.

.. py:property:: time_interval_lists
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_lists
    :type: TimeToolTimeIntervalListGroup

    Return a group of event interval lists.

.. py:property:: time_interval_collections
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_collections
    :type: TimeToolTimeIntervalCollectionGroup

    Return a group of event interval collections.

.. py:property:: parameter_sets
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.parameter_sets
    :type: CalculationToolParameterSetGroup

    Access, add new or remove existing parameter set components.

.. py:property:: conditions
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.conditions
    :type: CalculationToolConditionGroup

    Return a group of condition objects.

.. py:property:: condition_sets
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.condition_sets
    :type: CalculationToolConditionSetGroup

    Return a group of condition set objects.

.. py:property:: volume_grids
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volume_grids
    :type: SpatialAnalysisToolVolumeGridGroup

    Return a group of volume grid objects.

.. py:property:: volumes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volumes
    :type: SpatialAnalysisToolConditionGroup

    Return a group of volume objects.

.. py:property:: spatial_calculations
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.spatial_calculations
    :type: SpatialAnalysisToolCalculationGroup

    Return a group of volume calc objects.


Method detail
-------------

















.. py:method:: supports(self, feature: VectorGeometryToolComponentType) -> bool
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.supports

    Test whether the specified VGT feature is supported.

    :Parameters:

    **feature** : :obj:`~VectorGeometryToolComponentType`

    :Returns:

        :obj:`~bool`


.. py:method:: import_components(self, filename: str) -> AnalysisWorkbenchComponentCollection
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.import_components

    Import Analysis Workbench components from a file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~AnalysisWorkbenchComponentCollection`




