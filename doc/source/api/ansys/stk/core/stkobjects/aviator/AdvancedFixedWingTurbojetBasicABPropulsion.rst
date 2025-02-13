AdvancedFixedWingTurbojetBasicABPropulsion
==========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion

   Class defining the Turbojet - Basic w/AB (Thermodynamic model) powerplant in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingTurbojetBasicABPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.can_use_afterburner`
              - Opt whether the engine has an afterburner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.design_altitude`
              - Get or set the altitude design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.design_mach`
              - Get or set the mach number design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.design_thrust`
              - Get or set the thrust design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.afterburner_on`
              - Opt whether to specify the design point with the afterburner on.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.max_compression_temp`
              - Get or set the maximum temperature at the compressor stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.max_burner_temp`
              - Get or set the maximum temperature at the combustion stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.max_afterburner_temp`
              - Get or set the maximum temperature at the afterburner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.hpc_pressure_ratio`
              - Get or set the pressure ratio of the high-pressure compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.lpc_pressure_ratio`
              - Get or set the pressure ratio of the low-pressure compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.efficiencies_and_losses`
              - Get the jet engine's propulsion efficiencies and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.fuel_type`
              - Get or set the jet engine's fuel type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.fuel_mode_as_afprop`
              - Get the interface for a Kerosene - AFPROP fuel mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.fuel_mode_as_cea`
              - Get the interface for a Kerosene - CEA fuel mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingTurbojetBasicABPropulsion


Property detail
---------------

.. py:property:: can_use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.can_use_afterburner
    :type: bool

    Opt whether the engine has an afterburner.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.design_altitude
    :type: float

    Get or set the altitude design point of the engine.

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.design_mach
    :type: float

    Get or set the mach number design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.design_thrust
    :type: float

    Get or set the thrust design point of the engine.

.. py:property:: afterburner_on
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.afterburner_on
    :type: bool

    Opt whether to specify the design point with the afterburner on.

.. py:property:: max_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.max_compression_temp
    :type: float

    Get or set the maximum temperature at the compressor stage.

.. py:property:: max_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.max_burner_temp
    :type: float

    Get or set the maximum temperature at the combustion stage.

.. py:property:: max_afterburner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.max_afterburner_temp
    :type: float

    Get or set the maximum temperature at the afterburner.

.. py:property:: hpc_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.hpc_pressure_ratio
    :type: float

    Get or set the pressure ratio of the high-pressure compressor.

.. py:property:: lpc_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.lpc_pressure_ratio
    :type: float

    Get or set the pressure ratio of the low-pressure compressor.

.. py:property:: efficiencies_and_losses
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.efficiencies_and_losses
    :type: PropulsionEfficiencies

    Get the jet engine's propulsion efficiencies and losses.

.. py:property:: fuel_type
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.fuel_type
    :type: JetFuelType

    Get or set the jet engine's fuel type.

.. py:property:: fuel_mode_as_afprop
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.fuel_mode_as_afprop
    :type: FuelModelKeroseneAFPROP

    Get the interface for a Kerosene - AFPROP fuel mode.

.. py:property:: fuel_mode_as_cea
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTurbojetBasicABPropulsion.fuel_mode_as_cea
    :type: FuelModelKeroseneCEA

    Get the interface for a Kerosene - CEA fuel mode.


