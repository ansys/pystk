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
#

# """Test the `scenario_construction.construct_scenario_from_dict` function."""

import pytest

from ansys.stk.extensions.scenario_construction import construct_scenario_from_dict
from ansys.stk.core.stkobjects import Scenario, Place, Sensor, STKObjectType, Antenna

from stk_environment import stk_root


def test_construct_scenario_from_dict_empty_scenario(stk_root):
    scenario = construct_scenario_from_dict(stk_root, {"type": "Scenario", "name": "MyScenario", "children": []})

    assert scenario is not None
    assert isinstance(scenario, Scenario)
    assert scenario.instance_name == "MyScenario"
    assert scenario.children.count == 0


def test_construct_scenario_from_dict_scenario_with_a_place(stk_root):
    scenario = construct_scenario_from_dict(
        stk_root,
        {"type": "Scenario", "name": "MyScenario", "children": [{"type": "Place", "name": "MyPlace", "children": []}]},
    )

    assert scenario is not None
    assert isinstance(scenario, Scenario)
    assert scenario.instance_name == "MyScenario"
    assert scenario.children.count == 1

    assert isinstance(scenario.children[0], Place)
    assert scenario.children[0].instance_name == "MyPlace"
    assert scenario.children[0].children.count == 0


def test_construct_scenario_from_dict_scenario_with_a_place_and_a_sensor(stk_root):
    scenario = construct_scenario_from_dict(
        stk_root,
        {
            "type": "Scenario",
            "name": "MyScenario",
            "children": [
                {
                    "type": "Place",
                    "name": "MyPlace",
                    "children": [
                        {
                            "type": "Sensor",
                            "name": "MySensor",
                            "children": [],
                        }
                    ],
                }
            ],
        },
    )

    assert scenario is not None
    assert isinstance(scenario, Scenario)
    assert scenario.instance_name == "MyScenario"
    assert scenario.children.count == 1

    assert isinstance(scenario.children[0], Place)
    assert scenario.children[0].instance_name == "MyPlace"
    assert scenario.children[0].children.count == 1

    assert isinstance(scenario.children[0].children[0], Sensor)
    assert scenario.children[0].children[0].instance_name == "MySensor"
    assert scenario.children[0].children[0].children.count == 0


@pytest.mark.parametrize(
    "child_type",
    [
        STKObjectType.ADVCAT,
        STKObjectType.AIRCRAFT,
        STKObjectType.AREA_TARGET,
        STKObjectType.CHAIN,
        STKObjectType.COMM_SYSTEM,
        STKObjectType.CONSTELLATION,
        STKObjectType.COVERAGE_DEFINITION,
        STKObjectType.FACILITY,
        STKObjectType.GROUND_VEHICLE,
        STKObjectType.LAUNCH_VEHICLE,
        STKObjectType.LINE_TARGET,
        STKObjectType.MTO,
        STKObjectType.PLACE,
        STKObjectType.PLANET,
        STKObjectType.SATELLITE,
        STKObjectType.SHIP,
        STKObjectType.STAR,
        STKObjectType.TARGET,
        STKObjectType.VOLUMETRIC,
    ],
)
def test_construct_scenario_from_dict_scenario_top_level_objects(stk_root, child_type: STKObjectType):
    scenario = construct_scenario_from_dict(
        stk_root,
        {
            "type": "Scenario",
            "name": "MyScenario",
            "children": [{"type": f"{child_type.name}", "name": "obj", "children": []}],
        },
    )

    assert scenario is not None
    assert isinstance(scenario, Scenario)
    assert scenario.instance_name == "MyScenario"
    assert scenario.children.count == 1

    assert scenario.children[0].class_type == child_type
    assert scenario.children[0].instance_name == "obj"
    assert scenario.children[0].children.count == 0


