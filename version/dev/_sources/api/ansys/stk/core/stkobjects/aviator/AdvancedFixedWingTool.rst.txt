AdvancedFixedWingTool
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool

   Class defining the options for the Advanced Fixed Wing Tool of an aircraft.

.. py:currentmodule:: AdvancedFixedWingTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.create_all_performance_models`
              - Create a set of advanced performance models for the aircraft with the given name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_external`
              - Get the interface for an Extern File Aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_four_point`
              - Get the interface for a Four Point Aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_sub_super_hypersonic`
              - Get the interface for a Sub/Super/Hypersonic Aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_subsonic`
              - Get the interface for a Subsonic Aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_supersonic`
              - Get the interface for a Supersonic Aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_strategy`
              - Get or set the aerodynamic strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.cache_aerodynamic_data`
              - Get or set the option to store intermediate results for aerodynamics calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.cache_fuel_flow`
              - Get or set the option to store intermediate results for fuel flow calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.flaps_area`
              - Get or set the total surface area of the flaps.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_altitude`
              - Get or set the maximum altitude of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_eas`
              - Get or set the maximum equivalent airspeed of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_load_factor`
              - Get or set the maximum load factor the aircraft can bear.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_mach`
              - Get or set the maximum mach number of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_temperature`
              - Get or set the maximum total temperature limit of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.min_load_factor`
              - Get or set the minimum load factor the aircraft can bear.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_basic_turbofan`
              - Get the interface for a Turbofan - Basic w/ AB Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_basic_turbojet`
              - Get the interface for a Turbojet - Basic w/ AB Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_electric`
              - Get the interface for an Electric Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_empirical_jet_engine`
              - Get the interface for an Empirical Jet Engine Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_external`
              - Get the interface for an External Prop File Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_piston`
              - Get the interface for a Piston Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_sub_super_hypersonic`
              - Get the interface for a Sub/Super/Hypersoinc Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_turboprop`
              - Get the interface for a Turboprop Powerplant strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_strategy`
              - Get or set the powerplant strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.speedbrakes_area`
              - Get or set the total surface area of the speedbrakes.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.use_max_temperature_limit`
              - Get or set the option to limit the maximum speed of the aircraft so the specified temperature is not exceeded.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.wing_area`
              - Get or set the total surface area of the wing.



Examples
--------

Configure the Advanced Fixed Wing Tool and set the aircraft to use the resulting performance models

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the advanced fixed wing tool
    advFixedWingTool = aviatorAircraft.advanced_fixed_wing_tool
    # Set the basic geometry
    advFixedWingTool.wing_area = 300
    advFixedWingTool.flaps_area = 50
    advFixedWingTool.speedbrakes_area = 10
    # Set the structural and human factor limits
    advFixedWingTool.max_altitude = 65000
    advFixedWingTool.max_mach = 0.98
    advFixedWingTool.max_eas = 460
    advFixedWingTool.min_load_factor = -2.5
    advFixedWingTool.max_load_factor = 4.5

    # Opt to enforce the max temperature limit
    advFixedWingTool.use_max_temperature_limit = True
    advFixedWingTool.max_temperature = 900

    # Use a subsonic aerodynamic strategy
    advFixedWingTool.aerodynamic_strategy = AdvancedFixedWingAerodynamicStrategy.SUBSONIC_AERODYNAMIC
    # Cache the aerodynamic data to improve calculation speed
    advFixedWingTool.cache_aerodynamic_data = True
    # Use a high bypass turbofan
    advFixedWingTool.powerplant_strategy = AdvancedFixedWingPowerplantStrategy.TURBOFAN_HIGH_BYPASS
    # Cache the fuel flow data to improve calculation speed
    advFixedWingTool.cache_fuel_flow = True

    # Create the corresponding performance models that reference the advanced fixed wing tool
    # Specify the name, whether to override any existing models with the same name, and whether to set the new models as the default performance models
    advFixedWingTool.create_all_performance_models("AdvancedModels", True, True)

    # Save the changes in the catalog
    aviatorAircraft.save()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingTool


Property detail
---------------

.. py:property:: aerodynamic_mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_external
    :type: AdvancedFixedWingExternalAerodynamic

    Get the interface for an Extern File Aerodynamics strategy.

.. py:property:: aerodynamic_mode_as_four_point
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_four_point
    :type: AdvancedFixedWingFourPointAerodynamic

    Get the interface for a Four Point Aerodynamics strategy.

