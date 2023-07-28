from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class GPS(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(GPS, self).__init__(*args, **kwargs)

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
        GPS.m_Object: ISatellite = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, GPS.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(AgESTKObjectType.eSatellite, GPS.m_DefaultName)
        GPS.m_Object = None

    # endregion

    # region ConfigureGPSWithAlmanac
    def test_ConfigureGPSWithAlmanac(self):
        GPS.m_Object.SetPropagatorType(AgEVePropagatorType.ePropagatorGPS)

        propagator: IVehiclePropagatorGPS = clr.CastAs(GPS.m_Object.Propagator, IVehiclePropagatorGPS)

        self.ConfigureGPSWithAlmanac(
            propagator,
            TestBase.GetScenarioFile("CodeSnippetsTests", "GPSAlmanac.alm"),
            (clr.Convert(GPS.m_Object, IStkObject)).Root.CurrentScenario,
        )

    def ConfigureGPSWithAlmanac(self, propagator: "IVehiclePropagatorGPS", almanacPath: str, scenario: "IStkObject"):
        # Configure properties
        # Use the scenario's analysis interval
        propagator.EphemerisInterval.SetImplicitInterval(scenario.Vgt.EventIntervals["AnalysisInterval"])

        # PRN must be set before configuring GPS almanac
        propagator.PRN = int(clr.Convert(propagator.AvailablePRNs[0], str))

        # Turn the Auto-update off
        propagator.AutoUpdateEnabled = False

        # Specify a catalog
        propagator.SpecifyCatalog.Filename = almanacPath
        if propagator.SpecifyCatalog.Properties.Type == AgEVeGPSAlmanacType.eGPSAlmanacTypeSEM:
            # configure the SEM almanac
            sem: IVehicleGPSAlmanacPropertiesSEM = clr.CastAs(
                propagator.SpecifyCatalog.Properties, IVehicleGPSAlmanacPropertiesSEM
            )
            sem.ReferenceWeek = AgEGPSReferenceWeek.eGPSReferenceWeek22Aug1999
        elif propagator.SpecifyCatalog.Properties.Type == AgEVeGPSAlmanacType.eGPSAlmanacTypeSP3:
            # SP3 almanac contains no configurable properties
            sp3: IVehicleGPSAlmanacPropertiesSP3 = clr.CastAs(
                propagator.SpecifyCatalog.Properties, IVehicleGPSAlmanacPropertiesSP3
            )
        elif propagator.SpecifyCatalog.Properties.Type == AgEVeGPSAlmanacType.eGPSAlmanacTypeYUMA:
            # configure the YUMA almanac
            yuma: IVehicleGPSAlmanacPropertiesYUMA = clr.CastAs(
                propagator.SpecifyCatalog.Properties, IVehicleGPSAlmanacPropertiesYUMA
            )
            yuma.ReferenceWeek = AgEGPSReferenceWeek.eGPSReferenceWeek22Aug1999

        # Propagate
        propagator.Propagate()

    # endregion
