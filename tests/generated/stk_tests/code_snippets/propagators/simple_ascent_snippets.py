# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
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


class SimpleAscentSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        self.m_Object: "LaunchVehicle" = None
        super(SimpleAscentSnippets, self).__init__(*args, **kwargs)

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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STKObjectType.LAUNCH_VEHICLE, SimpleAscentSnippets.m_DefaultName
            ),
            LaunchVehicle,
        )

    # endregion

    # region TestTearDown
    def tearDown(self):
        (IStkObject(self.m_Object)).unload()
        self.m_Object = None

    # endregion

    # region ConfigureSimpleAscentPropagator
    def test_ConfigureSimpleAscentPropagator(self):
        # Set launch vehicle propagator to Simple Ascent
        self.m_Object.set_trajectory_type(PropagatorType.SIMPLE_ASCENT)

        # Get J2 PropagatorSimpleAscent interface
        propagator: "PropagatorSimpleAscent" = clr.CastAs(self.m_Object.trajectory, PropagatorSimpleAscent)

        self.ConfigureSimpleAscentPropagator(propagator)

    def ConfigureSimpleAscentPropagator(self, propagator: "PropagatorSimpleAscent"):
        # Configure time period
        propagator.ephemeris_interval.set_explicit_interval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        propagator.step = 60.0

        # Set the initial state
        propagator.initial_state.launch.assign_detic(38.3721, -77.6402, 25.0)
        propagator.initial_state.burnout.assign_detic(48.1395, -82.5145, 25.0)
        propagator.initial_state.burnout_velocity = 7.7258

        # Propagate
        propagator.propagate()

    # endregion
