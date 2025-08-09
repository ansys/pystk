AdvancedFixedWingTurbofanBasicABPropulsion
==========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion

   Class defining the Turbofan - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingTurbofanBasicABPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.afterburner_on`
              - Opt whether to specify the design point with the afterburner on.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.can_use_afterburner`
              - Opt whether the engine has an afterburner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.design_altitude`
              - Get or set the altitude design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.design_mach`
              - Get or set the mach number design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.design_thrust`
              - Get or set the thrust design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.efficiencies_and_losses`
              - Get the jet engine's propulsion efficiencies and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fan_pressure_ratio`
              - Get or set the pressure ratio of the fan.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fuel_mode_as_afprop`
              - Get the interface for a Kerosene - AFPROP fuel mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fuel_mode_as_cea`
              - Get the interface for a Kerosene - CEA fuel mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fuel_type`
              - Get or set the jet engine's fuel type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.hpc_pressure_ratio`
              - Get or set the pressure ratio of the high-pressure compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.lpc_pressure_ratio`
              - Get or set the pressure ratio of the low-pressure compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.max_afterburner_temp`
              - Get or set the maximum temperature at the afterburner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.max_burner_temp`
              - Get or set the maximum temperature at the combustion stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.max_compression_temp`
              - Get or set the maximum temperature at the compressor stage.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingTurbofanBasicABPropulsion


Property detail
---------------

.. py:property:: afterburner_on
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.afterburner_on
    :type: bool

    Opt whether to specify the design point with the afterburner on.

.. py:property:: can_use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.can_use_afterburner
    :type: bool

    Opt whether the engine has an afterburner.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.design_altitude
    :type: float

    Get or set the altitude design point of the engine.

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.design_mach
    :type: float

    Get or set the mach number design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.design_thrust
    :type: float

    Get or set the thrust design point of the engine.

.. py:property:: efficiencies_and_losses
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.efficiencies_and_losses
    :type: PropulsionEfficiencies

    Get the jet engine's propulsion efficiencies and losses.

.. py:property:: fan_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fan_pressure_ratio
    :type: float

    Get or set the pressure ratio of the fan.

.. py:property:: fuel_mode_as_afprop
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fuel_mode_as_afprop
    :type: FuelModelKeroseneAFPROP

    Get the interface for a Kerosene - AFPROP fuel mode.

.. py:property:: fuel_mode_as_cea
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fuel_mode_as_cea
    :type: FuelModelKeroseneCEA

    Get the interface for a Kerosene - CEA fuel mode.

.. py:property:: fuel_type
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.fuel_type
    :type: JetFuelType

    Get or set the jet engine's fuel type.

.. py:property:: hpc_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.hpc_pressure_ratio
    :type: float

    Get or set the pressure ratio of the high-pressure compressor.

.. py:property:: lpc_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.lpc_pressure_ratio
    :type: float

    Get or set the pressure ratio of the low-pressure compressor.

.. py:property:: max_afterburner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.max_afterburner_temp
    :type: float

    Get or set the maximum temperature at the afterburner.

.. py:property:: max_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.max_burner_temp
    :type: float

    Get or set the maximum temperature at the combustion stage.

.. py:property:: max_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbofanBasicABPropulsion.max_compression_temp
    :type: float

    Get or set the maximum temperature at the compressor stage.


