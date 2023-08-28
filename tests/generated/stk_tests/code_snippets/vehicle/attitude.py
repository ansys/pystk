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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, Attitude.m_DefaultName
            ),
            ISatellite,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, Attitude.m_DefaultName)
        Attitude.m_Object = None

    # endregion

    # region SetAttitudeProfileTypeIsSupported
    def test_SetAttitudeProfileTypeIsSupported(self):
        self.SetAttitudeProfileTypeIsSupported(Attitude.m_Object)

    def SetAttitudeProfileTypeIsSupported(self, satellite: "ISatellite"):
        standard: "IVehicleOrbitAttitudeStandard" = clr.CastAs(satellite.attitude, IVehicleOrbitAttitudeStandard)
        if standard.basic.is_profile_type_supported(VE_PROFILE.PROFILE_SPINNING):
            standard.basic.set_profile_type(VE_PROFILE.PROFILE_SPINNING)

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(self):
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(Attitude.m_Object)

    def AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(self, satellite: "ISatellite"):
        satellite.set_attitude_type(VE_ATTITUDE.ATTITUDE_STANDARD)
        standard: "IVehicleOrbitAttitudeStandard" = clr.CastAs(satellite.attitude, IVehicleOrbitAttitudeStandard)
        standard.basic.set_profile_type(VE_PROFILE.PROFILE_INERTIALLY_FIXED)
        interfix: "IVehicleProfileInertial" = clr.CastAs(standard.basic.profile, IVehicleProfileInertial)

        interfix.inertial.assign_quaternion(-0.34298, -0.47081, 0.70345, 0.40725)

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(self):
        dtTime: "IDate" = CodeSnippetsTestBase.m_Root.conversion_utility.new_date(
            CodeSnippetsTestBase.m_Root.unit_preferences.get_current_unit_abbrv("DateFormat"), "1 Jan 2012 12:00:00.000"
        )
        time: str = dtTime.format("UTCG")
        cpfQuaternion = [[time, 0.5, 0.5, 0.5, 0.5], [time, 0.125, 0.25, 0.5, 0.35], [time, 0.35, 0.4, 0.45, 0.5]]
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(
            CodeSnippetsTestBase.m_Root, Attitude.m_Object, cpfQuaternion
        )

    def AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(
        self, root: "IStkObjectRoot", satellite: "ISatellite", cpfQuaternion
    ):
        satellite.set_attitude_type(VE_ATTITUDE.ATTITUDE_REAL_TIME)
        realtime: "IVehicleAttitudeRealTime" = clr.CastAs(satellite.attitude, IVehicleAttitudeRealTime)

        i: int = 0
        while i <= (len(cpfQuaternion) - 1):
            realtime.add_cbf_quaternion(
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
        satellite.set_attitude_type(VE_ATTITUDE.ATTITUDE_STANDARD)
        # Get IVehicleOrbitAttitudeStandard interface
        standard: "IVehicleOrbitAttitudeStandard" = clr.CastAs(satellite.attitude, IVehicleOrbitAttitudeStandard)

        # Set Profile to Inertially Fixed
        standard.basic.set_profile_type(VE_PROFILE.PROFILE_INERTIALLY_FIXED)
        # Get IVehicleProfileInertial interface
        interfix: "IVehicleProfileInertial" = clr.CastAs(standard.basic.profile, IVehicleProfileInertial)

        interfix.inertial.assign_euler_angles(EULER_ORIENTATION_SEQUENCE.SEQUENCE_123, 20.1, 50.0, 20.0)

    # endregion

    # region ConfigureRealTimeAttitude
    def test_ConfigureRealTimeAttitude(self):
        self.ConfigureRealTimeAttitude(Attitude.m_Object)

    def ConfigureRealTimeAttitude(self, satellite: "ISatellite"):
        # set attitude type to real time
        satellite.set_attitude_type(VE_ATTITUDE.ATTITUDE_REAL_TIME)
        realtime: "IVehicleAttitudeRealTime" = clr.CastAs(satellite.attitude, IVehicleAttitudeRealTime)

        # Set our Attitude Look Ahead method to Extrapolate
        realtime.look_ahead_method = VE_LOOK_AHEAD_METHOD.EXTRAPOLATE

        # Duration
        duration: "IVehicleDuration" = realtime.duration
        duration.look_ahead = 1600.0
        duration.look_behind = 1600.0

        # BlockFactor
        realtime.block_factor = 40
        realtime.data_reference.set_profile_type(VE_PROFILE.PROFILE_INERTIALLY_FIXED)

    # endregion
