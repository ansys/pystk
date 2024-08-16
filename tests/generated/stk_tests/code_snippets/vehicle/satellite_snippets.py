from test_util import *
from code_snippets.code_snippets_test_base import *

from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *


class SatelliteSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(SatelliteSnippets, self).__init__(*args, **kwargs)

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
        SatelliteSnippets.m_Object = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(
                STK_OBJECT_TYPE.SATELLITE, SatelliteSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.unit_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, SatelliteSnippets.m_DefaultName
        )
        SatelliteSnippets.m_Object = None

    # endregion

    # region CreateSatelliteOnCurrentScenarioCentralBody
    def test_CreateSatelliteOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STK_OBJECT_TYPE.SATELLITE, SatelliteSnippets.m_DefaultName
        )
        self.CreateSatelliteOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Satellite
        satellite: "Satellite" = clr.CastAs(
            root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MySatellite"), Satellite
        )

    # endregion

    # region CreateSatelliteFromDatabase
    def test_CreateSatelliteFromDatabase(self):
        self.CreateSatelliteFromDatabase(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteFromDatabase(self, root: "StkObjectRoot"):
        # Get STK database location using Connect
        result: "ExecuteCommandResult" = root.execute_command("GetDirectory / Database Satellite")
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
        self.ConfigureSatelliteWithJ2PerturbationPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithJ2PerturbationPropagator(self, satellite: "Satellite"):
        # Set propagator to J2 Perturbation
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J2_PERTURBATION)

        # Get the J2 Perturbation propagator
        propagator: "VehiclePropagatorJ2Perturbation" = clr.CastAs(
            satellite.propagator, VehiclePropagatorJ2Perturbation
        )

    # endregion

    # region ConfigureSatelliteWithGPSPropagator
    def test_ConfigureSatelliteWithGPSPropagator(self):
        self.ConfigureSatelliteWithGPSPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithGPSPropagator(self, satellite: "Satellite"):
        # Set propagator to GPS
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GPS)

        # Get the GPS propagator
        propagator: "VehiclePropagatorGPS" = clr.CastAs(satellite.propagator, VehiclePropagatorGPS)

    # endregion

    # region ConfigureSatelliteWithStkExternalPropagator
    def test_ConfigureSatelliteWithStkExternalPropagator(self):
        self.ConfigureSatelliteWithStkExternalPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithStkExternalPropagator(self, satellite: "Satellite"):
        # Set propagator to STK External
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)

        # Get the STK External propagator
        propagator: "VehiclePropagatorStkExternal" = clr.CastAs(satellite.propagator, VehiclePropagatorStkExternal)

    # endregion

    # region ConfigureSatelliteWithSGP4Propagator
    def test_ConfigureSatelliteWithSGP4Propagator(self):
        self.ConfigureSatelliteWithSGP4Propagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithSGP4Propagator(self, satellite: "Satellite"):
        # Set propagator to SGP4
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)

        # Get the SGP4 propagator
        propagator: "VehiclePropagatorSGP4" = clr.CastAs(satellite.propagator, VehiclePropagatorSGP4)

    # endregion

    # region ConfigureSatelliteWithSPICEPropagator
    def test_ConfigureSatelliteWithSPICEPropagator(self):
        self.ConfigureSatelliteWithSPICEPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithSPICEPropagator(self, satellite: "Satellite"):
        # Set propagator to SPICE
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SPICE)

        # Get the SPICE propagator
        propagator: "VehiclePropagatorSPICE" = clr.CastAs(satellite.propagator, VehiclePropagatorSPICE)

    # endregion

    # region ConfigureSatelliteWithLOPPropagator
    def test_ConfigureSatelliteWithLOPPropagator(self):
        self.ConfigureSatelliteWithLOPPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithLOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to LOP
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_LOP)

        # Get the LOP propagator
        propagator: "VehiclePropagatorLOP" = clr.CastAs(satellite.propagator, VehiclePropagatorLOP)

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to HPOP
        satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_HPOP)

        # Get the HPOP propagator
        propagator: "VehiclePropagatorHPOP" = clr.CastAs(satellite.propagator, VehiclePropagatorHPOP)

    # endregion

    # region ConfigureTargetSlew
    def test_ConfigureTargetSlew(self):
        SatelliteSnippets.m_Object.set_attitude_type(VEHICLE_ATTITUDE.ATTITUDE_STANDARD)
        fac: "Facility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "FacSlew"), Facility
        )
        fac.position.assign_geodetic(0.0, 0.0, 0.0)
        self.ConfigureTargetSlew(SatelliteSnippets.m_Object)

    def ConfigureTargetSlew(self, satellite: "Satellite"):
        orbitAttStandard: "VehicleOrbitAttitudeStandard" = clr.CastAs(satellite.attitude, VehicleOrbitAttitudeStandard)
        orbitAttStandard.pointing.use_target_pointing = True
        orbitAttStandard.pointing.targets.add("Facility/FacSlew")
        orbitAttStandard.pointing.target_slew.set_slew_mode_type(VEHICLE_SLEW_MODE.CONSTRAINED2_ND_ORDER_SPLINE)

        constrainedSlew: "VehicleAttitudeSlewConstrained" = clr.CastAs(
            orbitAttStandard.pointing.target_slew.slew_mode, VehicleAttitudeSlewConstrained
        )
        constrainedSlew.maximum_slew_time = 20.0  # sec
        constrainedSlew.slew_timing_between_targets = VEHICLE_SLEW_TIMING_BETWEEN_TARGETS.OPTIMAL

        maxRate: "VehicleAttitudeMaximumSlewRate" = constrainedSlew.maximum_slew_rate
        maxRate.magnitude = 10.0  # deg/sec^2
        maxRate.per_axis_x_enabled = True
        maxRate.per_axis_x = 5.0  # deg/sec^2
        maxRate.per_axis_y_enabled = True
        maxRate.per_axis_y = 5.0  # deg/sec^2
        maxRate.per_axis_z_enabled = True
        maxRate.per_axis_z = 5.0  # deg/sec^2

        maxAcceleration: "VehicleAttitudeMaximumSlewAcceleration" = constrainedSlew.maximum_slew_acceleration
        maxAcceleration.magnitude = 10.0  # deg/sec^2
        maxAcceleration.per_axis_x_acceleration_enabled = True
        maxAcceleration.per_axis_x_acceleration = 5.0  # deg/sec^2
        maxAcceleration.per_axis_y_acceleration_enabled = True
        maxAcceleration.per_axis_y_acceleration = 5.0  # deg/sec^2
        maxAcceleration.per_axis_z_acceleration_enabled = True
        maxAcceleration.per_axis_z_acceleration = 5.0  # deg/sec^2

    # endregion
