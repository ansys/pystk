AtmosphericAbsorptionModelGraphics3DACAP
========================================

.. py:class:: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining an atmospheric absorption model.

.. py:currentmodule:: AtmosphericAbsorptionModelGraphics3DACAP

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.sunspot_number`
              - Do not use this property, as it is deprecated. The Sunspot Number Solar Activity Configuration should be used instead.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.multipath_power_tolerance`
              - Get or set the multipath power tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.multipath_delay_tolerance`
              - Get or set the multipath delay tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.compute_alternate_frequencies`
              - Get or set the indicator to compute alternate frequencies.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.coefficient_data_type`
              - Get or set the coefficient data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.use_day_of_month_average`
              - Get or set the indicator to use day of month average.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.solar_activity_configuration_type`
              - Get or set the solar activity configuration enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.solar_activity_configuration`
              - Get or set the solar activity configuration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AtmosphericAbsorptionModelGraphics3DACAP


Property detail
---------------

.. py:property:: sunspot_number
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.sunspot_number
    :type: int

    Do not use this property, as it is deprecated. The Sunspot Number Solar Activity Configuration should be used instead.

.. py:property:: multipath_power_tolerance
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.multipath_power_tolerance
    :type: float

    Get or set the multipath power tolerance.

.. py:property:: multipath_delay_tolerance
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.multipath_delay_tolerance
    :type: float

    Get or set the multipath delay tolerance.

.. py:property:: compute_alternate_frequencies
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.compute_alternate_frequencies
    :type: bool

    Get or set the indicator to compute alternate frequencies.

.. py:property:: coefficient_data_type
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.coefficient_data_type
    :type: Graphics3DACAPCoefficientDataType

    Get or set the coefficient data type.

.. py:property:: use_day_of_month_average
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.use_day_of_month_average
    :type: bool

    Get or set the indicator to use day of month average.

.. py:property:: solar_activity_configuration_type
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.solar_activity_configuration_type
    :type: Graphics3DACAPSolarActivityConfigurationType

    Get or set the solar activity configuration enumeration.

.. py:property:: solar_activity_configuration
    :canonical: ansys.stk.core.stkobjects.AtmosphericAbsorptionModelGraphics3DACAP.solar_activity_configuration
    :type: ISolarActivityConfiguration

    Get or set the solar activity configuration.


