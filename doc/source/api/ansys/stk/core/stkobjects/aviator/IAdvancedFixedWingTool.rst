IAdvancedFixedWingTool
======================

.. py:class:: IAdvancedFixedWingTool

   object
   
   Interface used to access the options for the Advanced Fixed Wing Tool of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create_all_perf_models`
              - Create a set of advanced performance models for the aircraft with the given name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~wing_area`
            * - :py:meth:`~flaps_area`
            * - :py:meth:`~speedbrakes_area`
            * - :py:meth:`~max_altitude`
            * - :py:meth:`~max_mach`
            * - :py:meth:`~max_eas`
            * - :py:meth:`~min_load_factor`
            * - :py:meth:`~max_load_factor`
            * - :py:meth:`~use_max_temperature_limit`
            * - :py:meth:`~max_temperature`
            * - :py:meth:`~cache_aero_data`
            * - :py:meth:`~cache_fuel_flow`
            * - :py:meth:`~aero_strategy`
            * - :py:meth:`~aero_mode_as_external`
            * - :py:meth:`~aero_mode_as_subsonic`
            * - :py:meth:`~aero_mode_as_sub_super_hypersonic`
            * - :py:meth:`~aero_mode_as_supersonic`
            * - :py:meth:`~powerplant_strategy`
            * - :py:meth:`~powerplant_mode_as_electric`
            * - :py:meth:`~powerplant_mode_as_external`
            * - :py:meth:`~powerplant_mode_as_piston`
            * - :py:meth:`~powerplant_mode_as_turboprop`
            * - :py:meth:`~powerplant_mode_as_empirical_jet_engine`
            * - :py:meth:`~powerplant_mode_as_basic_turbofan`
            * - :py:meth:`~powerplant_mode_as_basic_turbojet`
            * - :py:meth:`~powerplant_mode_as_sub_super_hypersonic`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingTool


Property detail
---------------

.. py:property:: wing_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.wing_area
    :type: float

    Gets or sets the total surface area of the wing.

.. py:property:: flaps_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.flaps_area
    :type: float

    Gets or sets the total surface area of the flaps.

.. py:property:: speedbrakes_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.speedbrakes_area
    :type: float

    Gets or sets the total surface area of the speedbrakes.

.. py:property:: max_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.max_altitude
    :type: float

    Gets or sets the maximum altitude of the aircraft.

.. py:property:: max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.max_mach
    :type: float

    Gets or sets the maximum mach number of the aircraft.

.. py:property:: max_eas
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.max_eas
    :type: float

    Gets or sets the maximum equivalent airspeed of the aircraft.

.. py:property:: min_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.min_load_factor
    :type: float

    Gets or sets the minimum load factor the aircraft can bear.

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.max_load_factor
    :type: float

    Gets or sets the maximum load factor the aircraft can bear.

.. py:property:: use_max_temperature_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.use_max_temperature_limit
    :type: bool

    Gets or sets the option to limit the maximum speed of the aircraft so the specified temperature is not exceeded.

.. py:property:: max_temperature
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.max_temperature
    :type: float

    Gets or sets the maximum total temperature limit of the aircraft.

.. py:property:: cache_aero_data
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.cache_aero_data
    :type: bool

    Gets or sets the option to store intermediate results for aerodynamics calculations.

.. py:property:: cache_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.cache_fuel_flow
    :type: bool

    Gets or sets the option to store intermediate results for fuel flow calculations.

.. py:property:: aero_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.aero_strategy
    :type: "ADVANCED_FIXED_WING_AERO_STRATEGY"

    Gets or sets the aerodynamic strategy type.

.. py:property:: aero_mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.aero_mode_as_external
    :type: "IAgAvtrAdvFixedWingExternalAero"

    Get the interface for an Extern File Aerodynamics strategy.

.. py:property:: aero_mode_as_subsonic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.aero_mode_as_subsonic
    :type: "IAgAvtrAdvFixedWingSubsonicAero"

    Get the interface for a Subsonic Aerodynamics strategy.

.. py:property:: aero_mode_as_sub_super_hypersonic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.aero_mode_as_sub_super_hypersonic
    :type: "IAgAvtrAdvFixedWingSubSuperHypersonicAero"

    Get the interface for a Sub/Super/Hypersonic Aerodynamics strategy.

.. py:property:: aero_mode_as_supersonic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.aero_mode_as_supersonic
    :type: "IAgAvtrAdvFixedWingSupersonicAero"

    Get the interface for a Supersonic Aerodynamics strategy.

.. py:property:: powerplant_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_strategy
    :type: "ADVANCED_FIXED_WING_POWERPLANT_STRATEGY"

    Gets or sets the powerplant strategy type.

.. py:property:: powerplant_mode_as_electric
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_electric
    :type: "IAgAvtrAdvFixedWingElectricPowerplant"

    Get the interface for an Electric Powerplant strategy.

.. py:property:: powerplant_mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_external
    :type: "IAgAvtrAdvFixedWingExternalProp"

    Get the interface for an External Prop File Powerplant strategy.

.. py:property:: powerplant_mode_as_piston
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_piston
    :type: "IAgAvtrAdvFixedWingPistonPowerplant"

    Get the interface for a Piston Powerplant strategy.

.. py:property:: powerplant_mode_as_turboprop
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_turboprop
    :type: "IAgAvtrAdvFixedWingTurbopropPowerplant"

    Get the interface for a Turboprop Powerplant strategy.

.. py:property:: powerplant_mode_as_empirical_jet_engine
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_empirical_jet_engine
    :type: "IAgAvtrAdvFixedWingEmpiricalJetEngine"

    Get the interface for an Empirical Jet Engine Powerplant strategy.

.. py:property:: powerplant_mode_as_basic_turbofan
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_basic_turbofan
    :type: "IAgAvtrAdvFixedWingTurbofanBasicABProp"

    Get the interface for a Turbofan - Basic w/ AB Powerplant strategy.

.. py:property:: powerplant_mode_as_basic_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_basic_turbojet
    :type: "IAgAvtrAdvFixedWingTurbojetBasicABProp"

    Get the interface for a Turbojet - Basic w/ AB Powerplant strategy.

.. py:property:: powerplant_mode_as_sub_super_hypersonic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingTool.powerplant_mode_as_sub_super_hypersonic
    :type: "IAgAvtrAdvFixedWingSubSuperHypersonicProp"

    Get the interface for a Sub/Super/Hypersoinc Powerplant strategy.


Method detail
-------------






































.. py:method:: create_all_perf_models(self, name:str, overwrite:bool, makeDefault:bool) -> None

    Create a set of advanced performance models for the aircraft with the given name.

    :Parameters:

    **name** : :obj:`~str`
    **overwrite** : :obj:`~bool`
    **makeDefault** : :obj:`~bool`

    :Returns:

        :obj:`~None`




