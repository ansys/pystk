from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class ObjectCoverageSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ObjectCoverageSnippets, self).__init__(*args, **kwargs)

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
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject
    def test_SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(self):
        scenario: "IStkObject" = TestBase.Application.current_scenario
        aircraft: "IStkObject" = scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "UAV")
        aircraft.children.new(STK_OBJECT_TYPE.SENSOR, "UAV_Camera")

        areaTarget: "IStkObject" = scenario.children.new(STK_OBJECT_TYPE.AREA_TARGET, "Airspace")

        try:
            self.SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(TestBase.Application)

        finally:
            areaTarget.unload()
            aircraft.unload()

    def SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(self, root: "StkObjectRoot"):
        # For this example, set the access times to use the light intervals of the area target.
        uavAircraft: "IStkObject" = root.get_object_from_path("Aircraft/UAV/Sensor/UAV_Camera")
        airspaceAreaTarget: "IStkObject" = root.get_object_from_path("AreaTarget/Airspace")

        firstSunlightEpoch: "ITimeToolInstant" = airspaceAreaTarget.vgt.time_instants[
            "LightingIntervals.Sunlight.First.Start"
        ]
        lastSunlightEpoch: "ITimeToolInstant" = airspaceAreaTarget.vgt.time_instants[
            "LightingIntervals.Sunlight.First.Stop"
        ]

        uavAircraft.object_coverage.use_object_times = False
        startEpoch: "TimeToolInstantSmartEpoch" = uavAircraft.object_coverage.access_interval.get_start_epoch()
        startEpoch.set_implicit_time(firstSunlightEpoch)

        stopEpoch: "TimeToolInstantSmartEpoch" = uavAircraft.object_coverage.access_interval.get_stop_epoch()
        stopEpoch.set_implicit_time(lastSunlightEpoch)

        uavAircraft.object_coverage.access_interval.set_start_and_stop_epochs(startEpoch, stopEpoch)

    # endregion
