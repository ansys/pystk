IMissileRamjetProp
==================

.. py:class:: IMissileRamjetProp

   object
   
   Interface used to access the Ramjet propulsion options for a missile.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~design_mach`
            * - :py:meth:`~design_altitude`
            * - :py:meth:`~design_thrust`
            * - :py:meth:`~engine_temp`
            * - :py:meth:`~fuel_heating_value`
            * - :py:meth:`~inlet_pressure_ratio`
            * - :py:meth:`~burner_pressure_ratio`
            * - :py:meth:`~nozzle_pressure_ratio`
            * - :py:meth:`~p_0over_p9`
            * - :py:meth:`~burner_efficiency`
            * - :py:meth:`~no_thrust_when_no_fuel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileRamjetProp


Property detail
---------------

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.design_mach
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.design_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.design_thrust
    :type: float

    Gets or sets the thrust design point of the engine.

.. py:property:: engine_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.engine_temp
    :type: float

    Gets or sets the maximum temperature that the engine material can support.

.. py:property:: fuel_heating_value
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.fuel_heating_value
    :type: float

    Gets or sets the heating value of the fuel.

.. py:property:: inlet_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.inlet_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the inlet exit to the entrance.

.. py:property:: burner_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.burner_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the burner exit to the entrance.

.. py:property:: nozzle_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.nozzle_pressure_ratio
    :type: float

    Gets or sets the pressure ratio from the nozzle exit to the entrance.

.. py:property:: p_0over_p9
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.p_0over_p9
    :type: float

    Gets or sets the pressure ratio from ambient conditions to the engine exit.

.. py:property:: burner_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.burner_efficiency
    :type: float

    Gets or sets the efficiency of the burner.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileRamjetProp.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


