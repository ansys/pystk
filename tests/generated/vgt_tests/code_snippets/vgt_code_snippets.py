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
        sat: "ISatellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(AgESTKObjectType.eSatellite, "Satellite1"), ISatellite
        )
        sat.set_propagator_type(AgEVePropagatorType.ePropagatorTwoBody)
        (clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)).propagate()

        fac: "IFacility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(AgESTKObjectType.eFacility, "Facility1"), IFacility
        )

        scenario: "IScenario" = clr.Convert(TestBase.Application.current_scenario, IScenario)
        scenario.epoch = "1 Jan 2012 12:00:00.000"

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        TestBase.Application.unit_preferences.set_current_unit("DateFormat", "EpSec")
        TestBase.Application.unit_preferences.set_current_unit("TimeUnit", "sec")

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region rootGetVGTProvider
    def test_rootGetVGTProvider(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        try:
            self.rootGetVGTProvider(root, "Satellite/Satellite1")

        finally:
            del root

    def rootGetVGTProvider(self, root: "IAnalysisWorkbenchRoot", path: str):
        # Returns a provider associated with the specified
        # instance of an STK Object or a Central Body.
        provider: "IAnalysisWorkbenchProvider" = root.get_provider(path)

    # endregion

    # region rootGetVGTTemplateProvider
    def test_rootGetVGTTemplateProvider(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        try:
            self.rootGetVGTTemplateProvider(root, "Satellite")

        finally:
            del root

    def rootGetVGTTemplateProvider(self, root: "IAnalysisWorkbenchRoot", className: str):
        # Returns a VGT provider associated with the specified
        # STK object class (i.e., Satellite, Facility, etc.) or
        # a Central Body.
        provider: "IAnalysisWorkbenchProvider" = root.get_template_provider(className)

    # endregion

    # region EnumerateThroughVectors
    def test_EnumerateThroughVectors(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughVectors(provider)

        finally:
            del root

    def EnumerateThroughVectors(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing vectors using specified CrdnProvider.
        vector: "IVectorGeometryToolVector"
        # Enumerate the existing vectors using specified CrdnProvider.
        for vector in provider.vectors:
            # All vectors implement IAgCrdn interface which provides
            # information about the vector instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(vector, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, vector.type)

    # endregion

    # region EnumerateThroughPoints
    def test_EnumerateThroughPoints(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughPoints(provider)

        finally:
            del root

    def EnumerateThroughPoints(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing points using specified CrdnProvider.
        point: "IVectorGeometryToolPoint"
        # Enumerate the existing points using specified CrdnProvider.
        for point in provider.points:
            # All points implement IAgCrdn interface which provides
            # information about the point instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(point, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, point.type)

    # endregion

    # region EnumerateThroughAngles
    def test_EnumerateThroughAngles(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughAngles(provider)

        finally:
            del root

    def EnumerateThroughAngles(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing angles using specified CrdnProvider.
        angle: "IVectorGeometryToolAngle"
        # Enumerate the existing angles using specified CrdnProvider.
        for angle in provider.angles:
            # All angles implement IAgCrdn interface which provides
            # information about the angle instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(angle, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, angle.type)

    # endregion

    # region EnumerateThroughAxes
    def test_EnumerateThroughAxes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughAxes(provider)

        finally:
            del root

    def EnumerateThroughAxes(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Axes using specified CrdnProvider.
        axes: "IVectorGeometryToolAxes"
        # Enumerate the existing Axes using specified CrdnProvider.
        for axes in provider.axes:
            # All axes implement IAgCrdn interface which provides
            # information about the axes instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(axes, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, axes.type)

    # endregion

    # region EnumerateThroughPlanes
    def test_EnumerateThroughPlanes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughPlanes(provider)

        finally:
            del root

    def EnumerateThroughPlanes(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Planes using specified CrdnProvider.
        plane: "IVectorGeometryToolPlane"
        # Enumerate the existing Planes using specified CrdnProvider.
        for plane in provider.planes:
            # All planes implement IAgCrdn interface which provides
            # information about the plane instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(plane, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, plane.type)

    # endregion

    # region EnumerateThroughSystems
    def test_EnumerateThroughSystems(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughSystems(provider)

        finally:
            del root

    def EnumerateThroughSystems(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Systems using specified CrdnProvider.
        system: "IVectorGeometryToolSystem"
        # Enumerate the existing Systems using specified CrdnProvider.
        for system in provider.systems:
            # All systems implement IAgCrdn interface which provides
            # information about the system instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(system, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, system.type)

    # endregion

    # region EnumerateThroughParameterSets
    def test_EnumerateThroughParameterSets(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughParameterSets(provider)

        finally:
            del root

    def EnumerateThroughParameterSets(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing ParameterSets using specified CrdnProvider.
        parameterSet: "ICalculationToolParameterSet"
        # Enumerate the existing ParameterSets using specified CrdnProvider.
        for parameterSet in provider.parameter_sets:
            # All parameter sets implement IAgCrdn interface which provides
            # information about the parameter set instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(parameterSet, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, parameterSet.type)

    # endregion

    # region EnumerateThroughCalcScalars
    def test_EnumerateThroughCalcScalars(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughCalcScalars(provider)

        finally:
            del root

    def EnumerateThroughCalcScalars(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing CalcScalars using specified CrdnProvider.
        calcScalar: "ICalculationToolScalar"
        # Enumerate the existing CalcScalars using specified CrdnProvider.
        for calcScalar in provider.calc_scalars:
            # All calc scalars implement IAgCrdn interface which provides
            # information about the calc scalar instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(calcScalar, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, calcScalar.type)

    # endregion

    # region EnumerateThroughConditions
    def test_EnumerateThroughConditions(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughConditions(provider)

        finally:
            del root

    def EnumerateThroughConditions(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Conditions using specified CrdnProvider.
        condition: "ICalculationToolCondition"
        # Enumerate the existing Conditions using specified CrdnProvider.
        for condition in provider.conditions:
            # All conditions implement IAgCrdn interface which provides
            # information about the condition instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(condition, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, condition.type)

    # endregion

    # region EnumerateThroughEvents
    def test_EnumerateThroughEvents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEvents(provider)

        finally:
            del root

    def EnumerateThroughEvents(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Events using specified CrdnProvider.
        event: "ITimeToolEvent"
        # Enumerate the existing Events using specified CrdnProvider.
        for event in provider.events:
            # All events implement IAgCrdn interface which provides
            # information about the event instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(event, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, event.type)

    # endregion

    # region EnumerateThroughEventArrays
    def test_EnumerateThroughEventArrays(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventArrays(provider)

        finally:
            del root

    def EnumerateThroughEventArrays(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventArrays using specified CrdnProvider.
        eventArray: "ITimeToolEventArray"
        # Enumerate the existing EventArrays using specified CrdnProvider.
        for eventArray in provider.event_arrays:
            # All event arrays implement IAgCrdn interface which provides
            # information about the event array instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventArray, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventArray.type)

    # endregion

    # region EnumerateThroughEventIntervals
    def test_EnumerateThroughEventIntervals(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervals(provider)

        finally:
            del root

    def EnumerateThroughEventIntervals(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventIntervals using specified CrdnProvider.
        eventInterval: "ITimeToolEventInterval"
        # Enumerate the existing EventIntervals using specified CrdnProvider.
        for eventInterval in provider.event_intervals:
            # All event intervals implement IAgCrdn interface which provides
            # information about the event interval instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventInterval, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventInterval.type)

    # endregion

    # region EnumerateThroughEventIntervalCollections
    def test_EnumerateThroughEventIntervalCollections(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervalCollections(provider)

        finally:
            del root

    def EnumerateThroughEventIntervalCollections(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventIntervalCollections using specified CrdnProvider.
        eventIntervalCollection: "ITimeToolEventIntervalCollection"
        # Enumerate the existing EventIntervalCollections using specified CrdnProvider.
        for eventIntervalCollection in provider.event_interval_collections:
            # All event interval collections implement IAgCrdn interface which provides
            # information about the event interval collection instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventIntervalCollection, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalCollection.type)

    # endregion

    # region EnumerateThroughEventIntervalLists
    def test_EnumerateThroughEventIntervalLists(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervalLists(provider)

        finally:
            del root

    def EnumerateThroughEventIntervalLists(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventIntervalLists using specified CrdnProvider.
        eventIntervalList: "ITimeToolEventIntervalList"
        # Enumerate the existing EventIntervalLists using specified CrdnProvider.
        for eventIntervalList in provider.event_interval_lists:
            # All event interval lists implement IAgCrdn interface which provides
            # information about the event interval list instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventIntervalList, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalList.type)

    # endregion

    # region IterateThroughVectors
    def test_IterateThroughVectors(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughVectors(provider)

        finally:
            del root

    def IterateThroughVectors(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.vectors.count:
            vector: "IVectorGeometryToolVector" = provider.vectors[i]
            # All vectors implement IAgCrdn interface which provides
            # information about the vector instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(vector, IAnalysisWorkbenchComponent)
            # Print the vector name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, vector.type)

            i += 1

    # endregion

    # region IterateThroughPoint
    def test_IterateThroughPoints(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughPoints(provider)

        finally:
            del root

    def IterateThroughPoints(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.points.count:
            point: "IVectorGeometryToolPoint" = provider.points[i]
            # All points implement IAgCrdn interface which provides
            # information about the point instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.points[i], IAnalysisWorkbenchComponent)
            # Print the point name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, point.type)

            i += 1

    # endregion

    # region IterateThroughAngles
    def test_IterateThroughAngles(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughAngles(provider)

        finally:
            del root

    def IterateThroughAngles(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.angles.count:
            angle: "IVectorGeometryToolAngle" = provider.angles[i]
            # All angles implement IAgCrdn interface which provides
            # information about the angle instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.angles[i], IAnalysisWorkbenchComponent)
            # Print the angle name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, angle.type)

            i += 1

    # endregion

    # region IterateThroughAxes
    def test_IterateThroughAxes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughAxes(provider)

        finally:
            del root

    def IterateThroughAxes(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.axes.count:
            axes: "IVectorGeometryToolAxes" = provider.axes[i]
            # All axes implement IAgCrdn interface which provides
            # information about the axes instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.axes[i], IAnalysisWorkbenchComponent)
            # Print the axes name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, axes.type)

            i += 1

    # endregion

    # region IterateThroughPlanes
    def test_IterateThroughPlanes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughPlanes(provider)

        finally:
            del root

    def IterateThroughPlanes(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.planes.count:
            plane: "IVectorGeometryToolPlane" = provider.planes[i]
            # All planes implement IAgCrdn interface which provides
            # information about the plane's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.planes[i], IAnalysisWorkbenchComponent)
            # Print the plane's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, plane.type)

            i += 1

    # endregion

    # region IterateThroughSystems
    def test_IterateThroughSystems(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughSystems(provider)

        finally:
            del root

    def IterateThroughSystems(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.systems.count:
            crdnSystem: "IVectorGeometryToolSystem" = provider.systems[i]
            # All coordinate reference frames implement IAgCrdn interface which provides
            # information about the reference frame's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.systems[i], IAnalysisWorkbenchComponent)
            # Print the reference frame's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, crdnSystem.type)

            i += 1

    # endregion

    # region IterateThroughParameterSets
    def test_IterateThroughParameterSets(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughParameterSets(provider)

        finally:
            del root

    def IterateThroughParameterSets(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.parameter_sets.count:
            parameterSet: "ICalculationToolParameterSet" = provider.parameter_sets[i]
            # All parameter sets implement IAgCrdn interface which provides
            # information about the parameter set's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.parameter_sets[i], IAnalysisWorkbenchComponent)
            # Print the parameter set's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, parameterSet.type)

            i += 1

    # endregion

    # region IterateThroughCalcScalars
    def test_IterateThroughCalcScalars(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughCalcScalars(provider)

        finally:
            del root

    def IterateThroughCalcScalars(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.calc_scalars.count:
            calcScalar: "ICalculationToolScalar" = provider.calc_scalars[i]
            # All calc scalars implement IAgCrdn interface which provides
            # information about the calc scalar's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.calc_scalars[i], IAnalysisWorkbenchComponent)
            # Print the calc scalar's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, calcScalar.type)

            i += 1

    # endregion

    # region IterateThroughConditions
    def test_IterateThroughConditions(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughConditions(provider)

        finally:
            del root

    def IterateThroughConditions(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.conditions.count:
            condition: "ICalculationToolCondition" = provider.conditions[i]
            # All conditions implement IAgCrdn interface which provides
            # information about the condition's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.conditions[i], IAnalysisWorkbenchComponent)
            # Print the condition's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, condition.type)

            i += 1

    # endregion

    # region IterateThroughEvents
    def test_IterateThroughEvents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEvents(provider)

        finally:
            del root

    def IterateThroughEvents(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.events.count:
            event: "ITimeToolEvent" = provider.events[i]
            # All events implement IAgCrdn interface which provides
            # information about the event's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.events[i], IAnalysisWorkbenchComponent)
            # Print the event's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, event.type)

            i += 1

    # endregion

    # region IterateThroughEventArrays
    def test_IterateThroughEventArrays(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventArrays(provider)

        finally:
            del root

    def IterateThroughEventArrays(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.event_arrays.count:
            eventArray: "ITimeToolEventArray" = provider.event_arrays[i]
            # All event arrays implement IAgCrdn interface which provides
            # information about the event array's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.event_arrays[i], IAnalysisWorkbenchComponent)
            # Print the event array's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventArray.type)

            i += 1

    # endregion

    # region IterateThroughEventIntervals
    def test_IterateThroughEventIntervals(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervals(provider)

        finally:
            del root

    def IterateThroughEventIntervals(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.event_intervals.count:
            eventInterval: "ITimeToolEventInterval" = provider.event_intervals[i]
            # All event intervals implement IAgCrdn interface which provides
            # information about the event interval's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.event_intervals[i], IAnalysisWorkbenchComponent)
            # Print the event interval's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventInterval.type)

            i += 1

    # endregion

    # region IterateThroughEventIntervalCollections
    def test_IterateThroughEventIntervalCollections(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervalCollections(provider)

        finally:
            del root

    def IterateThroughEventIntervalCollections(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.event_interval_collections.count:
            eventIntervalCollection: "ITimeToolEventIntervalCollection" = provider.event_interval_collections[i]
            # All event interval collections implement IAgCrdn interface which provides
            # information about the event interval collection's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.event_interval_collections[i], IAnalysisWorkbenchComponent
            )
            # Print the event interval collection's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalCollection.type)

            i += 1

    # endregion

    # region IterateThroughEventIntervalLists
    def test_IterateThroughEventIntervalLists(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervalLists(provider)

        finally:
            del root

    def IterateThroughEventIntervalLists(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.event_interval_lists.count:
            eventIntervalList: "ITimeToolEventIntervalList" = provider.event_interval_lists[i]
            # All event interval lists implement IAgCrdn interface which provides
            # information about the event interval list's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.event_interval_lists[i], IAnalysisWorkbenchComponent
            )
            # Print the event interval list's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.name, eventIntervalList.type)

            i += 1

    # endregion

    # region CreateAngleRateVector
    def test_CreateAngleRateVector(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("myVector")))
        try:
            self.CreateAngleRateVector(provider)

        finally:
            provider.vectors.remove("myVector")
            del root

    def CreateAngleRateVector(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a vector.perpendicular to the plane in which the angle is defined.
        vector: "IVectorGeometryToolVectorAngleRate" = clr.Convert(
            provider.vectors.factory.create(
                "myVector",
                "a vector.perpendicular to the plane in which the angle is defined.",
                AgECrdnVectorType.eCrdnVectorTypeAngleRate,
            ),
            IVectorGeometryToolVectorAngleRate,
        )

    # endregion

    # region IsVectorTypeSupported
    def test_IsVectorTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("myVector")))
        try:
            self.IsVectorTypeSupported(provider, AgECrdnVectorType.eCrdnVectorTypeAngleRate)

        finally:
            provider.vectors.remove("myVector")
            del root

    def IsVectorTypeSupported(self, provider: "IAnalysisWorkbenchProvider", vectorType: "AgECrdnVectorType"):
        if provider.vectors.factory.is_type_supported(vectorType):
            # Create a custom vector.
            vector: "IVectorGeometryToolVector" = provider.vectors.factory.create("myVector", String.Empty, vectorType)

    # endregion

    # region CreateDisplacementVector
    def test_CreateDisplacementVector(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("Point1")))
        Assert.assertTrue((not provider.points.contains("Point2")))
        p: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "Point1", String.Empty, AgECrdnPointType.eCrdnPointTypeGlint
        )
        p2: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "Point2", String.Empty, AgECrdnPointType.eCrdnPointTypeGrazing
        )
        try:
            self.CreateDisplacementVector(provider, p, p2)

        finally:
            provider.points.remove("Point1")
            provider.points.remove("Point2")
            del root

    def CreateDisplacementVector(
        self,
        provider: "IAnalysisWorkbenchProvider",
        OriginPoint: "IVectorGeometryToolPoint",
        DestinationPoint: "IVectorGeometryToolPoint",
    ):
        # Create a displacement vector with two specified points
        vector: "IVectorGeometryToolVectorDisplacement" = provider.vectors.factory.create_displacement_vector(
            "VectorName", OriginPoint, DestinationPoint
        )

    # endregion

    # region CreateCrossProductVector
    def test_CreateCrossProductVector(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("Vector1")))
        Assert.assertTrue((not provider.vectors.contains("Vector2")))
        v1: "IVectorGeometryToolVector" = provider.vectors.factory.create(
            "Vector1", "", AgECrdnVectorType.eCrdnVectorTypeLineOfNodes
        )
        v2: "IVectorGeometryToolVector" = provider.vectors.factory.create(
            "Vector2", "", AgECrdnVectorType.eCrdnVectorTypeEccentricity
        )
        try:
            self.CreateCrossProductVector(provider, v1, v2)

        finally:
            provider.vectors.remove("Vector1")
            provider.vectors.remove("Vector2")
            del root

    def CreateCrossProductVector(
        self,
        provider: "IAnalysisWorkbenchProvider",
        VectorA: "IVectorGeometryToolVector",
        VectorB: "IVectorGeometryToolVector",
    ):
        # Create a vector defined as cross product of vectors A and B.
        vector: "IVectorGeometryToolVectorCross" = provider.vectors.factory.create_cross_product_vector(
            "CrossVector", VectorA, VectorB
        )

    # endregion

    # region VectorContains
    def test_VectorContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.VectorContains(provider, "FlightPath")

        finally:
            del root

    def VectorContains(self, provider: "IAnalysisWorkbenchProvider", VectorName: str):
        if provider.vectors.contains(VectorName):
            Console.WriteLine("The vector {0} already exists!", VectorName)

    # endregion

    # region VectorRemove
    def test_VectorRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("SomeVector")))
        someVector: "IVectorGeometryToolVector" = provider.vectors.factory.create(
            "SomeVector", String.Empty, AgECrdnVectorType.eCrdnVectorTypeDisplacement
        )
        try:
            self.VectorRemove(provider, (clr.Convert(someVector, IAnalysisWorkbenchComponent)).name)

        finally:
            del root

    def VectorRemove(self, provider: "IAnalysisWorkbenchProvider", VectorName: str):
        if provider.vectors.contains(VectorName):
            provider.vectors.remove(VectorName)

    # endregion

    # region CreateAngleBetweenPlanes
    def test_CreateAngleBetweenPlanes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        try:
            self.CreateAngleBetweenPlanes(provider)

        finally:
            provider.angles.remove("AngleName")
            del root

    def CreateAngleBetweenPlanes(self, provider: "IAnalysisWorkbenchProvider"):
        # Create an angle between two planes.
        angle: "IVectorGeometryToolAngleBetweenPlanes" = clr.Convert(
            provider.angles.factory.create(
                "AngleName", "Angle from one plane to another.", AgECrdnAngleType.eCrdnAngleTypeBetweenPlanes
            ),
            IVectorGeometryToolAngleBetweenPlanes,
        )

    # endregion

    # region IsAngleTypeSupported
    def test_IsAngleTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("MyAngle")))
        try:
            self.IsAngleTypeSupported(provider, AgECrdnAngleType.eCrdnAngleTypeBetweenPlanes)

        finally:
            provider.angles.remove("MyAngle")
            del root

    # Review: see the comments for the Vector
    def IsAngleTypeSupported(self, provider: "IAnalysisWorkbenchProvider", angleType: "AgECrdnAngleType"):
        if provider.angles.factory.is_type_supported(angleType):
            # Create an Angle with the supported Type
            angle: "IVectorGeometryToolAngle" = provider.angles.factory.create("MyAngle", String.Empty, angleType)

    # endregion

    # region AngleContains
    def test_AngleContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.AngleContains(provider)

        finally:
            del root

    # Review: see the comments for the Angle
    def AngleContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.angles.contains("AngleName"):
            Console.WriteLine('The angle "{0}" already exists!', "AngleName")

    # endregion

    # region AngleRemove
    def test_AngleRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.angles.factory.create(
            "AngleName", String.Empty, AgECrdnAngleType.eCrdnAngleTypeBetweenPlanes
        )
        try:
            self.AngleRemove(provider)

        finally:
            del root

    def AngleRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.angles.contains("AngleName"):
            provider.angles.remove("AngleName")

    # endregion

    # region CreateNormalPlane
    def test_CreateNormalPlane(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.planes.contains("PlaneName")))
        try:
            self.CreateNormalPlane(provider)

        finally:
            provider.planes.remove("PlaneName")
            del root

    def CreateNormalPlane(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a plane normal to vector.
        p: "IVectorGeometryToolPlaneNormal" = clr.Convert(
            provider.planes.factory.create(
                "PlaneName", "A plane normal to vector.", AgECrdnPlaneType.eCrdnPlaneTypeNormal
            ),
            IVectorGeometryToolPlaneNormal,
        )

    # endregion

    # region IsPlaneTypeSupported
    def test_IsPlaneTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.planes.contains("PlaneName")))
        try:
            self.IsPlaneTypeSupported(provider, AgECrdnPlaneType.eCrdnPlaneTypeNormal)

        finally:
            provider.planes.remove("PlaneName")
            del root

    def IsPlaneTypeSupported(self, provider: "IAnalysisWorkbenchProvider", planeType: "AgECrdnPlaneType"):
        if provider.planes.factory.is_type_supported(planeType):
            p: "IVectorGeometryToolPlane" = provider.planes.factory.create("PlaneName", String.Empty, planeType)

    # endregion

    # region PlaneContains
    def test_PlaneContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.PlaneContains(provider)

        finally:
            del root

    def PlaneContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.planes.contains("PlaneName"):
            Console.WriteLine('The plane "{0}" already exists!', "PlaneName")

    # endregion

    # region PlaneRemove
    def test_PlaneRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.planes.contains("PlaneName")))
        plane: "IVectorGeometryToolPlane" = provider.planes.factory.create(
            "PlaneName", String.Empty, AgECrdnPlaneType.eCrdnPlaneTypeNormal
        )
        try:
            self.PlaneRemove(provider)

        finally:
            del root

    def PlaneRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.planes.contains("PlaneName"):
            provider.planes.remove("PlaneName")

    # endregion

    # region CreateAxesAlignedAndConstrained
    def test_CreateAxesAlignedAndConstrained(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        try:
            self.CreateAxesAlignedAndConstrained(provider)

        finally:
            provider.axes.remove("AxesName")
            del root

    def CreateAxesAlignedAndConstrained(self, provider: "IAnalysisWorkbenchProvider"):
        axes: "IVectorGeometryToolAxesAlignedAndConstrained" = clr.Convert(
            provider.axes.factory.create("AxesName", String.Empty, AgECrdnAxesType.eCrdnAxesTypeAlignedAndConstrained),
            IVectorGeometryToolAxesAlignedAndConstrained,
        )

    # endregion

    # region IsAxesTypeSupported
    def test_IsAxesTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        try:
            self.IsAxesTypeSupported(provider, AgECrdnAxesType.eCrdnAxesTypeAlignedAndConstrained)

        finally:
            provider.axes.remove("AxesName")
            del root

    def IsAxesTypeSupported(self, provider: "IAnalysisWorkbenchProvider", axesType: "AgECrdnAxesType"):
        if provider.axes.factory.is_type_supported(axesType):
            axes: "IVectorGeometryToolAxes" = provider.axes.factory.create("AxesName", String.Empty, axesType)

    # endregion

    # region AxesContains
    def test_AxesContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.AxesContains(provider)

        finally:
            del root

    def AxesContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.axes.contains("AxesName"):
            Console.WriteLine('Axes "{0}" already exist!', "AxesName")

    # endregion

    # region AxesRemove
    def test_AxesRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        axes: "IVectorGeometryToolAxes" = provider.axes.factory.create(
            "AxesName", String.Empty, AgECrdnAxesType.eCrdnAxesTypeFixed
        )
        try:
            self.AxesRemove(provider)

        finally:
            del root

    def AxesRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.axes.contains("AxesName"):
            provider.axes.remove("AxesName")

    # endregion

    # region CreatePointBPlane
    def test_CreatePointBPlane(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        try:
            self.CreatePointBPlane(provider, "Earth")

        finally:
            provider.points.remove("PointName")
            del root

    def CreatePointBPlane(self, provider: "IAnalysisWorkbenchProvider", TargetBody: str):
        # Create a B-Plane point using selected target body
        point: "IVectorGeometryToolPointBPlane" = clr.Convert(
            provider.points.factory.create("PointName", String.Empty, AgECrdnPointType.eCrdnPointTypeBPlane),
            IVectorGeometryToolPointBPlane,
        )
        point.target_body.set_path(TargetBody)

    # endregion

    # region IsPointTypeSupported
    def test_IsPointTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        try:
            self.IsPointTypeSupported(provider, AgECrdnPointType.eCrdnPointTypeBPlane)

        finally:
            provider.points.remove("PointName")
            del root

    def IsPointTypeSupported(self, provider: "IAnalysisWorkbenchProvider", PointType: "AgECrdnPointType"):
        if provider.points.factory.is_type_supported(PointType):
            point: "IVectorGeometryToolPoint" = provider.points.factory.create("PointName", String.Empty, PointType)

    # endregion

    # region PointContains
    def test_PointContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.PointContains(provider)

        finally:
            del root

    def PointContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.points.contains("PointName"):
            Console.WriteLine('The point "{0}" exists!', "PointName")

    # endregion

    # region PointRemove
    def test_PointRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "PointName", String.Empty, AgECrdnPointType.eCrdnPointTypeFixedInSystem
        )
        try:
            self.PointRemove(provider)

        finally:
            del root

    def PointRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.points.contains("PointName"):
            provider.points.remove("PointName")

    # endregion

    # region CreateSystemAssembled
    def test_CreateSystemAssembled(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.systems.contains("SystemName")))
        try:
            self.CreateSystemAssembled(provider, provider.points["Center"], provider.axes["Body"])

        finally:
            provider.systems.remove("SystemName")
            del root

    def CreateSystemAssembled(
        self,
        provider: "IAnalysisWorkbenchProvider",
        OriginPoint: "IVectorGeometryToolPoint",
        ReferenceAxes: "IVectorGeometryToolAxes",
    ):
        system: "IVectorGeometryToolSystemAssembled" = clr.Convert(
            provider.systems.factory.create("SystemName", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled),
            IVectorGeometryToolSystemAssembled,
        )
        # Set the system's origin point.
        system.origin_point.set_point(OriginPoint)
        # Set the system's reference axes.
        system.reference_axes.set_axes(ReferenceAxes)

    # endregion

    # region IsSystemTypeSupported
    def test_IsSystemTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.systems.contains("SystemName")))
        try:
            self.IsSystemTypeSupported(provider, AgECrdnSystemType.eCrdnSystemTypeAssembled)

        finally:
            provider.systems.remove("SystemName")
            del root

    def IsSystemTypeSupported(self, provider: "IAnalysisWorkbenchProvider", SystemType: "AgECrdnSystemType"):
        if provider.systems.factory.is_type_supported(SystemType):
            # Create a System with supported Type
            system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
                "SystemName", String.Empty, SystemType
            )

    # endregion

    # region SystemContains
    def test_SystemContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.SystemContains(provider)

        finally:
            del root

    def SystemContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.systems.contains("SystemName"):
            Console.WriteLine('The system "{0}" exists!', "SystemName")

    # endregion

    # region SystemRemove
    def test_SystemRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.systems.contains("SystemName")))
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "SystemName", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.SystemRemove(provider)

        finally:
            del root

    def SystemRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.systems.contains("SystemName"):
            provider.systems.remove("SystemName")

    # endregion

    # region CreateParameterSetAttitude
    def test_CreateParameterSetAttitude(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.parameter_sets.contains("ParameterSetName")))
        try:
            self.CreateParameterSetAttitude(provider)

        finally:
            provider.parameter_sets.remove("ParameterSetName")
            del root

    def CreateParameterSetAttitude(self, provider: "IAnalysisWorkbenchProvider"):
        # Create an attitude parameter set.
        parameterSet: "ICalculationToolParameterSetAttitude" = clr.Convert(
            provider.parameter_sets.factory.create(
                "ParameterSetName", "Attitude parameter set.", AgECrdnParameterSetType.eCrdnParameterSetTypeAttitude
            ),
            ICalculationToolParameterSetAttitude,
        )

    # endregion

    # region IsParameterSetTypeSupported
    def test_IsParameterSetTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.parameter_sets.contains("MyParameterSet")))
        try:
            self.IsParameterSetTypeSupported(provider, AgECrdnParameterSetType.eCrdnParameterSetTypeAttitude)

        finally:
            provider.parameter_sets.remove("MyParameterSet")
            del root

    def IsParameterSetTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", parameterSetType: "AgECrdnParameterSetType"
    ):
        if provider.parameter_sets.factory.is_type_supported(parameterSetType):
            # Create a ParameterSet with the supported Type
            parameterSet: "ICalculationToolParameterSet" = provider.parameter_sets.factory.create(
                "MyParameterSet", String.Empty, parameterSetType
            )

    # endregion

    # region ParameterSetContains
    def test_ParameterSetContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.ParameterSetContains(provider)

        finally:
            del root

    def ParameterSetContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.parameter_sets.contains("ParameterSetName"):
            Console.WriteLine('The parameter set "{0}" already exists!', "ParameterSetName")

    # endregion

    # region ParameterSetRemove
    def test_ParameterSetRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.parameter_sets.contains("ParameterSetName")))
        parameterSet: "ICalculationToolParameterSet" = provider.parameter_sets.factory.create(
            "ParameterSetName", String.Empty, AgECrdnParameterSetType.eCrdnParameterSetTypeAttitude
        )
        try:
            self.ParameterSetRemove(provider)

        finally:
            del root

    def ParameterSetRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.parameter_sets.contains("ParameterSetName"):
            provider.parameter_sets.remove("ParameterSetName")

    # endregion

    # region CreateCalcScalarConstant
    def test_CreateCalcScalarConstant(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.calc_scalars.contains("CalcScalarName")))
        try:
            self.CreateCalcScalarConstant(provider)

        finally:
            provider.calc_scalars.remove("CalcScalarName")
            del root

    def CreateCalcScalarConstant(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a calc scalar constant.
        calcScalar: "ICalculationToolScalarConstant" = clr.Convert(
            provider.calc_scalars.factory.create(
                "CalcScalarName", "Calc scalar constant.", AgECrdnCalcScalarType.eCrdnCalcScalarTypeConstant
            ),
            ICalculationToolScalarConstant,
        )

    # endregion

    # region IsCalcScalarTypeSupported
    def test_IsCalcScalarTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.calc_scalars.contains("MyCalcScalar")))
        try:
            self.IsCalcScalarTypeSupported(provider, AgECrdnCalcScalarType.eCrdnCalcScalarTypeConstant)

        finally:
            provider.calc_scalars.remove("MyCalcScalar")
            del root

    def IsCalcScalarTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", calcScalarType: "AgECrdnCalcScalarType"
    ):
        if provider.calc_scalars.factory.is_type_supported(calcScalarType):
            # Create a CalcScalar with the supported Type
            calcScalar: "ICalculationToolScalar" = provider.calc_scalars.factory.create(
                "MyCalcScalar", String.Empty, calcScalarType
            )

    # endregion

    # region CalcScalarContains
    def test_CalcScalarContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.CalcScalarContains(provider)

        finally:
            del root

    def CalcScalarContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.calc_scalars.contains("CalcScalarName"):
            Console.WriteLine('The calc scalar "{0}" already exists!', "CalcScalarName")

    # endregion

    # region CalcScalarRemove
    def test_CalcScalarRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.calc_scalars.contains("CalcScalarName")))
        calcScalar: "ICalculationToolScalar" = provider.calc_scalars.factory.create(
            "CalcScalarName", String.Empty, AgECrdnCalcScalarType.eCrdnCalcScalarTypeConstant
        )
        try:
            self.CalcScalarRemove(provider)

        finally:
            del root

    def CalcScalarRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.calc_scalars.contains("CalcScalarName"):
            provider.calc_scalars.remove("CalcScalarName")

    # endregion

    # region CreateConditionScalarBounds
    def test_CreateConditionScalarBounds(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.conditions.contains("ConditionName")))
        try:
            self.CreateConditionScalarBounds(provider)

        finally:
            provider.conditions.remove("ConditionName")
            del root

    def CreateConditionScalarBounds(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a condition from a scalar.
        condition: "ICalculationToolConditionScalarBounds" = clr.Convert(
            provider.conditions.factory.create(
                "ConditionName", "Condition from a scalar.", AgECrdnConditionType.eCrdnConditionTypeScalarBounds
            ),
            ICalculationToolConditionScalarBounds,
        )

    # endregion

    # region IsConditionTypeSupported
    def test_IsConditionTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.conditions.contains("MyCondition")))
        try:
            self.IsConditionTypeSupported(provider, AgECrdnConditionType.eCrdnConditionTypeScalarBounds)

        finally:
            provider.conditions.remove("MyCondition")
            del root

    def IsConditionTypeSupported(self, provider: "IAnalysisWorkbenchProvider", conditionType: "AgECrdnConditionType"):
        if provider.conditions.factory.is_type_supported(conditionType):
            # Create a Condition with the supported Type
            condition: "ICalculationToolCondition" = provider.conditions.factory.create(
                "MyCondition", String.Empty, conditionType
            )

    # endregion

    # region ConditionContains
    def test_ConditionContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.ConditionContains(provider)

        finally:
            del root

    def ConditionContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.conditions.contains("ConditionName"):
            Console.WriteLine('The condition "{0}" already exists!', "ConditionName")

    # endregion

    # region ConditionRemove
    def test_ConditionRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.conditions.contains("ConditionName")))
        condition: "ICalculationToolCondition" = provider.conditions.factory.create(
            "ConditionName", String.Empty, AgECrdnConditionType.eCrdnConditionTypeScalarBounds
        )
        try:
            self.ConditionRemove(provider)

        finally:
            del root

    def ConditionRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.conditions.contains("ConditionName"):
            provider.conditions.remove("ConditionName")

    # endregion

    # region IsEventTypeSupported
    def test_IsEventTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.events.contains("MyEvent")))
        try:
            self.IsEventTypeSupported(provider, AgECrdnEventType.eCrdnEventTypeEpoch)

        finally:
            provider.events.remove("MyEvent")
            del root

    def IsEventTypeSupported(self, provider: "IAnalysisWorkbenchProvider", eventType: "AgECrdnEventType"):
        if provider.events.factory.is_type_supported(eventType):
            # Create an Event with the supported Type
            event: "ITimeToolEvent" = provider.events.factory.create("MyEvent", String.Empty, eventType)

    # endregion

    # region EventContains
    def test_EventContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventContains(provider)

        finally:
            del root

    def EventContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.events.contains("EventName"):
            Console.WriteLine('The event "{0}" already exists!', "EventName")

    # endregion

    # region EventRemove
    def test_EventRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.events.contains("EventName")))
        event: "ITimeToolEvent" = provider.events.factory.create(
            "EventName", String.Empty, AgECrdnEventType.eCrdnEventTypeEpoch
        )
        try:
            self.EventRemove(provider)

        finally:
            del root

    def EventRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.events.contains("EventName"):
            provider.events.remove("EventName")

    # endregion

    # region IsEventArrayTypeSupported
    def test_IsEventArrayTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_arrays.contains("MyEventArray")))
        try:
            self.IsEventArrayTypeSupported(provider, AgECrdnEventArrayType.eCrdnEventArrayTypeConditionCrossings)

        finally:
            provider.event_arrays.remove("MyEventArray")
            del root

    def IsEventArrayTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventArrayType: "AgECrdnEventArrayType"
    ):
        if provider.event_arrays.factory.is_type_supported(eventArrayType):
            # Create an EventArray with the supported Type
            eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create(
                "MyEventArray", String.Empty, eventArrayType
            )

    # endregion

    # region EventArrayContains
    def test_EventArrayContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventArrayContains(provider)

        finally:
            del root

    def EventArrayContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_arrays.contains("EventArrayName"):
            Console.WriteLine('The event array "{0}" already exists!', "EventArrayName")

    # endregion

    # region EventArrayRemove
    def test_EventArrayRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_arrays.contains("EventArrayName")))
        eventArray: "ITimeToolEventArray" = provider.event_arrays.factory.create(
            "EventArrayName", String.Empty, AgECrdnEventArrayType.eCrdnEventArrayTypeConditionCrossings
        )
        try:
            self.EventArrayRemove(provider)

        finally:
            del root

    def EventArrayRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_arrays.contains("EventArrayName"):
            provider.event_arrays.remove("EventArrayName")

    # endregion

    # region IsEventIntervalTypeSupported
    def test_IsEventIntervalTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_intervals.contains("MyEventInterval")))
        try:
            self.IsEventIntervalTypeSupported(provider, AgECrdnEventIntervalType.eCrdnEventIntervalTypeFixed)

        finally:
            provider.event_intervals.remove("MyEventInterval")
            del root

    def IsEventIntervalTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventIntervalType: "AgECrdnEventIntervalType"
    ):
        if provider.event_intervals.factory.is_type_supported(eventIntervalType):
            # Create an EventInterval with the supported Type
            eventInterval: "ITimeToolEventInterval" = provider.event_intervals.factory.create(
                "MyEventInterval", String.Empty, eventIntervalType
            )

    # endregion

    # region EventIntervalContains
    def test_EventIntervalContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventIntervalContains(provider)

        finally:
            del root

    def EventIntervalContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_intervals.contains("EventIntervalName"):
            Console.WriteLine('The event interval "{0}" already exists!', "EventIntervalName")

    # endregion

    # region EventIntervalRemove
    def test_EventIntervalRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_intervals.contains("EventIntervalName")))
        eventInterval: "ITimeToolEventInterval" = provider.event_intervals.factory.create(
            "EventIntervalName", String.Empty, AgECrdnEventIntervalType.eCrdnEventIntervalTypeFixed
        )
        try:
            self.EventIntervalRemove(provider)

        finally:
            del root

    def EventIntervalRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_intervals.contains("EventIntervalName"):
            provider.event_intervals.remove("EventIntervalName")

    # endregion

    # region IsEventIntervalCollectionTypeSupported
    def test_IsEventIntervalCollectionTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_interval_collections.contains("MyEventIntervalCollection")))
        try:
            self.IsEventIntervalCollectionTypeSupported(
                provider, AgECrdnEventIntervalCollectionType.eCrdnEventIntervalCollectionTypeLighting
            )

        finally:
            provider.event_interval_collections.remove("MyEventIntervalCollection")
            del root

    def IsEventIntervalCollectionTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventIntervalCollectionType: "AgECrdnEventIntervalCollectionType"
    ):
        if provider.event_interval_collections.factory.is_type_supported(eventIntervalCollectionType):
            # Create an EventIntervalCollection with the supported Type
            eventIntervalCollection: "ITimeToolEventIntervalCollection" = (
                provider.event_interval_collections.factory.create(
                    "MyEventIntervalCollection", String.Empty, eventIntervalCollectionType
                )
            )

    # endregion

    # region EventIntervalCollectionContains
    def test_EventIntervalCollectionContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventIntervalCollectionContains(provider)

        finally:
            del root

    def EventIntervalCollectionContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_interval_collections.contains("EventIntervalCollectionName"):
            Console.WriteLine('The event interval collection "{0}" already exists!', "EventIntervalCollectionName")

    # endregion

    # region EventIntervalCollectionRemove
    def test_EventIntervalCollectionRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_interval_collections.contains("EventIntervalCollectionName")))
        eventIntervalCollection: "ITimeToolEventIntervalCollection" = (
            provider.event_interval_collections.factory.create(
                "EventIntervalCollectionName",
                String.Empty,
                AgECrdnEventIntervalCollectionType.eCrdnEventIntervalCollectionTypeLighting,
            )
        )
        try:
            self.EventIntervalCollectionRemove(provider)

        finally:
            del root

    def EventIntervalCollectionRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_interval_collections.contains("EventIntervalCollectionName"):
            provider.event_interval_collections.remove("EventIntervalCollectionName")

    # endregion

    # region IsEventIntervalListTypeSupported
    def test_IsEventIntervalListTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_interval_lists.contains("MyEventIntervalList")))
        try:
            self.IsEventIntervalListTypeSupported(
                provider, AgECrdnEventIntervalListType.eCrdnEventIntervalListTypeCondition
            )

        finally:
            provider.event_interval_lists.remove("MyEventIntervalList")
            del root

    def IsEventIntervalListTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventIntervalListType: "AgECrdnEventIntervalListType"
    ):
        if provider.event_interval_lists.factory.is_type_supported(eventIntervalListType):
            # Create an EventIntervalList with the supported Type
            eventIntervalList: "ITimeToolEventIntervalList" = provider.event_interval_lists.factory.create(
                "MyEventIntervalList", String.Empty, eventIntervalListType
            )

    # endregion

    # region EventIntervalListContains
    def test_EventIntervalListContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            self.EventIntervalListContains(provider)

        finally:
            del root

    def EventIntervalListContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_interval_lists.contains("EventIntervalListName"):
            Console.WriteLine('The event interval list "{0}" already exists!', "EventIntervalListName")

    # endregion

    # region EventIntervalListRemove
    def test_EventIntervalListRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.event_interval_lists.contains("EventIntervalListName")))
        eventIntervalList: "ITimeToolEventIntervalList" = provider.event_interval_lists.factory.create(
            "EventIntervalListName", String.Empty, AgECrdnEventIntervalListType.eCrdnEventIntervalListTypeCondition
        )
        try:
            self.EventIntervalListRemove(provider)

        finally:
            del root

    def EventIntervalListRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.event_interval_lists.contains("EventIntervalListName"):
            provider.event_interval_lists.remove("EventIntervalListName")

    # endregion

    # region Angle.FindAngle
    def test_FindAngle(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.angles.factory.create(
            "AngleName", String.Empty, AgECrdnAngleType.eCrdnAngleTypeBetweenVectors
        )
        try:
            self.FindAngle(angle)

        finally:
            provider.angles.remove("AngleName")
            del root

    def FindAngle(self, angle: "IVectorGeometryToolAngle"):
        result: "IVectorGeometryToolAngleFindAngleResult" = angle.find_angle(0)
        if result.is_valid:
            Console.WriteLine("Angle: {0}", result.angle)

    # endregion

    # region Angle.FindAngleAndRate
    def test_FindAngleAndRate(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.angles.contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.angles.factory.create(
            "AngleName", String.Empty, AgECrdnAngleType.eCrdnAngleTypeBetweenVectors
        )
        try:
            self.FindAngleAndRate(angle)

        finally:
            provider.angles.remove("AngleName")
            del root

    def FindAngleAndRate(self, angle: "IVectorGeometryToolAngle"):
        result: "IVectorGeometryToolAngleFindAngleWithRateResult" = angle.find_angle_with_rate(0)
        if result.is_valid:
            Console.WriteLine("Angle: {0}, Rate: {1}", result.angle, result.angle_rate)

    # endregion

    # region Axes.FindInAxes
    def test_FindAxesInEarthFixed(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.axes.contains("AxesName")))
        axes: "IVectorGeometryToolAxes" = provider.axes.factory.create(
            "AxesName", String.Empty, AgECrdnAxesType.eCrdnAxesTypeFixed
        )
        try:
            self.FindAxesInEarthFixed(provider, axes)

        finally:
            provider.axes.remove("AxesName")
            del root

    def FindAxesInEarthFixed(self, provider: "IAnalysisWorkbenchProvider", axes: "IVectorGeometryToolAxes"):
        result: "IVectorGeometryToolAxesFindInAxesResult" = axes.find_in_axes(0, provider.well_known_axes.earth.fixed)
        if result.is_valid:
            angles: "IOrientationEulerAngles" = clr.Convert(
                result.orientation.convert_to(AgEOrientationType.eEulerAngles), IOrientationEulerAngles
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
        dpGroup: "IDataProviderGroup" = clr.CastAs(sat.data_providers["Cartesian Position"], IDataProviderGroup)
        elements = ["x", "y", "z"]
        dp: "IDataProviderTimeVarying" = clr.CastAs(dpGroup.group["ICRF"], IDataProviderTimeVarying)
        dpResult: "IDataProviderResult" = dp.exec_elements(numEpSec, numEpSec, 60, elements)
        xICRF: float = float(dpResult.data_sets[0].get_values()[0])
        yICRF: float = float(dpResult.data_sets[1].get_values()[0])
        zICRF: float = float(dpResult.data_sets[2].get_values()[0])

        # Create a vector using the ICRF coordinates
        axesICRF: "IVectorGeometryToolAxes" = sat.vgt.well_known_axes.earth.icrf
        vectorICRF: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
        vectorICRF.set(xICRF, yICRF, zICRF)

        # Use the Transform method to transform ICRF to Fixed
        axesFixed: "IVectorGeometryToolAxes" = sat.vgt.well_known_axes.earth.fixed
        result: "IVectorGeometryToolAxesTransformResult" = axesICRF.transform(numEpSec, axesFixed, vectorICRF)

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
        dpGroup: "IDataProviderGroup" = clr.CastAs(sat.data_providers["Cartesian Position"], IDataProviderGroup)
        elements = ["x", "y", "z"]
        dp: "IDataProviderTimeVarying" = clr.CastAs(dpGroup.group["ICRF"], IDataProviderTimeVarying)
        dpResult: "IDataProviderResult" = dp.exec_elements(numEpSec, numEpSec, 60, elements)
        xICRF: float = float(dpResult.data_sets[0].get_values()[0])
        yICRF: float = float(dpResult.data_sets[1].get_values()[0])
        zICRF: float = float(dpResult.data_sets[2].get_values()[0])

        # Get the satellite's ICRF cartesian velocity at 180 EpSec using the data provider interface
        dpGroup = clr.CastAs(sat.data_providers["Cartesian Velocity"], IDataProviderGroup)
        dp = clr.CastAs(dpGroup.group["ICRF"], IDataProviderTimeVarying)
        dpResult = dp.exec_elements(numEpSec, numEpSec, 60, elements)
        xvelICRF: float = float(dpResult.data_sets[0].get_values()[0])
        yvelICRF: float = float(dpResult.data_sets[1].get_values()[0])
        zvelICRF: float = float(dpResult.data_sets[2].get_values()[0])

        # Create a position vector using the ICRF coordinates
        axesICRF: "IVectorGeometryToolAxes" = sat.vgt.well_known_axes.earth.icrf
        vectorICRF: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
        vectorICRF.set(xICRF, yICRF, zICRF)

        # Create a velocity vector using the ICRF coordinates
        vectorvelICRF: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
        vectorvelICRF.set(xvelICRF, yvelICRF, zvelICRF)

        # Use the TransformWithRate method to transform ICRF to Fixed
        axesFixed: "IVectorGeometryToolAxes" = sat.vgt.well_known_axes.earth.fixed
        result: "IVectorGeometryToolAxesTransformWithRateResult" = axesICRF.transform_with_rate(
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
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.points.contains("PointName")))
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "PointName", String.Empty, AgECrdnPointType.eCrdnPointTypeFixedInSystem
        )
        try:
            self.PointLocateInEarthFixedSystem(provider, point)

        finally:
            provider.points.remove("PointName")
            del root

    def PointLocateInEarthFixedSystem(self, provider: "IAnalysisWorkbenchProvider", point: "IVectorGeometryToolPoint"):
        result: "IVectorGeometryToolPointLocateInSystemResult" = point.locate_in_system(
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
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        Assert.assertTrue((not provider.vectors.contains("VectorName")))
        vector: "IVectorGeometryToolVector" = provider.vectors.factory.create(
            "PointName", String.Empty, AgECrdnVectorType.eCrdnVectorTypeDisplacement
        )
        try:
            self.VectorFindInEarthFixedAxes(provider, vector)

        finally:
            provider.points.remove("PointName")
            del root

    def VectorFindInEarthFixedAxes(self, provider: "IAnalysisWorkbenchProvider", vector: "IVectorGeometryToolVector"):
        result: "IVectorGeometryToolVectorFindInAxesResult" = vector.find_in_axes(
            0, provider.well_known_axes.earth.fixed
        )
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
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        try:
            vector: "ICartesian3Vector" = TestBase.Application.conversion_utility.new_cartesian3_vector()
            self.AxesAnonymousFixed(provider)

        finally:
            del root

    def AxesAnonymousFixed(self, provider: "IAnalysisWorkbenchProvider"):
        ecfAxes: "IVectorGeometryToolAxes" = provider.well_known_axes.earth.fixed
        axesFixed: "IVectorGeometryToolAxesFixed" = provider.axes.common_tasks.create_fixed(ecfAxes)

    # endregion

    # region Axes.CreateTopocentricAxesEulerAngles
    def test_AxesCreateTopocentricAxesEulerAngles(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        facility: "IFacility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            self.AxesCreateTopocentricAxesEulerAngles(provider, facility)

        finally:
            del root

    def AxesCreateTopocentricAxesEulerAngles(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0

        (lat, lon, alt) = facility.position.query_planetodetic()
        origin: "IVectorGeometryToolPointFixedInSystem" = (
            provider.points.common_tasks.create_fixed_in_system_cartographic(provider.systems["Fixed"], lat, lon, alt)
        )
        eastNorthUp: "IVectorGeometryToolAxesFixed" = provider.axes.common_tasks.create_topocentric_axes_euler_angles(
            clr.Convert(origin, IVectorGeometryToolPoint), AgEEulerOrientationSequence.e321, 90.0, 0.0, 0.0
        )

    # endregion

    # region Axes.CreateTopocentricAxesQuaternion
    def test_AxesCreateTopocentricAxesQuaternion(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        facility: "IFacility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            self.AxesCreateTopocentricAxesQuaternion(provider, facility)

        finally:
            del root

    def AxesCreateTopocentricAxesQuaternion(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0

        (lat, lon, alt) = facility.position.query_planetodetic()
        origin: "IVectorGeometryToolPointFixedInSystem" = (
            provider.points.common_tasks.create_fixed_in_system_cartographic(provider.systems["Fixed"], lat, lon, alt)
        )
        eastNorthUp: "IVectorGeometryToolAxesFixed" = provider.axes.common_tasks.create_topocentric_axes_quaternion(
            clr.Convert(origin, IVectorGeometryToolPoint), 0.0, 0.0, 0.0, 1.0
        )

    # endregion

    # region Systems.CreateAssembled
    def test_SystemsCreateAssembled(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        facility: "IFacility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            self.SystemsCreateAssembled(provider, facility)

        finally:
            del root

    def SystemsCreateAssembled(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        systemAssembled: "IVectorGeometryToolSystemAssembled" = provider.systems.common_tasks.create_assembled(
            (clr.Convert(facility, IStkObject)).vgt.points["Center"], provider.axes["Fixed"]
        )

    # endregion

    # region Systems.CreateEastNorthUpCartographic
    def test_SystemsCreateEastNorthUpCartographic(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        facility: "IFacility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.current_scenario.children["Facility1"].vgt
        try:
            self.SystemsCreateEastNorthUpCartographic(provider, facility)

        finally:
            del root

    def SystemsCreateEastNorthUpCartographic(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0
        (lat, lon, alt) = facility.position.query_planetodetic()
        systemAssembled: "IVectorGeometryToolSystemAssembled" = (
            provider.systems.common_tasks.create_east_north_up_cartographic(lat, lon, alt)
        )

    # endregion

    # region Point.CreateFixedInSystemCartographic
    def test_PointCreateFixedInSystemCartographic(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        facility: "IFacility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            self.PointCreateFixedInSystemCartographic(provider, facility)

        finally:
            del root

    def PointCreateFixedInSystemCartographic(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0
        (lat, lon, alt) = facility.position.query_planetodetic()
        origin: "IVectorGeometryToolPointFixedInSystem" = (
            provider.points.common_tasks.create_fixed_in_system_cartographic(provider.systems["Fixed"], lat, lon, alt)
        )

    # endregion

    # region Point.CreateFixedInSystemCartesian
    def test_PointCreateFixedInSystemCartesian(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        facility: "IFacility" = clr.CastAs(TestBase.Application.current_scenario.children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            self.PointCreateFixedInSystemCartesian(provider, facility)

        finally:
            del root

    def PointCreateFixedInSystemCartesian(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        X: float = 0
        Y: float = 0
        Z: float = 0

        (X, Y, Z) = facility.position.query_cartesian()
        origin: "IVectorGeometryToolPointFixedInSystem" = provider.points.common_tasks.create_fixed_in_system_cartesian(
            provider.systems["Fixed"], X, Y, Z
        )

    # endregion

    # region Duplicate
    def test_Duplicate(self):
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            provider.points.remove("OriginalPoint")
            self.Duplicate(provider)

        finally:
            pass

    def Duplicate(self, provider: "IAnalysisWorkbenchProvider"):
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "OriginalPoint", "description", AgECrdnPointType.eCrdnPointTypeAtTimeInstant
        )
        duplicate: "IAnalysisWorkbenchComponent" = (clr.Convert(point, IAnalysisWorkbenchComponent)).duplicate(
            "DuplicatePoint", "description"
        )

    # endregion

    # region AnonymousDuplicate
    def test_AnonymousDuplicate(self):
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.central_bodies["Earth"].vgt
        try:
            provider.points.remove("OriginalPoint")
            self.AnonymousDuplicate(provider)

        finally:
            pass

    def AnonymousDuplicate(self, provider: "IAnalysisWorkbenchProvider"):
        point: "IVectorGeometryToolPoint" = provider.points.factory.create(
            "OriginalPoint", "description", AgECrdnPointType.eCrdnPointTypeAtTimeInstant
        )
        anonymousDuplicate: "IAnalysisWorkbenchComponent" = (
            clr.Convert(point, IAnalysisWorkbenchComponent)
        ).anonymous_duplicate()

    # endregion

    # region GetEmbeddedComponent
    def test_GetEmbeddedComponent(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "mySystem", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.GetEmbeddedComponent(clr.Convert(system, IAnalysisWorkbenchComponent))

        finally:
            provider.systems.remove("mySystem")
            del root

    def GetEmbeddedComponent(self, crdn: "IAnalysisWorkbenchComponent"):
        if crdn.embedded_components.contains("Origin"):
            embeddedComponent: "IAnalysisWorkbenchComponent" = crdn.embedded_components["Origin"]

    # endregion

    # region EnumerateThroughEmbeddedComponents
    def test_EnumerateThroughEmbeddedComponents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "mySystem", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.EnumerateThroughEmbeddedComponents(clr.Convert(system, IAnalysisWorkbenchComponent))

        finally:
            provider.systems.remove("mySystem")
            del root

    def EnumerateThroughEmbeddedComponents(self, crdn: "IAnalysisWorkbenchComponent"):
        embeddedComponent: "IAnalysisWorkbenchComponent"
        for embeddedComponent in crdn.embedded_components:
            Console.WriteLine("Name: {0}, kind: {1}", embeddedComponent.name, embeddedComponent.kind)

    # endregion

    # region IterateThroughEmbeddedComponents
    def test_IterateThroughEmbeddedComponents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.systems.factory.create(
            "mySystem", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.IterateThroughEmbeddedComponents(clr.Convert(system, IAnalysisWorkbenchComponent))

        finally:
            provider.systems.remove("mySystem")
            del root

    def IterateThroughEmbeddedComponents(self, crdn: "IAnalysisWorkbenchComponent"):
        i: int = 0
        while i < crdn.embedded_components.count:
            embeddedComponent: "IAnalysisWorkbenchComponent" = crdn.embedded_components[i]
            Console.WriteLine("Name: {0}, kind: {1}", embeddedComponent.name, embeddedComponent.kind)

            i += 1

    # endregion

    # region AngleHasCyclicDependency
    def test_AngleHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        angleRate: "IVectorGeometryToolVectorAngleRate" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeAngleRate),
            IVectorGeometryToolVectorAngleRate,
        )
        angle: "IVectorGeometryToolAngle" = provider.angles["VelocityAzimuth"]
        try:
            self.AngleHasCyclicDependency(angleRate.angle, angle)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def AngleHasCyclicDependency(self, angleRefTo: "IVectorGeometryToolAngleRefTo", angle: "IVectorGeometryToolAngle"):
        if angleRefTo.has_cyclic_dependency(angle):
            Console.WriteLine(
                "The angle {0} has a cyclic dependency on angle {1}.",
                (clr.Convert(angleRefTo.get_angle(), IAnalysisWorkbenchComponent)).name,
                (clr.Convert(angle, IAnalysisWorkbenchComponent)).name,
            )

    # endregion

    # region AxesHasCyclicDependency
    def test_AxesHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        angVel: "IVectorGeometryToolVectorAngularVelocity" = clr.CastAs(
            provider.vectors.factory.create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeAngularVelocity
            ),
            IVectorGeometryToolVectorAngularVelocity,
        )
        axes: "IVectorGeometryToolAxes" = provider.axes["Body"]
        try:
            self.AxesHasCyclicDependency(angVel.axes, axes)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def AxesHasCyclicDependency(self, axesRefTo: "IVectorGeometryToolAxesRefTo", axes: "IVectorGeometryToolAxes"):
        if axesRefTo.has_cyclic_dependency(axes):
            Console.WriteLine(
                "The axes {0} has a cyclic dependency on axes {1}.",
                (clr.Convert(axesRefTo.get_axes(), IAnalysisWorkbenchComponent)).name,
                (clr.Convert(axes, IAnalysisWorkbenchComponent)).name,
            )

    # endregion

    # region PlaneHasCyclicDependency
    def test_PlaneHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        twoPlane: "IVectorGeometryToolVectorTwoPlanesIntersection" = clr.CastAs(
            provider.vectors.factory.create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeTwoPlanesIntersection
            ),
            IVectorGeometryToolVectorTwoPlanesIntersection,
        )
        plane: "IVectorGeometryToolPlane" = provider.planes["BodyXY"]
        try:
            self.PlaneHasCyclicDependency(twoPlane.plane_a, plane)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def PlaneHasCyclicDependency(self, planeRefTo: "IVectorGeometryToolPlaneRefTo", plane: "IVectorGeometryToolPlane"):
        if planeRefTo.has_cyclic_dependency(plane):
            Console.WriteLine(
                "The plane {0} has a cyclic dependency on plane {1}.",
                (clr.Convert(planeRefTo.get_plane(), IAnalysisWorkbenchComponent)).name,
                (clr.Convert(plane, IAnalysisWorkbenchComponent)).name,
            )

    # endregion

    # region PointHasCyclicDependency
    def test_PointHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        apoapsis: "IVectorGeometryToolVectorApoapsis" = clr.CastAs(
            provider.vectors.factory.create("DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeApoapsis),
            IVectorGeometryToolVectorApoapsis,
        )
        point: "IVectorGeometryToolPoint" = provider.points["Center"]
        try:
            self.PointHasCyclicDependency(apoapsis.reference_point, point)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def PointHasCyclicDependency(self, pointRefTo: "IVectorGeometryToolPointRefTo", point: "IVectorGeometryToolPoint"):
        if pointRefTo.has_cyclic_dependency(point):
            Console.WriteLine(
                "The point {0} has a cyclic dependency on point {1}.",
                (clr.Convert(pointRefTo.get_point(), IAnalysisWorkbenchComponent)).name,
                (clr.Convert(point, IAnalysisWorkbenchComponent)).name,
            )

    # endregion

    # region SystemHasCyclicDependency
    def test_SystemHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        displacement: "IVectorGeometryToolVectorDisplacement" = clr.CastAs(
            provider.vectors.factory.create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeDisplacement
            ),
            IVectorGeometryToolVectorDisplacement,
        )
        displacement.apparent = True
        system: "IVectorGeometryToolSystem" = provider.systems["Body"]
        try:
            self.SystemHasCyclicDependency(displacement.reference_system, system)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def SystemHasCyclicDependency(
        self, systemRefTo: "IVectorGeometryToolSystemRefTo", system: "IVectorGeometryToolSystem"
    ):
        if systemRefTo.has_cyclic_dependency(system):
            Console.WriteLine(
                "The system {0} has a cyclic dependency on system {1}.",
                (clr.Convert(systemRefTo.get_system(), IAnalysisWorkbenchComponent)).name,
                (clr.Convert(system, IAnalysisWorkbenchComponent)).name,
            )

    # endregion

    # region VectorHasCyclicDependency
    def test_VectorHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.vgt_root
        provider: "IAnalysisWorkbenchProvider" = root.get_provider("Satellite/Satellite1")
        reflection: "IVectorGeometryToolVectorReflection" = clr.CastAs(
            provider.vectors.factory.create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeReflection
            ),
            IVectorGeometryToolVectorReflection,
        )
        vector: "IVectorGeometryToolVector" = provider.vectors["Earth"]
        try:
            self.VectorHasCyclicDependency(reflection.normal_vector, vector)

        finally:
            provider.vectors.remove("DependencyTest")
            del root

    def VectorHasCyclicDependency(
        self, vectorRefTo: "IVectorGeometryToolVectorRefTo", vector: "IVectorGeometryToolVector"
    ):
        if vectorRefTo.has_cyclic_dependency(vector):
            Console.WriteLine(
                "The vector {0} has a cyclic dependency on vector {1}.",
                (clr.Convert(vectorRefTo.get_vector(), IAnalysisWorkbenchComponent)).name,
                (clr.Convert(vector, IAnalysisWorkbenchComponent)).name,
            )

    # endregion
