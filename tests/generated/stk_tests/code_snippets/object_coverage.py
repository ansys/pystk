from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


class ObjectCoverage(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ObjectCoverage, self).__init__(*args, **kwargs)

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
        scenario = TestBase.Application.CurrentScenario
        aircraft = scenario.Children.New(AgESTKObjectType.eAircraft, "UAV")
        aircraft.Children.New(AgESTKObjectType.eSensor, "UAV_Camera")

        areaTarget = scenario.Children.New(AgESTKObjectType.eAreaTarget, "Airspace")

        try:
            self.SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(
                clr.Convert(TestBase.Application, IStkObjectRoot)
            )

        finally:
            areaTarget.Unload()
            aircraft.Unload()

    def SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(self, root):
        # For this example, set the access times to use the light intervals of the area target.
        uavAircraft = root.GetObjectFromPath("Aircraft/UAV/Sensor/UAV_Camera")
        airspaceAreaTarget = root.GetObjectFromPath("AreaTarget/Airspace")

        firstSunlightEpoch = airspaceAreaTarget.Vgt.Events["LightingIntervals.Sunlight.First.Start"]
        lastSunlightEpoch = airspaceAreaTarget.Vgt.Events["LightingIntervals.Sunlight.First.Stop"]

        uavAircraft.ObjectCoverage.UseObjectTimes = False
        startEpoch = uavAircraft.ObjectCoverage.AccessInterval.GetStartEpoch()
        startEpoch.SetImplicitTime(firstSunlightEpoch)

        stopEpoch = uavAircraft.ObjectCoverage.AccessInterval.GetStopEpoch()
        stopEpoch.SetImplicitTime(lastSunlightEpoch)

        uavAircraft.ObjectCoverage.AccessInterval.SetStartAndStopEpochs(startEpoch, stopEpoch)

    # endregion
