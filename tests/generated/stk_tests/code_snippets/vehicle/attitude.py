from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Attitude(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Attitude, self).__init__(*args, **kwargs)

    m_Object: "ISatellite" = None
    m_DefaultName: str = "sat1"

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
        Attitude.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eSatellite, Attitude.m_DefaultName
            ),
            ISatellite,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, Attitude.m_DefaultName)
        Attitude.m_Object = None

    # endregion

    # region SetAttitudeProfileTypeIsSupported
    def test_SetAttitudeProfileTypeIsSupported(self):
        self.SetAttitudeProfileTypeIsSupported(Attitude.m_Object)

    def SetAttitudeProfileTypeIsSupported(self, satellite: "ISatellite"):
        standard = clr.CastAs(satellite.Attitude, IVehicleOrbitAttitudeStandard)
        if standard.Basic.IsProfileTypeSupported(AgEVeProfile.eProfileSpinning):
            standard.Basic.SetProfileType(AgEVeProfile.eProfileSpinning)

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(self):
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(Attitude.m_Object)

    def AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(self, satellite: "ISatellite"):
        satellite.SetAttitudeType(AgEVeAttitude.eAttitudeStandard)
        standard = clr.CastAs(satellite.Attitude, IVehicleOrbitAttitudeStandard)
        standard.Basic.SetProfileType(AgEVeProfile.eProfileInertiallyFixed)
        interfix = clr.CastAs(standard.Basic.Profile, IVehicleProfileInertial)

        interfix.Inertial.AssignQuaternion(-0.34298, -0.47081, 0.70345, 0.40725)

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(self):
        dtTime = CodeSnippetsTestBase.m_Root.ConversionUtility.NewDate(
            CodeSnippetsTestBase.m_Root.UnitPreferences.GetCurrentUnitAbbrv("DateFormat"), "1 Jan 2012 12:00:00.000"
        )
        time = dtTime.Format("UTCG")
        cpfQuaternion = [[time, 0.5, 0.5, 0.5, 0.5], [time, 0.125, 0.25, 0.5, 0.35], [time, 0.35, 0.4, 0.45, 0.5]]
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(
            CodeSnippetsTestBase.m_Root, Attitude.m_Object, cpfQuaternion
        )

    def AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(
        self, root: "IStkObjectRoot", satellite: "ISatellite", cpfQuaternion
    ):
        satellite.SetAttitudeType(AgEVeAttitude.eAttitudeRealTime)
        realtime = clr.CastAs(satellite.Attitude, IVehicleAttitudeRealTime)

        i = 0
        while i <= (len(cpfQuaternion) - 1):
            realtime.AddCBFQuaternion(
                cpfQuaternion[i][0],
                float(cpfQuaternion[i][1]),
                float(cpfQuaternion[i][2]),
                float(cpfQuaternion[i][3]),
                float(cpfQuaternion[i][4]),
            )

            i += 1

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfEulerAngles
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfEulerAngles(self):
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfEulerAngles(Attitude.m_Object)

    def AddsAttitudeDataBasedOnTimeOrderedSetOfEulerAngles(self, satellite: "ISatellite"):
        # Set Attitude to Standard
        satellite.SetAttitudeType(AgEVeAttitude.eAttitudeStandard)
        # Get IAgVeOrbitAttitudeStandard interface
        standard = clr.CastAs(satellite.Attitude, IVehicleOrbitAttitudeStandard)

        # Set Profile to Inertially Fixed
        standard.Basic.SetProfileType(AgEVeProfile.eProfileInertiallyFixed)
        # Get IAgVeProfileInertial interface
        interfix = clr.CastAs(standard.Basic.Profile, IVehicleProfileInertial)

        interfix.Inertial.AssignEulerAngles(AgEEulerOrientationSequence.e123, 20.1, 50.0, 20.0)

    # endregion

    # region ConfigureRealTimeAttitude
    def test_ConfigureRealTimeAttitude(self):
        self.ConfigureRealTimeAttitude(Attitude.m_Object)

    def ConfigureRealTimeAttitude(self, satellite: "ISatellite"):
        # set attitude type to real time
        satellite.SetAttitudeType(AgEVeAttitude.eAttitudeRealTime)
        realtime = clr.CastAs(satellite.Attitude, IVehicleAttitudeRealTime)

        # Set our Attitude Look Ahead method to Extrapolate
        realtime.LookAheadMethod = AgEVeLookAheadMethod.eExtrapolate

        # Duration
        duration = realtime.Duration
        duration.LookAhead = 1600.0
        duration.LookBehind = 1600.0

        # BlockFactor
        realtime.BlockFactor = 40
        realtime.DataReference.SetProfileType(AgEVeProfile.eProfileInertiallyFixed)

    # endregion