@pytest.mark.parametrize(
    "parent_type, child_type",
    [
        (STKObjectType.PLACE, STKObjectType.ANTENNA),
        (STKObjectType.PLACE, STKObjectType.RADAR),
        (STKObjectType.PLACE, STKObjectType.RECEIVER),
        (STKObjectType.PLACE, STKObjectType.SENSOR),
        (STKObjectType.PLACE, STKObjectType.TRANSMITTER),
        (STKObjectType.COVERAGE_DEFINITION, STKObjectType.FIGURE_OF_MERIT),
    ],
)
def test_construct_scenario_from_dict_scenario_attached_objects(
    stk_root, parent_type: STKObjectType, child_type: STKObjectType
):
    scenario = construct_scenario_from_dict(
        stk_root,
        {
            "type": "Scenario",
            "name": "MyScenario",
            "children": [
                {
                    "type": f"{parent_type.name}",
                    "name": "parent",
                    "children": [
                        {
                            "type": f"{child_type.name}",
                            "name": "attached_object",
                            "children": [],
                        }
                    ],
                }
            ],
        },
    )

    assert scenario is not None
    assert isinstance(scenario, Scenario)
    assert scenario.instance_name == "MyScenario"
    assert scenario.children.count == 1

    assert scenario.children[0].class_type == parent_type
    assert scenario.children[0].instance_name == "parent"
    assert scenario.children[0].children.count == 1

    assert scenario.children[0].children[0].class_type == child_type
    assert scenario.children[0].children[0].instance_name == "attached_object"
    assert scenario.children[0].children[0].children.count == 0


def test_construct_scenario_from_dict_max_depth(stk_root):
    scenario = construct_scenario_from_dict(
        stk_root,
        {
            "type": "Scenario",
            "name": "MyScenario",
            "children": [
                {
                    "type": "Place",
                    "name": "MyPlace",
                    "children": [
                        {
                            "type": "Sensor",
                            "name": "MySensor",
                            "children": [{"type": "Antenna", "name": "MyAntenna", "children": []}],
                        }
                    ],
                }
            ],
        },
    )

    assert scenario is not None
    assert isinstance(scenario, Scenario)
    assert scenario.instance_name == "MyScenario"
    assert scenario.children.count == 1

    assert isinstance(scenario.children[0], Place)
    assert scenario.children[0].instance_name == "MyPlace"
    assert scenario.children[0].children.count == 1

    assert isinstance(scenario.children[0].children[0], Sensor)
    assert scenario.children[0].children[0].instance_name == "MySensor"
    assert scenario.children[0].children[0].children.count == 1

    assert isinstance(scenario.children[0].children[0].children[0], Antenna)
    assert scenario.children[0].children[0].children[0].instance_name == "MyAntenna"
    assert scenario.children[0].children[0].children[0].children.count == 0


def test_construct_scenario_from_dict_invalid_type(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "type": "Scenario",
                "name": "MyScenario",
                "children": [{"type": "BadType", "name": "MyPlace", "children": []}],
            },
        )

    assert "BADTYPE is not a valid STK object type" in str(excinfo.value)


def test_construct_scenario_from_dict_missing_child_name(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "type": "Scenario",
                "name": "MyScenario",
                "children": [{"type": "facility", "children": []}],
            },
        )

    assert "Unexpected dictionary structure, missing 'name'" in str(excinfo.value)


def test_construct_scenario_from_dict_missing_scenario_name(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "type": "Scenario",
                "children": [{"type": "facility", "name": "MyFacility", "children": []}],
            },
        )

    assert "Unexpected dictionary structure, missing 'name'" in str(excinfo.value)


def test_construct_scenario_from_dict_missing_child_children(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "type": "Scenario",
                "name": "MyScenario",
                "children": [
                    {
                        "type": "facility",
                        "name": "MyFacility",
                    }
                ],
            },
        )

    assert "Unexpected dictionary structure, missing 'children'" in str(excinfo.value)


def test_construct_scenario_from_dict_missing_scenario_children(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "type": "Scenario",
                "name": "MyScenario",
            },
        )

    assert "Unexpected dictionary structure, missing 'children'" in str(excinfo.value)


def test_construct_scenario_from_dict_missing_child_type(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "type": "Scenario",
                "name": "MyScenario",
                "children": [
                    {
                        "name": "MyFacility",
                        "children": [],
                    }
                ],
            },
        )

    assert "Unexpected dictionary structure, missing 'type'" in str(excinfo.value)


def test_construct_scenario_from_dict_missing_scenario_type(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {
                "name": "MyScenario",
                "children": [],
            },
        )

    assert "Unexpected dictionary structure, missing 'type'" in str(excinfo.value)


def test_construct_scenario_from_dict_extra_keys(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {"type": "Scenario", "name": "MyScenario", "children": [], "one_more": True},
        )

    assert "Unexpected dictionary structure, expected 3 entries" in str(excinfo.value)


def test_construct_scenario_from_dict_invalid_name(stk_root):
    with pytest.raises(RuntimeError) as excinfo:
        scenario = construct_scenario_from_dict(
            stk_root,
            {"type": "Scenario", "name": "MyBack\\slash", "children": []},
        )

    assert "Instance name MyBack\\slash incorrectly formatted" in str(excinfo.value)
