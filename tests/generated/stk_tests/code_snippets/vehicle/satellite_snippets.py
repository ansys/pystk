# Copyright (C) 2022 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
                STKObjectType.SATELLITE, SatelliteSnippets.m_DefaultName
            ),
            Satellite,
        )
        CodeSnippetsTestBase.m_Root.units_preferences.reset_units()

    # endregion

    # region TestTearDown
    def tearDown(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, SatelliteSnippets.m_DefaultName
        )
        SatelliteSnippets.m_Object = None

    # endregion

    # region CreateSatelliteOnCurrentScenarioCentralBody
    def test_CreateSatelliteOnCurrentScenarioCentralBody(self):
        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(
            STKObjectType.SATELLITE, SatelliteSnippets.m_DefaultName
        )
        self.CreateSatelliteOnCurrentScenarioCentralBody(CodeSnippetsTestBase.m_Root)

    def CreateSatelliteOnCurrentScenarioCentralBody(self, root: "StkObjectRoot"):
        # Create the Satellite
        satellite: "Satellite" = clr.CastAs(
            root.current_scenario.children.new(STKObjectType.SATELLITE, "MySatellite"), Satellite
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
        satellite.set_propagator_type(PropagatorType.J2_PERTURBATION)

        # Get the J2 Perturbation propagator
        propagator: "PropagatorJ2Perturbation" = clr.CastAs(satellite.propagator, PropagatorJ2Perturbation)

    # endregion

    # region ConfigureSatelliteWithGPSPropagator
    def test_ConfigureSatelliteWithGPSPropagator(self):
        self.ConfigureSatelliteWithGPSPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithGPSPropagator(self, satellite: "Satellite"):
        # Set propagator to GPS
        satellite.set_propagator_type(PropagatorType.GPS)

        # Get the GPS propagator
        propagator: "PropagatorGPS" = clr.CastAs(satellite.propagator, PropagatorGPS)

    # endregion

    # region ConfigureSatelliteWithStkExternalPropagator
    def test_ConfigureSatelliteWithStkExternalPropagator(self):
        self.ConfigureSatelliteWithStkExternalPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithStkExternalPropagator(self, satellite: "Satellite"):
        # Set propagator to STK External
        satellite.set_propagator_type(PropagatorType.STK_EXTERNAL)

        # Get the STK External propagator
        propagator: "PropagatorStkExternal" = clr.CastAs(satellite.propagator, PropagatorStkExternal)

    # endregion

    # region ConfigureSatelliteWithSGP4Propagator
    def test_ConfigureSatelliteWithSGP4Propagator(self):
        self.ConfigureSatelliteWithSGP4Propagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithSGP4Propagator(self, satellite: "Satellite"):
        # Set propagator to SGP4
        satellite.set_propagator_type(PropagatorType.SGP4)

        # Get the SGP4 propagator
        propagator: "PropagatorSGP4" = clr.CastAs(satellite.propagator, PropagatorSGP4)

    # endregion

    # region ConfigureSatelliteWithSPICEPropagator
    def test_ConfigureSatelliteWithSPICEPropagator(self):
        self.ConfigureSatelliteWithSPICEPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithSPICEPropagator(self, satellite: "Satellite"):
        # Set propagator to SPICE
        satellite.set_propagator_type(PropagatorType.SPICE)

        # Get the SPICE propagator
        propagator: "PropagatorSPICE" = clr.CastAs(satellite.propagator, PropagatorSPICE)

    # endregion

    # region ConfigureSatelliteWithLOPPropagator
    def test_ConfigureSatelliteWithLOPPropagator(self):
        self.ConfigureSatelliteWithLOPPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithLOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to LOP
        satellite.set_propagator_type(PropagatorType.LOP)

        # Get the LOP propagator
        propagator: "PropagatorLOP" = clr.CastAs(satellite.propagator, PropagatorLOP)

    # endregion

    # region ConfigureSatelliteWithHPOPPropagator
    def test_ConfigureSatelliteWithHPOPPropagator(self):
        self.ConfigureSatelliteWithHPOPPropagator(SatelliteSnippets.m_Object)

    def ConfigureSatelliteWithHPOPPropagator(self, satellite: "Satellite"):
        # Set satellite propagator to HPOP
        satellite.set_propagator_type(PropagatorType.HPOP)

        # Get the HPOP propagator
        propagator: "PropagatorHPOP" = clr.CastAs(satellite.propagator, PropagatorHPOP)

    # endregion

    # region ConfigureTargetSlew
    def test_ConfigureTargetSlew(self):
        SatelliteSnippets.m_Object.set_attitude_type(VehicleAttitude.STANDARD)
        fac: "Facility" = clr.CastAs(
            TestBase.Application.current_scenario.children.new(STKObjectType.FACILITY, "FacSlew"), Facility
        )
        fac.position.assign_geodetic(0.0, 0.0, 0.0)
        self.ConfigureTargetSlew(SatelliteSnippets.m_Object)

    def ConfigureTargetSlew(self, satellite: "Satellite"):
        orbitAttStandard: "AttitudeStandardOrbit" = clr.CastAs(satellite.attitude, AttitudeStandardOrbit)
        orbitAttStandard.pointing.use_target_pointing = True
        orbitAttStandard.pointing.targets.add("Facility/FacSlew")
        orbitAttStandard.pointing.target_slew.set_slew_mode_type(VehicleSlewMode.CONSTRAINED_2ND_ORDER_SPLINE)

        constrainedSlew: "VehicleAttitudeSlewConstrained" = clr.CastAs(
            orbitAttStandard.pointing.target_slew.slew_mode, VehicleAttitudeSlewConstrained
        )
        constrainedSlew.maximum_slew_time = 20.0  # sec
        constrainedSlew.slew_timing_between_targets = VehicleSlewTimingBetweenTargetType.OPTIMAL

        maxRate: "VehicleAttitudeMaximumSlewRate" = constrainedSlew.maximum_slew_rate
        maxRate.magnitude = 10.0  # deg/sec^2
        maxRate.slew_rate_along_x_axis_enabled = True
        maxRate.slew_rate_along_x_axis = 5.0  # deg/sec^2
        maxRate.slew_rate_along_y_axis_enabled = True
        maxRate.slew_rate_along_y_axis = 5.0  # deg/sec^2
        maxRate.slew_rate_along_z_axis_enabled = True
        maxRate.slew_rate_along_z_axis = 5.0  # deg/sec^2

        maxAcceleration: "VehicleAttitudeMaximumSlewAcceleration" = constrainedSlew.maximum_slew_acceleration
        maxAcceleration.magnitude = 10.0  # deg/sec^2
        maxAcceleration.slew_acceleration_along_x_axis_enabled = True
        maxAcceleration.slew_acceleration_along_x_axis = 5.0  # deg/sec^2
        maxAcceleration.slew_acceleration_along_y_axis_enabled = True
        maxAcceleration.slew_acceleration_along_y_axis = 5.0  # deg/sec^2
        maxAcceleration.slew_acceleration_along_z_axis_enabled = True
        maxAcceleration.slew_acceleration_along_z_axis = 5.0  # deg/sec^2

    # endregion
