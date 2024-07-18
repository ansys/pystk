VehicleAttitudeMaximumSlewRate
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate

   Bases: 

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
              - Gets or sets the maximum overall magnitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_x_enabled`
              - Whether to constrain the slew rate along the direction of X axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_y_enabled`
              - Whether to constrain the slew rate along the direction of Y axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_z_enabled`
              - Whether to constrain the slew rate along the direction of Z axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_x`
              - Constraint the slew rate along the direction of X axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_y`
              - Constraint the slew rate along the direction of Y axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_z`
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

    Gets or sets the maximum overall magnitude.

.. py:property:: per_axis_x_enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_x_enabled
    :type: bool

    Whether to constrain the slew rate along the direction of X axis.

.. py:property:: per_axis_y_enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_y_enabled
    :type: bool

    Whether to constrain the slew rate along the direction of Y axis.

.. py:property:: per_axis_z_enabled
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_z_enabled
    :type: bool

    Whether to constrain the slew rate along the direction of Z axis.

.. py:property:: per_axis_x
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_x
    :type: float

    Constraint the slew rate along the direction of X axis.

.. py:property:: per_axis_y
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_y
    :type: float

    Constraint the slew rate along the direction of Y axis.

.. py:property:: per_axis_z
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeMaximumSlewRate.per_axis_z
    :type: float

    Constraint the slew rate along the direction of Z axis.


