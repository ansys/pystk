# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class AttitudeSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AttitudeSnippets, self).__init__(*args, **kwargs)

    m_Object: "Satellite" = None
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
        AttitudeSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.SATELLITE, AttitudeSnippets.m_DefaultName
            ),
            Satellite,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, AttitudeSnippets.m_DefaultName
        )
        AttitudeSnippets.m_Object = None

    # endregion

    # region SetAttitudeProfileTypeIsSupported
    def test_SetAttitudeProfileTypeIsSupported(self):
        self.SetAttitudeProfileTypeIsSupported(AttitudeSnippets.m_Object)

    def SetAttitudeProfileTypeIsSupported(self, satellite: "Satellite"):
        standard: "AttitudeStandardOrbit" = clr.CastAs(satellite.attitude, AttitudeStandardOrbit)
        if standard.basic.is_profile_type_supported(AttitudeProfile.SPINNING):
            standard.basic.set_profile_type(AttitudeProfile.SPINNING)

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(self):
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(AttitudeSnippets.m_Object)

    def AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternions(self, satellite: "Satellite"):
        satellite.set_attitude_type(VehicleAttitude.STANDARD)
        standard: "AttitudeStandardOrbit" = clr.CastAs(satellite.attitude, AttitudeStandardOrbit)
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        interfix: "AttitudeProfileInertial" = clr.CastAs(standard.basic.profile, AttitudeProfileInertial)

        interfix.inertial.assign_quaternion(-0.34298, -0.47081, 0.70345, 0.40725)

    # endregion

    # region AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF
    def test_AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(self):
        dtTime: "Date" = CodeSnippetsTestBase.m_Root.conversion_utility.new_date(
            CodeSnippetsTestBase.m_Root.units_preferences.get_current_unit_abbrv("DateFormat"),
            "1 Jan 2012 12:00:00.000",
        )
        time: str = dtTime.format("UTCG")
        cpfQuaternion = [[time, 0.5, 0.5, 0.5, 0.5], [time, 0.125, 0.25, 0.5, 0.35], [time, 0.35, 0.4, 0.45, 0.5]]
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(
            CodeSnippetsTestBase.m_Root, AttitudeSnippets.m_Object, cpfQuaternion
        )

    def AddsAttitudeDataBasedOnTimeOrderedSetOfQuaternionsInterpretedRelativeToCBF(
        self, root: "STKObjectRoot", satellite: "Satellite", cpfQuaternion
    ):
        satellite.set_attitude_type(VehicleAttitude.REAL_TIME)
        realtime: "VehicleAttitudeRealTime" = clr.CastAs(satellite.attitude, VehicleAttitudeRealTime)

        i: int = 0
        while i <= (len(cpfQuaternion) - 1):
            realtime.add_quaternion_relative_to_central_body_fixed(
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
        self.AddsAttitudeDataBasedOnTimeOrderedSetOfEulerAngles(AttitudeSnippets.m_Object)

    def AddsAttitudeDataBasedOnTimeOrderedSetOfEulerAngles(self, satellite: "Satellite"):
        # Set Attitude to Standard
        satellite.set_attitude_type(VehicleAttitude.STANDARD)
        # Get AttitudeStandardOrbit interface
        standard: "AttitudeStandardOrbit" = clr.CastAs(satellite.attitude, AttitudeStandardOrbit)

        # Set Profile to Inertially Fixed
        standard.basic.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)
        # Get AttitudeProfileInertial interface
        interfix: "AttitudeProfileInertial" = clr.CastAs(standard.basic.profile, AttitudeProfileInertial)

        interfix.inertial.assign_euler_angles(EulerOrientationSequenceType.SEQUENCE_123, 20.1, 50.0, 20.0)

    # endregion

    # region ConfigureRealTimeAttitude
    def test_ConfigureRealTimeAttitude(self):
        self.ConfigureRealTimeAttitude(AttitudeSnippets.m_Object)

    def ConfigureRealTimeAttitude(self, satellite: "Satellite"):
        # set attitude type to real time
        satellite.set_attitude_type(VehicleAttitude.REAL_TIME)
        realtime: "VehicleAttitudeRealTime" = clr.CastAs(satellite.attitude, VehicleAttitudeRealTime)

        # Set our Attitude Look Ahead method to Extrapolate
        realtime.look_ahead_method = VehicleLookAheadMethod.EXTRAPOLATE

        # Duration
        duration: "VehicleDuration" = realtime.duration
        duration.look_ahead = 1600.0
        duration.look_behind = 1600.0

        # BlockFactor
        realtime.block_factor = 40
        realtime.data_reference.set_profile_type(AttitudeProfile.INERTIALLY_FIXED)

    # endregion
