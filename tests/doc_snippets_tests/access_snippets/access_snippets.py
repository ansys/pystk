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
from ansys.stk.core.stkobjects import *

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippets_test_base import *
from code_snippet_decorator import *


class AccessSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(AccessSnippets, self).__init__(*args, **kwargs)

    satellite: "Satellite" = None
    accessConstraints: "AccessConstraintCollection" = None

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def setUp(self):
        AccessSnippets.satellite: "Satellite" = Satellite(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite")
        )
        propagator: "PropagatorTwoBody" = AccessSnippets.satellite.propagator
        propagator.propagate()
        AccessSnippets.accessConstraints: "AccessConstraintCollection" = AccessSnippets.satellite.access_constraints

    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite")
        AccessSnippets.satellite = None

    def test_TestAddExclusionZoneConstraintSnippet(self):
        self.TestAddExclusionZoneConstraintSnippet(CodeSnippetsTestBase.m_Root, AccessSnippets.accessConstraints)

    @code_snippet(
        name="AddExclusionZoneConstraint",
        description="Add an Exclusion Zone access constraint",
        category="STK Objects | Access",
        eid="STKObjects~IAgAccessConstraint",
    )
    def TestAddExclusionZoneConstraintSnippet(
        self, root: "StkObjectRoot", accessConstraints: "AccessConstraintCollection"
    ):
        # AccessConstraintCollection accessConstraints: Access Constraint collection
        excludeZone: "AccessConstraintLatitudeLongitudeZone" = accessConstraints.add_named_constraint("ExclusionZone")
        excludeZone.maximum_latitude = 45
        excludeZone.minimum_latitude = 15
        excludeZone.minimum_longitude = -75
        excludeZone.maximum_longitude = -35
