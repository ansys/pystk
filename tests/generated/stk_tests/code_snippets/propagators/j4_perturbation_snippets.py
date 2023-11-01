from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class J4PerturbationSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(J4PerturbationSnippets, self).__init__(*args, **kwargs)

    m_Object: "Satellite" = None
    m_DefaultName: str = "MySatellite"

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
        J4PerturbationSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, J4PerturbationSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, J4PerturbationSnippets.m_DefaultName
        )
        J4PerturbationSnippets.m_Object = None

    # endregion

    # region ConfigureJ4PerturbationPropagatorOrbitToCircular
    def test_ConfigureJ4PerturbationPropagatorOrbitToCircular(self):
        self.ConfigureJ4PerturbationPropagatorOrbitToCircular(J4PerturbationSnippets.m_Object, 45.0, 500.0)

    # This code snippet is taken from SatelliteOrbitWizard.cs in the test suite
    def ConfigureJ4PerturbationPropagatorOrbitToCircular(self, satellite: "Satellite", incl: float, altitude: float):
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        prop: "VehiclePropagatorJ4Perturbation" = clr.CastAs(satellite.propagator, VehiclePropagatorJ4Perturbation)

        keplerian: "OrbitStateClassical" = clr.CastAs(
            prop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), OrbitStateClassical
        )

        keplerian.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        size: "ClassicalSizeShapeAltitude" = clr.CastAs(keplerian.size_shape, ClassicalSizeShapeAltitude)

        size.apogee_altitude = altitude
        size.perigee_altitude = altitude

        keplerian.orientation.inclination = incl
        keplerian.orientation.arg_of_perigee = 0
        keplerian.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_RAAN
        (clr.CastAs(keplerian.orientation.asc_node, OrientationAscNodeRAAN)).value = 0

        keplerian.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        (clr.CastAs(keplerian.location, ClassicalLocationTrueAnomaly)).value = 0

        prop.initial_state.representation.assign(keplerian)
        prop.propagate()

    # endregion

    # region ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined
    def test_ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(self):
        self.ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(
            J4PerturbationSnippets.m_Object, 12000.0, 400.0, -100.0
        )

    # This code snippet is taken from SatelliteOrbitWizard.cs in the test suite
    def ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(
        self, satellite: "Satellite", apogeeAlt: float, perigeeAlt: float, ascNodeLon: float
    ):
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
        prop: "VehiclePropagatorJ4Perturbation" = clr.CastAs(satellite.propagator, VehiclePropagatorJ4Perturbation)

        keplerian: "OrbitStateClassical" = clr.CastAs(
            prop.initial_state.representation.convert_to(ORBIT_STATE_TYPE.CLASSICAL), OrbitStateClassical
        )

        keplerian.size_shape_type = CLASSICAL_SIZE_SHAPE.SIZE_SHAPE_ALTITUDE
        size: "ClassicalSizeShapeAltitude" = clr.CastAs(keplerian.size_shape, ClassicalSizeShapeAltitude)

        size.apogee_altitude = apogeeAlt
        size.perigee_altitude = perigeeAlt

        keplerian.orientation.inclination = 63.434949
        keplerian.orientation.arg_of_perigee = 270.0
        keplerian.orientation.asc_node_type = ORIENTATION_ASC_NODE.ASC_NODE_LAN
        (clr.CastAs(keplerian.orientation.asc_node, OrientationAscNodeLAN)).value = ascNodeLon

        keplerian.location_type = CLASSICAL_LOCATION.LOCATION_TRUE_ANOMALY
        (clr.CastAs(keplerian.location, ClassicalLocationTrueAnomaly)).value = 90.0

        prop.initial_state.representation.assign(keplerian)
        prop.propagate()

    # endregion
