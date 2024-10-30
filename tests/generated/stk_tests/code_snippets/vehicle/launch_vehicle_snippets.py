from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class LaunchVehicleSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LaunchVehicleSnippets, self).__init__(*args, **kwargs)

    m_Object: "LaunchVehicle" = None
    m_DefaultName: str = "MyLaunchVehicle"

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

    # region SetUp
    def setUp(self):
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()
        LaunchVehicleSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.LAUNCH_VEHICLE, LaunchVehicleSnippets.m_DefaultName
            ),
            LaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.LAUNCH_VEHICLE, LaunchVehicleSnippets.m_DefaultName
        )
        LaunchVehicleSnippets.m_Object = None

    # endregion

    # region CreateLaunchVehicleOnCurrentScenarioCentralBody
    def test_CreateLaunchVehicleOnCurrentScenarioCentralBody(self):
        (IStkObject(LaunchVehicleSnippets.m_Object)).unload()
        self.CreateLaunchVehicleOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateLaunchVehicleOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Launch vehicle
        launchVehicle: "LaunchVehicle" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "MyLaunchVehicle"), LaunchVehicle
        )

    # endregion

    # region DetermineIfTrajectoryIsSupported
    def test_DetermineIfTrajectoryIsSupported(self):
        self.DetermineIfTrajectoryIsSupported(LaunchVehicleSnippets.m_Object)

    def DetermineIfTrajectoryIsSupported(self, launchVehicle: "LaunchVehicle"):
        supported: bool = launchVehicle.is_trajectory_type_supported(PROPAGATOR_TYPE.REAL_TIME)

    # endregion
