VehicleAttitudeMaximumSlewRate
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate

   Define the maximum slew rate by entering a maximum overall magnitude. You can constrain the slew rate in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

.. py:currentmodule:: VehicleAttitudeMaximumSlewRate

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.magnitude`
              - Get or set the maximum overall magnitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_x_axis_enabled`
              - Whether to constrain the slew rate along the direction of X axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_y_axis_enabled`
              - Whether to constrain the slew rate along the direction of Y axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_z_axis_enabled`
              - Whether to constrain the slew rate along the direction of Z axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_x_axis`
              - Constraint the slew rate along the direction of X axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_y_axis`
              - Constraint the slew rate along the direction of Y axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_z_axis`
              - Constraint the slew rate along the direction of Z axis.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitudeMaximumSlewRate


Property detail
---------------

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.magnitude
    :type: float

    Get or set the maximum overall magnitude.

.. py:property:: slew_rate_along_x_axis_enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_x_axis_enabled
    :type: bool

    Whether to constrain the slew rate along the direction of X axis.

.. py:property:: slew_rate_along_y_axis_enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_y_axis_enabled
    :type: bool

    Whether to constrain the slew rate along the direction of Y axis.

.. py:property:: slew_rate_along_z_axis_enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_z_axis_enabled
    :type: bool

    Whether to constrain the slew rate along the direction of Z axis.

.. py:property:: slew_rate_along_x_axis
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_x_axis
    :type: float

    Constraint the slew rate along the direction of X axis.

.. py:property:: slew_rate_along_y_axis
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_y_axis
    :type: float

    Constraint the slew rate along the direction of Y axis.

.. py:property:: slew_rate_along_z_axis
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.slew_rate_along_z_axis
    :type: float

    Constraint the slew rate along the direction of Z axis.


