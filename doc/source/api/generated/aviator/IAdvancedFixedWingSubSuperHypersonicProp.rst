IAdvancedFixedWingSubSuperHypersonicProp
========================================

.. py:class:: IAdvancedFixedWingSubSuperHypersonicProp

   object
   
   Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~turbine_mode`
            * - :py:meth:`~turbine_mode_as_turbojet`
            * - :py:meth:`~turbine_mode_as_turbofan`
            * - :py:meth:`~ramjet_mode`
            * - :py:meth:`~ramjet_mode_as_basic`
            * - :py:meth:`~scramjet_mode`
            * - :py:meth:`~scramjet_mode_as_basic`
            * - :py:meth:`~turbine_reference_area`
            * - :py:meth:`~ramjet_reference_area`
            * - :py:meth:`~scramjet_reference_area`
            * - :py:meth:`~max_turbine_compression_temp`
            * - :py:meth:`~max_turbine_burner_temp`
            * - :py:meth:`~can_ram_compressor_pressure_ratio`
            * - :py:meth:`~must_ram_compressor_pressure_ratio`
            * - :py:meth:`~max_ram_scram_compression_temperature`
            * - :py:meth:`~max_ram_scram_burner_total_temperature`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingSubSuperHypersonicProp


Property detail
---------------

.. py:property:: turbine_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode
    :type: "TURBINE_MODE"

    Gets or sets the turbine operating mode.

.. py:property:: turbine_mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbojet
    :type: "IAgAvtrAdvFixedWingTurbojetBasicABProp"

    Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.

.. py:property:: turbine_mode_as_turbofan
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.turbine_mode_as_turbofan
    :type: "IAgAvtrAdvFixedWingTurbofanBasicABProp"

    Gets or sets the interface for a Turbojet Basic w/ AB tubrine mode.

.. py:property:: ramjet_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_mode
    :type: "RAMJET_MODE"

    Gets or sets the ramjet operating mode.

.. py:property:: ramjet_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.ramjet_mode_as_basic
    :type: "IAgAvtrAdvFixedWingRamjetBasic"

    Get the interface for a Ramjet - Basic.

.. py:property:: scramjet_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_mode
    :type: "SCRAMJET_MODE"

    Gets or sets the scramjet operating mode.

.. py:property:: scramjet_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicProp.scramjet_mode_as_basic
    :type: "IAgAvtrAdvFixedWingScramjetBasic"

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


