IVehicleAttitudeMaximumSlewAcceleration
=======================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration

   object
   
   Define the maximum slew acceleration by entering maximum overall magnitude. You can constrain the slew acceleration in specific directions by selecting one or more Per Axis rates and defining separate maximum rates for those axes.

.. py:currentmodule:: IVehicleAttitudeMaximumSlewAcceleration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.magnitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_x_accel_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_y_accel_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_z_accel_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_x_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_y_accel`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_z_accel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeMaximumSlewAcceleration


Property detail
---------------

.. py:property:: magnitude
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.magnitude
    :type: float

    Gets or sets the maximum overall magnitude.

.. py:property:: per_axis_x_accel_enabled
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_x_accel_enabled
    :type: bool

    Whether to constrain the slew acceleration along the direction of X axis.

.. py:property:: per_axis_y_accel_enabled
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_y_accel_enabled
    :type: bool

    Whether to constrain the slew acceleration along the direction of Y axis.

.. py:property:: per_axis_z_accel_enabled
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_z_accel_enabled
    :type: bool

    Whether to constrain the slew acceleration along the direction of Z axis.

.. py:property:: per_axis_x_accel
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_x_accel
    :type: float

    Constraint the slew acceleration along the direction of X axis.

.. py:property:: per_axis_y_accel
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_y_accel
    :type: float

    Constraint the slew acceleration along the direction of Y axis.

.. py:property:: per_axis_z_accel
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeMaximumSlewAcceleration.per_axis_z_accel
    :type: float

    Constraint the slew acceleration along the direction of Z axis.


