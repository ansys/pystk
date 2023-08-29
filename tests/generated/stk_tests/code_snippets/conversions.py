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

    def ConvertPositionToAnotherRepresentation(self, root: "IStkObjectRoot"):
        converter: "IConversionUtility" = root.conversion_utility

        # ConvertPositionArray expects a two dimensional array of positions
        cartesianPositions = [[1216.47, -4736.12, 4081.39], [1000, -2000, 2000]]

        # Convert cartesian dates to cylindrical
        # ConvertPositionArray returns a two dimensional array of cartesian dates
        cylindricalPositions = converter.convert_position_array(
            POSITION_TYPE.CARTESIAN, cartesianPositions, POSITION_TYPE.CYLINDRICAL
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
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), ISatellite
        )
        sat.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)
        j2prop: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(sat.propagator, IVehiclePropagatorJ2Perturbation)

        self.ConvertOrbitStateToAnotherRepresentation(j2prop.initial_state.representation)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.close_scenario()

    def ConvertOrbitStateToAnotherRepresentation(self, orbit: "IOrbitState"):
        newOrbit: "IOrbitStateClassical" = clr.CastAs(
            orbit.convert_to(ORBIT_STATE_TYPE.CLASSICAL), IOrbitStateClassical
        )

    # endregion

    # region QueryIAgDirectionAsAnotherRespresentation

    def test_QueryIAgDirectionAsAnotherRespresentation(self):
        direction: "IDirection" = TestBase.Application.conversion_utility.new_direction()
        self.QueryIAgDirectionAsAnotherRespresentation(direction)

    def QueryIAgDirectionAsAnotherRespresentation(self, direction: "IDirection"):
        b: typing.Any = None
        c: typing.Any = None

        (b, c) = direction.query_euler(EULER_DIRECTION_SEQUENCE.SEQUENCE_12)
        Console.WriteLine("B = {0}, C = {1}", b, c)
        # Method 2
        # The Query functions returns a one dimension array
        # The number of column rows depends on the representation
        euler = direction.query_euler_array(EULER_DIRECTION_SEQUENCE.SEQUENCE_12)
        Console.WriteLine("B = {0}, C = {1}", euler[0], euler[1])

    # endregion

    # region AssignIAgOrbitStateToAnotherRepresentation
    def test_AssignIAgOrbitStateToAnotherRepresentation(self):
        CodeSnippetsTestBase.m_Root.new_scenario("AssignIOrbitStateToAnotherRepresentation")
        sat: "ISatellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "sat1"), ISatellite
        )
        sat.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        oTwobody: "IVehiclePropagatorTwoBody" = clr.CastAs(sat.propagator, IVehiclePropagatorTwoBody)

        self.AssignIAgOrbitStateToAnotherRepresentation(oTwobody.initial_state.representation)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, "sat1")
        CodeSnippetsTestBase.m_Root.close_scenario()

    def AssignIAgOrbitStateToAnotherRepresentation(self, orbitState: "IOrbitState"):
        # orbitState can be extended to one of the other representations.
        # Here it is extended to Classical representation.
        newOrbitState: "IOrbitStateClassical" = clr.CastAs(
            orbitState.convert_to(ORBIT_STATE_TYPE.CLASSICAL), IOrbitStateClassical
        )

        # Set the new orbit state parameters
        newOrbitState.assign_classical(COORDINATE_SYSTEM.ICRF, 12000000, 0, 1.8, 0, -1.8, 0)

    # endregion
