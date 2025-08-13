import pytest
from ansys.stk.extensions.data_analysis.graphs.scenario_graphs import greenwich_hour_angle_line_chart, polewanderx_line_chart, polewandery_line_chart, ut1_utc_line_chart
from stk_environment import stk_root

@pytest.fixture()
def scenario(stk_root):
    stk_root.new_scenario("GraphTest")
    scenario = stk_root.current_scenario
    scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

    yield scenario

@pytest.mark.mpl_image_compare
def test_greenwich_hour_angle_line_chart_scenario(scenario):
    fig, _ = greenwich_hour_angle_line_chart(scenario)
    return fig

@pytest.mark.mpl_image_compare
def test_polewanderx_line_chart_scenario(scenario):
    fig, _ = polewanderx_line_chart(scenario)
    return fig

@pytest.mark.mpl_image_compare
def test_polewandery_line_chart_scenario(scenario):
    fig, _ = polewandery_line_chart(scenario)
    return fig

@pytest.mark.mpl_image_compare
def test_ut1_utc_line_chart_scenario(scenario):
    fig, _ = ut1_utc_line_chart(scenario)
    return fig

