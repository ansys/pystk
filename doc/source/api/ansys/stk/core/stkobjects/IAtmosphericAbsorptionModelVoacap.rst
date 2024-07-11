IAtmosphericAbsorptionModelVoacap
=================================

.. py:class:: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap

   object
   
   Provide access to the properties and methods of the VOACAP atmospheric absorption model.

.. py:currentmodule:: IAtmosphericAbsorptionModelVoacap

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.sunspot_number`
              - This property is deprecated. The Sunspot Number Solar Activity Configuration should be used instead.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.multipath_power_tolerance`
              - Gets or sets the multipath power tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.multipath_delay_tolerance`
              - Gets or sets the multipath delay tolerance.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.compute_alternate_frequencies`
              - Gets or sets the indicator to compute alternate frequencies.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.coefficient_data_type`
              - Gets or sets the coefficient data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.use_day_of_month_average`
              - Gets or sets the indicator to use day of month average.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.solar_activity_configuration_type`
              - Gets or sets the solar activity configuration enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.solar_activity_configuration`
              - Gets or sets the solar activity configuration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAtmosphericAbsorptionModelVoacap


Property detail
---------------

.. py:property:: sunspot_number
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.sunspot_number
    :type: int

    This property is deprecated. The Sunspot Number Solar Activity Configuration should be used instead.

.. py:property:: multipath_power_tolerance
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.multipath_power_tolerance
    :type: float

    Gets or sets the multipath power tolerance.

.. py:property:: multipath_delay_tolerance
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.multipath_delay_tolerance
    :type: float

    Gets or sets the multipath delay tolerance.

.. py:property:: compute_alternate_frequencies
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.compute_alternate_frequencies
    :type: bool

    Gets or sets the indicator to compute alternate frequencies.

.. py:property:: coefficient_data_type
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.coefficient_data_type
    :type: VOACAP_COEFFICIENT_DATA_TYPE

    Gets or sets the coefficient data type.

.. py:property:: use_day_of_month_average
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.use_day_of_month_average
    :type: bool

    Gets or sets the indicator to use day of month average.

.. py:property:: solar_activity_configuration_type
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.solar_activity_configuration_type
    :type: VOACAP_SOLAR_ACTIVITY_CONFIGURATION_TYPE

    Gets or sets the solar activity configuration enumeration.

.. py:property:: solar_activity_configuration
    :canonical: ansys.stk.core.stkobjects.IAtmosphericAbsorptionModelVoacap.solar_activity_configuration
    :type: ISolarActivityConfiguration

    Gets or sets the solar activity configuration.


