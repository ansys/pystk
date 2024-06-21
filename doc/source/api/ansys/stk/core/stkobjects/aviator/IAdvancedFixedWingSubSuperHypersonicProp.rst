IAdvancedFixedWingSubSuperHypersonicProp
========================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp

   object
   
   Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: IAdvancedFixedWingSubSuperHypersonicProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbojet`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbofan`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_mode_as_basic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_mode_as_basic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_reference_area`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_reference_area`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_reference_area`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_turbine_compression_temp`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_turbine_burner_temp`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.can_ram_compressor_pressure_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.must_ram_compressor_pressure_ratio`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_compression_temperature`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_burner_total_temperature`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingSubSuperHypersonicProp


Property detail
---------------

.. py:property:: turbine_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode
    :type: TURBINE_MODE

    Gets or sets the turbine operating mode.

.. py:property:: turbine_mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbojet
    :type: IAdvancedFixedWingTurbojetBasicABProp

    Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.

.. py:property:: turbine_mode_as_turbofan
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbofan
    :type: IAdvancedFixedWingTurbofanBasicABProp

    Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.

.. py:property:: ramjet_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_mode
    :type: RAMJET_MODE

    Gets or sets the ramjet operating mode.

.. py:property:: ramjet_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_mode_as_basic
    :type: IAdvancedFixedWingRamjetBasic

    Get the interface for a Ramjet - Basic.

.. py:property:: scramjet_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_mode
    :type: SCRAMJET_MODE

    Gets or sets the scramjet operating mode.

.. py:property:: scramjet_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_mode_as_basic
    :type: IAdvancedFixedWingScramjetBasic

    Get the interface for a Scramjet - Basic.

.. py:property:: turbine_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_reference_area
    :type: float

    Get the reference area used for the turbine operating mode.

.. py:property:: ramjet_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_reference_area
    :type: float

    Get the reference area used for the ramjet operating mode.

.. py:property:: scramjet_reference_area
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_reference_area
    :type: float

    Get the reference area used for the scramjet operating mode.

.. py:property:: max_turbine_compression_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_turbine_compression_temp
    :type: float

    Gets or sets the maximum temperature at the compressor stage in the turbine operating mode.

.. py:property:: max_turbine_burner_temp
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_turbine_burner_temp
    :type: float

    Gets or sets the maximum temperature at the combustion stage in the turbine operating mode.

.. py:property:: can_ram_compressor_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.can_ram_compressor_pressure_ratio
    :type: float

    Can Ram compressor pressure ratio.

.. py:property:: must_ram_compressor_pressure_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.must_ram_compressor_pressure_ratio
    :type: float

    Must Ram compressor pressure ratio.

.. py:property:: max_ram_scram_compression_temperature
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_compression_temperature
    :type: float

    Gets or sets the maximum temperature at the compressor stage in the Ramjet or Scramjet operating mode.

.. py:property:: max_ram_scram_burner_total_temperature
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.max_ram_scram_burner_total_temperature
    :type: float

    Gets or sets the maximum temperature at the combustion stage in the Ramjet or Scramjet operating mode.


