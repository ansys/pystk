construct_scenario_from_dict
============================

.. py:function:: construct_scenario_from_dict(root: StkObjectRoot, dict: Dict) -> Scenario
    :canonical: ansys.stk.extensions.scenario_construction.construct_scenario_from_dict

    Create a scenario with sub-objects from a dictionary describing its structure.

    The dictionary represents a hierarchy of nodes, where each node has a type, a name, and children. The type
    is case insensitive and corresponds to the values in the STKObjectType enumeration.

    :Parameters:

        **root** : :obj:`~StkObjectRoot`
        The STK object root.

        **dict** : :obj:`~Dict`
        A dictionary describing the scenario to construct.


    :Returns:

        :obj:`~Scenario`
        The newly created scenario.

    :Raises:

        :obj:`~RuntimeException`
        If the dictionary does not have the proper structure.

    :Examples:

      Construct a scenario with a place and a sensor attached to it:

      .. code-block:: python

        scenario = construct_scenario_from_dict(
            root,
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
                                "children": []
                            }
                         ]
                    }
                ]
            })

.. py:currentmodule:: construct_scenario_from_dict


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.scenario_construction import construct_scenario_from_dict


