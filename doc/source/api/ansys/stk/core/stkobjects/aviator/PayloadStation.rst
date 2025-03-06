PayloadStation
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.PayloadStation

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IStation`

   Class defining a payload station for an Aviator aircraft.

.. py:currentmodule:: PayloadStation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.set_position`
              - Set the payload station's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.remove_sub_item`
              - Remove any sub item that may be attached to the payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.add_external_fuel_tank`
              - Add an external fuel tank to the payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.get_external_fuel_tank`
              - Get the external fuel tank attached to the payload station.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.name`
              - Get or set the name of the payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.position_x`
              - Get the X value of the payload station's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.position_y`
              - Get the Y value of the payload station's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.position_z`
              - Get the Z value of the payload station's parent relative position.



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

    from ansys.stk.core.stkobjects.aviator import PayloadStation


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.name
    :type: str

    Get or set the name of the payload station.

.. py:property:: position_x
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.position_x
    :type: float

    Get the X value of the payload station's parent relative position.

.. py:property:: position_y
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.position_y
    :type: float

    Get the Y value of the payload station's parent relative position.

.. py:property:: position_z
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.position_z
    :type: float

    Get the Z value of the payload station's parent relative position.


Method detail
-------------






.. py:method:: set_position(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.set_position

    Set the payload station's parent relative position.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_sub_item(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.remove_sub_item

    Remove any sub item that may be attached to the payload station.

    :Returns:

        :obj:`~None`

.. py:method:: add_external_fuel_tank(self) -> FuelTankExternal
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.add_external_fuel_tank

    Add an external fuel tank to the payload station.

    :Returns:

        :obj:`~FuelTankExternal`

.. py:method:: get_external_fuel_tank(self) -> FuelTankExternal
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.get_external_fuel_tank

    Get the external fuel tank attached to the payload station.

    :Returns:

        :obj:`~FuelTankExternal`

