IMissileTurbojetProp
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp

   object
   
   Interface used to access the Turbojet propulsion options for a missile.

.. py:currentmodule:: IMissileTurbojetProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.design_mach`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.design_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.design_thrust`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.turbine_temp`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.compressor_pressure_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.fuel_heating_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.inlet_subsonic_pressure_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.burner_pressure_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.nozzle_pressure_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.p_0over_p9`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.compressor_efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.turbine_efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.burner_efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.mechanical_efficiency`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.no_thrust_when_no_fuel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileTurbojetProp


Property detail
---------------

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.design_mach
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.design_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.design_thrust
    :type: float

    Gets or sets the thrust design point of the engine.

.. py:property:: turbine_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.turbine_temp
    :type: float

    Gets or sets the maximum temperature that the turbine material can support.

.. py:property:: compressor_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.compressor_pressure_ratio
    :type: float

    Gets or sets the maximum compressor pressure ratio.

.. py:property:: fuel_heating_value
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.fuel_heating_value
    :type: float

    Gets or sets the heating value of the fuel.

.. py:property:: inlet_subsonic_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.inlet_subsonic_pressure_ratio
    :type: float

    Gets or sets the subsonic pressure ratio from the inlet exit to the entrance.

.. py:property:: burner_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.burner_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the burner exit to the entrance.

.. py:property:: nozzle_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.nozzle_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the nozzle exit to the entrance.

.. py:property:: p_0over_p9
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.p_0over_p9
    :type: float

    Gets or sets the pressure ratio from ambient conditions to the engine exit.

.. py:property:: compressor_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.compressor_efficiency
    :type: float

    Gets or sets the efficiency of the compressor.

.. py:property:: turbine_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.turbine_efficiency
    :type: float

    Gets or sets the efficiency of the turbine.

.. py:property:: burner_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.burner_efficiency
    :type: float

    Gets or sets the efficiency of the burner.

.. py:property:: mechanical_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.mechanical_efficiency
    :type: float

    Gets or sets the mechanical efficiency of the engine.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileTurbojetProp.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


