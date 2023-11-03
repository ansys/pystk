from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class SGP4Snippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SGP4Snippets, self).__init__(*args, **kwargs)

    m_Object: "Satellite" = None
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
        SGP4Snippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, SGP4Snippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, SGP4Snippets.m_DefaultName
        )
        SGP4Snippets.m_Object = None

    # endregion

    # region ConfigureSGP4WithFileSource
    def test_ConfigureSGP4WithFileSource(self):
        SGP4Snippets.m_Object.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)

        sgp4: "VehiclePropagatorSGP4" = clr.CastAs(SGP4Snippets.m_Object.propagator, VehiclePropagatorSGP4)
        self.ConfigureSGP4WithFileSource(
            sgp4, TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

    def ConfigureSGP4WithFileSource(self, propagator: "VehiclePropagatorSGP4", tleFilePath: str):
        # Configure propagator's TLE file path
        propagator.common_tasks.add_segs_from_file("2215", tleFilePath)

        # Propagate
        propagator.propagate()

    def ConfigureSGP4WithOnlineSource(self, propagator: "VehiclePropagatorSGP4"):
        # Configure time period
        propagator.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.step = 60.0

        # Add segments
        propagator.common_tasks.add_segs_from_online_source("25544")

        # Propagate
        propagator.propagate()

    # endregion

    # region SetSGP4ToAutoUpdateFromFileSource
    def test_SetSGP4ToAutoUpdateFromFileSource(self):
        # Set propagator
        SGP4Snippets.m_Object.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        sgp4: "VehiclePropagatorSGP4" = clr.CastAs(SGP4Snippets.m_Object.propagator, VehiclePropagatorSGP4)

        sgp4.common_tasks.add_segs_from_file(
            "2215", TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

        self.SetSGP4ToAutoUpdateFromFileSource(sgp4, TestBase.GetScenarioFile("CodeSnippetsTests", "stkAllTLE.tle"))

    def SetSGP4ToAutoUpdateFromFileSource(self, propagator: "VehiclePropagatorSGP4", fileUpdateSource: str):
        propagator.auto_update_enabled = True
        propagator.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_FILE
        propagator.auto_update.file_source.filename = fileUpdateSource

        # Preview TLEs (optional)
        # Preview() returns a one dimension string of tles
        tles = propagator.auto_update.file_source.preview()

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
        propagator.propagate()

    # endregion

    # region SetSGP4ToAutoUpdateFromOnlineSource
    def test_SetSGP4ToAutoUpdateFromOnlineSource(self):
        # Set propagator
        SGP4Snippets.m_Object.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        sgp4: "VehiclePropagatorSGP4" = clr.CastAs(SGP4Snippets.m_Object.propagator, VehiclePropagatorSGP4)

        sgp4.common_tasks.add_segs_from_file(
            "2215", TestBase.PathCombine(TestBase.GetSTKDBDir(), "Databases", "Satellite", "stkAllTLE.tce")
        )

        self.SetSGP4ToAutoUpdateFromOnlineSource(sgp4)

    def SetSGP4ToAutoUpdateFromOnlineSource(self, propagator: "VehiclePropagatorSGP4"):
        propagator.auto_update_enabled = True
        propagator.auto_update.selected_source = VEHICLE_SGP4_AUTO_UPDATE_SOURCE.SGP4_AUTO_UPDATE_SOURCE_ONLINE

        # Preview TLEs (optional)
        # Preview() returns a one dimension string of tles
        tles = propagator.auto_update.file_source.preview()

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
        propagator.propagate()

    # endregion