.. py:property:: aerodynamic_mode_as_sub_super_hypersonic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_sub_super_hypersonic
    :type: AdvancedFixedWingSubSuperHypersonicAerodynamic

    Get the interface for a Sub/Super/Hypersonic Aerodynamics strategy.

.. py:property:: aerodynamic_mode_as_subsonic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_subsonic
    :type: AdvancedFixedWingSubsonicAerodynamic

    Get the interface for a Subsonic Aerodynamics strategy.

.. py:property:: aerodynamic_mode_as_supersonic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_mode_as_supersonic
    :type: AdvancedFixedWingSupersonicAerodynamic

    Get the interface for a Supersonic Aerodynamics strategy.

.. py:property:: aerodynamic_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.aerodynamic_strategy
    :type: AdvancedFixedWingAerodynamicStrategy

    Get or set the aerodynamic strategy type.

.. py:property:: cache_aerodynamic_data
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.cache_aerodynamic_data
    :type: bool

    Get or set the option to store intermediate results for aerodynamics calculations.

.. py:property:: cache_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.cache_fuel_flow
    :type: bool

    Get or set the option to store intermediate results for fuel flow calculations.

.. py:property:: flaps_area
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.flaps_area
    :type: float

    Get or set the total surface area of the flaps.

.. py:property:: max_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_altitude
    :type: float

    Get or set the maximum altitude of the aircraft.

.. py:property:: max_eas
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_eas
    :type: float

    Get or set the maximum equivalent airspeed of the aircraft.

.. py:property:: max_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_load_factor
    :type: float

    Get or set the maximum load factor the aircraft can bear.

.. py:property:: max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_mach
    :type: float

    Get or set the maximum mach number of the aircraft.

.. py:property:: max_temperature
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.max_temperature
    :type: float

    Get or set the maximum total temperature limit of the aircraft.

.. py:property:: min_load_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.min_load_factor
    :type: float

    Get or set the minimum load factor the aircraft can bear.

.. py:property:: powerplant_mode_as_basic_turbofan
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_basic_turbofan
    :type: AdvancedFixedWingTurbofanBasicABPropulsion

    Get the interface for a Turbofan - Basic w/ AB Powerplant strategy.

.. py:property:: powerplant_mode_as_basic_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_basic_turbojet
    :type: AdvancedFixedWingTurbojetBasicABPropulsion

    Get the interface for a Turbojet - Basic w/ AB Powerplant strategy.

.. py:property:: powerplant_mode_as_electric
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_electric
    :type: AdvancedFixedWingElectricPowerplant

    Get the interface for an Electric Powerplant strategy.

.. py:property:: powerplant_mode_as_empirical_jet_engine
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_empirical_jet_engine
    :type: AdvancedFixedWingEmpiricalJetEngine

    Get the interface for an Empirical Jet Engine Powerplant strategy.

.. py:property:: powerplant_mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_external
    :type: AdvancedFixedWingExternalPropulsion

    Get the interface for an External Prop File Powerplant strategy.

.. py:property:: powerplant_mode_as_piston
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_piston
    :type: AdvancedFixedWingPistonPowerplant

    Get the interface for a Piston Powerplant strategy.

.. py:property:: powerplant_mode_as_sub_super_hypersonic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_sub_super_hypersonic
    :type: AdvancedFixedWingSubSuperHypersonicPropulsion

    Get the interface for a Sub/Super/Hypersoinc Powerplant strategy.

.. py:property:: powerplant_mode_as_turboprop
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_mode_as_turboprop
    :type: AdvancedFixedWingTurbopropPowerplant

    Get the interface for a Turboprop Powerplant strategy.

.. py:property:: powerplant_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.powerplant_strategy
    :type: AdvancedFixedWingPowerplantStrategy

    Get or set the powerplant strategy type.

.. py:property:: speedbrakes_area
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.speedbrakes_area
    :type: float

    Get or set the total surface area of the speedbrakes.

.. py:property:: use_max_temperature_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.use_max_temperature_limit
    :type: bool

    Get or set the option to limit the maximum speed of the aircraft so the specified temperature is not exceeded.

.. py:property:: wing_area
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.wing_area
    :type: float

    Get or set the total surface area of the wing.


Method detail
-------------












.. py:method:: create_all_performance_models(self, name: str, overwrite: bool, make_default: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingTool.create_all_performance_models

    Create a set of advanced performance models for the aircraft with the given name.

    :Parameters:

        **name** : :obj:`~str`

        **overwrite** : :obj:`~bool`

        **make_default** : :obj:`~bool`


    :Returns:

        :obj:`~None`































