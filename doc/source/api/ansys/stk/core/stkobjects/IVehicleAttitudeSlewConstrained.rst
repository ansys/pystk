IVehicleAttitudeSlewConstrained
===============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained

   IVehicleAttitudeSlewBase
   
   Constrained slew mode.

.. py:currentmodule:: IVehicleAttitudeSlewConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.maximum_slew_time`
              - Limits the maximum slew rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.slew_timing_between_targets`
              - Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.maximum_slew_rate`
              - Configure how to constrain the slew rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.maximum_slew_acceleration`
              - Configure how to constrain the slew acceleration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeSlewConstrained


Property detail
---------------

.. py:property:: maximum_slew_time
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.maximum_slew_time
    :type: float

    Limits the maximum slew rate.

.. py:property:: slew_timing_between_targets
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.slew_timing_between_targets
    :type: VEHICLE_SLEW_TIMING_BETWEEN_TARGETS

    Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

.. py:property:: maximum_slew_rate
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.maximum_slew_rate
    :type: IVehicleAttitudeMaximumSlewRate

    Configure how to constrain the slew rate.

.. py:property:: maximum_slew_acceleration
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewConstrained.maximum_slew_acceleration
    :type: IVehicleAttitudeMaximumSlewAcceleration

    Configure how to constrain the slew acceleration.


