import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Conversions(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Conversions, self).__init__(*args, **kwargs)

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

    def ConvertPositionToAnotherRepresentation(self, root):
        converter = root.ConversionUtility

        # ConvertPositionArray expects a two dimensional array of positions
        cartesianPositions = [[1216.47, -4736.12, 4081.39], [1000, -2000, 2000]]

        # Convert cartesian dates to cylindrical
        # ConvertPositionArray returns a two dimensional array of cartesian dates
        cylindricalPositions = converter.ConvertPositionArray(
            AgEPositionType.eCartesian, cartesianPositions, AgEPositionType.eCylindrical
        )

        i = 0
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
        CodeSnippetsTestBase.m_Root.NewScenario("ConvertOrbitStateToAnotherRepresentation")
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)
        j2prop = clr.CastAs(sat.Propagator, IVehiclePropagatorJ2Perturbation)

        self.ConvertOrbitStateToAnotherRepresentation(j2prop.InitialState.Representation)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CloseScenario()

    def ConvertOrbitStateToAnotherRepresentation(self, orbit):
        newOrbit = clr.CastAs(orbit.ConvertTo(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical)

    # endregion

    # region QueryIAgDirectionAsAnotherRespresentation

    def test_QueryIAgDirectionAsAnotherRespresentation(self):
        direction = TestBase.Application.ConversionUtility.NewDirection()
        self.QueryIAgDirectionAsAnotherRespresentation(direction)

    def QueryIAgDirectionAsAnotherRespresentation(self, direction):
        b = None
        c = None

        (b, c) = direction.QueryEuler(AgEEulerDirectionSequence.e12)
        Console.WriteLine("B = {0}, C = {1}", b, c)
        # Method 2
        # The Query functions returns a one dimension array
        # The number of column rows depends on the representation
        euler = direction.QueryEulerArray(AgEEulerDirectionSequence.e12)
        Console.WriteLine("B = {0}, C = {1}", euler[0], euler[1])

    # endregion

    # region AssignIAgOrbitStateToAnotherRepresentation
    def test_AssignIAgOrbitStateToAnotherRepresentation(self):
        CodeSnippetsTestBase.m_Root.NewScenario("AssignIOrbitStateToAnotherRepresentation")
        sat = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "sat1"), ISatellite
        )
        sat.SetPropagatorType(AgEVePropagatorType.ePropagatorTwoBody)
        oTwobody = clr.CastAs(sat.Propagator, IVehiclePropagatorTwoBody)

        self.AssignIAgOrbitStateToAnotherRepresentation(oTwobody.InitialState.Representation)

        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, "sat1")
        CodeSnippetsTestBase.m_Root.CloseScenario()

    def AssignIAgOrbitStateToAnotherRepresentation(self, orbitState):
        # orbitState can be extended to one of the other representations.
        # Here it is extended to Classical representation.
        newOrbitState = clr.CastAs(orbitState.ConvertTo(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical)

        # Set the new orbit state parameters
        newOrbitState.AssignClassical(AgECoordinateSystem.eCoordinateSystemICRF, 12000000, 0, 1.8, 0, -1.8, 0)

    # endregion
