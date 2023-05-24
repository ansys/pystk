import sys
import os

sys.path.insert(1, os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), ".."))
from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class J2Perturbation(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(J2Perturbation, self).__init__(*args, **kwargs)

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
        J2Perturbation.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eSatellite, J2Perturbation.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, J2Perturbation.m_DefaultName
        )
        J2Perturbation.m_Object = None

    # endregion

    # region ConfigureSatelliteWithJ2PerturbationPropagator
    def test_ConfigureSatelliteWithJ2PerturbationPropagator(self):
        self.ConfigureSatelliteWithJ2PerturbationPropagator(J2Perturbation.m_Object)

    def ConfigureSatelliteWithJ2PerturbationPropagator(self, satellite):
        # Set propagator to SGP4
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)

        # J2 Perturbation propagator
        j2prop = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)

        # Configure time period
        j2prop.EphemerisInterval.SetExplicitInterval("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")
        j2prop.Step = 60.0

        # Configure propagator initial state
        initial = j2prop.InitialState
        initial.Representation.Epoch = "1 Jan 2012 12:00:00.000"
        initial.Representation.AssignCartesian(
            AgECoordinateSystem.eCoordinateSystemFixed, -1514.4, -6790.1, -1.25, 4.8151, 1.771, 5.6414
        )  # in km/sec
        initial.EllipseOptions = AgEVeEllipseOptions.eSecularlyPrecessing

        # Propagate
        j2prop.Propagate()

    # endregion
