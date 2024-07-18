AdvancedFixedWingRamjetBasic
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic

   Bases: 

   Class defining the basic Ramjet model.

.. py:currentmodule:: AdvancedFixedWingRamjetBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.design_altitude`
              - Gets or sets the altitude design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.design_mach`
              - Gets or sets the mach number design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.design_thrust`
              - Gets or sets the thrust design point of the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.max_compression_temp`
              - Gets or sets the maximum temperature at the compressor stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.max_burner_temp`
              - Gets or sets the maximum temperature at the combustion stage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.fuel_type`
              - Gets or sets the jet engine's fuel type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.fuel_mode_as_afprop`
              - Get the interface for a Kerosene - AFPROP fuel mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.fuel_mode_as_cea`
              - Get the interface for a Kerosene - CEA fuel mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.efficiencies_and_losses`
              - Get the jet engine's propulsion efficiencies and losses.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingRamjetBasic


Property detail
---------------

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.design_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.design_mach
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.design_thrust
    :type: float

    Gets or sets the thrust design point of the engine.

.. py:property:: max_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.max_compression_temp
    :type: float

    Gets or sets the maximum temperature at the compressor stage.

.. py:property:: max_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.max_burner_temp
    :type: float

    Gets or sets the maximum temperature at the combustion stage.

.. py:property:: fuel_type
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.fuel_type
    :type: JET_FUEL_TYPE

    Gets or sets the jet engine's fuel type.

.. py:property:: fuel_mode_as_afprop
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.fuel_mode_as_afprop
    :type: IFuelModelKeroseneAFPROP

    Get the interface for a Kerosene - AFPROP fuel mode.

.. py:property:: fuel_mode_as_cea
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.fuel_mode_as_cea
    :type: IFuelModelKeroseneCEA

    Get the interface for a Kerosene - CEA fuel mode.

.. py:property:: efficiencies_and_losses
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingRamjetBasic.efficiencies_and_losses
    :type: IPropulsionEfficiencies

    Get the jet engine's propulsion efficiencies and losses.


