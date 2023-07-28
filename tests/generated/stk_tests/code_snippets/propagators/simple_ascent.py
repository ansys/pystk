from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *


class SimpleAscent(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "ILaunchVehicle" = None
        super(SimpleAscent, self).__init__(*args, **kwargs)

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
        self.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eLaunchVehicle, SimpleAscent.m_DefaultName
            ),
            ILaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        (clr.Convert(self.m_Object, IStkObject)).Unload()
        self.m_Object = None

    # endregion

    # region ConfigureSimpleAscentPropagator
    def test_ConfigureSimpleAscentPropagator(self):
        # Set launch vehicle propagator to Simple Ascent
        self.m_Object.SetTrajectoryType(AgEVePropagatorType.ePropagatorSimpleAscent)

        # Get J2 IAgVePropagatorSimpleAscent interface
        propagator: "IVehiclePropagatorSimpleAscent" = clr.CastAs(
            self.m_Object.Trajectory, IVehiclePropagatorSimpleAscent
        )

        self.ConfigureSimpleAscentPropagator(propagator)

    def ConfigureSimpleAscentPropagator(self, propagator: "IVehiclePropagatorSimpleAscent"):
        # Configure time period
        propagator.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.Step = 60.0

        # Set the initial state
        propagator.InitialState.Launch.AssignGeodetic(38.3721, -77.6402, 25.0)
        propagator.InitialState.Burnout.AssignGeodetic(48.1395, -82.5145, 25.0)
        propagator.InitialState.BurnoutVel = 7.7258

        # Propagate
        propagator.Propagate()

    # endregion
