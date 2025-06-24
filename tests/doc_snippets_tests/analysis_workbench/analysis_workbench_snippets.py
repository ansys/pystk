# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

from ansys.stk.core.stkobjects import STKObjectType
from ansys.stk.core.analysis_workbench import (
    AngleType,
    AxesType,
    CalculationScalarType,
    ParameterSetType,
    PointType,
    SystemType,
    VectorType,
)

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, category


class AnalysisWorkbenchSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_root(self):
        return CodeSnippetsTestBase.m_Root

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario

    def test_GetVGTPointSnippet(self):
        self.GetVGTPointSnippet(self.get_root())

    @code_snippet(
        name="GetVGTPoint",
        description="Get the Center point and Inertial System of Earth central body",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def GetVGTPointSnippet(self, root):
        # STKObjectRoot root: STK Object Model root
        centerPtEarth = root.central_bodies.earth.analysis_workbench_components.points.item("Center")
        icrf = root.central_bodies.earth.analysis_workbench_components.systems.item("ICRF")

    def test_GetVGTCompVehicleSnippet(self):
        try:
            satellite = self.get_scenario().children.new(STKObjectType.SATELLITE, "satellite")
            satellite.propagator.propagate()

            self.GetVGTCompVehicleSnippet(satellite)
        finally:
            satellite.unload()

    @code_snippet(
        name="GetVGTCompVehicle",
        description="Get a default VGT component on vehicle",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def GetVGTCompVehicleSnippet(self, satellite):
        # Satellite satellite: Satellite object
        vgtSat = satellite.analysis_workbench_components
        # Get handle to the Center point on the satellite
        centerPtSat = vgtSat.points.item("Center")
        # Get handle to the Body Y Vector
        bodyYSat = vgtSat.vectors.item("Body.Y")
        # Get handle to the Body Axes
        bodyAxes = vgtSat.axes.item("Body")
        icrfAxes = vgtSat.axes.item("ICRF")

    def test_CreateDisplacementVectorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            centerPtSat = parent.analysis_workbench_components.points.item("Center")
            centerPtEarth = parent.analysis_workbench_components.points.item("Center")

            self.CreateDisplacementVectorSnippet(vgtSat, centerPtSat, centerPtEarth)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateDisplacementVector",
        description="Create a new Displacement Vector",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateDisplacementVectorSnippet(self, vgtSat, centerPtSat, centerPtEarth):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # IVectorGeometryPoint centerPtSat: point component
        # IVectorGeometryPoint centerPtEarth: point component
        VectFactory = vgtSat.vectors.factory
        Sat2EarthCenter = VectFactory.create_displacement_vector("Sat2EarthCenter", centerPtSat, centerPtEarth)

    def test_CreateFixedAxesVectorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            bodyAxes = parent.analysis_workbench_components.axes.item("Body")

            self.CreateFixedAxesVectorSnippet(vgtSat, bodyAxes)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateFixedAxesVector",
        description="Create a new Fixed in Axes Vector",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateFixedAxesVectorSnippet(self, vgtSat, bodyAxes):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # IVectorGeometryToolAxes bodyAxes: axes component
        VectFactory = vgtSat.vectors.factory
        fixedAxesVector = VectFactory.create("FixedInAxes", "", VectorType.FIXED_IN_AXES)
        fixedAxesVector.reference_axes.set_axes(bodyAxes)
        fixedAxesVector.direction.assign_xyz(0, 0, 1)

    def test_CreateCrossProductVectorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            point1 = parent.analysis_workbench_components.points.factory.create("Point1", "", PointType.GRAZING)
            point2 = parent.analysis_workbench_components.points.factory.create("Point2", "", PointType.GLINT)
            Sat2EarthCenter = parent.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "MyDisplacementVector3", point1, point2
            )
            point1 = parent.analysis_workbench_components.points.factory.create("Point4", "", PointType.GRAZING)
            point2 = parent.analysis_workbench_components.points.factory.create("Point5", "", PointType.GLINT)
            fixedAxesVector = parent.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "MyDisplacementVector6", point1, point2
            )

            self.CreateCrossProductVectorSnippet(vgtSat, Sat2EarthCenter, fixedAxesVector)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateCrossProductVector",
        description="Create a new Cross Product Vector",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateCrossProductVectorSnippet(self, vgtSat, Sat2EarthCenter, fixedAxesVector):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
        # VectorGeometryToolVectorDisplacement fixedAxesVector: vector component
        VectFactory = vgtSat.vectors.factory
        lineOfNodesVector = VectFactory.create_cross_product("CrossProduct", Sat2EarthCenter, fixedAxesVector)

    @category("ExcludeOnLinux")  # uses vbscript
    def test_CreateScriptVectorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateScriptVectorSnippet(vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateScriptVector",
        description="Create a new Custom Script Vector",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateScriptVectorSnippet(self, vgtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        VectFactory = vgtSat.vectors.factory
        customScript = VectFactory.create("Script", "Description", VectorType.CUSTOM_SCRIPT)
        # Initialization script if needed
        # customScript.InitializationScriptFile = ''
        trainingSamplesDir = r"C:\Program Files\AGI\STK 12\Data\Resources\stktraining\samples"
        scriptFilePath = r"\Heliograph\Scripting\VectorTool\Vector\vector.vbs"
        customScript.script_file = trainingSamplesDir + scriptFilePath
        if customScript.is_valid is False:
            print("Script component not valid!")
            from os import getenv

            customScriptingDir = r"C:\Users\%s\Documents\STK 12\Config\Scripting\VectorTool" % getenv("USERNAME")
            print(r"Copy vbs file from " + trainingSamplesDir + scriptFilePath + r" to " + customScriptingDir)

    def test_CreateProjectionVectorSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            point1 = parent.analysis_workbench_components.points.factory.create("Point1", "", PointType.GRAZING)
            point2 = parent.analysis_workbench_components.points.factory.create("Point2", "", PointType.GLINT)
            Sat2EarthCenter = parent.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "MyDisplacementVector3", point1, point2
            )

            self.CreateProjectionVectorSnippet(vgtSat, Sat2EarthCenter)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateProjectionVector",
        description="Create a new Projection Vector",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateProjectionVectorSnippet(self, vgtSat, Sat2EarthCenter):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
        VectFactory = vgtSat.vectors.factory
        projectionVector = VectFactory.create("Projection", "", VectorType.PROJECTION)
        projectionVector.source.set_vector(Sat2EarthCenter)
        horizontalPlane = vgtSat.planes.item("LocalHorizontal")
        projectionVector.reference_plane.set_plane(horizontalPlane)

    def test_CreateFixedPointSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateFixedPointSnippet(vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateFixedPoint",
        description="Create a new Fixed in System Point",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateFixedPointSnippet(self, vgtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        PtFactory = vgtSat.points.factory
        fixedPt = PtFactory.create("FixedPt", "Point offset from Center", PointType.FIXED_IN_SYSTEM)
        fixedPt.fixed_point.assign_cartesian(0.005, 0, 0.005)

    def test_CreateModelAttachmentPointSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateModelAttachmentPointSnippet(vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateModelAttachmentPoint",
        description="Create a new Model Attachment Point",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateModelAttachmentPointSnippet(self, vgtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        PtFactory = vgtSat.points.factory
        modelPt = PtFactory.create("ModelPt", "Attach point defined in model", PointType.MODEL_ATTACHMENT)
        modelPt.pointable_element_name = "MainSensor-000000"

    def test_CreateFixedTimeInstantPointSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            icrf = parent.analysis_workbench_components.systems.factory.create(
                "MyLocalSystem1", "", SystemType.ASSEMBLED
            )

            self.CreateFixedTimeInstantPointSnippet(vgtSat, icrf)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateFixedTimeInstantPoint",
        description="Create a new Fixed at Time Instant Point",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateFixedTimeInstantPointSnippet(self, vgtSat, icrf):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # VectorGeometryToolSystemAssembled icrf: system component
        PtFactory = vgtSat.points.factory
        timeInstantPt = PtFactory.create("AtTimePt", "Point at time instant", PointType.AT_TIME_INSTANT)
        timeInstantPt.source_point = vgtSat.points.item("Center")
        timeInstantPt.reference_system = icrf
        timeInstantPt.reference_time_instant = vgtSat.time_instants.item("AvailabilityStartTime")

    def test_CreateBetweenAngleSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            point1 = parent.analysis_workbench_components.points.factory.create("Point1", "", PointType.GRAZING)
            point2 = parent.analysis_workbench_components.points.factory.create("Point2", "", PointType.GLINT)
            Sat2EarthCenter = parent.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "MyDisplacementVector3", point1, point2
            )
            bodyYSat = parent.analysis_workbench_components.vectors.factory.create(
                "MyFixedInAxesVector4", "", VectorType.FIXED_IN_AXES
            )

            self.CreateBetweenAngleSnippet(vgtSat, Sat2EarthCenter, bodyYSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateBetweenAngle",
        description="Create a new Between Vectors Angle",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateBetweenAngleSnippet(self, vgtSat, Sat2EarthCenter, bodyYSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
        # VectorGeometryToolVectorFixedInAxes bodyYSat: vector component
        AngFactory = vgtSat.angles.factory
        betwVect = AngFactory.create("SatEarth2Y", "Displacement Vector to Sat Body Y", AngleType.BETWEEN_VECTORS)
        betwVect.from_vector.set_vector(Sat2EarthCenter)
        betwVect.to_vector.set_vector(bodyYSat)

    def test_CreateAlignedConstrainedAxesSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            point1 = parent.analysis_workbench_components.points.factory.create("Point1", "", PointType.GRAZING)
            point2 = parent.analysis_workbench_components.points.factory.create("Point2", "", PointType.GLINT)
            Sat2EarthCenter = parent.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "MyDisplacementVector3", point1, point2
            )
            bodyYSat = parent.analysis_workbench_components.vectors.factory.create(
                "MyFixedInAxesVector4", "", VectorType.FIXED_IN_AXES
            )

            self.CreateAlignedConstrainedAxesSnippet(vgtSat, Sat2EarthCenter, bodyYSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateAlignedConstrainedAxes",
        description="Create new Aligned and Constrained Axes",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateAlignedConstrainedAxesSnippet(self, vgtSat, Sat2EarthCenter, bodyYSat):
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

    def test_CreateAssembledSystemSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            fixedPt = parent.analysis_workbench_components.points.factory.create(
                "MyFixedInSystemPoint1", "", PointType.FIXED_IN_SYSTEM
            )
            bodyAxes = parent.analysis_workbench_components.axes.item("Body")

            self.CreateAssembledSystemSnippet(vgtSat, fixedPt, bodyAxes)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateAssembledSystem",
        description="Create a new Assembled System",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateAssembledSystemSnippet(self, vgtSat, fixedPt, bodyAxes):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # IVectorGeometryPointFixedInSystem fixedPt: point component
        # IVectorGeometryToolAxes bodyAxes: axes component
        SysFactory = vgtSat.systems.factory
        assemSys = SysFactory.create("FixedPtSystem", "System with origin at the new point", SystemType.ASSEMBLED)
        assemSys.origin_point.set_point(fixedPt)
        assemSys.reference_axes.set_axes(bodyAxes)

    def test_CreateVectorMagScalarSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            point1 = parent.analysis_workbench_components.points.factory.create("Point1", "", PointType.GRAZING)
            point2 = parent.analysis_workbench_components.points.factory.create("Point2", "", PointType.GLINT)
            Sat2EarthCenter = parent.analysis_workbench_components.vectors.factory.create_displacement_vector(
                "MyDisplacementVector3", point1, point2
            )

            self.CreateVectorMagScalarSnippet(vgtSat, Sat2EarthCenter)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateVectorMagScalar",
        description="Create a new Vector Magnitude Scalar",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateVectorMagScalarSnippet(self, vgtSat, Sat2EarthCenter):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # VectorGeometryToolVectorDisplacement Sat2EarthCenter: vector component
        calcFactory = vgtSat.calculation_scalars.factory
        vectorMagnitudeSettings = ["VectorDisplacement", "Vector Magnitude of Displacement Vector"]
        displScalar = calcFactory.create_vector_magnitude(*vectorMagnitudeSettings)
        displScalar.input_vector = Sat2EarthCenter

    def test_CreateDataElementScalarSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateDataElementScalarSnippet(vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateDataElementScalar",
        description="Create a Data Element Scalar",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateDataElementScalarSnippet(self, vgtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        calcFactory = vgtSat.calculation_scalars.factory
        trueAnom = calcFactory.create("TrueAnomaly", "", CalculationScalarType.DATA_ELEMENT)
        trueAnom.set_with_group("Classical Elements", "ICRF", "True Anomaly")

    def test_GetScalarAndEvaluateSnippet(self):
        try:
            scenario = self.get_scenario()
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.GetScalarAndEvaluateSnippet(scenario, vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="GetScalarAndEvaluate",
        description="Get a Scalar component and evaluate at a specific time",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def GetScalarAndEvaluateSnippet(self, scenario, vgtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # Scenario scenario: Scenario object
        deticLatitude = vgtSat.calculation_scalars.item("GroundTrajectory.Detic.LLA.Latitude")
        result = deticLatitude.evaluate(scenario.start_time)
        print("The value of detic latitude is %s" % result.value)

    def test_CreateAttitudeParameterSetSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            bodyAxes = parent.analysis_workbench_components.axes.item("Body")
            icrfAxes = parent.analysis_workbench_components.axes.item("Body")

            self.CreateAttitudeParameterSetSnippet(vgtSat, bodyAxes, icrfAxes)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateAttitudeParameterSet",
        description="Create a new Attitude Parameter Set",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateAttitudeParameterSetSnippet(self, vgtSat, bodyAxes, icrfAxes):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # IVectorGeometryToolAxes bodyAxes: axes component
        # IVectorGeometryToolAxes icrfAxes: axes component
        paraFactory = vgtSat.parameter_sets.factory
        paraSet = paraFactory.create("attitudeICRF", "Attitude Set", ParameterSetType.ATTITUDE)
        paraSet.axes = bodyAxes
        paraSet.reference_axes = icrfAxes

    def test_CreateOrbitParameterSetSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateOrbitParameterSetSnippet(vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateOrbitParameterSet",
        description="Create a new Orbit Parameter Set",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateOrbitParameterSetSnippet(self, vgtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        paraFactory = vgtSat.parameter_sets.factory
        paraSetOribit = paraFactory.create("orbitSun", "Orbit", ParameterSetType.ORBIT)
        paraSetOribit.orbiting_point = vgtSat.points.item("Center")
        paraSetOribit.central_body = "Sun"
        paraSetOribit.use_central_body_gravitational_parameter = False
        paraSetOribit.gravitational_parameter = 398600  # km^3/sec^2

    def test_GetTimesFromTimeInstantSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.GetTimesFromTimeInstantSnippet(self.get_root(), vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="GetTimesFromTimeInstant",
        description="Get Times From a Defined Time Instant and create an cell array",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def GetTimesFromTimeInstantSnippet(self, root, vgtSat):
        # STKObjectRoot root: STK Object Model Root
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # Change DateFormat dimension to epoch seconds to make the time easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        satStart = vgtSat.time_instants.item("AvailabilityStartTime")
        start = satStart.find_occurrence().epoch

        satStop = vgtSat.time_instants.item("AvailabilityStopTime")
        stop = satStop.find_occurrence().epoch
        interval = [[start], [540], [600], [stop]]  # EpSec

    def test_CreateTimeInstantSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateTimeInstantSnippet(self.get_root(), vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateTimeInstant",
        description="Create a new Time Instant",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateTimeInstantSnippet(self, root, vgtSat):
        # STKObjectRoot root: STK Object Model Root
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # Change DateFormat dimension to epoch seconds to make the time easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        timeInstFactory = vgtSat.time_instants.factory
        timeEpoch = timeInstFactory.create_epoch("FixedTime", "Fixed Epoch Time")
        timeEpoch.epoch = 3600

    def test_CreateTimeIntervalSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components

            self.CreateTimeIntervalSnippet(self.get_root(), vgtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateTimeInterval",
        description="Create a new Time Interval",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateTimeIntervalSnippet(self, root, vgtSat):
        # STKObjectRoot root: STK Object Model Root
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # Change DateFormat dimension to epoch seconds to make the time easier to handle in
        # Python
        root.units_preferences.item("DateFormat").set_current_unit("EpSec")
        timeIntFactory = vgtSat.time_intervals.factory
        timeInterval = timeIntFactory.create_fixed("TimeInterval", "Fixed time interval")
        timeInterval.set_interval(60, 120)

    def test_CreateCollectionListSnippet(self):
        try:
            parent = self.get_scenario().children.new(STKObjectType.SATELLITE, "parent")
            parent.propagator.propagate()
            vgtSat = parent.analysis_workbench_components
            centerPtSat = parent.analysis_workbench_components.points.item("Center")

            self.CreateCollectionListSnippet(vgtSat, centerPtSat)
        finally:
            parent.unload()

    @code_snippet(
        name="CreateCollectionList",
        description="Create a new Collection of Interval List",
        category="Analysis Workbench",
        eid="analysis_workbench~AnalysisWorkbenchComponentProvider",
    )
    def CreateCollectionListSnippet(self, vgtSat, centerPtSat):
        # AnalysisWorkbenchComponentProvider vgtSat: Vector Geometry Tool Interface
        # IVectorGeometryPoint centerPtSat: point component
        timeCollListFactory = vgtSat.time_interval_collections.factory
        timeColl = timeCollListFactory.create_lighting("LightingList", "Collection of lighting intervals")
        timeColl.use_object_eclipsing_bodies = True
        timeColl.location = centerPtSat
