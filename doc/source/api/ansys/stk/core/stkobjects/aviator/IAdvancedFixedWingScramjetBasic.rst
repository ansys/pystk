IAdvancedFixedWingScramjetBasic
===============================

.. py:class:: IAdvancedFixedWingScramjetBasic

   object
   
   Interface used to access the options for a basic Scramjet mode.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~design_altitude`
            * - :py:meth:`~design_mach`
            * - :py:meth:`~design_thrust`
            * - :py:meth:`~max_compression_temp`
            * - :py:meth:`~max_burner_temp`
            * - :py:meth:`~fuel_type`
            * - :py:meth:`~fuel_mode_as_afprop`
            * - :py:meth:`~fuel_mode_as_cea`
            * - :py:meth:`~efficiencies_and_losses`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingScramjetBasic


Property detail
---------------

.. py:property:: design_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.design_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.design_mach
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: design_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.design_thrust
    :type: float

    Gets or sets the thrust design point of the engine.

.. py:property:: max_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.max_compression_temp
    :type: float

    Gets or sets the maximum temperature at the compressor stage.

.. py:property:: max_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.max_burner_temp
    :type: float

    Gets or sets the maximum temperature at the combustion stage.

.. py:property:: fuel_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.fuel_type
    :type: JET_FUEL_TYPE

    Gets or sets the jet engine's fuel type.

.. py:property:: fuel_mode_as_afprop
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.fuel_mode_as_afprop
    :type: IAgAvtrFuelModelKeroseneAFPROP

    Get the interface for a Kerosene - AFPROP fuel mode.

.. py:property:: fuel_mode_as_cea
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.fuel_mode_as_cea
    :type: IAgAvtrFuelModelKeroseneCEA

    Get the interface for a Kerosene - CEA fuel mode.

.. py:property:: efficiencies_and_losses
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingScramjetBasic.efficiencies_and_losses
    :type: IAgAvtrPropulsionEfficiencies

    Get the jet engine's propulsion efficiencies and losses.


