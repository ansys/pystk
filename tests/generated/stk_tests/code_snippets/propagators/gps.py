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
        GPS.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, GPS.m_DefaultName),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STK_OBJECT_TYPE.SATELLITE, GPS.m_DefaultName)
        GPS.m_Object = None

    # endregion

    # region ConfigureGPSWithAlmanac
    def test_ConfigureGPSWithAlmanac(self):
        GPS.m_Object.set_propagator_type(VE_PROPAGATOR_TYPE.PROPAGATOR_GPS)

        propagator: "IVehiclePropagatorGPS" = clr.CastAs(GPS.m_Object.propagator, IVehiclePropagatorGPS)

        self.ConfigureGPSWithAlmanac(
            propagator,
            TestBase.GetScenarioFile("CodeSnippetsTests", "GPSAlmanac.alm"),
            (clr.Convert(GPS.m_Object, IStkObject)).root.current_scenario,
        )

    def ConfigureGPSWithAlmanac(self, propagator: "IVehiclePropagatorGPS", almanacPath: str, scenario: "IStkObject"):
        # Configure properties
        # Use the scenario's analysis interval
        propagator.ephemeris_interval.set_implicit_interval(scenario.vgt.event_intervals["AnalysisInterval"])

        # PRN must be set before configuring GPS almanac
        propagator.prn = int(clr.Convert(propagator.available_pr_ns[0], str))

        # Turn the Auto-update off
        propagator.auto_update_enabled = False

        # Specify a catalog
        propagator.specify_catalog.filename = almanacPath
        if propagator.specify_catalog.properties.type == VE_GPS_ALMANAC_TYPE.GPS_ALMANAC_TYPE_SEM:
            # configure the SEM almanac
            sem: "IVehicleGPSAlmanacPropertiesSEM" = clr.CastAs(
                propagator.specify_catalog.properties, IVehicleGPSAlmanacPropertiesSEM
            )
            sem.reference_week = GPS_REFERENCE_WEEK.WEEK22_AUG1999
        elif propagator.specify_catalog.properties.type == VE_GPS_ALMANAC_TYPE.GPS_ALMANAC_TYPE_SP3:
            # SP3 almanac contains no configurable properties
            sp3: "IVehicleGPSAlmanacPropertiesSP3" = clr.CastAs(
                propagator.specify_catalog.properties, IVehicleGPSAlmanacPropertiesSP3
            )
        elif propagator.specify_catalog.properties.type == VE_GPS_ALMANAC_TYPE.GPS_ALMANAC_TYPE_YUMA:
            # configure the YUMA almanac
            yuma: "IVehicleGPSAlmanacPropertiesYUMA" = clr.CastAs(
                propagator.specify_catalog.properties, IVehicleGPSAlmanacPropertiesYUMA
            )
            yuma.reference_week = GPS_REFERENCE_WEEK.WEEK22_AUG1999

        # Propagate
        propagator.propagate()

    # endregion
