IPowerSolarArray
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray

   object
   
   Properties for the Solar Array Power power source component.

.. py:currentmodule:: IPowerSolarArray

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.area`
              - Gets or sets the solar array panel area. Uses Area Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.concentration`
              - Gets or sets the solar array concentrator factor. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.cell_efficiency_percent`
              - Gets or sets the cell efficiency in producing output power from incident sunlight. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.array_efficiency_percent`
              - Gets or sets the array efficiency in producing output power from a collection of cells. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.percent_degradation_per_year`
              - Gets or sets the percent degradation per year; degradation factor is (1-x%/yr)^(timeSinceRefEpoch). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.reference_epoch`
              - Gets or sets the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.inclination_to_sun_line`
              - Gets or sets the angle between the panel normal vector to the apparent sun line. Uses AngleUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c0`
              - Gets or sets the ThermalModel.C0 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c1`
              - Gets or sets the ThermalModel.C1 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c2`
              - Gets or sets the ThermalModel.C2 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c3`
              - Gets or sets the ThermalModel.C3 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c4`
              - Gets or sets the ThermalModel.C4 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.approximation_formula`
              - Get the thermal factor as function of distance (in AU) to Sun.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.control_parameters_available`
              - Returns whether or not the control parameters can be set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPowerSolarArray


Property detail
---------------

.. py:property:: area
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.area
    :type: float

    Gets or sets the solar array panel area. Uses Area Dimension.

.. py:property:: concentration
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.concentration
    :type: float

    Gets or sets the solar array concentrator factor. Dimensionless.

.. py:property:: cell_efficiency_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.cell_efficiency_percent
    :type: float

    Gets or sets the cell efficiency in producing output power from incident sunlight. Dimensionless.

.. py:property:: array_efficiency_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.array_efficiency_percent
    :type: float

    Gets or sets the array efficiency in producing output power from a collection of cells. Dimensionless.

.. py:property:: percent_degradation_per_year
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.percent_degradation_per_year
    :type: float

    Gets or sets the percent degradation per year; degradation factor is (1-x%/yr)^(timeSinceRefEpoch). Dimensionless.

.. py:property:: reference_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.reference_epoch
    :type: typing.Any

    Gets or sets the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.

.. py:property:: inclination_to_sun_line
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.inclination_to_sun_line
    :type: typing.Any

    Gets or sets the angle between the panel normal vector to the apparent sun line. Uses AngleUnit Dimension.

.. py:property:: c0
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c0
    :type: float

    Gets or sets the ThermalModel.C0 coefficient. Dimensionless.

.. py:property:: c1
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c1
    :type: float

    Gets or sets the ThermalModel.C1 coefficient. Dimensionless.

.. py:property:: c2
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c2
    :type: float

    Gets or sets the ThermalModel.C2 coefficient. Dimensionless.

.. py:property:: c3
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c3
    :type: float

    Gets or sets the ThermalModel.C3 coefficient. Dimensionless.

.. py:property:: c4
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.c4
    :type: float

    Gets or sets the ThermalModel.C4 coefficient. Dimensionless.

.. py:property:: approximation_formula
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.approximation_formula
    :type: str

    Get the thermal factor as function of distance (in AU) to Sun.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------


























.. py:method:: enable_control_parameter(self, param: CONTROL_POWER_SOLAR_ARRAY) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_POWER_SOLAR_ARRAY`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_POWER_SOLAR_ARRAY) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_POWER_SOLAR_ARRAY`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_POWER_SOLAR_ARRAY) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IPowerSolarArray.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_POWER_SOLAR_ARRAY`

    :Returns:

        :obj:`~bool`


