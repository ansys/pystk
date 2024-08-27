VehicleStepSizeControl
======================

.. py:class:: ansys.stk.core.stkobjects.VehicleStepSizeControl

   Class defining step size control for the HPOP integrator.

.. py:currentmodule:: VehicleStepSizeControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStepSizeControl.method`
              - Fixed step or relative error.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStepSizeControl.error_tolerance`
              - If the method is relative error. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStepSizeControl.min_step_size`
              - If the method is relative error. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStepSizeControl.max_step_size`
              - If the method is relative error. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleStepSizeControl


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.VehicleStepSizeControl.method
    :type: VEHICLE_METHOD

    Fixed step or relative error.

.. py:property:: error_tolerance
    :canonical: ansys.stk.core.stkobjects.VehicleStepSizeControl.error_tolerance
    :type: float

    If the method is relative error. Dimensionless.

.. py:property:: min_step_size
    :canonical: ansys.stk.core.stkobjects.VehicleStepSizeControl.min_step_size
    :type: float

    If the method is relative error. Uses Time Dimension.

.. py:property:: max_step_size
    :canonical: ansys.stk.core.stkobjects.VehicleStepSizeControl.max_step_size
    :type: float

    If the method is relative error. Uses Time Dimension.


