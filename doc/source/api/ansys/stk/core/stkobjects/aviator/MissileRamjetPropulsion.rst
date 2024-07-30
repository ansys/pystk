MissileRamjetPropulsion
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion

   Bases: 

   Class defining the Ramjet propulsion options for a missile.

.. py:currentmodule:: MissileRamjetPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.design_mach`
              - Gets or sets the mach number design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.design_altitude`
              - Gets or sets the altitude design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.design_thrust`
              - Gets or sets the thrust design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.engine_temp`
              - Gets or sets the maximum temperature that the engine material can support.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.fuel_heating_value`
              - Gets or sets the heating value of the fuel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.inlet_pressure_ratio`
              - Gets or sets the pressure ratio from the inlet exit to the entrance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.burner_pressure_ratio`
              - Gets or sets the pressure ratio from the burner exit to the entrance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.nozzle_pressure_ratio`
              - Gets or sets the pressure ratio from the nozzle exit to the entrance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.p_0over_p9`
              - Gets or sets the pressure ratio from ambient conditions to the engine exit.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.burner_efficiency`
              - Gets or sets the efficiency of the burner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.no_thrust_when_no_fuel`
              - Opt to have no thrust if the fuel is empty.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileRamjetPropulsion


Property detail
---------------

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.design_mach
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.design_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.design_thrust
    :type: float

    Gets or sets the thrust design point of the engine.

.. py:property:: engine_temp
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.engine_temp
    :type: float

    Gets or sets the maximum temperature that the engine material can support.

.. py:property:: fuel_heating_value
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.fuel_heating_value
    :type: float

    Gets or sets the heating value of the fuel.

.. py:property:: inlet_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.inlet_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the inlet exit to the entrance.

.. py:property:: burner_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.burner_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the burner exit to the entrance.

.. py:property:: nozzle_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.nozzle_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the nozzle exit to the entrance.

.. py:property:: p_0over_p9
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.p_0over_p9
    :type: float

    Gets or sets the pressure ratio from ambient conditions to the engine exit.

.. py:property:: burner_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.burner_efficiency
    :type: float

    Gets or sets the efficiency of the burner.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.MissileRamjetPropulsion.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


