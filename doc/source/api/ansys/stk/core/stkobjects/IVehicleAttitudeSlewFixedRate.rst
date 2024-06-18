IVehicleAttitudeSlewFixedRate
=============================

.. py:class:: IVehicleAttitudeSlewFixedRate

   IVehicleAttitudeSlewBase
   
   Fixed Rate slew.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~maximum_slew_time`
            * - :py:meth:`~slew_timing_between_targets`
            * - :py:meth:`~maximum_slew_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeSlewFixedRate


Property detail
---------------

.. py:property:: maximum_slew_time
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedRate.maximum_slew_time
    :type: float

    Limits the maximum slew rate.

.. py:property:: slew_timing_between_targets
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedRate.slew_timing_between_targets
    :type: "VEHICLE_SLEW_TIMING_BETWEEN_TARGETS"

    Choose an event within the window of opportunity to trigger each slew, or select Optimal to change attitude whenever the slew can be performed most efficiently.

.. py:property:: maximum_slew_rate
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedRate.maximum_slew_rate
    :type: "IAgVeAttMaximumSlewRate"

    Configure how to constrain the slew rate.


