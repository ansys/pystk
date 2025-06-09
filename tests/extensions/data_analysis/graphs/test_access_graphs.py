import pytest

from ansys.stk.extensions.data_analysis.graphs.access_graphs import access_duration_pie_graph, cumulative_dwell_cumulative_pie_graph, revisit_diagram_interval_pie_graph

from stk_environment import stk_root

@pytest.fixture()
def set_up_basic_access_scenario(stk_root):
    from ansys.stk.core.stkobjects import STKObjectType, PropagatorType, ConstraintLighting, AccessConstraintType

    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    facility = scenario.children.new(STKObjectType.FACILITY, "Facility")
    facility.position.assign_planetodetic(39.95, -75.16, 0)


    satellite = scenario.children.new(STKObjectType.SATELLITE, "Satellite")
    satellite.set_propagator_type(PropagatorType.SGP4)
    propagator = satellite.propagator
    propagator.common_tasks.add_segments_from_online_source("25544")
    propagator.propagate()

    lighting_constraint = satellite.access_constraints.add_constraint(
        AccessConstraintType.LIGHTING
    )
    lighting_constraint.condition = ConstraintLighting.DIRECT_SUN

    access = facility.get_access_to_object(satellite)
    access.compute_access()

    yield access

@pytest.mark.mpl_image_compare
def test_access_duration_pie_graph(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = access_duration_pie_graph(access)
    return fig

@pytest.mark.mpl_image_compare
def test_access_duration_pie_graph_non_default_start_stop(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = access_duration_pie_graph(access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_graph(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = cumulative_dwell_cumulative_pie_graph(access)
    return fig

@pytest.mark.mpl_image_compare
def test_cumulative_dwell_cumulative_pie_graph_non_default_start_stop(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = cumulative_dwell_cumulative_pie_graph(access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_graph(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = revisit_diagram_interval_pie_graph(access)
    return fig

@pytest.mark.mpl_image_compare
def test_revisit_diagram_interval_pie_graph_non_default_start_stop(set_up_basic_access_scenario):
    access = set_up_basic_access_scenario
    fig, _ = revisit_diagram_interval_pie_graph(access, start_time="5 Jun 2022 00:00:00.000", stop_time="5 Jun 2022 12:00:00.000")
    return fig