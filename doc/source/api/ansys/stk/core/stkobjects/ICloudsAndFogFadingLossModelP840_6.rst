ICloudsAndFogFadingLossModelP840_6
==================================

.. py:class:: ICloudsAndFogFadingLossModelP840_6

   object
   
   Provide access to the properties and methods for clouds and fog loss model ITU-R P.840-6.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~cloud_ceiling`
            * - :py:meth:`~cloud_layer_thickness`
            * - :py:meth:`~cloud_temperature`
            * - :py:meth:`~cloud_liquid_water_density`
            * - :py:meth:`~liquid_water_density_choice`
            * - :py:meth:`~liquid_water_percent_annual_exceeded`
            * - :py:meth:`~liquid_water_percent_monthly_exceeded`
            * - :py:meth:`~average_data_month`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICloudsAndFogFadingLossModelP840_6


Property detail
---------------

.. py:property:: cloud_ceiling
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.cloud_ceiling
    :type: float

    Gets or sets the cloud ceiling.

.. py:property:: cloud_layer_thickness
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.cloud_layer_thickness
    :type: float

    Gets or sets the cloud layer thickness.

.. py:property:: cloud_temperature
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.cloud_temperature
    :type: float

    Gets or sets the cloud temperature.

.. py:property:: cloud_liquid_water_density
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.cloud_liquid_water_density
    :type: float

    Gets or sets the cloud liquid water density.

.. py:property:: liquid_water_density_choice
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.liquid_water_density_choice
    :type: CLOUDS_AND_FOG_LIQUID_WATER_CHOICES

    Gets or sets the cloud liquid water density Choice.

.. py:property:: liquid_water_percent_annual_exceeded
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.liquid_water_percent_annual_exceeded
    :type: float

    Gets or sets the Liquid water % Annual Exceeded.

.. py:property:: liquid_water_percent_monthly_exceeded
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.liquid_water_percent_monthly_exceeded
    :type: float

    Gets or sets the Liquid water % Monthly Exceeded.

.. py:property:: average_data_month
    :canonical: ansys.stk.core.stkobjects.ICloudsAndFogFadingLossModelP840_6.average_data_month
    :type: int

    Gets or sets the month, (1 - 12) of the year, used to get average liquid water data.


