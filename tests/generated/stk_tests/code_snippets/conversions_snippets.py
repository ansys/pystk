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
from ansys.stk.core.stkutil import *


class ConversionsSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(ConversionsSnippets, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.InitializeWithNewScenario(False)

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

    # region ConvertPositionToAnotherRepresentation
    def test_ConvertPositionToAnotherRepresentation(self):
        self.ConvertPositionToAnotherRepresentation(CodeSnippetsTestBase.m_Root)

    def ConvertPositionToAnotherRepresentation(self, root: "StkObjectRoot"):
        converter: "ConversionUtility" = root.conversion_utility

        # ConvertPositionArray expects a two dimensional array of positions
        cartesianPositions = [[1216.47, -4736.12, 4081.39], [1000, -2000, 2000]]

        # Convert cartesian dates to cylindrical
        # ConvertPositionArray returns a two dimensional array of cartesian dates
        cylindricalPositions = converter.convert_position_array(
            PositionType.CARTESIAN, cartesianPositions, PositionType.CYLINDRICAL
        )

        i: int = 0
        while i < len(cylindricalPositions):
            Console.WriteLine(
                "X: {0}, Y: {1}, Z: {2}",
                cylindricalPositions[i][0],
                cylindricalPositions[i][1],
                cylindricalPositions[i][2],
            )

            i += 1

    # endregion

    # region ConvertOrbitStateToAnotherRepresentation
    def test_ConvertOrbitStateToAnotherRepresentation(self):
        CodeSnippetsTestBase.m_Root.new_scenario("ConvertOrbitStateToAnotherRepresentation")
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1"), Satellite
        )
        sat.set_propagator_type(PropagatorType.J2_PERTURBATION)
        j2prop: "PropagatorJ2Perturbation" = clr.CastAs(sat.propagator, PropagatorJ2Perturbation)

        self.ConvertOrbitStateToAnotherRepresentation(j2prop.initial_state.representation)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.close_scenario()

    def ConvertOrbitStateToAnotherRepresentation(self, orbit: "IOrbitState"):
        newOrbit: "OrbitStateClassical" = clr.CastAs(orbit.convert_to(OrbitStateType.CLASSICAL), OrbitStateClassical)

    # endregion

    # region QueryIAgDirectionAsAnotherRespresentation

    def test_QueryIAgDirectionAsAnotherRespresentation(self):
        direction: "IDirection" = TestBase.Application.conversion_utility.new_direction()
        self.QueryIAgDirectionAsAnotherRespresentation(direction)

    def QueryIAgDirectionAsAnotherRespresentation(self, direction: "IDirection"):
        b: typing.Any = None
        c: typing.Any = None

        (b, c) = direction.query_euler(EulerDirectionSequence.SEQUENCE_12)
        Console.WriteLine("B = {0}, C = {1}", b, c)
        # Method 2
        # The Query functions returns a one dimension array
        # The number of column rows depends on the representation
        euler = direction.query_euler_array(EulerDirectionSequence.SEQUENCE_12)
        Console.WriteLine("B = {0}, C = {1}", euler[0], euler[1])

    # endregion

    # region AssignIAgOrbitStateToAnotherRepresentation
    def test_AssignIAgOrbitStateToAnotherRepresentation(self):
        CodeSnippetsTestBase.m_Root.new_scenario("AssignIOrbitStateToAnotherRepresentation")
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1"), Satellite
        )
        sat.set_propagator_type(PropagatorType.TWO_BODY)
        oTwobody: "PropagatorTwoBody" = clr.CastAs(sat.propagator, PropagatorTwoBody)

        self.AssignIAgOrbitStateToAnotherRepresentation(oTwobody.initial_state.representation)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.close_scenario()

    def AssignIAgOrbitStateToAnotherRepresentation(self, orbitState: "IOrbitState"):
        # orbitState can be extended to one of the other representations.
        # Here it is extended to Classical representation.
        newOrbitState: "OrbitStateClassical" = clr.CastAs(
            orbitState.convert_to(OrbitStateType.CLASSICAL), OrbitStateClassical
        )

        # Set the new orbit state parameters
        newOrbitState.assign_classical(CoordinateSystem.ICRF, 12000000, 0, 1.8, 0, -1.8, 0)

    # endregion
