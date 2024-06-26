IMissileRocketProp
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileRocketProp

   object
   
   Interface used to access the Rocket propulsion options for a missile.

.. py:currentmodule:: IMissileRocketProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.nozzle_expansion_ratio`
              - Gets or sets the exit area divided by the throat area.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.nozzle_exit_diameter`
              - Gets or sets the diameter of the nozzle exit.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.combustion_chamber_pressure`
              - Gets or sets the pressure in the combustion chamber.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.propellant_specific_heat_ratio`
              - Gets or sets the ratio of the propellant's constant-pressure specific heat to the constant volume specific heat.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.propellant_characteristic_velocity`
              - Gets or sets the propellant's characteristic velocity (Chamber Pressure * Throat Area / Mass Flow Rate of the engine).
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.use_boost_sustain_mode`
              - Opt for the engine to use a boost phase to achieve a target velocity and then transition to a sustenance phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.boost_fuel_fraction`
              - Gets or sets the amount of fuel that is consumed during the boost phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.boost_chamber_pressure`
              - Gets or sets the combustion chamber pressure during the boost phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileRocketProp.no_thrust_when_no_fuel`
              - Opt to have no thrust if the fuel is empty.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileRocketProp


Property detail
---------------

.. py:property:: nozzle_expansion_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.nozzle_expansion_ratio
    :type: float

    Gets or sets the exit area divided by the throat area.

.. py:property:: nozzle_exit_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.nozzle_exit_diameter
    :type: float

    Gets or sets the diameter of the nozzle exit.

.. py:property:: combustion_chamber_pressure
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.combustion_chamber_pressure
    :type: float

    Gets or sets the pressure in the combustion chamber.

.. py:property:: propellant_specific_heat_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.propellant_specific_heat_ratio
    :type: float

    Gets or sets the ratio of the propellant's constant-pressure specific heat to the constant volume specific heat.

.. py:property:: propellant_characteristic_velocity
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.propellant_characteristic_velocity
    :type: float

    Gets or sets the propellant's characteristic velocity (Chamber Pressure * Throat Area / Mass Flow Rate of the engine).

.. py:property:: use_boost_sustain_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.use_boost_sustain_mode
    :type: bool

    Opt for the engine to use a boost phase to achieve a target velocity and then transition to a sustenance phase.

.. py:property:: boost_fuel_fraction
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.boost_fuel_fraction
    :type: float

    Gets or sets the amount of fuel that is consumed during the boost phase.

.. py:property:: boost_chamber_pressure
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.boost_chamber_pressure
    :type: float

    Gets or sets the combustion chamber pressure during the boost phase.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRocketProp.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


