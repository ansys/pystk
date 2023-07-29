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
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()
        LaunchVehicle.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eLaunchVehicle, LaunchVehicle.m_DefaultName
            ),
            ILaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eLaunchVehicle, LaunchVehicle.m_DefaultName
        )
        LaunchVehicle.m_Object = None

    # endregion

    # region CreateLaunchVehicleOnCurrentScenarioCentralBody
    def test_CreateLaunchVehicleOnCurrentScenarioCentralBody(self):
        (clr.Convert(LaunchVehicle.m_Object, IStkObject)).Unload()
        self.CreateLaunchVehicleOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateLaunchVehicleOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Launch vehicle
        launchVehicle: "ILaunchVehicle" = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eLaunchVehicle, "MyLaunchVehicle"), ILaunchVehicle
        )

    # endregion

    # region DetermineIfTrajectoryIsSupported
    def test_DetermineIfTrajectoryIsSupported(self):
        self.DetermineIfTrajectoryIsSupported(LaunchVehicle.m_Object)

    def DetermineIfTrajectoryIsSupported(self, launchVehicle: "ILaunchVehicle"):
        supported: bool = launchVehicle.IsTrajectoryTypeSupported(AgEVePropagatorType.ePropagatorRealtime)

    # endregion
