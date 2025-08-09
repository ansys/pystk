MissileTurbojetPropulsion
=========================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion

   Class defining the Turbojet propulsion options for a missile.

.. py:currentmodule:: MissileTurbojetPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.design_mach`
              - Get or set the mach number design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.design_altitude`
              - Get or set the altitude design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.design_thrust`
              - Get or set the thrust design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.turbine_temp`
              - Get or set the maximum temperature that the turbine material can support.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.compressor_pressure_ratio`
              - Get or set the maximum compressor pressure ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.fuel_heating_value`
              - Get or set the heating value of the fuel.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.inlet_subsonic_pressure_ratio`
              - Get or set the subsonic pressure ratio from the inlet exit to the entrance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.burner_pressure_ratio`
              - Get or set the pressure ratio from the burner exit to the entrance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.nozzle_pressure_ratio`
              - Get or set the pressure ratio from the nozzle exit to the entrance.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.p_0over_p9`
              - Get or set the pressure ratio from ambient conditions to the engine exit.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.compressor_efficiency`
              - Get or set the efficiency of the compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.turbine_efficiency`
              - Get or set the efficiency of the turbine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.burner_efficiency`
              - Get or set the efficiency of the burner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.mechanical_efficiency`
              - Get or set the mechanical efficiency of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.no_thrust_when_no_fuel`
              - Opt to have no thrust if the fuel is empty.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileTurbojetPropulsion


Property detail
---------------

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.design_mach
    :type: float

    Get or set the mach number design point of the engine.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.design_altitude
    :type: float

    Get or set the altitude design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.design_thrust
    :type: float

    Get or set the thrust design point of the engine.

.. py:property:: turbine_temp
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.turbine_temp
    :type: float

    Get or set the maximum temperature that the turbine material can support.

.. py:property:: compressor_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.compressor_pressure_ratio
    :type: float

    Get or set the maximum compressor pressure ratio.

.. py:property:: fuel_heating_value
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.fuel_heating_value
    :type: float

    Get or set the heating value of the fuel.

.. py:property:: inlet_subsonic_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.inlet_subsonic_pressure_ratio
    :type: float

    Get or set the subsonic pressure ratio from the inlet exit to the entrance.

.. py:property:: burner_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.burner_pressure_ratio
    :type: float

    Get or set the pressure ratio from the burner exit to the entrance.

.. py:property:: nozzle_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.nozzle_pressure_ratio
    :type: float

    Get or set the pressure ratio from the nozzle exit to the entrance.

.. py:property:: p_0over_p9
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.p_0over_p9
    :type: float

    Get or set the pressure ratio from ambient conditions to the engine exit.

.. py:property:: compressor_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.compressor_efficiency
    :type: float

    Get or set the efficiency of the compressor.

.. py:property:: turbine_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.turbine_efficiency
    :type: float

    Get or set the efficiency of the turbine.

.. py:property:: burner_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.burner_efficiency
    :type: float

    Get or set the efficiency of the burner.

.. py:property:: mechanical_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.mechanical_efficiency
    :type: float

    Get or set the mechanical efficiency of the engine.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.MissileTurbojetPropulsion.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


