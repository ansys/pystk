CloudsAndFogFadingLossModelP840Version6
=======================================

.. py:class:: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a clouds and fog Loss ITU-R P.840-6 model.

.. py:currentmodule:: CloudsAndFogFadingLossModelP840Version6

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_ceiling`
              - Gets or sets the cloud ceiling.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_layer_thickness`
              - Gets or sets the cloud layer thickness.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_temperature`
              - Gets or sets the cloud temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_liquid_water_density`
              - Gets or sets the cloud liquid water density.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.liquid_water_density_choice`
              - Gets or sets the cloud liquid water density Choice.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.liquid_water_percent_annual_exceeded`
              - Gets or sets the Liquid water % Annual Exceeded.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.liquid_water_percent_monthly_exceeded`
              - Gets or sets the Liquid water % Monthly Exceeded.
            * - :py:attr:`~ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.average_data_month`
              - Gets or sets the month, (1 - 12) of the year, used to get average liquid water data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CloudsAndFogFadingLossModelP840Version6


Property detail
---------------

.. py:property:: cloud_ceiling
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_ceiling
    :type: float

    Gets or sets the cloud ceiling.

.. py:property:: cloud_layer_thickness
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_layer_thickness
    :type: float

    Gets or sets the cloud layer thickness.

.. py:property:: cloud_temperature
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_temperature
    :type: float

    Gets or sets the cloud temperature.

.. py:property:: cloud_liquid_water_density
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.cloud_liquid_water_density
    :type: float

    Gets or sets the cloud liquid water density.

.. py:property:: liquid_water_density_choice
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.liquid_water_density_choice
    :type: CloudsAndFogLiquidWaterChoiceType

    Gets or sets the cloud liquid water density Choice.

.. py:property:: liquid_water_percent_annual_exceeded
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.liquid_water_percent_annual_exceeded
    :type: float

    Gets or sets the Liquid water % Annual Exceeded.

.. py:property:: liquid_water_percent_monthly_exceeded
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.liquid_water_percent_monthly_exceeded
    :type: float

    Gets or sets the Liquid water % Monthly Exceeded.

.. py:property:: average_data_month
    :canonical: ansys.stk.core.stkobjects.CloudsAndFogFadingLossModelP840Version6.average_data_month
    :type: int

    Gets or sets the month, (1 - 12) of the year, used to get average liquid water data.


