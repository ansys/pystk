from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class J4Perturbation(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(J4Perturbation, self).__init__(*args, **kwargs)

    m_Object = None
    m_DefaultName = "MySatellite"

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
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eSatellite, J4Perturbation.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, J4Perturbation.m_DefaultName
        )
        J4Perturbation.m_Object = None

    # endregion

    # region ConfigureJ4PerturbationPropagatorOrbitToCircular
    def test_ConfigureJ4PerturbationPropagatorOrbitToCircular(self):
        self.ConfigureJ4PerturbationPropagatorOrbitToCircular(J4Perturbation.m_Object, 45.0, 500.0)

    # This code snippet is taken from SatelliteOrbitWizard.cs in the test suite
    def ConfigureJ4PerturbationPropagatorOrbitToCircular(self, satellite, incl, altitude):
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ4Perturbation)
        prop = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ4Perturbation)

        keplerian = clr.CastAs(
            prop.InitialState.Representation.ConvertTo(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical
        )

        keplerian.SizeShapeType = AgEClassicalSizeShape.eSizeShapeAltitude
        size = clr.CastAs(keplerian.SizeShape, IClassicalSizeShapeAltitude)

        size.ApogeeAltitude = altitude
        size.PerigeeAltitude = altitude

        keplerian.Orientation.Inclination = incl
        keplerian.Orientation.ArgOfPerigee = 0
        keplerian.Orientation.AscNodeType = AgEOrientationAscNode.eAscNodeRAAN
        (clr.CastAs(keplerian.Orientation.AscNode, IOrientationAscNodeRAAN)).Value = 0

        keplerian.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
        (clr.CastAs(keplerian.Location, IClassicalLocationTrueAnomaly)).Value = 0

        prop.InitialState.Representation.Assign(keplerian)
        prop.Propagate()

    # endregion

    # region ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined
    def test_ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(self):
        self.ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(J4Perturbation.m_Object, 12000.0, 400.0, -100.0)

    # This code snippet is taken from SatelliteOrbitWizard.cs in the test suite
    def ConfigureJ4PerturbationPropagatorOrbitToCritcallyInclined(self, satellite, apogeeAlt, perigeeAlt, ascNodeLon):
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ4Perturbation)
        prop = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ4Perturbation)

        keplerian = clr.CastAs(
            prop.InitialState.Representation.ConvertTo(AgEOrbitStateType.eOrbitStateClassical), IOrbitStateClassical
        )

        keplerian.SizeShapeType = AgEClassicalSizeShape.eSizeShapeAltitude
        size = clr.CastAs(keplerian.SizeShape, IClassicalSizeShapeAltitude)

        size.ApogeeAltitude = apogeeAlt
        size.PerigeeAltitude = perigeeAlt

        keplerian.Orientation.Inclination = 63.434949
        keplerian.Orientation.ArgOfPerigee = 270.0
        keplerian.Orientation.AscNodeType = AgEOrientationAscNode.eAscNodeLAN
        (clr.CastAs(keplerian.Orientation.AscNode, IOrientationAscNodeLAN)).Value = ascNodeLon

        keplerian.LocationType = AgEClassicalLocation.eLocationTrueAnomaly
        (clr.CastAs(keplerian.Location, IClassicalLocationTrueAnomaly)).Value = 90.0

        prop.InitialState.Representation.Assign(keplerian)
        prop.Propagate()

    # endregion
