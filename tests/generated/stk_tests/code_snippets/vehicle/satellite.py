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
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                AgESTKObjectType.eSatellite, Satellite.m_DefaultName
            ),
            ISatellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eSatellite, Satellite.m_DefaultName
        )
        Satellite.m_Object = None

    # endregion

    # region CreateSatelliteOnCurrentScenarioCentralBody
    def test_CreateSatelliteOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            AgESTKObjectType.eSatellite, Satellite.m_DefaultName
        )
        self.CreateSatelliteOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteOnCurrentScenarioCentralBody(self, root: "IStkObjectRoot"):
        # Create the Satellite
        satellite: "ISatellite" = clr.CastAs(
            root.current_scenario.children.new(AgESTKObjectType.eSatellite, "MySatellite"), ISatellite
        )

    # endregion

    # region CreateSatelliteFromDatabase
    def test_CreateSatelliteFromDatabase(self):
        self.CreateSatelliteFromDatabase(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteFromDatabase(self, root: "IStkObjectRoot"):
        # Get STK database location using Connect
        result: "IExecCmdResult" = root.execute_command("GetDirectory / Database Satellite")
        satDataDir: str = result[0]
        filelocation: str = ('"' + Path.Combine(satDataDir, r"stkAllTLE.sd")) + '"'
        commonname: str = '"hst"'

        # Import object from database using Connect
        command: str = String.Format(
            "ImportFromDB * Satellite {0} Constellation ImportedFromSatDB Propagate On CommonName {1}",
            filelocation,
            commonname,
        )
        root.execute_command(command)

    # endregion

    # region ConfigureSatelliteWithJ2PerturbationPropagator
    def test_ConfigureSatelliteWithJ2PerturbationPropagator(self):
        self.ConfigureSatelliteWithJ2PerturbationPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithJ2PerturbationPropagator(self, satellite: "ISatellite"):
        # Set propagator to J2 Perturbation
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorJ2Perturbation)

        # Get the J2 Perturbation propagator
        propagator: "IVehiclePropagatorJ2Perturbation" = clr.CastAs(
            satellite.propagator, IVehiclePropagatorJ2Perturbation
        )

    # endregion

    # region ConfigureSatelliteWithGPSPropagator
    def test_ConfigureSatelliteWithGPSPropagator(self):
        self.ConfigureSatelliteWithGPSPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithGPSPropagator(self, satellite: "ISatellite"):
        # Set propagator to GPS
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorGPS)

        # Get the GPS propagator
        propagator: "IVehiclePropagatorGPS" = clr.CastAs(satellite.propagator, IVehiclePropagatorGPS)

    # endregion

    # region ConfigureSatelliteWithStkExternalPropagator
    def test_ConfigureSatelliteWithStkExternalPropagator(self):
        self.ConfigureSatelliteWithStkExternalPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithStkExternalPropagator(self, satellite: "ISatellite"):
        # Set propagator to STK External
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorStkExternal)

        # Get the STK External propagator
        propagator: "IVehiclePropagatorStkExternal" = clr.CastAs(satellite.propagator, IVehiclePropagatorStkExternal)

    # endregion

    # region ConfigureSatelliteWithSGP4Propagator
    def test_ConfigureSatelliteWithSGP4Propagator(self):
        self.ConfigureSatelliteWithSGP4Propagator(Satellite.m_Object)

    def ConfigureSatelliteWithSGP4Propagator(self, satellite: "ISatellite"):
        # Set propagator to SGP4
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorSGP4)

        # Get the SGP4 propagator
        propagator: "IVehiclePropagatorSGP4" = clr.CastAs(satellite.propagator, IVehiclePropagatorSGP4)

    # endregion

    # region ConfigureSatelliteWithSPICEPropagator
    def test_ConfigureSatelliteWithSPICEPropagator(self):
        self.ConfigureSatelliteWithSPICEPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithSPICEPropagator(self, satellite: "ISatellite"):
        # Set propagator to SPICE
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorSPICE)

        # Get the SPICE propagator
        propagator: "IVehiclePropagatorSPICE" = clr.CastAs(satellite.propagator, IVehiclePropagatorSPICE)

    # endregion

    # region ConfigureSatelliteWithLOPPropagator
    def test_ConfigureSatelliteWithLOPPropagator(self):
        self.ConfigureSatelliteWithLOPPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithLOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to LOP
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorLOP)

        # Get the LOP propagator
        propagator: "IVehiclePropagatorLOP" = clr.CastAs(satellite.propagator, IVehiclePropagatorLOP)

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(Satellite.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "ISatellite"):
        # Set satellite propagator to HPOP
        satellite.set_propagator_type(AgEVePropagatorType.ePropagatorHPOP)

        # Get the HPOP propagator
        propagator: "IVehiclePropagatorHPOP" = clr.CastAs(satellite.propagator, IVehiclePropagatorHPOP)

    # endregion

    # region ConfigureTargetSlew
    def test_ConfigureTargetSlew(self):
        Satellite.m_Object.set_attitude_type(AgEVeAttitude.eAttitudeStandard)
        fac: "IFacility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(AgESTKObjectType.eFacility, "FacSlew"), IFacility
        )
        fac.position.assign_geodetic(0.0, 0.0, 0.0)
        self.ConfigureTargetSlew(Satellite.m_Object)

    def ConfigureTargetSlew(self, satellite: "ISatellite"):
        orbitAttStandard: "IVehicleOrbitAttitudeStandard" = clr.CastAs(
            satellite.attitude, IVehicleOrbitAttitudeStandard
        )
        orbitAttStandard.pointing.use_target_pointing = True
        orbitAttStandard.pointing.targets.add("Facility/FacSlew")
        orbitAttStandard.pointing.target_slew.set_slew_mode_type(AgEVeSlewMode.eVeSlewModeConstrained2ndOrderSpline)

        constrainedSlew: "IVehicleAttitudeSlewConstrained" = clr.CastAs(
            orbitAttStandard.pointing.target_slew.slew_mode, IVehicleAttitudeSlewConstrained
        )
        constrainedSlew.maximum_slew_time = 20.0  # sec
        constrainedSlew.slew_timing_between_targets = AgEVeSlewTimingBetweenTargets.eVeSlewTimingBetweenTargetsOptimal

        maxRate: "IVehicleAttitudeMaximumSlewRate" = constrainedSlew.maximum_slew_rate
        maxRate.magnitude = 10.0  # deg/sec^2
        maxRate.per_axis_x_enabled = True
        maxRate.per_axis_x = 5.0  # deg/sec^2
        maxRate.per_axis_y_enabled = True
        maxRate.per_axis_y = 5.0  # deg/sec^2
        maxRate.per_axis_z_enabled = True
        maxRate.per_axis_z = 5.0  # deg/sec^2

        maxAcceleration: "IVehicleAttitudeMaximumSlewAcceleration" = constrainedSlew.maximum_slew_acceleration
        maxAcceleration.magnitude = 10.0  # deg/sec^2
        maxAcceleration.per_axis_x_accel_enabled = True
        maxAcceleration.per_axis_x_accel = 5.0  # deg/sec^2
        maxAcceleration.per_axis_y_accel_enabled = True
        maxAcceleration.per_axis_y_accel = 5.0  # deg/sec^2
        maxAcceleration.per_axis_z_accel_enabled = True
        maxAcceleration.per_axis_z_accel = 5.0  # deg/sec^2

    # endregion
