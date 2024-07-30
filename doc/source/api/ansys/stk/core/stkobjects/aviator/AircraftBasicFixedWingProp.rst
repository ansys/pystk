AircraftBasicFixedWingProp
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp

   Bases: 

   Class defining the basic fixed wing propulsion options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftBasicFixedWingProp

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.set_density_scaling`
              - Set the option to use density scaling and set the density ratio exponent.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propulsion_mode`
              - Gets or sets the option of whether to specify net thrust or net power.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propeller_count`
              - Gets or sets the number of propellers.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propeller_diameter`
              - Gets or sets the propeller diameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propeller_rpm`
              - Gets or sets the propeller RPM.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.min_power_thrust`
              - Gets or sets the minimum power/thrust depending on the propulsion mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.min_fuel_flow`
              - Gets or sets the fuel flow for the minimum thrust/power setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.max_power_thrust`
              - Gets or sets the maximum power/thrust depending on the propulsion mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.max_fuel_flow`
              - Gets or sets the fuel flow for the maximum thrust/power setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.max_thrust_accel`
              - Gets or sets the rate at which the aircraft speeds up at max throttle.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.min_thrust_decel`
              - Gets or sets the rate at which the aircraft slows down at minimum throttle setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.use_density_scaling`
              - Opt whether to scale the accel/decel performance by the density ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.density_ratio_exponent`
              - Get the relative impace of atmospheric density on the aircraft's performance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicFixedWingProp


Property detail
---------------

.. py:property:: propulsion_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propulsion_mode
    :type: BASIC_FIXED_WING_PROP_MODE

    Gets or sets the option of whether to specify net thrust or net power.

.. py:property:: propeller_count
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propeller_count
    :type: int

    Gets or sets the number of propellers.

.. py:property:: propeller_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propeller_diameter
    :type: float

    Gets or sets the propeller diameter.

.. py:property:: propeller_rpm
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.propeller_rpm
    :type: float

    Gets or sets the propeller RPM.

.. py:property:: min_power_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.min_power_thrust
    :type: float

    Gets or sets the minimum power/thrust depending on the propulsion mode.

.. py:property:: min_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.min_fuel_flow
    :type: float

    Gets or sets the fuel flow for the minimum thrust/power setting.

.. py:property:: max_power_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.max_power_thrust
    :type: float

    Gets or sets the maximum power/thrust depending on the propulsion mode.

.. py:property:: max_fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.max_fuel_flow
    :type: float

    Gets or sets the fuel flow for the maximum thrust/power setting.

.. py:property:: max_thrust_accel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.max_thrust_accel
    :type: float

    Gets or sets the rate at which the aircraft speeds up at max throttle.

.. py:property:: min_thrust_decel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.min_thrust_decel
    :type: float

    Gets or sets the rate at which the aircraft slows down at minimum throttle setting.

.. py:property:: use_density_scaling
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.use_density_scaling
    :type: bool

    Opt whether to scale the accel/decel performance by the density ratio.

.. py:property:: density_ratio_exponent
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.density_ratio_exponent
    :type: float

    Get the relative impace of atmospheric density on the aircraft's performance.


Method detail
-------------























.. py:method:: set_density_scaling(self, useScaling: bool, exponent: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicFixedWingProp.set_density_scaling

    Set the option to use density scaling and set the density ratio exponent.

    :Parameters:

    **useScaling** : :obj:`~bool`
    **exponent** : :obj:`~float`

    :Returns:

        :obj:`~None`

