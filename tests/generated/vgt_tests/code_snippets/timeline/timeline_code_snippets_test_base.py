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


class TimelineCodeSnippetsTestBase(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(TimelineCodeSnippetsTestBase, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.InitializeWithNewScenario(True)

        satellite: "Satellite" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.SATELLITE, "LEO"), Satellite
        )
        satellite.set_propagator_type(PropagatorType.TWO_BODY)
        (clr.CastAs(satellite.propagator, PropagatorTwoBody)).propagate()

        aircraft: "Aircraft" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.AIRCRAFT, "UAV"), Aircraft
        )
        aircraft.set_route_type(PropagatorType.GREAT_ARC)
        propagator: "PropagatorGreatArc" = clr.CastAs(aircraft.route, PropagatorGreatArc)
        waypoints = [
            [40.0399, -75.5973, 3.048, 0.045, 0],
            [40.0308, -75.592, 3.081, 0.045, 0],
            [40.0201, -75.5986, 3.071, 0.04, 0],
            [40.0259, -75.5873, 3.048, 0.045, 0],
        ]
        propagator.set_points_smooth_rate_and_propagate(waypoints)

        TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "Facility1")

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion
