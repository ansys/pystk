PowerSolarArray
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.PowerSolarArray

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Power - Solar Array.

.. py:currentmodule:: PowerSolarArray

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.area`
              - Get or set the solar array panel area. Uses Area Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.concentration`
              - Get or set the solar array concentrator factor. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.cell_efficiency_percent`
              - Get or set the cell efficiency in producing output power from incident sunlight. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.array_efficiency_percent`
              - Get or set the array efficiency in producing output power from a collection of cells. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.percent_degradation_per_year`
              - Get or set the percent degradation per year; degradation factor is (1-x%/yr)^(timeSinceRefEpoch). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.reference_epoch`
              - Get or set the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.inclination_to_sun_line`
              - Get or set the angle between the panel normal vector to the apparent sun line. Uses AngleUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c0`
              - Get or set the ThermalModel.C0 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c1`
              - Get or set the ThermalModel.C1 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c2`
              - Get or set the ThermalModel.C2 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c3`
              - Get or set the ThermalModel.C3 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c4`
              - Get or set the ThermalModel.C4 coefficient. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.approximation_formula`
              - Get the thermal factor as function of distance (in AU) to Sun.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PowerSolarArray.control_parameters_available`
              - Return whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import PowerSolarArray


Property detail
---------------

.. py:property:: area
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.area
    :type: float

    Get or set the solar array panel area. Uses Area Dimension.

.. py:property:: concentration
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.concentration
    :type: float

    Get or set the solar array concentrator factor. Dimensionless.

.. py:property:: cell_efficiency_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.cell_efficiency_percent
    :type: float

    Get or set the cell efficiency in producing output power from incident sunlight. Dimensionless.

.. py:property:: array_efficiency_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.array_efficiency_percent
    :type: float

    Get or set the array efficiency in producing output power from a collection of cells. Dimensionless.

.. py:property:: percent_degradation_per_year
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.percent_degradation_per_year
    :type: float

    Get or set the percent degradation per year; degradation factor is (1-x%/yr)^(timeSinceRefEpoch). Dimensionless.

.. py:property:: reference_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.reference_epoch
    :type: typing.Any

    Get or set the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.

.. py:property:: inclination_to_sun_line
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.inclination_to_sun_line
    :type: typing.Any

    Get or set the angle between the panel normal vector to the apparent sun line. Uses AngleUnit Dimension.

.. py:property:: c0
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c0
    :type: float

    Get or set the ThermalModel.C0 coefficient. Dimensionless.

.. py:property:: c1
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c1
    :type: float

    Get or set the ThermalModel.C1 coefficient. Dimensionless.

.. py:property:: c2
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c2
    :type: float

    Get or set the ThermalModel.C2 coefficient. Dimensionless.

.. py:property:: c3
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c3
    :type: float

    Get or set the ThermalModel.C3 coefficient. Dimensionless.

.. py:property:: c4
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.c4
    :type: float

    Get or set the ThermalModel.C4 coefficient. Dimensionless.

.. py:property:: approximation_formula
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.approximation_formula
    :type: str

    Get the thermal factor as function of distance (in AU) to Sun.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.


Method detail
-------------


























.. py:method:: enable_control_parameter(self, param: ControlPowerSolarArray) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlPowerSolarArray`


    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlPowerSolarArray) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlPowerSolarArray`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlPowerSolarArray) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.PowerSolarArray.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlPowerSolarArray`


    :Returns:

        :obj:`~bool`


