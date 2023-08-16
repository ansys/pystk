from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class J4Perturbation(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(J4Perturbation, self).__init__(*args, **kwargs)

    m_Object: "ISatellite" = None
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
        J4Perturbation.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eSatellite, J4Perturbation.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eSatellite, J4Perturbation.m_DefaultName
        )
        J4Perturbation.m_Object = None

    # endregion

    # region ConfigureJ4PerturbationPropagatorOrbitToCircular
    def test_ConfigureJ4PerturbationPropagatorOrbitToCircular(self):
        self.ConfigureJ4PerturbationPropagatorOrbitToCircular(J4Perturbation.m_Object, 45.0, 500.0)

    # This code snippet is taken from SatelliteOrbitWizard.cs in the test suite
    def ConfigureJ4PerturbationPropagatorOrbitToCircular(self, satellite: "ISatellite", incl: float, altitude: float):
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorJ4Perturbation)
        prop: "IVehiclePropagatorJ4Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ4Perturbation)

        keplerian: "IOrbitStateClassical" = clr.CastAs(
            prop.initial_state.representation.convert_to(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical
        )

        keplerian.size_shape_type = AgEClassicalSizeShape.eSizeShapeAltitude
        size: "IClassicalSizeShapeAltitude" = clr.CastAs(keplerian.size_shape, IClassicalSizeShapeAltitude)

        size.apogee_altitude = altitude
        size.perigee_altitude = altitude

        keplerian.orientation.inclination = incl
        keplerian.orientation.arg_of_perigee = 0
        keplerian.orientation.asc_node_type = AgEOrientationAscNode.eAscNodeRAAN
        (clr.CastAs(keplerian.orientation.asc_node, IOrientationAscNodeRAAN)).value = 0

        keplerian.location_type = AgEClassicalLocation.eLocationTrueAnomaly
        (clr.CastAs(keplerian.location, IClassicalLocationTrueAnomaly)).value = 0

        prop.initial_state.representation.assign(keplerian)
        prop.propagate()

    # endregion

    # region ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined
    def test_ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(self):
        self.ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(J4Perturbation.m_Object, 12000.0, 400.0, -100.0)

    # This code snippet is taken from SatelliteOrbitWizard.cs in the test suite
    def ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(
        self, satellite: "ISatellite", apogeeAlt: float, perigeeAlt: float, ascNodeLon: float
    ):
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorJ4Perturbation)
        prop: "IVehiclePropagatorJ4Perturbation" = clr.CastAs(satellite.propagator, IVehiclePropagatorJ4Perturbation)

        keplerian: "IOrbitStateClassical" = clr.CastAs(
            prop.initial_state.representation.convert_to(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical
        )

        keplerian.size_shape_type = AgEClassicalSizeShape.eSizeShapeAltitude
        size: "IClassicalSizeShapeAltitude" = clr.CastAs(keplerian.size_shape, IClassicalSizeShapeAltitude)

        size.apogee_altitude = apogeeAlt
        size.perigee_altitude = perigeeAlt

        keplerian.orientation.inclination = 63.434949
        keplerian.orientation.arg_of_perigee = 270.0
        keplerian.orientation.asc_node_type = AgEOrientationAscNode.eAscNodeLAN
        (clr.CastAs(keplerian.orientation.asc_node, IOrientationAscNodeLAN)).value = ascNodeLon

        keplerian.location_type = AgEClassicalLocation.eLocationTrueAnomaly
        (clr.CastAs(keplerian.location, IClassicalLocationTrueAnomaly)).value = 90.0

        prop.initial_state.representation.assign(keplerian)
        prop.propagate()

    # endregion
