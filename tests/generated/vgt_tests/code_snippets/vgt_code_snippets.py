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
            TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "Satellite1"), ISatellite
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        (clr.CastAs(sat.Propagator, IVehiclePropagatorTwoBody)).Propagate()

        fac: "IFacility" = clr.CastAs(
            TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "Facility1"), IFacility
        )

        scenario: "IScenario" = clr.Convert(TestBase.Application.CurrentScenario, IScenario)
        scenario.Epoch = "1 Jan 2012 12:00:00.000"

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        TestBase.Application.UnitPreferences.SetCurrentUnit("DateFormat", "EpSec")
        TestBase.Application.UnitPreferences.SetCurrentUnit("TimeUnit", "sec")

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region rootGetVGTProvider
    def test_rootGetVGTProvider(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        try:
            self.rootGetVGTProvider(root, "Satellite/Satellite1")

        finally:
            del root

    def rootGetVGTProvider(self, root: "IAnalysisWorkbenchRoot", path: str):
        # Returns a provider associated with the specified
        # instance of an STK Object or a Central Body.
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider(path)

    # endregion

    # region rootGetVGTTemplateProvider
    def test_rootGetVGTTemplateProvider(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        try:
            self.rootGetVGTTemplateProvider(root, "Satellite")

        finally:
            del root

    def rootGetVGTTemplateProvider(self, root: "IAnalysisWorkbenchRoot", className: str):
        # Returns a VGT provider associated with the specified
        # STK object class (i.e., Satellite, Facility, etc.) or
        # a Central Body.
        provider: "IAnalysisWorkbenchProvider" = root.GetTemplateProvider(className)

    # endregion

    # region EnumerateThroughVectors
    def test_EnumerateThroughVectors(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughVectors(provider)

        finally:
            del root

    def EnumerateThroughVectors(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing vectors using specified CrdnProvider.
        vector: "IVectorGeometryToolVector"
        # Enumerate the existing vectors using specified CrdnProvider.
        for vector in provider.Vectors:
            # All vectors implement IAgCrdn interface which provides
            # information about the vector instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(vector, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, vector.Type)

    # endregion

    # region EnumerateThroughPoints
    def test_EnumerateThroughPoints(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughPoints(provider)

        finally:
            del root

    def EnumerateThroughPoints(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing points using specified CrdnProvider.
        point: "IVectorGeometryToolPoint"
        # Enumerate the existing points using specified CrdnProvider.
        for point in provider.Points:
            # All points implement IAgCrdn interface which provides
            # information about the point instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(point, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, point.Type)

    # endregion

    # region EnumerateThroughAngles
    def test_EnumerateThroughAngles(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughAngles(provider)

        finally:
            del root

    def EnumerateThroughAngles(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing angles using specified CrdnProvider.
        angle: "IVectorGeometryToolAngle"
        # Enumerate the existing angles using specified CrdnProvider.
        for angle in provider.Angles:
            # All angles implement IAgCrdn interface which provides
            # information about the angle instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(angle, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, angle.Type)

    # endregion

    # region EnumerateThroughAxes
    def test_EnumerateThroughAxes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughAxes(provider)

        finally:
            del root

    def EnumerateThroughAxes(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Axes using specified CrdnProvider.
        axes: "IVectorGeometryToolAxes"
        # Enumerate the existing Axes using specified CrdnProvider.
        for axes in provider.Axes:
            # All axes implement IAgCrdn interface which provides
            # information about the axes instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(axes, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, axes.Type)

    # endregion

    # region EnumerateThroughPlanes
    def test_EnumerateThroughPlanes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughPlanes(provider)

        finally:
            del root

    def EnumerateThroughPlanes(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Planes using specified CrdnProvider.
        plane: "IVectorGeometryToolPlane"
        # Enumerate the existing Planes using specified CrdnProvider.
        for plane in provider.Planes:
            # All planes implement IAgCrdn interface which provides
            # information about the plane instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(plane, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, plane.Type)

    # endregion

    # region EnumerateThroughSystems
    def test_EnumerateThroughSystems(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughSystems(provider)

        finally:
            del root

    def EnumerateThroughSystems(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Systems using specified CrdnProvider.
        system: "IVectorGeometryToolSystem"
        # Enumerate the existing Systems using specified CrdnProvider.
        for system in provider.Systems:
            # All systems implement IAgCrdn interface which provides
            # information about the system instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(system, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, system.Type)

    # endregion

    # region EnumerateThroughParameterSets
    def test_EnumerateThroughParameterSets(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughParameterSets(provider)

        finally:
            del root

    def EnumerateThroughParameterSets(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing ParameterSets using specified CrdnProvider.
        parameterSet: "ICalculationToolParameterSet"
        # Enumerate the existing ParameterSets using specified CrdnProvider.
        for parameterSet in provider.ParameterSets:
            # All parameter sets implement IAgCrdn interface which provides
            # information about the parameter set instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(parameterSet, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, parameterSet.Type)

    # endregion

    # region EnumerateThroughCalcScalars
    def test_EnumerateThroughCalcScalars(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughCalcScalars(provider)

        finally:
            del root

    def EnumerateThroughCalcScalars(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing CalcScalars using specified CrdnProvider.
        calcScalar: "ICalculationToolScalar"
        # Enumerate the existing CalcScalars using specified CrdnProvider.
        for calcScalar in provider.CalcScalars:
            # All calc scalars implement IAgCrdn interface which provides
            # information about the calc scalar instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(calcScalar, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, calcScalar.Type)

    # endregion

    # region EnumerateThroughConditions
    def test_EnumerateThroughConditions(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughConditions(provider)

        finally:
            del root

    def EnumerateThroughConditions(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Conditions using specified CrdnProvider.
        condition: "ICalculationToolCondition"
        # Enumerate the existing Conditions using specified CrdnProvider.
        for condition in provider.Conditions:
            # All conditions implement IAgCrdn interface which provides
            # information about the condition instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(condition, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, condition.Type)

    # endregion

    # region EnumerateThroughEvents
    def test_EnumerateThroughEvents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEvents(provider)

        finally:
            del root

    def EnumerateThroughEvents(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing Events using specified CrdnProvider.
        event: "ITimeToolEvent"
        # Enumerate the existing Events using specified CrdnProvider.
        for event in provider.Events:
            # All events implement IAgCrdn interface which provides
            # information about the event instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(event, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, event.Type)

    # endregion

    # region EnumerateThroughEventArrays
    def test_EnumerateThroughEventArrays(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventArrays(provider)

        finally:
            del root

    def EnumerateThroughEventArrays(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventArrays using specified CrdnProvider.
        eventArray: "ITimeToolEventArray"
        # Enumerate the existing EventArrays using specified CrdnProvider.
        for eventArray in provider.EventArrays:
            # All event arrays implement IAgCrdn interface which provides
            # information about the event array instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventArray, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventArray.Type)

    # endregion

    # region EnumerateThroughEventIntervals
    def test_EnumerateThroughEventIntervals(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervals(provider)

        finally:
            del root

    def EnumerateThroughEventIntervals(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventIntervals using specified CrdnProvider.
        eventInterval: "ITimeToolEventInterval"
        # Enumerate the existing EventIntervals using specified CrdnProvider.
        for eventInterval in provider.EventIntervals:
            # All event intervals implement IAgCrdn interface which provides
            # information about the event interval instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventInterval, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventInterval.Type)

    # endregion

    # region EnumerateThroughEventIntervalCollections
    def test_EnumerateThroughEventIntervalCollections(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervalCollections(provider)

        finally:
            del root

    def EnumerateThroughEventIntervalCollections(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventIntervalCollections using specified CrdnProvider.
        eventIntervalCollection: "ITimeToolEventIntervalCollection"
        # Enumerate the existing EventIntervalCollections using specified CrdnProvider.
        for eventIntervalCollection in provider.EventIntervalCollections:
            # All event interval collections implement IAgCrdn interface which provides
            # information about the event interval collection instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventIntervalCollection, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventIntervalCollection.Type)

    # endregion

    # region EnumerateThroughEventIntervalLists
    def test_EnumerateThroughEventIntervalLists(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EnumerateThroughEventIntervalLists(provider)

        finally:
            del root

    def EnumerateThroughEventIntervalLists(self, provider: "IAnalysisWorkbenchProvider"):
        # Enumerate the existing EventIntervalLists using specified CrdnProvider.
        eventIntervalList: "ITimeToolEventIntervalList"
        # Enumerate the existing EventIntervalLists using specified CrdnProvider.
        for eventIntervalList in provider.EventIntervalLists:
            # All event interval lists implement IAgCrdn interface which provides
            # information about the event interval list instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(eventIntervalList, IAnalysisWorkbenchComponent)
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventIntervalList.Type)

    # endregion

    # region IterateThroughVectors
    def test_IterateThroughVectors(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughVectors(provider)

        finally:
            del root

    def IterateThroughVectors(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Vectors.Count:
            vector: "IVectorGeometryToolVector" = provider.Vectors[i]
            # All vectors implement IAgCrdn interface which provides
            # information about the vector instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(vector, IAnalysisWorkbenchComponent)
            # Print the vector name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, vector.Type)

            i += 1

    # endregion

    # region IterateThroughPoint
    def test_IterateThroughPoints(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughPoints(provider)

        finally:
            del root

    def IterateThroughPoints(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Points.Count:
            point: "IVectorGeometryToolPoint" = provider.Points[i]
            # All points implement IAgCrdn interface which provides
            # information about the point instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Points[i], IAnalysisWorkbenchComponent)
            # Print the point name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, point.Type)

            i += 1

    # endregion

    # region IterateThroughAngles
    def test_IterateThroughAngles(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughAngles(provider)

        finally:
            del root

    def IterateThroughAngles(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Angles.Count:
            angle: "IVectorGeometryToolAngle" = provider.Angles[i]
            # All angles implement IAgCrdn interface which provides
            # information about the angle instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Angles[i], IAnalysisWorkbenchComponent)
            # Print the angle name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, angle.Type)

            i += 1

    # endregion

    # region IterateThroughAxes
    def test_IterateThroughAxes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughAxes(provider)

        finally:
            del root

    def IterateThroughAxes(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Axes.Count:
            axes: "IVectorGeometryToolAxes" = provider.Axes[i]
            # All axes implement IAgCrdn interface which provides
            # information about the axes instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Axes[i], IAnalysisWorkbenchComponent)
            # Print the axes name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, axes.Type)

            i += 1

    # endregion

    # region IterateThroughPlanes
    def test_IterateThroughPlanes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughPlanes(provider)

        finally:
            del root

    def IterateThroughPlanes(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Planes.Count:
            plane: "IVectorGeometryToolPlane" = provider.Planes[i]
            # All planes implement IAgCrdn interface which provides
            # information about the plane's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Planes[i], IAnalysisWorkbenchComponent)
            # Print the plane's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, plane.Type)

            i += 1

    # endregion

    # region IterateThroughSystems
    def test_IterateThroughSystems(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughSystems(provider)

        finally:
            del root

    def IterateThroughSystems(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Systems.Count:
            crdnSystem: "IVectorGeometryToolSystem" = provider.Systems[i]
            # All coordinate reference frames implement IAgCrdn interface which provides
            # information about the reference frame's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Systems[i], IAnalysisWorkbenchComponent)
            # Print the reference frame's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, crdnSystem.Type)

            i += 1

    # endregion

    # region IterateThroughParameterSets
    def test_IterateThroughParameterSets(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughParameterSets(provider)

        finally:
            del root

    def IterateThroughParameterSets(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.ParameterSets.Count:
            parameterSet: "ICalculationToolParameterSet" = provider.ParameterSets[i]
            # All parameter sets implement IAgCrdn interface which provides
            # information about the parameter set's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.ParameterSets[i], IAnalysisWorkbenchComponent)
            # Print the parameter set's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, parameterSet.Type)

            i += 1

    # endregion

    # region IterateThroughCalcScalars
    def test_IterateThroughCalcScalars(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughCalcScalars(provider)

        finally:
            del root

    def IterateThroughCalcScalars(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.CalcScalars.Count:
            calcScalar: "ICalculationToolScalar" = provider.CalcScalars[i]
            # All calc scalars implement IAgCrdn interface which provides
            # information about the calc scalar's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.CalcScalars[i], IAnalysisWorkbenchComponent)
            # Print the calc scalar's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, calcScalar.Type)

            i += 1

    # endregion

    # region IterateThroughConditions
    def test_IterateThroughConditions(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughConditions(provider)

        finally:
            del root

    def IterateThroughConditions(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Conditions.Count:
            condition: "ICalculationToolCondition" = provider.Conditions[i]
            # All conditions implement IAgCrdn interface which provides
            # information about the condition's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Conditions[i], IAnalysisWorkbenchComponent)
            # Print the condition's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, condition.Type)

            i += 1

    # endregion

    # region IterateThroughEvents
    def test_IterateThroughEvents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughEvents(provider)

        finally:
            del root

    def IterateThroughEvents(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.Events.Count:
            event: "ITimeToolEvent" = provider.Events[i]
            # All events implement IAgCrdn interface which provides
            # information about the event's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.Events[i], IAnalysisWorkbenchComponent)
            # Print the event's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, event.Type)

            i += 1

    # endregion

    # region IterateThroughEventArrays
    def test_IterateThroughEventArrays(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughEventArrays(provider)

        finally:
            del root

    def IterateThroughEventArrays(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.EventArrays.Count:
            eventArray: "ITimeToolEventArray" = provider.EventArrays[i]
            # All event arrays implement IAgCrdn interface which provides
            # information about the event array's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.EventArrays[i], IAnalysisWorkbenchComponent)
            # Print the event array's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventArray.Type)

            i += 1

    # endregion

    # region IterateThroughEventIntervals
    def test_IterateThroughEventIntervals(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervals(provider)

        finally:
            del root

    def IterateThroughEventIntervals(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.EventIntervals.Count:
            eventInterval: "ITimeToolEventInterval" = provider.EventIntervals[i]
            # All event intervals implement IAgCrdn interface which provides
            # information about the event interval's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(provider.EventIntervals[i], IAnalysisWorkbenchComponent)
            # Print the event interval's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventInterval.Type)

            i += 1

    # endregion

    # region IterateThroughEventIntervalCollections
    def test_IterateThroughEventIntervalCollections(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervalCollections(provider)

        finally:
            del root

    def IterateThroughEventIntervalCollections(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.EventIntervalCollections.Count:
            eventIntervalCollection: "ITimeToolEventIntervalCollection" = provider.EventIntervalCollections[i]
            # All event interval collections implement IAgCrdn interface which provides
            # information about the event interval collection's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.EventIntervalCollections[i], IAnalysisWorkbenchComponent
            )
            # Print the event interval collection's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventIntervalCollection.Type)

            i += 1

    # endregion

    # region IterateThroughEventIntervalLists
    def test_IterateThroughEventIntervalLists(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.IterateThroughEventIntervalLists(provider)

        finally:
            del root

    def IterateThroughEventIntervalLists(self, provider: "IAnalysisWorkbenchProvider"):
        i: int = 0
        while i < provider.EventIntervalLists.Count:
            eventIntervalList: "ITimeToolEventIntervalList" = provider.EventIntervalLists[i]
            # All event interval lists implement IAgCrdn interface which provides
            # information about the event interval list's instance and its type.
            crdn: "IAnalysisWorkbenchComponent" = clr.CastAs(
                provider.EventIntervalLists[i], IAnalysisWorkbenchComponent
            )
            # Print the event interval list's name and type to the standard output.
            Console.WriteLine("Name: {0}, type: {1}", crdn.Name, eventIntervalList.Type)

            i += 1

    # endregion

    # region CreateAngleRateVector
    def test_CreateAngleRateVector(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Vectors.Contains("myVector")))
        try:
            self.CreateAngleRateVector(provider)

        finally:
            provider.Vectors.Remove("myVector")
            del root

    def CreateAngleRateVector(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a vector.perpendicular to the plane in which the angle is defined.
        vector: "IVectorGeometryToolVectorAngleRate" = clr.Convert(
            provider.Vectors.Factory.Create(
                "myVector",
                "a vector.perpendicular to the plane in which the angle is defined.",
                AgECrdnVectorType.eCrdnVectorTypeAngleRate,
            ),
            IVectorGeometryToolVectorAngleRate,
        )

    # endregion

    # region IsVectorTypeSupported
    def test_IsVectorTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Vectors.Contains("myVector")))
        try:
            self.IsVectorTypeSupported(provider, AgECrdnVectorType.eCrdnVectorTypeAngleRate)

        finally:
            provider.Vectors.Remove("myVector")
            del root

    def IsVectorTypeSupported(self, provider: "IAnalysisWorkbenchProvider", vectorType: "AgECrdnVectorType"):
        if provider.Vectors.Factory.IsTypeSupported(vectorType):
            # Create a custom vector.
            vector: "IVectorGeometryToolVector" = provider.Vectors.Factory.Create("myVector", String.Empty, vectorType)

    # endregion

    # region CreateDisplacementVector
    def test_CreateDisplacementVector(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Points.Contains("Point1")))
        Assert.assertTrue((not provider.Points.Contains("Point2")))
        p: "IVectorGeometryToolPoint" = provider.Points.Factory.Create(
            "Point1", String.Empty, AgECrdnPointType.eCrdnPointTypeGlint
        )
        p2: "IVectorGeometryToolPoint" = provider.Points.Factory.Create(
            "Point2", String.Empty, AgECrdnPointType.eCrdnPointTypeGrazing
        )
        try:
            self.CreateDisplacementVector(provider, p, p2)

        finally:
            provider.Points.Remove("Point1")
            provider.Points.Remove("Point2")
            del root

    def CreateDisplacementVector(
        self,
        provider: "IAnalysisWorkbenchProvider",
        OriginPoint: "IVectorGeometryToolPoint",
        DestinationPoint: "IVectorGeometryToolPoint",
    ):
        # Create a displacement vector with two specified points
        vector: "IVectorGeometryToolVectorDisplacement" = provider.Vectors.Factory.CreateDisplacementVector(
            "VectorName", OriginPoint, DestinationPoint
        )

    # endregion

    # region CreateCrossProductVector
    def test_CreateCrossProductVector(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Vectors.Contains("Vector1")))
        Assert.assertTrue((not provider.Vectors.Contains("Vector2")))
        v1: "IVectorGeometryToolVector" = provider.Vectors.Factory.Create(
            "Vector1", "", AgECrdnVectorType.eCrdnVectorTypeLineOfNodes
        )
        v2: "IVectorGeometryToolVector" = provider.Vectors.Factory.Create(
            "Vector2", "", AgECrdnVectorType.eCrdnVectorTypeEccentricity
        )
        try:
            self.CreateCrossProductVector(provider, v1, v2)

        finally:
            provider.Vectors.Remove("Vector1")
            provider.Vectors.Remove("Vector2")
            del root

    def CreateCrossProductVector(
        self,
        provider: "IAnalysisWorkbenchProvider",
        VectorA: "IVectorGeometryToolVector",
        VectorB: "IVectorGeometryToolVector",
    ):
        # Create a vector defined as cross product of vectors A and B.
        vector: "IVectorGeometryToolVectorCross" = provider.Vectors.Factory.CreateCrossProductVector(
            "CrossVector", VectorA, VectorB
        )

    # endregion

    # region VectorContains
    def test_VectorContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.VectorContains(provider, "FlightPath")

        finally:
            del root

    def VectorContains(self, provider: "IAnalysisWorkbenchProvider", VectorName: str):
        if provider.Vectors.Contains(VectorName):
            Console.WriteLine("The vector {0} already exists!", VectorName)

    # endregion

    # region VectorRemove
    def test_VectorRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Vectors.Contains("SomeVector")))
        someVector: "IVectorGeometryToolVector" = provider.Vectors.Factory.Create(
            "SomeVector", String.Empty, AgECrdnVectorType.eCrdnVectorTypeDisplacement
        )
        try:
            self.VectorRemove(provider, (clr.Convert(someVector, IAnalysisWorkbenchComponent)).Name)

        finally:
            del root

    def VectorRemove(self, provider: "IAnalysisWorkbenchProvider", VectorName: str):
        if provider.Vectors.Contains(VectorName):
            provider.Vectors.Remove(VectorName)

    # endregion

    # region CreateAngleBetweenPlanes
    def test_CreateAngleBetweenPlanes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Angles.Contains("AngleName")))
        try:
            self.CreateAngleBetweenPlanes(provider)

        finally:
            provider.Angles.Remove("AngleName")
            del root

    def CreateAngleBetweenPlanes(self, provider: "IAnalysisWorkbenchProvider"):
        # Create an angle between two planes.
        angle: "IVectorGeometryToolAngleBetweenPlanes" = clr.Convert(
            provider.Angles.Factory.Create(
                "AngleName", "Angle from one plane to another.", AgECrdnAngleType.eCrdnAngleTypeBetweenPlanes
            ),
            IVectorGeometryToolAngleBetweenPlanes,
        )

    # endregion

    # region IsAngleTypeSupported
    def test_IsAngleTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Angles.Contains("MyAngle")))
        try:
            self.IsAngleTypeSupported(provider, AgECrdnAngleType.eCrdnAngleTypeBetweenPlanes)

        finally:
            provider.Angles.Remove("MyAngle")
            del root

    # Review: see the comments for the Vector
    def IsAngleTypeSupported(self, provider: "IAnalysisWorkbenchProvider", angleType: "AgECrdnAngleType"):
        if provider.Angles.Factory.IsTypeSupported(angleType):
            # Create an Angle with the supported Type
            angle: "IVectorGeometryToolAngle" = provider.Angles.Factory.Create("MyAngle", String.Empty, angleType)

    # endregion

    # region AngleContains
    def test_AngleContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.AngleContains(provider)

        finally:
            del root

    # Review: see the comments for the Angle
    def AngleContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Angles.Contains("AngleName"):
            Console.WriteLine('The angle "{0}" already exists!', "AngleName")

    # endregion

    # region AngleRemove
    def test_AngleRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Angles.Contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.Angles.Factory.Create(
            "AngleName", String.Empty, AgECrdnAngleType.eCrdnAngleTypeBetweenPlanes
        )
        try:
            self.AngleRemove(provider)

        finally:
            del root

    def AngleRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Angles.Contains("AngleName"):
            provider.Angles.Remove("AngleName")

    # endregion

    # region CreateNormalPlane
    def test_CreateNormalPlane(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Planes.Contains("PlaneName")))
        try:
            self.CreateNormalPlane(provider)

        finally:
            provider.Planes.Remove("PlaneName")
            del root

    def CreateNormalPlane(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a plane normal to vector.
        p: "IVectorGeometryToolPlaneNormal" = clr.Convert(
            provider.Planes.Factory.Create(
                "PlaneName", "A plane normal to vector.", AgECrdnPlaneType.eCrdnPlaneTypeNormal
            ),
            IVectorGeometryToolPlaneNormal,
        )

    # endregion

    # region IsPlaneTypeSupported
    def test_IsPlaneTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Planes.Contains("PlaneName")))
        try:
            self.IsPlaneTypeSupported(provider, AgECrdnPlaneType.eCrdnPlaneTypeNormal)

        finally:
            provider.Planes.Remove("PlaneName")
            del root

    def IsPlaneTypeSupported(self, provider: "IAnalysisWorkbenchProvider", planeType: "AgECrdnPlaneType"):
        if provider.Planes.Factory.IsTypeSupported(planeType):
            p: "IVectorGeometryToolPlane" = provider.Planes.Factory.Create("PlaneName", String.Empty, planeType)

    # endregion

    # region PlaneContains
    def test_PlaneContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.PlaneContains(provider)

        finally:
            del root

    def PlaneContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Planes.Contains("PlaneName"):
            Console.WriteLine('The plane "{0}" already exists!', "PlaneName")

    # endregion

    # region PlaneRemove
    def test_PlaneRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Planes.Contains("PlaneName")))
        plane: "IVectorGeometryToolPlane" = provider.Planes.Factory.Create(
            "PlaneName", String.Empty, AgECrdnPlaneType.eCrdnPlaneTypeNormal
        )
        try:
            self.PlaneRemove(provider)

        finally:
            del root

    def PlaneRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Planes.Contains("PlaneName"):
            provider.Planes.Remove("PlaneName")

    # endregion

    # region CreateAxesAlignedAndConstrained
    def test_CreateAxesAlignedAndConstrained(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Axes.Contains("AxesName")))
        try:
            self.CreateAxesAlignedAndConstrained(provider)

        finally:
            provider.Axes.Remove("AxesName")
            del root

    def CreateAxesAlignedAndConstrained(self, provider: "IAnalysisWorkbenchProvider"):
        axes: "IVectorGeometryToolAxesAlignedAndConstrained" = clr.Convert(
            provider.Axes.Factory.Create("AxesName", String.Empty, AgECrdnAxesType.eCrdnAxesTypeAlignedAndConstrained),
            IVectorGeometryToolAxesAlignedAndConstrained,
        )

    # endregion

    # region IsAxesTypeSupported
    def test_IsAxesTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Axes.Contains("AxesName")))
        try:
            self.IsAxesTypeSupported(provider, AgECrdnAxesType.eCrdnAxesTypeAlignedAndConstrained)

        finally:
            provider.Axes.Remove("AxesName")
            del root

    def IsAxesTypeSupported(self, provider: "IAnalysisWorkbenchProvider", axesType: "AgECrdnAxesType"):
        if provider.Axes.Factory.IsTypeSupported(axesType):
            axes: "IVectorGeometryToolAxes" = provider.Axes.Factory.Create("AxesName", String.Empty, axesType)

    # endregion

    # region AxesContains
    def test_AxesContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.AxesContains(provider)

        finally:
            del root

    def AxesContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Axes.Contains("AxesName"):
            Console.WriteLine('Axes "{0}" already exist!', "AxesName")

    # endregion

    # region AxesRemove
    def test_AxesRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Axes.Contains("AxesName")))
        axes: "IVectorGeometryToolAxes" = provider.Axes.Factory.Create(
            "AxesName", String.Empty, AgECrdnAxesType.eCrdnAxesTypeFixed
        )
        try:
            self.AxesRemove(provider)

        finally:
            del root

    def AxesRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Axes.Contains("AxesName"):
            provider.Axes.Remove("AxesName")

    # endregion

    # region CreatePointBPlane
    def test_CreatePointBPlane(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Points.Contains("PointName")))
        try:
            self.CreatePointBPlane(provider, "Earth")

        finally:
            provider.Points.Remove("PointName")
            del root

    def CreatePointBPlane(self, provider: "IAnalysisWorkbenchProvider", TargetBody: str):
        # Create a B-Plane point using selected target body
        point: "IVectorGeometryToolPointBPlane" = clr.Convert(
            provider.Points.Factory.Create("PointName", String.Empty, AgECrdnPointType.eCrdnPointTypeBPlane),
            IVectorGeometryToolPointBPlane,
        )
        point.TargetBody.SetPath(TargetBody)

    # endregion

    # region IsPointTypeSupported
    def test_IsPointTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Points.Contains("PointName")))
        try:
            self.IsPointTypeSupported(provider, AgECrdnPointType.eCrdnPointTypeBPlane)

        finally:
            provider.Points.Remove("PointName")
            del root

    def IsPointTypeSupported(self, provider: "IAnalysisWorkbenchProvider", PointType: "AgECrdnPointType"):
        if provider.Points.Factory.IsTypeSupported(PointType):
            point: "IVectorGeometryToolPoint" = provider.Points.Factory.Create("PointName", String.Empty, PointType)

    # endregion

    # region PointContains
    def test_PointContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.PointContains(provider)

        finally:
            del root

    def PointContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Points.Contains("PointName"):
            Console.WriteLine('The point "{0}" exists!', "PointName")

    # endregion

    # region PointRemove
    def test_PointRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Points.Contains("PointName")))
        point: "IVectorGeometryToolPoint" = provider.Points.Factory.Create(
            "PointName", String.Empty, AgECrdnPointType.eCrdnPointTypeFixedInSystem
        )
        try:
            self.PointRemove(provider)

        finally:
            del root

    def PointRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Points.Contains("PointName"):
            provider.Points.Remove("PointName")

    # endregion

    # region CreateSystemAssembled
    def test_CreateSystemAssembled(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Systems.Contains("SystemName")))
        try:
            self.CreateSystemAssembled(provider, provider.Points["Center"], provider.Axes["Body"])

        finally:
            provider.Systems.Remove("SystemName")
            del root

    def CreateSystemAssembled(
        self,
        provider: "IAnalysisWorkbenchProvider",
        OriginPoint: "IVectorGeometryToolPoint",
        ReferenceAxes: "IVectorGeometryToolAxes",
    ):
        system: "IVectorGeometryToolSystemAssembled" = clr.Convert(
            provider.Systems.Factory.Create("SystemName", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled),
            IVectorGeometryToolSystemAssembled,
        )
        # Set the system's origin point.
        system.OriginPoint.SetPoint(OriginPoint)
        # Set the system's reference axes.
        system.ReferenceAxes.SetAxes(ReferenceAxes)

    # endregion

    # region IsSystemTypeSupported
    def test_IsSystemTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Systems.Contains("SystemName")))
        try:
            self.IsSystemTypeSupported(provider, AgECrdnSystemType.eCrdnSystemTypeAssembled)

        finally:
            provider.Systems.Remove("SystemName")
            del root

    def IsSystemTypeSupported(self, provider: "IAnalysisWorkbenchProvider", SystemType: "AgECrdnSystemType"):
        if provider.Systems.Factory.IsTypeSupported(SystemType):
            # Create a System with supported Type
            system: "IVectorGeometryToolSystem" = provider.Systems.Factory.Create(
                "SystemName", String.Empty, SystemType
            )

    # endregion

    # region SystemContains
    def test_SystemContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.SystemContains(provider)

        finally:
            del root

    def SystemContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Systems.Contains("SystemName"):
            Console.WriteLine('The system "{0}" exists!', "SystemName")

    # endregion

    # region SystemRemove
    def test_SystemRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Systems.Contains("SystemName")))
        system: "IVectorGeometryToolSystem" = provider.Systems.Factory.Create(
            "SystemName", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.SystemRemove(provider)

        finally:
            del root

    def SystemRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Systems.Contains("SystemName"):
            provider.Systems.Remove("SystemName")

    # endregion

    # region CreateParameterSetAttitude
    def test_CreateParameterSetAttitude(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.ParameterSets.Contains("ParameterSetName")))
        try:
            self.CreateParameterSetAttitude(provider)

        finally:
            provider.ParameterSets.Remove("ParameterSetName")
            del root

    def CreateParameterSetAttitude(self, provider: "IAnalysisWorkbenchProvider"):
        # Create an attitude parameter set.
        parameterSet: "ICalculationToolParameterSetAttitude" = clr.Convert(
            provider.ParameterSets.Factory.Create(
                "ParameterSetName", "Attitude parameter set.", AgECrdnParameterSetType.eCrdnParameterSetTypeAttitude
            ),
            ICalculationToolParameterSetAttitude,
        )

    # endregion

    # region IsParameterSetTypeSupported
    def test_IsParameterSetTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.ParameterSets.Contains("MyParameterSet")))
        try:
            self.IsParameterSetTypeSupported(provider, AgECrdnParameterSetType.eCrdnParameterSetTypeAttitude)

        finally:
            provider.ParameterSets.Remove("MyParameterSet")
            del root

    def IsParameterSetTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", parameterSetType: "AgECrdnParameterSetType"
    ):
        if provider.ParameterSets.Factory.IsTypeSupported(parameterSetType):
            # Create a ParameterSet with the supported Type
            parameterSet: "ICalculationToolParameterSet" = provider.ParameterSets.Factory.Create(
                "MyParameterSet", String.Empty, parameterSetType
            )

    # endregion

    # region ParameterSetContains
    def test_ParameterSetContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.ParameterSetContains(provider)

        finally:
            del root

    def ParameterSetContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.ParameterSets.Contains("ParameterSetName"):
            Console.WriteLine('The parameter set "{0}" already exists!', "ParameterSetName")

    # endregion

    # region ParameterSetRemove
    def test_ParameterSetRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.ParameterSets.Contains("ParameterSetName")))
        parameterSet: "ICalculationToolParameterSet" = provider.ParameterSets.Factory.Create(
            "ParameterSetName", String.Empty, AgECrdnParameterSetType.eCrdnParameterSetTypeAttitude
        )
        try:
            self.ParameterSetRemove(provider)

        finally:
            del root

    def ParameterSetRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.ParameterSets.Contains("ParameterSetName"):
            provider.ParameterSets.Remove("ParameterSetName")

    # endregion

    # region CreateCalcScalarConstant
    def test_CreateCalcScalarConstant(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.CalcScalars.Contains("CalcScalarName")))
        try:
            self.CreateCalcScalarConstant(provider)

        finally:
            provider.CalcScalars.Remove("CalcScalarName")
            del root

    def CreateCalcScalarConstant(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a calc scalar constant.
        calcScalar: "ICalculationToolScalarConstant" = clr.Convert(
            provider.CalcScalars.Factory.Create(
                "CalcScalarName", "Calc scalar constant.", AgECrdnCalcScalarType.eCrdnCalcScalarTypeConstant
            ),
            ICalculationToolScalarConstant,
        )

    # endregion

    # region IsCalcScalarTypeSupported
    def test_IsCalcScalarTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.CalcScalars.Contains("MyCalcScalar")))
        try:
            self.IsCalcScalarTypeSupported(provider, AgECrdnCalcScalarType.eCrdnCalcScalarTypeConstant)

        finally:
            provider.CalcScalars.Remove("MyCalcScalar")
            del root

    def IsCalcScalarTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", calcScalarType: "AgECrdnCalcScalarType"
    ):
        if provider.CalcScalars.Factory.IsTypeSupported(calcScalarType):
            # Create a CalcScalar with the supported Type
            calcScalar: "ICalculationToolScalar" = provider.CalcScalars.Factory.Create(
                "MyCalcScalar", String.Empty, calcScalarType
            )

    # endregion

    # region CalcScalarContains
    def test_CalcScalarContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.CalcScalarContains(provider)

        finally:
            del root

    def CalcScalarContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.CalcScalars.Contains("CalcScalarName"):
            Console.WriteLine('The calc scalar "{0}" already exists!', "CalcScalarName")

    # endregion

    # region CalcScalarRemove
    def test_CalcScalarRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.CalcScalars.Contains("CalcScalarName")))
        calcScalar: "ICalculationToolScalar" = provider.CalcScalars.Factory.Create(
            "CalcScalarName", String.Empty, AgECrdnCalcScalarType.eCrdnCalcScalarTypeConstant
        )
        try:
            self.CalcScalarRemove(provider)

        finally:
            del root

    def CalcScalarRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.CalcScalars.Contains("CalcScalarName"):
            provider.CalcScalars.Remove("CalcScalarName")

    # endregion

    # region CreateConditionScalarBounds
    def test_CreateConditionScalarBounds(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Conditions.Contains("ConditionName")))
        try:
            self.CreateConditionScalarBounds(provider)

        finally:
            provider.Conditions.Remove("ConditionName")
            del root

    def CreateConditionScalarBounds(self, provider: "IAnalysisWorkbenchProvider"):
        # Create a condition from a scalar.
        condition: "ICalculationToolConditionScalarBounds" = clr.Convert(
            provider.Conditions.Factory.Create(
                "ConditionName", "Condition from a scalar.", AgECrdnConditionType.eCrdnConditionTypeScalarBounds
            ),
            ICalculationToolConditionScalarBounds,
        )

    # endregion

    # region IsConditionTypeSupported
    def test_IsConditionTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Conditions.Contains("MyCondition")))
        try:
            self.IsConditionTypeSupported(provider, AgECrdnConditionType.eCrdnConditionTypeScalarBounds)

        finally:
            provider.Conditions.Remove("MyCondition")
            del root

    def IsConditionTypeSupported(self, provider: "IAnalysisWorkbenchProvider", conditionType: "AgECrdnConditionType"):
        if provider.Conditions.Factory.IsTypeSupported(conditionType):
            # Create a Condition with the supported Type
            condition: "ICalculationToolCondition" = provider.Conditions.Factory.Create(
                "MyCondition", String.Empty, conditionType
            )

    # endregion

    # region ConditionContains
    def test_ConditionContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.ConditionContains(provider)

        finally:
            del root

    def ConditionContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Conditions.Contains("ConditionName"):
            Console.WriteLine('The condition "{0}" already exists!', "ConditionName")

    # endregion

    # region ConditionRemove
    def test_ConditionRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Conditions.Contains("ConditionName")))
        condition: "ICalculationToolCondition" = provider.Conditions.Factory.Create(
            "ConditionName", String.Empty, AgECrdnConditionType.eCrdnConditionTypeScalarBounds
        )
        try:
            self.ConditionRemove(provider)

        finally:
            del root

    def ConditionRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Conditions.Contains("ConditionName"):
            provider.Conditions.Remove("ConditionName")

    # endregion

    # region IsEventTypeSupported
    def test_IsEventTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Events.Contains("MyEvent")))
        try:
            self.IsEventTypeSupported(provider, AgECrdnEventType.eCrdnEventTypeEpoch)

        finally:
            provider.Events.Remove("MyEvent")
            del root

    def IsEventTypeSupported(self, provider: "IAnalysisWorkbenchProvider", eventType: "AgECrdnEventType"):
        if provider.Events.Factory.IsTypeSupported(eventType):
            # Create an Event with the supported Type
            event: "ITimeToolEvent" = provider.Events.Factory.Create("MyEvent", String.Empty, eventType)

    # endregion

    # region EventContains
    def test_EventContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EventContains(provider)

        finally:
            del root

    def EventContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Events.Contains("EventName"):
            Console.WriteLine('The event "{0}" already exists!', "EventName")

    # endregion

    # region EventRemove
    def test_EventRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Events.Contains("EventName")))
        event: "ITimeToolEvent" = provider.Events.Factory.Create(
            "EventName", String.Empty, AgECrdnEventType.eCrdnEventTypeEpoch
        )
        try:
            self.EventRemove(provider)

        finally:
            del root

    def EventRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.Events.Contains("EventName"):
            provider.Events.Remove("EventName")

    # endregion

    # region IsEventArrayTypeSupported
    def test_IsEventArrayTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventArrays.Contains("MyEventArray")))
        try:
            self.IsEventArrayTypeSupported(provider, AgECrdnEventArrayType.eCrdnEventArrayTypeConditionCrossings)

        finally:
            provider.EventArrays.Remove("MyEventArray")
            del root

    def IsEventArrayTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventArrayType: "AgECrdnEventArrayType"
    ):
        if provider.EventArrays.Factory.IsTypeSupported(eventArrayType):
            # Create an EventArray with the supported Type
            eventArray: "ITimeToolEventArray" = provider.EventArrays.Factory.Create(
                "MyEventArray", String.Empty, eventArrayType
            )

    # endregion

    # region EventArrayContains
    def test_EventArrayContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EventArrayContains(provider)

        finally:
            del root

    def EventArrayContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventArrays.Contains("EventArrayName"):
            Console.WriteLine('The event array "{0}" already exists!', "EventArrayName")

    # endregion

    # region EventArrayRemove
    def test_EventArrayRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventArrays.Contains("EventArrayName")))
        eventArray: "ITimeToolEventArray" = provider.EventArrays.Factory.Create(
            "EventArrayName", String.Empty, AgECrdnEventArrayType.eCrdnEventArrayTypeConditionCrossings
        )
        try:
            self.EventArrayRemove(provider)

        finally:
            del root

    def EventArrayRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventArrays.Contains("EventArrayName"):
            provider.EventArrays.Remove("EventArrayName")

    # endregion

    # region IsEventIntervalTypeSupported
    def test_IsEventIntervalTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventIntervals.Contains("MyEventInterval")))
        try:
            self.IsEventIntervalTypeSupported(provider, AgECrdnEventIntervalType.eCrdnEventIntervalTypeFixed)

        finally:
            provider.EventIntervals.Remove("MyEventInterval")
            del root

    def IsEventIntervalTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventIntervalType: "AgECrdnEventIntervalType"
    ):
        if provider.EventIntervals.Factory.IsTypeSupported(eventIntervalType):
            # Create an EventInterval with the supported Type
            eventInterval: "ITimeToolEventInterval" = provider.EventIntervals.Factory.Create(
                "MyEventInterval", String.Empty, eventIntervalType
            )

    # endregion

    # region EventIntervalContains
    def test_EventIntervalContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EventIntervalContains(provider)

        finally:
            del root

    def EventIntervalContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventIntervals.Contains("EventIntervalName"):
            Console.WriteLine('The event interval "{0}" already exists!', "EventIntervalName")

    # endregion

    # region EventIntervalRemove
    def test_EventIntervalRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventIntervals.Contains("EventIntervalName")))
        eventInterval: "ITimeToolEventInterval" = provider.EventIntervals.Factory.Create(
            "EventIntervalName", String.Empty, AgECrdnEventIntervalType.eCrdnEventIntervalTypeFixed
        )
        try:
            self.EventIntervalRemove(provider)

        finally:
            del root

    def EventIntervalRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventIntervals.Contains("EventIntervalName"):
            provider.EventIntervals.Remove("EventIntervalName")

    # endregion

    # region IsEventIntervalCollectionTypeSupported
    def test_IsEventIntervalCollectionTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventIntervalCollections.Contains("MyEventIntervalCollection")))
        try:
            self.IsEventIntervalCollectionTypeSupported(
                provider, AgECrdnEventIntervalCollectionType.eCrdnEventIntervalCollectionTypeLighting
            )

        finally:
            provider.EventIntervalCollections.Remove("MyEventIntervalCollection")
            del root

    def IsEventIntervalCollectionTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventIntervalCollectionType: "AgECrdnEventIntervalCollectionType"
    ):
        if provider.EventIntervalCollections.Factory.IsTypeSupported(eventIntervalCollectionType):
            # Create an EventIntervalCollection with the supported Type
            eventIntervalCollection: "ITimeToolEventIntervalCollection" = (
                provider.EventIntervalCollections.Factory.Create(
                    "MyEventIntervalCollection", String.Empty, eventIntervalCollectionType
                )
            )

    # endregion

    # region EventIntervalCollectionContains
    def test_EventIntervalCollectionContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EventIntervalCollectionContains(provider)

        finally:
            del root

    def EventIntervalCollectionContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventIntervalCollections.Contains("EventIntervalCollectionName"):
            Console.WriteLine('The event interval collection "{0}" already exists!', "EventIntervalCollectionName")

    # endregion

    # region EventIntervalCollectionRemove
    def test_EventIntervalCollectionRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventIntervalCollections.Contains("EventIntervalCollectionName")))
        eventIntervalCollection: "ITimeToolEventIntervalCollection" = provider.EventIntervalCollections.Factory.Create(
            "EventIntervalCollectionName",
            String.Empty,
            AgECrdnEventIntervalCollectionType.eCrdnEventIntervalCollectionTypeLighting,
        )
        try:
            self.EventIntervalCollectionRemove(provider)

        finally:
            del root

    def EventIntervalCollectionRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventIntervalCollections.Contains("EventIntervalCollectionName"):
            provider.EventIntervalCollections.Remove("EventIntervalCollectionName")

    # endregion

    # region IsEventIntervalListTypeSupported
    def test_IsEventIntervalListTypeSupported(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventIntervalLists.Contains("MyEventIntervalList")))
        try:
            self.IsEventIntervalListTypeSupported(
                provider, AgECrdnEventIntervalListType.eCrdnEventIntervalListTypeCondition
            )

        finally:
            provider.EventIntervalLists.Remove("MyEventIntervalList")
            del root

    def IsEventIntervalListTypeSupported(
        self, provider: "IAnalysisWorkbenchProvider", eventIntervalListType: "AgECrdnEventIntervalListType"
    ):
        if provider.EventIntervalLists.Factory.IsTypeSupported(eventIntervalListType):
            # Create an EventIntervalList with the supported Type
            eventIntervalList: "ITimeToolEventIntervalList" = provider.EventIntervalLists.Factory.Create(
                "MyEventIntervalList", String.Empty, eventIntervalListType
            )

    # endregion

    # region EventIntervalListContains
    def test_EventIntervalListContains(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            self.EventIntervalListContains(provider)

        finally:
            del root

    def EventIntervalListContains(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventIntervalLists.Contains("EventIntervalListName"):
            Console.WriteLine('The event interval list "{0}" already exists!', "EventIntervalListName")

    # endregion

    # region EventIntervalListRemove
    def test_EventIntervalListRemove(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.EventIntervalLists.Contains("EventIntervalListName")))
        eventIntervalList: "ITimeToolEventIntervalList" = provider.EventIntervalLists.Factory.Create(
            "EventIntervalListName", String.Empty, AgECrdnEventIntervalListType.eCrdnEventIntervalListTypeCondition
        )
        try:
            self.EventIntervalListRemove(provider)

        finally:
            del root

    def EventIntervalListRemove(self, provider: "IAnalysisWorkbenchProvider"):
        if provider.EventIntervalLists.Contains("EventIntervalListName"):
            provider.EventIntervalLists.Remove("EventIntervalListName")

    # endregion

    # region Angle.FindAngle
    def test_FindAngle(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Angles.Contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.Angles.Factory.Create(
            "AngleName", String.Empty, AgECrdnAngleType.eCrdnAngleTypeBetweenVectors
        )
        try:
            self.FindAngle(angle)

        finally:
            provider.Angles.Remove("AngleName")
            del root

    def FindAngle(self, angle: "IVectorGeometryToolAngle"):
        result: "IVectorGeometryToolAngleFindAngleResult" = angle.FindAngle(0)
        if result.IsValid:
            Console.WriteLine("Angle: {0}", result.Angle)

    # endregion

    # region Angle.FindAngleAndRate
    def test_FindAngleAndRate(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Angles.Contains("AngleName")))
        angle: "IVectorGeometryToolAngle" = provider.Angles.Factory.Create(
            "AngleName", String.Empty, AgECrdnAngleType.eCrdnAngleTypeBetweenVectors
        )
        try:
            self.FindAngleAndRate(angle)

        finally:
            provider.Angles.Remove("AngleName")
            del root

    def FindAngleAndRate(self, angle: "IVectorGeometryToolAngle"):
        result: "IVectorGeometryToolAngleFindAngleWithRateResult" = angle.FindAngleWithRate(0)
        if result.IsValid:
            Console.WriteLine("Angle: {0}, Rate: {1}", result.Angle, result.AngleRate)

    # endregion

    # region Axes.FindInAxes
    def test_FindAxesInEarthFixed(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Axes.Contains("AxesName")))
        axes: "IVectorGeometryToolAxes" = provider.Axes.Factory.Create(
            "AxesName", String.Empty, AgECrdnAxesType.eCrdnAxesTypeFixed
        )
        try:
            self.FindAxesInEarthFixed(provider, axes)

        finally:
            provider.Axes.Remove("AxesName")
            del root

    def FindAxesInEarthFixed(self, provider: "IAnalysisWorkbenchProvider", axes: "IVectorGeometryToolAxes"):
        result: "IVectorGeometryToolAxesFindInAxesResult" = axes.FindInAxes(0, provider.WellKnownAxes.Earth.Fixed)
        if result.IsValid:
            angles: "ansys.stk.core.stkutil.IOrientationEulerAngles" = None
            angles = clr.Convert(result.Orientation.ConvertTo(AgEOrientationType.eEulerAngles), IOrientationEulerAngles)
            Console.WriteLine(
                "Euler Angles [A,B,C,SEQ] => [{1}, {1}, {2}, {3}]", angles.A, angles.B, angles.C, angles.Sequence
            )

    # endregion

    # region Axes.Transform
    def test_AxesTransformEarthFixed(self):
        sat: "IStkObject" = TestBase.Application.CurrentScenario.Children["Satellite1"]
        self.AxesTransformEarthFixed(sat)

    def AxesTransformEarthFixed(self, sat: "IStkObject"):
        # Get the satellite's ICRF cartesian position at 180 EpSec using the data provider interface
        numEpSec: int = 180
        dpGroup: "IDataProviderGroup" = clr.CastAs(sat.DataProviders["Cartesian Position"], IDataProviderGroup)
        elements = ["x", "y", "z"]
        dp: "IDataProviderTimeVarying" = clr.CastAs(dpGroup.Group["ICRF"], IDataProviderTimeVarying)
        dpResult: "IDataProviderResult" = dp.ExecElements(numEpSec, numEpSec, 60, elements)
        xICRF: float = float(dpResult.DataSets[0].GetValues()[0])
        yICRF: float = float(dpResult.DataSets[1].GetValues()[0])
        zICRF: float = float(dpResult.DataSets[2].GetValues()[0])

        # Create a vector using the ICRF coordinates
        axesICRF: "IVectorGeometryToolAxes" = sat.Vgt.WellKnownAxes.Earth.ICRF
        vectorICRF: "ICartesian3Vector" = TestBase.Application.ConversionUtility.NewCartesian3Vector()
        vectorICRF.Set(xICRF, yICRF, zICRF)

        # Use the Transform method to transform ICRF to Fixed
        axesFixed: "IVectorGeometryToolAxes" = sat.Vgt.WellKnownAxes.Earth.Fixed
        result: "IVectorGeometryToolAxesTransformResult" = axesICRF.Transform(numEpSec, axesFixed, vectorICRF)

        # Get the Fixed coordinates
        xFixed: float = result.Vector.X
        yFixed: float = result.Vector.Y
        zFixed: float = result.Vector.Z

    # endregion

    # region Axes.TransformWithRate
    def test_AxesTransformWithRateEarthFixed(self):
        sat: "IStkObject" = TestBase.Application.CurrentScenario.Children["Satellite1"]
        self.AxesTransformWithRateEarthFixed(sat)

    def AxesTransformWithRateEarthFixed(self, sat: "IStkObject"):
        numEpSec: int = 180

        # Get the satellite's ICRF cartesian position at 180 EpSec using the data provider interface
        dpGroup: "IDataProviderGroup" = clr.CastAs(sat.DataProviders["Cartesian Position"], IDataProviderGroup)
        elements = ["x", "y", "z"]
        dp: "IDataProviderTimeVarying" = clr.CastAs(dpGroup.Group["ICRF"], IDataProviderTimeVarying)
        dpResult: "IDataProviderResult" = dp.ExecElements(numEpSec, numEpSec, 60, elements)
        xICRF: float = float(dpResult.DataSets[0].GetValues()[0])
        yICRF: float = float(dpResult.DataSets[1].GetValues()[0])
        zICRF: float = float(dpResult.DataSets[2].GetValues()[0])

        # Get the satellite's ICRF cartesian velocity at 180 EpSec using the data provider interface
        dpGroup = clr.CastAs(sat.DataProviders["Cartesian Velocity"], IDataProviderGroup)
        dp = clr.CastAs(dpGroup.Group["ICRF"], IDataProviderTimeVarying)
        dpResult = dp.ExecElements(numEpSec, numEpSec, 60, elements)
        xvelICRF: float = float(dpResult.DataSets[0].GetValues()[0])
        yvelICRF: float = float(dpResult.DataSets[1].GetValues()[0])
        zvelICRF: float = float(dpResult.DataSets[2].GetValues()[0])

        # Create a position vector using the ICRF coordinates
        axesICRF: "IVectorGeometryToolAxes" = sat.Vgt.WellKnownAxes.Earth.ICRF
        vectorICRF: "ICartesian3Vector" = TestBase.Application.ConversionUtility.NewCartesian3Vector()
        vectorICRF.Set(xICRF, yICRF, zICRF)

        # Create a velocity vector using the ICRF coordinates
        vectorvelICRF: "ICartesian3Vector" = TestBase.Application.ConversionUtility.NewCartesian3Vector()
        vectorvelICRF.Set(xvelICRF, yvelICRF, zvelICRF)

        # Use the TransformWithRate method to transform ICRF to Fixed
        axesFixed: "IVectorGeometryToolAxes" = sat.Vgt.WellKnownAxes.Earth.Fixed
        result: "IVectorGeometryToolAxesTransformWithRateResult" = axesICRF.TransformWithRate(
            numEpSec, axesFixed, vectorICRF, vectorvelICRF
        )

        # Get the Fixed position and velocity coordinates
        xFixed: float = result.Vector.X
        yFixed: float = result.Vector.Y
        zFixed: float = result.Vector.Z
        xvelFixed: float = result.Velocity.X
        yvelFixed: float = result.Velocity.Y
        zvelFixed: float = result.Velocity.Z

    # endregion

    # region Point.LocateInEarthFixedSystem
    def test_PointLocateInEarthFixedSystem(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Points.Contains("PointName")))
        point: "IVectorGeometryToolPoint" = provider.Points.Factory.Create(
            "PointName", String.Empty, AgECrdnPointType.eCrdnPointTypeFixedInSystem
        )
        try:
            self.PointLocateInEarthFixedSystem(provider, point)

        finally:
            provider.Points.Remove("PointName")
            del root

    def PointLocateInEarthFixedSystem(self, provider: "IAnalysisWorkbenchProvider", point: "IVectorGeometryToolPoint"):
        result: "IVectorGeometryToolPointLocateInSystemResult" = point.LocateInSystem(
            0, provider.WellKnownSystems.Earth.Fixed
        )
        if result.IsValid:
            Console.WriteLine(
                "The position of the point in Earth's Fixed reference frame: {0},{1},{2}",
                result.Position.X,
                result.Position.Y,
                result.Position.Z,
            )

    # endregion

    # region Vector.VectorFindInEarthFixedAxes
    def test_VectorFindInEarthFixedAxes(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        Assert.assertTrue((not provider.Vectors.Contains("VectorName")))
        vector: "IVectorGeometryToolVector" = provider.Vectors.Factory.Create(
            "PointName", String.Empty, AgECrdnVectorType.eCrdnVectorTypeDisplacement
        )
        try:
            self.VectorFindInEarthFixedAxes(provider, vector)

        finally:
            provider.Points.Remove("PointName")
            del root

    def VectorFindInEarthFixedAxes(self, provider: "IAnalysisWorkbenchProvider", vector: "IVectorGeometryToolVector"):
        result: "IVectorGeometryToolVectorFindInAxesResult" = vector.FindInAxes(0, provider.WellKnownAxes.Earth.Fixed)
        if result.IsValid:
            Console.WriteLine(
                "Vector in the Earth's Fixed axes (x,y,z) => {0},{1},{2}",
                result.Vector.X,
                result.Vector.Y,
                result.Vector.Z,
            )

    # endregion

    # region Axes.AnonymousFixed
    def test_AxesAnonymousFixed(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        try:
            vector: "ICartesian3Vector" = TestBase.Application.ConversionUtility.NewCartesian3Vector()
            self.AxesAnonymousFixed(provider)

        finally:
            del root

    def AxesAnonymousFixed(self, provider: "IAnalysisWorkbenchProvider"):
        ecfAxes: "IVectorGeometryToolAxes" = provider.WellKnownAxes.Earth.Fixed
        axesFixed: "IVectorGeometryToolAxesFixed" = provider.Axes.CommonTasks.CreateFixed(ecfAxes)

    # endregion

    # region Axes.CreateTopocentricAxesEulerAngles
    def test_AxesCreateTopocentricAxesEulerAngles(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        facility: "IFacility" = clr.CastAs(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            self.AxesCreateTopocentricAxesEulerAngles(provider, facility)

        finally:
            del root

    def AxesCreateTopocentricAxesEulerAngles(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0

        (lat, lon, alt) = facility.Position.QueryPlanetodetic()
        origin: "IVectorGeometryToolPointFixedInSystem" = provider.Points.CommonTasks.CreateFixedInSystemCartographic(
            provider.Systems["Fixed"], lat, lon, alt
        )
        eastNorthUp: "IVectorGeometryToolAxesFixed" = provider.Axes.CommonTasks.CreateTopocentricAxesEulerAngles(
            clr.Convert(origin, IVectorGeometryToolPoint), AgEEulerOrientationSequence.e321, 90.0, 0.0, 0.0
        )

    # endregion

    # region Axes.CreateTopocentricAxesQuaternion
    def test_AxesCreateTopocentricAxesQuaternion(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        facility: "IFacility" = clr.CastAs(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            self.AxesCreateTopocentricAxesQuaternion(provider, facility)

        finally:
            del root

    def AxesCreateTopocentricAxesQuaternion(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0

        (lat, lon, alt) = facility.Position.QueryPlanetodetic()
        origin: "IVectorGeometryToolPointFixedInSystem" = provider.Points.CommonTasks.CreateFixedInSystemCartographic(
            provider.Systems["Fixed"], lat, lon, alt
        )
        eastNorthUp: "IVectorGeometryToolAxesFixed" = provider.Axes.CommonTasks.CreateTopocentricAxesQuaternion(
            clr.Convert(origin, IVectorGeometryToolPoint), 0.0, 0.0, 0.0, 1.0
        )

    # endregion

    # region Systems.CreateAssembled
    def test_SystemsCreateAssembled(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        facility: "IFacility" = clr.CastAs(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            self.SystemsCreateAssembled(provider, facility)

        finally:
            del root

    def SystemsCreateAssembled(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        systemAssembled: "IVectorGeometryToolSystemAssembled" = provider.Systems.CommonTasks.CreateAssembled(
            (clr.Convert(facility, IStkObject)).Vgt.Points["Center"], provider.Axes["Fixed"]
        )

    # endregion

    # region Systems.CreateEastNorthUpCartographic
    def test_SystemsCreateEastNorthUpCartographic(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        facility: "IFacility" = clr.CastAs(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CurrentScenario.Children["Facility1"].Vgt
        try:
            self.SystemsCreateEastNorthUpCartographic(provider, facility)

        finally:
            del root

    def SystemsCreateEastNorthUpCartographic(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0
        (lat, lon, alt) = facility.Position.QueryPlanetodetic()
        systemAssembled: "IVectorGeometryToolSystemAssembled" = (
            provider.Systems.CommonTasks.CreateEastNorthUpCartographic(lat, lon, alt)
        )

    # endregion

    # region Point.CreateFixedInSystemCartographic
    def test_PointCreateFixedInSystemCartographic(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        facility: "IFacility" = clr.CastAs(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            self.PointCreateFixedInSystemCartographic(provider, facility)

        finally:
            del root

    def PointCreateFixedInSystemCartographic(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        lat: typing.Any = 0
        lon: typing.Any = 0

        alt: float = 0
        (lat, lon, alt) = facility.Position.QueryPlanetodetic()
        origin: "IVectorGeometryToolPointFixedInSystem" = provider.Points.CommonTasks.CreateFixedInSystemCartographic(
            provider.Systems["Fixed"], lat, lon, alt
        )

    # endregion

    # region Point.CreateFixedInSystemCartesian
    def test_PointCreateFixedInSystemCartesian(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        facility: "IFacility" = clr.CastAs(TestBase.Application.CurrentScenario.Children["Facility1"], IFacility)
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            self.PointCreateFixedInSystemCartesian(provider, facility)

        finally:
            del root

    def PointCreateFixedInSystemCartesian(self, provider: "IAnalysisWorkbenchProvider", facility: "IFacility"):
        X: float = 0
        Y: float = 0
        Z: float = 0

        (X, Y, Z) = facility.Position.QueryCartesian()
        origin: "IVectorGeometryToolPointFixedInSystem" = provider.Points.CommonTasks.CreateFixedInSystemCartesian(
            provider.Systems["Fixed"], X, Y, Z
        )

    # endregion

    # region Duplicate
    def test_Duplicate(self):
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            provider.Points.Remove("OriginalPoint")
            self.Duplicate(provider)

        finally:
            pass

    def Duplicate(self, provider: "IAnalysisWorkbenchProvider"):
        point: "IVectorGeometryToolPoint" = provider.Points.Factory.Create(
            "OriginalPoint", "description", AgECrdnPointType.eCrdnPointTypeAtTimeInstant
        )
        duplicate: "IAnalysisWorkbenchComponent" = (clr.Convert(point, IAnalysisWorkbenchComponent)).Duplicate(
            "DuplicatePoint", "description"
        )

    # endregion

    # region AnonymousDuplicate
    def test_AnonymousDuplicate(self):
        provider: "IAnalysisWorkbenchProvider" = TestBase.Application.CentralBodies["Earth"].Vgt
        try:
            provider.Points.Remove("OriginalPoint")
            self.AnonymousDuplicate(provider)

        finally:
            pass

    def AnonymousDuplicate(self, provider: "IAnalysisWorkbenchProvider"):
        point: "IVectorGeometryToolPoint" = provider.Points.Factory.Create(
            "OriginalPoint", "description", AgECrdnPointType.eCrdnPointTypeAtTimeInstant
        )
        anonymousDuplicate: "IAnalysisWorkbenchComponent" = (
            clr.Convert(point, IAnalysisWorkbenchComponent)
        ).AnonymousDuplicate()

    # endregion

    # region GetEmbeddedComponent
    def test_GetEmbeddedComponent(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.Systems.Factory.Create(
            "mySystem", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.GetEmbeddedComponent(clr.Convert(system, IAnalysisWorkbenchComponent))

        finally:
            provider.Systems.Remove("mySystem")
            del root

    def GetEmbeddedComponent(self, crdn: "IAnalysisWorkbenchComponent"):
        if crdn.EmbeddedComponents.Contains("Origin"):
            embeddedComponent: "IAnalysisWorkbenchComponent" = crdn.EmbeddedComponents["Origin"]

    # endregion

    # region EnumerateThroughEmbeddedComponents
    def test_EnumerateThroughEmbeddedComponents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.Systems.Factory.Create(
            "mySystem", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.EnumerateThroughEmbeddedComponents(clr.Convert(system, IAnalysisWorkbenchComponent))

        finally:
            provider.Systems.Remove("mySystem")
            del root

    def EnumerateThroughEmbeddedComponents(self, crdn: "IAnalysisWorkbenchComponent"):
        embeddedComponent: "IAnalysisWorkbenchComponent"
        for embeddedComponent in crdn.EmbeddedComponents:
            Console.WriteLine("Name: {0}, kind: {1}", embeddedComponent.Name, embeddedComponent.Kind)

    # endregion

    # region IterateThroughEmbeddedComponents
    def test_IterateThroughEmbeddedComponents(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        system: "IVectorGeometryToolSystem" = provider.Systems.Factory.Create(
            "mySystem", String.Empty, AgECrdnSystemType.eCrdnSystemTypeAssembled
        )
        try:
            self.IterateThroughEmbeddedComponents(clr.Convert(system, IAnalysisWorkbenchComponent))

        finally:
            provider.Systems.Remove("mySystem")
            del root

    def IterateThroughEmbeddedComponents(self, crdn: "IAnalysisWorkbenchComponent"):
        i: int = 0
        while i < crdn.EmbeddedComponents.Count:
            embeddedComponent: "IAnalysisWorkbenchComponent" = crdn.EmbeddedComponents[i]
            Console.WriteLine("Name: {0}, kind: {1}", embeddedComponent.Name, embeddedComponent.Kind)

            i += 1

    # endregion

    # region AngleHasCyclicDependency
    def test_AngleHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        angleRate: "IVectorGeometryToolVectorAngleRate" = clr.CastAs(
            provider.Vectors.Factory.Create("DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeAngleRate),
            IVectorGeometryToolVectorAngleRate,
        )
        angle: "IVectorGeometryToolAngle" = provider.Angles["VelocityAzimuth"]
        try:
            self.AngleHasCyclicDependency(angleRate.Angle, angle)

        finally:
            provider.Vectors.Remove("DependencyTest")
            del root

    def AngleHasCyclicDependency(self, angleRefTo: "IVectorGeometryToolAngleRefTo", angle: "IVectorGeometryToolAngle"):
        if angleRefTo.HasCyclicDependency(angle):
            Console.WriteLine(
                "The angle {0} has a cyclic dependency on angle {1}.",
                (clr.Convert(angleRefTo.GetAngle(), IAnalysisWorkbenchComponent)).Name,
                (clr.Convert(angle, IAnalysisWorkbenchComponent)).Name,
            )

    # endregion

    # region AxesHasCyclicDependency
    def test_AxesHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        angVel: "IVectorGeometryToolVectorAngularVelocity" = clr.CastAs(
            provider.Vectors.Factory.Create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeAngularVelocity
            ),
            IVectorGeometryToolVectorAngularVelocity,
        )
        axes: "IVectorGeometryToolAxes" = provider.Axes["Body"]
        try:
            self.AxesHasCyclicDependency(angVel.Axes, axes)

        finally:
            provider.Vectors.Remove("DependencyTest")
            del root

    def AxesHasCyclicDependency(self, axesRefTo: "IVectorGeometryToolAxesRefTo", axes: "IVectorGeometryToolAxes"):
        if axesRefTo.HasCyclicDependency(axes):
            Console.WriteLine(
                "The axes {0} has a cyclic dependency on axes {1}.",
                (clr.Convert(axesRefTo.GetAxes(), IAnalysisWorkbenchComponent)).Name,
                (clr.Convert(axes, IAnalysisWorkbenchComponent)).Name,
            )

    # endregion

    # region PlaneHasCyclicDependency
    def test_PlaneHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        twoPlane: "IVectorGeometryToolVectorTwoPlanesIntersection" = clr.CastAs(
            provider.Vectors.Factory.Create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeTwoPlanesIntersection
            ),
            IVectorGeometryToolVectorTwoPlanesIntersection,
        )
        plane: "IVectorGeometryToolPlane" = provider.Planes["BodyXY"]
        try:
            self.PlaneHasCyclicDependency(twoPlane.PlaneA, plane)

        finally:
            provider.Vectors.Remove("DependencyTest")
            del root

    def PlaneHasCyclicDependency(self, planeRefTo: "IVectorGeometryToolPlaneRefTo", plane: "IVectorGeometryToolPlane"):
        if planeRefTo.HasCyclicDependency(plane):
            Console.WriteLine(
                "The plane {0} has a cyclic dependency on plane {1}.",
                (clr.Convert(planeRefTo.GetPlane(), IAnalysisWorkbenchComponent)).Name,
                (clr.Convert(plane, IAnalysisWorkbenchComponent)).Name,
            )

    # endregion

    # region PointHasCyclicDependency
    def test_PointHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        apoapsis: "IVectorGeometryToolVectorApoapsis" = clr.CastAs(
            provider.Vectors.Factory.Create("DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeApoapsis),
            IVectorGeometryToolVectorApoapsis,
        )
        point: "IVectorGeometryToolPoint" = provider.Points["Center"]
        try:
            self.PointHasCyclicDependency(apoapsis.ReferencePoint, point)

        finally:
            provider.Vectors.Remove("DependencyTest")
            del root

    def PointHasCyclicDependency(self, pointRefTo: "IVectorGeometryToolPointRefTo", point: "IVectorGeometryToolPoint"):
        if pointRefTo.HasCyclicDependency(point):
            Console.WriteLine(
                "The point {0} has a cyclic dependency on point {1}.",
                (clr.Convert(pointRefTo.GetPoint(), IAnalysisWorkbenchComponent)).Name,
                (clr.Convert(point, IAnalysisWorkbenchComponent)).Name,
            )

    # endregion

    # region SystemHasCyclicDependency
    def test_SystemHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        displacement: "IVectorGeometryToolVectorDisplacement" = clr.CastAs(
            provider.Vectors.Factory.Create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeDisplacement
            ),
            IVectorGeometryToolVectorDisplacement,
        )
        displacement.Apparent = True
        system: "IVectorGeometryToolSystem" = provider.Systems["Body"]
        try:
            self.SystemHasCyclicDependency(displacement.ReferenceSystem, system)

        finally:
            provider.Vectors.Remove("DependencyTest")
            del root

    def SystemHasCyclicDependency(
        self, systemRefTo: "IVectorGeometryToolSystemRefTo", system: "IVectorGeometryToolSystem"
    ):
        if systemRefTo.HasCyclicDependency(system):
            Console.WriteLine(
                "The system {0} has a cyclic dependency on system {1}.",
                (clr.Convert(systemRefTo.GetSystem(), IAnalysisWorkbenchComponent)).Name,
                (clr.Convert(system, IAnalysisWorkbenchComponent)).Name,
            )

    # endregion

    # region VectorHasCyclicDependency
    def test_VectorHasCyclicDependency(self):
        root: "IAnalysisWorkbenchRoot" = TestBase.Application.VgtRoot
        provider: "IAnalysisWorkbenchProvider" = root.GetProvider("Satellite/Satellite1")
        reflection: "IVectorGeometryToolVectorReflection" = clr.CastAs(
            provider.Vectors.Factory.Create(
                "DependencyTest", String.Empty, AgECrdnVectorType.eCrdnVectorTypeReflection
            ),
            IVectorGeometryToolVectorReflection,
        )
        vector: "IVectorGeometryToolVector" = provider.Vectors["Earth"]
        try:
            self.VectorHasCyclicDependency(reflection.NormalVector, vector)

        finally:
            provider.Vectors.Remove("DependencyTest")
            del root

    def VectorHasCyclicDependency(
        self, vectorRefTo: "IVectorGeometryToolVectorRefTo", vector: "IVectorGeometryToolVector"
    ):
        if vectorRefTo.HasCyclicDependency(vector):
            Console.WriteLine(
                "The vector {0} has a cyclic dependency on vector {1}.",
                (clr.Convert(vectorRefTo.GetVector(), IAnalysisWorkbenchComponent)).Name,
                (clr.Convert(vector, IAnalysisWorkbenchComponent)).Name,
            )

    # endregion
