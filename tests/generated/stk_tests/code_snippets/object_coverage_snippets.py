# Copyright (C) 2025 - 2025 ANSYS, Inc. and/or its affiliates.
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
        aircraft: "IStkObject" = scenario.children.new(STKObjectType.AIRCRAFT, "UAV")
        aircraft.children.new(STKObjectType.SENSOR, "UAV_Camera")

        areaTarget: "IStkObject" = scenario.children.new(STKObjectType.AREA_TARGET, "Airspace")

        try:
            self.SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(TestBase.Application)

        finally:
            areaTarget.unload()
            aircraft.unload()

    def SetObjectCoverageCustomTimeIntervalToLightingTimeOfAnObject(self, root: "StkObjectRoot"):
        # For this example, set the access times to use the light intervals of the area target.
        uavAircraft: "IStkObject" = root.get_object_from_path("Aircraft/UAV/Sensor/UAV_Camera")
        airspaceAreaTarget: "IStkObject" = root.get_object_from_path("AreaTarget/Airspace")

        firstSunlightEpoch: "ITimeToolInstant" = airspaceAreaTarget.analysis_workbench_components.time_instants[
            "LightingIntervals.Sunlight.First.Start"
        ]
        lastSunlightEpoch: "ITimeToolInstant" = airspaceAreaTarget.analysis_workbench_components.time_instants[
            "LightingIntervals.Sunlight.First.Stop"
        ]

        uavAircraft.object_coverage.use_object_times = False
        startEpoch: "TimeToolInstantSmartEpoch" = uavAircraft.object_coverage.access_interval.get_start_epoch()
        startEpoch.set_implicit_time(firstSunlightEpoch)

        stopEpoch: "TimeToolInstantSmartEpoch" = uavAircraft.object_coverage.access_interval.get_stop_epoch()
        stopEpoch.set_implicit_time(lastSunlightEpoch)

        uavAircraft.object_coverage.access_interval.set_start_and_stop_epochs(startEpoch, stopEpoch)

    # endregion
