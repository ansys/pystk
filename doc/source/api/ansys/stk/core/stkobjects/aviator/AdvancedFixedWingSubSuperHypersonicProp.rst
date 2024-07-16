AdvancedFixedWingSubSuperHypersonicProp
=======================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp

   Bases: 

   Class defining a Sub/Super/Hypersonic powerplant in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingSubSuperHypersonicProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_mode`
              - Gets or sets the turbine operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbojet`
              - Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbofan`
              - Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.ramjet_mode`
              - Gets or sets the ramjet operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.ramjet_mode_as_basic`
              - Get the interface for a Ramjet - Basic.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.scramjet_mode`
              - Gets or sets the scramjet operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.scramjet_mode_as_basic`
              - Get the interface for a Scramjet - Basic.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_reference_area`
              - Get the reference area used for the turbine operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.ramjet_reference_area`
              - Get the reference area used for the ramjet operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.scramjet_reference_area`
              - Get the reference area used for the scramjet operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_turbine_compression_temp`
              - Gets or sets the maximum temperature at the compressor stage in the turbine operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_turbine_burner_temp`
              - Gets or sets the maximum temperature at the combustion stage in the turbine operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.can_ram_compressor_pressure_ratio`
              - Can Ram compressor pressure ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.must_ram_compressor_pressure_ratio`
              - Must Ram compressor pressure ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_compression_temperature`
              - Gets or sets the maximum temperature at the compressor stage in the Ramjet or Scramjet operating mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_burner_total_temperature`
              - Gets or sets the maximum temperature at the combustion stage in the Ramjet or Scramjet operating mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingSubSuperHypersonicProp


Property detail
---------------

.. py:property:: turbine_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_mode
    :type: TURBINE_MODE

    Gets or sets the turbine operating mode.

.. py:property:: turbine_mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbojet
    :type: IAdvancedFixedWingTurbojetBasicABProp

    Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.

.. py:property:: turbine_mode_as_turbofan
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbofan
    :type: IAdvancedFixedWingTurbofanBasicABProp

    Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.

.. py:property:: ramjet_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.ramjet_mode
    :type: RAMJET_MODE

    Gets or sets the ramjet operating mode.

.. py:property:: ramjet_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.ramjet_mode_as_basic
    :type: IAdvancedFixedWingRamjetBasic

    Get the interface for a Ramjet - Basic.

.. py:property:: scramjet_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.scramjet_mode
    :type: SCRAMJET_MODE

    Gets or sets the scramjet operating mode.

.. py:property:: scramjet_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.scramjet_mode_as_basic
    :type: IAdvancedFixedWingScramjetBasic

    Get the interface for a Scramjet - Basic.

.. py:property:: turbine_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.turbine_reference_area
    :type: float

    Get the reference area used for the turbine operating mode.

.. py:property:: ramjet_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.ramjet_reference_area
    :type: float

    Get the reference area used for the ramjet operating mode.

.. py:property:: scramjet_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.scramjet_reference_area
    :type: float

    Get the reference area used for the scramjet operating mode.

.. py:property:: max_turbine_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_turbine_compression_temp
    :type: float

    Gets or sets the maximum temperature at the compressor stage in the turbine operating mode.

.. py:property:: max_turbine_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_turbine_burner_temp
    :type: float

    Gets or sets the maximum temperature at the combustion stage in the turbine operating mode.

.. py:property:: can_ram_compressor_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.can_ram_compressor_pressure_ratio
    :type: float

    Can Ram compressor pressure ratio.

.. py:property:: must_ram_compressor_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.must_ram_compressor_pressure_ratio
    :type: float

    Must Ram compressor pressure ratio.

.. py:property:: max_ram_scram_compression_temperature
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_compression_temperature
    :type: float

    Gets or sets the maximum temperature at the compressor stage in the Ramjet or Scramjet operating mode.

.. py:property:: max_ram_scram_burner_total_temperature
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_burner_total_temperature
    :type: float

    Gets or sets the maximum temperature at the combustion stage in the Ramjet or Scramjet operating mode.


