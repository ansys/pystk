IAdvancedFixedWingTurbofanBasicABProp
=====================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp

   object
   
   Interface used to access the options for the Turbofan - Basic w/AB (Thermodynamic) powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: IAdvancedFixedWingTurbofanBasicABProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.can_use_afterburner`
              - Opt whether the engine has an afterburner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.design_altitude`
              - Gets or sets the altitude design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.design_mach`
              - Gets or sets the mach number design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.design_thrust`
              - Gets or sets the thrust design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.afterburner_on`
              - Opt whether to specify the design point with the afterburner on.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.max_compression_temp`
              - Gets or sets the maximum temperature at the compressor stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.max_burner_temp`
              - Gets or sets the maximum temperature at the combustion stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.max_afterburner_temp`
              - Gets or sets the maximum temperature at the afterburner.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.hpc_pressure_ratio`
              - Gets or sets the pressure ratio of the high-pressure compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.lpc_pressure_ratio`
              - Gets or sets the pressure ratio of the low-pressure compressor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fan_pressure_ratio`
              - Gets or sets the pressure ratio of the fan.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.efficiencies_and_losses`
              - Get the jet engine's propulsion efficiencies and losses.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fuel_type`
              - Gets or sets the jet engine's fuel type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fuel_mode_as_afprop`
              - Get the interface for a Kerosene - AFPROP fuel mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fuel_mode_as_cea`
              - Get the interface for a Kerosene - CEA fuel mode.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingTurbofanBasicABProp


Property detail
---------------

.. py:property:: can_use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.can_use_afterburner
    :type: bool

    Opt whether the engine has an afterburner.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.design_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.design_mach
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.design_thrust
    :type: float

    Gets or sets the thrust design point of the engine.

.. py:property:: afterburner_on
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.afterburner_on
    :type: bool

    Opt whether to specify the design point with the afterburner on.

.. py:property:: max_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.max_compression_temp
    :type: float

    Gets or sets the maximum temperature at the compressor stage.

.. py:property:: max_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.max_burner_temp
    :type: float

    Gets or sets the maximum temperature at the combustion stage.

.. py:property:: max_afterburner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.max_afterburner_temp
    :type: float

    Gets or sets the maximum temperature at the afterburner.

.. py:property:: hpc_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.hpc_pressure_ratio
    :type: float

    Gets or sets the pressure ratio of the high-pressure compressor.

.. py:property:: lpc_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.lpc_pressure_ratio
    :type: float

    Gets or sets the pressure ratio of the low-pressure compressor.

.. py:property:: fan_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fan_pressure_ratio
    :type: float

    Gets or sets the pressure ratio of the fan.

.. py:property:: efficiencies_and_losses
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.efficiencies_and_losses
    :type: IPropulsionEfficiencies

    Get the jet engine's propulsion efficiencies and losses.

.. py:property:: fuel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fuel_type
    :type: JET_FUEL_TYPE

    Gets or sets the jet engine's fuel type.

.. py:property:: fuel_mode_as_afprop
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fuel_mode_as_afprop
    :type: IFuelModelKeroseneAFPROP

    Get the interface for a Kerosene - AFPROP fuel mode.

.. py:property:: fuel_mode_as_cea
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTurbofanBasicABProp.fuel_mode_as_cea
    :type: IFuelModelKeroseneCEA

    Get the interface for a Kerosene - CEA fuel mode.


