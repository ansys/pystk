from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *


class LaunchVehicle(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(LaunchVehicle, self).__init__(*args, **kwargs)

    m_Object: "ILaunchVehicle" = None
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
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()
        LaunchVehicle.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.LAUNCH_VEHICLE, LaunchVehicle.m_DefaultName
            ),
            ILaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.LAUNCH_VEHICLE, LaunchVehicle.m_DefaultName
        )
        LaunchVehicle.m_Object = None

    # endregion

    # region CreateLaunchVehicleOnCurrentScenarioCentralBody
    def test_CreateLaunchVehicleOnCurrentScenarioCentralBody(self):
        (clr.Convert(LaunchVehicle.m_Object, IStkObject)).unload()
        self.CreateLaunchVehicleOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateLaunchVehicleOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Launch vehicle
        launchVehicle: "ILaunchVehicle" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.LAUNCH_VEHICLE, "MyLaunchVehicle"), ILaunchVehicle
        )

    # endregion

    # region DetermineIfTrajectoryIsSupported
    def test_DetermineIfTrajectoryIsSupported(self):
        self.DetermineIfTrajectoryIsSupported(LaunchVehicle.m_Object)

    def DetermineIfTrajectoryIsSupported(self, launchVehicle: "ILaunchVehicle"):
        supported: bool = launchVehicle.is_trajectory_type_supported(VE_PROPAGATOR_TYPE.PROPAGATOR_REALTIME)

    # endregion
