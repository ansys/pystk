from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class Satellite(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(Satellite, self).__init__(*args, **kwargs)

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
        Satellite.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.CurrentScenario.Children.New(
                AgESTKObjectType.eSatellite, Satellite.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.UnitPreferences.ResetUnits()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, Satellite.m_DefaultName
        )
        Satellite.m_Object = None

    # endregion

    # region CreateSatelliteOnCurrentScenarioCentralBody
    def test_CreateSatelliteOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.CurrentScenario.Children.Unload(
            AgESTKObjectType.eSatellite, Satellite.m_DefaultName
        )
        self.CreateSatelliteOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Satellite
        satellite = clr.CastAs(
            root.CurrentScenario.Children.New(AgESTKObjectType.eSatellite, "MySatellite"), ISatellite
        )

    # endregion

    # region CreateSatelliteFromDatabase
    def test_CreateSatelliteFromDatabase(self):
        self.CreateSatelliteFromDatabase(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteFromDatabase(self, root: "IStkObjectRoot"):
        # Get STK database location using Connect
        result = root.ExecuteCommand("GetDirectory / Database Satellite")
        satDataDir = result[0]
        filelocation = ('"' + Path.Combine(satDataDir, r"stkAllTLE.sd")) + '"'
        commonname = '"hst"'

        # Import object from database using Connect
        command = String.Format(
            "ImportFromDB * Satellite {0} Constellation ImportedFromSatDB Propagate On CommonName {1}",
            filelocation,
            commonname,
        )
        root.ExecuteCommand(command)

    # endregion

    # region ConfigureSatelliteWithJ2PerturbationPropagator
    def test_ConfigureSatelliteWithJ2PerturbationPropagator(self):
        self.ConfigureSatelliteWithJ2PerturbationPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithJ2PerturbationPropagator(self, satellite: "ISatellite"):
        # Set propagator to J2 Perturbation
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorJ2Perturbation)

        # Get the J2 Perturbation propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorJ2Perturbation)

    # endregion

    # region ConfigureSatelliteWithGPSPropagator
    def test_ConfigureSatelliteWithGPSPropagator(self):
        self.ConfigureSatelliteWithGPSPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithGPSPropagator(self, satellite: "ISatellite"):
        # Set propagator to GPS
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorGPS)

        # Get the GPS propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorGPS)

    # endregion

    # region ConfigureSatelliteWithStkExternalPropagator
    def test_ConfigureSatelliteWithStkExternalPropagator(self):
        self.ConfigureSatelliteWithStkExternalPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithStkExternalPropagator(self, satellite: "ISatellite"):
        # Set propagator to STK External
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorStkExternal)

        # Get the STK External propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorStkExternal)

    # endregion

    # region ConfigureSatelliteWithSGP4Propagator
    def test_ConfigureSatelliteWithSGP4Propagator(self):
        self.ConfigureSatelliteWithSGP4Propagator(Satellite.m_Object)

    def ConfigureSatelliteWithSGP4Propagator(self, satellite: "ISatellite"):
        # Set propagator to SGP4
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorSGP4)

        # Get the SGP4 propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorSGP4)

    # endregion

    # region ConfigureSatelliteWithSPICEPropagator
    def test_ConfigureSatelliteWithSPICEPropagator(self):
        self.ConfigureSatelliteWithSPICEPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithSPICEPropagator(self, satellite: "ISatellite"):
        # Set propagator to SPICE
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorSPICE)

        # Get the SPICE propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorSPICE)

    # endregion

    # region ConfigureSatelliteWithLOPPropagator
    def test_ConfigureSatelliteWithLOPPropagator(self):
        self.ConfigureSatelliteWithLOPPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithLOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to LOP
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorLOP)

        # Get the LOP propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorLOP)

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to HPOP
        satellite.SetPropagatorType(AgEVePropagatorType.ePropagatorHPOP)

        # Get the HPOP propagator
        propagator = clr.CastAs(satellite.Propagator, IVehiclePropagatorHPOP)

    # endregion

    # region ConfigureTargetSlew
    def test_ConfigureTargetSlew(self):
        Satellite.m_Object.SetAttitudeType(AgEVeAttitude.eAttitudeStandard)
        fac = clr.CastAs(
            TestBase.Application.CurrentScenario.Children.New(AgESTKObjectType.eFacility, "FacSlew"), IFacility
        )
        fac.Position.AssignGeodetic(0.0, 0.0, 0.0)
        self.ConfigureTargetSlew(Satellite.m_Object)

    def ConfigureTargetSlew(self, satellite: "ISatellite"):
        orbitAttStandard = clr.CastAs(satellite.Attitude, IVehicleOrbitAttitudeStandard)
        orbitAttStandard.Pointing.UseTargetPointing = True
        orbitAttStandard.Pointing.Targets.Add("Facility/FacSlew")
        orbitAttStandard.Pointing.TargetSlew.SetSlewModeType(AgEVeSlewMode.eVeSlewModeConstrained2ndOrderSpline)

        constrainedSlew = clr.CastAs(orbitAttStandard.Pointing.TargetSlew.SlewMode, IVehicleAttitudeSlewConstrained)
        constrainedSlew.MaximumSlewTime = 20.0  # sec
        constrainedSlew.SlewTimingBetweenTargets = AgEVeSlewTimingBetweenTargets.eVeSlewTimingBetweenTargetsOptimal

        maxRate = constrainedSlew.MaximumSlewRate
        maxRate.Magnitude = 10.0  # deg/sec^2
        maxRate.PerAxisXEnabled = True
        maxRate.PerAxisX = 5.0  # deg/sec^2
        maxRate.PerAxisYEnabled = True
        maxRate.PerAxisY = 5.0  # deg/sec^2
        maxRate.PerAxisZEnabled = True
        maxRate.PerAxisZ = 5.0  # deg/sec^2

        maxAcceleration = constrainedSlew.MaximumSlewAcceleration
        maxAcceleration.Magnitude = 10.0  # deg/sec^2
        maxAcceleration.PerAxisXAccelEnabled = True
        maxAcceleration.PerAxisXAccel = 5.0  # deg/sec^2
        maxAcceleration.PerAxisYAccelEnabled = True
        maxAcceleration.PerAxisYAccel = 5.0  # deg/sec^2
        maxAcceleration.PerAxisZAccelEnabled = True
        maxAcceleration.PerAxisZAccel = 5.0  # deg/sec^2

    # endregion
