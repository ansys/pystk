FuelTankExternal
================

.. py:class:: ansys.stk.core.stkobjects.aviator.FuelTankExternal

   Class defining an external fuel tank for an Aviator aircraft.

.. py:currentmodule:: FuelTankExternal

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal.capacity`
              - Get or set the capacity of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal.consumption_order`
              - Get or set the consumption order of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal.drag_index`
              - Get or set the drag index of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal.empty_weight`
              - Get or set the empty weight of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal.initial_fuel_state`
              - Get or set the initial fuel state of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankExternal.name`
              - Get or set the name of the fuel tank.



Examples
--------

Set the Configuration used for the Mission

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the configuration used for the mission
    configuration = mission.configuration
    # Set the max landing weight
    configuration.max_landing_weight = 300000
    # Set the empty weight
    configuration.empty_weight = 210000
    # Update the center of gravity of the aircraft when empty
    configuration.set_empty_cg(2, 0, 1)

    # Get the stations
    stations = configuration.get_stations()
    # Check if there is an internal fuel station
    if stations.contains_station("Internal Fuel") is True:
        # Get the fuel tank
        fuelTank = stations.get_internal_fuel_tank_by_name("Internal Fuel")
        # Set the capacity of the fuel tank
        fuelTank.capacity = 175000
        # Set the initial state of the fuel tank
        fuelTank.initial_fuel_state = 125000

    # Add a new payload station
    newPayload = stations.add_payload_station()
    # Set the position of the payload station
    newPayload.set_position(0, 2, 0)
    # Add an external fuel tank
    externalTank = newPayload.add_external_fuel_tank()
    # Set the empty weight of the tank
    externalTank.empty_weight = 2000


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import FuelTankExternal


Property detail
---------------

.. py:property:: capacity
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankExternal.capacity
    :type: float

    Get or set the capacity of the fuel tank.

.. py:property:: consumption_order
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankExternal.consumption_order
    :type: int

    Get or set the consumption order of the fuel tank.

.. py:property:: drag_index
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankExternal.drag_index
    :type: float

    Get or set the drag index of the fuel tank.

.. py:property:: empty_weight
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankExternal.empty_weight
    :type: float

    Get or set the empty weight of the fuel tank.

.. py:property:: initial_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankExternal.initial_fuel_state
    :type: float

    Get or set the initial fuel state of the fuel tank.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankExternal.name
    :type: str

    Get or set the name of the fuel tank.


