from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class SGP4(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SGP4, self).__init__(*args, **kwargs)

    m_Object: "ISatellite" = None
    m_DefaultName: str = "MySatellite"

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        SGP4.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, SGP4.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, SGP4.m_DefaultName)
        SGP4.m_Object = None

    # endregion

    # region ConfigureSGP4WithFileSource
    def test_ConfigureSGP4WithFileSource(self):
        SGP4.m_Object.SetPropagatorType(AgEVePropagatorType.ePropagatorSGP4)

        sgp4: "IVehiclePropagatorSGP4" = clr.CastAs(SGP4.m_Object.Propagator, IVehiclePropagatorSGP4)
        self.ConfigureSGP4WithFileSource(
            sgp4, TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

    def ConfigureSGP4WithFileSource(self, propagator: "IVehiclePropagatorSGP4", tleFilePath: str):
        # Configure propagator's TLE file path
        propagator.CommonTasks.AddSegsFromFile("2215", tleFilePath)

        # Propagate
        propagator.Propagate()

    def ConfigureSGP4WithOnlineSource(self, propagator: "IVehiclePropagatorSGP4"):
        # Configure time period
        propagator.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.Step = 60.0

        # Add segments
        propagator.CommonTasks.AddSegsFromOnlineSource("25544")

        # Propagate
        propagator.Propagate()

    # endregion

    # region SetSGP4ToAutoUpdateFromFileSource
    def test_SetSGP4ToAutoUpdateFromFileSource(self):
        # Set propagator
        SGP4.m_Object.SetPropagatorType(AgEVePropagatorType.ePropagatorSGP4)
        sgp4: "IVehiclePropagatorSGP4" = clr.CastAs(SGP4.m_Object.Propagator, IVehiclePropagatorSGP4)

        sgp4.CommonTasks.AddSegsFromFile(
            "2215", TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

        self.SetSGP4ToAutoUpdateFromFileSource(sgp4, TestBase.GetScenarioFile("CodeSnippetsTests", "stkAllTLE.tle"))

    def SetSGP4ToAutoUpdateFromFileSource(self, propagator: "IVehiclePropagatorSGP4", fileUpdateSource: str):
        propagator.AutoUpdateEnabled = True
        propagator.AutoUpdate.SelectedSource = AgEVeSGP4AutoUpdateSource.eSGP4AutoUpdateSourceFile
        propagator.AutoUpdate.FileSource.Filename = fileUpdateSource

        # Preview TLEs (optional)
        # Preview() returns a one dimension string of tles
        tles = propagator.AutoUpdate.FileSource.Preview()

        rx = Regex(r"^(?<ssc>[-]?\d+) (?<orbitepoch>[-]?\d+[.]?\d+) (?<revnumber>[-]?\d+)$")
        line: typing.Any
        for line in tles:
            m = rx.Match(str(line))
            Console.WriteLine(
                "SCC: {0}, orbit epoch: {1}, rev number: {2}",
                m.Groups["ssc"],
                m.Groups["orbitepoch"],
                m.Groups["revnumber"],
            )

        # Propagate
        propagator.Propagate()

    # endregion

    # region SetSGP4ToAutoUpdateFromOnlineSource
    def test_SetSGP4ToAutoUpdateFromOnlineSource(self):
        # Set propagator
        SGP4.m_Object.SetPropagatorType(AgEVePropagatorType.ePropagatorSGP4)
        sgp4: "IVehiclePropagatorSGP4" = clr.CastAs(SGP4.m_Object.Propagator, IVehiclePropagatorSGP4)

        sgp4.CommonTasks.AddSegsFromFile(
            "2215", TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

        self.SetSGP4ToAutoUpdateFromOnlineSource(sgp4)

    def SetSGP4ToAutoUpdateFromOnlineSource(self, propagator: "IVehiclePropagatorSGP4"):
        propagator.AutoUpdateEnabled = True
        propagator.AutoUpdate.SelectedSource = AgEVeSGP4AutoUpdateSource.eSGP4AutoUpdateSourceOnline

        # Preview TLEs (optional)
        # Preview() returns a one dimension string of tles
        tles = propagator.AutoUpdate.FileSource.Preview()

        rx = Regex(r"^(?<ssc>[-]?\d+) (?<orbitepoch>[-]?\d+[.]?\d+) (?<revnumber>[-]?\d+)$")
        line: typing.Any
        for line in tles:
            m = rx.Match(str(line))
            Console.WriteLine(
                "SCC: {0}, orbit epoch: {1}, rev number: {2}",
                m.Groups["ssc"],
                m.Groups["orbitepoch"],
                m.Groups["revnumber"],
            )

        # Propagate
        propagator.Propagate()

    # endregion
