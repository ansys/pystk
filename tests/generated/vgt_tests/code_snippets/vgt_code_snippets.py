from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.vgt import *


class VGT(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(VGT, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.InitializeWithNewScenario(True)
        sat: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1"), Satellite
        )
        sat.set_propagator_type(PROPAGATOR_TYPE.TWO_BODY)
        (clr.CastAs(sat.propagator, PropagatorTwoBody)).propagate()

        fac: "Facility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "Facility1"), Facility
        )

        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        scenario.epoch = "1 Jan 2012 12:00:00.000"

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        TestBase.Application.units_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.units_preferences.set_current_unit("TimeUnit", "sec")

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region rootGetVGTProvider
    def test_rootGetVGTProvider(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        try:
            self.rootGetVGTProvider(root, "Satellite/Satellite1")

        finally:
            del root

    def rootGetVGTProvider(self, root: "AnalysisWorkbenchRoot", path: str):
        # Returns a provider associated with the specified
        # instance of an STK Object or a Central Body.
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider(path)

    # endregion

    # region rootGetVGTTemplateProvider
    def test_rootGetVGTTemplateProvider(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        try:
            self.rootGetVGTTemplateProvider(root, "Satellite")

        finally:
            del root

    def rootGetVGTTemplateProvider(self, root: "AnalysisWorkbenchRoot", className: str):
        # Returns a VGT provider associated with the specified
        # STK object class (i.e., Satellite, Facility, etc.) or
        # a Central Body.
        provider: "AnalysisWorkbenchComponentProvider" = root.get_template_provider(className)

    # endregion

    # region EnumerateThroughVectors
    def test_EnumerateThroughVectors(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughVectors(provider)

        finally:
            del root

    def EnumerateThroughVectors(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing vectors using specified CrdnProvider.
        vector: "IVectorGeometryToolVector"
        # Enumerate the existing vectors using specified CrdnProvider.
        for vector in provider.vectors:
            # All vectors implement IAnalysisWorkbenchComponent interface which provides
            # information about the vector instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(vector, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, vector.type)

    # endregion

    # region EnumerateThroughPoints
    def test_EnumerateThroughPoints(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughPoints(provider)

        finally:
            del root

    def EnumerateThroughPoints(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing points using specified CrdnProvider.
        point: "IVectorGeometryToolPoint"
        # Enumerate the existing points using specified CrdnProvider.
        for point in provider.points:
            # All points implement IAnalysisWorkbenchComponent interface which provides
            # information about the point instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(point, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, point.type)

    # endregion

    # region EnumerateThroughAngles
    def test_EnumerateThroughAngles(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughAngles(provider)

        finally:
            del root

    def EnumerateThroughAngles(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing angles using specified CrdnProvider.
        angle: "IVectorGeometryToolAngle"
        # Enumerate the existing angles using specified CrdnProvider.
        for angle in provider.angles:
            # All angles implement IAnalysisWorkbenchComponent interface which provides
            # information about the angle instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(angle, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, angle.type)

    # endregion

    # region EnumerateThroughAxes
    def test_EnumerateThroughAxes(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughAxes(provider)

        finally:
            del root

    def EnumerateThroughAxes(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing Axes using specified CrdnProvider.
        axes: "IVectorGeometryToolAxes"
        # Enumerate the existing Axes using specified CrdnProvider.
        for axes in provider.axes:
            # All axes implement IAnalysisWorkbenchComponent interface which provides
            # information about the axes instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(axes, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, axes.type)

    # endregion

    # region EnumerateThroughPlanes
    def test_EnumerateThroughPlanes(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughPlanes(provider)

        finally:
            del root

    def EnumerateThroughPlanes(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing Planes using specified CrdnProvider.
        plane: "IVectorGeometryToolPlane"
        # Enumerate the existing Planes using specified CrdnProvider.
        for plane in provider.planes:
            # All planes implement IAnalysisWorkbenchComponent interface which provides
            # information about the plane instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(plane, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, plane.type)

    # endregion

    # region EnumerateThroughSystems
    def test_EnumerateThroughSystems(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughSystems(provider)

        finally:
            del root

    def EnumerateThroughSystems(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing Systems using specified CrdnProvider.
        system: "IVectorGeometryToolSystem"
        # Enumerate the existing Systems using specified CrdnProvider.
        for system in provider.systems:
            # All systems implement IAnalysisWorkbenchComponent interface which provides
            # information about the system instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(system, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, system.type)

    # endregion

    # region EnumerateThroughParameterSets
    def test_EnumerateThroughParameterSets(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughParameterSets(provider)

        finally:
            del root

    def EnumerateThroughParameterSets(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing ParameterSets using specified CrdnProvider.
        parameterSet: "ICalculationToolParameterSet"
        # Enumerate the existing ParameterSets using specified CrdnProvider.
        for parameterSet in provider.parameter_sets:
            # All parameter sets implement IAnalysisWorkbenchComponent interface which provides
            # information about the parameter set instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(parameterSet, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, parameterSet.type)

    # endregion

    # region EnumerateThroughCalcScalars
    def test_EnumerateThroughCalcScalars(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughCalcScalars(provider)

        finally:
            del root

    def EnumerateThroughCalcScalars(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing CalcScalars using specified CrdnProvider.
        calcScalar: "ICalculationToolScalar"
        # Enumerate the existing CalcScalars using specified CrdnProvider.
        for calcScalar in provider.calculation_scalars:
            # All calc scalars implement IAnalysisWorkbenchComponent interface which provides
            # information about the calc scalar instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(calcScalar, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, calcScalar.type)

    # endregion

    # region EnumerateThroughConditions
    def test_EnumerateThroughConditions(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughConditions(provider)

        finally:
            del root

    def EnumerateThroughConditions(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing Conditions using specified CrdnProvider.
        condition: "ICalculationToolCondition"
        # Enumerate the existing Conditions using specified CrdnProvider.
        for condition in provider.conditions:
            # All conditions implement IAnalysisWorkbenchComponent interface which provides
            # information about the condition instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(condition, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, condition.type)

    # endregion

    # region EnumerateThroughEvents
    def test_EnumerateThroughEvents(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEvents(provider)

        finally:
            del root

    def EnumerateThroughEvents(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing Events using specified CrdnProvider.
        event: "ITimeToolInstant"
        # Enumerate the existing Events using specified CrdnProvider.
        for event in provider.time_instants:
            # All events implement IAnalysisWorkbenchComponent interface which provides
            # information about the event instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(event, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, event.type)

    # endregion

    # region EnumerateThroughEventArrays
    def test_EnumerateThroughEventArrays(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventArrays(provider)

        finally:
            del root

    def EnumerateThroughEventArrays(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing EventArrays using specified CrdnProvider.
        eventArray: "ITimeToolTimeArray"
        # Enumerate the existing EventArrays using specified CrdnProvider.
        for eventArray in provider.time_arrays:
            # All event arrays implement IAnalysisWorkbenchComponent interface which provides
            # information about the event array instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventArray, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventArray.type)

    # endregion

    # region EnumerateThroughEventIntervals
    def test_EnumerateThroughEventIntervals(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervals(provider)

        finally:
            del root

    def EnumerateThroughEventIntervals(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing EventIntervals using specified CrdnProvider.
        eventInterval: "ITimeToolTimeInterval"
        # Enumerate the existing EventIntervals using specified CrdnProvider.
        for eventInterval in provider.time_intervals:
            # All event intervals implement IAnalysisWorkbenchComponent interface which provides
            # information about the event interval instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventInterval, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventInterval.type)

    # endregion

    # region EnumerateThroughEventIntervalCollections
    def test_EnumerateThroughEventIntervalCollections(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervalCollections(provider)

        finally:
            del root

    def EnumerateThroughEventIntervalCollections(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing EventIntervalCollections using specified CrdnProvider.
        eventIntervalCollection: "ITimeToolTimeIntervalCollection"
        # Enumerate the existing EventIntervalCollections using specified CrdnProvider.
        for eventIntervalCollection in provider.time_interval_collections:
            # All event interval collections implement IAnalysisWorkbenchComponent interface which provides
            # information about the event interval collection instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventIntervalCollection, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalCollection.type)

    # endregion

    # region EnumerateThroughEventIntervalLists
    def test_EnumerateThroughEventIntervalLists(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervalLists(provider)

        finally:
            del root

    def EnumerateThroughEventIntervalLists(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Enumerate the existing EventIntervalLists using specified CrdnProvider.
        eventIntervalList: "ITimeToolTimeIntervalList"
        # Enumerate the existing EventIntervalLists using specified CrdnProvider.
        for eventIntervalList in provider.time_interval_lists:
            # All event interval lists implement IAnalysisWorkbenchComponent interface which provides
            # information about the event interval list instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventIntervalList, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalList.type)

    # endregion

    # region IterateThroughVectors
    def test_IterateThroughVectors(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughVectors(provider)

        finally:
            del root

    def IterateThroughVectors(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.vectors.count:
            vector: "IVectorGeometryToolVector" = provider.vectors[i]
            # All vectors implement IAnalysisWorkbenchComponent interface which provides
            # information about the vector instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(vector, IAnalysisWorkbenchComponent)
            # Print the vector name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, vector.type)

            i += 1

    # endregion

    # region IterateThroughPoint
    def test_IterateThroughPoints(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughPoints(provider)

        finally:
            del root

    def IterateThroughPoints(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.points.count:
            point: "IVectorGeometryToolPoint" = provider.points[i]
            # All points implement IAnalysisWorkbenchComponent interface which provides
            # information about the point instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.points[i], IAnalysisWorkbenchComponent)
            # Print the point name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, point.type)

            i += 1

    # endregion

    # region IterateThroughAngles
    def test_IterateThroughAngles(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughAngles(provider)

        finally:
            del root

    def IterateThroughAngles(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.angles.count:
            angle: "IVectorGeometryToolAngle" = provider.angles[i]
            # All angles implement IAnalysisWorkbenchComponent interface which provides
            # information about the angle instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.angles[i], IAnalysisWorkbenchComponent)
            # Print the angle name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, angle.type)

            i += 1

    # endregion

    # region IterateThroughAxes
    def test_IterateThroughAxes(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughAxes(provider)

        finally:
            del root

    def IterateThroughAxes(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.axes.count:
            axes: "IVectorGeometryToolAxes" = provider.axes[i]
            # All axes implement IAnalysisWorkbenchComponent interface which provides
            # information about the axes instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.axes[i], IAnalysisWorkbenchComponent)
            # Print the axes name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, axes.type)

            i += 1

    # endregion

    # region IterateThroughPlanes
    def test_IterateThroughPlanes(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughPlanes(provider)

        finally:
            del root

    def IterateThroughPlanes(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.planes.count:
            plane: "IVectorGeometryToolPlane" = provider.planes[i]
            # All planes implement IAnalysisWorkbenchComponent interface which provides
            # information about the plane's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.planes[i], IAnalysisWorkbenchComponent)
            # Print the plane's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, plane.type)

            i += 1

    # endregion

    # region IterateThroughSystems
    def test_IterateThroughSystems(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughSystems(provider)

        finally:
            del root

    def IterateThroughSystems(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.systems.count:
            crdnSystem: "IVectorGeometryToolSystem" = provider.systems[i]
            # All coordinate reference frames implement IAnalysisWorkbenchComponent interface which provides
            # information about the reference frame's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.systems[i], IAnalysisWorkbenchComponent)
            # Print the reference frame's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, crdnSystem.type)

            i += 1

    # endregion

    # region IterateThroughParameterSets
    def test_IterateThroughParameterSets(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughParameterSets(provider)

        finally:
            del root

    def IterateThroughParameterSets(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.parameter_sets.count:
            parameterSet: "ICalculationToolParameterSet" = provider.parameter_sets[i]
            # All parameter sets implement IAnalysisWorkbenchComponent interface which provides
            # information about the parameter set's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.parameter_sets[i], IAnalysisWorkbenchComponent)
            # Print the parameter set's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, parameterSet.type)

            i += 1

    # endregion

    # region IterateThroughCalcScalars
    def test_IterateThroughCalcScalars(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughCalcScalars(provider)

        finally:
            del root

    def IterateThroughCalcScalars(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.calculation_scalars.count:
            calcScalar: "ICalculationToolScalar" = provider.calculation_scalars[i]
            # All calc scalars implement IAnalysisWorkbenchComponent interface which provides
            # information about the calc scalar's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.calculation_scalars[i], IAnalysisWorkbenchComponent
            )
            # Print the calc scalar's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, calcScalar.type)

            i += 1

    # endregion

    # region IterateThroughConditions
    def test_IterateThroughConditions(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughConditions(provider)

        finally:
            del root

    def IterateThroughConditions(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.conditions.count:
            condition: "ICalculationToolCondition" = provider.conditions[i]
            # All conditions implement IAnalysisWorkbenchComponent interface which provides
            # information about the condition's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.conditions[i], IAnalysisWorkbenchComponent)
            # Print the condition's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, condition.type)

            i += 1

    # endregion

    # region IterateThroughEvents
    def test_IterateThroughEvents(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEvents(provider)

        finally:
            del root

    def IterateThroughEvents(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.time_instants.count:
            event: "ITimeToolInstant" = provider.time_instants[i]
            # All events implement IAnalysisWorkbenchComponent interface which provides
            # information about the event's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.time_instants[i], IAnalysisWorkbenchComponent)
            # Print the event's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, event.type)

            i += 1

    # endregion

    # region IterateThroughEventArrays
    def test_IterateThroughEventArrays(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventArrays(provider)

        finally:
            del root

    def IterateThroughEventArrays(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.time_arrays.count:
            eventArray: "ITimeToolTimeArray" = provider.time_arrays[i]
            # All event arrays implement IAnalysisWorkbenchComponent interface which provides
            # information about the event array's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.time_arrays[i], IAnalysisWorkbenchComponent)
            # Print the event array's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventArray.type)

            i += 1

    # endregion

    # region IterateThroughEventIntervals
    def test_IterateThroughEventIntervals(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervals(provider)

        finally:
            del root

    def IterateThroughEventIntervals(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.time_intervals.count:
            eventInterval: "ITimeToolTimeInterval" = provider.time_intervals[i]
            # All event intervals implement IAnalysisWorkbenchComponent interface which provides
            # information about the event interval's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.time_intervals[i], IAnalysisWorkbenchComponent)
            # Print the event interval's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventInterval.type)

            i += 1

    # endregion

    # region IterateThroughEventIntervalCollections
    def test_IterateThroughEventIntervalCollections(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervalCollections(provider)

        finally:
            del root

    def IterateThroughEventIntervalCollections(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.time_interval_collections.count:
            eventIntervalCollection: "ITimeToolTimeIntervalCollection" = provider.time_interval_collections[i]
            # All event interval collections implement IAnalysisWorkbenchComponent interface which provides
            # information about the event interval collection's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.time_interval_collections[i], IAnalysisWorkbenchComponent
            )
            # Print the event interval collection's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalCollection.type)

            i += 1

    # endregion

    # region IterateThroughEventIntervalLists
    def test_IterateThroughEventIntervalLists(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervalLists(provider)

        finally:
            del root

    def IterateThroughEventIntervalLists(self, provider: "AnalysisWorkbenchComponentProvider"):
        i: int = 0
        while i < provider.time_interval_lists.count:
            eventIntervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists[i]
            # All event interval lists implement IAnalysisWorkbenchComponent interface which provides
            # information about the event interval list's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.time_interval_lists[i], IAnalysisWorkbenchComponent
            )
            # Print the event interval list's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalList.type)

            i += 1

    # endregion

    # region CreateAngleRateVector
    def test_CreateAngleRateVector(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("myVector")))
        try:
            self.CreateAngleRateVector(provider)

        finally:
            provider.vectors.remove("myVector")
            del root

    def CreateAngleRateVector(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Create a vector.perpendicular to the plane in which the angle is defined.
        vector: "VectorGeometryToolVectorAngleRate" = VectorGeometryToolVectorAngleRate(
            provider.vectors.factory.create(
                "myVector", "a vector.perpendicular to the plane in which the angle is defined.", VECTOR_TYPE.ANGLE_RATE
            )
        )

    # endregion

    # region IsVectorTypeSupported
    def test_IsVectorTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("myVector")))
        try:
            self.IsVectorTypeSupported(provider, VECTOR_TYPE.ANGLE_RATE)

        finally:
            provider.vectors.remove("myVector")
            del root

    def IsVectorTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", vectorType: "VECTOR_TYPE"):
        if provider.vectors.factory.is_type_supported(vectorType):
            # Create a custom vector.
            vector: "IVectorGeometryToolVector" = provider.vectors.factory.create("myVector", String.Empty, vectorType)

    # endregion

    # region CreateDisplacementVector
    def test_CreateDisplacementVector(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("Point1")))
        Assert.assertTrue((not provider.points.contains("Point2")))
        p: "IVectorGeometryToolPoint" = provider.points.factory.create("Point1", String.Empty, POINT_TYPE.GLINT)
        p2: "IVectorGeometryToolPoint" = provider.points.factory.create("Point2", String.Empty, POINT_TYPE.GRAZING)
        try:
            self.CreateDisplacementVector(provider, p, p2)

        finally:
            provider.points.remove("Point1")
            provider.points.remove("Point2")
            del root

    def CreateDisplacementVector(
        self,
        provider: "AnalysisWorkbenchComponentProvider",
        OriginPoint: "IVectorGeometryToolPoint",
        DestinationPoint: "IVectorGeometryToolPoint",
    ):
        # Create a displacement vector with two specified points
        vector: "VectorGeometryToolVectorDisplacement" = provider.vectors.factory.create_displacement_vector(
            "VectorName", OriginPoint, DestinationPoint
        )

    # endregion

    # region CreateCrossProductVector
    def test_CreateCrossProductVector(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("Vector1")))
        Assert.assertTrue((not provider.vectors.contains("Vector2")))
        v1: "IVectorGeometryToolVector" = provider.vectors.factory.create("Vector1", "", VECTOR_TYPE.LINE_OF_NODES)
        v2: "IVectorGeometryToolVector" = provider.vectors.factory.create("Vector2", "", VECTOR_TYPE.ECCENTRICITY)
        try:
            self.CreateCrossProductVector(provider, v1, v2)

        finally:
            provider.vectors.remove("Vector1")
            provider.vectors.remove("Vector2")
            del root

    def CreateCrossProductVector(
        self,
        provider: "AnalysisWorkbenchComponentProvider",
        VectorA: "IVectorGeometryToolVector",
        VectorB: "IVectorGeometryToolVector",
    ):
        # Create a vector defined as cross product of vectors A and B.
        vector: "VectorGeometryToolVectorCross" = provider.vectors.factory.create_cross_product(
            "CrossVector", VectorA, VectorB
        )

    # endregion

    # region VectorContains
    def test_VectorContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.VectorContains(provider, "FlightPath")

        finally:
            del root

    def VectorContains(self, provider: "AnalysisWorkbenchComponentProvider", VectorName: str):
        if provider.vectors.contains(VectorName):
            Console.WriteLine("The vector {0} already exists!", VectorName)

    # endregion

    # region VectorRemove
    def test_VectorRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("SomeVector")))
        someVector: "IVectorGeometryToolVector" = provider.vectors.factory.create(
            "SomeVector", String.Empty, VECTOR_TYPE.DISPLACEMENT
        )
        try:
            self.VectorRemove(provider, (IAnalysisWorkbenchComponent(someVector)).name)

        finally:
            del root

    def VectorRemove(self, provider: "AnalysisWorkbenchComponentProvider", VectorName: str):
        if provider.vectors.contains(VectorName):
            provider.vectors.remove(VectorName)

    # endregion

    # region CreateAngleBetweenPlanes
    def test_CreateAngleBetweenPlanes(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        try:
            self.CreateAngleBetweenPlanes(provider)

        finally:
            provider.angles.remove("AngleName")
            del root

    def CreateAngleBetweenPlanes(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Create an angle between two planes.
        angle: "VectorGeometryToolAngleBetweenPlanes" = VectorGeometryToolAngleBetweenPlanes(
            provider.angles.factory.create("AngleName", "Angle from one plane to another.", ANGLE_TYPE.BETWEEN_PLANES)
        )

    # endregion

    # region IsAngleTypeSupported
    def test_IsAngleTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("MyAngle")))
        try:
            self.IsAngleTypeSupported(provider, ANGLE_TYPE.BETWEEN_PLANES)

        finally:
            provider.angles.remove("MyAngle")
            del root

    # Review: see the comments for the Vector
    def IsAngleTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", angleType: "ANGLE_TYPE"):
        if provider.angles.factory.is_type_supported(angleType):
            # Create an Angle with the supported Type
            angle: "IVectorGeometryToolAngle" = provider.angles.factory.create("MyAngle", String.Empty, angleType)

    # endregion

    # region AngleContains
    def test_AngleContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.AngleContains(provider)

        finally:
            del root

    # Review: see the comments for the Angle
    def AngleContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.angles.contains("AngleName"):
            Console.WriteLine('The angle "{0}" already exists!', "AngleName")

    # endregion

    # region AngleRemove
    def test_AngleRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.angles.factory.create(
            "AngleName", String.Empty, ANGLE_TYPE.BETWEEN_PLANES
        )
        try:
            self.AngleRemove(provider)

        finally:
            del root

    def AngleRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.angles.contains("AngleName"):
            provider.angles.remove("AngleName")

    # endregion

    # region CreateNormalPlane
    def test_CreateNormalPlane(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.planes.contains("PlaneName")))
        try:
            self.CreateNormalPlane(provider)

        finally:
            provider.planes.remove("PlaneName")
            del root

    def CreateNormalPlane(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Create a plane normal to vector.
        p: "VectorGeometryToolPlaneNormal" = VectorGeometryToolPlaneNormal(
            provider.planes.factory.create("PlaneName", "A plane normal to vector.", PLANE_TYPE.NORMAL)
        )

    # endregion

    # region IsPlaneTypeSupported
    def test_IsPlaneTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.planes.contains("PlaneName")))
        try:
            self.IsPlaneTypeSupported(provider, PLANE_TYPE.NORMAL)

        finally:
            provider.planes.remove("PlaneName")
            del root

    def IsPlaneTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", planeType: "PLANE_TYPE"):
        if provider.planes.factory.is_type_supported(planeType):
            p: "IVectorGeometryToolPlane" = provider.planes.factory.create("PlaneName", String.Empty, planeType)

    # endregion

    # region PlaneContains
    def test_PlaneContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.PlaneContains(provider)

        finally:
            del root

    def PlaneContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.planes.contains("PlaneName"):
            Console.WriteLine('The plane "{0}" already exists!', "PlaneName")

    # endregion

    # region PlaneRemove
    def test_PlaneRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.planes.contains("PlaneName")))
        plane: "IVectorGeometryToolPlane" = provider.planes.factory.create("PlaneName", String.Empty, PLANE_TYPE.NORMAL)
        try:
            self.PlaneRemove(provider)

        finally:
            del root

    def PlaneRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.planes.contains("PlaneName"):
            provider.planes.remove("PlaneName")

    # endregion

    # region CreateAxesAlignedAndConstrained
    def test_CreateAxesAlignedAndConstrained(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        try:
            self.CreateAxesAlignedAndConstrained(provider)

        finally:
            provider.axes.remove("AxesName")
            del root

    def CreateAxesAlignedAndConstrained(self, provider: "AnalysisWorkbenchComponentProvider"):
        axes: "VectorGeometryToolAxesAlignedAndConstrained" = VectorGeometryToolAxesAlignedAndConstrained(
            provider.axes.factory.create("AxesName", String.Empty, AXES_TYPE.ALIGNED_AND_CONSTRAINED)
        )

    # endregion

    # region IsAxesTypeSupported
    def test_IsAxesTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        try:
            self.IsAxesTypeSupported(provider, AXES_TYPE.ALIGNED_AND_CONSTRAINED)

        finally:
            provider.axes.remove("AxesName")
            del root

    def IsAxesTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", axesType: "AXES_TYPE"):
        if provider.axes.factory.is_type_supported(axesType):
            axes: "IVectorGeometryToolAxes" = provider.axes.factory.create("AxesName", String.Empty, axesType)

    # endregion

    # region AxesContains
    def test_AxesContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.AxesContains(provider)

        finally:
            del root

    def AxesContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.axes.contains("AxesName"):
            Console.WriteLine('Axes "{0}" already exist!', "AxesName")

    # endregion

    # region AxesRemove
    def test_AxesRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        axes: "IVectorGeometryToolAxes" = provider.axes.factory.create("AxesName", String.Empty, AXES_TYPE.FIXED)
        try:
            self.AxesRemove(provider)

        finally:
            del root

    def AxesRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.axes.contains("AxesName"):
            provider.axes.remove("AxesName")

    # endregion

    # region CreatePointBPlane
    def test_CreatePointBPlane(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        try:
            self.CreatePointBPlane(provider, "Earth")

        finally:
            provider.points.remove("PointName")
            del root

    def CreatePointBPlane(self, provider: "AnalysisWorkbenchComponentProvider", TargetBody: str):
        # Create a B-Plane point using selected target body
        point: "VectorGeometryToolPointBPlane" = VectorGeometryToolPointBPlane(
            provider.points.factory.create("PointName", String.Empty, POINT_TYPE.B_PLANE)
        )
        point.target_body.set_path(TargetBody)

    # endregion

    # region IsPointTypeSupported
    def test_IsPointTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        try:
            self.IsPointTypeSupported(provider, POINT_TYPE.B_PLANE)

        finally:
            provider.points.remove("PointName")
            del root

    def IsPointTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", PointType: "POINT_TYPE"):
        if provider.points.factory.is_type_supported(PointType):
            point: "IVectorGeometryToolPoint" = provider.points.factory.create("PointName", String.Empty, PointType)

    # endregion

    # region PointContains
    def test_PointContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.PointContains(provider)

        finally:
            del root

    def PointContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.points.contains("PointName"):
            Console.WriteLine('The point "{0}" exists!', "PointName")

    # endregion

    # region PointRemove
    def test_PointRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "PointName", String.Empty, POINT_TYPE.FIXED_IN_SYSTEM
        )
        try:
            self.PointRemove(provider)

        finally:
            del root

    def PointRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.points.contains("PointName"):
            provider.points.remove("PointName")

    # endregion

    # region CreateSystemAssembled
    def test_CreateSystemAssembled(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.systems.contains("SystemName")))
        try:
            self.CreateSystemAssembled(provider, provider.points["Center"], provider.axes["Body"])

        finally:
            provider.systems.remove("SystemName")
            del root

    def CreateSystemAssembled(
        self,
        provider: "AnalysisWorkbenchComponentProvider",
        OriginPoint: "IVectorGeometryToolPoint",
        ReferenceAxes: "IVectorGeometryToolAxes",
    ):
        system: "VectorGeometryToolSystemAssembled" = VectorGeometryToolSystemAssembled(
            provider.systems.factory.create("SystemName", String.Empty, SYSTEM_TYPE.ASSEMBLED)
        )
        # Set the system's origin point.
        system.origin_point.set_point(OriginPoint)
        # Set the system's reference axes.
        system.reference_axes.set_axes(ReferenceAxes)

    # endregion

    # region IsSystemTypeSupported
    def test_IsSystemTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.systems.contains("SystemName")))
        try:
            self.IsSystemTypeSupported(provider, SYSTEM_TYPE.ASSEMBLED)

        finally:
            provider.systems.remove("SystemName")
            del root

    def IsSystemTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", SystemType: "SYSTEM_TYPE"):
        if provider.systems.factory.is_type_supported(SystemType):
            # Create a System with supported Type
            system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
                "SystemName", String.Empty, SystemType
            )

    # endregion

    # region SystemContains
    def test_SystemContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.SystemContains(provider)

        finally:
            del root

    def SystemContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.systems.contains("SystemName"):
            Console.WriteLine('The system "{0}" exists!', "SystemName")

    # endregion

    # region SystemRemove
    def test_SystemRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.systems.contains("SystemName")))
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "SystemName", String.Empty, SYSTEM_TYPE.ASSEMBLED
        )
        try:
            self.SystemRemove(provider)

        finally:
            del root

    def SystemRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.systems.contains("SystemName"):
            provider.systems.remove("SystemName")

    # endregion

    # region CreateParameterSetAttitude
    def test_CreateParameterSetAttitude(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.parameter_sets.contains("ParameterSetName")))
        try:
            self.CreateParameterSetAttitude(provider)

        finally:
            provider.parameter_sets.remove("ParameterSetName")
            del root

    def CreateParameterSetAttitude(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Create an attitude parameter set.
        parameterSet: "CalculationToolParameterSetAttitude" = CalculationToolParameterSetAttitude(
            provider.parameter_sets.factory.create(
                "ParameterSetName", "Attitude parameter set.", PARAMETER_SET_TYPE.ATTITUDE
            )
        )

    # endregion

    # region IsParameterSetTypeSupported
    def test_IsParameterSetTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.parameter_sets.contains("MyParameterSet")))
        try:
            self.IsParameterSetTypeSupported(provider, PARAMETER_SET_TYPE.ATTITUDE)

        finally:
            provider.parameter_sets.remove("MyParameterSet")
            del root

    def IsParameterSetTypeSupported(
        self, provider: "AnalysisWorkbenchComponentProvider", parameterSetType: "PARAMETER_SET_TYPE"
    ):
        if provider.parameter_sets.factory.is_type_supported(parameterSetType):
            # Create a ParameterSet with the supported Type
            parameterSet: "ICalculationToolParameterSet" = provider.parameter_sets.factory.create(
                "MyParameterSet", String.Empty, parameterSetType
            )

    # endregion

    # region ParameterSetContains
    def test_ParameterSetContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.ParameterSetContains(provider)

        finally:
            del root

    def ParameterSetContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.parameter_sets.contains("ParameterSetName"):
            Console.WriteLine('The parameter set "{0}" already exists!', "ParameterSetName")

    # endregion

    # region ParameterSetRemove
    def test_ParameterSetRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.parameter_sets.contains("ParameterSetName")))
        parameterSet: "ICalculationToolParameterSet" = provider.parameter_sets.factory.create(
            "ParameterSetName", String.Empty, PARAMETER_SET_TYPE.ATTITUDE
        )
        try:
            self.ParameterSetRemove(provider)

        finally:
            del root

    def ParameterSetRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.parameter_sets.contains("ParameterSetName"):
            provider.parameter_sets.remove("ParameterSetName")

    # endregion

    # region CreateCalcScalarConstant
    def test_CreateCalcScalarConstant(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.calculation_scalars.contains("CalcScalarName")))
        try:
            self.CreateCalcScalarConstant(provider)

        finally:
            provider.calculation_scalars.remove("CalcScalarName")
            del root

    def CreateCalcScalarConstant(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Create a calc scalar constant.
        calcScalar: "CalculationToolScalarConstant" = CalculationToolScalarConstant(
            provider.calculation_scalars.factory.create(
                "CalcScalarName", "Calc scalar constant.", CALCULATION_SCALAR_TYPE.CONSTANT
            )
        )

    # endregion

    # region IsCalcScalarTypeSupported
    def test_IsCalcScalarTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.calculation_scalars.contains("MyCalcScalar")))
        try:
            self.IsCalcScalarTypeSupported(provider, CALCULATION_SCALAR_TYPE.CONSTANT)

        finally:
            provider.calculation_scalars.remove("MyCalcScalar")
            del root

    def IsCalcScalarTypeSupported(
        self, provider: "AnalysisWorkbenchComponentProvider", calcScalarType: "CALCULATION_SCALAR_TYPE"
    ):
        if provider.calculation_scalars.factory.is_type_supported(calcScalarType):
            # Create a CalcScalar with the supported Type
            calcScalar: "ICalculationToolScalar" = provider.calculation_scalars.factory.create(
                "MyCalcScalar", String.Empty, calcScalarType
            )

    # endregion

    # region CalcScalarContains
    def test_CalcScalarContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.CalcScalarContains(provider)

        finally:
            del root

    def CalcScalarContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.calculation_scalars.contains("CalcScalarName"):
            Console.WriteLine('The calc scalar "{0}" already exists!', "CalcScalarName")

    # endregion

    # region CalcScalarRemove
    def test_CalcScalarRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.calculation_scalars.contains("CalcScalarName")))
        calcScalar: "ICalculationToolScalar" = provider.calculation_scalars.factory.create(
            "CalcScalarName", String.Empty, CALCULATION_SCALAR_TYPE.CONSTANT
        )
        try:
            self.CalcScalarRemove(provider)

        finally:
            del root

    def CalcScalarRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.calculation_scalars.contains("CalcScalarName"):
            provider.calculation_scalars.remove("CalcScalarName")

    # endregion

    # region CreateConditionScalarBounds
    def test_CreateConditionScalarBounds(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.conditions.contains("ConditionName")))
        try:
            self.CreateConditionScalarBounds(provider)

        finally:
            provider.conditions.remove("ConditionName")
            del root

    def CreateConditionScalarBounds(self, provider: "AnalysisWorkbenchComponentProvider"):
        # Create a condition from a scalar.
        condition: "CalculationToolConditionScalarBounds" = CalculationToolConditionScalarBounds(
            provider.conditions.factory.create(
                "ConditionName", "Condition from a scalar.", CONDITION_TYPE.SCALAR_BOUNDS
            )
        )

    # endregion

    # region IsConditionTypeSupported
    def test_IsConditionTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.conditions.contains("MyCondition")))
        try:
            self.IsConditionTypeSupported(provider, CONDITION_TYPE.SCALAR_BOUNDS)

        finally:
            provider.conditions.remove("MyCondition")
            del root

    def IsConditionTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", conditionType: "CONDITION_TYPE"):
        if provider.conditions.factory.is_type_supported(conditionType):
            # Create a Condition with the supported Type
            condition: "ICalculationToolCondition" = provider.conditions.factory.create(
                "MyCondition", String.Empty, conditionType
            )

    # endregion

    # region ConditionContains
    def test_ConditionContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.ConditionContains(provider)

        finally:
            del root

    def ConditionContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.conditions.contains("ConditionName"):
            Console.WriteLine('The condition "{0}" already exists!', "ConditionName")

    # endregion

    # region ConditionRemove
    def test_ConditionRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.conditions.contains("ConditionName")))
        condition: "ICalculationToolCondition" = provider.conditions.factory.create(
            "ConditionName", String.Empty, CONDITION_TYPE.SCALAR_BOUNDS
        )
        try:
            self.ConditionRemove(provider)

        finally:
            del root

    def ConditionRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.conditions.contains("ConditionName"):
            provider.conditions.remove("ConditionName")

    # endregion

    # region IsEventTypeSupported
    def test_IsEventTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_instants.contains("MyEvent")))
        try:
            self.IsEventTypeSupported(provider, TIME_EVENT_TYPE.EPOCH)

        finally:
            provider.time_instants.remove("MyEvent")
            del root

    def IsEventTypeSupported(self, provider: "AnalysisWorkbenchComponentProvider", eventType: "TIME_EVENT_TYPE"):
        if provider.time_instants.factory.is_type_supported(eventType):
            # Create an Event with the supported Type
            event: "ITimeToolInstant" = provider.time_instants.factory.create("MyEvent", String.Empty, eventType)

    # endregion

    # region EventContains
    def test_EventContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventContains(provider)

        finally:
            del root

    def EventContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_instants.contains("EventName"):
            Console.WriteLine('The event "{0}" already exists!', "EventName")

    # endregion

    # region EventRemove
    def test_EventRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_instants.contains("EventName")))
        event: "ITimeToolInstant" = provider.time_instants.factory.create(
            "EventName", String.Empty, TIME_EVENT_TYPE.EPOCH
        )
        try:
            self.EventRemove(provider)

        finally:
            del root

    def EventRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_instants.contains("EventName"):
            provider.time_instants.remove("EventName")

    # endregion

    # region IsEventArrayTypeSupported
    def test_IsEventArrayTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_arrays.contains("MyEventArray")))
        try:
            self.IsEventArrayTypeSupported(provider, EVENT_ARRAY_TYPE.CONDITION_CROSSINGS)

        finally:
            provider.time_arrays.remove("MyEventArray")
            del root

    def IsEventArrayTypeSupported(
        self, provider: "AnalysisWorkbenchComponentProvider", eventArrayType: "EVENT_ARRAY_TYPE"
    ):
        if provider.time_arrays.factory.is_type_supported(eventArrayType):
            # Create an EventArray with the supported Type
            eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create(
                "MyEventArray", String.Empty, eventArrayType
            )

    # endregion

    # region EventArrayContains
    def test_EventArrayContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventArrayContains(provider)

        finally:
            del root

    def EventArrayContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_arrays.contains("EventArrayName"):
            Console.WriteLine('The event array "{0}" already exists!', "EventArrayName")

    # endregion

    # region EventArrayRemove
    def test_EventArrayRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_arrays.contains("EventArrayName")))
        eventArray: "ITimeToolTimeArray" = provider.time_arrays.factory.create(
            "EventArrayName", String.Empty, EVENT_ARRAY_TYPE.CONDITION_CROSSINGS
        )
        try:
            self.EventArrayRemove(provider)

        finally:
            del root

    def EventArrayRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_arrays.contains("EventArrayName"):
            provider.time_arrays.remove("EventArrayName")

    # endregion

    # region IsEventIntervalTypeSupported
    def test_IsEventIntervalTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_intervals.contains("MyEventInterval")))
        try:
            self.IsEventIntervalTypeSupported(provider, EVENT_INTERVAL_TYPE.FIXED)

        finally:
            provider.time_intervals.remove("MyEventInterval")
            del root

    def IsEventIntervalTypeSupported(
        self, provider: "AnalysisWorkbenchComponentProvider", eventIntervalType: "EVENT_INTERVAL_TYPE"
    ):
        if provider.time_intervals.factory.is_type_supported(eventIntervalType):
            # Create an EventInterval with the supported Type
            eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create(
                "MyEventInterval", String.Empty, eventIntervalType
            )

    # endregion

    # region EventIntervalContains
    def test_EventIntervalContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventIntervalContains(provider)

        finally:
            del root

    def EventIntervalContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_intervals.contains("EventIntervalName"):
            Console.WriteLine('The event interval "{0}" already exists!', "EventIntervalName")

    # endregion

    # region EventIntervalRemove
    def test_EventIntervalRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_intervals.contains("EventIntervalName")))
        eventInterval: "ITimeToolTimeInterval" = provider.time_intervals.factory.create(
            "EventIntervalName", String.Empty, EVENT_INTERVAL_TYPE.FIXED
        )
        try:
            self.EventIntervalRemove(provider)

        finally:
            del root

    def EventIntervalRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_intervals.contains("EventIntervalName"):
            provider.time_intervals.remove("EventIntervalName")

    # endregion

    # region IsEventIntervalCollectionTypeSupported
    def test_IsEventIntervalCollectionTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_interval_collections.contains("MyEventIntervalCollection")))
        try:
            self.IsEventIntervalCollectionTypeSupported(provider, EVENT_INTERVAL_COLLECTION_TYPE.LIGHTING)

        finally:
            provider.time_interval_collections.remove("MyEventIntervalCollection")
            del root

    def IsEventIntervalCollectionTypeSupported(
        self,
        provider: "AnalysisWorkbenchComponentProvider",
        eventIntervalCollectionType: "EVENT_INTERVAL_COLLECTION_TYPE",
    ):
        if provider.time_interval_collections.factory.is_type_supported(eventIntervalCollectionType):
            # Create an EventIntervalCollection with the supported Type
            eventIntervalCollection: "ITimeToolTimeIntervalCollection" = (
                provider.time_interval_collections.factory.create(
                    "MyEventIntervalCollection", String.Empty, eventIntervalCollectionType
                )
            )

    # endregion

    # region EventIntervalCollectionContains
    def test_EventIntervalCollectionContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventIntervalCollectionContains(provider)

        finally:
            del root

    def EventIntervalCollectionContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_interval_collections.contains("EventIntervalCollectionName"):
            Console.WriteLine('The event interval collection "{0}" already exists!', "EventIntervalCollectionName")

    # endregion

    # region EventIntervalCollectionRemove
    def test_EventIntervalCollectionRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_interval_collections.contains("EventIntervalCollectionName")))
        eventIntervalCollection: "ITimeToolTimeIntervalCollection" = provider.time_interval_collections.factory.create(
            "EventIntervalCollectionName", String.Empty, EVENT_INTERVAL_COLLECTION_TYPE.LIGHTING
        )
        try:
            self.EventIntervalCollectionRemove(provider)

        finally:
            del root

    def EventIntervalCollectionRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_interval_collections.contains("EventIntervalCollectionName"):
            provider.time_interval_collections.remove("EventIntervalCollectionName")

    # endregion

    # region IsEventIntervalListTypeSupported
    def test_IsEventIntervalListTypeSupported(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_interval_lists.contains("MyEventIntervalList")))
        try:
            self.IsEventIntervalListTypeSupported(provider, EVENT_INTERVAL_LIST_TYPE.CONDITION)

        finally:
            provider.time_interval_lists.remove("MyEventIntervalList")
            del root

    def IsEventIntervalListTypeSupported(
        self, provider: "AnalysisWorkbenchComponentProvider", eventIntervalListType: "EVENT_INTERVAL_LIST_TYPE"
    ):
        if provider.time_interval_lists.factory.is_type_supported(eventIntervalListType):
            # Create an EventIntervalList with the supported Type
            eventIntervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create(
                "MyEventIntervalList", String.Empty, eventIntervalListType
            )

    # endregion

    # region EventIntervalListContains
    def test_EventIntervalListContains(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventIntervalListContains(provider)

        finally:
            del root

    def EventIntervalListContains(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_interval_lists.contains("EventIntervalListName"):
            Console.WriteLine('The event interval list "{0}" already exists!', "EventIntervalListName")

    # endregion

    # region EventIntervalListRemove
    def test_EventIntervalListRemove(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.time_interval_lists.contains("EventIntervalListName")))
        eventIntervalList: "ITimeToolTimeIntervalList" = provider.time_interval_lists.factory.create(
            "EventIntervalListName", String.Empty, EVENT_INTERVAL_LIST_TYPE.CONDITION
        )
        try:
            self.EventIntervalListRemove(provider)

        finally:
            del root

    def EventIntervalListRemove(self, provider: "AnalysisWorkbenchComponentProvider"):
        if provider.time_interval_lists.contains("EventIntervalListName"):
            provider.time_interval_lists.remove("EventIntervalListName")

    # endregion

    # region Angle.FindAngle
    def test_FindAngle(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.angles.factory.create(
            "AngleName", String.Empty, ANGLE_TYPE.BETWEEN_VECTORS
        )
        try:
            self.FindAngle(angle)

        finally:
            provider.angles.remove("AngleName")
            del root

    def FindAngle(self, angle: "IVectorGeometryToolAngle"):
        result: "AnalysisWorkbenchAngleFindAngleResult" = angle.find_angle(0)
        if result.is_valid:
            Console.WriteLine("Angle: {0}", result.angle)

    # endregion

    # region Angle.FindAngleAndRate
    def test_FindAngleAndRate(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.angles.factory.create(
            "AngleName", String.Empty, ANGLE_TYPE.BETWEEN_VECTORS
        )
        try:
            self.FindAngleAndRate(angle)

        finally:
            provider.angles.remove("AngleName")
            del root

    def FindAngleAndRate(self, angle: "IVectorGeometryToolAngle"):
        result: "AnalysisWorkbenchAngleFindAngleWithRateResult" = angle.find_angle_with_rate(0)
        if result.is_valid:
            Console.WriteLine("Angle: {0}, Rate: {1}", result.angle, result.angle_rate)

    # endregion

    # region Axes.FindInAxes
    def test_FindAxesInEarthFixed(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        axes: "IVectorGeometryToolAxes" = provider.axes.factory.create("AxesName", String.Empty, AXES_TYPE.FIXED)
        try:
            self.FindAxesInEarthFixed(provider, axes)

        finally:
            provider.axes.remove("AxesName")
            del root

    def FindAxesInEarthFixed(self, provider: "AnalysisWorkbenchComponentProvider", axes: "IVectorGeometryToolAxes"):
        result: "AnalysisWorkbenchAxesFindInAxesResult" = axes.find_in_axes(0, provider.well_known_axes.earth.fixed)
        if result.is_valid:
            angles: "IOrientationEulerAngles" = IOrientationEulerAngles(
                result.orientation.convert_to(ORIENTATION_TYPE.EULER_ANGLES)
            )
            Console.WriteLine(
                "Euler Angles [A,B,C,SEQ] => [{1}, {1}, {2}, {3}]", angles.a, angles.b, angles.c, angles.sequence
            )

    # endregion

    # region Axes.Transform
    def test_AxesTransformEarthFixed(self):
        sat: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        self.AxesTransformEarthFixed(sat)

    def AxesTransformEarthFixed(self, sat: "IStkObject"):
        # Get the satellite's ICRF cartesian position at 180 EpSec using the data provider interface
        numEpSec: int = 180
        dpGroup: "DataProviderGroup" = clr.CastAs(sat.data_providers["Cartesian Position"], DataProviderGroup)
        elements = ["x", "y", "z"]
        dp: "DataProviderTimeVarying" = clr.CastAs(dpGroup.group["ICRF"], DataProviderTimeVarying)
        dpResult: "DataProviderResult" = dp.execute_elements(numEpSec, numEpSec, 60, elements)
        xICRF: float = float(dpResult.data_sets[0].get_values()[0])
        yICRF: float = float(dpResult.data_sets[1].get_values()[0])
        zICRF: float = float(dpResult.data_sets[2].get_values()[0])

        # Create a vector using the ICRF coordinates
        axesICRF: "IVectorGeometryToolAxes" = sat.analysis_workbench_components.well_known_axes.earth.icrf
        vectorICRF: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
        vectorICRF.set(xICRF, yICRF, zICRF)

        # Use the Transform method to transform ICRF to Fixed
        axesFixed: "IVectorGeometryToolAxes" = sat.analysis_workbench_components.well_known_axes.earth.fixed
        result: "AnalysisWorkbenchAxesTransformResult" = axesICRF.transform(numEpSec, axesFixed, vectorICRF)

        # Get the Fixed coordinates
        xFixed: float = result.vector.x
        yFixed: float = result.vector.y
        zFixed: float = result.vector.z

    # endregion

    # region Axes.TransformWithRate
    def test_AxesTransformWithRateEarthFixed(self):
        sat: "IStkObject" = TestBase.Application.current_scenario.children["Satellite1"]
        self.AxesTransformWithRateEarthFixed(sat)

    def AxesTransformWithRateEarthFixed(self, sat: "IStkObject"):
        numEpSec: int = 180

        # Get the satellite's ICRF cartesian position at 180 EpSec using the data provider interface
        dpGroup: "DataProviderGroup" = clr.CastAs(sat.data_providers["Cartesian Position"], DataProviderGroup)
        elements = ["x", "y", "z"]
        dp: "DataProviderTimeVarying" = clr.CastAs(dpGroup.group["ICRF"], DataProviderTimeVarying)
        dpResult: "DataProviderResult" = dp.execute_elements(numEpSec, numEpSec, 60, elements)
        xICRF: float = float(dpResult.data_sets[0].get_values()[0])
        yICRF: float = float(dpResult.data_sets[1].get_values()[0])
        zICRF: float = float(dpResult.data_sets[2].get_values()[0])

        # Get the satellite's ICRF cartesian velocity at 180 EpSec using the data provider interface
        dpGroup = clr.CastAs(sat.data_providers["Cartesian Velocity"], DataProviderGroup)
        dp = clr.CastAs(dpGroup.group["ICRF"], DataProviderTimeVarying)
        dpResult = dp.execute_elements(numEpSec, numEpSec, 60, elements)
        xvelICRF: float = float(dpResult.data_sets[0].get_values()[0])
        yvelICRF: float = float(dpResult.data_sets[1].get_values()[0])
        zvelICRF: float = float(dpResult.data_sets[2].get_values()[0])

        # Create a position vector using the ICRF coordinates
        axesICRF: "IVectorGeometryToolAxes" = sat.analysis_workbench_components.well_known_axes.earth.icrf
        vectorICRF: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
        vectorICRF.set(xICRF, yICRF, zICRF)

        # Create a velocity vector using the ICRF coordinates
        vectorvelICRF: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
        vectorvelICRF.set(xvelICRF, yvelICRF, zvelICRF)

        # Use the TransformWithRate method to transform ICRF to Fixed
        axesFixed: "IVectorGeometryToolAxes" = sat.analysis_workbench_components.well_known_axes.earth.fixed
        result: "AnalysisWorkbenchAxesTransformWithRateResult" = axesICRF.transform_with_rate(
            numEpSec, axesFixed, vectorICRF, vectorvelICRF
        )

        # Get the Fixed position and velocity coordinates
        xFixed: float = result.vector.x
        yFixed: float = result.vector.y
        zFixed: float = result.vector.z
        xvelFixed: float = result.velocity.x
        yvelFixed: float = result.velocity.y
        zvelFixed: float = result.velocity.z

    # endregion

    # region Point.LocateInEarthFixedSystem
    def test_PointLocateInEarthFixedSystem(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "PointName", String.Empty, POINT_TYPE.FIXED_IN_SYSTEM
        )
        try:
            self.PointLocateInEarthFixedSystem(provider, point)

        finally:
            provider.points.remove("PointName")
            del root

    def PointLocateInEarthFixedSystem(
        self, provider: "AnalysisWorkbenchComponentProvider", point: "IVectorGeometryToolPoint"
    ):
        result: "AnalysisWorkbenchPointLocateInSystemResult" = point.locate_in_system(
            0, provider.well_known_systems.earth.fixed
        )
        if result.is_valid:
            Console.WriteLine(
                "The position of the point in Earth's Fixed reference frame: {0},{1},{2}",
                result.position.x,
                result.position.y,
                result.position.z,
            )

    # endregion

    # region Vector.VectorFindInEarthFixedAxes
    def test_VectorFindInEarthFixedAxes(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("VectorName")))
        vector: "IVectorGeometryToolVector" = provider.vectors.factory.create(
            "PointName", String.Empty, VECTOR_TYPE.DISPLACEMENT
        )
        try:
            self.VectorFindInEarthFixedAxes(provider, vector)

        finally:
            provider.points.remove("PointName")
            del root

    def VectorFindInEarthFixedAxes(
        self, provider: "AnalysisWorkbenchComponentProvider", vector: "IVectorGeometryToolVector"
    ):
        result: "AnalysisWorkbenchVectorFindInAxesResult" = vector.find_in_axes(0, provider.well_known_axes.earth.fixed)
        if result.is_valid:
            Console.WriteLine(
                "Vector in the Earth's Fixed axes (x,y,z) => {0},{1},{2}",
                result.vector.x,
                result.vector.y,
                result.vector.z,
            )

    # endregion

    # region Axes.AnonymousFixed
    def test_AxesAnonymousFixed(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        try:
            vector: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
            self.AxesAnonymousFixed(provider)

        finally:
            del root

    def AxesAnonymousFixed(self, provider: "AnalysisWorkbenchComponentProvider"):
        ecfAxes: "IVectorGeometryToolAxes" = provider.well_known_axes.earth.fixed
        axesFixed: "VectorGeometryToolAxesFixed" = provider.axes.common_tasks.create_fixed(ecfAxes)

    # endregion

    # region Axes.CreateTopocentricAxesEulerAngles
    def test_AxesCreateTopocentricAxesEulerAngles(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        facility: "Facility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], Facility)
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            self.AxesCreateTopocentricAxesEulerAngles(provider, facility)

        finally:
            del root

    def AxesCreateTopocentricAxesEulerAngles(
        self, provider: "AnalysisWorkbenchComponentProvider", facility: "Facility"
    ):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0

        (lat, lon, alt) = facility.position.query_planetodetic()
        origin: "VectorGeometryToolPointFixedInSystem" = (
            provider.points.common_tasks.create_fixed_in_system_cartographic(provider.systems["Fixed"], lat, lon, alt)
        )
        eastNorthUp: "VectorGeometryToolAxesFixed" = provider.axes.common_tasks.create_topocentric_axes_euler_angles(
            IVectorGeometryToolPoint(origin), EULER_ORIENTATION_SEQUENCE_TYPE.SEQUENCE_321, 90.0, 0.0, 0.0
        )

    # endregion

    # region Axes.CreateTopocentricAxesQuaternion
    def test_AxesCreateTopocentricAxesQuaternion(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        facility: "Facility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], Facility)
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            self.AxesCreateTopocentricAxesQuaternion(provider, facility)

        finally:
            del root

    def AxesCreateTopocentricAxesQuaternion(self, provider: "AnalysisWorkbenchComponentProvider", facility: "Facility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0

        (lat, lon, alt) = facility.position.query_planetodetic()
        origin: "VectorGeometryToolPointFixedInSystem" = (
            provider.points.common_tasks.create_fixed_in_system_cartographic(provider.systems["Fixed"], lat, lon, alt)
        )
        eastNorthUp: "VectorGeometryToolAxesFixed" = provider.axes.common_tasks.create_topocentric_axes_quaternion(
            IVectorGeometryToolPoint(origin), 0.0, 0.0, 0.0, 1.0
        )

    # endregion

    # region Systems.CreateAssembled
    def test_SystemsCreateAssembled(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        facility: "Facility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], Facility)
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            self.SystemsCreateAssembled(provider, facility)

        finally:
            del root

    def SystemsCreateAssembled(self, provider: "AnalysisWorkbenchComponentProvider", facility: "Facility"):
        systemAssembled: "VectorGeometryToolSystemAssembled" = provider.systems.common_tasks.create_assembled(
            (IStkObject(facility)).analysis_workbench_components.points["Center"], provider.axes["Fixed"]
        )

    # endregion

    # region Systems.CreateEastNorthUpCartographic
    def test_SystemsCreateEastNorthUpCartographic(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        facility: "Facility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], Facility)
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.current_scenario.children[
            "Facility1"
        ].analysis_workbench_components
        try:
            self.SystemsCreateEastNorthUpCartographic(provider, facility)

        finally:
            del root

    def SystemsCreateEastNorthUpCartographic(
        self, provider: "AnalysisWorkbenchComponentProvider", facility: "Facility"
    ):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0
        (lat, lon, alt) = facility.position.query_planetodetic()
        systemAssembled: "VectorGeometryToolSystemAssembled" = (
            provider.systems.common_tasks.create_east_north_up_cartographic(lat, lon, alt)
        )

    # endregion

    # region Point.CreateFixedInSystemCartographic
    def test_PointCreateFixedInSystemCartographic(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        facility: "Facility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], Facility)
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            self.PointCreateFixedInSystemCartographic(provider, facility)

        finally:
            del root

    def PointCreateFixedInSystemCartographic(
        self, provider: "AnalysisWorkbenchComponentProvider", facility: "Facility"
    ):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0
        (lat, lon, alt) = facility.position.query_planetodetic()
        origin: "VectorGeometryToolPointFixedInSystem" = (
            provider.points.common_tasks.create_fixed_in_system_cartographic(provider.systems["Fixed"], lat, lon, alt)
        )

    # endregion

    # region Point.CreateFixedInSystemCartesian
    def test_PointCreateFixedInSystemCartesian(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        facility: "Facility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], Facility)
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            self.PointCreateFixedInSystemCartesian(provider, facility)

        finally:
            del root

    def PointCreateFixedInSystemCartesian(self, provider: "AnalysisWorkbenchComponentProvider", facility: "Facility"):
        X: float = 0
        Y: float = 0
        Z: float = 0

        (X, Y, Z) = facility.position.query_cartesian()
        origin: "VectorGeometryToolPointFixedInSystem" = provider.points.common_tasks.create_fixed_in_system_cartesian(
            provider.systems["Fixed"], X, Y, Z
        )

    # endregion

    # region Duplicate
    def test_Duplicate(self):
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            provider.points.remove("OriginalPoint")
            self.Duplicate(provider)

        finally:
            pass

    def Duplicate(self, provider: "AnalysisWorkbenchComponentProvider"):
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "OriginalPoint", "description", POINT_TYPE.AT_TIME_INSTANT
        )
        duplicate: "IAnalysisWorkbenchComponent" = (IAnalysisWorkbenchComponent(point)).duplicate(
            "DuplicatePoint", "description"
        )

    # endregion

    # region AnonymousDuplicate
    def test_AnonymousDuplicate(self):
        provider: "AnalysisWorkbenchComponentProvider" = TestBase.Application.central_bodies[
            "Earth"
        ].analysis_workbench_components
        try:
            provider.points.remove("OriginalPoint")
            self.AnonymousDuplicate(provider)

        finally:
            pass

    def AnonymousDuplicate(self, provider: "AnalysisWorkbenchComponentProvider"):
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "OriginalPoint", "description", POINT_TYPE.AT_TIME_INSTANT
        )
        anonymousDuplicate: "IAnalysisWorkbenchComponent" = (IAnalysisWorkbenchComponent(point)).anonymous_duplicate()

    # endregion

    # region GetEmbeddedComponent
    def test_GetEmbeddedComponent(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "mySystem", String.Empty, SYSTEM_TYPE.ASSEMBLED
        )
        try:
            self.GetEmbeddedComponent(IAnalysisWorkbenchComponent(system))

        finally:
            provider.systems.remove("mySystem")
            del root

    def GetEmbeddedComponent(self, crdn: "IAnalysisWorkbenchComponent"):
        if crdn.embedded_components.contains("Origin"):
            embeddedComponent: "IAnalysisWorkbenchComponent" = crdn.embedded_components["Origin"]

    # endregion

    # region EnumerateThroughEmbeddedComponents
    def test_EnumerateThroughEmbeddedComponents(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "mySystem", String.Empty, SYSTEM_TYPE.ASSEMBLED
        )
        try:
            self.EnumerateThroughEmbeddedComponents(IAnalysisWorkbenchComponent(system))

        finally:
            provider.systems.remove("mySystem")
            del root

    def EnumerateThroughEmbeddedComponents(self, crdn: "IAnalysisWorkbenchComponent"):
        embeddedComponent: "IAnalysisWorkbenchComponent"
        for embeddedComponent in crdn.embedded_components:
            Console.WriteLine("Name: {0}, kind: {1}", embeddedComponent.name, embeddedComponent.component_type)

    # endregion

    # region IterateThroughEmbeddedComponents
    def test_IterateThroughEmbeddedComponents(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "mySystem", String.Empty, SYSTEM_TYPE.ASSEMBLED
        )
        try:
            self.IterateThroughEmbeddedComponents(IAnalysisWorkbenchComponent(system))

        finally:
            provider.systems.remove("mySystem")
            del root

    def IterateThroughEmbeddedComponents(self, crdn: "IAnalysisWorkbenchComponent"):
        i: int = 0
        while i < crdn.embedded_components.count:
            embeddedComponent: "IAnalysisWorkbenchComponent" = crdn.embedded_components[i]
            Console.WriteLine("Name: {0}, kind: {1}", embeddedComponent.name, embeddedComponent.component_type)

            i += 1

    # endregion

    # region AngleHasCyclicDependency
    def test_AngleHasCyclicDependency(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        angleRate: "VectorGeometryToolVectorAngleRate" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, VECTOR_TYPE.ANGLE_RATE),
            VectorGeometryToolVectorAngleRate,
        )
        angle: "IVectorGeometryToolAngle" = provider.angles["VelocityAzimuth"]
        try:
            self.AngleHasCyclicDependency(angleRate.angle, angle)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def AngleHasCyclicDependency(
        self, angleRefTo: "VectorGeometryToolAngleReference", angle: "IVectorGeometryToolAngle"
    ):
        if angleRefTo.has_cyclic_dependency(angle):
            Console.WriteLine(
                "The angle {0} has a cyclic dependency on angle {1}.",
                (IAnalysisWorkbenchComponent(angleRefTo.get_angle())).name,
                (IAnalysisWorkbenchComponent(angle)).name,
            )

    # endregion

    # region AxesHasCyclicDependency
    def test_AxesHasCyclicDependency(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        angVel: "VectorGeometryToolVectorAngularVelocity" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, VECTOR_TYPE.ANGULAR_VELOCITY),
            VectorGeometryToolVectorAngularVelocity,
        )
        axes: "IVectorGeometryToolAxes" = provider.axes["Body"]
        try:
            self.AxesHasCyclicDependency(angVel.axes, axes)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def AxesHasCyclicDependency(self, axesRefTo: "VectorGeometryToolAxesReference", axes: "IVectorGeometryToolAxes"):
        if axesRefTo.has_cyclic_dependency(axes):
            Console.WriteLine(
                "The axes {0} has a cyclic dependency on axes {1}.",
                (IAnalysisWorkbenchComponent(axesRefTo.get_axes())).name,
                (IAnalysisWorkbenchComponent(axes)).name,
            )

    # endregion

    # region PlaneHasCyclicDependency
    def test_PlaneHasCyclicDependency(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        twoPlane: "VectorGeometryToolVectorTwoPlanesIntersection" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, VECTOR_TYPE.TWO_PLANES_INTERSECTION),
            VectorGeometryToolVectorTwoPlanesIntersection,
        )
        plane: "IVectorGeometryToolPlane" = provider.planes["BodyXY"]
        try:
            self.PlaneHasCyclicDependency(twoPlane.plane_a, plane)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def PlaneHasCyclicDependency(
        self, planeRefTo: "VectorGeometryToolPlaneReference", plane: "IVectorGeometryToolPlane"
    ):
        if planeRefTo.has_cyclic_dependency(plane):
            Console.WriteLine(
                "The plane {0} has a cyclic dependency on plane {1}.",
                (IAnalysisWorkbenchComponent(planeRefTo.get_plane())).name,
                (IAnalysisWorkbenchComponent(plane)).name,
            )

    # endregion

    # region PointHasCyclicDependency
    def test_PointHasCyclicDependency(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        apoapsis: "VectorGeometryToolVectorApoapsis" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, VECTOR_TYPE.APOAPSIS),
            VectorGeometryToolVectorApoapsis,
        )
        point: "IVectorGeometryToolPoint" = provider.points["Center"]
        try:
            self.PointHasCyclicDependency(apoapsis.reference_point, point)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def PointHasCyclicDependency(
        self, pointRefTo: "VectorGeometryToolPointReference", point: "IVectorGeometryToolPoint"
    ):
        if pointRefTo.has_cyclic_dependency(point):
            Console.WriteLine(
                "The point {0} has a cyclic dependency on point {1}.",
                (IAnalysisWorkbenchComponent(pointRefTo.get_point())).name,
                (IAnalysisWorkbenchComponent(point)).name,
            )

    # endregion

    # region SystemHasCyclicDependency
    def test_SystemHasCyclicDependency(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        displacement: "VectorGeometryToolVectorDisplacement" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, VECTOR_TYPE.DISPLACEMENT),
            VectorGeometryToolVectorDisplacement,
        )
        displacement.apparent = True
        system: "IVectorGeometryToolSystem" = provider.systems["Body"]
        try:
            self.SystemHasCyclicDependency(displacement.reference_system, system)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def SystemHasCyclicDependency(
        self, systemRefTo: "VectorGeometryToolSystemReference", system: "IVectorGeometryToolSystem"
    ):
        if systemRefTo.has_cyclic_dependency(system):
            Console.WriteLine(
                "The system {0} has a cyclic dependency on system {1}.",
                (IAnalysisWorkbenchComponent(systemRefTo.get_system())).name,
                (IAnalysisWorkbenchComponent(system)).name,
            )

    # endregion

    # region VectorHasCyclicDependency
    def test_VectorHasCyclicDependency(self):
        root: "AnalysisWorkbenchRoot" = TestBase.Application.analysis_workbench_components_root
        provider: "AnalysisWorkbenchComponentProvider" = root.get_provider("Satellite/Satellite1")
        reflection: "VectorGeometryToolVectorReflection" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, VECTOR_TYPE.REFLECTION),
            VectorGeometryToolVectorReflection,
        )
        vector: "IVectorGeometryToolVector" = provider.vectors["Earth"]
        try:
            self.VectorHasCyclicDependency(reflection.normal_vector, vector)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def VectorHasCyclicDependency(
        self, vectorRefTo: "VectorGeometryToolVectorReference", vector: "IVectorGeometryToolVector"
    ):
        if vectorRefTo.has_cyclic_dependency(vector):
            Console.WriteLine(
                "The vector {0} has a cyclic dependency on vector {1}.",
                (IAnalysisWorkbenchComponent(vectorRefTo.get_vector())).name,
                (IAnalysisWorkbenchComponent(vector)).name,
            )

    # endregion
