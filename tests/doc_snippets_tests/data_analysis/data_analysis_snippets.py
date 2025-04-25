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

import os
import sys

from ansys.stk.core.stkobjects import STKObjectType

# Add path to the parent directory to use some common utilities
sys.path.insert(1, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
from code_snippet_decorator import code_snippet
from code_snippets_test_base import CodeSnippetsTestBase, Scenario, TestBase

class DataAnalysisSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    def get_scenario(self):
        return CodeSnippetsTestBase.m_Root.current_scenario
    
    def get_root(self):
        return CodeSnippetsTestBase.m_Root
    
    def reset_to_default_scenario(self):
        # See CodeSnippetsTestBase.Initialize()
        if TestBase.Application.current_scenario != None:
            TestBase.Application.close_scenario()
        TestBase.Application.new_scenario("CodeSnippetScenario")
        scenario: "Scenario" = Scenario(TestBase.Application.current_scenario)
        scenario.set_time_period("1 Jan 2012 12:00:00.000", "2 Jan 2012 12:00:00.000")

    def _create_coverage_scenario(self):
        root = self.get_root()
        root.close_scenario()

        from ansys.stk.core.stkobjects import Scenario
        root.new_scenario(r"CoverageDataAnalysisSnippets")
        scenario: Scenario = root.current_scenario

        scenario.start_time = r"15 Mar 2024 16:00:00.000"
        scenario.stop_time = r"16 Mar 2024 16:00:00.000"

        from ansys.stk.core.stkobjects import Satellite, STKObjectType, PropagatorType, ClassicalLocation, OrientationAscNode, ClassicalSizeShape, PropagatorJ4Perturbation, OrbitStateClassical, CoordinateSystem
        from ansys.stk.core.stkutil import OrbitStateType

        # SATELLITES

        circ_sat = scenario.children.new(STKObjectType.SATELLITE, "Circ_Sat")
        repeat_sat = scenario.children.new(STKObjectType.SATELLITE, "Repeat_Sat")
        sun_sat = scenario.children.new(STKObjectType.SATELLITE, "Sun_Sat")

        orbit_states = {
        #   "instance_name": [semi_major_axis, eccentricity, inclination, argument_of_periapsis, raan, true_anomaly] 
            "Circ_Sat": [7078.14, 0, 55, 0, -105, 0],
            "Repeat_Sat": [6853.45, 0, 98, 0, 53.7464, 0],
            "Sun_Sat": [6778.14, 0, 97.0346, 0, 173.746, 0],
        }

        satellite: Satellite
        for satellite in [circ_sat, repeat_sat, sun_sat]:

            satellite.set_propagator_type(PropagatorType.J4_PERTURBATION)

            propagator: PropagatorJ4Perturbation = satellite.propagator
            circ_sat_orbit: OrbitStateClassical = propagator.initial_state.representation.convert_to(
                OrbitStateType.CLASSICAL
            )
            orbit_state: OrbitStateClassical = propagator.initial_state.representation.convert_to(OrbitStateType.CLASSICAL)
            orbit_state.coordinate_system_type = CoordinateSystem.TRUE_OF_DATE
            orbit_state.size_shape_type = ClassicalSizeShape.SEMIMAJOR_AXIS
            orbit_state.location_type = ClassicalLocation.TRUE_ANOMALY
            orbit_state.orientation.ascending_node_type = OrientationAscNode.RIGHT_ASCENSION_ASCENDING_NODE

            orbit_state.size_shape.semi_major_axis = orbit_states[satellite.instance_name][0]
            orbit_state.size_shape.eccentricity = orbit_states[satellite.instance_name][1]
            orbit_state.orientation.inclination = orbit_states[satellite.instance_name][2]
            orbit_state.orientation.argument_of_periapsis = orbit_states[satellite.instance_name][3]
            orbit_state.orientation.ascending_node.value = orbit_states[satellite.instance_name][4]
            orbit_state.location.value = orbit_states[satellite.instance_name][5]

            propagator.initial_state.representation.assign(orbit_state)
            propagator.initial_state.representation.epoch = scenario.start_time
            propagator.propagate()


        # SENSORS
        from ansys.stk.core.stkobjects import Sensor, SensorPattern

        circ_sens: Sensor = circ_sat.children.new(STKObjectType.SENSOR, "Circ_Sens")
        repeat_sens: Sensor = repeat_sat.children.new(STKObjectType.SENSOR, "Repeat_Sens")
        sun_sens: Sensor = sun_sat.children.new(STKObjectType.SENSOR, "Sun_Sens")

        for sensor in [circ_sens, repeat_sens, sun_sens]:
            sensor.set_pattern_type(SensorPattern.RECTANGULAR)
            sensor.common_tasks.set_pattern_rectangular(20, 10)

        # COVERAGE DEFINITION
        from ansys.stk.core.stkobjects import CoverageDefinition, CoverageBounds, CoverageResolution

        world_coverage: CoverageDefinition = scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "World_Cov")
        world_coverage.grid.bounds_type = CoverageBounds.GLOBAL
        world_coverage.grid.resolution_type = CoverageResolution.RESOLUTION_LATITUDE_LONGITUDE
        world_coverage.grid.resolution.latitude_longitude = 4

        for path in [circ_sens.path, repeat_sens.path, sun_sens.path]:
            world_coverage.asset_list.add(path)

        world_coverage.compute_accesses()

        return root

    def _create_access_scenario(self):
        root = self.get_root()
        root.close_scenario()

        from ansys.stk.core.stkobjects import Scenario
        root.new_scenario(r"AccessDataAnalysisSnippets")

        scenario: Scenario = root.current_scenario

        scenario.start_time = r"1 Jun 2020 18:00:00.000"
        scenario.stop_time = r"2 Jun 2020 18:00:00.000"

        from ansys.stk.core.stkobjects import STKObjectType, Facility

        facility: Facility = root.current_scenario.children.new(STKObjectType.FACILITY, "Castle_Rock_Teleport")

        facility.position.assign_geodetic(39.2768, -104.807, 2071)

        from ansys.stk.core.stkobjects import Sensor, SensorPattern, IAccessConstraint
        sensor: Sensor = facility.children.new(STKObjectType.SENSOR, "CR_FOV")

        sensor.set_pattern_type(SensorPattern.SIMPLE_CONIC)
        sensor.common_tasks.set_pattern_simple_conic(90, 1)

        constraint: IAccessConstraint = sensor.access_constraints.add_named_constraint("Range")
        constraint.enable_maximum = True
        constraint.maximum = 1500

        # KSU-CUBESAT_47954

        from ansys.stk.core.stkobjects import Satellite, PropagatorType, PropagatorSGP4

        ksu_cubesat: Satellite = root.current_scenario.children.new(STKObjectType.SATELLITE, "KSU-CUBESAT_47954")

        ksu_cubesat.set_propagator_type(PropagatorType.SGP4)
        ksu_cubesat_propagator: PropagatorSGP4 = ksu_cubesat.propagator
        ksu_cubesat_propagator.ephemeris_interval.set_implicit_interval(
            root.current_scenario.analysis_workbench_components.time_intervals.item("AnalysisInterval")
        )
        ksu_cubesat_propagator.common_tasks.add_segments_from_online_source("47954")
        ksu_cubesat_propagator.automatic_update_enabled = True
        ksu_cubesat_propagator.propagate()

        return root
    
    def _create_aviator_scenario(self):
        root = self.get_root()
        root.close_scenario()

        from ansys.stk.core.stkobjects import Scenario
        root.new_scenario(r"Aviator")

        scenario: Scenario = root.current_scenario

        scenario.start_time = r"1 Jul 2016 16:00:00.000"
        scenario.stop_time = r"1 Jul 2016 22:00:00.000"

        from ansys.stk.core.stkobjects import STKObjectType, AreaTarget

        area_target: AreaTarget = root.current_scenario.children.new(STKObjectType.AREA_TARGET, "Airstrip")
        area_target.area_type_data.remove_all()
        boundary = [[35.74833, -117.63113], [35.74835, -117.63107], [35.73713, -117.62753], [35.73711, -117.6276]]
        area_target.common_tasks.set_area_type_pattern(boundary)

        from ansys.stk.core.stkobjects import Place

        place: Place = root.current_scenario.children.new(STKObjectType.PLACE, "NavPoint")

        place.position.assign_geodetic(34.8977, -117.6446, 0)

        from ansys.stk.core.stkobjects import Target

        target: Target = root.current_scenario.children.new(STKObjectType.TARGET, "GndTarget")
        target.position.assign_geodetic(34.8979, -117.6857, 1)

        from ansys.stk.core.stkobjects import Aircraft, PropagatorType
        from ansys.stk.core.stkobjects.aviator import AviatorPropagator, SiteType, ProcedureType, ProcedureTakeoff, RunwayHeadingOptions, RunwayHighLowEnd, TakeoffNormal, Catalog, RunwayCategory

        aircraft: Aircraft = root.current_scenario.children.new(STKObjectType.AIRCRAFT, "TestFlight")
        aircraft.set_route_type(PropagatorType.AVIATOR)

        aviator_propagator: AviatorPropagator = aircraft.route.aviator_propagator

        catalog: Catalog = aviator_propagator.aviator_catalog
        runway_category: RunwayCategory = catalog.runway_category
        if not runway_category.user_runways.contains("Airstrip"):
            runway = runway_category.user_runways.add_user_runway("Airstrip")
        else:
            runway = runway_category.user_runways.get_user_runway("Airstrip")
        runway.latitude = 35.7427
        runway.longitude = -117.629
        runway.altitude = 0.619773

        runway.low_end_heading = 153.529
        runway.high_end_heading = 333.529
        runway.length = 4.24823

        phase1 = aviator_propagator.aviator_mission.phases[0]
        phase1.name = "Phase 1"

        takeoff: ProcedureTakeoff = phase1.procedures.add(SiteType.SITE_RUNWAY_FROM_CATALOG, ProcedureType.PROCEDURE_TAKEOFF)
        takeoff.name = "Takeoff"
        takeoff.site.set_catalog_runway(runway)

        heading_options: RunwayHeadingOptions = takeoff.runway_heading_options
        heading_options.runway_mode = RunwayHighLowEnd.LOW_END

        normal_takeoff: TakeoffNormal = takeoff.mode_as_normal
        normal_takeoff.runway_altitude_offset = 15
        normal_takeoff.use_runway_terrain = True
        normal_takeoff.departure_altitude = 48.6464

        from ansys.stk.core.stkobjects.aviator import FuelTankInternal, StationCollection, WindAtmosphereModelSource, WindModelType, AtmosphereModel, AtmosphereModelBasic, AtmosphereModelType

        wind_model = aviator_propagator.aviator_mission.wind_model
        wind_model.wind_model_source = WindAtmosphereModelSource.MISSION_MODEL
        wind_model.wind_model_type = WindModelType.CONSTANT_WIND
        constant_wind = wind_model.mode_as_constant
        constant_wind.wind_bearing = 200
        constant_wind.wind_speed = 20

        atmosphere_model: AtmosphereModel = aviator_propagator.aviator_mission.atmosphere_model
        atmosphere_model.atmosphere_model_source = WindAtmosphereModelSource.MISSION_MODEL
        basic_atmosphere: AtmosphereModelBasic = atmosphere_model.mode_as_basic
        basic_atmosphere.basic_model_type = AtmosphereModelType.STANDARD1976
        basic_atmosphere.use_non_standard_atmosphere = True
        basic_atmosphere.temperature = 316.483

        aviator_propagator.aviator_mission.configuration.empty_weight = 95000
        aviator_propagator.aviator_mission.configuration.max_landing_weight = 155000
        stations: StationCollection = aviator_propagator.aviator_mission.configuration.get_stations()
        fuel_tank: FuelTankInternal = stations.get_internal_fuel_tank_by_name("Internal Fuel")
        fuel_tank.initial_fuel_state = 20000
        fuel_tank.capacity = 60000

        from ansys.stk.core.stkobjects.aviator import SiteSTKObjectWaypoint, ProcedureHoldingCircular, CruiseSpeed, HoldingDirection, AirspeedType

        holding: ProcedureHoldingCircular = phase1.procedures.add(SiteType.SITE_STK_OBJECT_WAYPOINT, ProcedureType.PROCEDURE_HOLDING_CIRCULAR)
        site_as_waypoint = SiteSTKObjectWaypoint(holding.site)
        site_as_waypoint.object_name = "Place/NavPoint"
        holding.hold_cruise_airspeed_options.cruise_speed_type = CruiseSpeed.MIN_AIRSPEED
        holding.enroute_cruise_airspeed_options.cruise_speed_type = CruiseSpeed.OTHER_AIRSPEED
        holding.enroute_cruise_airspeed_options.set_other_airspeed(AirspeedType.TAS, 200)
        holding.bearing = 0
        holding.range = 0
        holding.diameter = 4
        holding.use_alternate_entry_points = False
        holding.turn_direction = HoldingDirection.OUTBOUND_LEFT_TURN

        from ansys.stk.core.stkobjects.aviator import ProcedureLanding, ApproachMode

        landing: ProcedureLanding = phase1.procedures.add(SiteType.SITE_RUNWAY_FROM_CATALOG, ProcedureType.PROCEDURE_LANDING)
        landing.site.set_catalog_runway(runway)

        landing.approach_mode = ApproachMode.INTERCEPT_GLIDESLOPE
        landing_heading_options: RunwayHeadingOptions = landing.runway_heading_options
        landing_heading_options.runway_mode = RunwayHighLowEnd.LOW_END
        landing.mode_as_intercept_glideslope.runway_altitude_offset = 15
        landing.mode_as_intercept_glideslope.use_runway_terrain = True

        aviator_propagator.propagate()

        return root


    def test_FlightProfileNumpyArraySnippet(self):
        root = self._create_aviator_scenario()
        aircraft = root.current_scenario.children.item("TestFlight")

        self.FlightProfileNumpyArraySnippet(aircraft)

    @code_snippet(
        name="FlightProfileNumpyArray",
        description="Load a Numpy array with flight profile data",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def FlightProfileNumpyArraySnippet(self, aircraft):
        # Aircraft aircraft: Aircraft object
        from scipy.spatial import ConvexHull
        import matplotlib.pyplot as plt

        # compute data provider results for an aircraft's Flight Profile By Time
        field_names = ['Mach #', 'Altitude']
        time_step_sec = 1.0

        flight_profile_data_provider = aircraft.data_providers.item('Flight Profile By Time')
        flight_profile_data = flight_profile_data_provider.execute_elements(self.get_scenario().start_time, self.get_scenario().stop_time, time_step_sec, field_names)

        # convert dataset collection in a row format as a Numpy array
        flight_profile_data_arr = flight_profile_data.data_sets.to_numpy_array()

        # plot estimated fligth envelope as a convex hull
        hull = ConvexHull(flight_profile_data_arr)

        plt.figure(figsize=(15, 10))
        for simplex in hull.simplices:
            plt.plot(flight_profile_data_arr[simplex, 1], flight_profile_data_arr[simplex, 0], color="darkblue")

        plt.title('Estimated Flight Envelope', fontsize=15)
        plt.xlabel('Mach Number', fontsize=15)
        plt.ylabel('Altitude', fontsize=15)

        plt.tick_params(axis='x', labelsize=15)
        plt.tick_params(axis='y', labelsize=15)
        plt.grid(visible=True)
    
    def test_CoverageDefinitionResultsToPandasDataFrameSnippet(self):
        root = self._create_coverage_scenario()
        coverage = root.current_scenario.children.item("World_Cov")

        self.CoverageDefinitionResultsToPandasDataFrameSnippet(coverage)

    @code_snippet(
        name="CoverageDefinitionResultsToPandasDataFrame",
        description="Convert coverage definition data provider results to a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def CoverageDefinitionResultsToPandasDataFrameSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        # compute data provider results for All Regions by Pass coverage
        coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
        coverage_data = coverage_data_provider.execute()

        # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
        coverage_df = coverage_data.data_sets.to_pandas_dataframe()

    def test_AccessResultsToPandasDataFrameSnippet(self):
        root = self._create_access_scenario()
        cube_sat_obj = root.current_scenario.children.item("KSU-CUBESAT_47954")
        facility_sensor_obj = root.current_scenario.children.item("Castle_Rock_Teleport").children.item("CR_FOV")
        
        facility_sensor_satellite_access = facility_sensor_obj.get_access_to_object(cube_sat_obj)
        facility_sensor_satellite_access.compute_access()

        self.AccessResultsToPandasDataFrameSnippet(facility_sensor_satellite_access)

    @code_snippet(
        name="AccessResultsToPandasDataFrame",
        description="Convert access data provider results to a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def AccessResultsToPandasDataFrameSnippet(self, facility_sensor_satellite_access):
        # Access facility_sensor_satellite_access: Access calculation
        # compute data provider results for basic Access
        field_names = ['Access Number', 'Start Time', 'Stop Time', 'Duration']

        access_data = facility_sensor_satellite_access.data_providers['Access Data'].execute_elements(
            self.get_scenario().start_time, self.get_scenario().stop_time, field_names
        )

        # convert dataset collection in a row format as a Pandas DataFrame
        index_column = 'Access Number'
        access_data_df = access_data.data_sets.to_pandas_dataframe(index_element_name=index_column)

    def test_DescriptiveStatisticsPandasDataFrameSnippet(self):
        root = self._create_coverage_scenario()
        coverage = root.current_scenario.children.item("World_Cov")

        self.DescriptiveStatisticsPandasDataFrameSnippet(coverage)

    @code_snippet(
        name="DescriptiveStatisticsPandasDataFrame",
        description="Compute descriptive statistics for access measurements using a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def DescriptiveStatisticsPandasDataFrameSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        import pandas as pd

        # compute data provider results for All Regions by Pass coverage
        coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
        coverage_data = coverage_data_provider.execute()

        # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
        all_regions_coverage_df = coverage_data.data_sets.to_pandas_dataframe()

        # compute descriptive statistics of Duration, Percent Coverage, Area Coverage
        all_regions_coverage_df[['duration', 'percent coverage', 'area coverage']].apply(pd.to_numeric).describe()

    def test_CoverageDefinitionResultsPandasDataFrameHeatMapSnippet(self):
        root = self._create_coverage_scenario()
        coverage = root.current_scenario.children.item("World_Cov")

        self.CoverageDefinitionResultsPandasDataFrameHeatMapSnippet(coverage)

    @code_snippet(
        name="CoverageDefinitionResultsPandasDataFrameHeatMap",
        description="Create a heat map of coverage definition results graphing duration by asset using a Pandas DataFrame",
        category="Data Analysis",
        eid="stkobjects~DataProviderResultDataSetCollection",
    )
    def CoverageDefinitionResultsPandasDataFrameHeatMapSnippet(self, coverage):
        # CoverageDefinition coverage: Coverage object
        from matplotlib import pyplot as plt
        import numpy as np

        # compute data provider results for All Regions by Pass coverage
        coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
        coverage_data = coverage_data_provider.execute()

        # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
        coverage_all_regions_elements = coverage_data_provider.elements
        all_regions_coverage_df = coverage_data.data_sets.to_pandas_dataframe(data_provider_elements=coverage_all_regions_elements)

        # reshape the DataFrame based on column values
        pivot = all_regions_coverage_df.pivot_table(index='region name', columns='asset name', values='duration')

        # plot heat map that shows duration by asset name by region
        plt.xlabel('Duration by Asset', fontsize=20)
        plt.xticks(ticks=range(len(pivot.columns.values)), labels=pivot.columns.values)

        plt.ylabel('Region Name', fontsize=20)
        plt.yticks(ticks=np.arange(len(pivot.index), step=10), labels=pivot.index[::10])

        im = plt.imshow(pivot, cmap="YlGnBu", aspect='auto', interpolation='none')
        plt.colorbar(orientation='vertical')