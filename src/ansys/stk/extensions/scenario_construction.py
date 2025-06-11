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

"""
PySTK Scenario Construction Extensions.

A set of convenience utilities to facilitate the construction of scenarios.
"""

from ansys.stk.core.stkobjects import ISTKObject, Scenario, STKObjectRoot, STKObjectType


def construct_scenario_from_dict(root: STKObjectRoot, dictionary: dict) -> Scenario:
    """Create a scenario with sub-objects from a dictionary describing its structure.

    The dictionary represents a hierarchy of nodes, where each node has a type, a name, and children. The type
    is case insensitive and corresponds to the values in the STKObjectType enumeration.

    Examples
    --------
    Construct a scenario with a place and a sensor attached to it:
    >>> scenario = construct_scenario_from_dict(
    >>>     root,
    >>>     {
    >>>         "type": "Scenario",
    >>>         "name": "MyScenario",
    >>>         "children": [
    >>>             {
    >>>                 "type": "Place",
    >>>                 "name": "MyPlace",
    >>>                 "children": [
    >>>                     {
    >>>                         "type": "Sensor",
    >>>                         "name": "MySensor",
    >>>                         "children": []
    >>>                     }
    >>>                  ]
    >>>             }
    >>>         ]
    >>>     })

    Parameters
    ----------
    root : ansys.stk.core.stkobjects.STKObjectRoot
        The STK object root.
    dict : dict
        A dictionary describing the scenario to construct.

    Returns
    -------
    ansys.stk.core.stkobjects.Scenario
        The newly created scenario.

    Raises
    ------
    RuntimeError
        If the dictionary does not have the proper structure.
    """

    def _validate_node(node):
        if "name" not in node:
            raise RuntimeError("Unexpected dictionary structure, missing 'name'")

        if "type" not in node:
            raise RuntimeError("Unexpected dictionary structure, missing 'type'")

        if "children" not in node:
            raise RuntimeError("Unexpected dictionary structure, missing 'children'")

        if len(node) != 3:
            raise RuntimeError("Unexpected dictionary structure, expected 3 entries")

    def _create_object(parent: ISTKObject, node: dict):
        for child in node["children"]:
            _validate_node(child)
            new_object_type_name: str = child["type"].upper()
            if new_object_type_name in STKObjectType.__dict__:
                new_object_type: STKObjectType = STKObjectType.__dict__[new_object_type_name]
                new_object_name: str = child["name"]
                new_object = parent.children.new(new_object_type, new_object_name)
                _create_object(new_object, child)
            else:
                raise RuntimeError(f"{new_object_type_name} is not a valid STK object type")

    if root.current_scenario is not None:
        root.close_scenario()

    _validate_node(dictionary)

    root.new_scenario(dictionary["name"])
    scenario: ISTKObject = root.current_scenario
    _create_object(parent=scenario, node=dictionary)

    return Scenario(root.current_scenario)
